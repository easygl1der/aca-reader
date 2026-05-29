# Homework 5 Solutions

## Problem 21.1: Variance of the Wald estimator

The Wald estimator is defined as:
$$
\hat{\tau}_\cp = \frac{\hat{\tau}_Y}{\hat{\tau}_D} = \frac{\bar{Y}_1 - \bar{Y}_0}{\bar{D}_1 - \bar{D}_0}
$$
In a finite sample of size $n$, the denominator $\hat{\tau}_D = \bar{D}_1 - \bar{D}_0$ is a random variable. Since $D_i$ is binary, $\bar{D}_1$ and $\bar{D}_0$ are averages of Bernoulli-like variables. Specifically, if $n_1$ units are assigned to $Z=1$ and $n_0$ to $Z=0$, then $n_1 \bar{D}_1$ follows a Binomial distribution (under certain assumptions) or a similar discrete distribution.

There exists a non-zero probability that $\hat{\tau}_D = 0$. For example, if all $D_i$ in the $Z=1$ group and all $D_i$ in the $Z=0$ group happen to be the same (e.g., all 0 or all 1), then $\hat{\tau}_D = 0$. 
The variance of a random variable $X$ is $E[X^2] - (E[X])^2$. For the Wald estimator:
$$
E[\hat{\tau}_\cp^2] = E\left[ \left( \frac{\hat{\tau}_Y}{\hat{\tau}_D} \right)^2 \right] = \sum_{d \in \text{support}(\hat{\tau}_D)} \pr(\hat{\tau}_D = d) E\left[ \hat{\tau}_\cp^2 \mid \hat{\tau}_D = d \right]
$$
If $\pr(\hat{\tau}_D = 0) > 0$, the term for $d=0$ involves division by zero, making the expectation (and thus the variance) undefined or infinite in a measure-theoretic sense. Even if we consider the limit as the denominator approaches zero, the integral blows up. Thus, $\var(\hat{\tau}_\cp) = \infty$.

## Problem 21.6: Binary IV and ordinal treatment received

We use Abel's lemma (summation by parts):
$$
\sum_{j=1}^J f_j(g_j - g_{j-1}) = f_J g_J - f_1 g_0 - \sum_{j=1}^{J-1} g_j(f_{j+1} - f_j)
$$
Wait, the suggested version is:
$$
\sum_{j=0}^J f_j(g_{j+1}-g_j) = f_Jg_{J+1}-f_0g_0-\sum_{j=1}^J g_j(f_j-f_{j-1})
$$
Let $D(z) = \sum_{j=1}^J \mathbb{I}(D(z) \ge j)$. Then:
$$
E[D(1) - D(0)] = \sum_{j=1}^J E[\mathbb{I}(D(1) \ge j) - \mathbb{I}(D(0) \ge j)] = \sum_{j=1}^J \pr(D(1) \ge j > D(0))
$$
by monotonicity $D(1) \ge D(0)$.
For the outcome, under exclusion restriction $Y(z,d) = Y(d)$:
$$
Y(D(z)) = Y(0) + \sum_{j=1}^J [Y(j) - Y(j-1)] \mathbb{I}(D(z) \ge j)
$$
The ITT effect is:
$$
E[Y(D(1)) - Y(D(0))] = \sum_{j=1}^J E[ (Y(j) - Y(j-1)) (\mathbb{I}(D(1) \ge j) - \mathbb{I}(D(0) \ge j)) ]
$$
By monotonicity, $\mathbb{I}(D(1) \ge j) - \mathbb{I}(D(0) \ge j) = \mathbb{I}(D(1) \ge j > D(0))$.
Thus:
$$
E[Y\mid Z=1] - E[Y\mid Z=0] = \sum_{j=1}^J E[ Y(j) - Y(j-1) \mid D(1) \ge j > D(0) ] \pr(D(1) \ge j > D(0))
$$
The ratio is:
$$
\frac{E[Y\mid Z=1] - E[Y\mid Z=0]}{E[D\mid Z=1] - E[D\mid Z=0]} = \frac{\sum_{j=1}^J E[ Y(j) - Y(j-1) \mid D(1) \ge j > D(0) ] \pr(D(1) \ge j > D(0))}{\sum_{j=1}^J \pr(D(1) \ge j > D(0))}
$$
This is exactly the weighted average $\sum w_j E\{Y(j)-Y(j-1)\mid D(1)\geq j>D(0)\}$ with $w_j$ defined as in the problem.

## Problem 22.2: Risk ratio for compliers

