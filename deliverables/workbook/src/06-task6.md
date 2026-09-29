# Task 6: a Bayesian estimate of the gamma rate

The previous tasks estimated a parameter from data alone. Here we also hold a
belief about it beforehand, and must combine the two coherently. Following Hogg
et al. (2020, exercise 11.2.2), ten observations come from a gamma distribution
whose rate is itself uncertain, with a prior expressing what that rate was
thought to be.

**Parameterisation, stated before anything is derived.** A gamma distribution is
written $\operatorname{Gamma}(\alpha, \beta)$ with density
$f(x) = x^{\alpha-1}e^{-x/\beta}/(\Gamma(\alpha)\beta^{\alpha})$, so $\beta$ is a
**scale**, the **rate** is $1/\beta$, and the mean is $\alpha\beta$. This is the
convention of Hogg et al. (2020). The distinction is not pedantic: it changes the
answer, and by how much is quantified at the end.

**Setting.** Let $x_1,\dots,x_n$ with $n = {{task6.n}}$ be a random sample from
$\operatorname{Gamma}(\alpha = {{task6.alpha_lik:.0f}}, \beta = 1/\theta)$. Since
$\beta = 1/\theta$ is a scale, $\theta$ is the **rate** of the sampling
distribution, and

$$f(x \mid \theta) = \frac{\theta^{3}}{\Gamma(3)}x^{2}e^{-\theta x},
 \qquad x > 0 .$$

The prior $\theta \sim \operatorname{Gamma}({{task6.prior_shape:.0f}},
{{task6.prior_beta:.0f}})$ therefore has rate {{task6.prior_rate:.6f}} and mean
$\xi_{17}\xi_{18} = {{task6.prior_mean:.0f}}$. From
$\bar x = \xi_{19} = {{task6.xbar:.2f}}$ we get
$\sum_i x_i = {{task6.total:.1f}}$. The $x_i$ are assumed independent given
$\theta$, which lets the likelihood factorise.

## (a) The posterior distribution

Keeping only what depends on $\theta$, the likelihood and prior are

$$L(\theta) \propto \theta^{3n}\exp\!\left(-\theta\sum_{i=1}^{n}x_i\right),
 \qquad h(\theta) \propto \theta^{\xi_{17}-1}e^{-\theta/\xi_{18}} .$$

By Bayes' theorem the posterior is proportional to their product, which is
recognisable as another gamma density without computing the normalising constant:

$$h(\theta \mid \mathbf{x}) \propto
 \theta^{\xi_{17}+3n-1}
 \exp\!\left(-\theta\left[\textstyle\sum_i x_i + \tfrac{1}{\xi_{18}}\right]\right)
 \;\Rightarrow\; \theta \mid \mathbf{x} \sim
 \operatorname{Gamma}({{task6.post_shape:.0f}},\ \text{rate }
 {{task6.post_rate:.4f}}),$$

equivalently a scale of {{task6.post_scale:sci3}}. This is conjugacy: the family
is closed under updating by a likelihood of this form, and the update is simply
"add $3n$ to the shape and $\sum_i x_i$ to the rate".

## (b) The Bayes estimate under squared-error loss

Under the loss $L(\theta, d) = (\theta - d)^{2}$ the posterior expected loss is a
quadratic in $d$ whose derivative $-2\mathbb{E}[\theta\mid\mathbf{x}] + 2d$
vanishes at $d = \mathbb{E}[\theta\mid\mathbf{x}]$, so it is minimised by the
posterior **mean**. A gamma with shape $a$ and rate $r$ has mean $a/r$, so

$$\hat\theta_{\text{Bayes}} = \frac{\xi_{17}+3n}{\sum_i x_i + 1/\xi_{18}}
 = \frac{{{task6.post_shape:.0f}}}{{{task6.post_rate:.4f}}}
 = {{task6.post_mean:.6f}} .$$

## (c) The Bayes estimate using the posterior mode

Differentiating $\log h(\theta\mid\mathbf{x}) = (a-1)\log\theta - r\theta +
\text{const}$ gives $(a-1)/\theta - r = 0$, so the mode is $(a-1)/r$, valid here
because $a = {{task6.post_shape:.0f}} > 1$:

$$\hat\theta_{\text{mode}} = \frac{\xi_{17}+3n-1}{\sum_i x_i + 1/\xi_{18}}
 = \frac{{{task6.post_shape:.0f}}-1}{{{task6.post_rate:.4f}}}
 = {{task6.post_mode:.6f}} .$$

The mode is smaller than the mean because the gamma density is right-skewed, and
the gap narrows as the shape grows.

![Figure 7. (a) The prior on $\theta$, with mean {{task6.prior_mean:.0f}}. (b) The posterior, with the Bayes estimate under squared-error loss, the posterior mode, the shaded 95 % credible interval, and the maximum likelihood estimate {{task6.mle:.5f}} shown for comparison. Note the change of horizontal scale between the panels.](figures/{{task6.fig}}){width=15.5cm}

**How much the prior is doing.** The data alone give
$\hat\theta_{\text{MLE}} = \alpha/\bar x = {{task6.mle:.6f}}$, well below the
Bayes estimate and outside the 95 % credible interval
$[{{task6.cred_lo:.4f}}, {{task6.cred_hi:.4f}}]$. The update rule explains why:
the prior contributes ${{task6.prior_shape:.0f}}$ of the
{{task6.post_shape:.0f}} shape units, over forty per cent, but only
{{task6.prior_rate:.4f}} of the {{task6.post_rate:.1f}} rate units, so it pulls
the estimate upwards. That the prior mean {{task6.prior_mean:.0f}} sits four
orders of magnitude from the posterior mean signals a prior poorly matched to the
data, exerting influence through the shape rather than the rate; in practice that
mismatch would be worth raising with whoever supplied it.

**The parameterisation, quantified.** Had $\xi_{18} = {{task6.prior_beta:.0f}}$
been read as a rate, the posterior rate would be {{task6.alt_rate:.1f}}, giving a
Bayes estimate {{task6.alt_mean:.6f}} and mode {{task6.alt_mode:.6f}}, differing
by {{task6.alt_mean_diff_pct:.2f}} % from the values above. Parts (a) to (c) use
the scale convention declared at the start.

**Trust.** The posterior, both estimators and the loss argument were derived by
hand; software only evaluated the expressions and supplied the credible interval
from the gamma quantile function in SciPy (Virtanen et al., 2020). Two checks:
the posterior shape and rate satisfy the conjugate update rule, and the posterior
mean, mode and standard deviation ({{task6.post_sd:.6f}}) are mutually consistent
with the gamma identities $a/r$, $(a-1)/r$ and $\sqrt{a}/r$.
