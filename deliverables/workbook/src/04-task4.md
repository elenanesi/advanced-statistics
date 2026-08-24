# Task 4: does the new system produce heavier hammers?

A factory has produced hammers long enough for the weight of its output to be
well characterised. A new production system is introduced and ten hammers are
weighed. Are those weights heavy enough to be evidence that the process now makes
heavier hammers, or is the difference what ten measurements throw up by chance?

**Branch.** The personal parameter is $\xi_{13} = {{meta.xi13}}$, so the question
is whether the new system makes **higher** weights. The questions for
$\xi_{13} \in \{0,1,3\}$, about more constant, lower and less constant weights,
do not apply and are not performed.

**Model and assumptions.** Let $X$ be the weight in grams of one hammer from the
new system, modelled as $X \sim \operatorname{Normal}(\mu, \sigma^{2})$. Weight
is the sum of many small independent contributions, so a normal shape is
plausible by a central limit argument; a normal variable can be negative whereas
a weight cannot, but at these values that probability is negligible. The ten
hammers are drawn independently and the process does not drift while they are
made. Finally, and this assumption does the real work, the historical figures
from 1,000 hammers are treated as **known**,
$\mu_0 = \xi_{11} = {{task4.mu0:.0f}}$ g and
$\sigma_0 = \xi_{12} = {{task4.sigma0:.1f}}$ g, with $\sigma$ unchanged by the new
system. Only $\mu$ is then in question.

**Hypotheses.** The question is directional, so the test is one-sided:

$$H_0: \mu \le \mu_0 = {{task4.mu0:.0f}}\ \text{g}
 \qquad \text{against} \qquad
 H_1: \mu > \mu_0 = {{task4.mu0:.0f}}\ \text{g}.$$

The claim to be established is placed in $H_1$, so the burden of proof falls on
it and the error controlled at level $\alpha$ is that of announcing an
improvement which is not there.

**Which test, and the lookalike to avoid.** Because $\sigma$ is taken as known,
the standardised sample mean is exactly standard normal under $H_0$, so the
correct statistic is a $z$-statistic. A $t$-statistic would be correct had
$\sigma$ been estimated from the ten hammers themselves. The two differ in what
sits in the denominator; both are reported below.

**Decision rule.** With $\alpha = {{task4.alpha:.2f}}$ and
$z_{1-\alpha} = {{task4.z_crit:.4f}}$ (IU International University of Applied
Sciences, 2025, Unit 7.1), the rule is

$$\text{reject } H_0 \iff
 Z = \frac{\bar X - \mu_0}{\sigma_0/\sqrt{n}} > {{task4.z_crit:.4f}}
 \iff \bar X > {{task4.crit_weight:.2f}}\ \text{g}.$$

**Computation and conclusion.** The sample $\xi_{14}$ is ({{task4.sample}})
grams, so $n = {{task4.n}}$, $\bar x = {{task4.xbar:.1f}}$ g and
$\sigma_0/\sqrt{n} = {{task4.se:.4f}}$ g. Therefore

$$z = \frac{{{task4.xbar:.1f}} - {{task4.mu0:.0f}}}{{{task4.se:.4f}}}
 = {{task4.z:.4f}}, \qquad p = P(Z > {{task4.z:.4f}}) = {{task4.p_value:.4f}} .$$

Since ${{task4.z:.4f}} < {{task4.z_crit:.4f}}$, equivalently
$\bar x = {{task4.xbar:.1f}} < {{task4.crit_weight:.2f}}$ g, we **fail to reject**
$H_0$: at the 5 % level there is no evidence that the new system produces higher
weights. That is not evidence that it does not; the test simply detected no
difference. Treating $\sigma$ as unknown gives $t = {{task4.t_stat:.4f}}$ on
${{task4.df}}$ degrees of freedom against a critical value {{task4.t_crit:.4f}}
and $p = {{task4.t_p:.4f}}$, so the conclusion is unchanged.

![Figure 5. Sampling distribution of the mean weight of ten hammers under $H_0$, in grams. The shaded upper tail is the rejection region of size {{task4.alpha_pct:.0f}} %, beginning at the critical value {{task4.crit_weight:.1f}} g; the solid line marks the observed mean {{task4.xbar:.1f}} g, which falls well short of it.](figures/{{task4.fig}}){width=14.5cm}

**Error probabilities.** The Type I error, rejecting $H_0$ when it holds, is
fixed at $\alpha = {{task4.alpha_pct:.0f}}$ % by construction. The Type II error
depends on the true mean: at an increase equal to the observed
{{task4.diff:.1f}} g the power is only {{task4.power_at_obs_pct:.2f}} %, so
$\beta \approx {{task4.beta_at_obs_pct:.2f}}$ %. Equivalently, with
$n = {{task4.n}}$ and $\sigma_0 = {{task4.sigma0:.1f}}$ g the smallest increase
this design detects with 80 % power is {{task4.delta_80:.2f}} g, over four times
what was seen. The non-rejection therefore says as much about the sample size as
about the hammers, and a larger sample is the appropriate next step.

**Trust.** The hypotheses, decision rule and power calculation were derived by
hand; SciPy (Virtanen et al., 2020) supplied only quantiles and tail
probabilities. One caveat should not be buried: $s = {{task4.s:.2f}}$ g against
the historical $\sigma_0 = {{task4.sigma0:.1f}}$ g is a variance ratio of
{{task4.var_ratio:.2f}}, so the assumption of unchanged spread is doubtful. If it
is wrong the true standard error exceeds the one used here, which weakens the
evidence for a higher mean rather than strengthening it.
