# INTRODUCTION TO MULTI-PARAMETER MODELS CHAPTER 3

AVERAGING OVER NUISANCE PARAMETERS   
2 NORMAL DATA WITH A NONINFORMATIVE PRIOR DISTRIBUTION   
3 NORMAL DATA WITH A CONJUGATE PRIOR DISTRIBUTION   
4 MULTINOMIAL MODEL FOR CATEGORICAL DATA   
5 MULTIVARIATE NORMAL MODEL WITH KNOWN VARIANCE   
6 MULTIVARIATE NORMAL WITH UNKNOWN MEAN AND VARIANCE   
EXAMPLE: ANALYSIS OF A BIOASSAY EXPERIMENT   
SUMMARY OF ELEMENTARY MODELING AND COMPUTATION

# AVERAGING OVER NUISANCE PARAMETERS

To express the ideas of joint and marginal posterior distributions mathematically, suppose $\theta$ has two parts, each of which can be a vector, $\theta = (\theta_{1},\theta_{2})$ , and further suppose that we are only interested (at least for the moment) in inference for $\theta_{1}$ , so $\theta_{2}$ may be considered a nuisance parameter.

For instance, in the simple example,

$$
y | \mu , \sigma^ {2} \sim N (\mu , \sigma^ {2}),
$$

in which both $\mu = \theta_{1}$ and $\sigma^2 = \theta_2$ are unknown, interest commonly centers on $\mu$ .

We seek the conditional distribution of the parameter of interest given the observed data; in this case, $p(\theta_1|y)$ .

This is derived from the joint posterior density,

$$
p \left(\theta_ {1}, \theta_ {2} \mid y\right) \propto p \left(y \mid \theta_ {1}, \theta_ {2}\right) \times p \left(\theta_ {1}, \theta_ {2}\right),
$$

by averaging over $\theta_{2}$ :

$$
p (\theta_ {1} | y) = \int p (\theta_ {1}, \theta_ {2} | y) d \theta_ {2}.
$$

Alternatively, the joint posterior density can be factored to yield

$$
p \left(\theta_ {1} | y\right) = \int p \left(\theta_ {1} \mid \theta_ {2}, y\right) \times p \left(\theta_ {2} \mid y\right) d \theta_ {2}.
$$

It shows that the posterior distribution of interest, $p(\theta_1|y)$ , is a mixture of the conditional posterior distributions given the nuisance parameter, $\theta_2$ , where $p(\theta_2|y)$ is a weighting function for the different possible values of $\theta_2$ .

The weights depend on the posterior density of $\theta_{2}$ and thus on a combination of evidence from data and prior model.

The averaging over nuisance parameters $\theta_{2}$ can be interpreted generally.

For example, $\theta_{2}$ can include a discrete component representing different possible sub-models.

We rarely evaluate the integral explicitly, but it suggests an important practical strategy for both constructing and computing with multi-parameter models.

Posterior distributions can be computed by marginal and conditional simulation, first drawing $\theta_{2}$ from its marginal posterior distribution and then $\theta_{1}$ from its conditional posterior distribution, given the drawn value of $\theta_{2}$ .

In this way the integration is performed indirectly.

A canonical example of this form of analysis is provided by the normal model with unknown mean and variance.

1 AVERAGING OVER NUISANCE PARAMETERS   
NORMAL DATA WITH A NONINFORMATIVE PRIOR DISTRIBUTION   
3 NORMAL DATA WITH A CONJUGATE PRIOR DISTRIBUTION   
4 MULTINOMIAL MODEL FOR CATEGORICAL DATA   
5 MULTIVARIATE NORMAL MODEL WITH KNOWN VARIANCE   
6 MULTIVARIATE NORMAL WITH UNKNOWN MEAN AND VARIANCE   
EXAMPLE: ANALYSIS OF A BIOASSAY EXPERIMENT   
SUMMARY OF ELEMENTARY MODELING AND COMPUTATION

# NORMAL DATA WITH A NONINFORMATIVE PRIOR DISTRIBUTION

As the prototype example of estimating the mean of a population from a sample, we consider a vector $y$ of $n$ independent observations from a univariate normal distribution, $N(\mu, \sigma^2)$ .

We begin by analyzing the model under a noninformative prior distribution, with the understanding that this is no more than a convenient assumption for the purposes of exposition and is easily extended to informative prior distributions.

# A NONINFORMATIVE PRIOR DISTRIBUTION

A sensible vague prior density for $\mu$ and $\sigma^2$ , assuming prior independence of location and scale parameters, is uniform on $(\mu, \log \sigma^2)$ or, equivalently,

$$
p (\boldsymbol {\mu}, \sigma^ {2}) \propto (\sigma^ {2}) ^ {- 1}.
$$

# THE JOINT POSTERIOR DISTRIBUTION, $p(\mu ,\sigma^2 |y)$

Under this conventional improper prior density, the joint posterior distribution is proportional to the likelihood function multiplied by the factor $1 / \sigma^2$ :