The mixture identification formulas are:
$\pi_\nt = \pr(D=0\mid Z=1)$
$\pi_\at = \pr(D=1\mid Z=0)$
$\pi_\cp = E(D\mid Z=1) - E(D\mid Z=0)$
Complier potential outcome means:
$\mu_{1\cp} = \frac{E(DY\mid Z=1) - E(DY\mid Z=0)}{\pi_\cp}$
$\mu_{0\cp} = \frac{E((1-D)Y\mid Z=0) - E((1-D)Y\mid Z=1)}{\pi_\cp}$

The risk ratio for compliers is $\RR_\cp = \frac{\mu_{1\cp}}{\mu_{0\cp}}$.
The numerator is $\frac{E(DY\mid Z=1) - E(DY\mid Z=0)}{\pi_\cp}$.
The denominator is $\frac{E((1-D)Y\mid Z=0) - E((1-D)Y\mid Z=1)}{\pi_\cp}$.
Note that $E((1-D)Y) = E(Y - DY)$.
Denominator numerator: $E(Y - DY \mid Z=0) - E(Y - DY \mid Z=1) = [E(Y\mid Z=0) - E(DY\mid Z=0)] - [E(Y\mid Z=1) - E(DY\mid Z=1)]$.
Also $(D-1)Y = DY - Y = -(1-D)Y$.
So $E((D-1)Y \mid Z=1) - E((D-1)Y \mid Z=0) = E(DY - Y \mid Z=1) - E(DY - Y \mid Z=0)$
$= [E(DY\mid Z=1) - E(Y\mid Z=1)] - [E(DY\mid Z=0) - E(Y\mid Z=0)]$
$= [E(Y\mid Z=0) - E(DY\mid Z=0)] - [E(Y\mid Z=1) - E(DY\mid Z=1)]$.
This is exactly the identified numerator for $\mu_{0\cp}$.
Thus $\RR_\cp = \frac{E(DY\mid Z=1)-E(DY\mid Z=0)}{E\{(D-1)Y\mid Z=1\}-E\{(D-1)Y\mid Z=0\}}$.

## Problem 22.7: Bounds on the ACE on the whole population

$\delta = \pi_\at(m_{1\at} - m_{0\at}) + \pi_\nt(m_{1\nt} - m_{0\nt}) + \pi_\cp(m_{1\cp} - m_{0\cp})$
Identified terms:
$\pi_\at = \pr(D=1\mid Z=0)$
$\pi_\nt = \pr(D=0\mid Z=1)$
$\pi_\cp = E(D\mid Z=1) - E(D\mid Z=0)$
$m_{1\at} = E(Y \mid Z=0, D=1)$
$m_{0\nt} = E(Y \mid Z=1, D=0)$
$m_{1\cp}, m_{0\cp}$ are identified via Wald-like formulas.
Specifically:
$\pi_\at m_{1\at} = E(DY \mid Z=0)$
$\pi_\nt m_{0\nt} = E((1-D)Y \mid Z=1)$
$\pi_\cp m_{1\cp} = E(DY \mid Z=1) - E(DY \mid Z=0)$
$\pi_\cp m_{0\cp} = E((1-D)Y \mid Z=0) - E((1-D)Y \mid Z=1)$

Substituting into $\delta$:
$\delta = [ \pi_\at m_{1\at} + \pi_\cp m_{1\cp} + \pi_\nt m_{1\nt} ] - [ \pi_\at m_{0\at} + \pi_\cp m_{0\cp} + \pi_\nt m_{0\nt} ]$
The term $\pi_\at m_{1\at} + \pi_\cp m_{1\cp} = E(DY \mid Z=0) + E(DY \mid Z=1) - E(DY \mid Z=0) = E(DY \mid Z=1)$.
The term $\pi_\cp m_{0\cp} + \pi_\nt m_{0\nt} = E((1-D)Y \mid Z=0) - E((1-D)Y \mid Z=1) + E((1-D)Y \mid Z=1) = E((1-D)Y \mid Z=0)$.
So $\delta = [ E(DY \mid Z=1) + \pi_\nt m_{1\nt} ] - [ E((1-D)Y \mid Z=0) + \pi_\at m_{0\at} ]$.
Let $\delta' = E(DY \mid Z=1) - E((1-D)Y \mid Z=0) = E(DY \mid Z=1) - E(Y - DY \mid Z=0)$.
Then $\delta = \delta' + \pi_\nt m_{1\nt} - \pi_\at m_{0\at}$.
Since $m_{1\nt}, m_{0\at} \in [\underline{y}, \overline{y}]$:
Lower bound: $\underline{\delta} = \delta' + \pi_\nt \underline{y} - \pi_\at \overline{y} = \delta' - \overline{y} \pr(D=1\mid Z=0) + \underline{y} \pr(D=0\mid Z=1)$.
Upper bound: $\overline{\delta} = \delta' + \pi_\nt \overline{y} - \pi_\at \underline{y} = \delta' - \underline{y} \pr(D=1\mid Z=0) + \overline{y} \pr(D=0\mid Z=1)$.

