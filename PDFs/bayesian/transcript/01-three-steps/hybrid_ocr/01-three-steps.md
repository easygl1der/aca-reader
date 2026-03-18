# PROBABILITY AND INFERENCE

# CHAPTER 1

THE THREE STEPS OF BAYESIAN DATA ANALYSIS   
2 GENERAL NOTATION FOR STATISTICAL INFERENCE   
3 BAYESIAN INFERENCE   
4 DISCRETE PROBABILITY EXAMPLES: GENETICS AND SPELL CHECKING   
5 PROBABILITY AS A MEASURE OF UNCERTAINTY   
EXAMPLE OF PROBABILITY ASSIGNMENT: FOOTBALL POINT SPREADS   
7 SOME USEFUL RESULTS FROM PROBABILITY THEORY

# THE THREE STEPS OF BAYESIAN DATA ANALYSIS

The process of Bayesian data analysis can be idealized by dividing it into the following three steps:

1. Setting up a full probability model, a joint probability distribution for all observable and unobservable quantities in a problem. The model should be consistent with knowledge about the underlying scientific problem and the data collection process.   
2. Conditioning on observed data: calculating and interpreting the appropriate posterior distribution, the conditional probability distribution of the unobserved quantities of ultimate interest, given the observed data.

3. Evaluating the fit of the model and the implications of the resulting posterior distribution:

- How well does the model fit the data, are the substantive conclusions reasonable?   
- How sensitive are the results to the modeling assumptions in step 1?

In response, one can alter or expand the model and repeat the three steps.

The second involving computational methodology and the third a delicate balance of technique and judgment, guided by the applied context of the problem.

The first step remains a major stumbling block for much Bayesian analysis:

Where do our models come from?   
- How do we go about constructing appropriate probability specifications?

This course provides some guidance on these issues and illustrate the importance of the third step in retrospectively evaluating the fit of models.

Along with the improved techniques available for computing conditional probability distributions in the second step, advances in carrying out the third step alleviate to some degree the need to assume correct model specification at the first attempt.

In particular, the much-feared dependence of conclusions on subjective prior distributions can be examined and explored.

A primary motivation for Bayesian thinking is that it facilitates a commonsense interpretation of statistical conclusions.

For instance,

- a Bayesian (probability) interval for an unknown quantity of interest can be directly regarded as having a high probability of containing the unknown quantity, in contrast to   
- a frequentist (confidence) interval, which may strictly be interpreted only in relation to a sequence of similar inferences that might be made in repeated practice.

1 THE THREE STEPS OF BAYESIAN DATA ANALYSIS   
2 GENERAL NOTATION FOR STATISTICAL INFERENCE   
3 BAYESIAN INFERENCE   
4 DISCRETE PROBABILITY EXAMPLES: GENETICS AND SPELL CHECKING   
5 PROBABILITY AS A MEASURE OF UNCERTAINTY   
EXAMPLE OF PROBABILITY ASSIGNMENT: FOOTBALL POINT SPREADS   
SOME USEFUL RESULTS FROM PROBABILITY THEORY

# PARAMETERS, DATA, AND PREDICTIONS

$\theta$ : unobservable vector quantities or population parameters of interest (such as the probabilities of survival under each treatment for randomly chosen members of the population in the clinical trial);   
$y$ : the observed data (such as the numbers of survivors and deaths in each treatment group).

$\tilde{y}$ : unknown, but potentially observable, quantities (such as the outcomes of the patients under the other treatment, or the outcome under each of the treatments for a new patient similar to those already in the trial);   
x: explanatory variables, or covariates (such variables might include the age and previous health status of each patient in the study).

THE THREE STEPS OF BAYESIAN DATA ANALYSIS   
GENERAL NOTATION FOR STATISTICAL INFERENCE   
BAYESIAN INFERENCE   
4 DISCRETE PROBABILITY EXAMPLES: GENETICS AND SPELL CHECKING   
PROBABILITY AS A MEASURE OF UNCERTAINTY   
EXAMPLE OF PROBABILITY ASSIGNMENT: FOOTBALL POINT SPREADS   
SOME USEFUL RESULTS FROM PROBABILITY THEORY

# BAYESIAN INFERENCE

Bayesian statistical conclusions about a parameter $\theta$ , or unobserved data $\tilde{y}$ , are made in terms of probability statements.

These probability statements are conditional on the observed value of $y$ , and in our notation are written simply as $p(\theta | y)$ or $p(\tilde{y} | y)$ .

We also implicitly condition on the known values of any covariates, $x$ .

# BAYES' RULE