$$
\begin{array}{l} p (\mu , \sigma^ {2} | y) \propto (\sigma^ {2}) ^ {- (n / 2 + 1)} \exp \left\{- \frac {1}{2 \sigma^ {2}} \sum_ {i = 1} ^ {n} (y _ {i} - \mu) ^ {2} \right\} \\ = (\sigma^ {2}) ^ {- (n / 2 + 1)} \exp \left\{- \frac {1}{2 \sigma^ {2}} \Big [ \sum_ {i = 1} ^ {n} (y _ {i} - \bar {y}) ^ {2} + n (\bar {y} - \mu) ^ {2} \Big ] \right\} \\ = (\sigma^ {2}) ^ {- (n / 2 + 1)} \exp \left\{- \frac {1}{2 \sigma^ {2}} \left[ (n - 1) s ^ {2} + n (\bar {y} - \mu) ^ {2} \right] \right\}. \\ \end{array}
$$

# NOTE

The sufficient statistics are $\bar{y}$ and $s^2$

# THE CONDITIONAL POSTERIOR DISTRIBUTION,

$$
p (\mu | \sigma^ {2}, y)
$$

In order to factor the joint posterior density, we consider first the conditional posterior density, $p(\mu | \sigma^2, y)$ , and then the marginal posterior density, $p(\sigma^2 | y)$ .

To determine the posterior distribution of $\mu$ , given $\sigma^2$ , we simply use the result derived in Chapter 2 for the mean of a normal distribution with known variance and a uniform prior distribution:

$$
\mu | \sigma^ {2}, y \sim N (\bar {y}, \sigma^ {2} / n).
$$

# THE MARGINAL POSTERIOR DISTRIBUTION, $p(\sigma^2 | y)$

To determine $p(\sigma^2 |y)$ , we must average the joint distribution $p(\mu, \sigma^2 | y)$ over $\mu$ :

$$
p \left(\sigma^ {2} | y\right) \propto \int \left(\sigma^ {2}\right) ^ {- (n / 2 + 1)} \exp \left\{- \frac {1}{2 \sigma^ {2}} \left[ (n - 1) s ^ {2} + n (\bar {y} - \mu) ^ {2} \right] \right\} d \mu .
$$

Integrating this expression over $\mu$ requires evaluating the integral

$$
\int \exp \left\{- \frac {1}{2 (\sigma^ {2} / n)} (\bar {y} - \mu) ^ {2} \right\} d \mu .
$$

# NOTE

It is a simple normal integral which yields

$$
\sqrt {2 \pi \sigma^ {2} / n}.
$$

Thus,

$$
p (\sigma^ {2} | y) \propto (\sigma^ {2}) ^ {- (n / 2 + 1)} \exp \left\{- \frac {1}{2 \sigma^ {2}} \Big [ (n - 1) s ^ {2} \Big ] \right\} \times \sqrt {2 \pi \sigma^ {2} / n}
$$

$$
\propto \left(\sigma^ {2}\right) ^ {- \left[ (n - 1) / 2 + 1 \right]} \exp \left\{- \frac {1}{2 \sigma^ {2}} \left[ (n - 1) s ^ {2} \right] \right\}.
$$

# NOTE

It is a scale inverse- $\chi^2$ density:

$$
\sigma^ {2} | y \sim \operatorname {I n v} - \chi^ {2} (n - 1, s ^ {2}).
$$

# SCALE INVERSE- $\chi^2$ DENSITY

$$
p (x | \nu , \sigma^ {2}) = \frac {(\nu \sigma^ {2} / 2) ^ {\nu / 2}}{\Gamma (\nu / 2)} x ^ {- (\nu / 2 + 1)} \exp \left(- \frac {\nu \sigma^ {2}}{2 x}\right).
$$

$\nu$ : the degrees of freedom;

$\sigma^2$ : the scale parameter.

# RELATED DISTRIBUTIONS

- If $X \sim \chi^2(\nu)$ and $Y = 1 / X$ , then $Y \sim \operatorname{Inv} - \chi^2(\nu)$ (inverse- $\chi^2$ distribution).   
- $\operatorname{Inv} - \chi^2(\nu) \doteq \operatorname{Inv} - \chi^2(\nu, 1/\nu)$ .   
- If $Y \sim \operatorname{Inv} - \chi^2(\nu, 1 / \nu)$ and $Z = \nu \sigma^2 X$ , then $Z \sim \operatorname{Inv} - \chi^2(\nu, \sigma^2)$ (scale inverse- $\chi^2$ distribution).

# WIKI

- Chi-squared distribution:

https://en.wikipedia.org/wiki/Chi-squared_distribution

- Inverse-chi-squared distribution:

https://en.wikipedia.org/wiki/Inverse-chi-squared_distribution

- Scaled inverse chi-squared distribution:

https://en.wikipedia.org/wiki/Scaled_inverse_chi-squared_distribution

# NOTE

$$
\begin{array}{l} \sigma^ {2} | y \sim \operatorname {I n v} - \chi^ {2} (n - 1, s ^ {2}) \\ \Rightarrow \frac {\sigma^ {2}}{(n - 1) s ^ {2}} \Bigg | y \sim \mathrm {I n v} - \chi^ {2} (n - 1) \doteq \mathrm {I n v} - \chi^ {2} \left(n - 1, \frac {1}{n - 1}\right) \\ \Rightarrow \frac {(n - 1) s ^ {2}}{\sigma^ {2}} \Bigg | y \sim \chi^ {2} (n - 1) \\ \end{array}
$$

This marginal posterior distribution for $\sigma^2$ has a remarkable similarity to the analogous sampling theory result.

