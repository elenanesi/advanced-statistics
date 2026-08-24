"""Every number and every figure in the Advanced Workbook.

Running this module writes ``build/results.json`` and the PNG files in
``figures/``. The prose in ``src/*.md`` never contains a hard-coded numeric
result: it references keys of ``results.json`` through ``{{...}}`` tokens that
``render.py`` substitutes. Text and computation therefore cannot drift apart.

Each task follows the same shape: derive the quantity in closed form where one
exists, evaluate it numerically, and cross-check the two against each other.
Those cross-checks are what the "trust" paragraph of each task reports.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from scipy import integrate, optimize, special, stats  # noqa: E402

import params as P  # noqa: E402

HERE = Path(__file__).resolve().parent
FIGDIR = HERE / "figures"
BUILDDIR = HERE / "build"

# Sober academic figure style: sans-serif, restrained colours, print-legible.
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "font.size": 9,
    "axes.titlesize": 10,
    "axes.labelsize": 9,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.linewidth": 0.5,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 200,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.02,
})

INK = "#1a1a1a"
ACCENT = "#1a5ca8"
ALT = "#c42848"
MUTED = "#8a8a8a"

#: 16 cm wide at the mandated 2 cm margins leaves a 17 cm text block.
FIGSIZE = (6.3, 3.4)


def _matvec(matrix: np.ndarray, vector: np.ndarray) -> np.ndarray:
    """Matrix-vector product guarded against a spurious BLAS warning.

    NumPy 2.0 built against Apple's Accelerate framework raises divide-by-zero,
    overflow and invalid warnings from ``matmul`` even when every input and
    every output is finite; the vectorised kernel evaluates masked lanes and
    reports their flags. The products here were checked against ``einsum`` and
    agree to 2e-16, so the warning is suppressed for this call only and the
    result is verified rather than trusted blindly.
    """
    with np.errstate(divide="ignore", over="ignore", invalid="ignore"):
        out = matrix @ vector
    if not np.isfinite(out).all():
        raise FloatingPointError("non-finite value in matrix-vector product")
    return out


def _save(fig, name: str) -> str:
    FIGDIR.mkdir(parents=True, exist_ok=True)
    path = FIGDIR / f"{name}.png"
    fig.savefig(path)
    plt.close(fig)
    return path.name


# --------------------------------------------------------------------------
# Task 1 - Bernoulli vote
# --------------------------------------------------------------------------

def task1() -> dict:
    p = P.XI2
    q = 1.0 - p
    mean, var = p, p * q

    fig, ax = plt.subplots(figsize=(4.6, 3.2))
    bars = ax.bar(["against\n(x = 0)", "for\n(x = 1)"], [100 * q, 100 * p],
                  width=0.55, color=[MUTED, ACCENT], edgecolor=INK, linewidth=0.7)
    for bar, value in zip(bars, [100 * q, 100 * p]):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 1.5, f"{value:.1f} %",
                ha="center", va="bottom", fontsize=9, fontweight="bold")
    ax.axhline(100 * mean, color=ALT, linestyle="--", linewidth=1.1,
               label=f"E[X] = {mean:.2f} (= {100 * mean:.0f} % of the unit scale)")
    ax.set_ylim(0, 100)
    ax.set_yticks(range(0, 101, 10))
    ax.set_ylabel("probability of the outcome (%)")
    ax.set_xlabel("outcome of the single vote")
    ax.legend(loc="upper left", frameon=False, fontsize=8)
    fig1 = _save(fig, "task1_bernoulli")

    return {
        "p": p, "q": q, "mean": mean, "var": var, "sd": math.sqrt(var),
        "p_pct": 100 * p, "q_pct": 100 * q,
        "fig": fig1,
    }


# --------------------------------------------------------------------------
# Task 2 - waiting time for the owl
# --------------------------------------------------------------------------

def task2() -> dict:
    w1, w2 = P.XI5_STAR, P.XI7_STAR
    a, b = P.XI6, P.XI8

    def survival(y):
        y = np.asarray(y, dtype=float)
        return w1 * np.exp(-a * y ** 2) + w2 * np.exp(-b * y ** 8)

    def density(y):
        y = np.asarray(y, dtype=float)
        return (w1 * 2 * a * y * np.exp(-a * y ** 2)
                + w2 * 8 * b * y ** 7 * np.exp(-b * y ** 8))

    # Closed forms. With Fbar(y) = w1 exp(-a y^2) + w2 exp(-b y^8) and Y >= 0,
    #   E[Y]   = int_0^inf Fbar = w1/2 sqrt(pi/a) + w2 Gamma(9/8) b^(-1/8)
    #   E[Y^2] = 2 int_0^inf y Fbar = w1/a + w2 Gamma(1/4) / (4 b^(1/4))
    mean_exact = (w1 * 0.5 * math.sqrt(math.pi / a)
                  + w2 * special.gamma(9 / 8) * b ** (-1 / 8))
    second_exact = w1 / a + w2 * special.gamma(0.25) / (4 * b ** 0.25)
    var_exact = second_exact - mean_exact ** 2

    mean_num = integrate.quad(lambda y: y * density(y), 0, np.inf)[0]
    second_num = integrate.quad(lambda y: y ** 2 * density(y), 0, np.inf)[0]
    total_mass = integrate.quad(density, 0, np.inf)[0]

    quartiles = [optimize.brentq(lambda y: 1 - survival(y) - q, 0, 20)
                 for q in (0.25, 0.5, 0.75)]

    # Both components are Weibull survival functions: exp(-a y^2) is Weibull
    # with shape 2 (a Rayleigh) and scale a^(-1/2), and exp(-b y^8) is Weibull
    # with shape 8 and scale b^(-1/8). Naming them makes the mixture readable.
    comp1_scale, comp2_scale = a ** -0.5, b ** -0.125
    comp1_mean = comp1_scale * special.gamma(1 + 1 / 2)
    comp2_mean = comp2_scale * special.gamma(1 + 1 / 8)

    p_2_4 = float(survival(2.0) - survival(4.0))
    p_within_hour = float(1 - survival(1.0))

    # Probability that the owl is first heard during minute k.
    minutes = np.arange(1, 61)
    per_minute = survival((minutes - 1) / 60) - survival(minutes / 60)

    grid = np.linspace(0, 1.4, 1400)
    fig, ax = plt.subplots(figsize=FIGSIZE)
    ax.plot(grid, density(grid), color=ACCENT, linewidth=1.6,
            label=r"$f_Y(y)$")
    ax.fill_between(grid, density(grid), color=ACCENT, alpha=0.12)
    top = ax.get_ylim()[1]
    for value, label, colour, height in zip(
            quartiles, [r"$Q_1$", "median", r"$Q_3$"],
            [MUTED, ALT, MUTED], [0.62, 0.44, 0.62]):
        ax.axvline(value, color=colour, linestyle=":", linewidth=1.1)
        ax.text(value, top * height, f" {label}\n {value * 60:.1f} min",
                fontsize=7.5, color=colour, va="top")
    ax.axvline(mean_exact, color=ALT, linestyle="--", linewidth=1.3,
               label=f"E[Y] = {mean_exact:.4f} h = {mean_exact * 60:.1f} min")
    ax.set_xlabel("waiting time y (hours)")
    ax.set_ylabel(r"probability density $f_Y(y)$  (hour$^{-1}$)")
    ax.set_xlim(0, 1.4)
    ax.set_ylim(bottom=0)
    ax.legend(loc="upper right", frameon=False, fontsize=8)
    fig_pdf = _save(fig, "task2_density")

    fig, ax = plt.subplots(figsize=FIGSIZE)
    ax.bar(minutes, 100 * per_minute, width=0.85, color=ACCENT,
           edgecolor=INK, linewidth=0.25)
    ax.axvline(mean_exact * 60, color=ALT, linestyle="--", linewidth=1.3,
               label=f"E[Y] = {mean_exact * 60:.1f} min")
    ax.axvline(quartiles[1] * 60, color=MUTED, linestyle=":", linewidth=1.2,
               label=f"median = {quartiles[1] * 60:.1f} min")
    ax.set_xlabel("minute k after opening the window")
    ax.set_ylabel("P(owl first heard during minute k)  (%)")
    ax.set_xlim(0, 61)
    ax.legend(loc="upper right", frameon=False, fontsize=8)
    fig_hist = _save(fig, "task2_minutes")

    return {
        "xi5": P.XI5, "xi7": P.XI7, "xi5_plus_xi7": P.XI5 + P.XI7,
        # The mass the delivered weights leave unassigned at y = 0.
        "xi_deficit": 1 - (P.XI5 + P.XI7),
        "xi6": a, "xi8": b,
        "w1": w1, "w2": w2,
        "w1_frac": "2/3", "w2_frac": "1/3",
        "survival_at_0_raw": P.XI5 + P.XI7,
        "survival_at_0": float(survival(0.0)),
        "mass": total_mass,
        "mean_h": mean_exact, "mean_min": mean_exact * 60,
        "mean_num_h": mean_num,
        "mean_abs_err": abs(mean_exact - mean_num),
        "second_exact": second_exact, "second_num": second_num,
        "var_h2": var_exact, "var_min2": var_exact * 3600,
        "sd_h": math.sqrt(var_exact), "sd_min": math.sqrt(var_exact) * 60,
        "q1_h": quartiles[0], "q1_min": quartiles[0] * 60,
        "median_h": quartiles[1], "median_min": quartiles[1] * 60,
        "q3_h": quartiles[2], "q3_min": quartiles[2] * 60,
        "iqr_min": (quartiles[2] - quartiles[0]) * 60,
        "p_2_4": p_2_4,
        "p_within_hour": p_within_hour,
        "p_within_hour_pct": 100 * p_within_hour,
        "peak_minute": int(minutes[int(np.argmax(per_minute))]),
        "peak_minute_pct": float(100 * per_minute.max()),
        # The two leading minutes differ in the fourth decimal of a per cent, so
        # the prose reports them as a tie rather than naming a single winner.
        "peak_minute_2": int(minutes[int(np.argsort(per_minute)[-2])]),
        "peak_minute_2_pct": float(100 * np.sort(per_minute)[-2]),
        "comp1_shape": 2, "comp2_shape": 8,
        "comp1_scale": comp1_scale, "comp2_scale": comp2_scale,
        "comp1_mean_min": comp1_mean * 60, "comp2_mean_min": comp2_mean * 60,
        "mode1_min": 60 * float(optimize.minimize_scalar(
            lambda y: -density(y), bounds=(0.01, 0.5), method="bounded").x),
        "mode2_min": 60 * float(optimize.minimize_scalar(
            lambda y: -density(y), bounds=(0.6, 1.2), method="bounded").x),
        "fig_pdf": fig_pdf, "fig_hist": fig_hist,
    }


# --------------------------------------------------------------------------
# Task 3 - dual router system
# --------------------------------------------------------------------------

def task3() -> dict:
    t = np.array(P.XI10, dtype=float)
    n = t.size
    total = t.sum()
    theta_hat = total / (2 * n)

    def loglik(theta):
        theta = np.asarray(theta, dtype=float)
        return np.sum(np.log(t)) - 2 * n * np.log(theta) - total / theta

    # Numerical maximisation as an independent check on the closed form.
    numeric = optimize.minimize_scalar(lambda th: -loglik(th),
                                       bracket=(theta_hat / 2, theta_hat * 2))

    expected_t = 2 * theta_hat
    fisher = 2 * n / theta_hat ** 2
    se = 1 / math.sqrt(fisher)

    cv_obs = t.std(ddof=1) / t.mean()
    cv_model = 1 / math.sqrt(2)

    grid = np.linspace(theta_hat * 0.35, theta_hat * 2.6, 600)
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.9))

    ax = axes[0]
    ax.plot(grid, loglik(grid), color=ACCENT, linewidth=1.5)
    ax.axvline(theta_hat, color=ALT, linestyle="--", linewidth=1.2,
               label=fr"$\hat\theta$ = {theta_hat:.2f} TB")
    ax.set_xlabel(r"$\theta$  (terabytes)")
    ax.set_ylabel(r"log-likelihood $\ell(\theta)$")
    ax.legend(loc="lower center", frameon=False, fontsize=8)

    ax = axes[1]
    tt = np.linspace(0, max(t.max(), 4 * expected_t) * 1.05, 500)
    ax.plot(tt, stats.gamma.pdf(tt, a=2, scale=theta_hat), color=ACCENT,
            linewidth=1.5, label=r"fitted $f_T(t)$, Gamma(2, $\hat\theta$)")
    ax.plot(t, np.zeros_like(t), "|", color=ALT, markersize=12,
            markeredgewidth=1.4, label="observed sample")
    ax.axvline(expected_t, color=ALT, linestyle="--", linewidth=1.2,
               label=f"E[T] = {expected_t:.1f} TB")
    ax.set_xlabel("bandwidth to failure t of the pair  (terabytes)")
    ax.set_ylabel(r"density $f_T(t)$  (TB$^{-1}$)")
    ax.set_ylim(bottom=0)
    ax.legend(loc="upper right", frameon=False, fontsize=7.5)

    fig.tight_layout()
    fig_t3 = _save(fig, "task3_mle")

    return {
        "n": n, "sample": ", ".join(f"{v:g}" for v in t),
        "total": total, "mean": t.mean(),
        "theta_hat": theta_hat,
        "theta_numeric": float(numeric.x),
        "theta_abs_err": abs(theta_hat - float(numeric.x)),
        "expected_t": expected_t,
        "se": se, "fisher": fisher,
        "ci_lo": theta_hat - 1.959964 * se, "ci_hi": theta_hat + 1.959964 * se,
        "cv_obs": cv_obs, "cv_model": cv_model,
        "sd_t": math.sqrt(2) * theta_hat,
        "fig": fig_t3,
    }


# --------------------------------------------------------------------------
# Task 4 - hypothesis test on hammer weights
# --------------------------------------------------------------------------

def task4() -> dict:
    x = np.array(P.XI14, dtype=float)
    n = x.size
    mu0, sigma0 = P.XI11, P.XI12
    xbar = x.mean()
    s = x.std(ddof=1)

    se = sigma0 / math.sqrt(n)
    z = (xbar - mu0) / se
    alpha = 0.05
    z_crit = stats.norm.ppf(1 - alpha)
    p_value = float(stats.norm.sf(z))
    crit_weight = mu0 + z_crit * se

    t_stat = (xbar - mu0) / (s / math.sqrt(n))
    t_crit = stats.t.ppf(1 - alpha, df=n - 1)
    t_p = float(stats.t.sf(t_stat, df=n - 1))

    # Power of the z-test at the observed mean, and the difference the design
    # could detect with 80 % power.
    power_at_obs = float(stats.norm.sf(z_crit - (xbar - mu0) / se))
    delta_80 = (z_crit + stats.norm.ppf(0.80)) * se
    n_for_obs = ((z_crit + stats.norm.ppf(0.80)) * sigma0 / (xbar - mu0)) ** 2

    grid = np.linspace(mu0 - 4 * se, mu0 + 4.5 * se, 700)
    fig, ax = plt.subplots(figsize=FIGSIZE)
    ax.plot(grid, stats.norm.pdf(grid, mu0, se), color=ACCENT, linewidth=1.6,
            label=r"sampling density of $\bar{X}$ under $H_0$")
    reject = grid >= crit_weight
    ax.fill_between(grid[reject], stats.norm.pdf(grid[reject], mu0, se),
                    color=ALT, alpha=0.25,
                    label=fr"rejection region, $\alpha$ = {alpha:.2f}")
    ax.axvline(crit_weight, color=ALT, linestyle="--", linewidth=1.2,
               label=f"critical value = {crit_weight:.1f} g")
    ax.axvline(xbar, color=INK, linestyle="-", linewidth=1.6,
               label=fr"observed $\bar{{x}}$ = {xbar:.1f} g")
    ax.set_xlabel("mean weight of a sample of 10 hammers  (grams)")
    ax.set_ylabel(r"density  (g$^{-1}$)")
    ax.set_ylim(bottom=0)
    ax.legend(loc="upper left", frameon=False, fontsize=7.5)
    fig_t4 = _save(fig, "task4_test")

    return {
        "n": n, "sample": ", ".join(f"{v:g}" for v in x),
        "mu0": mu0, "sigma0": sigma0,
        "xbar": xbar, "s": s, "se": se,
        "diff": xbar - mu0,
        "z": z, "z_crit": z_crit, "p_value": p_value,
        "crit_weight": crit_weight,
        "alpha": alpha, "alpha_pct": 100 * alpha,
        "t_stat": t_stat, "t_crit": t_crit, "t_p": t_p, "df": n - 1,
        "power_at_obs": power_at_obs, "power_at_obs_pct": 100 * power_at_obs,
        "beta_at_obs_pct": 100 * (1 - power_at_obs),
        "delta_80": delta_80,
        "n_for_obs": math.ceil(n_for_obs),
        "var_ratio": (s / sigma0) ** 2,
        "fig": fig_t4,
    }


# --------------------------------------------------------------------------
# Task 5 - OLS and ridge on a degree-10 polynomial
# --------------------------------------------------------------------------

def _design(x_scaled: np.ndarray, degree: int) -> np.ndarray:
    return np.vander(x_scaled, degree + 1, increasing=True)


class _Ridge:
    """Ridge regression with an unpenalised intercept, solved by SVD.

    Forming and inverting the Gram matrix X'X squares the condition number and
    is unusable here: even after rescaling x the design has condition number
    around 4e3, so X'X sits near 1e7 and small penalties lose all precision.
    Following Hastie, Tibshirani and Friedman (2009, sec. 3.4.1) the intercept
    is excluded from the penalty by centring the remaining columns, and the
    penalised solution is read straight off the singular value decomposition:

        beta(lambda) = V diag(d / (d^2 + lambda)) U' y_centred

    which is stable for every lambda >= 0.
    """

    def __init__(self, X: np.ndarray, y: np.ndarray) -> None:
        self.x_mean = X[:, 1:].mean(axis=0)
        self.y_mean = float(y.mean())
        self.Xc = X[:, 1:] - self.x_mean
        self.yc = y - self.y_mean
        self.U, self.d, self.Vt = np.linalg.svd(self.Xc, full_matrices=False)
        self.n = X.shape[0]

    def coefficients(self, lam: float) -> np.ndarray:
        """Return coefficients in the original basis, intercept first."""
        shrunk = self.d / (self.d ** 2 + lam)
        slope = _matvec(self.Vt.T, shrunk * _matvec(self.U.T, self.yc))
        intercept = self.y_mean - float(self.x_mean @ slope)
        return np.concatenate([[intercept], slope])

    def leverages(self, lam: float) -> np.ndarray:
        """Diagonal of the hat matrix, including the unpenalised intercept."""
        factors = self.d ** 2 / (self.d ** 2 + lam)
        return 1.0 / self.n + _matvec(self.U ** 2, factors)

    def loo_mse(self, lam: float) -> float:
        """Leave-one-out mean squared error via the closed-form shortcut."""
        beta = self.coefficients(lam)
        residual = self.yc - _matvec(self.Xc, beta[1:])
        return float(np.mean((residual / (1.0 - self.leverages(lam))) ** 2))


def _pairs_table(pairs: list[tuple[float, float]]) -> str:
    """Render the Task 5 coordinate pairs as Markdown rows, two pairs per row.

    The generator prints these to two decimals, so ``.2f`` reproduces them
    verbatim; building the appendix table here rather than typing it keeps it
    from drifting if the parameter set is ever regenerated.
    """
    half = (len(pairs) + 1) // 2
    left, right = pairs[:half], pairs[half:]
    rows = []
    for index in range(half):
        cells = []
        for column in (left, right):
            if index < len(column):
                x, y = column[index]
                cells += [f"${x:.0f}$", f"${y:.2f}$"]
            else:
                cells += ["", ""]
        rows.append("| " + " | ".join(cells) + " |")
    return "\n".join(rows)


def task5() -> dict:
    pairs = sorted(P.XI16)
    x = np.array([a for a, _ in pairs], dtype=float)
    y = np.array([b for _, b in pairs], dtype=float)
    n, degree = x.size, 10

    x_scale = np.abs(x).max()
    y_scale = np.abs(y).max()
    xs, ys = x / x_scale, y / y_scale

    X_raw = _design(x, degree)
    X = _design(xs, degree)
    cond_raw = float(np.linalg.cond(X_raw))
    cond_scaled = float(np.linalg.cond(X))

    fit = _Ridge(X, ys)

    beta_ols = fit.coefficients(0.0)
    resid_ols = ys - _matvec(X, beta_ols)
    rmse_ols = float(np.sqrt(np.mean(resid_ols ** 2)))

    # Independent check that the SVD route at lambda = 0 is ordinary least
    # squares: compare against NumPy's own least-squares solver.
    beta_lstsq = np.linalg.lstsq(X, ys, rcond=None)[0]
    ols_check = float(np.abs(beta_ols - beta_lstsq).max())

    # Penalty weight by leave-one-out cross-validation on the standardised
    # problem. Both axes are rescaled first: lambda trades against the squared
    # residual, so it is meaningless until x and y are dimensionless.
    lambdas = np.logspace(-12, 2, 281)
    loo = np.array([fit.loo_mse(lam) for lam in lambdas])
    coarse = int(np.argmin(loo))

    # The grid is only for the figure: at 20 points per decade its spacing is
    # 12 %, which would fix the second significant digit of lambda* by accident.
    # Refine within the bracketing grid cell so the quoted value is the actual
    # minimiser rather than the nearest grid node.
    lo = math.log10(lambdas[max(coarse - 1, 0)])
    hi = math.log10(lambdas[min(coarse + 1, lambdas.size - 1)])
    lam_star = float(10 ** optimize.minimize_scalar(
        lambda t: fit.loo_mse(10 ** t), bounds=(lo, hi), method="bounded",
        options={"xatol": 1e-6}).x)

    # The criterion is shallow near its minimum, so report the range of
    # penalties that are within 1 % of the best score rather than implying that
    # lambda* is sharply determined.
    loo_star = fit.loo_mse(lam_star)
    band = np.logspace(lo - 1, hi + 1, 2001)
    inside = band[np.array([fit.loo_mse(l) for l in band]) <= loo_star * 1.01]
    lam_band_lo, lam_band_hi = float(inside.min()), float(inside.max())

    beta_ridge = fit.coefficients(lam_star)
    resid_ridge = ys - _matvec(X, beta_ridge)
    rmse_ridge = float(np.sqrt(np.mean(resid_ridge ** 2)))

    # A deliberately heavy penalty, to show what the trade-off looks like.
    lam_heavy = 1e-2
    beta_heavy = fit.coefficients(lam_heavy)
    rmse_heavy = float(np.sqrt(np.mean((ys - _matvec(X, beta_heavy)) ** 2)))

    # Absolute-error least squares is dominated by the largest |y|. Measuring
    # the fit on the points with |x| <= 7, where |y| stays below 2e9, shows how
    # little either estimate says about that part of the curve.
    small = np.abs(x) <= 7
    def small_rel_err(beta):
        fitted = y_scale * _matvec(X[small], beta)
        return float(np.max(np.abs((fitted - y[small]) / y[small])))

    def to_original(beta_scaled: np.ndarray) -> np.ndarray:
        """Map coefficients of the scaled fit back to the original x and y."""
        return beta_scaled * y_scale / x_scale ** np.arange(degree + 1)

    alpha_ols = to_original(beta_ols)
    alpha_ridge = to_original(beta_ridge)
    alpha_heavy = to_original(beta_heavy)

    grid = np.linspace(x.min() - 0.5, x.max() + 0.5, 800)
    Xg = _design(grid / x_scale, degree)
    fit_ols = y_scale * _matvec(Xg, beta_ols)
    fit_ridge = y_scale * _matvec(Xg, beta_ridge)

    fig, axes = plt.subplots(1, 3, figsize=(7.0, 2.5))

    # (a) Full range. On this scale both estimates are indistinguishable from
    # the data, which is the entire reason panel (b) is needed.
    ax = axes[0]
    ax.plot(x, y / 1e13, "o", color=INK, markersize=3.0,
            label="sample", zorder=5)
    ax.plot(grid, fit_ols / 1e13, color=ACCENT, linewidth=1.2, label="OLS")
    ax.plot(grid, fit_ridge / 1e13, color=ALT, linewidth=1.2, linestyle="--",
            label="ridge")
    ax.set_xlabel("x")
    ax.set_ylabel(r"y  ($\times 10^{13}$)")
    ax.set_title("(a) full range", fontsize=8.5)
    ax.legend(loc="lower center", frameon=False, fontsize=7)

    # (b) The small-|x| region, where both fits are worthless.
    ax = axes[1]
    zoom = np.abs(grid) <= 7
    ax.plot(x[small], y[small] / 1e11, "o", color=INK, markersize=3.0,
            label="sample", zorder=5)
    ax.plot(grid[zoom], fit_ols[zoom] / 1e11, color=ACCENT, linewidth=1.2,
            label="OLS")
    ax.plot(grid[zoom], fit_ridge[zoom] / 1e11, color=ALT, linewidth=1.2,
            linestyle="--", label="ridge")
    ax.axhline(0, color=MUTED, linewidth=0.6)
    ax.set_xlabel("x")
    ax.set_ylabel(r"y  ($\times 10^{11}$)")
    ax.set_title(r"(b) zoom, $|x| \leq 7$", fontsize=8.5)
    ax.legend(loc="upper right", frameon=False, fontsize=7)

    # (c) How the penalty was chosen.
    ax = axes[2]
    ax.loglog(lambdas, loo, color=ACCENT, linewidth=1.3)
    ax.axvline(lam_star, color=ALT, linestyle="--", linewidth=1.2,
               label=fr"$\lambda^*$ = {lam_star:.1e}")
    ax.set_xlabel(r"penalty $\lambda$")
    ax.set_ylabel("leave-one-out MSE")
    ax.set_title("(c) penalty choice", fontsize=8.5)
    ax.legend(loc="upper left", frameon=False, fontsize=7)

    fig.tight_layout()
    fig_t5 = _save(fig, "task5_ridge")

    def fmt(vec: np.ndarray) -> str:
        return ", ".join(f"{v:.4g}" for v in vec)

    return {
        "n": n, "degree": degree, "n_params": degree + 1,
        "x_min": x.min(), "x_max": x.max(),
        "y_min": y.min(), "y_max": y.max(),
        "x_scale": x_scale, "y_scale": y_scale,
        "cond_raw": cond_raw, "cond_scaled": cond_scaled,
        "cond_ratio": cond_raw / cond_scaled,
        "lam_star": lam_star, "lam_heavy": lam_heavy,
        "lam_band_lo": lam_band_lo, "lam_band_hi": lam_band_hi,
        "pairs_rows": _pairs_table(pairs),
        "rmse_ols": rmse_ols * y_scale, "rmse_ridge": rmse_ridge * y_scale,
        "rmse_heavy": rmse_heavy * y_scale,
        "rmse_ols_rel": rmse_ols, "rmse_ridge_rel": rmse_ridge,
        "rmse_heavy_rel": rmse_heavy,
        "norm_ols": float(np.linalg.norm(beta_ols[1:])),
        "norm_ridge": float(np.linalg.norm(beta_ridge[1:])),
        "norm_heavy": float(np.linalg.norm(beta_heavy[1:])),
        "norm_shrink_pct": 100 * (1 - float(np.linalg.norm(beta_ridge[1:]))
                                  / float(np.linalg.norm(beta_ols[1:]))),
        "alpha_ols": fmt(alpha_ols), "alpha_ridge": fmt(alpha_ridge),
        "alpha_heavy": fmt(alpha_heavy),
        "a0_ols": alpha_ols[0], "a0_ridge": alpha_ridge[0],
        "a10_ols": alpha_ols[10], "a10_ridge": alpha_ridge[10],
        "y_at_zero": float(y[x == 0][0]) if np.any(x == 0) else float("nan"),
        "n_small": int(small.sum()),
        "small_rel_ols": small_rel_err(beta_ols),
        "small_rel_ridge": small_rel_err(beta_ridge),
        "ols_check": ols_check,
        "fig": fig_t5,
    }


# --------------------------------------------------------------------------
# Task 6 - Bayesian estimate of the gamma rate
# --------------------------------------------------------------------------

def task6() -> dict:
    n, alpha_lik = P.TASK6_N, P.TASK6_ALPHA
    prior_shape, prior_beta = P.XI17, P.XI18
    xbar = P.XI19
    total = n * xbar

    # Hogg, McKean and Craig write the gamma density with beta as a scale.
    # Read consistently, the prior rate is 1/xi18.
    post_shape = prior_shape + alpha_lik * n
    post_rate = 1.0 / prior_beta + total
    post_mean = post_shape / post_rate
    post_mode = (post_shape - 1) / post_rate

    # The alternative reading, in which xi18 is a rate, is reported so that a
    # reader who uses the other convention can locate the difference at once.
    alt_rate = prior_beta + total
    alt_mean = post_shape / alt_rate
    alt_mode = (post_shape - 1) / alt_rate

    prior_mean = prior_shape * prior_beta
    mle = alpha_lik / xbar

    lo = stats.gamma.ppf(0.025, a=post_shape, scale=1 / post_rate)
    hi = stats.gamma.ppf(0.975, a=post_shape, scale=1 / post_rate)

    fig, axes = plt.subplots(1, 2, figsize=(6.8, 2.9))

    ax = axes[0]
    grid = np.linspace(0, prior_mean * 2.4, 600)
    ax.plot(grid, stats.gamma.pdf(grid, a=prior_shape, scale=prior_beta),
            color=MUTED, linewidth=1.5,
            label=fr"prior Gamma({prior_shape:.0f}, scale {prior_beta:.0f})")
    ax.axvline(prior_mean, color=MUTED, linestyle=":", linewidth=1.1,
               label=f"prior mean = {prior_mean:.0f}")
    ax.set_xlabel(r"$\theta$  (rate, per unit of x)")
    ax.set_ylabel(r"prior density $h(\theta)$")
    ax.set_title("(a) prior", fontsize=8.5)
    ax.set_ylim(bottom=0)
    ax.legend(loc="upper right", frameon=False, fontsize=7)

    ax = axes[1]
    grid = np.linspace(post_mean * 0.5, post_mean * 1.55, 600)
    density = stats.gamma.pdf(grid, a=post_shape, scale=1 / post_rate)
    ax.plot(grid, density, color=ACCENT, linewidth=1.6,
            label=fr"posterior Gamma({post_shape:.0f}, rate {post_rate:.1f})")
    band = (grid >= lo) & (grid <= hi)
    ax.fill_between(grid[band], density[band], color=ACCENT, alpha=0.15,
                    label=f"95 % credible: [{lo:.4f}, {hi:.4f}]")
    ax.axvline(post_mean, color=ALT, linestyle="--", linewidth=1.3,
               label=f"mean = {post_mean:.5f}")
    ax.axvline(post_mode, color=INK, linestyle=":", linewidth=1.3,
               label=f"mode = {post_mode:.5f}")
    ax.axvline(mle, color=MUTED, linestyle="-.", linewidth=1.3,
               label=fr"MLE $\alpha/\bar{{x}}$ = {mle:.5f}")
    ax.set_xlabel(r"$\theta$")
    ax.set_ylabel(r"posterior density $h(\theta \mid \mathbf{x})$")
    ax.set_title("(b) posterior", fontsize=8.5)
    ax.set_ylim(bottom=0)
    ax.legend(loc="upper left", frameon=False, fontsize=6.5)

    fig.tight_layout()
    fig_t6 = _save(fig, "task6_posterior")

    return {
        "n": n, "alpha_lik": alpha_lik,
        "prior_shape": prior_shape, "prior_beta": prior_beta,
        "prior_rate": 1 / prior_beta, "prior_mean": prior_mean,
        "xbar": xbar, "total": total,
        "post_shape": post_shape, "post_rate": post_rate,
        "post_scale": 1 / post_rate,
        "post_mean": post_mean, "post_mode": post_mode,
        "post_sd": math.sqrt(post_shape) / post_rate,
        "alt_rate": alt_rate, "alt_mean": alt_mean, "alt_mode": alt_mode,
        "alt_mean_diff_pct": 100 * abs(alt_mean - post_mean) / post_mean,
        "mle": mle,
        "cred_lo": float(lo), "cred_hi": float(hi),
        "prior_weight_pct": 100 * (1 / prior_beta) / post_rate,
        "fig": fig_t6,
    }


# --------------------------------------------------------------------------

def flatten(nested: dict) -> dict:
    """Turn ``{"task1": {"p": 0.65}}`` into ``{"task1.p": 0.65}``."""
    flat = {}
    for section, values in nested.items():
        for key, value in values.items():
            flat[f"{section}.{key}"] = value
    return flat


def main() -> int:
    BUILDDIR.mkdir(parents=True, exist_ok=True)
    results = {
        "task1": task1(),
        "task2": task2(),
        "task3": task3(),
        "task4": task4(),
        "task5": task5(),
        "task6": task6(),
    }
    results["meta"] = {
        "signature": P.SIGNATURE,
        "signature_short": P.SIGNATURE[:8],
        "xi1": P.XI1, "xi2": P.XI2, "xi4": P.XI4, "xi5": P.XI5, "xi6": P.XI6,
        "xi7": P.XI7, "xi8": P.XI8, "xi9": P.XI9,
        "xi10": ", ".join(f"{v:g}" for v in P.XI10),
        "xi11": P.XI11, "xi12": P.XI12, "xi13": P.XI13,
        "xi14": ", ".join(f"{v:g}" for v in P.XI14),
        "xi15": P.XI15,
        "xi16_n": len(P.XI16),
        "xi17": P.XI17, "xi18": P.XI18, "xi19": P.XI19,
    }

    out = BUILDDIR / "results.json"
    out.write_text(json.dumps(flatten(results), indent=2, sort_keys=True,
                              default=float), encoding="utf-8")
    print(f"wrote {out.relative_to(HERE)} with {len(flatten(results))} keys")
    print(f"wrote {len(list(FIGDIR.glob('*.png')))} figures to figures/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