In order to make probability statements about $\theta$ given $y$ , we must begin with a model providing a joint probability distribution for $\theta$ and $y$ .

The joint probability mass or density function can be written as a product of two densities that are often referred to as the prior distribution $p(\theta)$ and the sampling distribution (or data distribution) $p(y|\theta)$ , respectively:

$$
p (\theta , y) = p (\theta) \times p (y | \theta).
$$

Simply conditioning on the known value of the data $y$ , using the basic property of conditional probability known as Bayes' rule, yields the posterior density:

$$
p (\theta | y) = \frac {p (\theta , y)}{p (y)} = \frac {p (\theta) \times p (y | \theta)}{p (y)};
$$

$$
p (y) = \left\{ \begin{array}{l l} \sum_ {\theta} p (\theta) \times p (y | \theta), & \theta \text {i s d i s c r e t e}, \\ \int p (\theta) \times p (y | \theta) d \theta , & \theta \text {i s c o n t i n u o u s}. \end{array} \right.
$$

An equivalent form omits the factor $p(y)$ , which does not depend on $\theta$ and, with fixed $y$ , can thus be considered a constant, yielding the unnormalized posterior density:

$$
p (\theta | y) \propto p (\theta) \times p (y | \theta).
$$

# NOTE

$p(y|\theta)$ is taken as a function of $\theta$ , not of $y$ .

These simple formulas encapsulate the technical core of Bayesian inference:

The primary task of any specific application is to develop the model $p(\theta, y)$ and perform the computations to summarize $p(\theta | y)$ in appropriate ways.

# PREDICTION

To make inferences about an unknown observable, often called predictive inferences, we follow a similar logic.

Before the data $y$ are considered, the distribution of the unknown but observable $y$ is

$$
p (y) = \int p (y, \theta) d \theta = \int p (y | \theta) \times p (\theta) d \theta .
$$

This is often called the marginal distribution of $y$ , but a more informative name is the prior predictive distribution:

- prior because it is not conditional on a previous observation of the process;   
- predictive because it is the distribution for a quantity that is observable.

After the data $y$ have been observed, we can predict an unknown observable, $\tilde{y}$ , from the same process.

# EXAMPLE

$y = (y_{1},\ldots ,y_{n})$ may be the vector of recorded weights of an object weighed $n$ times on a scale, $\theta = (\mu ,\sigma^2)$ may be the unknown true weight of the object and the measurement variance of the scale, and $\tilde{y}$ may be the yet to be recorded weight of the object in a planned new weighing.

The distribution of $\tilde{y}$ is called the posterior predictive distribution:

$\bullet$ posterior because it is conditional on the observed $y$ ;   
- predictive because it is a prediction for an observable $\tilde{y}$ .

$$
\begin{array}{l} p (\tilde {y} | y) = \int p (\tilde {y}, \theta | y) d \theta \quad p (\tilde {y}, \theta | y) = p (\tilde {y} | \theta , y) \times p (\theta | y) \\ = \int p (\tilde {y} | \theta , y) \times p (\theta | y) d \theta \quad p (\tilde {y} | \theta , y) = p (\tilde {y} | \theta) \\ = \int p (\tilde {y} | \theta) \times p (\theta | y) d \theta . \\ \end{array}
$$

# NOTE

- The second line displays the posterior predictive distribution as an average of conditional predictions over the posterior distribution of $\theta$ .   
- The last step follows from the assumed conditional independence of $y$ and $\tilde{y}$ given $\theta$ .

# LIKELIHOOD

Using Bayes' rule with a chosen probability model means that the data $y$ affect the posterior inference only through $p(y|\theta)$ , which, when regarded as a function of $\theta$ , for fixed $y$ , is called the likelihood function.

In this way Bayesian inference obeys what is sometimes called the likelihood principle, which states that for a given sample of data, any two probability models $p(y|\theta)$ that have the same likelihood function yield the same inference for $\theta$ .

The likelihood principle is reasonable, but only within the framework of the model or family of models adopted for a particular analysis.

In practice, one can rarely be confident that the chosen model is correct.

In fact, our view of an applied Bayesian statistician is one who is willing to apply Bayes' rule under a variety of possible models.

# LIKELIHOOD AND ODDS RATIOS

The ratio of the posterior density $p(\theta | y)$ evaluated at the points $\theta_{1}$ and $\theta_{2}$ under a given model is called the posterior odds for $\theta_{1}$ compared to $\theta_{2}$ .

The most familiar application of this concept is with discrete parameters, with $\theta_{2}$ taken to be the complement of $\theta_{1}$ .

Odds provide an alternative representation of probabilities and have the attractive property that Bayes' rule takes a particularly simple form when expressed in terms of them:

$$
\frac {p \left(\theta_ {1} \mid y\right)}{p \left(\theta_ {2} \mid y\right)} = \frac {p \left(\theta_ {1}\right) p \left(y \mid \theta_ {1}\right) / p (y)}{p \left(\theta_ {2}\right) p \left(y \mid \theta_ {2}\right) / p (y)} = \frac {p \left(\theta_ {1}\right)}{p \left(\theta_ {2}\right)} \times \frac {p \left(y \mid \theta_ {1}\right)}{p \left(y \mid \theta_ {2}\right)}.
$$

# NOTE

The posterior odds are equal to the prior odds multiplied by the likelihood ratio,

$$
\frac {p (y | \theta_ {1})}{p (y | \theta_ {2})}.
$$

1 THE THREE STEPS OF BAYESIAN DATA ANALYSIS   
2 GENERAL NOTATION FOR STATISTICAL INFERENCE   
3 BAYESIAN INFERENCE   
4 DISCRETE PROBABILITY EXAMPLES: GENETICS AND SPELL CHECKING   
5 PROBABILITY AS A MEASURE OF UNCERTAINTY   
EXAMPLE OF PROBABILITY ASSIGNMENT: FOOTBALL POINT SPREADS   
7 SOME USEFUL RESULTS FROM PROBABILITY THEORY

# DISCRETE PROBABILITY EXAMPLES: GENETICS AND SPELL CHECKING

See the textbook.

1 THE THREE STEPS OF BAYESIAN DATA ANALYSIS   
2 GENERAL NOTATION FOR STATISTICAL INFERENCE   
3 BAYESIAN INFERENCE   
4 DISCRETE PROBABILITY EXAMPLES: GENETICS AND SPELL CHECKING   
5 PROBABILITY AS A MEASURE OF UNCERTAINTY   
EXAMPLE OF PROBABILITY ASSIGNMENT: FOOTBALL POINT SPREADS   
7 SOME USEFUL RESULTS FROM PROBABILITY THEORY

# PROBABILITY AS A MEASURE OF UNCERTAINTY

In Bayesian statistics, probability is used as the fundamental measure or yardstick of uncertainty.

Within this paradigm, it is equally legitimate to discuss the probability of rain tomorrow or of a Brazilian victory in the soccer World Cup as it is to discuss the probability that a coin toss will land heads.

Hence, it becomes as natural to consider the probability that an unknown estimand lies in a particular range of values as it is to consider the probability that the mean of a random sample of 10 items from a known fixed population of size 100 will lie in a certain range.

The first of these two probabilities (rain tomorrow) is of more interest after data have been acquired whereas the second (a Brazilian victory in the soccer World Cup) is more relevant beforehand.

Bayesian methods enable statements to be made about the partial knowledge available (based on data) concerning some situation or state of nature (unobservable or as yet unobserved) in a systematic way, using probability as the yardstick.

The guiding principle is that the state of knowledge about anything unknown is described by a probability distribution.

What is meant by a numerical measure of uncertainty?

# EXAMPLE

The probability of heads in a coin toss is widely agreed to be $1 / 2$ .

Why is this so? Two justifications seem to be commonly given.

# SYMMETRY OR EXCHANGEABILITY ARGUMENT

$$
\text {p r o b a b i l i t y} = \frac {\text {n u m b e r o f f a v o r a b l e c a s e s}}{\text {n u m b e r o f p o s s i b i l i t i e s}}
$$

assuming equally likely possibilities.

For a coin toss this is really a physical argument, based on assumptions about the forces at work in determining the manner in which the coin will fall, as well as the initial physical conditions of the toss.

# FREQUENCY ARGUMENT

probability $=$ relative frequency obtained in a long sequence of tosses

assumed to be performed in an identical manner, physically independently of each other.

Both the above arguments are in a sense subjective, in that they require judgments about the nature of the coin and the tossing procedure, and both involve semantic arguments about the meaning of equally likely events, identical measurements, and independence.

The frequency argument may be perceived to have certain special difficulties, in that it involves the hypothetical notion of a long sequence of identical tosses. If taken strictly, this point of view does not allow a statement of probability for a single coin toss that does not happen to be embedded, at least conceptually, in a long sequence of identical events.

Why is probability a reasonable way of quantifying uncertainty? The following reasons are often advanced.

1. By analogy: physical randomness induces uncertainty, so it seems reasonable to describe uncertainty in the language of random events.

Common speech uses many terms such as probably and unlikely, and it appears consistent with such usage to extend a more formal probability calculus to problems of scientific inference.

2. Axiomatic or normative approach: related to decision theory, this approach places all statistical inference in the context of decision-making with gains and losses.

Then reasonable axioms (ordering, transitivity, and so on) imply that uncertainty must be represented in terms of probability.

We view this normative rationale as suggestive but not compelling.

# 3. Coherence of bets.

Define the probability p attached (by you) to an event E as the fraction (p ∈ [0, 1]) at which you would exchange (that is, bet) $p for a return of $1 if E occurs.

That is, if E occurs, you gain extra $(1 - p); if the complement of E occurs, you lose $p.

# NOTE

The principle of coherence states that your assignment of probabilities to all possible events should be such that it is not possible to make a definite gain by betting with you.

It can be proved that probabilities constructed under this principle must satisfy the basic axioms of probability theory.

The betting rationale has some fundamental difficulties:

- Exact odds are required, on which you would be willing to bet in either direction, for all events. How can you assign exact odds if you are not sure?   
- If a person is willing to bet with you, and has information you do not, it might not be wise for you to take the bet. In practice, probability is an incomplete (necessary but not sufficient) guide to betting.

All of these considerations suggest that probabilities may be a reasonable approach to summarizing uncertainty in applied statistics, but the ultimate proof is in the success of the applications.

# SUBJECTIVITY AND OBJECTIVITY

All statistical methods that use probability are subjective in the sense of relying on mathematical idealizations of the world.

Bayesian methods are sometimes said to be especially subjective because of their reliance on a prior distribution, but in most problems, scientific judgment is necessary to specify both the likelihood and the prior parts of the model.

A general principle is at work here: whenever there is replication, in the sense of many exchangeable units observed, there is scope for estimating features of a probability distribution from data and thus making the analysis more objective.

If an experiment as a whole is replicated several times, then the parameters of the prior distribution can themselves be estimated from data.

1 THE THREE STEPS OF BAYESIAN DATA ANALYSIS   
2 GENERAL NOTATION FOR STATISTICAL INFERENCE   
3 BAYESIAN INFERENCE   
4 DISCRETE PROBABILITY EXAMPLES: GENETICS AND SPELL CHECKING   
5 PROBABILITY AS A MEASURE OF UNCERTAINTY   
EXAMPLE OF PROBABILITY ASSIGNMENT: FOOTBALL POINT SPREADS   
7 SOME USEFUL RESULTS FROM PROBABILITY THEORY

# EXAMPLE OF PROBABILITY ASSIGNMENT: FOOTBALL POINT SPREADS

See the textbook.

1 THE THREE STEPS OF BAYESIAN DATA ANALYSIS   
2 GENERAL NOTATION FOR STATISTICAL INFERENCE   
3 BAYESIAN INFERENCE   
4 DISCRETE PROBABILITY EXAMPLES: GENETICS AND SPELL CHECKING   
5 PROBABILITY AS A MEASURE OF UNCERTAINTY   
EXAMPLE OF PROBABILITY ASSIGNMENT: FOOTBALL POINT SPREADS

7 SOME USEFUL RESULTS FROM PROBABILITY THEORY

# SOME USEFUL RESULTS FROM PROBABILITY THEORY

See the textbook.

# ASSIGNMENT

1. Conditional probability: suppose that if $\theta = 1$ , then $y$ has a normal distribution with mean 1 and standard deviation $\sigma$ , and if $\theta = 2$ , then $y$ has a normal distribution with mean 2 and standard deviation $\sigma$ . Also, suppose $\operatorname{Pr}(\theta = 1) = 0.5$ and $\operatorname{Pr}(\theta = 2) = 0.5$ .

(a) For $\sigma = 2$ , write the formula for the marginal probability density for $y$ and sketch it.   
(b) What is $\operatorname{Pr}(\theta = 1 | y = 1)$ , again supposing $\sigma = 2$ ?   
(c) Describe how the posterior density of $\theta$ changes in shape as $\sigma$ is increased and as it is decreased.

4. Probability assignment: we will use the football dataset to estimate some conditional probabilities about professional football games. There were twelve games with point spreads of 8 points; the outcomes in those games were: $-7, -5, -3, -3, 1, 6, 7, 13, 15, 16, 20,$ and 21, with positive values indicating wins by the favorite and negative values indicating wins by the underdog. Consider the following conditional probabilities:

Pr(favorite wins | point spread = 8),

Pr(favorite wins by at least 8 | point spread = 8),

Pr(favorite wins by at least 8 | point spread = 8 and favorite wins).

(a) Estimate each of these using the relative frequencies of games with a point spread of 8.   
(b) Estimate each using the normal approximation for the distribution of (outcome - point spread).