Conditional on $\sigma^2$ (and $\mu$ ), the distribution of the appropriately scaled sufficient statistic,

$$
\frac {(n - 1) s ^ {2}}{\sigma^ {2}} \sim \chi_ {n - 1} ^ {2}.
$$

# SAMPLING FROM THE JOINT POSTERIOR

# DISTRIBUTION

It is easy to draw samples from the joint posterior distribution:

1. draw $\sigma^2$ from the marginal posterior distribution, $p(\sigma^2 |y)$   
2. draw $\mu$ from the conditional posterior distribution, $p(\mu |\sigma^2,y)$

We also derive some analytical results for the posterior distribution, since this is one of the few multi-parameter problems simple enough to solve in closed form.

# ANALYTIC FORM OF THE MARGINAL POSTERIOR DISTRIBUTION OF $\mu$

The population mean, $\mu$ , is typically the estimand of interest, and so the objective of the Bayesian analysis is the marginal posterior distribution of $\mu$ , which can be obtained by integrating $\sigma^2$ out of the joint posterior distribution.

The representation of joint posterior distribution shows that the posterior distribution of $\mu$ can be regarded as a mixture of normal distributions, mixed over the scaled inverse- $\chi^2$ distribution for the variance, $\sigma^2$ .

We can derive the marginal posterior density for $\mu$ by integrating the joint posterior density over $\sigma^2$ :

$$
p (\mu | y) = \int_ {0} ^ {\infty} p (\mu , \sigma^ {2} | y) d \sigma^ {2}.
$$

# NOTE

$$
p (\mu , \sigma^ {2}) \propto (\sigma^ {2}) ^ {- (n / 2 + 1)} \exp \left\{- \frac {1}{2 \sigma^ {2}} \left[ (n - 1) s ^ {2} + n (\bar {y} - \mu) ^ {2} \right] \right\}.
$$

This integral can be evaluated using the substitution

$$
z = \frac {A}{2 \sigma^ {2}}, \quad A = (n - 1) s ^ {2} + n (\mu - \bar {y}) ^ {2},
$$

and recognizing that the result is an unnormalized gamma integral.

$$
\begin{array}{l} p (\mu | y) \propto \int_ {0} ^ {\infty} \left(\sigma^ {2}\right) ^ {- (n / 2 + 1)} \exp \left\{- \frac {1}{2 \sigma^ {2}} \left[ (n - 1) s ^ {2} + n (\bar {y} - \mu) ^ {2} \right] \right\} d \sigma^ {2} \\ = \int_ {0} ^ {\infty} \left(\sigma^ {2}\right) ^ {- (n / 2 + 1)} \exp \left\{- \frac {A}{2 \sigma^ {2}} \right\} d \sigma^ {2} \quad z = \frac {A}{2 \sigma^ {2}}, \sigma^ {2} = \frac {A}{2} z ^ {- 1} \\ = \int_ {\infty} ^ {0} \left(\frac {2 z}{A}\right) ^ {(n / 2 + 1)} \exp (- z) \left(- \frac {A}{2} z ^ {- 2}\right) d z \quad d \sigma^ {2} = - \frac {A}{2} z ^ {- 2} \\ \propto A ^ {- n / 2} \times \int_ {0} ^ {\infty} z ^ {n / 2 - 1} \exp (- z) d z \\ \propto \left[ (n - 1) s ^ {2} + n (\mu - \bar {y}) ^ {2} \right] ^ {- n / 2} \propto \left[ 1 + \frac {n (\mu - \bar {y}) ^ {2}}{(n - 1) s ^ {2}} \right] ^ {- n / 2}. \\ \end{array}
$$

This is the $t_{n - 1}(\bar{y},s^2 /n)$ density.

# GENERAL $t$ DISTRIBUTION

$$
p (x | \nu , \mu , \sigma) = \frac {\Gamma ((v + 1) / 2)}{\Gamma (v / 2) \sqrt {\pi \nu} \sigma} \left[ 1 + \frac {1}{\nu} \frac {(x - \mu) ^ {2}}{\sigma^ {2}} \right] ^ {- (\nu + 1) / 2}.
$$

$\nu$ degrees of freedom;   
$\mu$ : mean;   
$\sigma$ : simply sets the overall scaling of the distribution. (It does not correspond to a standard deviation: it is not the standard deviation of the scaled $t$ distribution, which may not even exist; nor is it the standard deviation of the underlying normal distribution, which is unknown.)

# RELATED DISTRIBUTIONS

- If $X \sim t_{\nu}$ and $Y = \sigma X + \mu$ , then $Y \sim t_{\nu}(\mu, \sigma^2)$ (general $t$ distribution).   
$t_{\nu}\dot{=} t_{\nu}(0,1).$

# WIKI

$t$ distribution:

https://en.wikipedia.org/wiki/Student%27s_t-distribution

# NOTE

To put it another way, we have shown that, under the noninformative uniform prior distribution on $(\mu, \log \sigma^2)$ , the posterior distribution of $\mu$ has the form

$$
\begin{array}{l} \mu \big | y \sim t _ {n - 1} (\bar {y}, s ^ {2} / n) \\ \Rightarrow \frac {\mu - \bar {y}}{s / \sqrt {n}} \Bigg | y \sim t _ {n - 1} \doteq t _ {n - 1} (0, 1). \\ \end{array}
$$