## Problem 23.1: More algebra for TSLS

$\hat{D} = Z \hat{\Gamma}$, where $\hat{\Gamma} = (Z^T Z)^{-1} Z^T D$ (standard OLS).
$\hat{\beta}_\TSLS = (\hat{D}^T \hat{D})^{-1} \hat{D}^T Y$.
$\hat{D}^T \hat{D} = (Z \hat{\Gamma})^T (Z \hat{\Gamma}) = \hat{\Gamma}^T Z^T Z \hat{\Gamma} = D^T Z (Z^T Z)^{-1} Z^T Z (Z^T Z)^{-1} Z^T D = D^T Z (Z^T Z)^{-1} Z^T D$.
$\hat{D}^T Y = \hat{\Gamma}^T Z^T Y = D^T Z (Z^T Z)^{-1} Z^T Y$.
In the just-identified case ($Z$ and $D$ have same dimension $k$ and $Z^T Z, Z^T D$ are invertible):
$\hat{\Gamma} = (Z^T Z)^{-1} Z^T D$ is a $k \times k$ matrix.
$\hat{\Gamma}^T = D^T Z (Z^T Z)^{-1}$.
$\hat{D}^T \hat{D} = \hat{\Gamma}^T Z^T Z \hat{\Gamma}$. Since $\hat{\Gamma}$ is invertible, $(\hat{\Gamma}^T Z^T Z \hat{\Gamma})^{-1} = \hat{\Gamma}^{-1} (Z^T Z)^{-1} (\hat{\Gamma}^T)^{-1}$.
$\hat{\beta}_\TSLS = \hat{\Gamma}^{-1} (Z^T Z)^{-1} (\hat{\Gamma}^T)^{-1} \hat{\Gamma}^T Z^T Y = \hat{\Gamma}^{-1} (Z^T Z)^{-1} Z^T Y$.
Substitute $\hat{\Gamma}^{-1} = (Z^T D)^{-1} (Z^T Z)$:
$\hat{\beta}_\TSLS = (Z^T D)^{-1} (Z^T Z) (Z^T Z)^{-1} Z^T Y = (Z^T D)^{-1} Z^T Y = \hat{\beta}_{\textsc{iv}}$.

## Problem 23.3: Control function in the linear IV model

1. $D = \hat{D} + \check{D}$, where $\hat{D} = Z \hat{\Gamma}$.
2. Regress $Y$ on $D$ and $\check{D}$: $Y = D \beta + \check{D} \rho + \text{error}$.
By FWL theorem, the coefficient $\hat{\beta}_{\textsc{cf}}$ is obtained by regressing $Y$ on the residuals of $D$ regressed on $\check{D}$.
But $D = \hat{D} + \check{D}$, and $\hat{D} \perp \check{D}$ by OLS property.
So the residual of $D$ regressed on $\check{D}$ is just $\hat{D}$.
Thus $\hat{\beta}_{\textsc{cf}}$ is the coefficient of $Y$ regressed on $\hat{D}$, which is exactly $\hat{\beta}_\TSLS = (\hat{D}^T \hat{D})^{-1} \hat{D}^T Y$.

## Additional Problem 2: Wald and TSLS

CACE $= \frac{E(Y\mid Z=1)-E(Y\mid Z=0)}{E(D\mid Z=1)-E(D\mid Z=0)}$.
For binary $Z$:
$\cov(Z, Y) = E[ZY] - E[Z]E[Y] = \pr(Z=1)E[Y\mid Z=1] - \pr(Z=1) [ \pr(Z=1)E[Y\mid Z=1] + \pr(Z=0)E[Y\mid Z=0] ]$
$= \pr(Z=1) [ (1 - \pr(Z=1))E[Y\mid Z=1] - \pr(Z=0)E[Y\mid Z=0] ]$
$= \pr(Z=1)\pr(Z=0) [ E[Y\mid Z=1] - E[Y\mid Z=0] ]$.
Similarly, $\cov(Z, D) = \pr(Z=1)\pr(Z=0) [ E[D\mid Z=1] - E[D\mid Z=0] ]$.
Thus $\frac{\cov(Z, Y)}{\cov(Z, D)} = \frac{E(Y\mid Z=1)-E(Y\mid Z=0)}{E(D\mid Z=1)-E(D\mid Z=0)} = \text{CACE}$.
In linear IV model $Y = \beta D + U$, if $\cov(Z, U) = 0$, then $\cov(Z, Y) = \beta \cov(Z, D) + \cov(Z, U) = \beta \cov(Z, D)$.
So $\beta = \frac{\cov(Z, Y)}{\cov(Z, D)}$.
