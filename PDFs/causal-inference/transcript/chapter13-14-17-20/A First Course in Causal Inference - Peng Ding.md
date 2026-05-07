Before proving Theorem 11.2, it is important to note the additional assumption $0 < e ( X ) < 1$ . It is called the overlap or positivity condition. The formulas in Theorem 11.2 become infinity if $e ( X ) = 0$ or 1 for some values of $X$ . It is not a requirement only for the identification formulas based on propensity score weighting. Although it was not stated explicitly in Theorem 10.1, the conditional expectations $E ( Y \mid Z = 1 , X )$ and $E ( Y \mid Z = 0 , X )$ in the identification formula of $\tau$ in (10.6) is well defined only if $0 < e ( X ) < 1$ . The overlap condition can be viewed as a technical condition to ensure that the formulas in Theorems 10.1 and 11.2 are well defined. It can also cause some philosophical issues for causal inference with observational studies. When unit $i$ has $e ( X _ { i } ) = 1$ , we always observe its potential outcome under the treatment, $Y _ { i } ( 1 )$ , but can never observe its potential outcome under the control, $Y _ { i } ( 0 )$ . In this case, the potential outcome $Y _ { i } ( 0 )$ may not even be well defined, making the definition of the causal effect ambiguous for unit $_ i$ . King and Zeng (2006) called $Y _ { i } ( 0 )$ an extreme counterfactual when $e ( X _ { i } ) = 1$ , and discussed their dangers in causal inference. A similar problem arises if unit $i$ has $e ( X _ { i } ) = 0$ .

In sum, $Z \bot \bot \{ Y ( 1 ) , Y ( 0 ) \} \mid X$ requires adequate covariates to ensure the conditional independence of the treatment and potential outcomes, and $0 < e ( X ) < 1$ requires residual randomness in the treatment conditional on the covariates. In fact, Rosenbaum and Rubin (1983b)’s definition of strong ignorability includes both of these conditions. In modern literature, they are often stated separately.

Proof of Theorem 11.2: I only prove the result for $E \{ Y ( 1 ) \}$ because the proof of the result for $E \{ Y ( 0 ) \}$ is similar. We have

$$
\begin{array}{l} E \left\{\frac {Z Y}{e (X)} \right\} \\ = E \left\{\frac {Z Y (1)}{e (X)} \right\} \\ = E \left[ E \left\{\frac {Z Y (1)}{e (X)} \mid X \right\} \right] \quad (\text {t o w e r p r o p e r t y}) \\ = E \left[ \frac {1}{e (X)} E \left\{Z Y (1) \mid X \right\} \right] \\ = E \left[ \frac {1}{e (X)} E (Z \mid X) E \{Y (1) \mid X \} \right] (\text {s t r o n g i g n o r a b i l i t y}) \\ = E \left[ \frac {1}{e (X)} e (X) E \{Y (1) \mid X \} \right] \\ = E \left[ E \left\{Y (1) \mid X \right\} \right] \\ = E \{Y (1) \}. \\ \end{array}
$$

# 11.2.2 Inverse propensity score weighting estimators

Theorem 11.2 motivates the following moment estimator for the average causal effect:

$$
\hat {\tau} ^ {\mathrm {h t}} = \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {Z _ {i} Y _ {i}}{\hat {e} (X _ {i})} - \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {(1 - Z _ {i}) Y _ {i}}{1 - \hat {e} (X _ {i})},
$$

where $\hat { e } ( X _ { i } )$ is the estimated propensity score. This is the inverse propensity score weighting (IPW) estimator, which is also called the Horvitz–Thompson (HT) estimator. Horvitz and Thompson (1952) proposed it in survey sampling and Rosenbaum (1987a) used in causal inference with observational studies.

However, the estimator $\hat { \tau } ^ { \mathrm { h t } }$ has many problems. In particular, it is not invariant to the location transformation of the outcome. Proposition 11.1 states this problem precisely, with the proof relegated to Problem 11.3.

Proposition 11.1 (lack of invariance for the HT estimator) If we change $Y _ { i }$ to $Y _ { i } + c$ with a constant c, then the HT estimator $\hat { \tau } ^ { \mathrm { h t } }$ becomes $\hat { \tau } ^ { \mathrm { h t } } + c ( \hat { 1 } _ { \mathrm { T } } -$ $\hat { 1 } _ { \mathrm { C } }$ ), where

$$
\hat {1} _ {\mathrm {T}} = \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {Z _ {i}}{\hat {e} (X _ {i})}, \quad \hat {1} _ {\mathrm {C}} = \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {(1 - Z _ {i})}{1 - \hat {e} (X _ {i})}
$$

can be viewed as two different estimates of the constant 1.

In Proposition 11.1, I use the funny notation $\hat { 1 } _ { \mathrm { T } }$ and $\hat { 1 } _ { \mathrm { C } }$ because with the true propensity score these two terms both have expectation 1; see Problem 11.3 for more details. In general, $\hat { 1 } _ { \mathrm { T } } - \hat { 1 } _ { \mathrm { C } }$ is not zero in finite samples. Since adding a constant to every outcome should not change the average causal effect, the HT estimator is not reasonable because of its dependence on $c$ . A simple fix to the problem is to normalize the weights by $\hat { 1 } _ { \mathrm { T } }$ and $\hat { 1 } _ { \mathrm { C } }$ respectively, resulting in the following estimator

$$
\hat {\tau} ^ {\mathrm {h a j e k}} = \frac {\sum_ {i = 1} ^ {n} \frac {Z _ {i} Y _ {i}}{\hat {e} (X _ {i})}}{\sum_ {i = 1} ^ {n} \frac {Z _ {i}}{\hat {e} (X _ {i})}} - \frac {\sum_ {i = 1} ^ {n} \frac {(1 - Z _ {i}) Y _ {i}}{1 - \hat {e} (X _ {i})}}{\sum_ {i = 1} ^ {n} \frac {1 - Z _ {i}}{1 - \hat {e} (X _ {i})}}.
$$

This is the Hajek estimator due to H´ajek (1971) in the context of survey sampling with varying probabilities. We can verify that the Hajek estimator is invariant to the location transformation. That is, if we replace $Y _ { i }$ by $Y _ { i } + c$ , then $\hat { \tau } ^ { \mathrm { h a j e k } }$ remains the same; see Problem 11.3. Moreover, many numerical studies have found that $\hat { \tau } ^ { \mathrm { h a j e k } }$ is much more stable than $\hat { \tau } ^ { \mathrm { h t } }$ in finite samples.

# 11.2.3 A problem of IPW and a fundamental problem of causal inference

Many asymptotic analyses require a strong overlap condition

$$
0 <   \alpha_ {\mathrm {L}} \leq e (X) \leq \alpha_ {\mathrm {U}} <   1,
$$

that is, the true propensity score is bounded away from 0 and 1. However, D’Amour et al. (2021) pointed out that this is a rather strong assumption, especially with many covariates. Chapter 20 will discuss this problem in detail.

Even if the strong overlap condition holds for the true propensity score, the estimated propensity scores can be close to 0 or 1. When this happens, the weighting estimators blow up to infinity, which results in extremely unstable behavior in finite samples. We can either truncate the estimated propensity score by changing it to

$$
\max \left[ \alpha_ {\mathrm {L}}, \min \{\hat {e} (X _ {i}), \alpha_ {\mathrm {U}} \} \right],
$$

or trim the observations by dropping units with $\hat { e } ( X _ { i } )$ outside the interval $[ \alpha _ { \mathrm { L } } , \alpha _ { \mathrm { U } } ]$ . Crump et al. (2009) suggested $\alpha _ { \mathrm { L } } = 0 . 1$ and $\alpha _ { \mathrm { U } } = 0 . 9$ , and Kurth et al. (2005) suggested $\alpha _ { \mathrm { L } } = 0 . 0 5$ and $\alpha _ { \mathrm { U } } ~ = ~ 0 . 9 5$ . Yang and Ding (2018b) established some asymptotic theory for trimming. Overall, although trimming often stabilizes the IPW estimators, it also injects additional arbitrariness into the procedure.

# 11.2.4 Application

The following functions can compute the IPW estimators and their bootstrap standard errors.

```r
ipw.est = function(z, y, x, truncps = c(0, 1))  
{  
    ## fitted propensity score  
    pscore = glm(z ~ x, family = binomial) $fitted.values  
    pscore = pmax(truncps[1], Tmin(truncps[2], pscore))  
    ace.ipw0 = mean(z*y/pscore - (1 - z)*y/(1 - pscore))  
    ace.ipw = mean(z*y/pscore)/mean(z/pscore) 
    mean((1 - z)*y/(1 - pscore))/mean((1 - z)/(1 - pscore))  
    return(c(ace.ipw0, ace.ipw))  
}  
ipw.boot = function(z, y, x, n.boot = 500, truncps = c(0, 1))  
{  
    point.est = ipw.est(z, y, x, truncps)  
    ## nonparametric bootstrap  
    n.sample = length(z)  
    x = as.matrix(x)  
    boot.est = replicate(n.boot, {id.boot = sample(1:n/sample, n/sample, replace = TRUE)  
        ipw.est(z[id.boot], y[id.boot], x[id.boot], ], truncps)  
}) 
```

```julia
boot.se = apply(boot.est, 1, sd)
res = cbind(point.est, boot.se)
colnames(res) = c("est", "se")
rownames(res) = c("HT", "Hajek")
return(res) 
```

Revisiting Example 10.3, we can obtain the IPW estimators based on different truncations of the estimated propensity scores. The following results are the two weighting estimators with the bootstrap standard errors, with truncations at $( 0 , 1 )$ , (0.01, 0.99), (0.05, 0.95), and (0.1, 0.9):

```txt
> trunc.list = list(trunc0 = c(0,1),
+ trunc.01 = c(0.01, 0.99),
+ trunc.05 = c(0.05, 0.95),
+ trunc.1 = c(0.1, 0.9))
> trunc.est = lapply(trunc.list,
+ function(t) {
+ est = ipw.boot(z, y, x, truncps = t)
+ round(est, 3)
+ }
>
trunc.est
$trunc0
est se
HT -1.516 0.496
Hajek -0.156 0.258
$trunc.01
est se
HT -1.516 0.501
Hajek -0.156 0.254
$trunc.05
est se
HT -1.499 0.501
Hajek -0.152 0.255
$trunc.1
est se
HT -0.713 0.425
Hajek -0.054 0.246 
```