This marginal posterior distribution provides another interesting comparison with sampling theory.

Under the sampling distribution, $p(y|\mu ,\sigma^2)$ , the following relation holds:

$$
\frac {\bar {y} - \mu}{s / \sqrt {n}} \Big | \mu , \sigma^ {2} \sim t _ {n - 1}.
$$

The sampling distribution of the pivotal quantity $\frac{\bar{y} - \mu}{s / \sqrt{n}}$ does not depend on the nuisance parameter $\sigma^2$ , and its posterior distribution does not depend on data.

In general, a pivotal quantity for the estimand is defined as a nontrivial function of the data and the estimand whose sampling distribution is independent of all parameters and data.

# POSTERIOR PREDICTIVE DISTRIBUTION FOR A FUTURE OBSERVATION

The posterior predictive distribution for a future observation, $\tilde{y}$ can be written as a mixture,

$$
\begin{array}{l} p (\tilde {y} | y) = \int \int p (\tilde {y} | \mu , \sigma^ {2}, y) \times p (\mu , \sigma^ {2} | y) d \mu d \sigma^ {2} \\ = \int \int p (\tilde {y} | \mu , \sigma^ {2}) \times p (\mu , \sigma^ {2} | y) d \mu d \sigma^ {2}. \\ \end{array}
$$

The first of the two factors in the integral is just the normal distribution for the future observation given the values of $(\mu, \sigma^2)$ , and does not depend on $y$ at all.

To draw from the posterior predictive distribution, first draw $\mu$ , $\sigma^2$ from their joint posterior distribution and then simulate $\tilde{y} \sim N(\mu, \sigma^2)$ .

In fact, the posterior predictive distribution of $\tilde{y}$ is a $t$ distribution with location $\bar{y}$ , scale $\sqrt{(1 + 1/n)s^2}$ , and $n - 1$ degrees of freedom.

This analytic form is obtained using the same techniques as in the derivation of the posterior distribution of $\mu$ .

Specifically, the distribution can be obtained by integrating out the parameters $\mu$ , $\sigma^2$ according to their joint posterior distribution.

We can identify the result more easily by noticing that the factorization

$$
p (\tilde {y} | \sigma^ {2}, y) = \int p (\tilde {y} | \mu , \sigma^ {2}, y) \times p (\mu | \sigma^ {2}, y) d \mu
$$

$$
\Longrightarrow \tilde {y} | \sigma^ {2}, y \sim N \big (\bar {y}, (1 + 1 / n) \sigma^ {2} \big).
$$

# NOTE

$(\tilde{y}|\sigma^2, y)$ is the same, up to a changed scale factor, as the distribution of $(\mu|\sigma^2, y) \sim N(\bar{y}, \sigma^2/n)$ .

# EXAMPLE: ESTIMATING THE SPEED OF LIGHT

See the textbook.

1 AVERAGING OVER NUISANCE PARAMETERS   
2 NORMAL DATA WITH A NONINFORMATIVE PRIOR DISTRIBUTION   
3 NORMAL DATA WITH A CONJUGATE PRIOR DISTRIBUTION   
4 MULTINOMIAL MODEL FOR CATEGORICAL DATA   
5 MULTIVARIATE NORMAL MODEL WITH KNOWN VARIANCE   
6 MULTIVARIATE NORMAL WITH UNKNOWN MEAN AND VARIANCE   
EXAMPLE: ANALYSIS OF A BIOASSAY EXPERIMENT   
SUMMARY OF ELEMENTARY MODELING AND COMPUTATION

# A FAMILY OF CONJUGATE PRIOR DISTRIBUTIONS

A first step toward a more general model is to assume a conjugate prior distribution for the two-parameter univariate normal sampling model in place of the noninformative prior distribution just considered.

The form of the likelihood of normal sampling model and the subsequent discussion shows that the conjugate prior density must also have the product form $p(\sigma^2) \times p(\mu | \sigma^2)$ ,

the marginal distribution of $\sigma^2$ is scaled inverse- $\chi^2$   
- the conditional distribution of $\mu$ given $\sigma^2$ is normal (so that marginally $\mu$ has a $t$ distribution).

A convenient parameterization is given by the following specification:

$$
\mu | \sigma^ {2} \sim N (\mu_ {0}, \sigma^ {2} / \kappa_ {0}), \quad \sigma^ {2} \sim \operatorname {I n v} - \chi^ {2} (\nu_ {0}, \sigma_ {0} ^ {2}),
$$

which corresponds to the joint prior density $N\text{-Inv - }\chi^2 (\mu_0,\sigma^2 /\kappa_0,\nu_0,\sigma_0^2)$ density.

Four hyperparameters can be identified as the location and scale of $\mu$ and the degrees of freedom and scale of $\sigma^2$ , respectively.

The appearance of $\sigma^2$ in the conditional distribution of $\mu |\sigma^2$ means that $\mu$ and $\sigma^2$ are necessarily dependent in their joint conjugate prior density.

For example, if $\sigma^2$ is large, then a high-variance prior distribution is induced on $\mu$ .

This dependence is notable, considering that conjugate prior distributions are used largely for convenience.

Upon reflection, however, it often makes sense for the prior variance of the mean to be tied to $\sigma^2$ , which is the sampling variance of the observation $y$ .

