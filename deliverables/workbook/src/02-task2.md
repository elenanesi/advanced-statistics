# Task 2: waiting for the owl

You open a window and wait to hear an owl. What is modelled is not whether the
owl calls but *how long* the wait is, so the natural object is the chance that
you are **still** waiting after $y$ hours. That quantity, read as a function of
$y$, is the survival function, and everything else in this task is obtained from
it.

**Branch.** With $\xi_4 = {{meta.xi4}}$ the survival function is

$$\bar F_Y(y) = P(Y > y) = \xi_5 e^{-\xi_6 y^2} + \xi_7 e^{-\xi_8 y^8},
  \qquad y \ge 0,$$

with $\xi_6 = {{task2.xi6:.0f}}$ and $\xi_8 = {{task2.xi8:.0f}}$. The branches
$\xi_4 \in \{0,2,3\}$ do not apply and are not performed.

**A correction to the parameters, made explicit.** The task sheet requires
$\xi_5 + \xi_7 = 1$, but the generator returned $\xi_5 = {{task2.xi5:.2f}}$ and
$\xi_7 = {{task2.xi7:.2f}}$, summing to {{task2.xi5_plus_xi7:.2f}}. This is not
cosmetic: $\bar F_Y(0) = \xi_5 + \xi_7$, so the model as delivered would assign
probability ${{task2.xi_deficit:.2f}}$ to the owl already being audible the
instant the window opens,
and its density would integrate to {{task2.xi5_plus_xi7:.2f}} rather than to one.
The discrepancy is a rounding artefact, and dividing by the observed total
recovers $\xi_5^{*} = {{task2.w1_frac}}$ and $\xi_7^{*} = {{task2.w2_frac}}$
exactly, so the generator drew those fractions and truncated each to two
decimals. The renormalised weights are used from here on; they satisfy the
required constraint and give $\bar F_Y(0) = 1$.

**Model and assumptions.** $Y \ge 0$ is the waiting time in hours from the moment
the window is opened. $\bar F_Y$ is continuous and strictly decreasing with
$\bar F_Y(0) = 1$ and $\bar F_Y(y) \to 0$, so $Y$ is continuous with no atoms.
Both terms are Weibull survival functions, which shows what the model says: a
**mixture** of a fast mechanism (shape ${{task2.comp1_shape}}$, scale
{{task2.comp1_scale:.4f}} h, weight ${{task2.w1_frac}}$, mean
{{task2.comp1_mean_min:.1f}} min) and a slow one (shape ${{task2.comp2_shape}}$,
scale {{task2.comp2_scale:.4f}} h, weight ${{task2.w2_frac}}$, mean
{{task2.comp2_mean_min:.1f}} min). The two mechanisms are why the density in
Figure 2 has peaks near {{task2.mode1_min:.0f}} and {{task2.mode2_min:.0f}}
minutes.

**Derivation.** Since $F_Y = 1 - \bar F_Y$, the density is minus the derivative
of the survival function (Ross, 2019, ch. 5):

$$f_Y(y) = -\frac{d}{dy}\bar F_Y(y)
 = 2\xi_6\,\xi_5^{*}\, y\, e^{-\xi_6 y^2}
 + 8\xi_8\,\xi_7^{*}\, y^{7} e^{-\xi_8 y^8}, \qquad y \ge 0 .$$

For a non-negative variable the expectation is the area under the survival
function, $\mathbb{E}[Y] = \int_0^{\infty}\bar F_Y(y)\,dy$, and likewise
$\mathbb{E}[Y^2] = 2\int_0^{\infty} y\,\bar F_Y(y)\,dy$. Both integrals are
standard gamma integrals, giving closed forms rather than only numbers:

$$\mathbb{E}[Y] = \frac{\xi_5^{*}}{2}\sqrt{\frac{\pi}{\xi_6}}
 + \xi_7^{*}\,\Gamma\!\left(\tfrac{9}{8}\right)\xi_8^{-1/8}, \qquad
 \mathbb{E}[Y^2] = \frac{\xi_5^{*}}{\xi_6}
 + \frac{\xi_7^{*}\,\Gamma\!\left(\tfrac{1}{4}\right)}{4\,\xi_8^{1/4}} .$$

**Results.** $\mathbb{E}[Y] = {{task2.mean_h:.5f}}$ h $= {{task2.mean_min:.2f}}$
minutes and $\operatorname{Var}(Y) = {{task2.var_h2:.5f}}$ h$^2$, a standard
deviation of {{task2.sd_min:.2f}} minutes. Solving $F_Y(y) = q$ numerically
gives quartiles $Q_1 = {{task2.q1_min:.2f}}$, median $= {{task2.median_min:.2f}}$
and $Q_3 = {{task2.q3_min:.2f}}$ minutes, an interquartile range of
{{task2.iqr_min:.2f}} minutes. The requested probability is

$$P(2 < Y < 4) = \bar F_Y(2) - \bar F_Y(4) = {{task2.p_2_4:sci3}} ,$$

which is effectively zero, and not by accident: the model places
{{task2.p_within_hour_pct:.2f}} % of the probability inside the first hour, so a
wait of two to four hours is essentially impossible under it. A reader should
treat this as a statement about the model, not about owls.

![Figure 2. Probability density of the waiting time, in hours. The vertical axis is a density in units of hour$^{-1}$, so areas, not heights, are probabilities. Dotted lines mark the quartiles and the dashed line the mean; both are annotated in minutes.](figures/{{task2.fig_pdf}}){width=15cm}

**Units.** The density is expressed per hour, so a per-minute statement must be
obtained as a probability over an interval, not by rescaling the density: the
chance of first hearing the owl during minute $k$ is
$\bar F_Y((k-1)/60) - \bar F_Y(k/60)$. Minutes {{task2.peak_minute_2}} and
{{task2.peak_minute}} tie for the largest value at
{{task2.peak_minute_2_pct:.2f}} % and {{task2.peak_minute_pct:.2f}} %; the
difference between them is smaller than the rounding shown, so neither should be
quoted as the single most likely minute.

![Figure 3. Probability of first hearing the owl during each of the first 60 minutes. The vertical scale is a probability in per cent, and the 60 bars sum to {{task2.p_within_hour_pct:.2f}} %, the probability of hearing the owl within the first hour.](figures/{{task2.fig_hist}}){width=15cm}

**Trust.** The density, both expectation integrals and the closed forms were
derived by hand; SciPy (Virtanen et al., 2020) only evaluated them and solved for
the quartiles by bisection. Checking algebra and code together, quadrature of
$\int y f_Y(y)\,dy$ returns {{task2.mean_num_h:.9f}} against the closed form
{{task2.mean_h:.9f}}, and $\int_0^{\infty} f_Y(y)\,dy = {{task2.mass:.6f}}$,
confirming the renormalised density integrates to one.