The HT estimator gives results far away from all other estimators we discussed so far. The point estimates seem too large and they are negatively significant unless we truncate the estimated propensity scores at (0.1, 0.9). This is an example showing the instability of the HT estimator.

# 11.3 The balancing property of the propensity score

# 11.3.1 Theory

Theorem 11.3 The propensity score satisfies

$$
Z \perp \perp X \mid e (X).
$$

Moreover, for any function $h ( \cdot )$ , we have

$$
E \left\{\frac {Z h (X)}{e (X)} \right\} = E \left\{\frac {(1 - Z) h (X)}{1 - e (X)} \right\} \tag {11.2}
$$

provided the existence of the moments on both sides of (11.2).

Theorem 11.3 does not require the ignorability assumption. It is about the treatment $Z$ and covariates $X$ only. The first part of Theorem 11.3 states that conditional on the propensity score, the treatment indicator, and the covariates are independent. Therefore, within the same level of the propensity score, the covariate distributions are balanced across the treatment and control groups. The second part of Theorem 11.3 states that an equivalent form of covariate balance based on the weighting form. I give a proof of Theorem 11.3 below.

Proof of Theorem 11.3: First, we show $Z \bot \bot X \mid e ( X )$ , that is,

$$
\Pr \{Z = 1 \mid X, e (X) \} = \Pr \{Z = 1 \mid e (X) \}. \tag {11.3}
$$

Following similar steps as the proof of Theorem 11.1, we can show that the left-hand side of (11.3) equals

$$
\operatorname * {p r} \{Z = 1 \mid X, e (X) \} = \operatorname * {p r} (Z = 1 \mid X) = e (X),
$$

and the right-hand side of (11.3) equals

$$
\begin{array}{l} \Pr \{Z = 1 \mid e (X) \} = E \{Z \mid e (X) \} \\ = E \left[ E \{Z \mid X, e (X) \} \mid e (X) \right] \\ = E \left[ E \{Z \mid X \} \mid e (X) \right] \\ = E \left[ e (X) \mid e (X) \right] \\ = e (X). \\ \end{array}
$$

Therefore, (11.3) holds.

Second, we show (11.2). We can use similar steps as the proof of Theorem 11.2. But given Theorem 11.2, we have a simpler proof. If we view $h ( X )$ as an outcome, then its two potential outcomes are identical and ignorability holds: $Z \bot \bot \{ h ( X ) , h ( X ) \} \mid X$ . The difference between the left-hand and right-hand sides of (11.2) is the average causal effect of $Z$ on $h ( X )$ , which is zero. □

# 11.3.2 Covariate balance check

The proof of Theorem 11.3 is simple. But Theorem 11.3 has useful implications for the statistical analysis. Before getting access to the outcome data, we can check whether the propensity score model is specified well enough to ensure the covariate balance in the data. Rubin (2007) viewed this as the design stage of the observational study, and Rubin (2008) argued that this can result in more objective causal inference because the design stage does not involve the values of the outcomes.1

In the propensity score stratification, we have the discretized estimated propensity score $\hat { e } ^ { \prime } ( X )$ and approximately

$$
Z \text {止} X \mid \hat {e} ^ {\prime} (X) = e _ {k} \quad (k = 1, \dots , K).
$$

Therefore, we can check whether the covariate distributions are the same across the treatment and control groups within each stratum of the discretized estimated propensity score.

In propensity score weighting, we can view $h ( X )$ as a pseudo outcome and estimate the average causal effect on $h ( X )$ . Because the true average causal effect on $h ( X )$ is $0$ , the estimate should not be significantly different from 0. A canonical choice of $h ( X )$ is $X$ .

Let us revisit Example 10.3 again. Based on propensity score stratification with $K = 5$ , all the covariates are well-balanced across the treatment and control groups. Similar results hold for the Hajek estimator. The only exception is Food_Stamp, the 7th covariate in Figure 11.2. Figure 11.2 shows the balance-checking results.

# 11.4 Homework Problems

# 11.1 Another version of Theorem 11.1

Prove that

$$
Z \bot \{Y (1), Y (0), X \} \mid e (X, Y (1), Y (0)). \tag {11.4}
$$

Remark: This result holds without assuming strong ignorability. It implies that