In this way, prior belief about $\mu$ is calibrated by the scale of measurement of $y$ and is equivalent to $\kappa_0$ prior measurements on this scale.

# THE JOINT POSTERIOR DISTRIBUTION, $p(\mu ,\sigma^2 |y)$

Multiplying the prior density by the normal likelihood yields the posterior density

$$
= N - \operatorname {I n v} - \chi^ {2} \left(\mu_ {n}, \sigma_ {n} ^ {2} / \kappa_ {n}; \nu_ {n}, \sigma_ {n} ^ {2}\right).
$$

$$
\begin{array}{l} p (\mu , \sigma^ {2} | y) \propto (\sigma^ {2}) ^ {- 1 / 2} \times (\sigma^ {2}) ^ {- (\nu_ {0} / 2 + 1)} \exp \left\{- \frac {1}{2 \sigma^ {2}} \left[ \nu_ {0} \sigma_ {0} ^ {2} + \kappa_ {0} (\mu - \mu_ {0}) ^ {2} \right] \right\} \\ \times \left(\sigma^ {2}\right) ^ {- n / 2} \exp \left\{- \frac {1}{2 \sigma^ {2}} \left[ (n - 1) s ^ {2} + n (\bar {y} - \mu) ^ {2} \right] \right\} \\ \end{array}
$$

The parameters of the posterior distribution combine the prior information and the information contained in the data, as follows:

$$
\mu_ {n} = \frac {\kappa_ {0}}{\kappa_ {0} + n} \mu_ {0} + \frac {n}{\kappa_ {0} + n} \overline {{y}},
$$

$$
\kappa_ {n} = \kappa_ {0} + n,
$$

$$
\nu_ {n} = \nu_ {0} + n,
$$

$$
\nu_ {n} \sigma_ {n} ^ {2} = \nu_ {0} \sigma_ {0} ^ {2} + (n - 1) s ^ {2} + \frac {\kappa_ {0} n}{\kappa_ {n}} (\bar {y} - \mu_ {0}) ^ {2}.
$$

# THE CONDITIONAL POSTERIOR DISTRIBUTION,

$$
p (\mu | \sigma^ {2}, y)
$$

The conditional posterior density of $\mu$ , given $\sigma^2$ , is proportional to the joint posterior density with $\sigma^2$ held constant,

$$
\mu | \sigma^ {2}, y \sim N (\mu_ {n}, \sigma^ {2} / \kappa_ {n})
$$

which agrees, as it must, with the analysis of $\mu$ with $\sigma^2$ considered fixed (known).

# THE MARGINAL POSTERIOR DISTRIBUTION, $p(\sigma^2 | y)$

The marginal posterior density of $\sigma^2$ is scaled inverse- $\chi^2$ :

$$
\sigma^ {2} | y \sim \operatorname {I n v} - \chi^ {2} \left(\nu_ {n}, \sigma_ {n} ^ {2}\right).
$$

# SAMPLING FROM THE JOINT POSTERIOR

# DISTRIBUTION

To sample from the joint posterior distribution, just as in the previous section,

1. first draw $\sigma^2$ from its marginal posterior distribution,   
2. then draw $\mu$ from its normal conditional posterior distribution, using the simulated value of $\sigma^2$ in Step 1.

# ANALYTIC FORM OF THE MARGINAL POSTERIOR DISTRIBUTION OF $\mu$

Integration of the joint posterior density with respect to $\sigma^2$ , in a precisely analogous way to that used in the previous section, shows that the marginal posterior density for $\mu$ is

$$
\mu | y \sim t _ {\nu_ {n}} (\mu_ {n}, \sigma_ {n} ^ {2} / \kappa_ {n}).
$$

1 AVERAGING OVER NUISANCE PARAMETERS   
NORMAL DATA WITH A NONINFORMATIVE PRIOR DISTRIBUTION   
3 NORMAL DATA WITH A CONJUGATE PRIOR DISTRIBUTION   
4 MULTINOMIAL MODEL FOR CATEGORICAL DATA   
5 MULTIVARIATE NORMAL MODEL WITH KNOWN VARIANCE   
6 MULTIVARIATE NORMAL WITH UNKNOWN MEAN AND VARIANCE   
EXAMPLE: ANALYSIS OF A BIOASSAY EXPERIMENT   
SUMMARY OF ELEMENTARY MODELING AND COMPUTATION

# MULTINOMIAL MODEL FOR CATEGORICAL DATA

The multinomial sampling distribution is used to describe data for which each observation is one of $k$ possible outcomes.

If $y$ is the vector of counts of the number of observations of each outcome, then

$$
p (y | \theta) \propto \prod_ {j = 1} ^ {k} \theta_ {j} ^ {y _ {j}}, \quad \sum_ {j = 1} ^ {k} \theta_ {j} = 1.
$$

# NOTE

The distribution is typically thought of as implicitly conditioning on the number of observations, $\sum_{j=1}^{k} y_{j} = n$ .

The conjugate prior distribution is a multivariate generalization of the beta distribution known as the Dirichlet,

$$
p (\theta | \alpha) \propto \prod_ {j = 1} ^ {k} \theta_ {j} ^ {\alpha_ {j} - 1},
$$

where the distribution is restricted to nonnegative $\theta_{j}$ 's with $\sum_{j=1}^{k} \theta_{j} = 1$ .

