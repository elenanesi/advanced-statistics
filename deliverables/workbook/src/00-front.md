```{=openxml}
<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="2400" w:after="240"/></w:pPr><w:r><w:rPr><w:sz w:val="24"/></w:rPr><w:t>IU International University of Applied Sciences</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="960"/></w:pPr><w:r><w:rPr><w:sz w:val="22"/></w:rPr><w:t>Examination Office</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="120"/></w:pPr><w:r><w:rPr><w:b/><w:sz w:val="40"/></w:rPr><w:t>Advanced Workbook</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="960"/></w:pPr><w:r><w:rPr><w:sz w:val="28"/></w:rPr><w:t>Solutions to Assignments 1 to 6</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="60"/></w:pPr><w:r><w:t>Type of assessment: Advanced Workbook</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="60"/></w:pPr><w:r><w:t>Course: Advanced Statistics (DLMDSAS01)</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="600"/></w:pPr><w:r><w:t>Degree programme: [[PLACEHOLDER: full degree programme name, no abbreviations]]</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="60"/></w:pPr><w:r><w:t>Submitted by: [[PLACEHOLDER: first name and last name]]</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="60"/></w:pPr><w:r><w:t>Registration number: [[PLACEHOLDER: registration number]]</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="60"/></w:pPr><w:r><w:t>Tutor: [[PLACEHOLDER: academic title and name of the tutor]]</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="60"/></w:pPr><w:r><w:t>Place: [[PLACEHOLDER: place]]</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="720"/></w:pPr><w:r><w:t>Date of submission: [[PLACEHOLDER: YYYY-MM-DD]]</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="60"/></w:pPr><w:r><w:rPr><w:sz w:val="18"/></w:rPr><w:t>Parameters produced by the IU parameter generator.</w:t></w:r></w:p>
<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="0"/></w:pPr><w:r><w:rPr><w:sz w:val="18"/></w:rPr><w:t>Signature string: {{meta.signature}}</w:t></w:r></w:p>
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Table of contents {-}

```{=openxml}
<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r><w:r><w:instrText xml:space="preserve"> TOC \o "1-3" \h \z \u </w:instrText></w:r><w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>Right-click here in Word and choose "Update field" to build the table of contents.</w:t></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# List of figures {-}

```{=openxml}
<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r><w:r><w:instrText xml:space="preserve"> TOC \h \z \t "Image Caption,1" </w:instrText></w:r><w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>Right-click here in Word and choose "Update field" to build the list of figures.</w:t></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# List of abbreviations {-}

| Abbreviation | Meaning |
|---|---|
| CDF | Cumulative distribution function |
| i.i.d. | Independent and identically distributed |
| IQR | Interquartile range |
| LOOCV | Leave-one-out cross-validation |
| MLE | Maximum likelihood estimation, or the maximum likelihood estimate |
| MSE | Mean squared error |
| OLS | Ordinary least squares |
| PDF | Probability density function |
| PMF | Probability mass function |
| RMSE | Root mean squared error |
| SVD | Singular value decomposition |

# Notation {-}

Every symbol used in this workbook is listed here, because a notation that is
not declared carries the same risk of misreading as an invented word.

| Symbol | Meaning |
|---|---|
| $\xi_k$ | The $k$-th personal parameter produced by the IU parameter generator |
| $X, Y, S, T, \Theta$ | Random variables, written as capital letters |
| $x, y, s, t, \theta$ | Realised values or arguments of a function, written in lower case |
| $P(A)$ | Probability of the event $A$ |
| $f_X(x)$ | Probability density function of the continuous random variable $X$ |
| $F_X(x)$ | Cumulative distribution function, $F_X(x) = P(X \le x)$ |
| $\bar F_X(x)$ | Survival function, $\bar F_X(x) = P(X > x) = 1 - F_X(x)$ |
| $\mathbb{E}[X]$ | Expectation of $X$ |
| $\operatorname{Var}(X)$ | Variance of $X$, equal to $\mathbb{E}[X^2] - (\mathbb{E}[X])^2$ |
| $\bar x$ | Arithmetic mean of an observed sample |
| $s$ | Sample standard deviation, computed with denominator $n-1$ |
| $\hat\theta$ | An estimate of the parameter $\theta$ |
| $L(\theta)$, $\ell(\theta)$ | Likelihood and log-likelihood of $\theta$ |
| $\Gamma(\cdot)$ | The gamma function, $\Gamma(n) = (n-1)!$ for integer $n$ |
| $\alpha$ | Significance level in Task 4; polynomial coefficients in Task 5; gamma shape in Task 6 |
| $\lambda$ | Ridge penalty weight in Task 5 |
| $\propto$ | "Is proportional to", used when a normalising constant is omitted |

A gamma distribution is written $\operatorname{Gamma}(\alpha, \beta)$ with
density $f(x) = x^{\alpha-1}e^{-x/\beta}/(\Gamma(\alpha)\beta^{\alpha})$, so
that $\beta$ is a **scale**. Where a **rate** is meant, it is stated explicitly
and equals $1/\beta$. This is the convention of Hogg et al. (2020) and is used
without exception throughout, including in Tasks 3 and 6.

# Personal parameters and scope {-}

The parameter generator returned the values reproduced in Appendix A under the
signature `{{meta.signature}}`. Several tasks branch on a parameter: the branch
that applies is stated at the start of each section, and the branches that do
not apply are named and skipped, as the task sheet requires.

The applicable branches are $\xi_1 = {{meta.xi1}}$ (Task 1),
$\xi_4 = {{meta.xi4}}$ (Task 2), $\xi_9 = {{meta.xi9}}$ (Task 3),
$\xi_{13} = {{meta.xi13}}$ (Task 4) and $\xi_{15} = {{meta.xi15}}$ (Task 5).
Task 6 has no branch.

```{=openxml}
<w:p><w:pPr><w:pStyle w:val="BodyText"/></w:pPr><w:r><w:t>%%SECTION-BREAK-ARABIC%%</w:t></w:r></w:p>
```