$$
Z \bot \{Y (1), Y (0) \} \mid \{X, e (X, Y (1), Y (0) \}.
$$

Rosenbaum (2020) and Rosenbaum and Rubin (2023) pointed out the result in (11.4) and called $e ( X , Y ( 1 ) , Y ( 0 ) )$ the principal unobserved covariate.

![](images/f1caec90925bdb54e8d481bf6a6b12f0435d735245a7f3413ec65b5548d2e142.jpg)

![](images/b024e2bbdab45a1d472de5db2d71f48a053041af2bff2ee8eff0566a8abc6300.jpg)  
FIGURE 11.2: Balance check: point estimates and 95% confidence intervals of the average causal effect on covariates

TABLE 11.1: Table 1 of Rosenbaum and Rubin (1983a)   

<table><tr><td>stratum by e(X)</td><td>treatment</td><td>number of patients</td><td>proportion improved</td></tr><tr><td rowspan="2">1</td><td>Surgical</td><td>26</td><td>0.54</td></tr><tr><td>Medical</td><td>277</td><td>0.35</td></tr><tr><td rowspan="2">2</td><td>Surgical</td><td>68</td><td>0.70</td></tr><tr><td>Medical</td><td>235</td><td>0.40</td></tr><tr><td rowspan="2">3</td><td>Surgical</td><td>98</td><td>0.70</td></tr><tr><td>Medical</td><td>205</td><td>0.35</td></tr><tr><td rowspan="2">4</td><td>Surgical</td><td>164</td><td>0.71</td></tr><tr><td>Medical</td><td>139</td><td>0.30</td></tr><tr><td rowspan="2">5</td><td>Surgical</td><td>234</td><td>0.70</td></tr><tr><td>Medical</td><td>69</td><td>0.39</td></tr></table>

# 11.2 Another version of Theorem 11.1

Theorem 11.1 states a result under strong ignorability. An analogous result also holds under ignorability. That is, if ignorability holds conditional on covariates $X$ , then it also holds conditional on the scalar propensity score $e ( X )$ .

Theorem 11.4 If $Z \bot Y ( z ) \mid X$ for $z = 0 , 1$ , then Z $\underline { { \cdot } } \sqcup Y ( z ) \mid e ( X )$ for $z =$ $0 , 1$ .

Prove Theorem 11.4.

# 11.3 More results on the IPW estimators

This is related to the discussion of the HT estimator in Section 11.2.2. First, prove Proposition 11.1. Second, prove

$$
E \left\{\frac {1}{n} \sum_ {i = 1} ^ {n} \frac {Z _ {i}}{e (X _ {i})} \right\} = 1, \quad E \left\{\frac {1}{n} \sum_ {i = 1} ^ {n} \frac {(1 - Z _ {i})}{1 - e (X _ {i})} \right\} = 1.
$$

Third, prove that if we add a constant $c$ to every observed outcome $Y _ { i }$ , the Hajek estimator $\hat { \tau } ^ { \mathrm { h a j e k } }$ remains the same.

# 11.4 Re-analysis of Rosenbaum and Rubin (1983a)

Table 11.1 is from Rosenbaum and Rubin (1983a), which concerned the causal effect of the coronary artery bypass surgery compared with the medical therapy on the functional improvement 6 months after cardiac catheterization. They first estimated the propensity score based on 74 observed covariates and then formed 5 strata based on the discretized estimated propensity score. Because the treatment is binary and the outcome is also binary, they represented the data in a table. Based on Table 11.1 , estimate the average causal effect, and report the 95% confidence interval of the average causal effect.

Remark: If you are interested, you can read the whole paper of Rosenbaum

and Rubin (1983a) after reading Part IV of the book. It is a canonical paper on sensitivity analysis in causal inference.

# 11.5 Balancing score and propensity score: more theoretical results

Rosenbaum and Rubin (1983b) also introduced the notion of balancing score.

Definition 11.2 (balancing score) $b ( X )$ is a balancing score if

$$
Z \perp \perp X \mid b (X).
$$

In Definition 11.2, $b ( X )$ can be a scalar or a vector. An obvious balancing score is $b ( X ) = X$ , but it is not a useful one without any simplification of the original covariates. By Theorem 11.3, the propensity score is a special balancing score. More interestingly, Rosenbaum and Rubin (1983b) showed that the propensity score is the coarsest balancing score, as in Theorem 11.5 below which includes Theorem 11.3 as a special case.

Theorem 11.5 $b ( X )$ is a balancing score if and only if $b ( X )$ is finer than $e ( X )$ in the sense that $e ( X ) = f ( b ( X ) )$ for some function $f ( \cdot )$ .

Theorem 11.5 is relevant in subgroup analysis. In particular, we may be interested in not only the average causal effect $\tau$ but also the subgroup effects. For instance, we may want to estimate the average causal effects among boys and girls, respectively. Without loss of generality, assume the first component of $X$ is the indicator for girls, and we are interested in estimating

$$
\tau (x _ {1}) = E \{Y (1) - Y (0) \mid X _ {1} = x _ {1} \}, \quad (x _ {1} = 1, 0).
$$

Theorem 11.5 implies that under ignorability, we also have

$$
Z \perp \perp \{Y (1), Y (0) \} \mid e (X), X _ {1} \tag {11.5}
$$

because $b ( X ) = \{ e ( X ) , X _ { 1 } \}$ is finer than $e ( X )$ and thus a balancing score. The conditional independence in (11.5) ensures ignorability holds given the propensity score, within each level of $X _ { 1 }$ . Therefore, we can perform the same analysis based on the propensity score, within each level of $X _ { 1 }$ , yielding estimates for two subgroup effects.

With the above motivation in mind, now prove Theorem 11.5.

# 11.6 Some basics of subgroup effects

This problem is related to Problem 11.5, but you can work on it independently.

Consider a standard observational study with covariates $\boldsymbol { X } = ( X _ { 1 } , X _ { 2 } )$ , where $X _ { 1 }$ denotes a binary subgroup indicator (e.g., statistics major or not statistics major) and $X _ { 2 }$ contains the rest of the covariates. The parameter of interest is the subgroup causal effect

$$
\tau (x _ {1}) = E \{Y (1) - Y (0) \mid X _ {1} = x _ {1} \}, \quad (x _ {1} = 1, 0).
$$

Show that

$$
\tau (x _ {1}) = E \left\{\frac {1 (X _ {1} = x _ {1}) Z Y}{e (X)} - \frac {1 (X _ {1} = x _ {1}) (1 - Z) Y}{1 - e (X)} \right\} \Big / \operatorname * {p r} (X _ {1} = x _ {1})
$$

and give the corresponding HT and Hajek estimators for $\tau ( x _ { 1 } )$

# 11.7 Recommended reading

The title of this chapter is the same as the title of the classic paper by Rosenbaum and Rubin (1983b). Most results in this chapter are directly drawn from their original paper.

Rubin (2007) and Rubin (2008) highlighted the importance of the design stage of observational studies for more objective causal inference

# 12

# The Doubly Robust or the Augmented Inverse Propensity Score Weighting Estimator for the Average Causal Effect

Under ignorability $Z \bot \bot \{ Y ( 1 ) , Y ( 0 ) \} \mid X$ and overlap $0 < e ( X ) < 1$ , Chapter 11 has shown two identification formulas of the average causal effect $\tau =$ $E \{ Y ( 1 ) - Y ( 0 ) \}$ . First, the outcome regression formula is

$$
\tau = E \left\{\mu_ {1} (X) \right\} - E \left\{\mu_ {0} (X) \right\} \tag {12.1}
$$

where

$$
\mu_ {1} (X) = E \{Y (1) \mid X \} = E (Y \mid Z = 1, X),
$$

$$
\mu_ {0} (X) = E \{Y (0) \mid X \} = E (Y \mid Z = 0, X)
$$

are the two conditional mean functions of the outcome given covariates under the treatment and control, respectively. Second, the IPW formula is

$$
\tau = E \left\{\frac {Z Y}{e (X)} \right\} - E \left\{\frac {(1 - Z) Y}{1 - e (X)} \right\} \tag {12.2}
$$

where

$$
e (X) = \operatorname {p r} (Z = 1 \mid X)
$$

is the propensity score introduced in Chapter 11.

The outcome regression estimator requires fitting a model for the outcome given the treatment and covariates. It is consistent if the outcome model is correctly specified. The IPW estimator requires fitting a model for the treatment given the covariates. It is consistent if the propensity score model is correctly specified.

Mathematically, we have many combinations of (12.1) and (12.2) that lead to different identification formulas of the average causal effect. Below I will discuss a particular combination that has appealing theoretical properties. This combination motivates an estimator that is consistent if either the propensity score or the outcome model is correctly specified. It is called the doubly robust estimator, championed by James Robins (Scharfstein et al., 1999; Bang and Robins, 2005).

```r
OS_est = function(z, y, x, out.family = gaussian,
truncps = c(0, 1))
{
    ## fitted propensity score
    pscore = glm(z ~ x, family = binomial) $fitted.values
    pscore = pmax(truncps[1], pmin(truncps[2], pscore))
    ## fitted potential outcomes
    outcome1 = glm(y ~ x, weights = z,
                      family = out.family) $fitted.values
    outcome0 = glm(y ~ x, weights = (1 - z),
                      family = out.family) $fitted.values
    ## outcome regression estimator
    ace.reg = mean(outcome1 - outcome0)
    ## IPW estimators
    y.treat = mean(z*y/pscore)
    y.control = mean((1 - z)*y/(1 - pscore))
    one.treat = mean(z/pscore)
    one.control = mean((1 - z)/(1 - pscore))
    ace.ipw0 = y.treat - y.control
    ace.ipw = y.treat/one.treat - y.control/one.control
    ## doubly robust estimator
    res1 = y - outcome1
    res0 = y - outcome0
    r.treat = mean(z*res1/pscore)
    r.control = mean((1 - z)*res0/(1 - pscore))
    ace.dr = ace.reg + r.treat - r.control
    return(c(ace.reg, ace.ipw0, ace.ipw, ace.dr))
} 
```

It is tedious to calculate the analytic formulas for the variances of the above estimators. The bootstrap provides convenient approximations to the variances based on resampling from $\{ Z _ { i } , X _ { i } , Y _ { i } \} _ { i = 1 } ^ { n }$ . Building upon the function OS_est above, the following function returns point estimators as well as the bootstrap standard errors.

OS_ATE $=$ function(z，y，x，n.boot $= 2*10^{\circ}2$ out.family $\equiv$ gaussian，truncps $= c(0,1)$ { point.est $=$ OS_est(z，y，x，out.family，truncps）   
##nonparametricbootstrap   
n $=$ length(z)   
x $=$ as.matrix(x)   
boot.est $=$ replicate(n.boot,{ id.boot $=$ sample(1:n，n，replace $=$ TRUE) OS.boot(z[id.boot]，y[id.boot]，x[id.boot]，], out.family，truncps)

# 12.3 Examples

}）   
boot.se $=$ apply(boot.est，1，sd)   
res $=$ rbind(point.est，boot.se)   
rownames(res） $=$ c("est"，"se")   
colnames(res） $=$ c("reg"，"HT"，"Hajek"，"DR")   
return(res)   
}

# 12.3.2 Simulation

I will use simulation to evaluate the finite-sample properties of the estimators under four scenarios:

1. both the propensity score and outcome models are correct;   
2. the propensity score model is wrong but the outcome model is correct;   
3. the propensity score model is correct but the outcome model is wrong;   
4. both the propensity score and outcome models are wrong.

I will report the average bias, the true standard error, and the average estimated standard error of the estimators over simulation.

In case 1, the data generating process is

```matlab
x = matrix(rnorm(n*2), n, 2)  
x1 = cbind(1, x)  
beta.z = c(0, 1, 1)  
pscore = 1/(1 + exp(- as.vector(x1%*%beta.z)))  
z = rbinom(n, 1, pscore)  
beta.y1 = c(1, 2, 1)  
beta.y0 = c(1, 2, 1)  
y1 = rnorm(n, x1%*%beta.y1)  
y0 = rnorm(n, x1%*%beta.y0)  
y = z*y1 + (1 - z)*y0 
```

In case 2, I modify the propensity score model to be nonlinear:

$\begin{array}{rl}\mathrm{x1} & = \mathrm{cbind}(1,\mathrm{x},\exp (\mathrm{x}))\\ \mathrm{beta.z} & = \mathrm{c}(-1,0,0,1, - 1)\\ \mathrm{pscore} & = 1 / (1 + \exp (-\mathrm{as}).\mathrm{vector}(\mathrm{x1}\% *\% \mathrm{beta.z})) \end{array}$

In case 3, I modify the outcome model to be nonlinear:

```matlab
beta.y1 = c(1, 0, 0, 0.2, -0.1)  
beta.y0 = c(1, 0, 0, -0.2, 0.1)  
y1 = rnorm(n, x1%*%beta.y1)  
y0 = rnorm(n, x1%*%beta.y0) 
```

In case 4, I modify both the propensity score and the outcome model.

We set the sample size to be $n = 5 0 0$ and generate 500 independent data sets according to the data-generating processes above. In case 1,

<table><tr><td></td><td>reg</td><td>HT</td><td>Hajek</td><td>DR</td></tr><tr><td>ave.bias</td><td>0.00</td><td>0.02</td><td>0.03</td><td>0.01</td></tr><tr><td>true.se</td><td>0.11</td><td>0.28</td><td>0.26</td><td>0.13</td></tr><tr><td>est.se</td><td>0.10</td><td>0.25</td><td>0.23</td><td>0.12</td></tr></table>

All estimators are nearly unbiased. The two weighting estimators have larger variances. In case 2,

<table><tr><td></td><td>reg</td><td>HT</td><td>Hajek</td><td>DR</td></tr><tr><td>ave.bias</td><td>0.00</td><td>-0.76</td><td>-0.75</td><td>-0.01</td></tr><tr><td>true.se</td><td>0.12</td><td>0.59</td><td>0.47</td><td>0.18</td></tr><tr><td>est.se</td><td>0.13</td><td>0.50</td><td>0.38</td><td>0.18</td></tr></table>

The two weighting estimators are severely biased due to the misspecification of the propensity score model. The outcome regression and doubly robust estimators are nearly unbiased.

In case 3,

<table><tr><td></td><td>reg</td><td>HT</td><td>Hajek</td><td>DR</td></tr><tr><td>ave.bias</td><td>-0.05</td><td>0.00</td><td>-0.01</td><td>0.00</td></tr><tr><td>true.se</td><td>0.11</td><td>0.15</td><td>0.14</td><td>0.14</td></tr><tr><td>est.se</td><td>0.11</td><td>0.14</td><td>0.13</td><td>0.14</td></tr></table>

The outcome regression estimator has a larger bias than the other three estimators due to the misspecification of the outcome model. The weighting and doubly robust estimators are nearly unbiased.

In case 4,

<table><tr><td></td><td>reg</td><td>HT</td><td>Hajek</td><td>DR</td></tr><tr><td>ave.bias</td><td>-0.08</td><td>0.11</td><td>-0.07</td><td>0.16</td></tr><tr><td>true.se</td><td>0.13</td><td>0.32</td><td>0.20</td><td>0.41</td></tr><tr><td>est.se</td><td>0.13</td><td>0.25</td><td>0.16</td><td>0.26</td></tr></table>

All estimators are biased because both the propensity score and outcome models are wrong. The HT and doubly robust estimator has the largest bias. When both models are wrong, the doubly robust estimator appears to be doubly fragile.

In all the cases above, the bootstrap standard errors are close to the true ones when the estimators are nearly unbiased for the true average causal effect.

# 12.3.3 Applications

Revisiting Example 10.3, we obtain the following estimators and bootstrap standard errors:

<table><tr><td></td><td>reg</td><td>HT</td><td>Hajek</td><td>DR</td></tr><tr><td>est</td><td>-0.017</td><td>-1.516</td><td>-0.156</td><td>-0.019</td></tr><tr><td>se</td><td>0.230</td><td>0.492</td><td>0.246</td><td>0.233</td></tr></table>

The two weighting estimators are much larger than the other two estimators. Truncating the estimated propensity score at [0.1, 0.9], we obtain the following estimators and bootstrap standard errors:

<table><tr><td></td><td>reg</td><td>HT</td><td>Hajek</td><td>DR</td></tr><tr><td>est</td><td>-0.017</td><td>-0.713</td><td>-0.054</td><td>-0.043</td></tr><tr><td>se</td><td>0.223</td><td>0.422</td><td>0.235</td><td>0.231</td></tr></table>

The Hajek estimator becomes much closer to the outcome regression and doubly robust estimators, while the Horvitz–Thompson estimator is still an outlier.

# 12.4 Some further discussion

Recall the proof of Theorem 12.1, the key for the double robustness property is the product structure in

$$
\tilde {\mu} _ {1} ^ {\mathrm {d r}} - E \{Y (1) \} = E \left[ \frac {e (X) - e (X , \alpha)}{e (X , \alpha)} \times \{\mu_ {1} (X) - \mu_ {1} (X, \beta_ {1}) \} \right],
$$

which ensures that the estimation error is zero if either $e ( X ) = e ( X , \alpha )$ or $\mu _ { 1 } ( X ) = \mu _ { 1 } ( X , \beta _ { 1 } )$ . This delicate structure renders the doubly robust estimator possibly doubly fragile when both the propensity score and the outcome models are misspecified. The product of two errors multiply to yield potentially much larger errors. The simulation in Chapter 12.3.2 confirms this point.

Kang and Schafer (2007) criticized the doubly robust estimator based on simulation studies. They found that the finite-sample performance of the doubly robust estimator can be even wilder than the simple outcome regression and IPW estimators. Despite the critique from Kang and Schafer (2007), the doubly robust estimator has been a standard strategy in causal inference since the seminal work of Scharfstein et al. (1999). Recently, it was resurrected in the theoretical statistics and econometrics literature with a fancier name “double machine learning” (Chernozhukov et al., 2018). The basic idea is to replace the working models for the propensity score and outcome with machine learning tools which can be viewed as more flexible models than the traditional parametric models.

# 12.5 Homework problems

# 12.1 A sanity check

Consider the case in which the covariate is discrete $X \in \{ 1 , \ldots , K \}$ and the parameter of interest is $\tau$ . Without imposing any model assumptions, the estimated propensity score $\hat { e } ( X )$ equals ${ \hat { e } } _ { [ k ] } = { \hat { \mathrm { p r } } } ( Z = 1 \mid X = k )$ , the proportion of units receiving the treatment, and the estimated outcome means are the sample means of the outcomes $\hat { \bar { Y } } _ { [ k ] } ( 1 ) ~ = ~ \hat { E } ( Y ~ \vert ~ Z ~ = ~ 1 , X ~ = ~ k )$ and $\hat { \bar { Y } } _ { [ k ] } ( 0 ) ~ = ~ \hat { E } ( Y ~ \vert ~ Z ~ = ~ 0 , X ~ = ~ k )$ ) under treatment, within stratum $X = k$ $k = 1 , \ldots , K ,$ ). Show that the stratified estimator, outcome regression estimator, HT estimator, Hajek estimator, and doubly robust estimator are all identical numerically.

# 12.2 An alternative form of the doubly robust estimator for $\tau$

Motivated by (12.7), we have an alternative form of the doubly robust estimator for $\mu _ { 1 } = E \{ Y ( 1 ) \}$ :

$$
\tilde {\mu} _ {1} ^ {\mathrm {d r 2}} = \frac {E \left[ \frac {Z \{Y - \mu_ {1} (X , \beta_ {1}) \}}{e (X , \alpha)} \right]}{E \left[ \frac {Z}{e (X , \alpha)} \right]} + E \{\mu_ {1} (X, \beta_ {1}) \}.
$$

Show that $\tilde { \mu } _ { 1 } ^ { \mathrm { d r 2 } } = \mu _ { 1 }$ if either $e ( X , \alpha ) = e ( X )$ or $\mu _ { 1 } ( X , \beta _ { 1 } ) = \mu _ { 1 } ( X )$ . Give the analogous formula for estimating $\mu _ { 0 }$ . Give the sample analog of the doubly robust estimator for $\tau$ based on these formulas.

Remark: This form of doubly robust estimator appeared in Robins et al. (2007).

# 12.3 An upper bound of the bias of the doubly robust estimator

Consider the population version of the doubly robust estimator $\tilde { \mu } _ { 1 } ^ { \mathrm { d r } }$ for $E \{ Y ( 1 ) \}$ . Show that

$$
| \tilde {\mu} _ {1} ^ {\mathrm {d r}} - E \{Y (1) \} | \leq \sqrt {E \left[ \frac {\{e (X) - e (X , \alpha) \} ^ {2}}{e (X , \alpha) ^ {2}} \right] \times E \left[ \{\mu_ {1} (X) - \mu_ {1} (X , \beta_ {1}) \} ^ {2} \right]}.
$$

Find the analogous upper bound for the bias of $\tilde { \mu } _ { 0 } ^ { \mathrm { d r } }$ for $E \{ Y ( 0 ) \}$

Remark: You may find Section A.1.4 useful for the proof.

# 12.4 Data analysis of Example 10.1

Analyze the dataset cps1re74.csv using the methods discussed so far.

# 12.5 Analyzing a dataset from the Karolinska Institute

Rubin (2008) used the dataset karolinska.txt to illustrate the ideas of causal inference in observational studies. The dataset has 158 cardia cancer patients diagnosed between 1988 and 1995 in Central and Northern Sweden, 79 diagnosed at large volume hospitals, defined as treating more than ten patients with cardia cancer during that period, and 79 diagnosed at the remaining small volume hospitals. The treatment $_ { z }$ is the indicator of whether a patient was diagnosed at a large volume hospital. The outcome y is whether the patient survived longer than 1 year after the diagnosis. The covariates x contain information about age, whether a patient was from a rural area, and whether a patient was male.

```txt
karolinska = read.table("karolinska.txt", header = TRUE)  
z = karolinska$hvdiag  
y = 1 - (karolinska$year survived == 1)  
x = as.matrix(karolinska[, c(3, 4, 5)]) 
```

Analyze the dataset using the methods discussed so far.

# 12.6 Recommended reading

Lunceford and Davidian (2004) gave a review and comparison of many methods discussed in Chapters 11 and 12.

estimated propensity score $1 / \hat { e } ( X _ { i } )$ will be large, and at the same time, it will be matched to many control units, resulting in large $K _ { i }$ and thus large $1 + K _ { i } / M$ . However, this connection also raised an obvious question regarding matching. With a fixed $M$ , the estimator $1 + K _ { i } / M$ for $1 / e ( X _ { i } )$ will be very noisy. Allowing $M$ to grow with the sampling size is likely to improve the matching-based nonparametric estimator for the propensity score and thus improve the asymptotic properties of the matching and bias-corrected matching estimators. Lin et al. (2023) provided a formal theory that once we allow $M$ to grow at a proper rate, the bias-corrected matching estimator $\hat { \tau } ^ { \mathrm { m b c } }$ can achieve similar properties as the doubly robust estimator.

# 15.4 Matching estimator for the average causal effect on the treated

For the average causal effect on the treated

$$
\tau_ {\mathrm {T}} = E (Y \mid Z = 1) - E \{Y (0) \mid Z = 1 \},
$$

we only need to impute the missing potential outcomes under control for all the treated units, resulting in the following estimator

$$
\hat {\tau} _ {\mathrm {T}} ^ {\mathrm {m}} = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} \{Y _ {i} - \hat {Y} _ {i} (0) \}.
$$

Again it is biased with multidimensional $X$ . Otsu and Rai (2017) propose to estimate its bias by

$$
\hat {B} _ {\mathrm {T}} = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} \hat {B} _ {\mathrm {T}, i}
$$

where

$$
\hat {B} _ {\mathrm {T}, i} = M ^ {- 1} \sum_ {k \in J _ {i}} \{\hat {\mu} _ {0} (X _ {i}) - \hat {\mu} _ {0} (X _ {k}) \}
$$

corrects the bias due to the mismatch of covariates for a treated unit with $Z _ { i } = 1$ .

The final bias-corrected estimator is

$$
\hat {\tau} _ {\mathrm {T}} ^ {\mathrm {m b c}} = \hat {\tau} _ {\mathrm {T}} ^ {\mathrm {m}} - \hat {B} _ {\mathrm {T}},
$$

which has the following linear expansion.

Proposition 15.3 We have

$$
\hat {\tau} _ {\mathrm {T}} ^ {\mathrm {m b c}} = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} \hat {\psi} _ {\mathrm {T}, i}, \tag {15.2}
$$

