# Task 1: a single vote and its expectation

A single person casts one vote, which comes out either *for* or *against*. We
know that, across the population being sampled, a share
{{task1.p_pct:.0f}} % of votes are cast in favour. The question is what a
probability model of that one vote looks like, and whether an average value can
sensibly be attached to something that happens exactly once.

**Branch.** The personal parameter is $\xi_1 = {{meta.xi1}}$, so the Bernoulli
sub-task applies with $P(\text{vote} = \textit{for}) = \xi_2 = {{task1.p:.2f}}$.
The sub-tasks for $\xi_1 \in \{1,2,3\}$, which model meteorite counts by a
Poisson, negative binomial or geometric distribution, do not apply and are not
performed.

**Model.** The outcomes *for* and *against* are labels, not numbers, and nothing
can be averaged until they are coded numerically. We therefore define the random
variable $X$ on the two-point sample space $\Omega = \{\textit{against},
\textit{for}\}$ by $X(\textit{against}) = 0$ and $X(\textit{for}) = 1$. This
coding is a modelling choice and it is the choice that gives the expectation its
meaning. With $p = \xi_2 = {{task1.p:.2f}}$, the distribution of $X$ is described
by a probability mass function, not a density, because $X$ takes only isolated
values:

$$P(X = 1) = p = {{task1.p:.2f}}, \qquad P(X = 0) = 1 - p = {{task1.q:.2f}} .$$

The assumptions required are that exactly one vote is cast, that its two
outcomes are mutually exclusive and exhaustive so that the probabilities sum to
one, and that $p$ is a fixed constant rather than something varying between
voters. Abstention is excluded by construction; were it possible, the model
would need a third outcome (IU International University of Applied Sciences,
2025, Unit 1.3).

**Can an expectation be calculated?** Yes, and three conditions are worth
separating. First, $X$ must map outcomes to real numbers, which the coding above
provides. Second, $X$ must be measurable, which is automatic here because
$\Omega$ is finite and every subset is an event. Third, the expectation must
converge; for a variable taking finitely many values the defining sum has
finitely many terms, so $\mathbb{E}[|X|] < \infty$ holds trivially and no
integrability question arises. Hence

$$\mathbb{E}[X] = 0 \cdot (1-p) + 1 \cdot p = p = {{task1.mean:.2f}},$$

$$\operatorname{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2
 = p - p^2 = p(1-p) = {{task1.var:.4f}},$$

using $X^2 = X$, which holds because $X$ only takes the values $0$ and $1$. The
standard deviation is {{task1.sd:.4f}}.

Two readings must be kept apart. The value {{task1.mean:.2f}} is **not** a
possible result of the single vote, which yields either $0$ or $1$; it is the
long-run average over many independent repetitions. Equally, the percentages in
Figure 1 are *probabilities*, not observed relative frequencies: a single trial
can only ever produce a 100 %/0 % split of actual votes.

![Figure 1. Probability distribution of one vote. The vertical scale runs from 0 % to 100 % in steps of 10 %; bar heights are the probabilities of each coded outcome, and the dashed line marks the expectation at {{task1.mean:.2f}} on the $\{0,1\}$ coding.](figures/{{task1.fig}}){width=11cm}

**Trust.** Both results are elementary enough to be obtained by hand, and they
were: the arithmetic above is the complete derivation. The figure was drawn with
Matplotlib (Hunter, 2007) from the same two numbers. As a check, the
probabilities sum to ${{task1.p:.2f}} + {{task1.q:.2f}} = 1$, and the variance
attains the maximum value $p(1-p) \le 0.25$ expected for a Bernoulli variable,
consistent with $p$ lying near, but not at, one half.
