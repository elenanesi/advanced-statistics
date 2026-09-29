# Task 5: fitting a degree-ten polynomial, with and without a penalty

We are given an unknown function's values at {{task5.n}} points and asked to fit
a polynomial, first by ordinary least squares (OLS) and then with a ridge
penalty. The difficulty is arithmetic reliability: $x$ spans
${{task5.x_min:.0f}}$ to ${{task5.x_max:.0f}}$ and $20^{10}\approx 10^{13}$, so a
naive computation destroys precision before any statistics begin.

**Branch.** The personal parameter is $\xi_{15} = {{meta.xi15}}$, so the model is
the polynomial of degree {{task5.degree}},

$$f(x) = \alpha_0 + \alpha_1 x + \alpha_2 x^{2} + \dots + \alpha_{10}x^{10},$$

with ${{task5.n_params}}$ coefficients. The branch $\xi_{15} = 0$, of degree
twelve, does not apply. With {{task5.n}} points against {{task5.n_params}}
coefficients the system is overdetermined, so least squares is well posed.

**Setting up, and why scaling is not optional.** The model is non-linear in $x$
but **linear in the parameters**, which is what lets least squares apply. Writing
$y = X\alpha + \varepsilon$ with the Vandermonde design matrix
$X_{ij} = x_i^{\,j}$, the condition number of $X$ on the raw data is
${{task5.cond_raw:sci2}}$. A condition number measures how far relative input
errors are amplified, so at $10^{13}$, against sixteen significant digits of
double precision, almost nothing survives. Rescaling to
$\tilde x = x/{{task5.x_scale:.0f}} \in [-1,1]$ lowers it to
${{task5.cond_scaled:.0f}}$, a factor of ${{task5.cond_ratio:sci1}}$; the
response is rescaled by $\max_i|y_i| = {{task5.y_scale:sci2}}$ for the same
reason, and coefficients are mapped back afterwards. All penalties below refer to
this standardised problem, since $\lambda$ is meaningless until both axes are
fixed.

**The two estimates.** OLS minimises $\lVert y - X\alpha\rVert^{2}$; ridge adds a
penalty on coefficient size (Hastie et al., 2009, sec. 3.4.1),

$$\hat\alpha(\lambda) = \arg\min_{\alpha}
 \left\{ \lVert y - X\alpha \rVert^{2} + \lambda \sum_{j\ge 1}\alpha_j^{2} \right\},$$

with the intercept excluded so the fit does not depend on where the origin of
$y$ sits. Rather than forming $X^{\top}X$, which would square the condition
number back to $10^{7}$, the solution is read off the singular value
decomposition $X = UDV^{\top}$ as
$\hat\alpha(\lambda) = V\operatorname{diag}(d_j/(d_j^{2}+\lambda))U^{\top}y$:
stable for every $\lambda \ge 0$, equal to OLS at $\lambda = 0$, and showing what
the penalty does: shrink the directions with small singular values, exactly those
the data determines poorly. The weight was chosen by leave-one-out
cross-validation, which for a linear smoother needs no refitting: with $h_i$ the
$i$-th diagonal element of the hat matrix the criterion
$\frac{1}{n}\sum_i (e_i/(1-h_i))^{2}$ is minimised at
$\lambda^{*} = {{task5.lam_star:sci2}}$: a prediction criterion rather than a
preference. It is shallow, though — every penalty from
${{task5.lam_band_lo:sci1}}$ to ${{task5.lam_band_hi:sci1}}$ scores within 1 % of
the best, so only the order of magnitude of $\lambda^{*}$ is determined.

**Qualities of the two solutions.** In-sample OLS fits best, as it must: root
mean squared error ${{task5.rmse_ols:sci2}}$ against ${{task5.rmse_ridge:sci2}}$
for ridge at $\lambda^{*}$ and ${{task5.rmse_heavy:sci2}}$ at a heavy
$\lambda = {{task5.lam_heavy}}$. Ridge buys stability: the non-intercept
coefficient norm falls from {{task5.norm_ols:.3f}} to {{task5.norm_ridge:.3f}}, a
reduction of {{task5.norm_shrink_pct:.1f}} %, the bias-variance trade in concrete
form.

A more serious limitation affects **both**. Least squares minimises absolute
squared error, so the fit is dominated by the largest $|y|$, around
${{task5.y_scale:sci1}}$ at the edges. Where $|x| \le 7$ and $|y|$ stays
below about $2\times 10^{9}$, neither estimate carries information: the sample
contains $x = 0$ with $y = {{task5.y_at_zero:.2f}}$, yet the fitted intercept is
${{task5.a0_ols:sci2}}$ for OLS and ${{task5.a0_ridge:sci2}}$ for ridge, both
wrong by orders of magnitude on a directly observed point. Figure 6 shows both
fits indistinguishable from the data over the full range, while the zoom reveals
them swinging through $\pm 10^{11}$ around observations effectively zero at that
scale. Were that region to matter, the remedy would be a relative-error
criterion, not a larger penalty.

![Figure 6. (a) Data and both fits over the full range, in units of $10^{13}$. (b) The same fits for $|x| \le 7$, in units of $10^{11}$, where the observations are indistinguishable from zero and both fits oscillate wildly. (c) Leave-one-out mean squared error against the penalty, with the minimum at $\lambda^{*} = {{task5.lam_star:sci2}}$.](figures/{{task5.fig}}){width=16cm}

**Trust.** The estimators and the leave-one-out identity were derived by hand and
no black-box regression routine was used; NumPy (Harris et al., 2020) supplied
only the decomposition and the condition numbers. As a check, $\lambda = 0$
reproduces the fit from `numpy.linalg.lstsq` to
{{task5.ols_check:sci1}} across all {{task5.n_params}} coefficients.