where

$$
\hat {\psi} _ {\mathrm {T}, i} = Z _ {i} \left\{Y _ {i} - \hat {\mu} _ {0} (X _ {i}) \right\} - (1 - Z _ {i}) K _ {i} / M \left\{Y _ {i} - \hat {\mu} _ {0} (X _ {i}) \right\}.
$$

I leave the proof to Problem 15.1. Motivated by Otsu and Rai (2017), we can view $\hat { \tau } _ { \mathrm { T } } ^ { \mathrm { m b c } }$ as $n / n _ { 1 }$ multiplied by the sample average of the $\hat { \psi } _ { \mathrm { T } , i }$ ’s, so an intuitive variance estimator is

$$
\hat {V} _ {\mathrm {T}} ^ {\mathrm {m b c}} = \left(\frac {n}{n _ {1}}\right) ^ {2} \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} (\hat {\psi} _ {\mathrm {T}, i} - \hat {\tau} _ {\mathrm {T}} ^ {\mathrm {m b c}} n _ {1} / n) ^ {2} = \frac {1}{n _ {1} ^ {2}} \sum_ {i = 1} ^ {n} (\hat {\psi} _ {\mathrm {T}, i} - \hat {\tau} _ {\mathrm {T}} ^ {\mathrm {m b c}} n _ {1} / n) ^ {2}.
$$

Similar to the discussion in Section 15.3.2, we can compare the doubly robust and bias-corrected matching estimators with the outcome regression estimator. For the average causal effect on the treated units $\tau _ { \mathrm { T } }$ , recall the outcome regression estimator

$$
\hat {\tau} _ {\mathrm {T}} ^ {\mathrm {r e g}} = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} \left\{Y _ {i} - \hat {\mu} _ {0} \left(X _ {i}\right) \right\},
$$