The resulting posterior distribution for the $\theta_{j}$ 's is Dirichlet with parameters $\alpha_{j} + y_{j}$ .

The prior distribution is mathematically equivalent to a likelihood resulting from $\sum_{j=1}^{k} \alpha_{j}$ observations with $\alpha_{j}$ observations of the $j$ th outcome category.

- A uniform density is obtained by setting $\alpha_{j} = 1$ for all $j$ ; this distribution assigns equal density to any vector $\theta$ satisfying $\sum_{j=1}^{k} \theta_{j} = 1$ .   
- Setting $\alpha_{j} = 0$ for all $j$ results in an improper prior distribution that is uniform in the $\log (\theta_j)$ 's. The resulting posterior distribution is proper if there is at least one observation in each of the $k$ categories, so that each component of $y$ is positive.

# EXAMPLE: PRE-ELECTION POLLING

See the textbook.

1 AVERAGING OVER NUISANCE PARAMETERS   
2 NORMAL DATA WITH A NONINFORMATIVE PRIOR DISTRIBUTION   
3 NORMAL DATA WITH A CONJUGATE PRIOR DISTRIBUTION   
4 MULTINOMIAL MODEL FOR CATEGORICAL DATA   
5 MULTIVARIATE NORMAL MODEL WITH KNOWN VARIANCE   
6 MULTIVARIATE NORMAL WITH UNKNOWN MEAN AND VARIANCE   
EXAMPLE: ANALYSIS OF A BIOASSAY EXPERIMENT   
SUMMARY OF ELEMENTARY MODELING AND COMPUTATION

# MULTIVARIATE NORMAL LIKELIHOOD

The likelihood function of multivariate normal model, $N(\mu, \Sigma)$ , for a single observation is

$$
p \big (y | \mu , \Sigma \big) \propto | \Sigma | ^ {- 1 / 2} \exp \left\{- \frac {1}{2} \big (y - \mu \big) ^ {T} \Sigma^ {- 1} \big (y - \mu \big) \right\}.
$$

For a sample of $n$ independent and identically distributed observations, $y_{1},\ldots ,y_{n}$ , is

$$
p \left(y _ {1}, \dots , y _ {n} \mid \mu , \Sigma\right) \propto | \Sigma | ^ {- n / 2} \exp \left\{- \frac {1}{2} \sum_ {i = 1} ^ {n} \left(y _ {i} - \mu\right) ^ {T} \Sigma^ {- 1} \left(y _ {i} - \mu\right) \right\}
$$

$$
= | \Sigma | ^ {- n / 2} \exp \left\{- \frac {1}{2} \operatorname {t r} \left(\Sigma^ {- 1} S _ {0}\right) \right\}.
$$

- $S_0 = \sum_{i=1}^{n} (y_i - \mu)(y_i - \mu)^T$ is the matrix of sums of squares relative to $\mu$ .

# CONJUGATE PRIOR DISTRIBUTION FOR $\mu$ WITH KNOWN $\Sigma$

The log-likelihood is a quadratic form in $\mu$ , and therefore the conjugate prior distribution for $\mu$ is the multivariate normal distribution, which we parameterize as $\mu \sim N(\mu_0, \Lambda_0)$ .

# POSTERIOR DISTRIBUTION FOR $\mu$ WITH KNOWN $\Sigma$

The posterior distribution of $\mu$ is

$$
p (\mu | y, \Sigma) \propto \exp \left\{- \frac {1}{2} \left[ (\mu - \mu_ {0}) ^ {T} \Lambda_ {0} ^ {- 1} (\mu - \mu_ {0}) + \sum_ {i = 1} ^ {n} (y _ {i} - \mu) ^ {T} \Sigma^ {- 1} (y _ {i} - \mu) \right] \right\},
$$

which is an exponential of a quadratic form in $\mu$ .

Completing the quadratic form and pulling out constant factors gives

$$
p (\mu | y, \Sigma) = \mathcal {N} (\mu | \mu_ {n}, \Lambda_ {n}),
$$

$$
\mu_ {n} = \big (\Lambda_ {0} ^ {- 1} + n \Sigma^ {- 1} \big) ^ {- 1} \big (\Lambda_ {0} ^ {- 1} \mu_ {0} + n \Sigma^ {- 1} \bar {y} \big),
$$

$$
\Lambda_ {n} ^ {- 1} = \Lambda_ {0} ^ {- 1} + n \Sigma^ {- 1}.
$$

# REMARKS

These are similar to the results for the univariate normal model,

- the posterior mean being a weighted average of the data and the prior mean, with weights given by the data and prior precision matrices, $n\Sigma^{-1}$ and $\Lambda_0^{-1}$ , respectively;   
- the posterior precision is the sum of the prior and data precisions.

# POSTERIOR PREDICTIVE DISTRIBUTION FOR NEW DATA

We now work out the analytic form of the posterior predictive distribution for a new observation $\tilde{y} \sim N(\mu, \Sigma)$ .

As with the univariate normal, we first note that the joint distribution, $p(\tilde{y}, \mu | y) = N(\tilde{y} | \mu, \Sigma) N(\mu | \mu_n, \Lambda_n)$ , is the exponential of a quadratic form in $(\tilde{y}, \mu)$ .

