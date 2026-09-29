# Task 3: bandwidth to failure of a pair of routers

A router carries traffic until its hardware fails; the quantity of interest is
the total volume of data it moves before that happens, in terabytes. A second,
identical router takes over automatically when the first dies. The question is
how much data the pair delivers in total, and what an experiment tells us about
the model's single unknown parameter.

**Branch.** The personal parameter is $\xi_9 = {{meta.xi9}}$, so the single-router
density is

$$f_S(s) = \frac{1}{\theta}e^{-s/\theta}, \qquad s > 0, \; \theta > 0 ,$$

that is, $S$ is exponentially distributed with mean $\theta$. The branches
$\xi_9 = 1$ and $\xi_9 = 2$, which give gamma densities of shapes 5 and 7, do not
apply and are not performed.

**Expressing $T$, and the assumptions this needs.** The second router only
carries traffic once the first has failed, so the totals add: $T = S_1 + S_2$.
Four assumptions are needed. The routers are of the same type, so $S_1$ and
$S_2$ are identically distributed. Their failures have independent physical
causes, so $S_1$ and $S_2$ are independent; this would fail if they shared a
power supply or an over-heating rack. Failover is immediate and perfect, so no
traffic is lost and nothing double-counted. Finally, the exponential model
asserts the memoryless property: a router that has already carried $s$ terabytes
is as likely to survive the next terabyte as a new one. That last assumption is
the questionable one, since real hardware shows wear-out, and it should be
checked against maintenance records before the model is relied upon.

**Density of $T$.** For independent non-negative variables the density of a sum
is the convolution of the densities (IU International University of Applied
Sciences, 2025, Unit 3.5):

$$f_T(t) = \int_0^{t} f_S(u)\,f_S(t-u)\,du
 = \int_0^{t} \frac{1}{\theta^2}e^{-u/\theta}e^{-(t-u)/\theta}\,du
 = \frac{1}{\theta^{2}}e^{-t/\theta}\int_0^{t} du
 = \frac{t}{\theta^{2}}e^{-t/\theta} .$$

The exponents sum to $-t/\theta$ regardless of $u$, leaving an integrand constant
in $u$. The result is the $\operatorname{Gamma}(2, \theta)$ density, also called
the two-stage Erlang distribution.

**Likelihood and the transformation requested.** For an independent sample
$T_1, \dots, T_n$,

$$L(\theta) = \prod_{i=1}^{n} \frac{T_i}{\theta^{2}}e^{-T_i/\theta}
 = \left(\prod_{i=1}^{n} T_i\right)\theta^{-2n}
   \exp\!\left(-\frac{1}{\theta}\sum_{i=1}^{n} T_i\right).$$

The transformation that makes this tractable is the logarithm: $\log$ is
strictly increasing, so it preserves the location of the maximum while turning
the product into a sum. Writing $\ell(\theta) = \log L(\theta)$,

$$\ell(\theta) = \sum_{i=1}^{n}\log T_i - 2n\log\theta
 - \frac{1}{\theta}\sum_{i=1}^{n} T_i, \qquad
 \ell'(\theta) = -\frac{2n}{\theta} + \frac{1}{\theta^{2}}\sum_{i=1}^{n} T_i .$$

Setting $\ell'(\theta) = 0$ gives
$\hat\theta = \frac{1}{2n}\sum_i T_i = \bar T/2$, a maximum rather than a minimum
or inflexion since $\ell''(\hat\theta) = -2n/\hat\theta^{2} < 0$ and $\ell$ tends
to $-\infty$ at both ends of $(0, \infty)$.

**Results.** The experiment gave $\xi_{10} = ({{task3.sample}})$ terabytes, so
$n = {{task3.n}}$, $\sum_i T_i = {{task3.total:.0f}}$ and
$\bar T = {{task3.mean:.1f}}$. Hence

$$\hat\theta = \frac{{{task3.total:.0f}}}{2 \times {{task3.n}}}
 = {{task3.theta_hat:.2f}}\ \text{TB}, \qquad
 \mathbb{E}[T] = 2\hat\theta = {{task3.expected_t:.1f}}\ \text{TB}.$$

That $\mathbb{E}[T]$ equals $\bar T$ is no coincidence: the likelihood equation
matches the model mean to the sample mean.

![Figure 4. Left: the log-likelihood in terabytes, with the maximum at $\hat\theta = {{task3.theta_hat:.2f}}$ TB. Right: the fitted density of $T$ in units of TB$^{-1}$, with the five observations shown as ticks and the fitted mean {{task3.expected_t:.1f}} TB marked.](figures/{{task3.fig}}){width=15.5cm}

**Trust.** The convolution, likelihood and estimator were derived by hand. As an
independent check the log-likelihood was also maximised numerically with SciPy
(Virtanen et al., 2020), returning {{task3.theta_numeric:.6f}} against the closed
form {{task3.theta_hat:.6f}}, a difference of {{task3.theta_abs_err:sci1}}. Two
cautions belong with the result. With $n = {{task3.n}}$ the Fisher information
$2n/\hat\theta^{2}$ gives a standard error of {{task3.se:.2f}} TB and an
approximate 95 % interval $[{{task3.ci_lo:.2f}}, {{task3.ci_hi:.2f}}]$, which is
very wide. As a rough goodness-of-fit check the observed coefficient of variation
is {{task3.cv_obs:.3f}} against the {{task3.cv_model:.3f}} implied by
$\operatorname{Gamma}(2, \theta)$: close enough not to contradict the model,
though five points establish little.