and the doubly robust estimator

$$
\hat {\tau} _ {\mathrm {T}} ^ {\mathrm {d r}} = \hat {\tau} _ {\mathrm {T}} ^ {\mathrm {r e g}} - n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} \frac {\hat {e} (X _ {i})}{1 - \hat {e} (X _ {i})} (1 - Z _ {i}) \hat {R} _ {i}.
$$

Furthermore, we can verify that $\hat { \tau } _ { \mathrm { T } } ^ { \mathrm { m b c } }$ has a form similar to $\hat { \tau } _ { \mathrm { T } } ^ { \mathrm { d r } }$

Proposition 15.4 The bias correction matching estimator for $\tau _ { \mathrm { T } }$ equals

$$
\hat {\tau} _ {\mathrm {T}} ^ {\mathrm {m b c}} = \hat {\tau} _ {\mathrm {T}} ^ {\mathrm {r e g}} - n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} \frac {K _ {i}}{M} (1 - Z _ {i}) \hat {R} _ {i}.
$$

I leave the proof of Proposition 15.4 as Problem 15.3. Proposition 15.4 suggests that matching essentially uses $K _ { i } / M$ to estimate the odds of the treatment given covariates.

# 15.5 A case study

# 15.5.1 Experimental data

Now I revisit the LaLonde data using Sekhon (2011)’s Matching package. We have used this package several times for the dataset lalonde, and now we will use its key function Match. The experimental part gives us the following results:

# 15.5 A case study

```txt
> library("car")
> library("Matching")
>
> ## Chapter 15.5.1
> ## experimental data
> data("lalonde")
> y = lalonde$re78
> z = lalonde$treat
> x = as.matrix(lalonde[, c("age", "educ", "black",
+ "hisp", "married", "nodegr",
+ "re74", "re75")])
>
>
## analysis the randomized experiment
> neymanols = lm(y ~ z)
> fisherols = lm(y ~ z + x)
> xc = scale(x)
> linols = lm(y ~ z*xc)
> resols = c(neymanols$coef[2],
+ fisherols$coef[2],
+ linols$coef[2],
+ sqrt(hccm(neymanols, type = "hc2") [2, 2]),
+ sqrt(hccm(fisherols, type = "hc2") [2, 2]),
+ sqrt(hccm(linols, type = "hc2") [2, 2]))
> resols = matrix(resols, 3, 2)
> rownames(resols) = c("neyman", "fisher", "lin")
> colnames(resols) = c("est", "se")
> resols
est se
neyman 1794.343 670.9967
fisher 1676.343 677.0493
lin 1621.584 694.7217 
```

All regression estimators show positive significant results on the job training program. We can analyze the data as if it is an observational study based on 1-1 matching, yielding the following results:

>matchest.adj $=$ Match $(Y = y$ ，Tr $= z$ ， $X = x$ ，BiasAdjust $=$ TRUE)   
>summary(matchest.adj)   
Estimate. 2119.7   
AI SE. .876.42   
T-stat. 2.4185   
p.val. 0.015583   
Original number of observations. 445   
Original number of treated obs. 185   
Matched number of observations. 185   
Matched number of observations (unweighted). 268

Both the point estimator and standard error increase, but qualitatively, the conclusion remains the same.

# 15.5.2 Observational data

Then I revisit the observational counterpart of the data:

```r
> dat <- read.table("cps1re74.csv", header = TRUE)
> dat$u74 <- as.numeric(da$re74==0)
> dat$u75 <- as.numeric(da$re75==0)
> y = dat$re78
> z = dat$treat
> x = as.matrix(da[, c("age", "educ", "black",
+ "hispan", "married", "nodegree",
+ "re74", "re75", "u74", "u75"))]) 
```

If we use simple OLS estimators, the results are far from the experimental benchmark and are sensitive to the specification of the regression:

```txt
> neymanols = lm(y ~ z)
> fisherols = lm(y ~ z + x)
> xc = scale(x)
> linols = lm(y ~ z*xc)
> resols = c(neymanols$coef[2],
+     fisherols$coef[2],
+     linols$coef[2],
+     sqrt(hccm(neymanols, type = "hc2") [2, 2]),
+     sqrt(hccm(fisherols, type = "hc2") [2, 2]),
+     sqrt(hccm(linols, type = "hc2") [2, 2]))
> resols = matrix(resols, 3, 2)
> rnames(resols) = c("neyman", "fisher", "lin")
> colnames(resols) = c("est", "se")
> resols
est se
neyman -8506.495 583.4426
fisher 1067.546 628.4389
lin -4265.801 3211.7718 
```

However, if we use 1-1 matching, the results almost recover those based on the experimental data:

>matchest $\equiv$ Match(Y=y，Tr $= z$ ，X=x，BiasAdjust $\equiv$ TRUE)   
>summary（matchest）   
Estimate. 1747.8   
AI SE. .916.59   
T-stat. 1.9068   
p.val. 0.056543   
Original number of observations.. 16177   
Original number of treated obs. 185

Matched number of observations . 1 8 5

Matched number of observations ( unweighted ). 248

Ignoring the ties in the matched data, we can also use the matched-pairs analysis, which again yields results similar to those based on the experimental data:

```txt
>diff = y[matchest\\(index.treated] - +y[matchest\\)index.control] > round (summary(lm(diff ~ 1))\\(coef [1, ], 2) Estimate Std. Error t value \)\operatorname*{Pr}(\text{>}|\text{t}|)$ 1581.44 558.55 2.83 0.01 > diff.x = x[matchest\\)index.treated, ] - +x[matchest\\(index.control, ] > round (summary(lm(diff ~ diff.x))\\)coef [1, ], 2) Estimate Std. Error t value \)\operatorname*{Pr}(\text{>}|\text{t}|)$ 1842.06 578.37 3.18 0.00 
```

# 15.5.3 Covariate balance checks

Moreover, we can use simple OLS to check covariate balance. Before matching, the covariates are highly imbalanced, signified by many stars associated with the coefficients.

> lm . before = lm ( z ~ x )

> summary ( lm . before )

Residuals :   
```txt
Min 1Q Median 3Q Max -0.18508 -0.01057 0.00303 0.01018 1.01355
```

Coefficients :   
Estimate Std. Error t value $\mathrm{Pr}(|t|)$ (Intercept) 1.404e-03 6.326e-03 0.222 0.8243 xage -4.043e-04 8.512e-05 -4.750 2.05e-06 *** xeduc 3.220e-04 4.073e-04 0.790 0.4293 xblack 1.070e-01 2.902e-03 36.871 < 2e-16 *** xhispan 6.377e-03 3.103e-03 2.055 0.0399 * xmarried -1.525e-02 2.023e-03 -7.537 5.06e-14 *** xnodegree 1.345e-02 2.523e-03 5.331 9.89e-08 *** xre74 7.601e-07 1.806e-07 4.208 2.59e-05 *** xre75 -1.231e-07 1.829e-07 -0.673 0.5011 xu74 4.224e-02 3.271e-03 12.914 < 2e-16 *** xu75 2.424e-02 3.399e-03 7.133 1.02e-12 ***

However, after matching, the covariates are well-balanced, signified by the absence of stars for all coefficients.

>lm.after $= \mathrm{lm(z}$ ~x,

+ subset = c(matchest\ $index.treated, + matchest\$ index.control)) > summary(lm.after)

Residuals :

```txt
Min 1Q Median 3Q Max -0.66864 -0.49161 -0.03679 0.50378 0.65122
```

Coefficients :

```txt
Estimate Std. Error t value Pr(>|t|)  
(Intercept) 6.003e-01 2.427e-01 2.474 0.0137  
xage 3.199e-03 3.427e-03 0.933 0.3511  
xeduc -1.501e-02 1.634e-02 -0.918 0.3590  
xblack 6.141e-05 7.408e-02 0.001 0.9993  
xhispan 1.391e-02 1.208e-01 0.115 0.9084  
xmarried -1.328e-02 6.729e-02 -0.197 0.8437  
xnodegree -3.023e-02 7.144e-02 -0.423 0.6723  
xre74 6.754e-06 9.864e-06 0.685 0.4939  
xre75 -9.848e-06 1.279e-05 -0.770 0.4417  
xu74 2.179e-02 1.027e-01 0.212 0.8321  
xu75 -2.642e-02 8.327e-02 -0.317 0.7512 
```

# 15.6 Discussion

With many covariates, matching based on the original covariates may suffer from the curse of dimensionality. Rosenbaum and Rubin (1983b) suggested to use matching based on the estimated propensity score. Abadie and Imbens (2016) provided a form theory for this strategy.

# 15.7 Homework Problems

15.1 Linear expansions of the bias-corrected estimators

Prove Propositions 15.1 and 15.3.

15.2 Doubly robust form of the bias-corrected matching estimator for τ

Prove Proposition 15.2.

15.3 Doubly robust form of the bias-corrected matching estimator for $\tau _ { \mathrm { T } }$

Prove Proposition 15.4.

# 15.4 Revisit Example 10.3

Analyze the dataset in Example 10.3 using the matching estimator. Compare the results with previous results. You should check the covariate balance before and after matching. You can also choose a different number of matches for the matching estimator. Moreover, you can even apply various estimators to the matched data. Are your results sensitive to your choices?

# 15.5 Revisit Chapter 15.5

Chapter 15.5 analyzed the LaLonde observational study using matching. Matching performs well because it gives an estimator that is close to the experimental gold standard. Reanalyze the data using the outcome regression, propensity score stratification, two IPW, and the doubly robust estimators. Compare the results to the matching estimator and to the estimator from the experimental gold standard.

Note that you have many choices. For example, the number of strata for stratification and the threshold to trim to data based on the estimated propensity scores. You may consider fitting different propensity score and outcome models, e.g., including some quadratic terms of the basic covariates. You can even apply these estimators to the matched data.

This is a classic dataset and hundreds of papers have used it. You can read some references (Dehejia and Wahba, 1999; Hainmueller, 2012) and you can also be creative in your data analysis.

# 15.6 Data re-analyses

Ho et al. (2007) is an influential paper in political science, based on which the authors have developed an R package MatchIt (Ho et al., 2011). Ho et al. (2007) analyzed two datasets, both of which are available from the Harvard Dataverse.