Hence $(\tilde{y}, \mu)$ have a joint normal posterior distribution, and so the marginal posterior distribution of $\tilde{y}$ is (multivariate) normal.

As in the univariate case, we can determine the posterior mean and variance of $\tilde{y}$ as follows:

$$
\mathsf {E} (\tilde {y} | y) = \mathsf {E} \bigl (\mathsf {E} (\tilde {y} | \mu , y) | y \bigr) = \mathsf {E} (\mu | y) = \mu_ {n},
$$

$$
\begin{array}{l} \operatorname {V a r} (\tilde {y} | y) = \operatorname {E} \left(\operatorname {V a r} (\tilde {y} | \mu , y) | y\right) + \operatorname {V a r} \left(\operatorname {E} (\tilde {y} | \mu , y) | y\right) \\ = \operatorname {E} (\Sigma | y) + \operatorname {V a r} (\mu | y) = \Sigma + \Lambda_ {n}. \\ \end{array}
$$

# NONINFORMATIVE PRIOR DENSITY FOR $\mu$

A noninformative uniform prior density for $\mu$ is $p(\mu) \propto \text{constant}$ , obtained in the limit as the prior precision tends to zero in the sense $|\Lambda_0^{-1}| \to 0$ ; in the limit of infinite prior variance (zero prior precision), the prior mean is irrelevant.

The posterior density is then proportional to the likelihood.

This is a proper posterior distribution only if $n \geq d$ , that is, if the sample size is greater than or equal to the dimension of the multivariate normal; otherwise the matrix $S_0$ is not full rank.

If $n \geq d$ , the posterior distribution for $\mu$ , given the uniform prior density, is $\mu |\Sigma, y \sim N(\bar{y}, \Sigma / n)$ .

1 AVERAGING OVER NUISANCE PARAMETERS   
2 NORMAL DATA WITH A NONINFORMATIVE PRIOR DISTRIBUTION   
3 NORMAL DATA WITH A CONJUGATE PRIOR DISTRIBUTION   
4 MULTINOMIAL MODEL FOR CATEGORICAL DATA   
5 MULTIVARIATE NORMAL MODEL WITH KNOWN VARIANCE   
6 MULTIVARIATE NORMAL WITH UNKNOWN MEAN AND VARIANCE   
EXAMPLE: ANALYSIS OF A BIOASSAY EXPERIMENT   
SUMMARY OF ELEMENTARY MODELING AND COMPUTATION

# CONJUGATE INVERSE-WISHART FAMILY OF PRIOR DISTRIBUTIONS

The conjugate prior distribution for $(\mu, \Sigma)$ , the normal-inverse-Wishart, is conveniently parameterized in terms of hyperparameters $(\mu_0, \Lambda_0 / \kappa_0; \nu_0, \Lambda_0)$ :

$$
\Sigma \sim \operatorname {I n v - W i s h a r t} _ {\nu_ {0}} \left(\Lambda_ {0} ^ {- 1}\right), \quad \mu | \Sigma \sim N \left(\mu_ {0}, \Sigma / \kappa_ {0}\right),
$$

which corresponds to the joint prior density

$$
p (\boldsymbol {\mu}, \boldsymbol {\Sigma}) \propto | \boldsymbol {\Sigma} | ^ {- (\frac {\nu_ {0} + d}{2} + 1)} \exp \left\{- \frac {1}{2} \mathrm {t r} (\boldsymbol {\Lambda} _ {0} \boldsymbol {\Sigma} ^ {- 1}) - \frac {\kappa_ {0}}{2} (\boldsymbol {\mu} - \boldsymbol {\mu} _ {0}) ^ {T} \boldsymbol {\Sigma} ^ {- 1} (\boldsymbol {\mu} - \boldsymbol {\mu} _ {0}) \right\}.
$$

The parameters $\nu_0$ and $\Lambda_0$ describe the degrees of freedom and the scale matrix for the inverse-Wishart distribution on $\Sigma$ .

The remaining parameters are the prior mean, $\mu_0$ , and the number of prior measurements, $\kappa_0$ , on the $\Sigma$ scale.

# POSTERIOR DISTRIBUTION

Multiplying the prior density by the normal likelihood results in a posterior density of the same family with parameters

$$
\mu_ {n} = \frac {\kappa_ {0}}{\kappa_ {0} + n} \mu_ {0} + \frac {n}{\kappa_ {0} + n} \bar {y},
$$

$$
\kappa_ {n} = \kappa_ {0} + n, \quad \nu_ {n} = \nu_ {0} + n,
$$

$$
\Lambda_ {n} = \Lambda_ {0} + S + \frac {\kappa_ {0} n}{\kappa_ {0} + n} (\bar {y} - \mu_ {0}) (\bar {y} - \mu_ {0}) ^ {T},
$$

$$
S = \sum_ {i = 1} ^ {n} (y _ {i} - \bar {y}) (y _ {i} - \bar {y}) ^ {T}.
$$

# OTHER RESULTS

The marginal posterior distribution of $\mu$ is multivariate $t$ distribution:

$$
t _ {\nu_ {n} - d + 1} \left(\mu_ {n}, \frac {\Lambda_ {n}}{\kappa_ {n} (\nu_ {n} - d + 1)}\right).
$$

The posterior predictive distribution of a new observation $\tilde{y}$ is also multivariate $t$ with an additional factor of $\kappa_{n} + 1$ in the numerator of the scale matrix.