Re-analyze these two datasets using the methods discussed so far. You can also try other methods as long as you can justify them.

# 15.7 Recommended reading

The literature on matching estimators is massive, and three excellent review papers are Sekhon (2009), Stuart (2010), and Imbens (2015).

# Part IV

# Difficulties and challenges of observational studies

# Difficulties of Unconfoundedness in Observational Studies for Causal Effects

Part III of this book discusses causal inference with observational studies under two assumptions: unconfoundedness and overlap. Both are strong assumptions and are likely to be violated in practice. This chapter will discuss the difficulties of the unconfoundedness assumption. Chapters 17–19 will discuss various strategies for sensitivity analysis in observational studies with unmeasured confounding. Chapter 20 will discuss the difficulties of the overlap assumption.

# 16.1 Some basics of the causal diagram

Pearl (1995) introduced the causal diagram as a powerful tool for causal inference in empirical research. Pearl (2000) is a textbook on the causal diagram. Here I introduce the causal diagram as an intuitive tool for illustrating the causal relationships among variables.

For example, if we have the causal diagram

![](images/23138e42145a6c54e92509846e16af0c9d9c706c69229fe42e94c4b85554564d.jpg)

and focus on the causal effect of $Z$ on $Y$ , we can read it as the following data-generating process:

$$
\left\{ \begin{array}{l} X \sim F _ {X} (x), \\ Z = f _ {Z} (X, \varepsilon_ {Z}), \\ Y (z) = f _ {Y} (X, z, \varepsilon_ {Y} (z)), \end{array} \right.
$$

where $\varepsilon _ { Z } \bot \bot \varepsilon _ { Y } ( z )$ for both $z = 0 , 1$ . In the above, covariates $X$ are generated from a distribution $F _ { X } ( x )$ , the treatment assignment is a function of $X$ with a random error term $\varepsilon _ { Z }$ , and the potential outcome $Y ( z )$ is a function of $X$ , $z$ and a random error term $\varepsilon _ { Y } ( z )$ . We can easily read from the equations that $Z \bot Y ( z ) \mid X$ , i.e., the unconfoundedness assumption holds.

Remark: First verify that if $\mathrm { R R } _ { Z Y | U = 0 } = \mathrm { R R } _ { Z Y | U = 1 }$ then

$$
\mathrm {R R} _ {Z Y} ^ {\text {t r u e}} = \mathrm {R R} _ {Z Y | U = 0} = \mathrm {R R} _ {Z Y | U = 1}.
$$

This identity shows the collapsibility of the risk ratio. In epidemiology, the risk ratio is a collapsible measure of association.

Schlesselman (1978)’s formula does not assume conditional independence $Z \bot \bot Y \mid U$ , but assumes homogeneity of the $Z$ - $Y$ and $U$ - $Y$ risk ratios. It is a classic formula for sensitivity analysis. It is an identity that is simple to implement with pre-specified

$$
\{\gamma , \operatorname {p r} (U = 1 \mid Z = 1), \operatorname {p r} (U = 1 \mid Z = 0) \}.
$$

However, it involves more sensitivity parameters than Theorem 17.1. Even though Theorem 17.1 only gives an inequality, it is not a loose inequality compared to Schlesselman (1978)’s formula under stronger assumptions. With Theorem 17.1, Schlesselman (1978)’s formula is only of historical interest.

# 17.5 E-value after logistic regression: data analysis

This problem uses the same dataset as Example 17.2.

Report the E-value for the outcome preeclampsia.

# 17.6 Cornfield-type inequalities for the risk difference

Consider binary $Z , Y , U$ , and condition on $X$ implicitly. Assume latent ignorability given $U$ . Show that under $Z \bot Y \mid U$ , we have

$$
\mathrm {R D} _ {Z Y} ^ {\mathrm {o b s}} = \mathrm {R D} _ {Z U} \times \mathrm {R D} _ {U Y} \tag {17.3}
$$

where $\mathrm { R D } _ { Z Y } ^ { \mathrm { o b s } }$ is the observed risk difference of $Z$ on $Y$ , and $\mathrm { R D } _ { Z U }$ and $\operatorname { R D } _ { U Y }$ are the treatment-confounder and confounder-outcome risk differences, respectively (recall the definition of the risk difference in Chapter 1.2.2).

Remark: Without loss of generality, assume that rdobsZY , rdZU , rdUY are all positive. Then (17.3) implies that

$$
\min \left(\mathrm {R D} _ {Z U}, \mathrm {R D} _ {U Y}\right) \geq \mathrm {R D} _ {Z Y} ^ {\mathrm {o b s}}
$$

and

$$
\max  \left(\mathrm {R D} _ {Z U}, \mathrm {R D} _ {U Y}\right) \geq \sqrt {\mathrm {R D} _ {Z Y} ^ {\mathrm {o b s}}}.
$$

These are the Cornfield inequalities for the risk difference with a binary confounder. They show that for an unmeasured confounder to explain away an observed risk difference $\mathrm { R D } _ { Z Y } ^ { \mathrm { o b s } }$ , the treatment-confounder and confounderoutcome risk differences must both be larger than $\mathrm { R D } _ { Z Y } ^ { \mathrm { o b s } }$ dobsZY , and the maximum of them must be larger than the square root of rdobsZY .

Cornfield et al. (1959) obtained, but did not appreciate the significance of (17.3). Gastwirth et al. (1998) and Poole (2010) discussed the first Cornfield

condition for the risk difference, and Ding and VanderWeele (2014) discussed the second.

Ding and VanderWeele (2014) also derived more general results without assuming a binary $U$ . Unfortunately, the results for a general $U$ are weaker than those above for a binary $U$ , that is, the inequalities become looser with more levels of $U$ . This motivated Ding and VanderWeele (2016) to focus on the Cornfield inequalities for the risk ratio, which do not deteriorate with more levels of $U$ .

# 17.7 Recommended reading

Ding and VanderWeele (2016) extended and unified the Cornfield-type sensitivity analysis, which is the theoretical basis for the notion of E-value.

# Sensitivity Analysis for the Average Causal Effect with Unmeasured Confounding

Cornfield-type sensitivity analysis works best for binary outcomes on the risk ratio scale, conditional on the observed covariates. Although Ding and VanderWeele (2016) also proposed Cornfield-type sensitivity analysis methods for the average causal effect, they are not general enough and are not convenient to apply. Below I give a more direct approach to sensitivity analysis based on the conditional expectations of the potential outcomes. The advantage of this approach is that it can deal with commonly used estimators for the average causal effect under the sensitivity analysis framework. The idea appeared in the early work of Robins (1999) and Scharfstein et al. (1999). This chapter is based on Lu and Ding (2023)’s recent formulation.

The approach is closely related to the idea of deriving worse-case bounds on the average potential outcomes. I will first review the simpler idea of bounds, and then extend the approach to sensitivity analysis.

# 18.1 Introduction

Recall the canonical setup of an observational study with $\{ Z _ { i } , X _ { i } , Y _ { i } ( 1 ) , Y _ { i } ( 0 ) \} _ { i = 1 } ^ { n } \stackrel { \mathrm { l l } \mathrm { \scriptsize { D } } } { \sim }$ $\{ Z , X , Y ( 1 ) , Y ( 0 ) \}$ and focus on the average causal effect

$$
\tau = E \{Y (1) - Y (0) \}.
$$

It decomposes to

$$
\begin{array}{l} \tau = \left[ E (Y \mid Z = 1) \Pr (Z = 1) + E \{Y (1) \mid Z = 0 \} \Pr (Z = 0) \right] \\ - \left[ E \{Y (0) \mid Z = 1 \} \Pr (Z = 1) + E (Y \mid Z = 0) \Pr (Z = 0) \right]. \\ \end{array}
$$

So the fundamental difficulty is to estimate the counterfactual means

$$
E \{Y (1) \mid Z = 0 \}, \qquad E \{Y (0) \mid Z = 1 \}.
$$

There are in general two extreme strategies to estimate them.

We have discussed the first strategy in Part III, which relies on ignorability.

TABLE 18.1: Science Table with bounded outcome $[ y , { \overline { { y } } } ]$ , where $\underline { { y } }$ and $\bar { y }$ are two constants   

<table><tr><td>Z</td><td>Y(1)</td><td>Y(0)</td><td>Lower Y(1)</td><td>Upper Y(1)</td><td>Lower Y(0)</td><td>Upper Y(0)</td></tr><tr><td>1</td><td>Y1(1)</td><td>?</td><td>Y1(1)</td><td>Y1(1)</td><td>\u</td><td>\u</td></tr><tr><td>\(\vdots\)</td><td>\(\vdots\)</td><td>\(\vdots\)</td><td>\(\vdots\)</td><td>\(\vdots\)</td><td>\(\vdots\)</td><td>\(\vdots\)</td></tr><tr><td>1</td><td>\(Y_{n_1}(1)\)</td><td>?</td><td>\(Y_{n_1}(1)\)</td><td>\(Y_{n_1}(1)\)</td><td>\u</td><td>\u</td></tr><tr><td>0</td><td>?</td><td>\(Y_{n_1+1}(0)\)</td><td>\u</td><td>\u</td><td>\(Y_{n_1+1}(0)\)</td><td>\(Y_{n_1+1}(0)\)</td></tr><tr><td>\(\vdots\)</td><td>\(\vdots\)</td><td>\(\vdots\)</td><td>\(\vdots\)</td><td>\(\vdots\)</td><td>\(\vdots\)</td><td>\(\vdots\)</td></tr><tr><td>0</td><td>?</td><td>\(Y_n(0)\)</td><td>\u</td><td>\u</td><td>\(Y_n(0)\)</td><td>\(Y_n(0)\)</td></tr></table>

Assuming

$$
E \{Y (1) \mid Z = 1, X \} = E \{Y (1) \mid Z = 0, X \},
$$

$$
E \{Y (0) \mid Z = 1, X \} = E \{Y (0) \mid Z = 0, X \},
$$

we can identify the counterfactual means by the observables:

$$
E \{Y (1) \mid Z = 0 \} = E \left\{E \left(Y \mid Z = 1, X\right) \mid Z = 0 \right\}
$$

and, similarly,

$$
E \left\{Y (0) \mid Z = 1 \right\} = E \left\{E \left(Y \mid Z = 0, X\right) \mid Z = 1 \right\}.
$$

The second strategy in the next section assumes nothing except that the outcomes are bounded between $\underline { { y } }$ and $y$ . This is natural for binary outcomes with $\underline { { y } } = 0$ and $\overline { { y } } = 1$ . With this assumption, the two counterfactual means are also bounded between $\underline { { y } }$ and $y$ , which implies the worst-case bounds on $\tau$ . Table 18.1 illustrates the basic idea and Chapter 18.2 below reviews this strategy in more detail.

# 18.2 Manski-type worse-case bounds on the average causal effect without assumptions

Assume that the outcome is bounded between $\underline { { y } }$ and $\overline { y }$ . From the decomposition

$$
E \{Y (1) \} = E \{Y (1) \mid Z = 1 \} \Pr (Z = 1) + E \{Y (1) \mid Z = 0 \} \Pr (Z = 0),
$$

we can derive that $E \{ Y ( 1 ) \}$ has lower bound

$$
E \{Y \mid Z = 1 \} \Pr (Z = 1) + \underline {{y}} \Pr (Z = 0)
$$

# 18.2 Manski-type worse-case bounds on the average causal effect without assumptions 249

and upper bound

$$
E \{Y \mid Z = 1 \} \Pr (Z = 1) + \bar {y} \Pr (Z = 0).
$$

Similarly, from the decomposition

$$
E \{Y (0) \} = E \{Y (0) \mid Z = 1 \} \Pr (Z = 1) + E \{Y (0) \mid Z = 0 \} \Pr (Z = 0),
$$

we can derive that $E \{ Y ( 0 ) \}$ has lower bound

$$
\underline {{y}} \operatorname {p r} (Z = 1) + E \{Y \mid Z = 0 \} \operatorname {p r} (Z = 0)
$$

and upper bound

$$
\overline {{y}} \operatorname {p r} (Z = 1) + E \{Y \mid Z = 0 \} \operatorname {p r} (Z = 0).
$$

Combining these bounds, we can derive that the average causal effect $\tau =$ $E \{ Y ( 1 ) \} - E \{ Y ( 0 ) \}$ has the lower bound

$$
E \{Y \mid Z = 1 \} \operatorname {p r} (Z = 1) + \underline {{y}} \operatorname {p r} (Z = 0) - \bar {y} \operatorname {p r} (Z = 1) - E \{Y \mid Z = 0 \} \operatorname {p r} (Z = 0)
$$

and the upper bound

$$
E \{Y \mid Z = 1 \} \operatorname {p r} (Z = 1) + \bar {y} \operatorname {p r} (Z = 0) - \underline {{y}} \operatorname {p r} (Z = 1) - E \{Y \mid Z = 0 \} \operatorname {p r} (Z = 0).
$$

The length of the bounds is ${ \overline { { y } } } - y$ . The bounds are not informative but are better than the a priori bounds $[ \underline { { y } } - \overline { { y } } , \overline { { y } } - \underline { { y } } ]$ with length $2 ( { \overline { { y } } } - y )$ . Without further assumptions, the observed data distribution does not uniquely determine $\tau$ . In this case, we say that $\tau$ is partially identified, with the formal definition below.

Definition 18.1 (partial identification) A parameter $\theta$ is partially identified if the observed data distribution is compatible with multiple values of $\theta$ .

Compare Definitions 10.1 and 18.1. If the parameter $\theta$ is uniquely determined by the observed data distribution, then it is identifiable; otherwise, it is only partially identifiable. Therefore, $\tau$ is identifiable with the ignorability assumption, but only partially identifiable without the ignorability assumption.

Cochran (1953) used the idea of worse-case bounds in surveys with missing data but abandoned the idea because it often gives very conservative results. Similarly, the above worst-case bounds on $\tau$ are often uninteresting from a practical perspective because they often cover 0. Moreover, this strategy does not apply to the settings with unbounded outcomes.

Manski applied the idea to causal inference (Manski, 1990) and many other econometric models (Manski, 2003). This idea of bounding causal parameters with minimal assumptions is powerful when coupled with other qualitative

assumptions. Manski (2003) surveyed many strategies. For instance, we may believe that the treatment does not harm any units, so the monotonicity assumption holds: $Y ( 1 ) \ge Y ( 0 )$ . Then the lower bound on $\tau$ is zero but the upper bound is unchanged. Another type of assumption is $Z = I \{ Y ( 1 ) \geq$ $Y ( 0 ) \}$ , that is, the treatment selection is based on the difference between the latent potential outcomes. This assumption can also improve the bounds on $\tau$ . A more detailed discussion of this approach is beyond the scope of this book.

# 18.3 Sensitivity analysis for the average causal effect

The first strategy is optimistic and assumes that the potential outcomes do not differ across treatment and control groups, conditional on the observed covariates. The second strategy is pessimistic and does not infer the counterfactual means based on the observed data at all. The following strategy is in-between.

# 18.3.1 Identification formulas

Define

$$
\frac {E \{Y (1) \mid Z = 1 , X \}}{E \{Y (1) \mid Z = 0 , X \}} = \varepsilon_ {1} (X),
$$

$$
\frac {E \{Y (0) \mid Z = 1 , X \}}{E \{Y (0) \mid Z = 0 , X \}} = \varepsilon_ {0} (X),
$$

which are the sensitivity parameters. For simplicity, we can further assume that they are constant independent of $X$ . In practice, we need to fix them or vary them in a pre-specified range. Recall that $\mu _ { 1 } ( X ) = E ( Y \mid Z = 1 , X )$ and $\mu _ { 0 } ( X ) = E ( Y \mid Z = 0 , X )$ are the conditional mean functions of the observed outcomes under treatment and control, respectively. We can identify the two counterfactual means and the average causal effect as follows.

Theorem 18.1 With known $\varepsilon _ { 1 } ( X )$ and $\varepsilon _ { 0 } ( X )$ , we have

$$
E \left\{Y (1) \mid Z = 0 \right\} = E \left\{\mu_ {1} (X) / \varepsilon_ {1} (X) \mid Z = 0 \right\},
$$

$$
E \left\{Y (0) \mid Z = 1 \right\} = E \left\{\mu_ {0} (X) \varepsilon_ {0} (X) \mid Z = 1 \right\}
$$

and therefore

$$
\begin{array}{l} \tau = E \left\{Z Y + (1 - Z) \mu_ {1} (X) / \varepsilon_ {1} (X) \right\} \\ - E \left\{Z \mu_ {0} (X) \varepsilon_ {0} (X) + (1 - Z) Y \right\} (18.1) \\ = E \left\{Z \mu_ {1} (X) + (1 - Z) \mu_ {1} (X) / \varepsilon_ {1} (X) \right\} \\ - E \left\{Z \mu_ {0} (X) \varepsilon_ {0} (X) + (1 - Z) \mu_ {0} (X) \right\}. (18.2) \\ \end{array}
$$

I leave the proof of Theorem 18.1 to Problem 18.1. With the fitted outcome model, (18.1) and (18.2) motivate the following predictive and projective estimators for $\tau$ :

$$
\begin{array}{l} \hat {\tau} ^ {\text {p r e d}} = \left\{n ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} Y _ {i} + n ^ {- 1} \sum_ {i = 1} ^ {n} \left(1 - Z _ {i}\right) \hat {\mu} _ {1} \left(X _ {i}\right) / \varepsilon_ {1} \left(X _ {i}\right) \right\} \\ - \left\{n ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} \hat {\mu} _ {0} (X _ {i}) \varepsilon_ {0} (X _ {i}) + n ^ {- 1} \sum_ {i = 1} ^ {n} (1 - Z _ {i}) Y _ {i} \right\}, \\ \end{array}
$$

and

$$
\begin{array}{l} \hat {\tau} ^ {\text {p r o j}} = \left\{n ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} \hat {\mu} _ {1} \left(X _ {i}\right) + n ^ {- 1} \sum_ {i = 1} ^ {n} \left(1 - Z _ {i}\right) \hat {\mu} _ {1} \left(X _ {i}\right) / \varepsilon_ {1} \left(X _ {i}\right) \right\} \\ - \left\{n ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} \hat {\mu} _ {0} (X _ {i}) \varepsilon_ {0} (X _ {i}) + n ^ {- 1} \sum_ {i = 1} ^ {n} (1 - Z _ {i}) \hat {\mu} _ {0} (X _ {i}) \right\}. \\ \end{array}
$$

The terminology “predictive” and “projective” is from the survey sampling literature (Firth and Bennett, 1998; Ding and Li, 2018); see also Chapter 6.2.2.2. The estimators $\hat { \tau } ^ { \mathrm { p r e d } }$ and $\hat { \tau } ^ { \mathrm { p r o } ] }$ differ slightly: the former uses the observed outcomes when available, whereas the latter replaces the observed outcomes with the fitted values.

More interesting, we can also identify $\tau$ by an inverse probability weighting formula.

Theorem 18.2 With known $\varepsilon _ { 1 } ( X )$ and $\varepsilon _ { 0 } ( X )$ , we have

$$
E \{Y (1) \} = E \left\{w _ {1} (X) \frac {Z}{e (X)} Y \right\}, \quad E \{Y (0) \} = E \left\{w _ {0} (X) \frac {1 - Z}{1 - e (X)} Y \right\},
$$

where

$$
w _ {1} (X) = e (X) + \{1 - e (X) \} / \varepsilon_ {1} (X), \quad w _ {0} (X) = e (X) \varepsilon_ {0} (X) + 1 - e (X).
$$

I leave the proof of Theorem 18.2 to Problem 18.2. Theorem 18.2 modifies the classic IPW formulas with two extra factors $w _ { 1 } ( X )$ and $w _ { 0 } ( X )$ , which depend on both the propensity score and the sensitivity parameters. With the fitted propensity scores, Theorem 18.2 motivates the following estimators for $\tau$ :