Samples from the joint posterior distribution of $(\mu, \Sigma)$ are easily obtained using the following procedure:

1. first draw $\Sigma |y\sim \mathrm{Inv - Wishart}_{\nu_n}(\Lambda_n^{-1})$   
2. the draw $\mu |\Sigma ,y\sim N(\mu_n,\Sigma /\kappa_n)$

To draw from the posterior predictive distribution of a new observation,

1. first draw $(\mu, \Sigma)$ from the posterior distribution by the above procedure,   
2. then draw $\tilde{y}|\mu, \Sigma, y \sim \mathcal{N}(\mu, \Sigma)$ given the already drawn values of $\mu$ and $\Sigma$ .

# DIFFERENT NONINFORMATIVE PRIOR DISTRIBUTIONS

Setting $\Sigma \sim \operatorname{Inv-Wishart}_{d+1}(I)$ has the appealing feature that each of the correlations in $\Sigma$ has, marginally, a uniform prior distribution.

# NOTE

The joint distribution is not uniform, however, because of the constraint that the correlation matrix be positive definite.

Another proposed noninformative prior distribution is the multivariate Jeffreys prior density,

$$
p (\mu , \Sigma) \propto | \Sigma | ^ {- (d + 1) / 2},
$$

which is the limit of the conjugate prior density as $\kappa_0\to 0$ $\nu_{0}\rightarrow -1$ $|\Lambda_0|\to 0$

The corresponding posterior distribution can be written as

$$
\Sigma | y \sim \operatorname {I n v - W i s h a r t} _ {n - 1} (S ^ {- 1}), \quad \mu | \Sigma , y \sim N (\bar {y}, \Sigma / n).
$$

1 AVERAGING OVER NUISANCE PARAMETERS   
NORMAL DATA WITH A NONINFORMATIVE PRIOR DISTRIBUTION   
3 NORMAL DATA WITH A CONJUGATE PRIOR DISTRIBUTION   
4 MULTINOMIAL MODEL FOR CATEGORICAL DATA   
5 MULTIVARIATE NORMAL MODEL WITH KNOWN VARIANCE   
6 MULTIVARIATE NORMAL WITH UNKNOWN MEAN AND VARIANCE   
EXAMPLE: ANALYSIS OF A BIOASSAY EXPERIMENT   
SUMMARY OF ELEMENTARY MODELING AND COMPUTATION

# EXAMPLE: ANALYSIS OF A BIOASSAY EXPERIMENT

See the textbook.

1 AVERAGING OVER NUISANCE PARAMETERS   
2 NORMAL DATA WITH A NONINFORMATIVE PRIOR DISTRIBUTION   
3 NORMAL DATA WITH A CONJUGATE PRIOR DISTRIBUTION   
4 MULTINOMIAL MODEL FOR CATEGORICAL DATA   
5 MULTIVARIATE NORMAL MODEL WITH KNOWN VARIANCE   
6 MULTIVARIATE NORMAL WITH UNKNOWN MEAN AND VARIANCE   
EXAMPLE: ANALYSIS OF A BIOASSAY EXPERIMENT

SUMMARY OF ELEMENTARY MODELING AND COMPUTATION

# SUMMARY OF ELEMENTARY MODELING AND

# COMPUTATION

The lack of multi-parameter models permitting easy calculation of posterior distributions is NOT a major practical handicap for three main reasons.

1. When there are few parameters, posterior inference in non-conjugate multi-parameter models can be obtained by simple simulation methods.   
2. Sophisticated models can often be represented in a hierarchical or conditional manner, for which effective computational strategies are available.

3. We can often apply a normal approximation to the posterior distribution, and therefore the conjugate structure of the normal model can play an important role in practice, well beyond its application to explicitly normal sampling models.

The following summarizes what we have done so far and foreshadows the general methods.

1. Write the likelihood part of the model, $p(y|\theta)$ , ignoring any factors that are free of $\theta$ .   
2. Write the posterior density, $p(\theta |y)\propto p(\theta)\times p(y|\theta)$

- If prior information is well-formulated, include it in $p(\theta)$ .   
- Otherwise use a weakly informative prior distribution or temporarily set $p(\theta) \propto$ constant, with the understanding that the prior density can be altered later to include additional information or structure.

3. Create a crude estimate of the parameters, $\theta$ , for use as a starting point and a comparison to the computation in the next step.   
4. Draw simulations $\theta^1, \ldots, \theta^S$ , from the posterior distribution. Use the sample draws to compute the posterior density of any functions of $\theta$ that may be of interest.   
5. If any predictive quantities, $\tilde{y}$ , are of interest, simulate $\tilde{y}^1, \ldots, \tilde{y}^s$ by drawing each $\tilde{y}^s$ from the sampling distribution conditional on the drawn value $\theta^s$ , $p(\tilde{y} | \theta^s)$ .

# NOTE

For non-conjugate models, step 4 above can be difficult.

Various methods have been developed to draw posterior simulations in complicated models.

Occasionally, high-dimensional problems can be solved by combining analytical and numerical simulation methods.

If $\theta$ has only one or two components, it is possible to draw simulations by computing on a grid.

# ASSIGNMENT

3.3   
3.10   
3.15   
3.11 (optional)