$$
\begin{array}{l} \hat {\tau} ^ {\mathrm {h t}} = n ^ {- 1} \sum_ {i = 1} ^ {n} \frac {\{\hat {e} (X _ {i}) \varepsilon_ {1} (X _ {i}) + 1 - \hat {e} (X _ {i}) \} Z _ {i} Y _ {i}}{\varepsilon_ {1} (X _ {i}) \hat {e} (X _ {i})} \\ - n ^ {- 1} \sum_ {i = 1} ^ {n} \frac {\left\{\hat {e} \left(X _ {i}\right) \varepsilon_ {0} \left(X _ {i}\right) + 1 - \hat {e} \left(X _ {i}\right) \right\} \left(1 - Z _ {i}\right) Y _ {i}}{1 - \hat {e} \left(X _ {i}\right)} \\ \end{array}
$$

and

$$
\begin{array}{l} \hat {\tau} ^ {\mathrm {h a j}} = \sum_ {i = 1} ^ {n} \frac {\{\hat {e} (X _ {i}) \varepsilon_ {1} (X _ {i}) + 1 - \hat {e} (X _ {i}) \} Z _ {i} Y _ {i}}{\varepsilon_ {1} (X _ {i}) \hat {e} (X _ {i})} \Big / \sum_ {i = 1} ^ {n} \frac {Z _ {i}}{\hat {e} (X _ {i})} \\ - n ^ {- 1} \sum_ {i = 1} ^ {n} \frac {\{\hat {e} (X _ {i}) \varepsilon_ {0} (X _ {i}) + 1 - \hat {e} (X _ {i}) \} (1 - Z _ {i}) Y _ {i}}{1 - \hat {e} (X _ {i})} \Big / \sum_ {i = 1} ^ {n} \frac {1 - Z _ {i}}{1 - \hat {e} (X _ {i})}. \\ \end{array}
$$

More interestingly, with fitted propensity score and outcome models, the following estimator for $\tau$ is doubly robust:

$$
\hat {\tau} ^ {\mathrm {h t}} = \hat {\tau} ^ {\mathrm {h t}} - n ^ {- 1} \sum_ {i = 1} ^ {n} \{Z _ {i} - \hat {e} (X _ {i}) \} \left\{\frac {\hat {\mu} _ {1} (X _ {i})}{\hat {e} (X _ {i}) \varepsilon_ {1} (X _ {i})} + \frac {\hat {\mu} _ {0} (X _ {i}) \varepsilon_ {0} (X _ {i})}{1 - \hat {e} (X _ {i})} \right\}.
$$

That is, with known $\varepsilon _ { 1 } ( X _ { i } )$ and $\varepsilon _ { 0 } ( X _ { i } )$ , the estimator ${ \hat { \tau } } ^ { \mathrm { d r } }$ is consistent for $^ { \prime }$ if either the propensity score model or the outcome model is correctly specified. We can use the bootstrap to approximate the variance of the above estimators. See Lu and Ding (2023) for technical details.

When $\varepsilon _ { 1 } ( X _ { i } ) = \varepsilon _ { 0 } ( X _ { i } ) = 1$ , the above estimators reduce to the predictive estimator, IPW estimator, and the doubly robust estimators introduced in Part III.

# 18.3.2 Example

# 18.3.2.1 R functions for sensitivity analysis

The following R function can compute the point estimates for sensitivity analysis.

```txt
OS_est_ta = function(z, y, x, out.family = gaussian,
truncps = c(0, 1), e1 = 1, e0 = 1)
{
    ## fitted propensity score
    pscore = glm(z ~ x, family = binomial) $fitted.values
    pscore = pmax(truncps[1], pmin(truncps[2], pscore))
    ## fitted potential outcomes
    outcome1 = glm(y ~ x, weights = z,
                      family = out.family) $fitted.values
    outcome0 = glm(y ~ x, weights = (1 - z),
                      family = out.family) $fitted.values
    ## outcome regression estimator
    ace.reg = mean(z*y) + mean((1-z)*outcome1/e1) -
                     mean(z*outcome0*e0) - mean((1-z)*y)
    ## IPW estimators
    w1 = pscore + (1-pscore)/e1
    w0 = pscore*e0 + (1-pscore) 
```

```txt
ace.ipw0 = mean(z*y*w1/pscore) - mean((1 - z)*y*w0/(1 - pscore))  
ace.ipw = mean(z*y*w1/pscore)/mean(z/pscore) - mean((1 - z)*y*w0/(1 - pscore))/mean((1 - z)/(1 - pscore))  
## doubly robust estimator  
aug = outcome1/pscore/e1 + outcome0*e0/(1-pscore)  
ace.dr = ace.ipw0 + mean((z-pscore)*aug)  
return(c(ace.reg, ace.ipw0, ace.ipw, ace.dr)) 
```

I relegate the calculation of the standard errors to Problem 18.3.

# 18.3.2.2 Revisit Example 10.3

With

$$
\varepsilon_ {1} (X) = \varepsilon_ {0} (X) \in \{1 / 2, 1 / 1. 7, 1 / 1. 5, 1 / 1. 3, 1, 1. 3, 1. 5, 1. 7, 2 \},
$$

we obtain an array of doubly robust estimates of $\tau$ based on the following R code:

```txt
> nhanes_bmi = read.csv("nhanes_bmi.csv")[, -1]
> z = nhanes_bmi$Schoolmeal
> y = nhanes_bmi$BMI
> x = as.matrix(nhanes_bmi[, -c(1, 2)]) 
> x = scale(x)
>
>
>
> E1 = c(1/2, 1/1.7, 1/1.5, 1/1.3, 1, 1.3, 1.5, 1.7, 2)
> E0 = c(1/2, 1/1.7, 1/1.5, 1/1.3, 1, 1.3, 1.5, 1.7, 2)
> EST = outer(E1, E0)
> l11 = length(E1)
> l10 = length(E0)
> for(i in 1:lll)
+ for(j in 1:ll0)
+ EST[i, j] = OS_est_ta(z, y, x, e1 = E1[i], e0 = E0[j])[4] 
```

Table 18.2 presents the point estimates. The signs of the estimates are not sensitive to sensitivity parameters larger than 1, but they are quite sensitive to sensitivity parameters smaller than 1. When the participants of the meal plan tend to have higher BMI (that is, $\varepsilon _ { 1 } ( X ) > 1$ and $\varepsilon _ { 0 } ( X ) > 1$ ), the average causal effect of the meal plan on BMI is negative. However, this conclusion can be quite sensitive if the participants of the meal plan tend to have lower BMI.

TABLE 18.2: Sensitivity analysis for the average causal effect   

<table><tr><td></td><td>1/2</td><td>1/1.7</td><td>1/1.5</td><td>1/1.3</td><td>1</td><td>1.3</td><td>1.5</td><td>1.7</td><td>2</td></tr><tr><td>1/2</td><td>11.62</td><td>10.44</td><td>9.40</td><td>8.03</td><td>4.96</td><td>0.97</td><td>-1.69</td><td>-4.35</td><td>-8.34</td></tr><tr><td>1/1.7</td><td>9.22</td><td>8.05</td><td>7.00</td><td>5.64</td><td>2.57</td><td>-1.42</td><td>-4.08</td><td>-6.75</td><td>-10.74</td></tr><tr><td>1/1.5</td><td>7.63</td><td>6.45</td><td>5.41</td><td>4.05</td><td>0.97</td><td>-3.02</td><td>-5.68</td><td>-8.34</td><td>-12.33</td></tr><tr><td>1/1.3</td><td>6.03</td><td>4.86</td><td>3.81</td><td>2.45</td><td>-0.62</td><td>-4.61</td><td>-7.27</td><td>-9.94</td><td>-13.93</td></tr><tr><td>1</td><td>3.64</td><td>2.47</td><td>1.42</td><td>0.06</td><td>-3.01</td><td>-7.01</td><td>-9.67</td><td>-12.33</td><td>-16.32</td></tr><tr><td>1.3</td><td>1.80</td><td>0.63</td><td>-0.42</td><td>-1.78</td><td>-4.85</td><td>-8.85</td><td>-11.51</td><td>-14.17</td><td>-18.16</td></tr><tr><td>1.5</td><td>0.98</td><td>-0.19</td><td>-1.24</td><td>-2.60</td><td>-5.67</td><td>-9.66</td><td>-12.33</td><td>-14.99</td><td>-18.98</td></tr><tr><td>1.7</td><td>0.36</td><td>-0.82</td><td>-1.86</td><td>-3.23</td><td>-6.30</td><td>-10.29</td><td>-12.95</td><td>-15.61</td><td>-19.60</td></tr><tr><td>2</td><td>-0.35</td><td>-1.52</td><td>-2.57</td><td>-3.93</td><td>-7.00</td><td>-10.99</td><td>-13.65</td><td>-16.32</td><td>-20.31</td></tr></table>

# 18.4 Homework Problems

18.1 Proof of Theorem 18.1

Prove Theorem 18.1.

18.2 Proof of Theorem 18.2

Prove Theorem 18.2.

18.3 Standard errors in sensitivity analysis

Chapter 18.3.2 only presents the point estimates. Report the corresponding bootstrap standard errors.

18.4 Sensitivity analysis for the average causal effect on the treated units $\tau _ { \mathrm { T } }$

This problem extends Chapter 13 to allow for unmeasured confounding for estimating

$$
\tau_ {\mathrm {T}} = E \{Y (1) - Y (0) \mid Z = 1 \} = E (Y \mid Z = 1) - E \{Y (0) \mid Z = 1 \}.
$$

We can easily estimate $E ( Y \mid Z = 1 )$ ) by the sample moment, $\begin{array} { r l } { \hat { \mu } _ { \mathrm { T 1 } } } & { { } = } \end{array}$ $\textstyle \sum _ { i = 1 } ^ { n } Z _ { i } Y _ { i } / \sum _ { i = 1 } ^ { n } Z _ { i }$ P . The only counterfactual term is $E \{ Y ( 0 ) \mid Z = 1 \}$ . Therefore, we only need the sensitivity parameter $\varepsilon _ { 0 } ( X )$ . We have the following two identification formulas with a known $\varepsilon _ { 0 } ( X )$ .

Theorem 18.3 With known $\varepsilon _ { 0 } ( X )$ , we have

$$
\begin{array}{l} E \left\{Y (0) \mid Z = 1 \right\} = E \left\{Z \mu_ {0} (X) \varepsilon_ {0} (X) \right\} / e \\ = E \left\{e (X) \varepsilon_ {0} (X) \frac {1 - Z}{1 - e (X)} Y \right\} / e, \\ \end{array}
$$

where $e = \mathrm { p r } ( Z = 1 )$