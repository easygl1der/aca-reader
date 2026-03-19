# A First Course in Causal Inference

To students and readers who are interested in causal inference

# Contents

Preface XVii

Acronyms xxiii

Notation xxv

I Introduction 1

1 Correlation, Association, and the Yule-Simpson Paradox 3

1.1 Traditional view of statistics 3

1.2 Some commonly-used measures of association 4

1.2.1 Correlation and regression 4

1.2.2 Contingency tables 5

1.3 An example of the Yule-Simpson Paradox 7

1.3.1 Data 7

1.3.2 Explanation 8

1.3.3 Geometry of the Yule-Simpson Paradox 9

1.4 The Berkeley graduate school admission data 10

1.5 Homework Problems 13

2 Potential Outcomes 15

2.1 Experimentalists' view of causal inference 15

2.2 Formal notation of potential outcomes 16

2.2.1 Causal effects, subgroups, and the non-existence of Yule-Simpson Paradox 18

2.2.2 Subtlety of the definition of the experimental unit 18

2.3 Treatment assignment mechanism 19

2.4 Homework Problems 21

II Randomized experiments 23

3 The Completely Randomized Experiment and the Fisher Randomization Test 25

3.1 CRE 25   
3.2 FRT 26   
3.3 Canonical choices of the test statistic 28   
3.4 A case study of the LaLonde experimental data 33

vi

Contents

3.5 Some history of randomized experiments and FRT 35

3.5.1 James Lind's experiment 35   
3.5.2 Lady tasting tea 37   
3.5.3 Two Fisherian principles for experiments 38

3.6 Discussion 38

3.6.1 Other sharp null hypotheses and confidence intervals. 38   
3.6.2 Other test statistics 39   
3.6.3 Final remarks 39

3.7 Homework Problems 40

# 4 Neymanian Repeated Sampling Inference in Completely Randomized Experiments

4.1 Finite population quantities 43   
4.2 Neyman (1923)'s theorem 44   
4.3 Proofs 47   
4.4 Regression analysis of the CRE 49   
4.5 Examples 50

4.5.1 Simulation 50   
4.5.2 Heavy-tailed outcome and failure of Normal approximations   
4.5.3 Application 51

4.6 Homework Problems 55

# 5 Stratification and Post-Stratification in Randomized Experiments

5.1 Stratification 59   
5.2 FRT 61

5.2.1 Theory 61   
5.2.2 An application 63

5.3 Neymanian inference 66

5.3.1 Point and interval estimation 66   
5.3.2 Numerical examples 66   
5.3.3 Comparing the SRE and the CRE 70

5.4 Post-stratification in a CRE 72

5.4.1 Meinert et al. (1970)'s Example 73   
5.4.2 Chong et al. (2016)'s Example 73

5.5 Practical questions 75   
5.6 Homework Problems 76

# 6Rerandomization and Regression Adjustment

6.1Rerandomization 81

6.1.1 Experimental design 81   
6.1.2 Statistical inference 82

6.2 Regression adjustment 85

6.2.1 Covariate-adjusted FRT 85

# Contents vii

6.2.2 Analysis of covariance and extensions 86   
6.2.2.1 Some heuristics for Lin (2013)'s results 86   
6.2.2.2 Understanding Lin (2013)'s estimator via predicting the potential outcomes 89   
6.2.2.3 Understanding Lin (2013)'s estimator via adjusting for covariate imbalance 90   
6.2.3 Some additional remarks on regression adjustment 90   
6.2.3.1 Duality between ReM and regression adjustment 90   
6.2.3.2 Equivalence of regression adjustment and post-stratification 91   
6.2.3.3 Difference-in-difference as a special case of covariate adjustment $\hat{\tau} (\beta_1,\beta_0)$ 91   
6.2.4 Extension to the SRE 92   
6.3 Unification, combination, and comparison 92   
6.4 Simulation 93   
6.5 Final remarks 95   
6.6 Homework Problems 96

# 7Matched-PairsExperiment 99

7.1 Design of the experiment and potential outcomes 99   
7.2 FRT 100   
7.3 Neymanian inference 103   
7.4 Covariate adjustment 105

7.4.1 FRT 106   
7.4.2 Regression adjustment 106

7.5 Examples 108

7.5.1 Darwin's data comparing cross-fertilizing and selffertilizing on the height of corns 108   
7.5.2 Children's television workshop experiment data 110

7.6 Comparing the MPE and CRE 112

7.7 Extension to the general matched experiment 113

7.7.1 FRT 113   
7.7.2 Estimating the average of the within-strata effects 114   
7.7.3 A more general causal estimand 114

7.8 Homework Problems 115

# 8 Unification of the Fisherian and Neymanian Inferences in Randomized Experiments 119

8.1 Testing strong and weak null hypotheses in the CRE 119   
8.2 Covariate-adjusted FRTs in the CRE 121   
8.3 A simulation study 122   
8.4 General recommendations 122   
8.5 A case study 124   
8.6 Homework Problems 125

viii

Contents

# 9 Bridging Finite and Super Population Causal Inference 129

9.1 CRE 130   
9.2 Simulation under the CRE: the super population perspective 132   
9.3 Extension to the SRE 133   
9.4Homework Problems 134

# III Observational studies 137

# 10 Observational Studies, Selection Bias, and Nonparametric Identification of Causal Effects 139

10.1 Motivating Examples 139   
10.2 Causal effects and selection bias under the potential outcomes framework 141   
10.3 Sufficient conditions for nonparametric identification of causal effects 142

10.3.1 Identification 142   
10.3.2 Plausibility of the ignorance assumption 145

10.4 Two simple estimation strategies and their limitations 146

10.4.1 Stratification or standardization based on discrete covariates 146   
10.4.2 Outcome regression 147

10.5 Homework Problems 149

# 11 The Central Role of the Propensity Score in Observational Studies for Causal Effects 153

11.1 The propensity score as a dimension reduction tool 154

11.1.1 Theory 154   
11.1.2 Propensity score stratification 155   
11.1.3 Application 157

11.2 Propensity score weighting 158

11.2.1 Theory 158   
11.2.2 Inverse propensity score weighting estimators 160   
11.2.3 A problem of IPW and a fundamental problem of causal inference 160   
11.2.4 Application 161

11.3 The balancing property of the propensity score 163

11.3.1 Theory 163   
11.3.2 Covariate balance check 164

11.4 Homework Problems 164

# 12 The Doubly Robust or the Augmented Inverse Propensity Score Weighting Estimator for the Average Causal Effect

12.1 The doubly robust estimator 170

12.1.1 Population version 170   
12.1.2 Sample version 171

12.2 More intuition and theory for the doubly robust estimator 172

# #

12.2.1 Reducing the variance of the IPW estimator 172   
12.2.2 Reducing the bias of the outcome regression estimator 173

# 12.3 Examples 173

12.3.1 Summary of some canonical estimators for $\tau$ 173   
12.3.2 Simulation 175   
12.3.3 Applications 176

# 12.4 Some further discussion 177

# 12.5 Homework problems 178

# 13 The Average Causal Effect on the Treated Units and Other Estimands

13.1 Nonparametric identification of $\tau_{\mathrm{T}}$ 181   
13.2 Inverse propensity score weighting and doubly robust estimation of $\tau_{\mathrm{T}}$ 183   
13.3 An example 186   
13.4 Other estimands 187   
13.5 Homework Problems 189

# 14 Using the Propensity Score in Regressions for Causal Effects 193

14.1 Regressions with the propensity score as a covariate 193   
14.2 Regressions weighted by the inverse of the propensity score 196

14.2.1 Average causal effect 196   
14.2.2 Average causal effect on the treated units 199

# 14.3 Homework problems 200

# 15 Matching in Observational Studies 203

15.1 A simple starting point: many more control units 203   
15.2 A more complicated but realistic scenario 205   
15.3 Matching estimator for the average causal effect 206

15.3.1 Point estimation and bias correction 206   
15.3.2 Connection with the doubly robust estimators 208

15.4 Matching estimator for the average causal effect on the treated 209   
15.5 A case study 210

15.5.1 Experimental data 210   
15.5.2 Observational data 212   
15.5.3 Covariate balance checks 213

15.6 Discussion 214   
15.7 Homework Problems 214

# IV Difficulties and challenges of observational studies 2

217

# 16 Difficulties of Unconfoundedness in Observational Studies for Causal Effects

16.1 Some basics of the causal diagram 219   
16.2 Assessing the unconfoundedness assumption 220

16.2.1 Using negative outcomes 221   
16.2.2 Using negative exposures 222   
16.2.3 Summary 222

16.3 Problems of over-adjustment 223

16.3.1 M-bias 223   
16.3.2 Z-bias 225   
16.3.3 What covariates should we adjust for in observational studies? 227

16.4 Homework Problems 228

# 17 E-Value: Evidence for Causation in Observational Studies with Unmeasured Confounding

17.1 Cornfield-type sensitivity analysis 231   
17.2 E-value 235   
17.3 A classic example 236   
17.4 Extensions 237

17.4.1 E-value and Bradford Hill's criteria for causation 237   
17.4.2 E-value after logistic regression 239   
17.4.3 Non-zero true causal effect 241

17.5 Critiques and responses 241

17.5.1 E-value is just a monotone transformation of the risk ratio 241   
17.5.2 Calibration of the E-value 242   
17.5.3 It works the best for a binary outcome and the risk ratio 242

17.6 Homework Problems 243

# 18 Sensitivity Analysis for the Average Causal Effect with Unmeasured Confounding

18.1 Introduction 247   
18.2 Manski-type worse-case bounds on the average causal effect without assumptions 248   
18.3 Sensitivity analysis for the average causal effect 250

18.3.1 Identification formulas 250   
18.3.2 Example 252

18.3.2.1 R functions for sensitivity analysis 252   
18.3.2.2 Revisit Example 10.3 253

18.4 Homework Problems 254

# Contents

xi

# 19 Rosenbaum-Style $p$ -Values for Matched Observational Studies with Unmeasured Confounding

257

19.1 A model for sensitivity analysis with matched data 257   
19.2 Worst-case $p$ -values under Rosenbaum's sensitivity analysis model 258   
19.3 Examples 259

19.3.1 Revisiting the LaLonde data 259   
19.3.2 Two examples from Rosenbaum's packages 260

19.4 Homework Problems 263

# 20 Overlap in Observational Studies: Difficulties and Opportunities

267

20.1 Implications of overlap 267

20.1.1 Trimming in the presence of limited overlap 268   
20.1.2 Outcome modeling in the presence of limited overlap. 268

20.2 Causal inference with no overlap: regression discontinuity 269

20.2.1 Examples and graphical diagnostics 269   
20.2.2 A mathematical formulation of regression discontinuity 271   
20.2.3 Regressions near the boundary 272   
20.2.4 An example 274   
20.2.5 Problems of regression discontinuity 276

20.3 Homework Problems 277

# V Instrumental variables 2

279

# 21 An Experimental Perspective of the Instrumental Variable

21.1 Encouragement Design and Noncompliance 281   
21.2 Latent Compliance Status and Effects 282

21.2.1 Nonparametric identification 282   
21.2.2 Estimation 285

21.3 Covariates 287

21.3.1 Covariate adjustment in the CRE 287   
21.3.2 Covariates in conditional randomization or unconfounded observational studies 287

21.4 Weak IV 288

21.4.1 Some simulation 288   
21.4.2 A procedure robust to weak IV 288   
21.4.3 Implementation and simulation 291

21.5 Application 293   
21.6 Interpreting the CACE 294   
21.7 Homework problems 296

xii

Contents

# 22 Disentangle Mixture Distributions and Instrumental Variable Inequalities 301

22.1 Disentangle Mixture Distributions 301   
22.2 Testable implications: Instrumental Variable Inequalities 304   
22.3 Examples 304   
22.4 Homework problems 308

# 23 An Econometric Perspective of the Instrumental Variable 315

23.1 Examples of studies with IVs 316   
23.2 Brief Review of the Ordinary Least Squares 317   
23.3 Linear Instrumental Variable Model 319   
23.4 The Just-Identified Case 320   
23.5 The Over-Identified Case 321   
23.6 A Special Case: A Single IV for a Single Endogenous Treatment 323

23.6.1 Two-stage least squares 323   
23.6.2 Indirect least squares 323   
23.6.3 Weak IV 324

23.7 Application 325   
23.8 Homework 326

# 24 Application of the Instrumental Variable Method: Fuzzy Regression Discontinuity 329

24.1 Motivating examples 329   
24.2 Mathematical formulation 330   
24.3 Application 332

24.3.1 Re-analyzing Asher and Novosad (2020)'s data 332   
24.3.2 Re-analyzing Li et al. (2015)'s data 333

24.4 Discussion 335   
24.5 Homework Problems 337

# 25 Application of the Instrumental Variable Method: Mendelian Randomization 339

25.1 Background and motivation 339   
25.2 MR based on summary statistics 342

25.2.1 Fixed-effect estimator 342   
25.2.2 Egger regression 343

25.3 An example 344

25.4 Critiques of the analysis based on MR 346   
25.5 Homework Problems 346

# VI Causal Mechanisms with Post-Treatment Variables 347

# Contents xiii

# 26Principal Stratification 349

26.1 Motivating Examples 349   
26.2 The Problem of Conditioning on the Post-Treatment Variable 350   
26.3 Conditioning on the Potential Values of the Post-Treatment Variable 352   
26.4 Statistical Inference and Its Difficulty 353

26.4.1 Special case: truncation by death with binary outcome 354   
26.4.2 An application 356   
26.4.3 Extensions 356

26.5 Principal score method 357

26.5.1 Principal score method under strong monotonicity 357   
26.5.2 An example 359   
26.5.3 Extensions 360

26.6 Other methods 360   
26.7 Homework problems 361

# 27 Mediation Analysis: Natural Direct and Indirect Effects 365

27.1 Motivating Examples 365   
27.2 Nested Potential Outcomes 366

27.2.1 Natural Direct and Indirect Effects 366   
27.2.2 Metaphysics or Science 368

27.3 The Mediation Formula 370   
27.4 The Mediation Formula Under Linear Models 374

27.4.1 The Baron-Kenny Method 374   
27.4.2 An Example 375

27.5 Sensitivity analysis 377   
27.6 Homework problems 377

# 28 Controlled Direct Effect 381

28.1 Definition of the controlled direct effect 381   
28.2 Identification and estimation of the controlled direct effect 381   
28.3 Discussion 383   
28.4Homework problems 384

# 29 Time-Varying Treatment and Confounding 387

29.1 Basic setup and sequential ignorability 387   
29.2 g-formula and outcome modeling 389

29.2.1 Plug-in estimation based on outcome modeling 390   
29.2.2 Recursive estimation based on outcome modeling 392

29.3 Inverse propensity score weighting 393   
29.4 Multiple time points 394

29.4.1 Marginal structural model 394   
29.4.2Structural nested model 395

29.5 Homework problems 398

# VII Appendices 405

# A Probability and Statistics 407

A.1 Probability 407

A.1.1 Pearson correlation coefficient and squared multiple correlation coefficient 407   
A.1.2 Multivariate Normal random vector 407   
A.1.3 $\chi^2$ and $t$ distributions 408   
A.1.4 Cauchy-Schwarz inequality 408   
A.1.5 Tower property and variance decomposition 409   
A.1.6 Limiting theorems 409   
A.1.7 Delta method 410

A.2 Statistical inference 411

A.2.1 Point estimation 411   
A.2.2 Confidence interval 412   
A.2.3 Hypothesis testing 412   
A.2.4 Wald-type confidence interval and test 413   
A.2.5 Duality between constructing confidence sets and testing null hypotheses 413

A.3 Inference with two-by-two tables 414

A.3.1 Fisher's exact test 414   
A.3.2 Estimation with two-by-two tables 415

A.4 Two famous problems in statistics 415

A.4.1 Behrens-Fisher problem 415   
A.4.2 Fieller-Creasy problem 416

A.5 Monte Carlo method in statistics 417

A.6 Bootstrap 417   
A.7 Homework problems 419

# B Linear and Logistic Regressions 421

B.1 Population ordinary least squares 421   
B.2 Sample ordinary least squares 422   
B.3 Frisch-Waugh-Lovell Theorem 423   
B.4 Linear model 424   
B.5 Weighted least squares 426   
B.6 Logistic regression 427

B.6.1 Model 427   
B.6.2 Maximum likelihood estimate 428   
B.6.3 Extension to the case-control study 429   
B.6.4 Logistic regression with weights 430

B.7 Homework problems 430

# C Some Useful Lemmas for Simple Random Sampling From a Finite Population 433

C.1 Lemmas 433   
C.2 Proofs 435   
C.3 Comments on the literature 437

Contents XV

C.4Homework Problems 438

# Preface

# Causal inference research and education in the past decade

The past decade has witnessed an explosion of interest in research and education in causal inference, due to its wide applications in biomedical research, social sciences, tech companies, etc. It was quite different even ten years ago when I was a Ph.D. student in statistics. At that time, causal inference was not a mainstream research topic in statistics and very few undergraduate and graduate programs offered courses in causal inference. In the academic world of statistics, many people were still very skeptical about the foundation of causal inference. Many leading statisticians were reluctant to accept causal inference because of the fundamental conceptual difficulties, which differ from the traditional training of mathematical statistics.

The applications of causal inference in empirical research have changed the field of statistics in both research and education. In the end, statistics is not only about abstract theory but also about solving real-world problems. Many talented researchers have joined the effort to advance our knowledge of causal inference. Many students are eager to learn state-of-the-art theory and methods in causal inference so that they are better equipped to solve problems from various fields.

Due to the needs of the students, my colleagues encouraged me to develop a course in causal inference. Initially, I taught a graduate-level course cross-listed under Political Science and Statistics, which was taught by my former colleague Jas Sekhon for many years at UC Berkeley. Later, I developed this course for both undergraduate and graduate students. At UC Berkeley, the course numbers for "Causal Inference" are Stat 156 and Stat 256, with undergraduate students in Stat 156 and graduate students in Stat 256. Students in both sessions used the same lecture notes and attended the same lectures given by me and my teaching assistants, although they needed to finish different homework problems, reading assignments, and final projects.

Given the mixed levels of technical preparations of my students, the most challenging part of my teaching was to balance the interests of both undergraduate and graduate students. On the one hand, I wanted to present the materials in an intuitive way and only required the undergraduate students to have the basic knowledge of probability, statistics, linear regression, and logistic regression. On the other hand, I also wanted to introduce recent research topics and results to the graduate students. This book is a product of my efforts in the past seven years.

# Recommendations for instructors

This book contains 29 chapters in the main text and 3 chapters in the appendix. UC Berkeley is on the semester system and each semester has 14 weeks of lectures. I could not finish all 32 chapters in one semester. Here are some recommendations based on my own teaching experience.

# Appendix

I started with the chapters in the main text but asked my teaching assistants to review the basics in Chapters A and B. To encourage the students to review Chapters A-C before reading the main text, I also assigned several homework problems from Chapters A-C at the beginning of the semester.

# Part I

The key topic in Chapter 1 is the Yule-Simpson Paradox. Chapter 2 introduces the notion of potential outcomes, which is the foundation for the whole book.

# Part II

Different researchers and instructors may have quite different views on the materials in Part II on randomized experiments. I have talked to many friends about the pros and cons of the current presentation in Part II. Causal inference in randomized experiments is relatively straightforward because randomization eliminates unmeasured confounding. So some friends feel that Chapters 3-9 are too long at least for beginners of causal inference. This also disappointed some of my students when I spent a month on randomized experiments. On the other hand, I was trained from the book of Imbens and Rubin (2015) and believed that to understand observational studies, it is better to understand randomized experiments first. Moreover, I am a big fan of the canonical research of Neyman (1923) and Fisher (1935). Therefore, Part II deeply reflects my own intellectual history and personal taste in statistics. Other instructors may not want to spend a month on randomized experiments and can cover Chapters 5, 7, 8 and 9 quickly.

# Part III

Part III covers the key ideas in observational studies without unmeasured confounding. Four pillars of observational studies are outcome regression, inverse propensity score weighting, doubly robust, and matching estimators, which are covered in Chapters 10, 11, 12 and 15, respectively. Chapters 13 and 14 are optional in teaching. But the results in Chapters 13 and 14 are not uninteresting, so I sometimes covered one or two results there, asked the teaching assistants to cover more in the lab sessions, and encouraged students to read them by assigning some homework problems from those chapters.

# Preface

xix

# Part IV

Part IV is a novel treatment of the fundamental difficulties of observational studies including unmeasured confounding and overlap. However, this part is far from perfect due to the complexities and subtleties of the issues. Chapters 17, 18 and 20 are central, whereas Chapters 16 and 19 are optional.

# Part V

Part V discusses the idea of the instrumental variable. Chapters 21, 23 and 24 are key, whereas Chapters 22 and 25 are optional.

# Part VI

Part VI are some special topics. They are all optional in some sense. Probably it is worth teaching Chapter 27 given the popularity of the Baron-Kenny method in mediation analysis.

# Omitted topics

This book does not cover some popular econometric methods including the difference in differences, panel data, and synthetic controls. Instructors can use Angrist and Pischke (2008) as a reference for those topics. This book assumes minimal preparation for the background knowledge in probability and statistics. Since most introductory statistics courses use the frequentists' view that assumes the unknown parameters are fixed, I adopt this view in this book and omit the Bayesian view for causal inference. In fact, many fundamental ideas of causal inference are from the Bayesian view, starting from Rubin (1978). If readers and students are interested in Bayesian causal inference, please read the review paper by Li et al. (2023).

# Help from teaching assistants

My teaching assistants offered invaluable help for my courses at UC Berkeley. Since I could not cover everything in my notes, I consistently relied on them to cover some technical details or R program sessions in their labs.

# Solution to some homework problems

I have also prepared the solutions to most theory problems. If you are an instructor for a causal inference course, please contact me for the solutions with detailed information about your course.

# Additional recommendations for readers and students

Readers and students can first read my recommendations for instructors above. In addition, I have two other recommendations.

# Homework problems

Each chapter of this book contains homework problems. To deepen the understanding, it is important to try some homework problems. Moreover, some homework problems contain useful theoretical results. Even if you do not have time to figure out the details for those problems, it is helpful to at least read the statements of the problems.

# Recommended reading

Each chapter of this book contains recommended reading. If you want to do research in causal inference, those recommended papers can be useful background knowledge of the literature. When I taught the graduate-level causal inference course at UC Berkeley, I assigned the following papers to the students as weekly reading from week one to the end of the semester:

- Bickel et al. (1975);   
Holland (1986);   
- Miratrix et al. (2013);   
Lin (2013);   
Li et al. (2018b);   
- Rosenbaum and Rubin (1983b);   
- Lunceford and Davidian (2004);   
- Ding and VanderWeele (2016);   
Pearl (1995);   
Angrist et al. (1996);   
- Imbens (2014);   
- Frangakis and Rubin (2002).

Many students gave me positive feedback about their experience of reading the papers above. I recommend reading the above papers even if you do not read this book.

# Features of the book

There are already many excellent causal inference books published in the last decade. Some of them have profound influences on me. When I was in college, I read some draft chapters of Imbens and Rubin (2015) from the internet. They completely challenged my way of thinking about statistics and helped to build my research interest in causal inference. I read Angrist and Pischke (2008)

many times and have gained new insights each time I re-read it. Rosenbaum (2002b), Morgan and Winship (2015), and Hernán and Robins (2020) are another three excellent books from leading researchers in causal inference. When I was preparing for the book, Cunningham (2021), Huntington-Klein (2022), Brumback (2022) and Huber (2023) appeared as four recent excellent books on causal inference.

Thanks to my teaching experience at UC Berkeley, this book has the following features that instructors, students, and readers may find attractive.

- This book assumes minimal preparation for causal inference and reviews the basic probability and statistics knowledge in the appendix.   
- This book covers causal inference from the statistics, biostatistics, and econometrics perspectives, and draws applications from various fields.   
- This book uses R code and data analysis to illustrate the ideas of causal inference. All the R code and datasets are publicly available at Harvard Dataverse: https://doi.org/10.7910/DVN/ZX3VEV   
- This book contains homework problems and can be used as a textbook for both undergraduate and graduate students. Instructors can also ask me for solutions to some homework problems.

# Acknowledgments

Professor Zhi Geng at Peking University introduced me to the area of causal inference when I was studying in college. Professors Luke Miratrix, Tirthankar Dasgupta, and Don Rubin served on my Ph.D. thesis committee at the Harvard Statistics Department. Professor Tyler VanderWeele supervised me as a postdoctoral researcher in Epidemiology at the Harvard T. H. Chan School of Public Health.

My colleagues at the Berkeley Statistics Department have created a critical and productive research environment. Bin Yu and Jas Sekhon have been very supportive since I was a junior faculty. My department chairs, Deb Nolan, Sandrine Dudoit, and Haiyan Huang, encouraged me to develop the "Causal Inference" course. It has been a rewarding experience for me.

I have been lucky to work with many collaborators, in particular, Avi Feller, Laura Forastiere, Zhichao Jiang, Fang Han, Fan Li, Xinran Li, Alessandra Mattei, Fabrizia Mealli, Shu Yang, and Anqi Zhao. I will report in this book what I have learned from them.

Many students at UC Berkeley made critical and constructive comments on early versions of my lecture notes. As teaching assistants for my "Causal Inference" course, Emily Flanagan and Sizhu Lu read early versions of my book carefully and helped me to improve the book a lot.

Professor Joe Blitzstein read an early version of the book carefully and made very detailed comments. Addressing his comments leads to significant

xxii

Preface

improvement in the book. Professors Hongyuan Cao and Zhichao Jiang taught "Causal Inference" courses based on an early version of the book. They made very valuable suggestions.

I am also very grateful for the suggestions from Young Woong Min, Fangzhou Su, Chaoran Yu, and Lo-Hua Yuan.

If you identify any errors, please feel free to email me.

# Acronyms

To simplify the writing, I will use the many acronyms in this book. The following table gives the acronyms, their full names, and the first chapters in which they appear.

<table><tr><td>acronym</td><td>full name</td><td>first chapter</td></tr><tr><td>ACE</td><td>average causal effect</td><td>2</td></tr><tr><td>AI</td><td>Abadie and Imbens (for matching estimators)</td><td>15</td></tr><tr><td>ANCOVA</td><td>analysis of covariance</td><td>6</td></tr><tr><td>BMI</td><td>body mass index</td><td>2</td></tr><tr><td>BRE</td><td>Bernoulli randomized experiment</td><td>3</td></tr><tr><td>CACE</td><td>complier average causal effect</td><td>21</td></tr><tr><td>CATE</td><td>conditional average causal effect</td><td>10</td></tr><tr><td>CDE</td><td>controlled direct effect</td><td>28</td></tr><tr><td>CLT</td><td>central limit theorem</td><td>3 and A</td></tr><tr><td>CRE</td><td>completely randomized experiment</td><td>3</td></tr><tr><td>EHW</td><td>Eicker-Huber-White (robust standard error)</td><td>4 and B</td></tr><tr><td>FAR</td><td>Fieller-Anderson-Rubin (confidence set)</td><td>21</td></tr><tr><td>FRT</td><td>Fisher randomization test</td><td>3</td></tr><tr><td>FWL</td><td>Frisch-Waugh-Lovell (theorem)</td><td>B</td></tr><tr><td>HT</td><td>Horvitz-Thompson (estimator)</td><td>11</td></tr><tr><td>IID</td><td>independent and identically distributed</td><td>3 and A</td></tr><tr><td>ILS</td><td>indirect least squares</td><td>23</td></tr><tr><td>IPW</td><td>inverse propensity score weighting</td><td>11</td></tr><tr><td>ITT</td><td>intention-to-treat (analysis)</td><td>21</td></tr><tr><td>IV</td><td>instrumental variable</td><td>21</td></tr><tr><td>LASSO</td><td>least absolute shrinkage and selection operator</td><td>6</td></tr><tr><td>LATE</td><td>local average treatment effect</td><td>21</td></tr><tr><td>MLE</td><td>maximum likelihood estimate</td><td>B</td></tr><tr><td>MPE</td><td>matched-pairs experiment</td><td>7</td></tr><tr><td>MR</td><td>Mendelian randomization</td><td>25</td></tr><tr><td>MSM</td><td>marginal structural model</td><td>28</td></tr><tr><td>NDE</td><td>natural direct effect</td><td>27</td></tr><tr><td>NHANES</td><td>National Health and Nutrition Examination Survey</td><td>10</td></tr><tr><td>NIE</td><td>natural indirect effect</td><td>27</td></tr><tr><td>OLS</td><td>ordinary least squares</td><td>4 and B</td></tr><tr><td>OR</td><td>odds ratio</td><td>1</td></tr><tr><td>RCT</td><td>randomized controlled trial</td><td>1</td></tr><tr><td>RD</td><td>risk difference</td><td>1</td></tr><tr><td>ReM</td><td>rerandomization using the Mahalanobis distance</td><td>6</td></tr><tr><td>RR</td><td>risk ratio or relative risk</td><td>1</td></tr><tr><td>SNP</td><td>single nucleotide polymorphism</td><td>25</td></tr><tr><td>SRE</td><td>stratified randomized experiment</td><td>5</td></tr><tr><td>SUTVA</td><td>stable unit treatment value assumption</td><td>2</td></tr><tr><td>TSLS</td><td>two-stage least squares</td><td>23</td></tr><tr><td>WLS</td><td>weighted least squares</td><td>14 and B</td></tr></table>

# Notation

I use the following conventional notation in this book.

# Math

$\binom{n}{m}$ "n choose m" which equals $\frac{n!}{m!(n-m)!}$ ∑ summation, e.g., $\sum_{i=1}^{n} a_i = a_1 + \cdots + a_n$ $I(\cdot)$ indicator function, i.e., $I(A) = 1$ if $A$ happens and 0 otherwise  
# counting the number of units in a set  
≈ approximately equal $\propto$ proportional to (by dropping some unimportant constant)  
logit $\operatorname{logit}(x) = \log \frac{x}{1-x}$ $\operatorname{expit}\left(x\right) = \frac{e^x}{1 + e^x} = (1 + e^{-x})^{-1}$

# Basic probability and statistics

pr(·) probability  
E(·) expectation of a random variable  
var(·) variance of a random variable  
cov(·) covariance between random variables $\sim$ "A $\sim$ B" means that A and B have the same asymptotic distribution $\rho_{YX}$ Pearson correlation coefficient between Y and X $R_{YX}^{2}$ squared multiple correlation coefficient between Y and X

# Random variables

Bernoulli $(p)$ Bernoulli distribution with probability $p$ Binomial $(n,p)$ Binomial distribution with $n$ trials and probability $p$ $\mathrm{N}(\mu ,\sigma^2)$ Normal distribution with mean $\mu$ and variance $\sigma^2$ $t_\nu$ t distribution with degrees of freedom $\nu$ $\chi_{\nu}^{2}$ chi-squared distribution with degrees of freedom $\nu$ $z_{1 - \alpha /2}$ the $1 - \alpha /2$ upper quantile of $\mathrm{N}(0,1)$ , e.g., $z_{0.975} = 1.96$

# Causal inference

<table><tr><td>Yi(1), Yi(0)</td><td>potential outcomes of unit i under treatment and control</td></tr><tr><td>τ</td><td>finite-population average causal effect τ = n-1 ∑i=1n{Yi(1) - Yi(0)}</td></tr><tr><td>τ</td><td>super-population average causal effect τ = E{Y(1) - Y(0)}</td></tr><tr><td>μ1(X)</td><td>outcome model μ1(X) = E{Y | Z = 1, X}</td></tr><tr><td>μ0(X)</td><td>outcome model μ0(X) = E{Y | Z = 0, X}</td></tr><tr><td>e(X)</td><td>propensity score e(X) = pr(Z = 1 | X)</td></tr><tr><td>τc</td><td>complier average causal effect τc = E{Y(1) - Y(0) | U = c}</td></tr><tr><td>U</td><td>unmeasured confounder</td></tr><tr><td>U</td><td>latent compliance status U = (D(1), D(0))</td></tr><tr><td>Y(z, Mz&#x27;)</td><td>nested potential outcome (for mediation analysis)</td></tr></table>

# Part I

# Introduction

# 1

# Correlation, Association, and the Yule-Simpson Paradox

Causality is central to human knowledge. Two famous quotes from ancient Greeks are below.

"I would rather discover one causal law than be King of Persia."

— Democritus

"We do not have knowledge of a thing until we grasped its cause."

— Aristotle

However, the major part of classic statistics is about association rather than causation. This chapter will review some basic association measures and point out their fundamental limitations.

# 1.1 Traditional view of statistics

A traditional view of statistics is to infer correlation or association among variables. Based on this view, there is no role for causal inference in statistics. Two famous aphorisms associated with this view are as follows:

- "Correlation does not imply causation."   
- "You can not prove causality with statistics."

This book has a very different view: statistics is crucial for understanding causality. The main focus of this book is to introduce the formal language for causal inference and develop statistical methods to estimate causal effects in randomized experiments and observational studies.

# 1.2 Some commonly-used measures of association

# 1.2.1 Correlation and regression

The Pearson correlation coefficient between two random variables $Z$ and $Y$ is

$$
\rho_ {Z Y} = \frac {\operatorname {c o v} (Z , Y)}{\sqrt {\operatorname {v a r} (Z) \operatorname {v a r} (Y)}},
$$

which measures the linear dependence of $Z$ and $Y$ .

The linear regression of $Y$ on $Z$ is the model

$$
Y = \alpha + \beta Z + \varepsilon , \tag {1.1}
$$

where $E(\varepsilon) = 0$ and $E(\varepsilon Z) = 0$ . We can show that the regression coefficient $\beta$ equals

$$
\beta = \frac {\operatorname {c o v} (Z , Y)}{\operatorname {v a r} (Z)} = \rho_ {Z Y} \sqrt {\frac {\operatorname {v a r} (Y)}{\operatorname {v a r} (Z)}}.
$$

So $\beta$ and $\rho_{ZY}$ always have the same sign.

We can also define multiple regression of $Y$ on $Z$ and $X$ :

$$
Y = \alpha + \beta Z + \gamma X + \varepsilon , \tag {1.2}
$$

where $E(\varepsilon) = 0, E(\varepsilon Z) = 0$ and $E(\varepsilon X) = 0$ . We usually interpret $\beta$ as the "effect" of $Z$ on $Y$ , holding $X$ constant or conditioning on $X$ or controlling for $X$ . Chapter B reviews the basics of linear regression.

More interestingly, the $\beta$ 's in the above two regressions (1.1) and (1.2) can be different; they can even have different signs. The following R code reanalyzed the LaLonde observational data used by Hainmueller (2012). The main question of interest is the "causal effect" of a job training program on earnings. The regression controlling for all covariates gives a coefficient 1067.5461 for treat, whereas the regression not controlling for any covariates gives a coefficient -8506.4954 for treat.

```txt
> dat <- read.table("cps1re74.csv", header = TRUE)
> dat$u74 <- as.numeric(da\$re74==0)
> dat$u75 <- as.numeric(da\$re75==0)
>
>
## linear regression on the outcome
## . means regression on all other variable in dat
lmoutcome = lm(re78 ~ , data = dat)
round.summary(1moutcome)$coef[2, ], 3)
Estimate Std. Error t value Pr(>|t|)
1067.546 554.060 1.927 0.054
>
lmoutcome = lm(re78 ~ treat, data = dat) 
```

> round.summary(lmoutcome) $coef [2, ], 3)
Estimate Std. Error t value Pr(>|t|)
-8506.495 712.766 -11.934 0.000

# 1.2.2 Contingency tables

We can represent the joint distribution of two binary variables $Z$ and $Y$ by a two-by-two contingency table. With $p_{zy} = \operatorname{pr}(Z = z, Y = y)$ , we can summarize the joint distribution in the following table:

<table><tr><td></td><td>Y = 1</td><td>Y = 0</td></tr><tr><td>Z = 1</td><td>p11</td><td>p10</td></tr><tr><td>Z = 0</td><td>p01</td><td>p00</td></tr></table>

Viewing $Z$ as the treatment or exposure and $Y$ as the outcome, we can define the risk difference as

$$
\begin{array}{l} \mathrm {R D} = \operatorname {p r} (Y = 1 \mid Z = 1) - \operatorname {p r} (Y = 1 \mid Z = 0) \\ = \frac {p _ {1 1}}{p _ {1 1} + p _ {1 0}} - \frac {p _ {0 1}}{p _ {0 1} + p _ {0 0}}, \\ \end{array}
$$

the risk ratio as

$$
\begin{array}{l} \mathrm {R R} = \frac {\operatorname {p r} (Y = 1 \mid Z = 1)}{\operatorname {p r} (Y = 1 \mid Z = 0)} \\ = \left. \frac {p _ {1 1}}{p _ {1 1} + p _ {1 0}} \right/ \frac {p _ {0 1}}{p _ {0 1} + p _ {0 0}}, \\ \end{array}
$$

and the odds ratio<sup>1</sup> as

$$
\begin{array}{l} \text {o r} = \frac {\operatorname* {p r} (Y = 1 \mid Z = 1) / \operatorname* {p r} (Y = 0 \mid Z = 1)}{\operatorname* {p r} (Y = 1 \mid Z = 0) / \operatorname* {p r} (Y = 0 \mid Z = 0)} \\ = \frac {\frac {p _ {1 1}}{p _ {1 1} + p _ {1 0}} / \frac {p _ {1 0}}{p _ {1 1} + p _ {1 0}}}{\frac {p _ {0 1}}{p _ {0 1} + p _ {0 0}} / \frac {p _ {0 0}}{p _ {0 1} + p _ {0 0}}} \\ = \frac {p _ {1 1} p _ {0 0}}{p _ {1 0} p _ {0 1}}. \\ \end{array}
$$

The terminology "risk difference", "risk ratio", and "odds ratio" comes from epidemiology. Because the outcomes in epidemiology are often diseases, it is natural to use the name "risk" for the probability of having diseases.

We have the following simple facts about these measures.

Proposition 1.1 (1) The following statements are all equivalent: $Z \sqcup Y$ ,

$\mathrm{RD} = 0$ , $\mathrm{RR} = 1$ , and $\mathrm{OR} = 1$ . (2) If $p_{zy}$ 's are all positive, then $\mathrm{RD} > 0$ is equivalent to $\mathrm{RR} > 1$ and is also equivalent to $\mathrm{OR} > 1$ . (3) $\mathrm{OR} \approx \mathrm{RR}$ if $\operatorname{pr}(Y = 1 \mid Z = 1)$ and $\operatorname{pr}(Y = 1 \mid Z = 0)$ are small.

I leave the proofs of statements (1) and (2) as Problem 1.1. Statement (3) is informal. The approximation holds because the odds $p / (1 - p)$ is close to the probability $p$ for rare diseases with $p \approx 0$ : by Taylor expansion $p / (1 - p) = p + p^2 + \dots \approx p$ . In epidemiology, if the outcome represents the occurrence of a rare disease, then it is reasonable to assume that $\operatorname{pr}(Y = 1 \mid X = 1)$ and $\operatorname{pr}(Y = 1 \mid X = 0)$ are small.

We can also define conditional versions of the RD, RR, and OR if the probabilities are replaced by the conditional probabilities given another variable $X$ , i.e., $\operatorname{pr}(Y = 1 \mid Z = 1, X = x)$ and $\operatorname{pr}(Y = 1 \mid Z = 0, X = x)$ .

With counts $n_{zy} = \# \{i:Z_i = z,Y_i = y\}$ , we can summarize the observed data in the following two-by-two table:

<table><tr><td></td><td>Y = 1</td><td>Y = 0</td></tr><tr><td>Z = 1</td><td>n11</td><td>n10</td></tr><tr><td>Z = 0</td><td>n01</td><td>n00</td></tr></table>

We can estimate RD, RR, and OR by replacing the true probabilities by the sample proportions $\hat{p}_{zy} = n_{zy} / n$ , where $n$ is the total sample size (see Chapter A.3.2). In R, functions fisher.test performs an exact test and chisq.test performs an asymptotic test for $Z \perp Y$ based on a two-by-two table of observed data.

Example 1.1 Bertrand and Mullainathan (2004) conducted a randomized experiment on resumes to study the effect of perceived race on callbacks for interviews. They randomly assigned Black-sounding or White-sounding names on fictitious resumes to help-wanted ads in Boston and Chicago newspapers. The following two-by-two table summarizes perceived race and callback:

> resume = read.csv("resume.csv")
> Alltable = table(resume\ $race, resume\$ call)
> Alltable
0 1
black 2278 157
white 2200 235

The two rows have the same total count, so it is apparent that Whitesounding names received more callbacks. Fisher's exact test below shows that this difference is statistically significant.

$\succ$ fisher.test(Alltable) Fisher's Exact Test for Count Data data: Alltable

# 1.3 An example of the Yule-Simpson Paradox

p-value = 4.759e-05

alternative hypothesis: true odds ratio is not equal to 1  
95 percent confidence interval:

1.249828 1.925573

sample estimates:

odds ratio

1.549732

# 1.3 An example of the Yule-Simpson Paradox

# 1.3.1 Data

The classic kidney stone example is from Charig et al. (1986), where $Z$ is the treatment with 1 for an open surgical procedure and 0 for a small puncture procedure, and $Y$ is the outcome with 1 for success and 0 for failure. The treatment and outcome data can be summarized in the following two-by-two table:

<table><tr><td></td><td>Y = 1</td><td>Y = 0</td></tr><tr><td>Z = 1</td><td>273</td><td>77</td></tr><tr><td>Z = 0</td><td>289</td><td>61</td></tr></table>

The estimated RD is

$$
\widehat{\mathrm{RD}} = \frac{273}{273 + 77} -\frac{289}{289 + 61} = 78\% -83\% = -5\% <   0.
$$

Treatment 0 seems better, that is, the small puncture leads to a higher success rate compared to the open surgical procedure.

However, the data were not from a randomized controlled trial $(\mathrm{RCT})^3$ . Patients receiving treatment 1 can be very different from patients receiving treatment 0. A "lurking variable" in this study is the severity of the case: some patients have smaller stones and some patients have larger stones. We can split the data according to the size of the stones.

For patients with smaller stones, the treatment and outcome data can be summarized in the following two-by-two table:

<table><tr><td></td><td>Y = 1</td><td>Y = 0</td></tr><tr><td>Z = 1</td><td>81</td><td>6</td></tr><tr><td>Z = 0</td><td>234</td><td>36</td></tr></table>

For patients with larger stones, the treatment and outcome data can be summarized in the following two-by-two table:

<table><tr><td></td><td>Y = 1</td><td>Y = 0</td></tr><tr><td>Z = 1</td><td>192</td><td>71</td></tr><tr><td>Z = 0</td><td>55</td><td>25</td></tr></table>

The latter two tables must add up to the first table:

$$
8 1 + 1 9 2 = 2 7 3, \quad 6 + 7 1 = 7 7, \quad 2 3 4 + 5 5 = 2 8 9, \quad 3 6 + 2 5 = 6 1.
$$

From the table for patients with smaller stones, the estimated RD is

$$
\widehat{\mathrm{RD}_{\text{smaller}}} = \frac{81}{81 + 6} -\frac{234}{234 + 36} = 93\% -87\% = 6\% >0,
$$

suggesting that treatment 1 is better. From the table for patients with larger stones, the estimated RD is

$$
\widehat{\mathrm{RDlarger}} = \frac{192}{192 + 71} -\frac{55}{55 + 25} = 73\% -69\% = 4\% >0,
$$

also suggesting that treatment 1 is better.

The above data analysis leads to

$$
\widehat {\mathrm {R D}} <   0, \quad \widehat {\mathrm {R D}} _ {\text {s m a l l e r}} > 0, \quad \widehat {\mathrm {R D}} _ {\text {l a r g e r}} > 0.
$$

Informally, treatment 1 is better for both patients with smaller and larger stones, but treatment 1 is worse for the whole population. This interpretation is quite confusing if the goal is to infer the treatment effect. In statistics, this is called the Yule-Simpson Paradox or Simpson's Paradox in which the marginal association has the opposite sign to the conditional associations at all levels.

# 1.3.2 Explanation

Let $X$ be the binary indicator with $X = 1$ for smaller stones and $X = 0$ for larger stones. Let us first take a look at the $X - Z$ relationship by comparing the probabilities of receiving treatment 1 among patients with smaller and larger stones:

$$
\begin{array}{l} \widehat {\operatorname {p r}} (Z = 1 \mid X = 1) - \widehat {\operatorname {p r}} (Z = 1 \mid X = 0) \\ = \frac {8 1 + 6}{8 1 + 6 + 2 3 4 + 3 6} - \frac {1 9 2 + 7 1}{1 9 2 + 7 1 + 5 5 + 2 5} \\ = 24 \% -77 \% \\ = -53 \% <   0. \\ \end{array}
$$

So patients with larger stones tend to take treatment 1 more frequently. Statistically, $X$ and $Z$ have negative association.

Let us then take a look at the $X - Y$ relationship by comparing the probabilities of success among patients with smaller and larger stones: under treatment

![](images/1ec869d27257a2d84807edabf50e421528ad0f421d63fb84ae9ed3586ebd31e9.jpg)  
FIGURE 1.1: A diagram for the kidney stone example. The signs indicate the associations of two variables, conditioning on other variables pointing to the downstream variable.

1,

$$
\begin{array}{l} \widehat {\Pr} (Y = 1 \mid Z = 1, X = 1) - \widehat {\Pr} (Y = 1 \mid Z = 1, X = 0) \\ = \frac {8 1}{8 1 + 6} - \frac {1 9 2}{1 9 2 + 7 1} \\ = 93 \% -73 \% \\ = 20 \% > 0; \\ \end{array}
$$

under treatment 0,

$$
\begin{array}{l} \widehat {\Pr} (Y = 1 \mid Z = 0, X = 1) - \widehat {\Pr} (Y = 1 \mid Z = 0, X = 0) \\ = \frac {2 3 4}{2 3 4 + 3 6} - \frac {5 5}{5 5 + 2 5} \\ = 87 \% -69 \% \\ = 18 \% >0. \\ \end{array}
$$

So under both treatment levels, patients with smaller stones have higher success probabilities. Statistically, $X$ and $Y$ have positive association conditional on both treatment levels.

We can summarize the qualitative associations in the diagram in Figure 1.1. In technical terms, the treatment has a positive path $(Z \to Y)$ and a more negative path $(Z \gets X \to Y)$ to the outcome, so the overall association is negative between the treatment and outcome. In plain English, when less effective treatment 0 is applied more frequently to the less severe cases, it can appear to be a more effective treatment.

In general, the association between $Z$ and $Y$ can differ qualitatively from the conditional association between $Z$ and $Y$ given $X$ due to the association between $X$ and $Z$ and the association between $X$ and $Y$ . When the Yule-Simpson Paradox happens, we say that $X$ is a confounding variable or confounder for the relationship between $Z$ and $Y$ , or $Z$ and $Y$ are confounded by $X$ . See Chapters 10 and 17 for more in-depth discussion.

# 1.3.3 Geometry of the Yule-Simpson Paradox

Assume that the two-by-two table based on the aggregated data has counts

<table><tr><td>whole population</td><td>Y = 1</td><td>Y = 0</td></tr><tr><td>Z = 1</td><td>n11</td><td>n10</td></tr><tr><td>Z = 0</td><td>n01</td><td>n00</td></tr></table>

The two two-by-two tables based on subgroups have counts

<table><tr><td>subpopulation X = 1</td><td>Y = 1</td><td>Y = 0</td></tr><tr><td>Z = 1</td><td>n11|1</td><td>n10|1</td></tr><tr><td>Z = 0</td><td>n01|1</td><td>n00|1</td></tr></table>

for the subgroup with $X = 1$ and

<table><tr><td>subpopulation X = 0</td><td>Y = 1</td><td>Y = 0</td></tr><tr><td>Z = 1</td><td>n11|0</td><td>n10|0</td></tr><tr><td>Z = 0</td><td>n01|0</td><td>n00|0</td></tr></table>

for the subgroup with $X = 0$ .

Figure 1.2 shows the geometry of the Yule-Simpson Paradox. The y-axis shows the count of successes with $Y = 1$ and the x-axis shows the count of failures with $Y = 0$ . The two parallelograms correspond to aggregating the counts of successes and failures under two treatment levels. The slope of $OA_{1}$ is larger than that of $OB_{1}$ , and the slope of $OA_{0}$ is larger than that of $OB_{0}$ . So the treatment seems beneficial to the outcome within both levels of $X$ . However, the slope of $OA$ is smaller than that of $OB$ . So the treatment seems harmful to the outcome for the whole population. The Yule-Simpson Paradox arises.

# 1.4 The Berkeley graduate school admission data

Bickel et al. (1975) investigated the admission rates of male and female students into the graduate school of Berkeley. The R package datasets contains the original data UCBAdmissions. The raw data by the six largest departments are shown below:

```txt
> library(datasets)  
> UCBAdmissions = aperm(UCBAdmissions, c(2, 1, 3))  
> UCBAdmissions  
, , Dept = A  
Admit  
Gender Admitted Rejected  
Male 512 313  
Female 89 19  
, , Dept = B 
```

![](images/9fb9369210b61fdbabd30391bf88e33dbc65fc15471fdd34174c931837f5881b.jpg)  
FIGURE 1.2: Geometry of the Yule-Simpson Paradox

Admit   
Gender Admitted Rejected   
Male 353 207   
Female 17 8   
,Dept $=$ C   
Admit   
Gender Admitted Rejected   
Male 120 205   
Female 202 391   
,Dept $=$ D   
Admit   
Gender Admitted Rejected   
Male 138 279   
Female 131 244   
,Dept $=$ E   
Admit   
Gender Admitted Rejected   
Male 53 138   
Female 94 299   
,Dept $=$ F   
Admit   
Gender Admitted Rejected   
Male 22 351   
Female 24 317

Aggregating the data over departments, we have a simple two-by-two table:

>UCBAdmissions-sum $=$ apply(UCBAdmissions，c(1，2)，sum)  
>UCBAdmissions-sum Admit  
Gender Admitted Rejected  
Male 1198 1493  
Female 557 1278

The following function, building upon chisq.test, have a two-by-two table as the input and the estimated RD and $p$ -value as output:

>risk.difference $=$ function(tb2)   
+{ $\begin{array}{rl}{\mathrm{p1}}&{=~\mathrm{tb2[1,~1]}/(\mathrm{tb2[1,~1]}+\mathrm{tb2[1,~2]})}\\{\mathrm{p2}}&{=~\mathrm{tb2[2,~1]/(tb2[2,~1]}+\mathrm{tb2[2,~2]})}\\{\mathrm{testp}}&{=~\mathrm{chisq.test(tb2)}}\end{array}$ +

# 1.5 Homework Problems

```txt
+ return(list(p.diff = p1 - p2, + pv = testp\\(p.value))   
+} 
```

With this function, we find a large, significant difference between the admission rates of male and female students:

> risk.difference(UCBAdmissions-sum)
\(p.diff
[1] 0.1416454
\)pv
[1] 1.055797e-21

Stratifying on the departments, we find smaller and insignificant differences between the admission rates of male and female students. In department A, the difference is significant but negative.

> P.diff = rep(0, 6)
> PV = rep(0, 6)
> for(dd in 1:6)
+ {
+ department = risk.difference(UCBA admissions[., dd])
+ P.diff[dd] = department\\(p.diff
+ PV[dd] = department\\)pv
+ }
>
> round(P.diff, 2)
[1] -0.20 -0.05 0.03 -0.02 0.04 -0.01
> round(PV, 2)
[1] 0.00 0.77 0.43 0.64 0.37 0.64

# 1.5 Homework Problems

# 1.1 Independence in two-by-two tables

Prove (1) and (2) in Proposition 1.1.

# 1.2 More examples of the Yule-Simpson Paradox

Give a numeric example of a two-by-two-by-two table in which the Yule-Simpson Paradox arises.

Find a real-life example in which the Yule-Simpson Paradox arises.

# 1.3 Correlation and partial correlation

Consider a three-dimensional Normal random vector:

$$
\left( \begin{array}{c} X \\ Y \\ Z \end{array} \right) \sim \mathrm {N} \left(\left( \begin{array}{c} 0 \\ 0 \\ 0 \end{array} \right), \left( \begin{array}{c c c} 1 & \rho_ {X Y} & \rho_ {X Z} \\ \rho_ {X Y} & 1 & \rho_ {Y Z} \\ \rho_ {X Z} & \rho_ {Y Z} & 1 \end{array} \right)\right).
$$

The correlation coefficient between $Y$ and $Z$ is $\rho_{YZ}$ . There are many equivalent definitions of the partial correlation coefficient. For a multivariate Normal vector, let $\rho_{YZ|X}$ denote the partial correlation coefficient between $Y$ and $Z$ given $X$ , which is defined as their correlation coefficient in the conditional distribution $(Y,Z) \mid X$ . Show that

$$
\rho_ {Y Z | X} = \frac {\rho_ {Y Z} - \rho_ {Y X} \rho_ {Z X}}{\sqrt {1 - \rho_ {Y X} ^ {2}} \sqrt {1 - \rho_ {Z X} ^ {2}}}.
$$

Give a numerical example with $\rho_{YZ} > 0$ and $\rho_{YZ|X} < 0$ .

Remark: This is the Yule-Simpson Paradox for a Normal random vector. You can use the results in Chapter A.1.2 to prove the formula for the partial correlation coefficient.

# 1.4 Specification searches

Section 1.2.1 re-analyzes the data used by Hainmueller (2012). We used the outcome named re78 and the treatment named treat in the analysis. Moreover, the data also contain 10 covariates and therefore $2^{10} = 1024$ possible subsets of covariates in the linear regression. Run 1024 linear regressions with all possible subsets of covariates, and report the regression coefficients of the treatment. How many coefficients of the treatment are positively significant, how many are negatively significant, and how many are not significant? You can also report other interesting findings from these regressions.

# 1.5 More on racial discrimination

Section 1.2.2 re-analyzes the data collected by Bertrand and Mullainathan (2004). Conduct analyses separately for males and females. What do you find from these subgroup analyses?

# 1.6 Recommended reading

Bickel et al. (1975) is the original paper for the paradox reported in Section 1.4. Pearl and Mackenzie (2018) recently revisited the study from the causal inference perspective.

# 2

# Potential Outcomes

# 2.1 Experimentalists' view of causal inference

Rubin (1975) and Holland (1986) made up the aphorism:

"No causation without manipulation."

Not everybody agrees with this point of view. However, it is quite helpful to clarify ambiguity in thinking about causal relationships. This book follows this view and defines causal effects using the potential outcomes framework (Neyman, 1923; Rubin, 1974). In this framework, an experiment, or at least a thought experiment, has a treatment, and we are interested in its effect on an outcome or multiple outcomes. Sometimes, the treatment is also called an intervention or a manipulation.

Example 2.1 If we are interested in the effect of taking aspirin or not on the relief of headaches, the intervention is taking aspirin or not.

Example 2.2 If we are interested in the effect of participating in a job training program or not on employment and wage, the intervention is participating in the job training program or not.

Example 2.3 If we are interested in the effect of studying in a small classroom or a large classroom on standardized test scores, the intervention is studying in a small classroom or not.

Example 2.4 Gerber et al. (2008) were interested in the effect of different get-out-to-vote messages on the voting behavior. The intervention is the different get-out-to-vote messages.

Example 2.5 Pearl (2018) claimed that we could infer the effect of obesity on life span. A popular measure of obesity is the body mass index (BMI), defined as the body mass divided by the square of the body height in units of $kg/m^2$ . So the intervention can be different levels of BMI.

However, there are different levels of ambiguity in the interventions above. The meanings of interventions in Examples 2.1-2.4 are relatively clear, but the meaning of intervention on BMI in Example 2.5 is less clear. In particular, we

can imagine different versions of BMI reduction: healthier diet, more physical exercise, bariatric surgery, etc. These different versions of the intervention can have quite different effects on the outcome. In this book, we will view the intervention in Example 2.5 as ill-defined without further clarifications.

Another ill-defined intervention is race. Racial discrimination is an important issue in the labor market, but it is not easy to imagine an experiment to change the race of any experimental unit. Bertrand and Mullainathan (2004) give an interesting experiment that partially answers the question.

Example 2.6 Recall Example 1.1. Bertrand and Mullainathan (2004) randomly change the names on the resumes, and compare the callback rates of resumes with African-American- or White-sounding names. For each resume, the intervention is the binary indicator of a Black-sounding or White-sounding name, and the outcome is the binary indicator of callback. I analyzed the following two-by-two table in Section 1.2.2:

<table><tr><td></td><td>callback</td><td>no callback</td></tr><tr><td>Black</td><td>157</td><td>2278</td></tr><tr><td>White</td><td>235</td><td>2200</td></tr></table>

From the above, we can compare the probabilities of being called back among Black-sounding and White-sounding names:

$$
\frac{157}{2278 + 157} -\frac{235}{2200 + 235} = 6.45\% -9.65\% = -3.20\% <   0
$$

with $p$ -value from the Fisher exact test being much smaller than 0.001.

In Bertrand and Mullainathan (2004)'s experiment, the treatment is the perceived race which can be manipulated by experimenters. They design an experiment to answer a well-defined causal question. However, critics may raise the concern that the causal effect of the perceived race may differ from the causal effect of the actual race.

# 2.2 Formal notation of potential outcomes

Consider a study with $n$ experimental units indexed by $i = 1, \ldots, n$ . As a starting point, we focus on a treatment with two levels: 1 for the treatment and 0 for the control. For each unit $i$ , the outcome of interest $Y$ has two versions:

$$
Y _ {i} (1) \text {a n d} Y _ {i} (0),
$$

which are potential outcomes under the hypothetical interventions 1 and 0. Neyman (1923) first used this notation. It seems intuitive but has some hidden assumptions. Rubin (1980) made the following clarifications on the hidden assumptions.

Assumption 2.1 (no interference) Unit $i$ 's potential outcomes do not depend on other units' treatments. This is sometimes called the no-interference assumption.

Assumption 2.2 (consistency) There are no other versions of the treatment. Equivalently, we require that the treatment levels be well-defined, or have no ambiguity at least for the outcome of interest. This is sometimes called the consistency assumption.<sup>1</sup>

Assumption 2.1 can be violated in infectious diseases or network experiments. For instance, if some of my friends receive flu shots, my chance of getting the flu decreases even if I do not receive the flu shot; if my friends see an advertisement on Facebook, my chance of buying that product increases even if I do not see the advertisement directly. It is an active research area to study situations with interfering units in modern causal inference literature (e.g., Hudgens and Halloran, 2008).

Assumption 2.2 can be violated for treatments with complex components. For instance, when studying the effect of cigarette smoking on lung cancer, the type of cigarettes may matter; when studying the effect of college education on income, the type and major of college education may matter.

Rubin (1980) called the Assumptions 2.1 and 2.2 above together the Stable Unit Treatment Value Assumption (SUTVA).

Assumption 2.3 (SUTVA) Both Assumptions 2.1 and 2.2 hold.

Under SUTVA, Rubin (2005) called the $n \times 2$ matrix of potential outcomes the Science Table:

<table><tr><td>i</td><td>Yi(1)</td><td>Yi(0)</td></tr><tr><td>1</td><td>Y1(1)</td><td>Y1(0)</td></tr><tr><td>2</td><td>Y2(1)</td><td>Y2(0)</td></tr><tr><td>:</td><td>:</td><td>:</td></tr><tr><td>n</td><td>Yn(1)</td><td>Yn(0)</td></tr></table>

Due to the fundamental contributions of Neyman and Rubin to statistical causal inference, the potential outcomes framework is sometimes referred to as the Neyman Model, the Neyman-Rubin Model, or the Rubin Causal Model. I prefer using "the potential outcomes framework" in this book and my other scientific writings.

Causal effects are functions of the Science Table. Inferring individual causal effects

$$
\tau_ {i} = Y _ {i} (1) - Y _ {i} (0), \quad (i = 1, \dots , n)
$$

is fundamentally challenging because we can only observe either $Y_{i}(1)$ or $Y_{i}(0)$ .

for each unit $i$ , that is, we can observe only half of the Science Table. As a starting point, most parts of the book focus on the average causal effect (ACE):

$$
\begin{array}{l} \tau = n ^ {- 1} \sum_ {i = 1} ^ {n} \left\{Y _ {i} (1) - Y _ {i} (0) \right\} \\ = \quad n ^ {- 1} \sum_ {i = 1} ^ {n} Y _ {i} (1) - n ^ {- 1} \sum_ {i = 1} ^ {n} Y _ {i} (0). \\ \end{array}
$$

But we can extend our discussion to many other parameters (also called estimands). Problem 2.2 gives some examples.

# 2.2.1 Causal effects, subgroups, and the non-existence of Yule-Simpson Paradox

If we have two subgroups defined by a binary variable $X_{i}$ , we can define the subgroup causal effects as

$$
\tau_ {x} = \frac {\sum_ {i = 1} ^ {n} I (X _ {i} = x) \{Y _ {i} (1) - Y _ {i} (0) \}}{\sum_ {i = 1} ^ {n} I (X _ {i} = x)}, \quad (x = 0, 1)
$$

where $I(\cdot)$ is the indicator function. A simple identity is that

$$
\tau = \pi_ {1} \tau_ {1} + \pi_ {0} \tau_ {0}
$$

where $\pi_x = \sum_{i=1}^n I(X_i = x) / n$ is the proportion of units with $X_i = x$ ( $x = 0, 1$ ). Therefore, if $\tau_1 > 0$ and $\tau_0 > 0$ , we must have $\tau > 0$ . The Yule-Simpson Paradox thus cannot happen to causal effects.

# 2.2.2 Subtlety of the definition of the experimental unit

I now discuss a subtlety related to the definition of the experimental unit. Simply speaking, the experimental unit can be different from the physical unit. For example, if I did not take aspirin before and my headache did not go away, but I take aspirin now and my headache goes away, then you might think that we can observe my potential outcomes under both control and treatment. Let $i$ index myself, and let $Y = 1$ denote the indicator of no headache. Then, the above heuristic suggests that $Y_{i}(0) = 0$ and $Y_{i}(1) = 1$ , so it seems that aspirin kills my headache. But this logic is very wrong because of the misunderstanding of the definition of the experimental unit. At different time points, I, the same physical person, become two distinct experimental units, indexed by “ $i$ , before” and “ $i$ , after”. Therefore, we have four potential outcomes

$$
Y _ {i, \mathrm {b e f o r e}} (0) = 0, \quad Y _ {i, \mathrm {b e f o r e}} (1) =?, \quad Y _ {i, \mathrm {a f t e r}} (0) =?, \quad Y _ {i, \mathrm {a f t e r}} (1) = 1,
$$

with two of them observed and two of them missing. The individual causal effects

$$
Y _ {i, \text {b e f o r e}} (1) - Y _ {i, \text {b e f o r e}} (0) =? - 0 \text {a n d} Y _ {i, \text {a f t e r}} (1) - Y _ {i, \text {a f t e r}} (0) = 1 - ?
$$

are unknown. It is possible that my headache goes away even if I do not take aspirin:

$$
Y _ {i, \text {a f t e r}} (0) = 1, \quad Y _ {i, \text {a f t e r}} (1) = 1
$$

which implies zero effect; it is also possible that my headache does not go away if I do not take aspirin:

$$
Y _ {i, \text {a f t e r}} (0) = 0, \quad Y _ {i, \text {a f t e r}} (1) = 1
$$

which implies a positive effect of aspirin.

The wrong heuristic argument might get the right answer if the control potential outcomes are stable at the before and after periods:

$$
Y _ {i, \text {b e f o r e}} (0) = Y _ {i, \text {a f t e r}} (0) = 0.
$$

But this assumption is rather strong and fundamentally untestable. Rubin (2001) offered a related discussion in the context of self-experimentation for causal effects.

# 2.3 Treatment assignment mechanism

Let $Z_{i}$ be the binary treatment indicator for unit $i$ , vectorized as $Z = (Z_{1},\ldots ,Z_{n})$ . The observed outcome of unit $i$ is a function of the potential outcomes and the treatment indicator:

$$
\begin{array}{l} Y _ {i} = \left\{ \begin{array}{l l} Y _ {i} (1), & \text {i f} Z _ {i} = 1 \\ Y _ {i} (0), & \text {i f} Z _ {i} = 0 \end{array} \right. (2.1) \\ = Z _ {i} Y _ {i} (1) + \left(1 - Z _ {i}\right) Y _ {i} (0) (2.2) \\ = Y _ {i} (0) + Z _ {i} \left\{Y _ {i} (1) - Y _ {i} (0) \right\} (2.3) \\ = Y _ {i} (0) + Z _ {i} \tau_ {i}. (2.4) \\ \end{array}
$$

Equation (2.1) is the definition of the observed outcome. Equation (2.2) is equivalent to (2.1). It is a trivial fact, but Pearl (2010b) viewed it as the fundamental bridge between the potential outcomes and the observed outcome. Equations (2.3) and (2.4) highlight the fact that the individual causal effect $\tau_{i} = Y_{i}(1) - Y_{i}(0)$ can be heterogeneous across units.

The experiment reveals only one of unit $i$ 's potential outcomes with the

other one missing:

$$
\begin{array}{l} Y _ {i} ^ {\text {m i s}} = \left\{ \begin{array}{l l} Y _ {i} (0), & \text {i f Z _ {i} = 1} \\ Y _ {i} (1), & \text {i f Z _ {i} = 0} \end{array} \right. \\ = Z _ {i} Y _ {i} (0) + (1 - Z _ {i}) Y _ {i} (1). \\ \end{array}
$$

The missing potential outcome corresponds to the opposite treatment level of unit $i$ . For this reason, the potential outcomes framework is also called the counterfactual framework. This name can be confusing because before the experiment, both the potential outcomes can be observed. Only after the experiment, one potential outcome is observed whereas the other potential outcome is counterfactual.

The treatment assignment mechanism, i.e., the probability distribution of $Z$ , plays an important role in inferring causal effects. The following simple numerical examples illustrate this point. We first generate potential outcomes from Normal distributions with the average causal effect close to -0.5.

$$
\begin{array}{l} > n = 5 0 0 \\ > Y O = r n o r m (n) \\ > t a u = - 0. 5 + Y 0 \\ > Y 1 = Y 0 + t a u \\ \end{array}
$$

A perfect doctor assigns the treatment to the patient if $s/he$ knows that the individual causal effect is non-negative. This results in a positive difference in means of the observed outcomes:

$$
\begin{array}{l} > Z = (t a u > = 0) \\ > Y = Z * Y 1 + (1 - Z) * Y 0 \\ > \text {m e a n} (\mathrm {Y} [ \mathrm {Z} = = 1 ]) - \text {m e a n} (\mathrm {Y} [ \mathrm {Z} = = 0 ]) \\ [ 1 ] \quad 2. 1 6 6 5 0 9 \\ \end{array}
$$

A clueless doctor does not know any information about the individual causal effects and assigns the treatment to patients by flipping a fair coin. This results in a difference in means of the observed outcomes close to the true average causal effect:

$$
\begin{array}{l} > Z = \text {r b i n o m} (n, 1, 0. 5) \\ > Y = Z * Y 1 + (1 - Z) * Y 0 \\ > \text {m e a n} (\mathrm {Y} [ \mathrm {Z} = = 1 ]) - \text {m e a n} (\mathrm {Y} [ \mathrm {Z} = = 0 ]) \\ [ 1 ] \quad - 0. 5 5 2 0 6 4 \\ \end{array}
$$

The above examples are hypothetical since no doctors perfectly know the individual causal effects. However, the examples do demonstrate the crucial role of the treatment assignment mechanism. This book will organize the topics based on the treatment assignment mechanism.

# 2.4 Homework Problems

# 2.1 A perfect doctor

Following the first perfect doctor example in Section 2.3, assume the potential outcomes are random variables generated from

$$
Y (0) \sim \mathrm {N} (0, 1), \quad \tau = - 0. 5 + Y (0), \quad Y (1) = Y (0) + \tau .
$$

The binary treatment is determined by the treatment effect as $Z = 1(\tau \geq 0)$ , and the observed outcome is determined by the potential outcomes and the treatment by $Y = ZY(1) + (1 - Z)Y(0)$ . Calculate the difference in means

$$
E (Y \mid Z = 1) - E (Y \mid Z = 0).
$$

Remark: The mean of a truncated Normal random variable equals

$$
E (X \mid a <   X <   b) = \mu - \sigma \frac {\phi \left(\frac {b - \mu}{\sigma}\right) - \phi \left(\frac {a - \mu}{\sigma}\right)}{\Phi \left(\frac {b - \mu}{\sigma}\right) - \Phi \left(\frac {a - \mu}{\sigma}\right)},
$$

where $X \sim \mathrm{N}(\mu, \sigma^2)$ , and $\phi(\cdot)$ and $\Phi(\cdot)$ are the probability density and cumulative distribution functions of a standard Normal random variable $\mathrm{N}(0,1)$ .

# 2.2 Nonlinear causal estimands

With potential outcomes $\{(Y_i(1), Y_i(0))\}_{i=1}^n$ for $n$ units under the treatment and control, the difference in means equals the mean of the individual treatment effects:

$$
\bar {Y} (1) - \bar {Y} (0) = n ^ {- 1} \sum_ {i = 1} ^ {n} \{Y _ {i} (1) - Y _ {i} (0) \}.
$$

Therefore, the average treatment effect is a linear causal estimand in the sense that the difference in average potential outcomes equals the average of the differences in individual potential outcomes.

Other estimands may not be linear. For instance, we can define the median treatment effect as

$$
\delta_ {1} = \operatorname {m e d i a n} \{(Y _ {i} (1) \} _ {i = 1} ^ {n} - \operatorname {m e d i a n} \{(Y _ {i} (0) \} _ {i = 1} ^ {n},
$$

which is, in general, different from the median of the individual treatment effect

$$
\delta_ {2} = \operatorname {m e d i a n} \left\{\left(Y _ {i} (1) - Y _ {i} (0) \right\} _ {i = 1} ^ {n}. \right.
$$

1. Give numerical examples that have $\delta_1 = \delta_2$ , $\delta_1 > \delta_2$ , and $\delta_1 < \delta_2$ , respectively.   
2. Which estimand makes more sense, $\delta_{1}$ or $\delta_{2}$ ? Why? Use examples to justify your conclusion. If you feel that both $\delta_{1}$ and $\delta_{2}$ can make sense in different applications, you can also give examples to justify both estimands.

# 2.3 Average and individual effects

Give a numerical example in which $\tau = n^{-1}\sum_{i=1}^{n}\{Y_i(1) - Y_i(0)\} > 0$ but the proportion of units with $Y_i(1) > Y_i(0)$ is smaller than 0.5. That is, the average causal effect is positive, but the treatment benefits less than half of the units.

# 2.4 Recommended reading

Holland (1986) is a classic review article on statistical causal inference. It popularized the name "Rubin Causal Model" for the potential outcomes framework. At the University of California Berkeley, we call it the "Neyman Model" for obvious reasons.

# Part II

# Randomized experiments

# 3

# The Completely Randomized Experiment and the Fisher Randomization Test

The potential outcomes framework has intrinsic connections with randomized experiments. Understanding causal inference in various randomized experiments is fundamental and helpful for understanding causal inference in more complicated non-experimental studies.

Part II of this book focuses on randomized experiments. This chapter focuses on the simplest experiment, the completely randomized experiment (CRE).

# 3.1 CRE

Consider an experiment with $n$ units, with $n_1$ receiving the treatment and $n_0$ receiving the control. We can define the CRE based on its treatment assignment mechanism<sup>1</sup>.

Definition 3.1 (CRE) Fix $n_1$ and $n_0$ with $n = n_1 + n_0$ . A CRE has the treatment assignment mechanism:

$$
\operatorname {pr}(\boldsymbol {Z} = \boldsymbol {z}) = 1\Big{/}\binom {n}{n_{1}},
$$

where $\mathbf{z} = (z_{1},\dots ,z_{n})$ satisfies $\sum_{i = 1}^{n}z_{i} = n_{1}$ and $\sum_{i = 1}^{n}(1 - z_{i}) = n_{0}$ .

In Definition 3.1, we assume that the potential outcome vector under treatment $\mathbf{Y}(1) = (Y_{1}(1),\ldots ,Y_{n}(1))$ and the potential outcome vector under control $\mathbf{Y}(0) = (Y_{1}(0),\dots ,Y_{n}(0))$ are both fixed. Even if we view them as random, we can condition on them and the treatment assignment mechanism becomes

$$
\operatorname {pr}\{\boldsymbol {Z} = \boldsymbol {z}\mid \boldsymbol {Y}(1),\boldsymbol {Y}(0)\} = 1\Big{/}\binom {n}{n_{1}}
$$

because $\mathbf{Z} \perp \{\mathbf{Y}(1), \mathbf{Y}(0)\}$ in a CRE. In a CRE, the treatment vector $\mathbf{Z}$ is from a random permutation of $n_1$ 1's and $n_0$ 0's.

In his seminal book Design of Experiments, Fisher (1935) pointed out the following advantages of randomization:

1. It creates comparable treatment and control groups on average.   
2. It serves as a "reasoned basis" for statistical inference.

Point 1 is intuitive because the random treatment assignment does not bias toward the treatment or the control. Most people understand point 1 well. Point 2 is more subtle. What Fisher meant is that randomization justifies a statistical test, which is now called the Fisher Randomization Test (FRT). This chapter illustrates the basic idea of the FRT under a CRE.

# 3.2 FRT

Fisher (1935) was interested in testing the following null hypothesis:2

$$
H _ {0 \mathrm {F}}: Y _ {i} (1) = Y _ {i} (0) \text {f o r a l l u n i t s} i = 1, \dots , n.
$$

Rubin (1980) called it the sharp null hypothesis in the sense that it can determine all the potential outcomes based on the observed data: $\mathbf{Y}(1) = \mathbf{Y}(0) = \mathbf{Y} = (Y_1, \ldots, Y_n)$ , the vector of the observed outcomes. It is also called the strong null hypothesis (e.g., Wu and Ding, 2021).

Conceptually, under $H_{0\mathrm{F}}$ , the FRT works for any test statistic

$$
T = T (\boldsymbol {Z}, \boldsymbol {Y}), \tag {3.1}
$$

which is a function of the observed data. The observed outcome vector $\mathbf{Y}$ is fixed under $H_{0\mathrm{F}}$ , so the only random component in the test statistic $T$ is the treatment vector $\mathbf{Z}$ . The experimenter determines the distribution of $\mathbf{Z}$ , which in turn determines the distribution of $T$ under $H_{0\mathrm{F}}$ . This is the basis for calculating the $p$ -value. I will give more details below.

In a CRE, $Z$ is uniform over the set

$$
\{z ^ {1}, \ldots , z ^ {M} \}
$$

where $M = \binom{n}{n_1}$ , and the $z^{m}$ 's are all possible vectors with $n_1$ 1's and $n_0$ 0's. For instance, with $n = 5$ and $n_1 = 3$ , we can enumerate $M = \binom{5}{3} = 10$ vectors as follows:

# 3.2 FRT

```diff
> permutation10 = function(n, n1)  
+ M = choose(n, n1)  
+ treat.index = combn(n, n1)  
+ Z = matrix(0, n, M)  
+ for(m in 1:M)  
+ treat = treat.index[, m]  
+ Z[treat, m] = 1  
+ }  
+ Z  
+ }  
> permutation10(5, 3)  
[.,1] [,2] [,3] [,4] [,5] [,6] [,7] [,8] [,9] [,10]  
[1,] 1 1 1 1 1 1 0 0 0 0  
[2,] 1 1 1 0 0 0 1 1 1 0  
[3,] 1 0 0 1 1 0 1 1 0 1  
[4,] 0 1 0 1 0 1 1 0 1 1  
[5,] 0 0 1 0 1 1 0 1 1 1 
```

As a consequence, $T$ is uniform over the set (with possible duplications)

$$
\{T (\boldsymbol {z} ^ {1}, \boldsymbol {Y}), \dots , T (\boldsymbol {z} ^ {M}, \boldsymbol {Y}) \}.
$$

That is, the distribution of $T$ is known due to the design of the CRE. We will call this distribution of $T$ the randomization distribution.

If larger values are more extreme for $T$ , we can use the following tail probability to measure the extremeness of the test statistic with respect to its randomization distribution:

$$
p _ {\mathrm {F R T}} = M ^ {- 1} \sum_ {m = 1} ^ {M} I \left\{T \left(\boldsymbol {z} ^ {m}, \boldsymbol {Y}\right) \geq T (\boldsymbol {Z}, \boldsymbol {Y}) \right\}, \tag {3.2}
$$

which is called the $p$ -value by Fisher. Figure 3.1 illustrates the computational process of $p_{\mathrm{FRT}}$ .

The $p$ -value, $p_{\mathrm{FRT}}$ , in (3.2) works for any choice of test statistic and any outcome-generating process. It also extends naturally to any experiment, which will be a topic repeatedly discussed in the following chapters. Importantly, it is finite-sample exact in the sense<sup>4</sup> that under $H_{0\mathrm{F}}$ ,

$$
\Pr \left(p _ {\mathrm {F R T}} \leq u\right) \leq u \quad \text {f o r a l l} \quad 0 \leq u \leq 1. \tag {3.3}
$$

![](images/4d0349520b2329171d2c4dd54aede05609fc1eec275852e6ac43f75016574e92.jpg)  
FIGURE 3.1: Illustration of the FRT

In practice, $M$ is often too large (e.g., with $n = 100$ , $n_1 = 50$ , we have $M > 10^{29}$ ), and it is computationally infeasible to enumerate all possible values of the treatment vector. We often approximate $p_{\mathrm{FRT}}$ by Monte Carlo (see Section A.5 for a review of the basic Monte Carlo method). To be more specific, we take independent random draws from all possible values of the treatment vector, or, equivalently, we randomly permute $Z$ , and approximate $p_{\mathrm{FRT}}$ by

$$
\hat {p} _ {\mathrm {F R T}} = R ^ {- 1} \sum_ {r = 1} ^ {R} I \left\{T \left(\boldsymbol {z} ^ {r}, \boldsymbol {Y}\right) \geq T (\boldsymbol {Z}, \boldsymbol {Y}) \right\}, \tag {3.4}
$$

where the $z^r$ 's are the $R$ random permutations of $Z$ . The $p$ -value in (3.4) has Monte Carlo error decreasing fast with an increasing $R$ ; see Problem 3.2. Because the calculation of the $p$ -value in (3.4) involves permutations of $Z$ , the FRT is sometimes called the permutation test in the context of the CRE. However, the idea of FRT is more general than the permutation test in more complex experiments.

# 3.3 Canonical choices of the test statistic

From the above discussion, the FRT generates finite-sample exact $p$ -value for any choice of the test statistic. This is a feature of the FRT. However, this feature should not encourage arbitrary choice of the test statistic. Intuitively, we must choose test statistics that give information for possible violations of $H_{0\mathrm{F}}$ . Below I will review some canonical choices.

Example 3.1 (difference-in-means) The difference-in-means statistic is

$$
\hat {\tau} = \hat {\bar {Y}} (1) - \hat {\bar {Y}} (0)
$$

where

$$
\hat {\bar {Y}} (1) = n _ {1} ^ {- 1} \sum_ {Z _ {i} = 1} Y _ {i} = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} Y _ {i}
$$

is the sample mean of the outcomes under the treatment and

$$
\hat {\tilde {Y}} (0) = n _ {0} ^ {- 1} \sum_ {Z _ {i} = 0} Y _ {i} = n _ {0} ^ {- 1} \sum_ {i = 1} ^ {n} (1 - Z _ {i}) Y _ {i}
$$

is the sample mean of the outcomes under the control, respectively. Under $H_{0\mathrm{F}}$ , it has mean

$$
E (\hat {\tau}) = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} E (Z _ {i}) Y _ {i} - n _ {0} ^ {- 1} \sum_ {i = 1} ^ {n} E (1 - Z _ {i}) Y _ {i} = 0
$$

and variance

$$
\begin{array}{l} \operatorname {v a r} (\hat {\tau}) = \operatorname {v a r} \left\{n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} Y _ {i} - n _ {0} ^ {- 1} \sum_ {i = 1} ^ {n} (1 - Z _ {i}) Y _ {i} \right\} \\ = \quad \operatorname {v a r} \left(\frac {n}{n _ {0}} \frac {1}{n _ {1}} \sum_ {i = 1} ^ {n} Z _ {i} Y _ {i}\right) \\ = _ {*} \quad \frac {n ^ {2}}{n _ {0} ^ {2}} \left(1 - \frac {n _ {1}}{n}\right) \frac {s ^ {2}}{n _ {1}} \\ { = } { \frac { n } { n _ { 1 } n _ { 0 } } s ^ { 2 } , } \\ \end{array}
$$

where $= _*$ follows from Lemma C.2 for simple random sampling with

$$
\bar {Y} = n ^ {- 1} \sum_ {i = 1} ^ {n} Y _ {i}, \quad s ^ {2} = (n - 1) ^ {- 1} \sum_ {i = 1} ^ {n} (Y _ {i} - \bar {Y}) ^ {2}.
$$

Furthermore, the randomization distribution of $\hat{\tau}$ is approximately Normal due to the finite population central limit theorem (CLT) in Lemma C.4:

$$
\frac {\hat {\tau}}{\sqrt {\frac {n}{n _ {1} n _ {0}} s ^ {2}}} \rightarrow \mathrm {N} (0, 1) \tag {3.5}
$$

in distribution. Since $s^2$ is fixed under $H_{0\mathrm{F}}$ , it is equivalent to use

$$
\frac {\hat {\tau}}{\sqrt {\frac {n}{n _ {1} n _ {0}} s ^ {2}}}
$$

as the test statistic in the FRT, which is asymptotically $\mathrm{N}(0,1)$ as shown in (3.5). Then we can calculate an approximate $p$ -value.

The observed data are $\{Y_{i}:Z_{i} = 1\}$ and $\{Y_{i}:Z_{i} = 0\}$ , so the problem is essentially a two-sample problem. Under the assumption of independent and identically distributed (IID) Normal outcomes (see Section A.4.1), the classic two-sample $t$ -test assuming equal variance is based on

$$
\frac {\hat {\tau}}{\sqrt {\frac {n}{n _ {1} n _ {0} (n - 2)} \left[ \sum_ {Z _ {i} = 1} \left\{Y _ {i} - \hat {\bar {Y}} (1) \right\} ^ {2} + \sum_ {Z _ {i} = 0} \left\{Y _ {i} - \hat {\bar {Y}} (0) \right\} ^ {2} \right]}} \sim t _ {n - 2}. \tag {3.6}
$$

Based on some algebra (see Problem 3.8), we have the expansion

$$
(n - 1) s ^ {2} = \sum_ {Z _ {i} = 1} \left\{Y _ {i} - \hat {\bar {Y}} (1) \right\} ^ {2} + \sum_ {Z _ {i} = 0} \left\{Y _ {i} - \hat {\bar {Y}} (0) \right\} ^ {2} + \frac {n _ {1} n _ {0}}{n} \hat {\tau} ^ {2}. \tag {3.7}
$$

With a large sample size $n$ , we can ignore the difference between $\mathrm{N}(0,1)$ and $t_{n-2}$ and the difference between $n-1$ and $n-2$ . Moreover, under $H_{0\mathrm{F}}$ , $\hat{\tau}$ converges to zero in probability, so $n_1n_0 / n\hat{\tau}^2$ can be ignored asymptotically. Therefore, under $H_{0\mathrm{F}}$ , the approximate $p$ -value in Example 3.1 is close to the $p$ -value from the classic two-sample $t$ -test assuming equal variance, which can be calculated by $\mathbf{t} \cdot \mathbf{t} \cdot \mathbf{s}$ with var. equal = TRUE. Under alternative hypotheses with nonzero $\tau$ , the additional term $\frac{n_1n_0}{n}\hat{\tau}^2$ in the expansion (3.7) can make the FRT less powerful than the usual $t$ -test; Ding (2016) made this point.

Based on the above discussion, the FRT with $\hat{\tau}$ effectively uses a pooled variance ignoring the heteroskedasticity between these two groups. In classical statistics, the two-sample problem with heteroskedastic Normal outcomes is called the Behrens-Fisher problem (see Section A.4.1). In the Behrens-Fisher problem, a standard choice of the test statistic is the studentized statistic below.

Example 3.2 (studentized statistic) The studentized statistic is

$$
t = \frac {\hat {\bar {Y}} (1) - \hat {\bar {Y}} (0)}{\sqrt {\frac {\hat {S} ^ {2} (1)}{n _ {1}} + \frac {\hat {S} ^ {2} (0)}{n _ {0}}}},
$$

where

$$
\hat {S} ^ {2} (1) = \left(n _ {1} - 1\right) ^ {- 1} \sum_ {Z _ {i} = 1} \left\{Y _ {i} - \hat {\bar {Y}} (1) \right\} ^ {2}, \quad \hat {S} ^ {2} (0) = \left(n _ {0} - 1\right) ^ {- 1} \sum_ {Z _ {i} = 0} \left\{Y _ {i} - \hat {\bar {Y}} (0) \right\} ^ {2}
$$

are the sample variances of the observed outcomes under the treatment and control, respectively. Under $H_{0\mathrm{F}}$ , the finite population CLT again implies that it is asymptotically Normal:

$$
t \to \mathrm {N} (0, 1)
$$

in distribution. Then we can calculate an approximate $p$ -value which is close to the $p$ -value from $t$ . test with var equal = FALSE.

An extremely important point is that the FRT justifies the traditional $t$ -tests using t.test with either var.equal = TRUE or var.equal = FALSE, even if the underlying distributions are not Normal. Standard statistics textbooks motivate the $t$ -tests based on the Normality assumption, but the assumption can be too strong in practice. Fortunately, the $t$ -test procedures can still be used as long as the finite population CLTs hold. Even if we do not believe the CLTs, we can still use $\hat{\tau}$ and $t$ as test statistics in the FRT to obtain finite-sample exact $p$ -values.

We will motivate this studentized statistic from another perspective in Chapter 8. The theory there shows that using $t$ in FRT is more robust to heteroskedasticity across the two groups.

The following test statistic is robust to outliers resulting from heavy-tailed outcome data.

Example 3.3 (Wilcoxon rank sum) The difference-in-means statistic $\hat{\tau}$ uses the sample means of the original outcomes, and its sampling distribution depends on the variances of the outcomes. The studentized statistic $t$ uses the sample means and variances of the original outcomes, and its sampling distribution depends on higher moments of the outcomes. This makes $\hat{\tau}$ and $t$ sensitive to outliers.

Another popular test statistic is based on the ranks of the pooled observed outcomes. Let $R_{i}$ denote the rank of $Y_{i}$ in the pooled samples $Y$ :

$$
R _ {i} = \# \left\{j: Y _ {j} \leq Y _ {i} \right\}.
$$

The Wilcoxon rank sum statistic is the sum of the ranks under treatment:

$$
W = \sum_ {i = 1} ^ {n} Z _ {i} R _ {i}.
$$

For algebraic simplicity, we assume that there are no ties in the outcomes. Because the sum of the ranks of the pooled samples is fixed at $1 + 2 + \dots + n = n(n + 1) / 2$ , the Wilcoxon statistic is equivalent to the difference in the means of the ranks under the treatment and control. Under $H_{0\mathrm{F}}$ , the $R_i$ 's are fixed, so $W$ has mean

$$
E (W) = \sum_ {i = 1} ^ {n} E (Z _ {i}) R _ {i} = \frac {n _ {1}}{n} \sum_ {i = 1} ^ {n} i = \frac {n _ {1}}{n} \times \frac {n (n + 1)}{2} = \frac {n _ {1} (n + 1)}{2}
$$

andvariance

$$
\begin{array}{l} \operatorname {v a r} (W) = \operatorname {v a r} \left(n _ {1} \frac {1}{n _ {1}} \sum_ {i = 1} ^ {n} Z _ {i} R _ {i}\right) \\ = _ {*} n _ {1} ^ {2} \left(1 - \frac {n _ {1}}{n}\right) \frac {1}{n _ {1}} \frac {1}{n - 1} \sum_ {i = 1} ^ {n} \left(R _ {i} - \frac {n + 1}{2}\right) ^ {2} \\ = \frac {n _ {1} n _ {0}}{n (n - 1)} \sum_ {i = 1} ^ {n} \left(i - \frac {n + 1}{2}\right) ^ {2} \\ = \frac {n _ {1} n _ {0}}{n (n - 1)} \left\{\sum_ {i = 1} ^ {n} i ^ {2} - n \left(\frac {n + 1}{2}\right) ^ {2} \right\} \\ = \frac {n _ {1} n _ {0}}{n (n - 1)} \left\{\frac {n (n + 1) (2 n + 1)}{6} - n \left(\frac {n + 1}{2}\right) ^ {2} \right\} \\ = \frac {n _ {1} n _ {0} (n + 1)}{1 2}, \\ \end{array}
$$

where $= _*$ follows from Lemma C.2. Furthermore, under $H_{0\mathrm{F}}$ , the finite population CLT ensures that the randomization distribution of $\widehat{\tau}$ is approximately Normal:

$$
\frac {\sum_ {i = 1} ^ {n} Z _ {i} R _ {i} - \frac {n _ {1} (n + 1)}{2}}{\sqrt {\frac {n _ {1} n _ {0} (n + 1)}{1 2}}} \rightarrow \mathrm {N} (0, 1) \tag {3.8}
$$

in distribution. Based on (3.8), we can conduct an asymptotic test. In $R$ , the function wilcox.test can compute both exact and asymptotic $p$ -values based on the statistic $W - n_{1}(n_{1} + 1) / 2$ . Based on some asymptotic analyses, Lehmann (1975) showed that the FRT using $W$ has reasonable power over a wide range of data-generating processes.

Example 3.4 (Kolmogorov-Smirnov statistic) The treatment may affect the outcome in different ways. It seems natural to summarize the treatment outcomes and control outcomes based on the empirical distributions:

$$
\hat {F} _ {1} (y) = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} I (Y _ {i} \leq y), \quad \hat {F} _ {0} (y) = n _ {0} ^ {- 1} \sum_ {i = 1} ^ {n} (1 - Z _ {i}) I (Y _ {i} \leq y).
$$

Comparing these two empirical distributions yields the famous Kolmogorov-Smirnov statistic

$$
D = \max  _ {y} \left| \hat {F} _ {1} (y) - \hat {F} _ {0} (y) \right|.
$$

It is a challenging mathematics problem to derive the distribution of $D$ . With large sample sizes $n_1 \to \infty$ and $n_0 \to \infty$ , its distribution function converges to

$$
\operatorname * {p r} \left(\frac {n _ {1} n _ {0}}{n} D \leq x\right) \to \frac {\sqrt {2 \pi}}{x} \sum_ {j = 1} ^ {\infty} e ^ {- (2 j - 1) ^ {2} \pi^ {2} / (8 x ^ {2})},
$$

based on which we calculate an asymptotic $p$ -value (Van der Vaart, 2000). In $R$ , the function $ks.test$ can compute both exact and asymptotic $p$ -values.

# 3.4 A case study of the LaLonde experimental data

I use LaLonde (1986)'s experimental data to illustrate the FRT. The data are available in the Matching package (Sekhon, 2011):

> library(Matching)
> data(lalonde)
> z = lalonde\(treat
> y = lalonde\)re78

In the above, $\mathbf{z}$ denotes the binary treatment vector indicating whether a unit was randomly assigned to the job training program or not, and $\mathbf{y}$ is the outcome vector representing a unit's real earnings in 1978. Figure 3.2 shows the histograms of the outcomes under the treatment and control.

The following code computes the observed values of the test statistics using existing functions:

```txt
> tauhat = t.test(y[z == 1], y[z == 0],
+ var.equal = TRUE) $statistic
> tauhat
t
2.835321
> student = t.test(y[z == 1], y[z == 0],
+ var.equal = FALSE) $statistic
> student
t
2.674146
> W = wilcox.test(y[z == 1], y[z == 0]) $statistic
> W
W
27402.5
> D = ks.test(y[z == 1], y[z == 0]) $statistic
> D
D
0.1321206 
```

By randomly permuting the treatment vector, we can obtain the Monte Carlo approximation of the randomization distributions of the test statistics, stored in four vectors Tauhat, Student, Wilcox, and Ks.

>MC $= 10\hat{4}$ > Tauhat $\equiv$ rep(0，MC)  
>Student $\equiv$ rep(0，MC)  
> Wilcox $\equiv$ rep(0，MC)

![](images/481b290661e002a6a1ea31bb9a4c5a9d45cc03164e1ca250ea022828da93511e.jpg)  
FIGURE 3.2: Histograms of the outcomes in the LaLonde experimental data: the treatment in white and the control in grey. The vertical lines are the sample means of the outcomes: the solid line for the treatment and the dashed line for the control.

```diff
> Ks = rep(0, MC)
> for (mc in 1:MC)
+ {
+ zperm = sample(z)
+ Tauhat [mc] = t.test(y[zperm == 1], y[zperm == 0],
+ var.equal = TRUE) $statistic
+ Student [mc] = t.test(y[zperm == 1], y[zperm == 0],
+ var.equal = FALSE) $statistic
+ Wilcox [mc] = wilcox.test(y[zperm == 1],
+ y[zperm == 0]) $statistic
+ Ks [mc] = ks.test(y[zperm == 1],
+ y[zperm == 0]) $statistic
+} 
```

The one-sided $p$ -values based on the FRT are all smaller than 0.05:

```txt
> exact.pv = c(mean(Tauhat >= tauhat), + mean(Student >= student), 
```

+ mean（Wilcox $\geq = W$ ）, + mean(Ks $\geq = D$ ）> round(exact.pv，3) [1]0.0020.0020.0060.040

Without using Monte Carlo, we can also compute the asymptotic $p$ -values which are all smaller than 0.05:

```txt
> asym.mpv = c(t.test(y[z == 1], y[z == 0],
+ var unequal = TRUE)$p.value,
+ t.test(y[z == 1], y[z == 0],
+ var unequal = FALSE)$p.value,
+ wilcox.test(y[z == 1], y[z == 0])$p.value,
+ ks.test(y[z == 1], y[z == 0])$p.value)
> round(asym.mpv, 3)
[1] 0.005 0.008 0.011 0.046 
```

The differences between the $p$ -values are due to the asymptotic approximations as well as the fact that the default choices for t.test and wilcox.test are two-sided tests. To make fair comparisons, we need to multiply the first three $p_{\mathrm{FRT}}$ 's by a factor of 2.

Figure 3.3 shows the histograms of the randomization distributions of four test statistics, as well as their corresponding observed values. For the first three test statistics, the Normal approximations work quite well even though the underlying outcome data distribution is far from Normal as shown in Figure 3.2. In general, a figure like Figure 3.3 can give clearer information for testing the sharp null hypothesis. Recently, Bind and Rubin (2020) proposes, in the title of their paper, that "when possible, report a Fisher-exact $p$ -value and display its underlying null randomization distribution." I agree.

# 3.5 Some history of randomized experiments and FRT

# 3.5.1 James Lind's experiment

James Lind (1716-1794) was a Scottish doctor and a pioneer of naval hygiene in the Royal Navy. At his time, scurvy was a major cause of death among sailors. He conducted one of the earliest randomized experiments with clear documentation of the details and concluded that citrus fruits cured scurvy before the discovery of Vitamin C.

In Lind (1753), he described the following randomized experiment with 12 patients of scurvy assigned to 6 groups. With some simplifications, the 6 groups are:

1. two received a quart of cider every day;   
2. two received twenty-five drops of sulfuric acid three times every day;

![](images/80e1db8c82bae947eb041509b9ad960af658e55299bd99cff0a3d61d0d9f474b.jpg)

![](images/d04ea949be989af2e26571d633fbcfa213db314eb8b2dad2420be10839395ce0.jpg)

![](images/fd495aa8483058db5ec8a7b1324c7442c28a2c3162307ad2d464707d52007170.jpg)

![](images/0b00a45d0f3fabc1a1b64ebd750a3140317f9dd1582fba367e5dc6a28aa45ca3.jpg)  
FIGURE 3.3: The randomization distributions of four test statistics based on the LaLonde experimental data

3. two received two spoonfuls of vinegar three times every day;   
4. two received half a pint of seawater every day;   
5. two received two oranges and one lemon every day;   
6. two received a spicy paste plus a drink of barley water every day.

After six days, patients in the fifth group recovered, but patients in other groups did not. If we simplify the treatment as

$$
Z _ {i} = 1 (\text {u n i t} i \text {r e c e i v e d c i t r u s f r u i t s})
$$

and the outcome as

$$
Y _ {i} = 1 (\text {u n i t} i \text {r e c o v e r e d a f t e r s i x d a y s}),
$$

then we have a two-by-two table

<table><tr><td></td><td>Y = 1</td><td>Y = 0</td></tr><tr><td>Z = 1</td><td>2</td><td>0</td></tr><tr><td>Z = 0</td><td>0</td><td>10</td></tr></table>

This is the extremest possible two-by-two table we can observe under this experiment, and the data contain strong evidence for the positive effect of citrus fruits for curing scurvy. Statistically, how do we measure the strength of the evidence?

Following the logic of the FRT, if the treatment has no effect at all (under $H_{0\mathrm{F}}$ ), this extreme two-by-two table will occur with probability

$$
\frac {1}{\binom {1 2} {2}} = \frac {1}{6 6} = 0. 0 1 5
$$

which is the $p_{\mathrm{FRT}}$ . This seems a surprise under $H_{0\mathrm{F}}$ : we can easily reject $H_{0\mathrm{F}}$ at the level of 0.05.

# 3.5.2 Lady tasting tea

Fisher (1935) described the following famous experiment of Lady Tasting Tea.7 A lady claimed that she could tell the difference between the two ways of making milk tea: one with milk added first, and the other with tea added first. This might sound odd to most people. As a statistician, Fisher designed an experiment to test whether the lady could actually tell the difference between the two ways of making milk tea.

He made 8 cups of tea, 4 with milk added first and the other 4 with tea added first. Then he presented these 8 cups of tea in a random order to the lady and asked the lady to pick up the 4 with milk added first. The final experiment result can be summarized in the following two-by-two table:

<table><tr><td></td><td>milk first (lady)</td><td>tea first (lady)</td><td>column sum</td></tr><tr><td>milk first (Fisher)</td><td>X</td><td>4-X</td><td>4</td></tr><tr><td>tea first (Fisher)</td><td>4-X</td><td>X</td><td>4</td></tr><tr><td>row sum</td><td>4</td><td>4</td><td>8</td></tr></table>

The $X$ can be 0,1,2,3,4. In the real experiment, $X = 4$ , which is the most extreme data, strongly suggesting that the lady could tell the difference between the two ways of making milk tea. Again, how do we measure the strength of the evidence?

Under the null hypothesis that the lady could not tell the difference, only one of the $\binom{8}{4}=70$ possible orders yields the two-by-two table with $X=4$ . So the $p$ -value is

$$
p _ {\mathrm {F R T}} = \frac {1}{7 0} = 0. 0 1 4.
$$

Given the significance level of 0.05, we reject the null hypothesis.

# 3.5.3 Two Fisherian principles for experiments

In the above two examples in Sections 3.5.1 and 3.5.2, the $p_{\mathrm{FRT}}$ 's are justified by the randomization of the experiments. This highlights the first Fisherian principle of experiments: randomization.

Moreover, the above two experiments are in some sense the smallest possible experiments that can yield statistically meaningful results. For instance, if Lind only assigned one patient to each of the six groups, then the smallest $p$ -value is

$$
\frac {1}{\binom {6} {1}} = \frac {1}{6} = 0. 1 6 7;
$$

if Fisher only made 6 cups of tea, 3 with milk added first and the other 3 with tea added first, then the smallest $p$ -value is

$$
\frac {1}{\binom {6} {3}} = \frac {1}{2 0} = 0. 0 5.
$$

We can never reject the null hypotheses at the level of 0.05. This highlights the second Fisherian principle of experiments: replications. This is, to ensure the FRT to have power, we must have enough units in experiments.

Chapter 5 will discuss the third Fisherian principle of experiments: blocking.

# 3.6 Discussion

# 3.6.1 Other sharp null hypotheses and confidence intervals

I focus on the sharp null hypothesis $H_{0\mathrm{F}}$ above. In fact, the logic of the FRT also works for other sharp null hypotheses. For instance, we can test

$$
H _ {0} (\tau): Y _ {i} (1) - Y _ {i} (0) = \tau_ {i} \text {f o r a l l} i = 1, \dots , n
$$

for a known vector $\pmb{\tau} = (\tau_{1},\dots,\tau_{n})$ . Because the individual causal effects are all known under $H_0(\pmb{\tau})$ , we can impute all missing potential outcomes based on the observed data. With known potential outcomes, the distribution of any test statistic $T = T(\mathbf{Z},\mathbf{Y}(1),\mathbf{Y}(0))$ is completely determined by the treatment assignment mechanism, and therefore, we can compute the corresponding $p_{\mathrm{FRT}}$ as a function of $\pmb{\tau}$ , denoted by $p_{\mathrm{FRT}}(\pmb{\tau})$ . If we can specify all possible $\pmb{\tau}$ 's, then we can compute a series of $p_{\mathrm{FRT}}(\pmb{\tau})$ s. By duality of hypothesis testing and confidence set (see Section A.2.5), we can obtain a $(1 - \alpha)$ -level confidence set for the average causal effect:

$$
\left\{\tau = n ^ {- 1} \sum_ {i = 1} ^ {n} \tau_ {i}: p _ {\mathrm {F R T}} (\boldsymbol {\tau}) \geq \alpha \right\}.
$$

Although this strategy is conceptually straightforward, it has practical complexities due to the large number of all possible $\pmb{\tau}$ 's. In the special case of a binary outcome, Rigdon and Hudgens (2015) and Li and Ding (2016) proposed some computationally feasible approaches to constructing confidence intervals for $\pmb{\tau}$ based on the FRT. For general unbounded outcomes, this strategy is often computationally infeasible.

A canonical simplification (Rosenbaum, 2002b, 2010) is to consider a subclass of the sharp null hypotheses with constant individual causal effects:

$$
H _ {0} (c): Y _ {i} (1) - Y _ {i} (0) = c \mathrm {f o r a l l} i = 1, \ldots , n
$$

for a known constant $c$ . Given $c$ , we can compute $p_{\mathrm{FRT}}(c)$ . By duality, we can obtain a $(1 - \alpha)$ -level confidence set for the average causal effect:

$$
\left\{c: p _ {\mathrm {F R T}} (c) \geq \alpha \right\}.
$$

Because this procedure only involves a one-dimensional search, it is computationally feasible. However, the constant individual causal effect assumption is too strong. In particular, it does not hold for binary outcomes unless all units have effects 0, -1, or 1. In general, the constant individual causal effect assumption has testable implications that can be rejected by the observed data; Ding et al. (2016) proposed a formal statistical test.

# 3.6.2 Other test statistics

The FRT is a general strategy because it is applicable in any randomized experiment with any test statistic. I have given several examples of test statistics in Section 3.3. In fact, the definition of a test statistic can be much more general. For instance, with pre-treatment covariate matrix $\mathbf{X}$ with the $i$ th row being $X_{i}$ for unit $i$ ( $i = 1, \dots, n$ )<sup>8</sup>, we can allow the test statistic $T(\mathbf{Z}, \mathbf{Y}, \mathbf{X})$ to be a function of the treatment vector, outcome vector, and the covariate matrix. Problem 3.6 gives an example.

# 3.6.3 Final remarks

For a general experiment, the probability distribution of $Z$ is not uniform over all possible permutations of $n_1$ 1's and $n_0$ 0's. However, its distribution is completely known by the experimenter. Therefore, we can always simulate its distribution which in turn implies the distribution of any test statistic under the sharp null hypothesis. A finite-sample exact $p$ -value equals

$$
p _ {\mathrm {F R T}} = \operatorname {p r} ^ {\prime} \left\{T \left(\boldsymbol {Z} ^ {\prime}, \boldsymbol {Y}\right) \geq T (\boldsymbol {Z}, \boldsymbol {Y}) \right\}
$$

where $\mathrm{pr}'$ is average over the distribution of $Z'$ conditional on data. I will discuss other experiments in the subsequent chapters and I want to emphasize that the FRT works beyond the specific experiments discussed in this book.

The FRT works with any test statistic. However, this does not answer the practical question of how to choose a test statistic in the data analysis. If the goal is to find surprises with respect to the sharp null hypothesis, it is desirable to choose a test statistic that yields high power under alternative hypotheses. In general, no test statistic can dominate others in terms of power because power depends on the alternative hypothesis. The four test statistics in Section 3.3 are motivated by different alternative hypotheses. For instance, $\hat{\tau}$ and $t$ are motivated by an alternative hypothesis with a nonzero average treatment effect; $W$ is motivated by an alternative hypothesis with a constant causal effect with heavy-tailed outcomes. Specifying a working alternative hypothesis is often helpful for constructing a test statistic although it does not have to be precise to guarantee the validity of the FRT. Problems 3.6 and 3.7 illustrate the idea of using a working alternative hypothesis or statistical model to construct test statistics.

# 3.7 Homework Problems

# 3.1 Exactness of $p_{\mathrm{FRT}}$

Prove (3.3).

# 3.2 Monte Carlo error of $\hat{p}_{\mathrm{FRT}}$

Given data, $p_{\mathrm{FRT}}$ is a fixed number while its Monte Carlo estimator $\hat{p}_{\mathrm{FRT}}$ in (3.4) is random. Show that

$$
E _ {\mathrm {m c}} (\hat {p} _ {\mathrm {F R T}}) = p _ {\mathrm {F R T}}
$$

and

$$
\operatorname {v a r} _ {\mathrm {m c}} \left(\hat {p} _ {\mathrm {F R T}}\right) \leq \frac {1}{4 R},
$$

where the subscript "mc" signifies the randomness due to Monte Carlo, that is, $\hat{p}_{\mathrm{FRT}}$ is random because $z^{r}$ 's are $R$ independent random draws from all possible values of $Z$ .

Remark: $p_{\mathrm{FRT}}$ is random because $Z$ is random. But in this problem, we condition on data, so $p_{\mathrm{FRT}}$ becomes a fixed number. $\hat{p}_{\mathrm{FRT}}$ is random because the $z^r$ 's are random permutations of $Z$ . Problem 3.2 shows that $\hat{p}_{\mathrm{FRT}}$ is unbiased for $p_{\mathrm{FRT}}$ over the Monte Carlo randomness and gives an upper bound on the variance of $\hat{p}_{\mathrm{FRT}}$ . Luo et al. (2021, Theorem 2) gives a more delicate bound on the Monte Carlo error.

# 3.3 A finite-sample valid Monte Carlo approximation of $p_{\mathrm{FRT}}$

Although $\hat{p}_{\mathrm{FRT}}$ is unbiased for $p_{\mathrm{FRT}}$ by the result in Problem 3.2, it may not be a valid $p$ -value in the sense that $\operatorname{pr}(\hat{p}_{\mathrm{FRT}} \leq u) \leq u$ for all $u \in (0,1)$ due to Monte Carlo error with a finite $R$ . The following modified Monte Carlo approximation is always a finite-sample valid $p$ -value. Phipson and Smyth (2010) pointed out this trick in the permutation test.

Define

$$
\tilde {p} _ {\mathrm {F R T}} = \frac {1 + \sum_ {r = 1} ^ {R} I \left\{T \left(\boldsymbol {z} ^ {r} , \boldsymbol {Y}\right) \geq T (\boldsymbol {Z} , \boldsymbol {Y}) \right\}}{1 + R}
$$

where the $z^r$ 's the $R$ random permutations of $Z$ . Show that with an arbitrary $R$ , the Monte Carlo approximation $\tilde{p}_{\mathrm{FRT}}$ is always a finite-sample valid $p$ -value in the sense that $\operatorname{pr}(\tilde{p}_{\mathrm{FRT}} \leq u) \leq u$ for all $u \in (0,1)$ .

Remark: You can use the following two basic probability results to prove the claim in Problem 3.3.

Lemma 3.1 For two Binomial random variables $X_{1} \sim \text{Binomial}(R, p_{1})$ and $X_{2} \sim \text{Binomial}(R, p_{2})$ with $p_{1} \geq p_{2}$ , we have $\operatorname{pr}(X_{1} \leq x) \leq \operatorname{pr}(X_{2} \leq x)$ for all $x$ .

Lemma 3.2 If $p \sim \text{Uniform}(0,1)$ and $X \mid p \sim \text{Binomial}(R,p)$ , then, marginally, $X$ is a uniform random variable over $\{0,1,\ldots,R\}$ .

# 3.4 Fisher's exact test

Consider a CRE with a binary outcome, with data summarized in the following two-by-two table:

<table><tr><td></td><td>Y = 1</td><td>Y = 0</td><td>total</td></tr><tr><td>Z = 1</td><td>n11</td><td>n10</td><td>n1</td></tr><tr><td>Z = 0</td><td>n01</td><td>n00</td><td>n0</td></tr></table>

Under $H_{0\mathrm{F}}$ , show that any test statistic $T(n_{11},n_{10},n_{01},n_{00})$ is a function of $n_{11}$ and other non-random fixed constants, and the exact distribution of $n_{11}$ is Hypergeometric. Specify the parameters for the Hypergeometric distribution.

Remark: Barnard (1947) and Ding and Dasgupta (2016) pointed out the equivalence of Fisher's exact test (reviewed in Section A.3.1) and the FRT under a CRE with a binary outcome.

# 3.5 More details for lady tasting tea

Recall the example in Section 3.5.2. Calculate $\operatorname{pr}(X = k)$ for $k = 0,1,2,3,4$ .

# 3.6 Covariate-adjusted FRT

This problem gives more details for Section 3.6.2.

Section 3.4 re-analyzed the LaLonde experimental data using the FRT with four test statistics. With additional covariates, the FRT can be more general

with at least the following two additional strategies. Assume all potential outcomes and covariates are fixed numbers.

First, we can use test statistics based on residuals from the linear regression. Run a linear regression of the outcomes on the covariates, and obtain the residuals (i.e., view the residuals as the "pseudo outcomes"). Then define the four test statistics based on the residuals. Conduct the FRT using these four new test statistics. Report the corresponding $p$ -values.

Second, we can define the test statistic as the coefficient in the linear regression of the outcomes on the treatment and covariates. Conduct the FRT using this test statistic. Report the corresponding $p$ -value.

Why are the five $p$ -values from the above two strategies finite-sample exact? Justify them.

# 3.7 FRT with a generalized linear model

Use the same dataset as Problem 3.6 but change the outcome to a binary indicator for whether re78 is positive or not. Run logistic regression of the outcome on the treatment and covariates. Is the coefficient of the treatment significant and what is the $p$ -value? Calculate the $p$ -value from the FRT using the coefficient of the treatment as the test statistic.

# 3.8 An algebraic detail

Verify (3.7).

# 3.9 Recommended reading

Bind and Rubin (2020) is a recent paper advocating the use of $p$ -values as well as the display of the corresponding randomization distributions in analyzing complex experiments.

# 4

# Neymanian Repeated Sampling Inference in Completely Randomized Experiments

In his seminal paper, Neyman (1923) not only proposed the notation of potential outcomes but also derived rigorous mathematical results for making inference for the average causal effect under a CRE. In contrast to Fisher's idea of calculating the $p$ -value under the sharp null hypothesis, Neyman (1923) proposed an unbiased point estimator and a conservative confidence interval based on the sampling distribution of the point estimator. This chapter will introduce Neyman (1923)'s fundamental results, which are very important for understanding later chapters in Part II of this book.

# 4.1 Finite population quantities

Consider a CRE with $n$ units, where $n_1$ of them receive the treatment and $n_0$ of them receive the control. For unit $i = 1, \ldots, n$ , we have potential outcomes $Y_i(1)$ and $Y_i(0)$ , and individual effect $\tau_i = Y_i(1) - Y_i(0)$ . The potential outcomes have finite population means

$$
\bar {Y} (1) = n ^ {- 1} \sum_ {i = 1} ^ {n} Y _ {i} (1), \quad \bar {Y} (0) = n ^ {- 1} \sum_ {i = 1} ^ {n} Y _ {i} (0),
$$

variances

$$
S ^ {2} (1) = (n - 1) ^ {- 1} \sum_ {i = 1} ^ {n} \left\{Y _ {i} (1) - \bar {Y} (1) \right\} ^ {2}, \quad S ^ {2} (0) = (n - 1) ^ {- 1} \sum_ {i = 1} ^ {n} \left\{Y _ {i} (0) - \bar {Y} (0) \right\} ^ {2},
$$

and covariance

$$
S (1, 0) = (n - 1) ^ {- 1} \sum_ {i = 1} ^ {n} \left\{Y _ {i} (1) - \bar {Y} (1) \right\} \left\{Y _ {i} (0) - \bar {Y} (0) \right\}.
$$

The individual effects have mean

$$
\tau = n ^ {- 1} \sum_ {i = 1} ^ {n} \tau_ {i} = \bar {Y} (1) - \bar {Y} (0).
$$

and variance

$$
S ^ {2} (\tau) = (n - 1) ^ {- 1} \sum_ {i = 1} ^ {n} (\tau_ {i} - \tau) ^ {2}.
$$

We have the following relationship between the variances and covariance.

Lemma 4.1 $2S(1,0) = S^{2}(1) + S^{2}(0) - S^{2}(\tau)$ .

Lemma 4.1 is a basic result and will be useful for later discussion. The proof of Lemma 4.1 follows from elementary algebra. I leave it as Problem 4.1.

These fixed quantities are functions of the Science Table $\{Y_{i}(1), Y_{i}(0)\}_{i=1}^{n}$ . We are interested in estimating the average causal effect $\tau$ based on the data $(Z_{i}, Y_{i})_{i=1}^{n}$ from a CRE.

# 4.2 Neyman (1923)'s theorem

Based on the observed outcomes, we can calculate the sample means

$$
\hat {\tilde {Y}} (1) = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} Y _ {i}, \quad \hat {\tilde {Y}} (0) = n _ {0} ^ {- 1} \sum_ {i = 1} ^ {n} (1 - Z _ {i}) Y _ {i},
$$

the sample variances

$$
\hat {S} ^ {2} (1) = \left(n _ {1} - 1\right) ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} \left\{Y _ {i} - \hat {\bar {Y}} (1) \right\} ^ {2}, \quad \hat {S} ^ {2} (0) = \left(n _ {0} - 1\right) ^ {- 1} \sum_ {i = 1} ^ {n} \left(1 - Z _ {i}\right) \left\{Y _ {i} - \hat {\bar {Y}} (0) \right\} ^ {2}.
$$

But there are no sample versions of $S(1,0)$ and $S^2(\tau)$ because the potential outcomes $Y_i(1)$ and $Y_i(0)$ are never jointly observed for each unit $i$ . Neyman (1923) proved the following theorem.

Theorem 4.1 Under a CRE,

1. the difference-in-means estimator $\hat{\tau} = \hat{\bar{Y}}(1) - \hat{\bar{Y}}(0)$ is unbiased for $\tau$ :

$$
E (\hat {\tau}) = \tau ;
$$

2. $\hat{\tau}$ has variance

$$
\begin{array}{l} \operatorname {v a r} (\hat {\tau}) = \frac {S ^ {2} (1)}{n _ {1}} + \frac {S ^ {2} (0)}{n _ {0}} - \frac {S ^ {2} (\tau)}{n} (4.1) \\ = \frac {n _ {0}}{n _ {1} n} S ^ {2} (1) + \frac {n _ {1}}{n _ {0} n} S ^ {2} (0) + \frac {2}{n} S (1, 0); (4.2) \\ \end{array}
$$

3. the variance estimator

$$
\hat {V} = \frac {\hat {S} ^ {2} (1)}{n _ {1}} + \frac {\hat {S} ^ {2} (0)}{n _ {0}}
$$

is conservative for estimating $\operatorname{var}(\hat{\tau})$ in the sense that

$$
E (\hat {V}) - \mathrm {v a r} (\hat {\tau}) = \frac {S ^ {2} (\tau)}{n} \geq 0
$$

with equality holding if and only if $\tau_{i} = \tau$ for all units.

I will present the proof of Theorem 4.1 in Section 4.3. Before proving Theorem 4.1, it is important to clarify the meanings of $E(\cdot)$ and $\mathrm{var}(\cdot)$ in Theorem 4.1. The potential outcomes are all fixed numbers, and only the treatment indicators $Z_{i}$ 's are random. Therefore, the expectations and variances are all over the randomness of the $Z_{i}$ 's, which are random permutations of $n_1$ 1's and $n_0$ 0's. Figure 4.1 illustrates the randomness of $\hat{\tau}$ , which is a discrete uniform distribution over $\{\hat{\tau}^1, \dots, \hat{\tau}^M\}$ induced by $M = \binom{n}{n_1}$ possible treatment allocations. Compare Figure 4.1 with Figure 3.1 to see the key differences between the FRT and Neyman (1923)'s theorem:

1. The FRT works for any test statistic but Neyman (1923)'s theorem is only about the difference in means. Although we could derive the properties of other estimators similar to Neyman (1923)'s theorem, this mathematical exercise is often quite challenging for general estimators.   
2. In Figure 3.1, the observed outcome vector $\mathbf{Y}$ is fixed but in Figure 4.1, the observed outcome vector $\mathbf{Y}(\mathbf{z}^m)$ changes as $\mathbf{z}^m$ changes.   
3. The $T(\pmb{z}^m, \pmb{Y})$ 's In Figure 3.1 are all computable based on the observed data, but the $\hat{\tau}^{m}$ 's in Figure 4.1 are hypothetical values because not all potential outcomes are known.

The point estimator $\hat{\tau}$ is standard but it has a non-trivial variance under the potential outcomes framework with a CRE. The variance formula (4.1) differs from the classic variance formula for the difference in means because it not only depends on the finite population variances of the potential outcomes but also depends on the finite population variance of the individual effects, or, equivalently, the finite population covariance of the potential outcomes.

![](images/b2ed548e54e531624bf472d8d1ce8007d27da5353e2dbf68059f2dd95170365c.jpg)  
FIGURE 4.1: Illustration of Neyman (1923)'s theorem, where $\mathbf{Y}(\mathbf{z}^m)$ is the observed outcome vector under the treatment vector $\mathbf{z}^m$ .

Unfortunately, $S^2(\tau)$ and $S(1,0)$ are not identifiable from the data because $Y_i(1)$ and $Y_i(0)$ are never jointly observed.

The formula (4.1) is a little puzzling in that the more heterogeneous the individual effects are the smaller the variability of $\hat{\tau}$ is. Section 4.5.1 will use numerical examples to verify (4.1). What is the intuition here? I give an explanation based on the equivalent form (4.2). Compare the case with positively correlated potential outcomes and the case with negatively correlated potential outcomes. Although the treatment group is a simple random sample from the finite population of $n$ units, it is possible to observe relatively large treatment potential outcomes in a realized experiment. Assume this happens.

1. If $S(1,0) > 0$ , then those treated units also have relatively large control potential outcomes. Consequently, the observed outcomes under control are relatively small, which results in large $\hat{\tau}$ .   
2. If $S(1,0) < 0$ , then those treated units have relatively small control potential outcomes. Consequently, the observed outcomes under control are relatively large, which results in small $\hat{\tau}$ .

The reverse can also happen if we observe relatively small treatment potential outcomes in a realized experiment. Overall, although the unbiasedness of $\hat{\tau}$ does not depend on the correlation between the potential outcomes, it is more likely to observe more extreme $\hat{\tau}$ under $S(1,0) > 0$ than under $S(1,0) < 0$ . So the variance of $\hat{\tau}$ is larger when the potential outcomes are positively correlated.

Li and Ding (2017, Theorem 5 and Proposition 3) further proved the following asymptotic Normality of $\hat{\tau}$ based on the finite population CLT.

Theorem 4.2 Let $n \to \infty$ and $n_1 \to \infty$ . If $n_1 / n$ has a limiting value in

# 4.3 Proofs

$(0,1),\{S^{2}(1),S^{2}(0),S(1,0)\}$ have limiting values, and

$$
\max  _ {1 \leq i \leq n} \left\{Y _ {i} (1) - \bar {Y} (1) \right\} ^ {2} / n \to 0, \quad \max  _ {1 \leq i \leq n} \left\{Y _ {i} (0) - \bar {Y} (0) \right\} ^ {2} / n \to 0,
$$

then

$$
\frac {\hat {\tau} - \tau}{\sqrt {\operatorname {v a r} (\hat {\tau})}} \to \mathrm {N} (0, 1)
$$

in distribution, and

$$
\hat {S} ^ {2} (1) \to S ^ {2} (1), \quad \hat {S} ^ {2} (0) \to S ^ {2} (0)
$$

in probability.

The proof of Theorem 4.2 is technical and beyond the scope of this book. It ensures that the sampling distribution of $\hat{\tau}$ can be approximated by a Normal distribution with a large sample size and some regularity conditions. Moreover, it ensures that the sample variances of the outcomes are consistent for the population variances, which further ensures that the probability limit of Neyman (1923)'s variance estimator is larger than the true variance of $\hat{\tau}$ . This justifies a conservative large-sample confidence interval for $\tau$ :

$$
\hat {\tau} \pm z _ {1 - \alpha / 2} \sqrt {\hat {V}},
$$

where $z_{1 - \alpha /2}$ is the $1 - \alpha /2$ upper quantile of the standard Normal random variable. It is the same as the confidence interval for the standard two-sample problem asymptotically (see Chapter A.4.1). This confidence interval covers $\tau$ with probability at least as large as $1 - \alpha$ when the sample size is large enough. By duality, the confidence interval implies a test for

$$
H _ {0 \mathrm {N}}: \tau = 0,
$$

which is called the weak null hypothesis.

Due to the fundamental problem of missing one potential outcome, we can at most obtain a conservative variance estimator. In statistics, the definition of the confidence interval allows for over coverage and thus conservativeness in variance estimation (see Chapter A.2). Conservativeness is not a big problem if underreporting the treatment effect is not a big problem in practice. Sometimes, it can be problematic if the outcomes measure the side effects of a treatment. In medical experiments, underreporting the side effects of a new drug can have severe consequences on patients' health.

# 4.3 Proofs

In this section, I will prove Theorem 4.1.

First, the unbiasedness of $\hat{\tau}$ follows from the representation

$$
\begin{array}{l} \hat {\tau} = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} Y _ {i} - n _ {0} ^ {- 1} \sum_ {i = 1} ^ {n} (1 - Z _ {i}) Y _ {i} \\ = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} Y _ {i} (1) - n _ {0} ^ {- 1} \sum_ {i = 1} ^ {n} (1 - Z _ {i}) Y _ {i} (0) \\ \end{array}
$$

and the linearity of the expectation:

$$
\begin{array}{l} E (\hat {\tau}) = E \left\{n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} Y _ {i} (1) - n _ {0} ^ {- 1} \sum_ {i = 1} ^ {n} (1 - Z _ {i}) Y _ {i} (0) \right\} \\ = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} E (Z _ {i}) Y _ {i} (1) - n _ {0} ^ {- 1} \sum_ {i = 1} ^ {n} E (1 - Z _ {i}) Y _ {i} (0) \\ = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} \frac {n _ {1}}{n} Y _ {i} (1) - n _ {0} ^ {- 1} \sum_ {i = 1} ^ {n} \frac {n _ {0}}{n} Y _ {i} (0) \\ = \quad n ^ {- 1} \sum_ {i = 1} ^ {n} Y _ {i} (1) - n ^ {- 1} \sum_ {i = 1} ^ {n} Y _ {i} (0) \\ = \tau . \\ \end{array}
$$

Second, we can further write $\hat{\tau}$ as

$$
\hat {\tau} = \sum_ {i = 1} ^ {n} Z _ {i} \left\{\frac {Y _ {i} (1)}{n _ {1}} + \frac {Y _ {i} (0)}{n _ {0}} \right\} - n _ {0} ^ {- 1} \sum_ {i = 1} ^ {n} Y _ {i} (0).
$$

The variance of $\hat{\tau}$ follows from Lemma C.2 of simple random sampling:

$$
\begin{array}{l} \mathrm {v a r} (\hat {\tau}) = \frac {n _ {1} n _ {0}}{n (n - 1)} \sum_ {i = 1} ^ {n} \left\{\frac {Y _ {i} (1)}{n _ {1}} + \frac {Y _ {i} (0)}{n _ {0}} - \frac {\bar {Y} (1)}{n _ {1}} - \frac {\bar {Y} (0)}{n _ {0}} \right\} ^ {2} \\ = \frac {n _ {1} n _ {0}}{n (n - 1)} \left[ \frac {1}{n _ {1} ^ {2}} \sum_ {i = 1} ^ {n} \left\{Y _ {i} (1) - \bar {Y} (1) \right\} ^ {2} + \frac {1}{n _ {0} ^ {2}} \sum_ {i = 1} ^ {n} \left\{Y _ {i} (0) - \bar {Y} (0) \right\} ^ {2} \right. \\ \left. + \frac {2}{n _ {1} n _ {0}} \sum_ {i = 1} ^ {n} \left\{Y _ {i} (1) - \bar {Y} (1) \right\} \left\{Y _ {i} (0) - \bar {Y} (0) \right\} \right] \\ = \frac {n _ {0}}{n _ {1} n} S ^ {2} (1) + \frac {n _ {1}}{n _ {0} n} S ^ {2} (0) + \frac {2}{n} S (1, 0). \\ \end{array}
$$

From Lemma 4.1, we can also write the variance as

$$
\begin{array}{l} \operatorname {v a r} (\hat {\tau}) = \frac {n _ {0}}{n _ {1} n} S ^ {2} (1) + \frac {n _ {1}}{n _ {0} n} S ^ {2} (0) + \frac {1}{n} \left\{S ^ {2} (1) + S ^ {2} (0) - S ^ {2} (\tau) \right\} \\ = \frac {S ^ {2} (1)}{n _ {1}} + \frac {S ^ {2} (0)}{n _ {0}} - \frac {S ^ {2} (\tau)}{n}. \\ \end{array}
$$

Third, because the treatment group is a simple random sample of size $n_1$ from the $n$ units, Lemma C.3 ensures that the sample variance of $Y_{i}(1)$ 's is unbiased for its population variance:

$$
E \{\hat {S} ^ {2} (1) \} = S ^ {2} (1).
$$

Similarly, $E\{\hat{S}^2(0)\} = S^2(0)$ . Therefore, $\hat{V}$ is unbiased for the first two terms in (4.1).

# 4.4 Regression analysis of the CRE

Practitioners often use regression-based inference for the average causal effect $\tau$ . A standard approach is to run the ordinary least squares (OLS) of the outcomes on the treatment indicators with an intercept

$$
(\hat {\alpha}, \hat {\beta}) = \arg \min _ {(a, b)} \sum_ {i = 1} ^ {n} (Y _ {i} - a - b Z _ {i}) ^ {2},
$$

and use the coefficient of the treatment $\hat{\beta}$ as the estimator for the average causal effect. We can show the coefficient $\hat{\beta}$ equals the difference in means:

$$
\hat {\beta} = \hat {\tau}. \tag {4.3}
$$

However, the usual variance estimator from the OLS (see (B.4) in Chapter B), e.g., the output from the $1\mathrm{m}$ function of $\mathsf{R}$ , equals

$$
\begin{array}{l} \hat {V} _ {\mathrm {O L S}} = \frac {n (n _ {1} - 1)}{(n - 2) n _ {1} n _ {0}} \hat {S} ^ {2} (1) + \frac {n (n _ {0} - 1)}{(n - 2) n _ {1} n _ {0}} \hat {S} ^ {2} (0) \tag {4.4} \\ \approx \frac {\hat {S} ^ {2} (1)}{n _ {0}} + \frac {\hat {S} ^ {2} (0)}{n _ {1}}, \\ \end{array}
$$

where the approximation holds with large $n_1$ and $n_0$ . It differs from $\hat{V}$ even with large $n_1$ and $n_0$ .

Fortunately, the Eicker-Huber-White (EHW) robust variance estimator (see (B.3) in Chapter B) is close to $\hat{V}$ :

$$
\begin{array}{l} \hat {V} _ {\mathrm {E H W}} = \frac {\hat {S} ^ {2} (1)}{n _ {1}} \frac {n _ {1} - 1}{n _ {1}} + \frac {\hat {S} ^ {2} (0)}{n _ {0}} \frac {n _ {0} - 1}{n _ {0}} \tag {4.5} \\ \approx \frac {\hat {S} ^ {2} (1)}{n _ {1}} + \frac {\hat {S} ^ {2} (0)}{n _ {0}} \\ \end{array}
$$

where the approximation holds with large $n_1$ and $n_0$ . It is almost identical to $\hat{V}$ . Moreover, the so-called HC2 variant of the EHW robust variance estimator is identical to $\hat{V}$ . The hccm function in the car package returns the EHW robust variance estimator as well as its HC2 variant.

Problem 4.3 provides more technical details for (4.3)-(4.5).

# 4.5 Examples

# 4.5.1 Simulation

I first choose the sample size as $n = 100$ with 60 treated and 40 control units, and generate the potential outcomes with constant individual causal effects.

```txt
n = 100  
n1 = 60  
n0 = 40  
y0 = rexp(n)  
y0 = sort(y0, decreasing = TRUE)  
y1 = y0 + 1 
```

With the Science Table fixed, I repeatedly generate CREs and apply Theorem 4.1 to obtain the point estimator, the conservative variance estimator, and the confidence interval based on the Normal approximation. The $(1,1)$ th panel of Figure 4.2 shows the scatter plot of the potential outcomes, and the $(1,2)$ th panel of Figure 4.2 shows the histogram of $\hat{\tau} - \tau$ .

I then change the potential outcomes by sorting the control potential outcomes in reverse order

```txt
y0 = sort(y0, decreasing = FALSE) 
```

and repeat the above simulation. The $(2,1)$ th panel of Figure 4.2 shows the scatter plot of the potential outcomes, and the $(2,2)$ th panel of Figure 4.2 shows the histogram of $\hat{\tau} -\tau$

I finally permute the control potential outcomes randomly

```txt
y0 = sample(y0) 
```

and repeat the above simulation. The (3,1)th panel of Figure 4.2 shows the scatter plot of the potential outcomes, and the (2,2)th panel of Figure 4.2 shows the histogram of $\hat{\tau} - \tau$ .

Importantly, in the above three sets of simulations, the correlations between potential outcomes are different but the marginal distributions are the same. The following table compares the true variances, the average estimated variances, and the coverage rates of the $95\%$ confidence intervals.

<table><tr><td></td><td>constant</td><td>negative</td><td>independent</td></tr><tr><td>var</td><td>0.036</td><td>0.007</td><td>0.020</td></tr><tr><td>estimated var</td><td>0.036</td><td>0.036</td><td>0.036</td></tr><tr><td>coverage rate</td><td>0.947</td><td>1.000</td><td>0.989</td></tr></table>

The true variance depends on the correlation between the potential outcomes, with positively correlated potential outcomes corresponding to a larger sampling variance. This verifies (4.2). The estimated variances are almost identical because the formula of $\hat{V}$ depends only on the marginal distributions of the potential outcomes. Due to the discrepancy between the true and estimated

# 4.5 Examples

variances, the coverage rates differ across the three sets of simulations. Only with constant causal effects, the estimated variance is identical to the true variance, verifying point 3 of Theorem 4.1.

Figure 4.2 also shows the Normal density curves based on the CLT for $\hat{\tau}$ . They are very close to the histogram over simulations, verifying Theorem 4.2.

# 4.5.2 Heavy-tailed outcome and failure of Normal approximations

The CLT of $\hat{\tau}$ in Theorem 4.2 holds under some regularity conditions. Those conditions will be violated with heavy-tailed potential outcomes. We can modify the above simulation studies to illustrate this point. Assume the individual causal effects are constant but the control potential outcomes are contaminated by a Cauchy component with probability 0.1, 0.3, or 0.5. The following code generates the potential outcomes with the probability of contamination being 0.1.

```txt
eps = rbinom(n, 1, 0.1)  
y0 = (1 - eps) * rexp(n) + eps * rcauchy(n)  
y1 = y0 + 1 
```

Figures 4.3 and 4.4 show two realizations of the histograms of $\hat{\tau} -\tau$ with the corresponding Normal approximations. With heavy-tailed potential outcomes, the Normal approximations are quite poor. Moreover, unlike Figure 4.2, the histograms are quite sensitive to the random seed of the simulation.

# 4.5.3 Application

I analyzed the lalonde data in Chapter 3.4 to illustrate the idea of the FRT. Now I use the data to illustrate the theory in this chapter.

> library(Matching)
> data(lalonde)
> z = lalonde\(treat
> y = lalonde\)re78

We can easily calculate the point estimator and standard error based on the formulas in Theorem 4.1:

```txt
> n1 = sum(z)  
> n0 = length(z) - n1  
> tauhat = mean(y[z==1]) - mean(y[z==0])  
> what = var(y[z==1])/n1 + var(y[z==0])/n0  
> sehat = sqrt(what)  
> tauhat  
[1] 1794.343  
> sehat  
[1] 670.9967 
```

![](images/b83263aaffc194dcfa513c42e7d4bcece27a78dbb15b6cd369528e1d206f0462.jpg)

![](images/635f57f9c1a4036639b54a95a5db0fb0063825bda6109f917b6ec369f563b042.jpg)

![](images/cd3d69f43be3e91bbda56ff85bf3dad657f0f44e1c79892c28586e3ff80212f7.jpg)

![](images/63b9f48545dad64018ee4c460d9d6800b53a1bcb0fd283e1eb1a6ed9c0f4d01d.jpg)

![](images/da8210420bba46fa05c179fa84e33c7aed65253a1c72120869589e5a702ca85e.jpg)

![](images/a4c7fd315da2e707d5ed913fd5f134d55264e52a2610177917fbcbbe62ca229a.jpg)  
FIGURE 4.2: Left: joint distributions of the potential outcomes with the same marginal distributions. Right: sampling distribution of $\hat{\tau} -\tau$ over $10^{4}$ simulations with different joint distributions of the potential outcomes.

![](images/e659688d2d2a0b4b00b7a4ccde9b7d89e77c6a7fbccbdafae3c490152c8caa4d.jpg)

![](images/4ae905f9cb85c13a4ffd1c6cbfb2c10bd0c4b4fc3e2b9d7509ad8452d9a60673.jpg)

![](images/3b9e1f083ea4a586695a0c196a63bac19ba84edf2ced3138244302de500a2a65.jpg)  
FIGURE 4.3: Sampling distribution of $\hat{\tau} -\tau$ with contaminated potential outcomes (with different contamination probabilities): realization one

![](images/6467264934d61411987dbe5bca0e34fe4493799e624c883dabe74fbed5940c6a.jpg)

![](images/8260fa05d3bdf6123732798cfa827191deddb87355f1fd334f347de020b51460.jpg)

![](images/e82de9a8edc1fac6f48408fcb2ffeaf9577b8628f6fdcced48f3c7f0b2f6c826.jpg)  
FIGURE 4.4: Sampling distribution of $\hat{\tau} -\tau$ with contaminated potential outcomes (with different contamination probabilities): realization two

Practitioners often use OLS to estimate the average causal effect which also gives a standard error.

```txt
> olsfit = lm(y ~ z)
> summary(olsfit) $ coef [2, 1: 2]
Estimate Std. Error
1794.3431 632.8536 
```

However, the above standard error seems too small compared to the one based on Theorem 4.1. This can be solved by using the EHW robust standard error.

```txt
> library(car)  
> sqrt(hccm(olsfit)[2, 2])  
[1] 672.6823  
> sqrt(hccm(olsfit, type = "hc0") [2, 2])  
[1] 669.3155  
> sqrt(hccm(olsfit, type = "hc2") [2, 2])  
[1] 670.9967 
```

# 4.6 Homework Problems

# 4.1 Proof of Lemma 4.1

Prove Lemma 4.1.

# 4.2 Alternative proof of Theorem 4.1

Under a CRE, calculate

$$
\operatorname {v a r} \{\hat {\bar {Y}} (1) \}, \quad \operatorname {v a r} \{\hat {\bar {Y}} (0) \}, \quad \operatorname {c o v} \{\hat {\bar {Y}} (1), \hat {\bar {Y}} (0) \}
$$

and use these formulas to calculate $\operatorname{var}(\hat{\tau})$ .

Remark: Use the results in Chapter C.

# 4.3 Neymanian inference and OLS

Prove (4.3)-(4.5). Moreover, prove that the HC2 variant of the EHW robust variance estimator recovers $\hat{V}$ exactly.

Remark: Chapter B reviews some important technical results about OLS.

# 4.4 Treatment effect heterogeneity

Show that $S^2(\tau) = 0$ implies that $S^2(1) = S^2(0)$ . Given a counterexample with $S^2(1) = S^2(0)$ but $S^2(\tau) \neq 0$ .

Show that $S^2(1) < S^2(0)$ implies that

$$
S (Y (0), \tau) = (n - 1) ^ {- 1} \sum_ {i = 1} ^ {n} \left\{Y _ {i} (0) - \bar {Y} (0) \right\} (\tau_ {i} - \tau) <   0.
$$

Give a counterexample with $S^2(1) > S^2(0)$ but $S(Y(0), \tau) < 0$ .

Remark: The first result states that no treatment effect heterogeneity implies equal variances in the treated and control potential outcomes. But the converse is not true. The second result states that if the treated potential outcome has a smaller variance than the control potential outcome, then the individual treatment effect is negatively correlated with the control potential outcome. But the converse is not true. Gerber and Green (2012, page 293) and Ding et al. (2019, Appendix B.3) gave related discussions.

# 4.5 A better bound of the variance formula

Neyman (1923)'s conservative variance estimator essentially uses the following upper bound on the true variance:

$$
\mathrm {v a r} (\widehat {\tau}) = \frac {S ^ {2} (1)}{n _ {1}} + \frac {S ^ {2} (0)}{n _ {0}} - \frac {S ^ {2} (\tau)}{n} \leq \frac {S ^ {2} (1)}{n _ {1}} + \frac {S ^ {2} (0)}{n _ {0}},
$$

which uses the trivial fact that $S^2(\tau) \geq 0$ . Show the following upper bound

$$
\operatorname {v a r} (\widehat {\tau}) \leq \frac {1}{n} \left\{\sqrt {\frac {n _ {0}}{n _ {1}}} S (1) + \sqrt {\frac {n _ {1}}{n _ {0}}} S (0) \right\} ^ {2}. \tag {4.6}
$$

When does the equality in (4.6) hold?

The upper bound (4.6) motivates another conservative variance estimator

$$
\hat {V} ^ {\prime} = \frac {1}{n} \left\{\sqrt {\frac {n _ {0}}{n _ {1}}} \hat {S} (1) + \sqrt {\frac {n _ {1}}{n _ {0}}} \hat {S} (0) \right\} ^ {2}.
$$

Section 4.5.1 used $\hat{V}$ in the simulation. Repeat the simulation with an additional comparison with the variance estimator $\hat{V}'$ and the associated confidence interval.

Remark: You may find Section A.1.4 useful for the proof. The upper bound (4.6) can be further improved. Aronow et al. (2014) derived the sharp upper bound for $\mathrm{var}(\hat{\tau})$ using the Frechet-Hoeffding inequality. Those improvements are rarely used in practice mainly for two reasons. First, they are more complicated than $\hat{V}$ which can be conveniently implemented by OLS. Second, the confidence interval based on $\hat{V}$ also works under other formulations, for example, under a true linear model of the outcome on the treatment, but those improvements do not. Although they are theoretically interesting, those improvements have little practical impact.

# 4.6 Vector version of Neyman (1923)

The classic result of Neyman (1923) is about a scalar outcome. It is common to have multiple outcomes in practice. Therefore, we now extend the potential outcomes to vectors. We consider the average causal effect on a vector outcome

$\pmb{V} \in \mathbb{R}^{K}$ :

$$
\tau_ {V} = \frac {1}{n} \sum_ {i = 1} ^ {n} \left\{V _ {i} (1) - V _ {i} (0) \right\},
$$

where $\mathbf{V}_i(1)$ and $\mathbf{V}_i(0)$ are the potential outcomes of $\mathbf{V}$ for unit $i$ . The Neyman-type estimator for $\tau_{\mathbf{V}}$ is the difference between the sample mean vectors of the observed outcomes under treatment and control:

$$
\widehat {\tau} _ {V} = \bar {V} _ {1} - \bar {V} _ {0} = \frac {1}{n _ {1}} \sum_ {i = 1} ^ {n} Z _ {i} V _ {i} - \frac {1}{n _ {0}} \sum_ {i = 1} ^ {n} (1 - Z _ {i}) V _ {i}.
$$

Consider a CRE. Show that $\widehat{\tau}_{\mathbf{V}}$ is unbiased for $\tau_{\mathbf{V}}$ . Find the covariance matrix of $\widehat{\tau}_{\mathbf{V}}$ . Find a (possibly conservative) estimator for the variance.

# 4.7 Inference in the BRE

In this book, I use the following definition for the BRE.

Definition 4.1 (BRE) The treatment indicators $Z_{i}$ 's are IID Bernoulli( $\pi$ ) with $n_1 = \sum_{i=1}^{n} Z_{i}$ receiving the treatment and $n_0 = \sum_{i=1}^{n} (1 - Z_{i})$ receiving the control, respectively.

First, we can use the FRT to analyze the BRE. How do we test $H_{0\mathrm{F}}$ in the BRE? Can we use the same FRT procedure as in the CRE if the actual experiment is the BRE? If yes, give a justification; if no, explain why.

Second, we can obtain point estimators for $\tau$ and find the associated variance estimators, as Neyman (1923) did for the CRE.

1. Is $\hat{\tau}$ unbiased for $\tau$ ? Is it consistent?   
2. Find an unbiased estimator for $\tau$ .   
3. Compare the variance of the above unbiased estimator and the asymptotic variance of $\hat{\tau}$ .

Remark: Under the BRE, the estimator $\hat{\tau}$ does not have finite variance but the variance of its asymptotic distribution is finite.

# 4.8 Recommended reading

Ding (2016) compared the Fisherian approach and Neymanian approach to analyzing the CRE.

# 5

# Stratification and Post-Stratification in Randomized Experiments

Block what you can and randomize what you cannot.

-Box et al. (1978, page 103)

This is the second most famous quote from George Box<sup>1</sup>. This chapter will explain its meaning.

# 5.1 Stratification

A CRE may generate an undesired treatment allocation by chance. Let us start with a CRE with a discrete covariate $X_{i} \in \{1, \dots, K\}$ , and define $n_{[k]} = \# \{i : X_{i} = k\}$ and $\pi_{[k]} = n_{[k]} / n$ as the number and proportion of units in stratum $k$ ( $k = 1, \dots, K$ ). A CRE assigns $n_{1}$ units to the treatment group and $n_{0}$ units to the control group, which results in

$$
n _ {[ k ] 1} = \# \left\{i: X _ {i} = k, Z _ {i} = 1 \right\}, \quad n _ {[ k ] 0} = \# \left\{i: X _ {i} = k, Z _ {i} = 0 \right\}
$$

units in the treatment and control groups, respectively, within stratum $k$ . With positive probability, $n_{[k]1}$ or $n_{[k]0}$ is zero for some $k$ , that is, it is possible that some strata only have treated or control units. Even if none of the $n_{[k]1}$ 's or $n_{[k]0}$ 's are zero, with high probability

$$
\frac {n _ {[ k ] 1}}{n _ {1}} - \frac {n _ {[ k ] 0}}{n _ {0}} \neq 0, \tag {5.1}
$$

and the magnitude can be quite large. So the proportions of units in stratum $k$ are different across the treatment and control groups although on average their difference is zero (see Problem 5.1):

$$
E \left(\frac {n _ {[ k ] 1}}{n _ {1}} - \frac {n _ {[ k ] 0}}{n _ {0}}\right) = 0. \tag {5.2}
$$

When $n_{[k]1} / n_1 - n_{[k]0} / n_0$ is large for some strata $k$ 's, the treatment and control groups have undesirable covariate imbalance. Such covariate imbalance deteriorates the quality of the experiment, making it difficult to interpret the results of the experiment since the difference in the outcomes may be attributed to the treatment or the covariate imbalance.

How can we actively avoid covariate imbalance in the experiment? We can conduct stratified randomized experiments (SRE).

Definition 5.1 (SRE) Fix the $n_{[k]1}$ 's or $n_{[k]0}$ 's. We conduct $K$ independent CREs within the $K$ strata of a discrete covariate $X$ .

In agricultural experiments, the SRE is also called the randomized block design, with the strata called the blocks. Analogously, stratified randomization is also called block randomization. The total number of randomizations in an SRE equals

$$
\prod_ {k = 1} ^ {K} \left( \begin{array}{c} n _ {[ k ]} \\ n _ {[ k ] 1} \end{array} \right),
$$

and each feasible randomization has equal probability. Within stratum $k$ , the proportion of units receiving the treatment is

$$
e _ {[ k ]} = \frac {n _ {[ k ] 1}}{n _ {[ k ]}},
$$

which is also called the propensity score, a concept that will play a central role in Part III of this book (see Definition 11.1). An SRE is different from a CRE: first, all feasible randomizations in an SRE form a subset of all feasible randomizations in a CRE, so

$$
\prod_ {k = 1} ^ {K} \binom {n _ {[ k ]}} {n _ {[ k ] 1}} <   \binom {n} {n _ {1}};
$$

second, $e_{[k]}$ is fixed in an SRE but random in a CRE.

For every unit $i$ , we have potential outcomes $Y_{i}(1)$ and $Y_{i}(0)$ , and individual causal effect $\tau_{i} = Y_{i}(1) - Y_{i}(0)$ . For stratum $k$ , we have the stratum-specific average causal effect

$$
\tau_ {[ k ]} = n _ {[ k ]} ^ {- 1} \sum_ {X _ {i} = k} \tau_ {i}.
$$

The average causal effect is

$$
\tau = n ^ {- 1} \sum_ {i = 1} ^ {n} \tau_ {i} = n ^ {- 1} \sum_ {k = 1} ^ {K} \sum_ {X _ {i} = k} \tau_ {i} = \sum_ {k = 1} ^ {K} \pi_ {[ k ]} \tau_ {[ k ]},
$$

which is a weighted average of the stratum-specific average causal effects.

If we are interested in $\tau_{[k]}$ , then we can use the methods in Chapters 3 and 4 for the CRE within stratum $k$ . Below I will discuss statistical inference for $\tau$ .

# 5.2 FRT

# 5.2.1 Theory

In parallel with the discussion of a CRE, I will start with the FRT in an SRE. The sharp null hypothesis is still

$$
H _ {0 \mathrm {F}}: Y _ {i} (1) = Y _ {i} (0) \text {f o r a l l u n i t s} i = 1, \dots , n.
$$

The fundamental idea of the FRT applies to any randomized experiment: we can use any test statistic $T = T(\mathbf{Z}, \mathbf{Y}, \mathbf{X})$ , where $\mathbf{Z}, \mathbf{Y}$ and $\mathbf{X}$ are the treatment vector, observed outcome vector and the covariate matrix, respectively. Under the SRE and $H_{0\mathrm{F}}$ , the test statistic $T$ has a known distribution because $\mathbf{Z}$ has a known distribution under the SRE. However, we must be careful with two subtle issues. First, when we simulate the treatment vector, we must permute the treatment indicators within strata of $X$ according to Definition 5.1. The resulting FRT is sometimes called the conditional randomization test or conditional permutation test. Second, we should choose test statistics that can reflect the nature of the SRE. Below I give some canonical choices of the test statistic.

Example 5.1 (Stratified estimator) Motivated by estimating $\tau$ (see Chapter 5.3 below), we can use the following stratified estimator in the FRT:

$$
\hat {\tau} _ {\mathrm {S}} = \sum_ {k = 1} ^ {K} \pi_ {[ k ]} \hat {\tau} _ {[ k ]},
$$

where

$$
\hat {\tau} _ {[ k ]} = n _ {[ k ] 1} ^ {- 1} \sum_ {i = 1} ^ {n} I (X _ {i} = k, Z _ {i} = 1) Y _ {i} - n _ {[ k ] 0} ^ {- 1} \sum_ {i = 1} ^ {n} I (X _ {i} = k, Z _ {i} = 0) Y _ {i}
$$

is the stratum-specific difference-in-means within stratum $k$ .

Example 5.2 (Studentized stratified estimator) Motivated by the studentized statistic in the simple two-sample problem, we can use the following studentized statistic for the stratified estimator in the FRT:

$$
t _ {\mathrm {S}} = \frac {\hat {\tau} _ {\mathrm {S}}}{\sqrt {\hat {V} _ {\mathrm {S}}}},
$$

with

$$
\hat {V} _ {\mathrm {S}} = \sum_ {k = 1} ^ {K} \pi_ {[ k ]} ^ {2} \left(\frac {\hat {S} _ {[ k ]} ^ {2} (1)}{n _ {[ k ] 1}} + \frac {\hat {S} _ {[ k ]} ^ {2} (0)}{n _ {[ k ] 0}}\right)
$$

where $\hat{S}_{[k]}^2 (1)$ and $\hat{S}_{[k]}^2 (0)$ are the stratum-specific sample variances of the outcomes under the treatment and control, respectively. The exact form of this statistic is motivated by the Neymanian perspective discussed in Section 5.3 below.

Example 5.3 (Combining Wilcoxon rank-sum statistics) We first compute the Wilcoxon rank sum statistic $W_{[k]}$ within stratum $k$ (recall Example 3.3) and then combine them as

$$
W _ {\mathrm {S}} = \sum_ {k = 1} ^ {K} c _ {[ k ]} W _ {[ k ]}.
$$

Based on different asymptotic schemes and optimality criteria, Van Elteren (1960) proposed two weighting methods, one with

$$
c _ {[ k ]} = \frac {1}{n _ {[ k ] 1} n _ {[ k ] 0}},
$$

and the other with

$$
c _ {[ k ]} = \frac {1}{n _ {[ k ]} + 1}.
$$

The motivations for these weights are quite technical, and other choices of weights may also be reasonable.

Example 5.4 (Hodges and Lehmann (1962)'s aligned rank statistic) Van Elteren (1960)'s statistic works well with a few large strata. However, it does not work well with many small strata since it does not make enough comparisons, potentially losing information in the data. Hodges and Lehmann (1962) proposed a test statistic that makes more comparisons across strata after standardizing the outcomes. They suggested first centering the outcomes as

$$
\tilde {Y} _ {i} = Y _ {i} - \bar {Y} _ {[ k ]}
$$

with the stratum-specific mean $\bar{Y}_{[k]} = n_{[k]}^{-1}\sum_{X_i = k}Y_i$ if $X_{i} = k$ , then obtaining the ranks $(\tilde{R}_1,\dots ,\tilde{R}_n)$ of the pooled outcomes $(\tilde{Y}_1,\ldots ,\tilde{Y}_n)$ , and finally constructing the test statistic

$$
\tilde {W} = \sum_ {i = 1} ^ {n} Z _ {i} \tilde {R} _ {i}.
$$

We can simulate the exact distributions of the above test statistics under the SRE. We can also calculate their means and variances and obtain the $p$ -values based on Normal approximations.

After searching for a while, I failed to find a detailed discussion of the Kolmogorov-Smirnov statistic for the SRE. Below is my proposal.

Example 5.5 (Kolmogorov-Smirnov statistic) We compute $D_{[k]}$ , the maximum difference between the empirical distributions of the outcomes under treatment and control within stratum $k$ . The final test statistic can be

$$
D _ {\mathrm {S}} = \sum_ {k = 1} ^ {K} c _ {[ k ]} D _ {[ k ]}
$$

or

$$
D _ {\max} = \max _ {1 \leq k \leq K} c _ {[ k ]} D _ {[ k ]},
$$

where $c_{[k]} = \sqrt{n_{[k]1}n_{[k]0} / n_{[k]}}$ is motivated by the limiting distribution of $D_{[k]}$ with $n_{[k]1}$ and $n_{[k]0}$ approaching infinity (see Example 3.4). The statistics $D_{\mathrm{S}}$ and $D_{\mathrm{max}}$ are more appropriate when all strata have large sample sizes. Another reasonable choice is

$$
D = \max _ {y} \left| \sum_ {k = 1} ^ {K} \pi_ {[ k ]} \{\hat {F} _ {[ k ] 1} (y) - \hat {F} _ {[ k ] 0} (y) \} \right|,
$$

where $\hat{F}_{[k]1}(y)$ and $\hat{F}_{[k]0}(y)$ are the stratum-specific empirical distribution functions of the outcomes under the treatment and control, respectively. The statistic $D$ is appropriate in both the cases with large strata and the cases with many small strata.

# 5.2.2 An application

The Penn Bonus experiment is an example to illustrate the FRT in the SRE. The dataset used by Koenker and Xiao (2002) is from a job training program stratified on quarter, with the outcome being the duration before employment.

> penndata = read.table("Penn46.ascii.txt")   
> z = penndata\(treatment   
> y = log(penndata$duration)   
> block = penndata$quarter   
> table(penndata $treatment, penndata$ quarter)

<table><tr><td></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>0</td><td>234</td><td>41</td><td>687</td><td>794</td><td>738</td><td>860</td></tr><tr><td>1</td><td>87</td><td>48</td><td>757</td><td>866</td><td>811</td><td>461</td></tr></table>

I will focus on $\hat{\tau}_{\mathrm{S}}$ and $W_{\mathrm{S}}$ , and leave the FRT with other statistics as Problem 5.6. The following function computes $\hat{\tau}_{\mathrm{S}}$ and $W_{\mathrm{S}}$ :

stat_SRE $=$ function(z，y，x)   
{ xlevels $=$ unique(x) K = length(xlevels) PiK $=$ rep(0,K) TauK $=$ rep(0,K)

```r
WK = rep(0, K)
for(k in 1:K)
{
    xk = xlevels[k]
    zk = z[x == xk]
    yk = y[x == xk]
    PiK[k] = length(zk)/length(z)
    TauK[k] = mean(yk[zk==1]) - mean(yk[zk==0])
    WK[k] = wilcox.test(yk[zk==1], yk[zk==0]) $statistic
}
return(c(sum(PiK*TauK), sum(WK/PiK))) 
```

The following function generates a random treatment assignment in the SRE based on the observed data:

zRandomSRE $=$ function(z，x)   
{ xlevels $=$ unique(x) K $=$ length(xlevels) zrandom $=$ z for(k in 1:K) { $\mathrm{xk} =$ xlevels[k] zrandom[x == xk] $=$ sample(z[x == xk]) } return (zrandom)

Based on the above data and functions, we can simulate the randomization distributions of the test statistics and compute the $p$ -values.

```diff
> stat_obs = stat_SRE(z, y, block)  
> MC = 10^3  
> statSREMC = matrix(0, MC, 2)  
> for (mc in 1:MC)  
+ {  
+     zrandom     = zRandomSRE(z, block)  
+     statSREMC[mc, ] = stat_SRE(zrandom, y, block)  
+}  
> mean(statSREMC[, 1] <= stat_obs[1])  
[1] 0.002  
> mean(statSREMC[, 2] <= stat_obs[2])  
[1] 0.001 
```

In the above, I calculate the $p$ -values based on left-tail probabilities because the treatment has a negative effect on the outcome. See Figure 5.1 for more details about the observed test statistics and randomization distributions.

![](images/d711e82f8046abcf53500f9a89c9d8291dbf8bc86068871cdf812b3e866cb649.jpg)

![](images/543af2329890ad69dcc4b77a46cfb92ecc4b6240141de38287453d8e8e3b740a.jpg)  
FIGURE 5.1: The randomization distributions of $\hat{\tau}_{\mathrm{S}}$ and $W_{\mathrm{S}}$ based on the data from the Penn Bonus experiment, with $10^{4}$ Monte Carlo draws.

# 5.3 Neymanian inference

# 5.3.1 Point and interval estimation

Statistical inference for an SRE builds on the fact that it essentially consists of $K$ independent CREs. Based on this, we can extend Neyman (1923)'s results to the SRE. Within stratum $k$ , the difference-in-means $\hat{\tau}_{[k]}$ is unbiased for $\tau_{[k]}$ with variance

$$
\mathrm {v a r} (\hat {\tau} _ {[ k ]}) = \frac {S _ {[ k ]} ^ {2} (1)}{n _ {[ k ] 1}} + \frac {S _ {[ k ]} ^ {2} (0)}{n _ {[ k ] 0}} - \frac {S _ {[ k ]} ^ {2} (\tau)}{n _ {[ k ]}},
$$

where $S_{[k]}^2 (1), S_{[k]}^2 (0)$ and $S_{[k]}^2 (\tau)$ are the stratum-specific variances of potential outcomes and the individual causal effects, respectively. Therefore, the stratified estimator $\hat{\tau}_{\mathrm{S}} = \sum_{k = 1}^{K}\pi_{[k]}\hat{\tau}_{[k]}$ is unbiased for $\tau = \sum_{k = 1}^{K}\pi_{[k]}\tau_{[k]}$ with variance

$$
\mathrm {v a r} (\hat {\tau} _ {\mathrm {S}}) = \sum_ {k = 1} ^ {K} \pi_ {[ k ]} ^ {2} \mathrm {v a r} (\hat {\tau} _ {[ k ]}).
$$

If $n_{[k]1} \geq 2$ and $n_{[k]0} \geq 2$ , then we can obtain the sample variances $\hat{S}_{[k]}^2(1)$ and $\hat{S}_{[k]}^2(0)$ of the outcomes within stratum $k$ and construct a conservative variance estimator

$$
\hat {V} _ {\mathrm {S}} = \sum_ {k = 1} ^ {K} \pi_ {[ k ]} ^ {2} \left(\frac {\hat {S} _ {[ k ]} ^ {2} (1)}{n _ {[ k ] 1}} + \frac {\hat {S} _ {[ k ]} ^ {2} (0)}{n _ {[ k ] 0}}\right),
$$

where $\hat{S}_{[k]}^2 (1)$ and $\hat{S}_{[k]}^2 (0)$ are the stratum-specific sample variances of the outcomes under treatment and control, respectively. Based on a Normal approximation of $\hat{\tau}_{\mathrm{S}}$ , we can construct a Wald-type $1 - \alpha$ confidence interval for $\tau$ ..

$$
\hat {\tau} _ {\mathrm {S}} \pm z _ {1 - \alpha / 2} \sqrt {\hat {V} _ {\mathrm {S}}}.
$$

From a hypothesis testing perspective, under $H_{0\mathrm{N}}: \tau = 0$ , we can compare $t_{\mathrm{S}} = \hat{\tau}_{\mathrm{S}} / \sqrt{\hat{V}_{\mathrm{S}}}$ with the standard Normal quantiles to obtain asymptotic $p$ -values. The statistic $t_{\mathrm{S}}$ appears in Example 5.2 for the FRT. Chapter 8 later will show that using $t_{\mathrm{S}}$ in the FRT yields finite-sample exact $p$ -value under $H_{0\mathrm{F}}$ and asymptotically valid $p$ -value under $H_{0\mathrm{N}}$ .

Here I omit the technical details for the CLT of $\hat{\tau}_{\mathrm{S}}$ . See Liu and Yang (2020) for a proof, which includes the two regimes with a few large strata and many small strata. I will illustrate this theoretical issue using numerical examples in Chapter 5.3.2 below.

# 5.3.2 Numerical examples

The following function computes the Neymanian point and variance estimators under the SRE:

Neyman_SRE $=$ function(z，y，x)   
{ xlevels $=$ unique(x) K $=$ length(xlevels) PiK $=$ rep(0,K) TauK $=$ rep(0,K) varK $=$ rep(0,K) for(k in 1:K) { $\begin{array}{rl}{\mathrm{xk}}&{=}\end{array}$ xlevels[k] zk $=$ z[x == xk] yk $=$ y[x == xk] PiK[k] = length(zk)/length(z) TauK[k] $=$ mean(yk[zk==1]) - mean(yk[zk==0]) varK[k] $=$ var(yk[zk==1])/sum(zk)+ var(yk[zk==0])/sum(1-zk) } return(c(sum(PiK*TauK)，sum(PiK^2*varK)))

The first simulation setting has $K = 5$ and each stratum has 80 units. TauHat and VarHat are the point and variance estimators over $10^{4}$ simulations.

```diff
> K = 5  
> n = 80  
> n1 = 50  
> n0 = 30  
> x = rep(1:K, each = n)  
> y0 = rexp(n*K, rate = x)  
> y1 = y0 + 1  
> zb = c(rep(1, n1), rep(0, n0))  
> MC = 10^4  
> TauHat = rep(0, MC)  
> VarHat = rep(0, MC)  
> for (mc in 1:MC)  
+ {  
+ z = replicate(K, sample(zb))  
+ z = as.vector(z)  
+ y = z*y1 + (1-z)*y0  
+ est = Neyman_SRE(z, y, x)  
+ TauHat[mc] = est[1]  
+ VarHat[mc] = est[2]  
+ }  
> var(TauHat)  
[1] 0.002248925  
> mean(VarHat)  
[1] 0.002266396 
```

The upper panel of Figure 5.2 shows the histogram of the point estimator,

which is symmetric and bell-shaped around the true parameter. From the above, the average value of the variance estimator is almost identical to the variance of the estimators because the individual causal effects are constant.

The second simulation setting has $K = 50$ and each stratum has 8 units.

```diff
> K = 50  
> n = 8  
> n1 = 5  
> n0 = 3  
> x = rep(1:K, each = n)  
> y0 = rexp(n*K, rate = log(x + 1))  
> y1 = y0 + 1  
> zb = c(rep(1, n1), rep(0, n0))  
> MC = 10^4  
> TauHat = rep(0, MC)  
> VarHat = rep(0, MC)  
> for(mc in 1:MC)  
+ {  
+ z = replicate(K, sample(zb))  
+ z = as.vector(z)  
+ y = z*y1 + (1-z)*y0  
+ est = Neyman_SRE(z, y, x)  
+ TauHat[mc] = est[1]  
+ VarHat[mc] = est[2]  
+}  
>  
> hist(TauHat, xlab = expression(hat(tau)[S]),  
+ ylab = "", main = "many small strata",  
+ border = FALSE, col = "grey",  
+ breaks = 30, yaxt = 'n',  
+ xlim = c(0.8, 1.2))  
> abline(v = 1)  
>  
> var(TauHat)  
[1] 0.001443111  
> mean(VarHat)  
[1] 0.001473616 
```

The lower panel of Figure 5.2 shows the histogram of the point estimator, which is symmetric and bell-shaped around the true parameter. Again, the average value of the variance estimator is almost identical to the variance of the estimators because the individual causal effects are constant.

We finally use the Penn Bonus Experiment to illustrate the Neymanian inference in an SRE. Applying the function Neyman_SRE to the dataset, we obtain:

```txt
> penndata = read.table("Penn46ascii.txt")
> z = penndata$treatment
> y = log(penndata$duration)
> block = penndata$quarter 
```

![](images/27f2f39c85cb780517ecd7023dfbc1a530f8d07714f423bae6234370ff9979bc.jpg)

![](images/6176d13283325a13de034acf93180274750da61e31b1d6e67a2d38cb4e679513.jpg)  
FIGURE 5.2: Normal approximations under two regimes

```txt
> est = Neyman_SRE(z, y, block)  
> est[1]  
[1] -0.08990646  
> sqrt(est[2])  
[1] 0.03079775 
```

So the job training program significantly shortens the log of the duration time before employment.

# 5.3.3 Comparing the SRE and the CRE

What are the benefits of the SRE compared with the CRE? I have motivated the SRE from the covariate balance perspective. In addition, I will show that better covariate balance in turn results in better estimation precision of the average causal effect. To make a fair comparison, I assume that $e_{[k]} = e$ for all $k$ which ensures that the difference in means equals the stratified estimator:

$$
\hat {\tau} = \hat {\tau} _ {\mathrm {S}}. \tag {5.3}
$$

I leave the proof of (5.3) as Problem 5.2.

We now compare the sampling variances. The classic analysis of variance technique motivates the decomposition of the total variance into the summation of the within-strata and between-strata variances, yielding

$$
\begin{array}{l} S ^ {2} (1) = (n - 1) ^ {- 1} \sum_ {i = 1} ^ {n} \left\{Y _ {i} (1) - \bar {Y} (1) \right\} ^ {2} \\ = \left(n - 1\right) ^ {- 1} \sum_ {k = 1} ^ {K} \sum_ {X _ {i} = k} \left\{Y _ {i} (1) - \bar {Y} _ {[ k ]} (1) + \bar {Y} _ {[ k ]} (1) - \bar {Y} (1) \right\} ^ {2} \\ = (n - 1) ^ {- 1} \sum_ {k = 1} ^ {K} \sum_ {X _ {i} = k} \left[ \left\{Y _ {i} (1) - \bar {Y} _ {[ k ]} (1) \right\} ^ {2} + \left\{\bar {Y} _ {[ k ]} (1) - \bar {Y} (1) \right\} ^ {2} \right] \\ = \sum_ {k = 1} ^ {K} \left[ \frac {n _ {[ k ]} - 1}{n - 1} S _ {[ k ]} ^ {2} (1) + \frac {n _ {[ k ]}}{n - 1} \{\bar {Y} _ {[ k ]} (1) - \bar {Y} (1) \} ^ {2} \right], \\ \end{array}
$$

and similarly,

$$
S ^ {2} (0) = \sum_ {k = 1} ^ {K} \left[ \frac {n _ {[ k ]} - 1}{n - 1} S _ {[ k ]} ^ {2} (0) + \frac {n _ {[ k ]}}{n - 1} \{\bar {Y} _ {[ k ]} (0) - \bar {Y} (0) \} ^ {2} \right],
$$

$$
S ^ {2} (\tau) = \sum_ {k = 1} ^ {K} \left[ \frac {n _ {[ k ]} - 1}{n - 1} S _ {[ k ]} ^ {2} (\tau) + \frac {n _ {[ k ]}}{n - 1} \{\tau_ {[ k ]} - \tau \} ^ {2} \right].
$$

The variance of the difference-in-means estimator under the CRE decomposes

into

$$
\begin{array}{l} \operatorname {v a r} _ {\mathrm {C R E}} (\hat {\tau}) \\ = \frac {S ^ {2} (1)}{n _ {1}} + \frac {S ^ {2} (0)}{n _ {0}} - \frac {S ^ {2} (\tau)}{n} \\ { = } { \sum _ { k = 1 } ^ { K } \left[ \frac { n _ { [ k ] } - 1 } { ( n - 1 ) n _ { 1 } } S _ { [ k ] } ^ { 2 } ( 1 ) + \frac { n _ { [ k ] } - 1 } { ( n - 1 ) n _ { 0 } } S _ { [ k ] } ^ { 2 } ( 0 ) - \frac { n _ { [ k ] } - 1 } { ( n - 1 ) n } S _ { [ k ] } ^ { 2 } ( \tau ) \right] } \\ + \sum_ {k = 1} ^ {K} \left[ \frac {n _ {[ k ]} - 1}{(n - 1) n _ {1}} \{\bar {Y} _ {[ k ]} (1) - \bar {Y} (1) \} ^ {2} + \frac {n _ {[ k ]} - 1}{(n - 1) n _ {0}} \{\bar {Y} _ {[ k ]} (0) - \bar {Y} (0) \} ^ {2} \right. \\ \left. - \frac {n _ {[ k ]} - 1}{(n - 1) n} \{\tau_ {[ k ]} - \tau \} ^ {2} \right]. \\ \end{array}
$$

With large $n_{[k]}$ 's, it is approximately

$$
\begin{array}{l} \mathrm {v a r} _ {\mathrm {C R E}} (\hat {\tau}) \\ \approx \sum_ {k = 1} ^ {K} \left[ \frac {\pi_ {[ k ]}}{n _ {1}} S _ {[ k ]} ^ {2} (1) + \frac {\pi_ {[ k ]}}{n _ {0}} S _ {[ k ]} ^ {2} (0) - \frac {\pi_ {[ k ]}}{n} S _ {[ k ]} ^ {2} (\tau) \right] \\ + \sum_ {k = 1} ^ {K} \left[ \frac {\pi_ {[ k ]}}{n _ {1}} \{\bar {Y} _ {[ k ]} (1) - \bar {Y} (1) \} ^ {2} + \frac {\pi_ {[ k ]}}{n _ {0}} \{\bar {Y} _ {[ k ]} (0) - \bar {Y} (0) \} ^ {2} - \frac {\pi_ {[ k ]}}{n} \{\tau_ {[ k ]} - \tau \} ^ {2} \right]. \\ \end{array}
$$

The constant propensity scores assumption ensures

$$
\pi_ {[ k ]} / n _ {[ k ] 1} = 1 / (n e), \quad \pi_ {[ k ]} / n _ {[ k ] 0} = 1 / \{n (1 - e) \}, \quad \pi_ {[ k ]} / n _ {[ k ]} = 1 / n,
$$

which allow us to rewrite the variance of $\hat{\tau}_{\mathrm{S}}$ under the SRE as

$$
\begin{array}{l} \mathrm {v a r} _ {\mathrm {S R E}} (\hat {\tau} _ {\mathrm {S}}) = \sum_ {k = 1} ^ {K} \pi_ {[ k ]} ^ {2} \left[ \frac {S _ {[ k ]} ^ {2} (1)}{n _ {[ k ] 1}} + \frac {S _ {[ k ]} ^ {2} (0)}{n _ {[ k ] 0}} - \frac {S _ {[ k ]} ^ {2} (\tau)}{n _ {[ k ]}} \right] \\ = \sum_ {k = 1} ^ {K} \left[ \frac {\pi_ {[ k ]}}{n _ {1}} S _ {[ k ]} ^ {2} (1) + \frac {\pi_ {[ k ]}}{n _ {0}} S _ {[ k ]} ^ {2} (0) - \frac {\pi_ {[ k ]}}{n} S _ {[ k ]} ^ {2} (\tau) \right]. \\ \end{array}
$$

With large $n_{[k]}$ 's, approximately, the difference between $\mathrm{var}_{\mathrm{CRE}}(\hat{\tau})$ and $\mathrm{var}_{\mathrm{SRE}}(\hat{\tau}_{\mathrm{S}})$ is

$$
\sum_ {k = 1} ^ {K} \left[ \frac {\pi_ {[ k ]}}{n _ {1}} \{\bar {Y} _ {[ k ]} (1) - \bar {Y} (1) \} ^ {2} + \frac {\pi_ {[ k ]}}{n _ {0}} \{\bar {Y} _ {[ k ]} (0) - \bar {Y} (0) \} ^ {2} - \frac {\pi_ {[ k ]}}{n} (\tau_ {[ k ]} - \tau) ^ {2} \right]
$$

which is nonnegative because it equals (see Problem 5.4)

$$
\sum_ {k = 1} ^ {K} \frac {\pi_ {[ k ]}}{n} \left\{\sqrt {\frac {n _ {0}}{n _ {1}}} \left\{\bar {Y} _ {[ k ]} (1) - \bar {Y} (1) \right\} + \sqrt {\frac {n _ {1}}{n _ {0}}} \left\{\bar {Y} _ {[ k ]} (0) - \bar {Y} (0) \right\} \right\} ^ {2} \geq 0, \tag {5.4}
$$

The difference in (5.4) is zero only in the extreme case that

$$
\sqrt {\frac {n _ {0}}{n _ {1}}} \{\bar {Y} _ {[ k ]} (1) - \bar {Y} (1) \} + \sqrt {\frac {n _ {1}}{n _ {0}}} \{\bar {Y} _ {[ k ]} (0) - \bar {Y} (0) \} = 0
$$

for $k = 1, \ldots, K$ . When the covariate is predictive of the potential outcomes, the above quantities are usually not all zeros, which ensures the efficiency gain of the SRE compared with the CRE. Only in the extreme cases that the covariate is not predictive at all, the large-sample efficiency gain is zero. In those cases, the SRE can even result in less efficient estimators in finite samples. The above discussion corroborates the quote from George Box at the beginning of this chapter.

I will end this section with several remarks. First, the above comparison is based on the sampling variance, and we can also compare the estimated variances under the SRE and the CRE. The results are similar. Second, increasing $K$ improves efficiency, but this argument depends on the large strata assumption. So we face a trade-off in practice. We cannot arbitrarily increase $K$ , and the most extreme case is $n_{[k]1} = n_{[k]0} = 1$ , which is called the matched-pairs experiment and will be discussed in Chapter 7.

# 5.4 Post-stratification in a CRE

In a CRE with a discrete covariate $X$ , the numbers of units receiving the treatment and control are random within stratum $k$ . In a SRE, these numbers are fixed. But if we conduct conditional inference given $\pmb{n} = \{n_{[k]1}, n_{[k]0}\}_{k=1}^{K}$ , then a CRE becomes a SRE. Mathematically, if none of the components of $\pmb{n}$ are zero, then

$$
\Pr_ {\mathrm {C R E}} (\boldsymbol {Z} = \boldsymbol {z} \mid \boldsymbol {n}) = \frac {\Pr_ {\mathrm {C R E}} (\boldsymbol {Z} = \boldsymbol {z} , \boldsymbol {n})}{\Pr_ {\mathrm {C R E}} (\boldsymbol {n})} = \frac {1}{\prod_ {k = 1} ^ {K} \binom {n _ {[ k ]}} {n _ {[ k ] 1}}}, \tag {5.5}
$$

that is, the conditional distribution of $Z$ from a CRE given $n$ is identical to the distribution of $Z$ from an SRE. I leave the proof of (5.5) as Problem 5.5. So conditional on $n$ , we can analyze a CRE with a discrete covariate $X$ in the same way as in a SRE. In particular, the FRT becomes a conditional FRT, and the Neymanian analysis becomes post-stratification:

$$
\hat {\tau} _ {\mathrm {P S}} = \sum_ {k = 1} ^ {K} \pi_ {[ k ]} \hat {\tau} _ {[ k ]},
$$

which has an identical form as $\hat{\tau}_{\mathrm{S}}$ . The variance of $\hat{\tau}_{\mathrm{PS}}$ conditioning on $\pmb{n}$ is identical to the variance of $\hat{\tau}_{\mathrm{S}}$ under the SRE.

Hennessy et al. (2016) used simulation to show that the conditional FRT is often more powerful than the unconditional one. Miratrix et al. (2013) used theory to show that in many cases, post-stratification improves efficiency compared with $\hat{\tau}$ . Both results hold if $X$ is predictive of the outcome. However, the simulation is based on a limited number of data-generating processes, and the theory assumes all strata are large enough. We can not go too extreme in the conditional FRT or post-stratification because with a larger $K$ it is more likely that some $n_{[k]1}$ or $n_{[k]0}$ become zero. Small or zero values of $n_{[k]1}$ or $n_{[k]0}$ greatly reduce the number of randomizations in the FRT, possibly reducing the power dramatically. The problem for the Neymanian counterpart is more salient because we cannot even define $\hat{\tau}_{\mathrm{PS}}$ and the corresponding variance estimator.

Stratification uses $X$ in the design stage and post-stratification uses $X$ in the analysis stage. They are duals for using $X$ . Asymptotically, their difference is small with large strata (Miratrix et al., 2013).

# 5.4.1 Meinert et al. (1970)'s Example

We use the data from a CRE reported in Meinert et al. (1970), which were also used by Rothman et al. (2008). The treatment is tolbutamide and the control is a placebo.

<table><tr><td colspan="3">Age &lt; 55</td><td colspan="3">Age ≥ 55</td></tr><tr><td></td><td>Surviving</td><td>Dead</td><td colspan="2">Surviving</td><td>Dead</td></tr><tr><td>Z = 1</td><td>98</td><td>8</td><td>Z = 1</td><td>76</td><td>22</td></tr><tr><td>Z = 0</td><td>115</td><td>5</td><td>Z = 0</td><td>69</td><td>16</td></tr><tr><td colspan="6">Total</td></tr><tr><td></td><td></td><td>Surviving</td><td>Dead</td><td></td><td></td></tr><tr><td>Z = 1</td><td></td><td>174</td><td>30</td><td></td><td></td></tr><tr><td>Z = 0</td><td></td><td>184</td><td>21</td><td></td><td></td></tr></table>

The following table shows the estimates for two strata separately, the poststratified estimator, and the crude estimator ignoring the binary covariate, as well as the corresponding standard errors.

<table><tr><td></td><td>stratum 1</td><td>stratum 2</td><td>post-stratification</td><td>crude</td></tr><tr><td>est</td><td>-0.034</td><td>-0.036</td><td>-0.035</td><td>-0.045</td></tr><tr><td>se</td><td>0.031</td><td>0.060</td><td>0.032</td><td>0.033</td></tr></table>

The crude estimator and the post-stratification estimator do not lead to fundamentally different results. However, the crude estimator is larger than both of the stratum-specific estimators, whereas the post-stratification estimator is within the range.

# 5.4.2 Chong et al. (2016)'s Example

Chong et al. (2016) conducted an SRE on 219 students of a rural secondary

school in the Cajamarca district of Peru during the 2009 school year. They first provided the village clinic with iron supplements and trained the local staff to distribute one free iron pill to any adolescent who requested one in person. They then randomly assigned students to three arms with three different types of videos: in the first video, a popular soccer player was encouraging the use of iron supplements to maximize energy ("soccer" arm); in the second video, a physician was encouraging the use of iron supplements to improve overall health ("physician" arm); the third video did not mention iron at all ("control" arm). The experiment was stratified on the class level (1-5). The treatment and control group sizes within classes are shown below:

```txt
> library("foreign")
> dat_chong = read.dta("chong.dta")
> table (dat_chong$treatment, dat_chong-class_level) 
```

```txt
1 2 3 4 5  
Soccer Player 16 19 15 10 10  
Physician 17 20 15 11 10  
Placebo 15 19 16 12 10 
```

One outcome of interest is the average grades in the third and fourth quarters of 2009, and an important background covariate was the anemia status at baseline. I will only use a subset of the original data in this chapter.

```txt
>use vars \(=\) c("treatment", + "gradesq34", + "class_level", + "anemic_base_re") >dat_physician \(=\) subset旻echong, treatment \(! =\) "Soccer Player", + select \(=\) use.vars) >dat_physician\\(z \(=\) (dat_physician\\)treatment \(= =\) "Physician") >dat_physician\\)y \(=\) dat_physician\\(gradesq34 >table旻echician\\)z, +dat_physician\\(class_level) 12345 FALSE 15 19 16 12 10 TRUE 17 20 15 11 10 >table旻echician\\)z, +dat_physician\\(class_level, +dat_physician\\)anemic_base_re) ,, \(=\) No 12345 FALSE 6 14 12 7 4 TRUE 8 12 9 5 6 
```

```txt
1 2 3 4 5  
FALSE 9 5 4 5 6  
TRUE 9 8 6 6 4 
```

We can use the Neyman_SRE function defined before to compute the stratified estimator and its estimated variance.

```txt
tauS = with(mat_physician, Neyman_SRE(z, gradesq34, class_level)) 
```

An important additional covariate is the baseline anemic indicator which is quite important for predicting the outcome. Further conditioning the baseline anemic indicator, we have an experiment with $5 \times 2 = 10$ strata, with the treatment and control group sizes shown above. Again we can use the Neyman_SRE function defined before to compute the post-stratified estimator and its estimated variance.

```diff
> tauSPS = with/dat_physician, {
+     sps = interaction(class_level, anemic_base_re)
+     Neyman_SRE(z, gradesq34, sps)
+ }) 
```

The following table compares these two estimators. The post-stratified estimator yields a much smaller $p$ -value.

```txt
est se t Stat p.value stratify 0.406 0.202 2.005 0.045 stratify and post-stratify 0.463 0.190 2.434 0.015 
```

This example illustrates that post-stratification can be used not only in the CRE but also in the SRE with additional discrete covariates.

# 5.5 Practical questions

How do we choose $X$ to construct an SRE? Theoretically, $X$ should be predictive of the potential outcomes. In some cases, the experimenter has enough background knowledge about the predictive covariates based on, for example, some pilot studies. Then the choice of $X$ should be straightforward. In some other cases, this background knowledge may not be clear enough. Experimenters instead choose $X$ based on logistical convenience, for example, $X$ can be the indicator for the study areas or the cohort of students.

The choice of $K$ is a related problem. Theoretically, more stratification increases the estimation efficiency if all strata are large enough. However, extremely large $K$ may even decrease the estimation efficiency. In simulation

studies, we observe diminishing marginal returns of increasing $K$ . Anecdotally, $K = 5$ often suffices for efficiency gain (the magic number 5 will appear again in Chapter 11). Some experimenter prefers the most extreme version of the SRE with $K = n / 2$ . This results in the matched-pairs experiment, which will be discussed in Chapter 7 later.

Some experiments have multidimensional continuous covariates. Can the SRE still be used? If we have a pilot study, we can build a model for the potential outcome $Y(0)$ given those covariates, and then we can choose $X$ as a discretized version of the predictor $\hat{Y}(0)$ . In general, if we do not have such a pilot study or we do not want to make ad hoc discretizations, we can use a more general strategy called rerandomization, which will be the topic for Chapter 6.

# 5.6 Homework Problems

# 5.1 Covariate balance in the CRE

Under the CRE, prove (5.2).

# 5.2 Consequence of the constant propensity score

Prove (5.3).

# 5.3 Consequence of constant individual causal effects

Assume that the individual causal effects are constant $\tau_{i} = \tau$ for all $i = 1, \ldots, n$ . Consider the following class of weighted estimator for $\tau$ :

$$
\hat {\tau} _ {w} = \sum_ {k = 1} ^ {K} w _ {[ k ]} \hat {\tau} _ {[ k ]},
$$

where the weights $w_{[k]}$ 's are non-negative for all $k$ .

Find the condition on the $w_{[k]}$ 's such that $\hat{\tau}_w$ is unbiased for $\tau$ . Among all unbiased estimators, find the weights that give the $\hat{\tau}_w$ with the minimum variance.

# 5.4 Compare the CRE and SRE

Prove (5.4).

# 5.5 From the CRE to the SRE

Prove (5.5).

# 5.6 More FRTs for Section 5.2.2

Extend the analysis in Section 5.2.2 using FRTs with other test statistics.

# 5.7 FRT for an SRE in Imbens and Rubin (2015)

Imbens and Rubin (2015) discussed an SRE from the Student/Teacher Achievement Ratio experiment conducted in 1985-1986 in Tennessee. The kindergarten data are below:

treatment $=$ list(c(1,1,0,0), c(1,1,0,0), c(1,1,1,0,0), c(1,1,0,0), c(1,1,0,0), c(1,1,0,0), c(1,1,0,0), c(1,1,1,1,0,0), c(1,1,0,0), c(1,1,0,0), c(1,1,0,0), c(1,1,0,0), c(1,1,1,0,0), c(1,1,0,0), c(1,1,0,0), c(1,1,0,0), c(1,1,0,0), c(1,1,0,0), c(1,1,0,0))   
outcome $=$ listc(0.165,0.321,-0.197,0.236), c(0.918,-0.202，1.19，0.117)， c(0.341，0.561，-0.059，-0.496，0.225）， c(-0.024，-0.450，-1.104，-0.956)， c(-0.258，-0.083，-0.126，0.106)， c(1.151，0.707，0.597，-0.495)， c(0.077，0.371，0.685，0.270)， c(-0.870，-0.496，-0.444，0.392，-0.934，-0.633)， c(-0.568，-1.189，-0.891，-0.856)， c(-0.727，-0.580，-0.473，-0.807)， c(-0.533，0.458，-0.383，0.313)， c(1.001，0.102，0.484，0.474，0.14O)， c(0.855，0.509，0.205，0.296)， c(0.618，0.978，0.742，0.175)， c(-0.545，0.234，-0.434，-0.293）， c(-0.24O，-o.15O，o.355，-o.13O))

The strata correspond to schools, and the unit of analysis is the teacher or class. The treatment equals 1 for small classes (13-17 students per teacher) and 0 for regular classes (22-25 students per teacher). The outcome is the standardized average mathematics score.

Reanalyze the Project STAR data below using the FRT. Use $\hat{\tau}_{\mathrm{S}}$ , $W_{\mathrm{S}}$ and $\tilde{W}$ in the FRT. Compare the $p$ -values.

Remark: This book uses $Z$ for the treatment indicator but Imbens and Rubin (2015) use $W$ .

# 5.8 A multi-center trial

Gould (1998, Table 1) reported the following data from a multi-center trial:

<table><tr><td colspan="11">&gt; multicenter = read.csv(&quot;multicenter.csv&quot;)</td></tr><tr><td colspan="11">&gt; multicenter</td></tr><tr><td></td><td>center</td><td>n0</td><td>mean0</td><td>sd0</td><td>n1</td><td>mean1</td><td>sd1</td><td>n5</td><td>mean5</td><td>sd5</td></tr><tr><td>1</td><td>1</td><td>7</td><td>0.43</td><td>4.58</td><td>7</td><td>-5.43</td><td>5.53</td><td>8</td><td>-2.63</td><td>3.38</td></tr><tr><td>2</td><td>2</td><td>11</td><td>0.10</td><td>4.21</td><td>11</td><td>-2.59</td><td>3.95</td><td>12</td><td>-2.21</td><td>4.14</td></tr><tr><td>3</td><td>3</td><td>6</td><td>2.58</td><td>4.80</td><td>6</td><td>-3.94</td><td>4.25</td><td>7</td><td>1.29</td><td>7.39</td></tr><tr><td>4</td><td>4</td><td>10</td><td>-2.30</td><td>3.86</td><td>10</td><td>-1.23</td><td>5.17</td><td>10</td><td>-1.40</td><td>2.27</td></tr><tr><td>5</td><td>5</td><td>10</td><td>2.08</td><td>6.46</td><td>10</td><td>-6.70</td><td>7.45</td><td>10</td><td>-5.13</td><td>3.91</td></tr><tr><td>6</td><td>6</td><td>6</td><td>1.13</td><td>3.24</td><td>5</td><td>3.40</td><td>8.17</td><td>5</td><td>-1.59</td><td>3.19</td></tr><tr><td>7</td><td>7</td><td>5</td><td>1.20</td><td>7.85</td><td>6</td><td>-3.67</td><td>4.89</td><td>5</td><td>-1.40</td><td>2.61</td></tr><tr><td>8</td><td>8</td><td>12</td><td>-1.21</td><td>2.66</td><td>13</td><td>0.18</td><td>3.81</td><td>12</td><td>-4.08</td><td>6.32</td></tr><tr><td>9</td><td>9</td><td>8</td><td>1.13</td><td>5.28</td><td>8</td><td>-2.19</td><td>5.17</td><td>9</td><td>-1.96</td><td>5.84</td></tr><tr><td>10</td><td>10</td><td>9</td><td>-0.11</td><td>3.62</td><td>10</td><td>-2.00</td><td>5.35</td><td>10</td><td>0.60</td><td>3.53</td></tr><tr><td>11</td><td>11</td><td>15</td><td>-4.37</td><td>6.12</td><td>14</td><td>-2.68</td><td>5.34</td><td>15</td><td>-2.14</td><td>4.27</td></tr><tr><td>12</td><td>12</td><td>8</td><td>-1.06</td><td>5.27</td><td>9</td><td>0.44</td><td>4.39</td><td>9</td><td>-2.03</td><td>5.76</td></tr><tr><td>13</td><td>13</td><td>12</td><td>-0.08</td><td>3.32</td><td>12</td><td>-4.60</td><td>6.16</td><td>11</td><td>-6.22</td><td>5.33</td></tr><tr><td>14</td><td>14</td><td>9</td><td>0.00</td><td>5.20</td><td>9</td><td>-0.25</td><td>8.23</td><td>7</td><td>-3.29</td><td>5.12</td></tr><tr><td>15</td><td>15</td><td>6</td><td>1.83</td><td>5.85</td><td>7</td><td>-1.23</td><td>4.33</td><td>6</td><td>-1.00</td><td>2.61</td></tr><tr><td>16</td><td>16</td><td>14</td><td>-4.21</td><td>7.53</td><td>14</td><td>-2.10</td><td>5.78</td><td>12</td><td>-5.75</td><td>5.63</td></tr><tr><td>17</td><td>17</td><td>13</td><td>0.76</td><td>3.82</td><td>13</td><td>0.55</td><td>2.53</td><td>13</td><td>-0.63</td><td>5.41</td></tr><tr><td>18</td><td>18</td><td>15</td><td>-1.05</td><td>4.54</td><td>13</td><td>2.54</td><td>4.16</td><td>14</td><td>-2.80</td><td>2.89</td></tr><tr><td>19</td><td>19</td><td>15</td><td>2.07</td><td>4.88</td><td>15</td><td>-1.67</td><td>4.95</td><td>15</td><td>-3.43</td><td>4.71</td></tr><tr><td>20</td><td>20</td><td>11</td><td>-1.46</td><td>5.48</td><td>10</td><td>-1.99</td><td>5.63</td><td>10</td><td>-6.77</td><td>5.19</td></tr><tr><td>21</td><td>21</td><td>5</td><td>0.80</td><td>4.21</td><td>5</td><td>-3.35</td><td>4.73</td><td>5</td><td>-0.23</td><td>4.14</td></tr><tr><td>22</td><td>22</td><td>11</td><td>-2.92</td><td>5.42</td><td>10</td><td>-1.22</td><td>5.95</td><td>11</td><td>-4.45</td><td>6.65</td></tr><tr><td>23</td><td>23</td><td>9</td><td>-3.37</td><td>4.73</td><td>9</td><td>-1.38</td><td>4.17</td><td>7</td><td>0.57</td><td>2.70</td></tr><tr><td>24</td><td>24</td><td>12</td><td>-1.92</td><td>2.91</td><td>12</td><td>-0.66</td><td>3.55</td><td>12</td><td>-2.39</td><td>2.27</td></tr><tr><td>25</td><td>25</td><td>9</td><td>-3.89</td><td>4.76</td><td>9</td><td>-3.22</td><td>5.54</td><td>8</td><td>-1.23</td><td>4.91</td></tr><tr><td>26</td><td>26</td><td>15</td><td>-3.48</td><td>5.98</td><td>15</td><td>-2.13</td><td>3.25</td><td>14</td><td>-3.71</td><td>5.30</td></tr><tr><td>27</td><td>27</td><td>11</td><td>-1.91</td><td>6.49</td><td>12</td><td>-1.33</td><td>4.40</td><td>11</td><td>-1.52</td><td>4.68</td></tr><tr><td>28</td><td>28</td><td>10</td><td>-2.66</td><td>3.80</td><td>10</td><td>-1.29</td><td>3.18</td><td>10</td><td>-4.70</td><td>3.43</td></tr><tr><td>29</td><td>29</td><td>13</td><td>-0.77</td><td>4.73</td><td>13</td><td>-2.31</td><td>3.88</td><td>13</td><td>-0.47</td><td>4.95</td></tr></table>

This is a SRE with centers being the strata. The trial was conducted to study the efficacy and tolerability of finasteride, a drug for treating benign prostatic hyperplasia. Within each of the 29 centers, patients were randomized into three arms: control, finasteride $1\mathrm{mg}$ , and finasteride $5\mathrm{mg}$ . The above dataset provides summary statistics for the outcome, which is the change from baseline in total symptom score. The total symptom score is the sum of the responses to nine questions (score 0 to 4) about symptoms of various aspects of impaired urinary ability. The meanings of the columns are:

1. center: ID of the centers;

2. n0, n1, n5: sample sizes under the three arms;   
3. mean0, mean1, mean5: means of the outcomes under the three arms;   
4. sd0, sd1, sd5: standard deviations of the outcomes under the three arms.

The individual-level outcomes are not reported so we cannot implement the FRT. However, the Neymanian inference only requires the summary statistics. Report the point estimators and variance estimators for comparing "finasteride $1\mathrm{mg}$ " and "finasteride $5\mathrm{mg}$ " to "control", separately.

# 5.9 Data re-analyses

Re-analyze the LaLonde data used in Chapter 4.5.3. Conduct both Fisherian and Neymanian inferences.

The original experiment is a CRE. Now we pretend that the original experiment is an SRE. First, re-analyze the data pretending that the experiment is stratified on the race (black, Hispanic, or other). Second, re-analyze the data pretending that the experiment is stratified on marital status. Third, re-analyze the data pretending that the experiment is stratified on the indicator of a high school diploma.

Compare with the results obtained under a CRE.

# 5.10 Recommended reading

Miratrix et al. (2013) provided a solid theory for post-stratification and compared it with stratification. A main theoretical result is that their difference is small asymptotically although they can differ in finite samples.

# 6

# Rerandomization and Regression Adjustment

Stratification and post-stratification in Chapter 5 are duals for discrete covariates in the design and analysis of randomized experiments. How should we deal with multidimensional, possibly continuous, covariates? We can discretize continuous covariates, but this is not an ideal strategy with many covariates. Rerandomization and regression adjustment are duals for general covariates, which are the topics for this chapter.

The following table summarizes the topics of Chapters 5 and 6:

<table><tr><td></td><td>design</td><td>analysis</td></tr><tr><td>discrete covariate</td><td>stratification</td><td>post-stratification</td></tr><tr><td>general covariate</td><td>rerandomization</td><td>regression adjustment</td></tr></table>

# 6.1 Rerandomization

# 6.1.1 Experimental design

Again we consider a finite population of $n$ experimental units, where $n_1$ of them receive the treatment and $n_0$ of them receive the control. Let $Z = (Z_{1},\ldots ,Z_{n})$ be the treatment vector for these units. Unit $i$ has covariate $X_{i}\in \mathbb{R}^{K}$ which can have continuous or binary components. Concatenate them as an $n\times K$ covariate matrix $\pmb {X} = (X_{1},\dots,X_{n})^{\mathrm{T}}$ and center them at mean zero $\bar{X} = n^{-1}\sum_{i = 1}^{n}X_{i} = 0$ to simplify the presentation.

The CRE balances the covariates in the treatment and control groups on average, for instance, the difference in means of the covariates

$$
\hat {\tau} _ {X} = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} X _ {i} - n _ {0} ^ {- 1} \sum_ {i = 1} ^ {n} (1 - Z _ {i}) X _ {i}
$$

has mean zero under the CRE. However, it can result in undesired covariate balance across the treatment and control groups in the realized treatment allocation, that is, the realized value of $\hat{\tau}_X$ is often not zero. Using the vector form of Neyman (1923) in Problem 4.6 before, we can show that

$$
\operatorname {c o v} (\hat {\tau} _ {X}) = \frac {1}{n _ {1}} S _ {X} ^ {2} + \frac {1}{n _ {0}} S _ {X} ^ {2} = \frac {n}{n _ {1} n _ {0}} S _ {X} ^ {2},
$$

where $S_X^2 = (n - 1)^{-1}\sum_{i = 1}^n X_iX_i^\top$ is the finite-population covariance matrix of the covariates. The following Mahalanobis distance measures the difference between the treatment and control groups:

$$
M = \hat {\tau} _ {X} ^ {\mathsf {T}} \operatorname {c o v} (\hat {\tau} _ {X}) ^ {- 1} \hat {\tau} _ {X} = \hat {\tau} _ {X} ^ {\mathsf {T}} \left(\frac {n}{n _ {1} n _ {0}} S _ {X} ^ {2}\right) ^ {- 1} \hat {\tau} _ {X}. \tag {6.1}
$$

Technically, the above formula for $M$ in (6.1) is meaningful only if $S_X^2$ is invertible, which means that the columns of the covariate matrix $X$ are linearly independent. If a column can be represented by a linear combination of other columns, it is redundant and should be dropped before the experiment. A nice feature of $M$ is that it is invariant under non-degenerate linear transformations of $X$ . Lemma 6.1 below summarizes the result with the proof relegated to Problem 6.2.

Lemma 6.1 M in (6.1) remains the same if we transform $X_{i}$ to $b_{0} + BX_{i}$ for all units $i = 1, \ldots, n$ where $b_{0} \in \mathbb{R}^{K}$ and $B \in \mathbb{R}^{K \times K}$ is invertible.

The finite population CLT (Li and Ding, 2017) ensures that with large $n$ , the Mahalanobis distance $M$ is approximately $\chi_K^2$ under the CRE. Therefore, it is likely that $M$ has a large realized value under the CRE with asymptotic mean $K$ and variance $2K$ . Rerandomization avoids covariate imbalance by discarding the treatment allocations with large values of $M$ . Below I give a formal definition of the rerandomization using the Mahalanobis distance (ReM), which was proposed by Cox (1982) and further studied by Morgan and Rubin (2012).

Definition 6.1 (ReM) Draw $Z$ from CRE and accept it if and only if

$$
M \leq a,
$$

for some predetermined constant $a > 0$ .

The problem of choosing $a$ is similar to the problem of choosing the number of strata in the SRE, which is non-trivial in practice. At one extreme, $a = \infty$ , we just conduct the CRE. At the other extreme, $a = 0$ , there are very few feasible treatment allocations, and consequently, the experiment has little randomness, rendering randomization-based inference useless. As a compromise, we choose a small but not extremely small $a$ , for example, $a = 0.001$ or some upper quantile of a $\chi_K^2$ distribution.

ReM has many desirable properties. As mentioned above, it is invariant to linear transformations of the covariates. Moreover, it has nice geometric properties and elegant mathematical theory. This chapter will focus on ReM.

# 6.1.2 Statistical inference

An important question is how to analyze the data under ReM. Bruhn and McKenzie (2009) and Morgan and Rubin (2012) argued that we can always

use the FRT as long as we simulate $\mathbf{Z}$ under the constraint $M \leq a$ . This always yields finite-sample exact $p$ -values under the sharp null hypothesis. See Problem 6.1.

It is a challenging problem to derive the finite sample properties of ReM without assuming the sharp null hypothesis. Instead, Li et al. (2018b) derived the asymptotic distribution of the difference in means of the outcome $\hat{\tau}$ under ReM and the regularity conditions below.

Condition 6.1 As $n\to \infty$

1. $n_1 / n$ and $n_0 / n$ have positive limits;   
2. the finite population covariance of $\{X_i, Y_i(1), Y_i(0), \tau_i\}$ has a finite limit;   
3. $\max_{1\leq i\leq n}\{Y_i(1) - \bar{Y} (1)\} ^2 /n\to 0,\max_{1\leq i\leq n}\{Y_i(0) - \bar{Y} (0)\} ^2 /n\to$ $0$ , and $\max_{1\leq i\leq n}X_i^{\mathsf{T}}X_i / n\to 0$

Below is the main theorem for ReM, which relies on additional notation. Let

$$
L _ {K, a} \sim D _ {1} \mid \boldsymbol {D} ^ {\intercal} \boldsymbol {D} \leq a
$$

where $\pmb{D} = (D_{1},\dots ,D_{K})$ follows a $K$ -dimensional standard Normal distribution; let $\varepsilon$ follow a univariate standard Normal distribution; $L_{K,a}\bot \varepsilon$

Theorem 6.1 Under $ReM$ with $M \leq a$ and Condition 6.1, we have

$$
\hat {\tau} - \tau \stackrel {.} {\sim} \sqrt {\mathrm {v a r} (\hat {\tau})} \left\{\sqrt {R ^ {2}} L _ {K, a} + \sqrt {1 - R ^ {2}} \varepsilon \right\},
$$

where

$$
\operatorname {v a r} (\hat {\tau}) = \frac {S ^ {2} (1)}{n _ {1}} + \frac {S ^ {2} (0)}{n _ {0}} - \frac {S ^ {2} (\tau)}{n}
$$

is Neyman (1923)'s variance formula proved in Chapter 4, and

$$
R ^ {2} = \mathrm {c o r r} ^ {2} (\hat {\tau}, \hat {\tau} _ {X})
$$

is the squared multiple correlation coefficient (see Section A.1.1 for the definition) between $\hat{\tau}$ and $\hat{\tau}_X$ under the CRE.

Although the proof of Li et al. (2018b) is technical, the asymptotic distribution in Theorem 6.1 has a clear geometric interpretation, as shown in Figure 6.1. It shows that $\hat{\tau}$ decomposes into a component that is a linear combination of $\hat{\tau}_X$ and a component that is orthogonal to $\hat{\tau}_X$ . Geometrically, $\cos^2\theta = R^2$ , where $\theta$ is the angle between $\hat{\tau}$ and $\hat{\tau}_X$ . ReM affects the first component but does not change the second component. The truncated Normal distribution $L_{K,a}$ is due to the restriction of ReM on the first component.

![](images/e8e25992f074f110a78bfa9648dd952e25c7f7c56cfa52ff43b4a5d13a452389.jpg)  
FIGURE 6.1: Geometry of the asymptotic distribution of $\hat{\tau}$ under ReM

When $a = \infty$ , the asymptotic distribution simplifies to the one under the CRE:

$$
\hat {\tau} - \tau \dot {\sim} \sqrt {\operatorname {v a r} (\hat {\tau})} \varepsilon .
$$

When the threshold $a$ is close to zero, the asymptotic distribution simplifies to

$$
\hat {\tau} - \tau \stackrel {.} {\sim} \sqrt {\operatorname {v a r} (\hat {\tau}) (1 - R ^ {2})} \varepsilon ;
$$

see Wang and Li (2022) for a rigorous proof. So with a small threshold $a$ , the efficiency gain due to ReM depends on $R^2$ , which has the following equivalent form.

Proposition 6.1 Under the CRE, we have

$$
R ^ {2} = \mathrm {c o r r} ^ {2} (\hat {\tau}, \hat {\tau} _ {X}) = \frac {n _ {1} ^ {- 1} S ^ {2} (1 \mid X) + n _ {0} ^ {- 1} S ^ {2} (0 \mid X) - n ^ {- 1} S ^ {2} (\tau \mid X)}{n _ {1} ^ {- 1} S ^ {2} (1) + n _ {0} ^ {- 1} S ^ {2} (0) - n ^ {- 1} S ^ {2} (\tau)},
$$

where $\{S^2(1), S^2(0), S^2(\tau)\}$ are the finite population variances of $\{Y_i(1), Y_i(0), \tau_i\}_{i=1}^n$ , and $\{S^2(1 \mid x), S^2(0 \mid x), S^2(\tau \mid x)\}$ are the corresponding finite population variances of their linear projections on $(1, X_i)$ ; see Section B.2 for the definition of linear projections. Under the constant causal effect assumption with $\tau_i = \tau$ , the $R^2$ reduces to $S^2(0 \mid X)/S^2(0)$ , the finite population squared multiple correlation between $Y_i(0)$ and $X_i$ .

I leave the proof of Proposition 6.1 to Problem 6.4.

When $0 < a < \infty$ , the asymptotic distribution of $\hat{\tau}$ has a more complicated form and is more concentrated at $\tau$ and thus the difference in means $\hat{\tau}$ is more precise under ReM than under the CRE.

If we ignore the design of ReM and still use the confidence interval based on Neyman (1923)'s variance formula and the Normal approximation, it is

overly conservative and overcovers $\tau$ even if the individual causal effects are constant. Li et al. (2018b) proposed to construct confidence intervals based on Theorem 6.1. We omit the discussion here but will come back to the inference issue in Section 6.3.

# 6.2 Regression adjustment

What if we do not conduct rerandomization in the design stage but want to adjust for covariate imbalance in the analysis stage of the CRE? We will discuss several regression adjustment strategies.

# 6.2.1 Covariate-adjusted FRT

The covariates $\mathbf{X}$ are all fixed, and furthermore, under $H_{0\mathrm{F}}$ , the observed outcomes are all fixed. Therefore, we can simulate the distribution of any test statistic $T = T(\mathbf{Z},\mathbf{Y},\mathbf{X})$ and calculate the $p$ -value. The basic idea of the FRT remains the same in the presence of additional covariates.

There are two general strategies to construct the test statistic. Problem 3.6 before hints at both of them. I summarize them below, using the terminology from Zhao and Ding (2021a).

Definition 6.2 (pseudo-outcome strategy for covariate-adjusted FRT) We can construct the test statistic based on residuals from fitted statistical models. We can regress $Y_{i}$ on $X_{i}$ to obtain residual $\hat{\varepsilon}_i$ , and then treat $\hat{\varepsilon}_i$ as the pseudo outcome to construct test statistics.

# Definition 6.3 (model-output strategy for covariate-adjusted FRT)

We can use a regression coefficient as a test statistic. We can regress $Y_{i}$ on $(Z_{i},X_{i})$ to obtain the coefficient of $Z_{i}$ as the test statistic.

In the pseudo-outcome strategy in Definition 6.2, the regression of $Y_{i}$ on $X_{i}$ should not include the treatment $Z_{i}$ because we want to ensure that the pseudo outcome satisfies $H_{0\mathrm{F}}$ if the original outcome satisfies $H_{0\mathrm{F}}$ . In the model-output strategy in Definition 6.3, the regression of $Y_{i}$ on $(Z_{i},X_{i})$ includes the treatment $Z_{i}$ because we want to use the coefficient of $Z_{i}$ to measure the deviation from $H_{0\mathrm{F}}$ . Computationally, in strategy one, we only need to run regression once, whereas in strategy two, we need to run regression many times.

In the above, "regression" is a generic term, which can be linear regression, logistic regression, or even machine learning algorithms. The FRT with any test statistics from these two strategies will be finite-sample exact under $H_{0\mathrm{F}}$ although they differ under alternative hypotheses. The rest of this section will review some test statistics based on OLS.

# 6.2.2 Analysis of covariance and extensions

Now we turn to direct estimation of the average causal effect $\tau$ that adjusts for the observed covariates.

Historically, Fisher (1925) proposed to use the analysis of covariance (ANCOVA) to improve estimation efficiency. This remains a standard strategy in many fields. He suggested running the OLS of $Y_{i}$ on $(1,Z_{i},X_{i})$ and obtaining the coefficient of $Z_{i}$ as an estimator for $\tau$ . Let $\hat{\tau}_{\mathrm{F}}$ denote Fisher's ANCOVA estimator.

A former Berkeley Statistics Professor, David A. Freedman, reanalyzed Fisher's ANCOVA under Neyman (1923)'s potential outcomes framework. Freedman (2008a,b) found the following negative results:

1. $\hat{\tau}_{\mathrm{F}}$ is biased, but the simple difference in means $\hat{\tau}$ is unbiased.   
2. The asymptotic variance of $\hat{\tau}_{\mathrm{F}}$ may be even larger than that of $\hat{\tau}$ when $n_1 \neq n_0$ .   
3. The standard error from the OLS is inconsistent for the true standard error of $\hat{\tau}_{\mathrm{F}}$ under the CRE.

A former Berkeley Ph.D. student, Winston Lin, wrote a thesis in response to Freedman's critiques. Lin (2013) found the following positive results:

1. The bias of $\hat{\tau}_{\mathrm{F}}$ is small in large samples, and it goes to zero as the sample size approaches infinity.   
2. We can improve the asymptotic efficiency of both $\hat{\tau}$ and $\hat{\tau}_{\mathrm{F}}$ by using the coefficient of $Z_{i}$ in the OLS of $Y_{i}$ on $(1,Z_{i},X_{i},Z_{i}\times X_{i})$ . Let $\hat{\tau}_{\mathrm{L}}$ denote Lin (2013)'s estimator. Moreover, the EHW standard error is a conservative estimator for the true standard error of $\hat{\tau}_{\mathrm{L}}$ under the CRE.   
3. The EHW standard error $^2$ for $\hat{\tau}_{\mathrm{F}}$ in the OLS fit of $Y_{i}$ on $(1,Z_{i},X_{i})$ is a conservative estimator for the true standard error of $\hat{\tau}_{\mathrm{F}}$ under the CRE.

# 6.2.2.1 Some heuristics for Lin (2013)'s results

Neyman (1923)'s result demonstrates that the variance of the difference-in-means estimator $\hat{\tau}$ depends on the variances of the potential outcomes. Intuitively, we can reduce the variance of the estimator by reducing the variances

of the potential outcomes. A family of linearly adjusted estimators is

$$
\begin{array}{l} \hat {\tau} \left(\beta_ {1}, \beta_ {0}\right) = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} \left(Y _ {i} - \beta_ {1} ^ {\mathsf {T}} X _ {i}\right) - n _ {0} ^ {- 1} \sum_ {i = 1} ^ {n} \left(1 - Z _ {i}\right) \left(Y _ {i} - \beta_ {0} ^ {\mathsf {T}} X _ {i}\right) (6. 2) \\ = \left\{\hat {\hat {Y}} (1) - \beta_ {1} ^ {\mathrm {T}} \hat {\hat {X}} (1) \right\} - \left\{\hat {\hat {Y}} (0) - \beta_ {0} ^ {\mathrm {T}} \hat {\hat {X}} (0) \right\}, \tag {6.3} \\ \end{array}
$$

where $\{\hat{\bar{Y}}(1), \hat{\bar{Y}}(0)\}$ are the sample means of the outcomes, and $\{\hat{\bar{X}}(1), \hat{\bar{X}}(0)\}$ are the sample means of the covariates. This covariate-adjusted estimator $\hat{\tau}(\beta_1, \beta_0)$ tries to reduce the variance of $\hat{\tau}$ by residualizing the potential outcomes. It reduces to $\hat{\tau}$ with $\beta_1 = \beta_0 = 0$ . It has mean $\tau$ for any fixed values of $\beta_1$ and $\beta_0$ because $\bar{X} = 0$ . We are interested in finding the $(\beta_1, \beta_0)$ that minimizes the variance of $\hat{\tau}(\beta_1, \beta_0)$ . This estimator is essentially the difference in means of the adjusted potential outcomes $\{Y_i(1) - \beta_1^\top X_i, Y_i(0) - \beta_0^\top X_i\}_{i=1}^n$ . Applying Neyman (1923)'s result, this estimator has variance

$$
\mathrm {v a r} \{\hat {\tau} (\beta_ {1}, \beta_ {0}) \} = \frac {S ^ {2} (1 ; \beta_ {1})}{n _ {1}} + \frac {S ^ {2} (0 ; \beta_ {0})}{n _ {0}} - \frac {S ^ {2} (\tau ; \beta_ {1} , \beta_ {0})}{n},
$$

where $S^2 (z;\beta_z)$ ( $z = 1,0$ ) and $S^2 (\tau ;\beta_1,\beta_0)$ are the finite population variances of the adjusted potential outcomes and individual causal effects, respectively; moreover, a conservative variance estimate is

$$
\hat {V} (\beta_ {1}, \beta_ {0}) = \frac {\hat {S} ^ {2} (1 ; \beta_ {1})}{n _ {1}} + \frac {\hat {S} ^ {2} (0 ; \beta_ {0})}{n _ {0}},
$$

where

$$
\hat {S} ^ {2} (1; \beta_ {1}) = (n _ {1} - 1) ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} (Y _ {i} - \gamma_ {1} - \beta_ {1} ^ {\mathsf {T}} X _ {i}) ^ {2},
$$

$$
\hat {S} ^ {2} (0; \beta_ {0}) = (n _ {0} - 1) ^ {- 1} \sum_ {i = 1} ^ {n} (1 - Z _ {i}) (Y _ {i} - \gamma_ {0} - \beta_ {0} ^ {\mathsf {T}} X _ {i}) ^ {2}
$$

are the sample variances of the adjusted potential outcomes with $\gamma_{1}$ and $\gamma_{0}$ being the sample means of $Y_{i} - \beta_{1}^{\mathrm{T}}X_{i}$ under treatment and $Y_{i} - \beta_{0}^{\mathrm{T}}X_{i}$ under control. To minimize $\hat{V} (\beta_1,\beta_0)$ , we need to solve two OLS problems $^3$ :

$$
\min _ {\gamma_ {1}, \beta_ {1}} \sum_ {i = 1} ^ {n} Z _ {i} (Y _ {i} - \gamma_ {1} - \beta_ {1} ^ {\mathsf {T}} X _ {i}) ^ {2}, \quad \min _ {\gamma_ {0}, \beta_ {0}} \sum_ {i = 1} ^ {n} (1 - Z _ {i}) (Y _ {i} - \gamma_ {0} - \beta_ {0} ^ {\mathsf {T}} X _ {i}) ^ {2}.
$$

We run OLS of $Y_{i}$ on $X_{i}$ for the treatment and control groups separately and obtain $(\hat{\gamma}_1,\hat{\beta}_1)$ and $(\hat{\gamma}_0,\hat{\beta}_0)$ . The final estimator is

$$
\begin{array}{l} \hat {\tau} (\hat {\beta} _ {1}, \hat {\beta} _ {0}) = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} (Y _ {i} - \hat {\beta} _ {1} ^ {\mathsf {T}} X _ {i}) - n _ {0} ^ {- 1} \sum_ {i = 1} ^ {n} (1 - Z _ {i}) (Y _ {i} - \hat {\beta} _ {0} ^ {\mathsf {T}} X _ {i}) \\ = \left\{\hat {\tilde {Y}} (1) - \hat {\beta} _ {1} ^ {\mathsf {T}} \hat {\tilde {X}} (1) \right\} - \left\{\hat {\tilde {Y}} (0) - \hat {\beta} _ {0} ^ {\mathsf {T}} \hat {\tilde {X}} (0) \right\}. \\ \end{array}
$$

From the properties of the OLS fits (see (B.5)), we know

$$
\hat {\bar {Y}} (1) = \hat {\gamma} _ {1} + \hat {\beta} _ {1} ^ {\mathsf {T}} \hat {\bar {X}} (1), \quad \hat {\bar {Y}} (0) = \hat {\gamma} _ {0} + \hat {\beta} _ {0} ^ {\mathsf {T}} \hat {\bar {X}} (0).
$$

Therefore, we can rewrite the estimator as

$$
\hat {\tau} \left(\hat {\beta} _ {1}, \hat {\beta} _ {0}\right) = \hat {\gamma} _ {1} - \hat {\gamma} _ {0} \tag {6.4}
$$

The equivalent form in (6.4) suggests that we can obtain $\hat{\tau} (\hat{\beta}_1,\hat{\beta}_0)$ from a single OLS fit below.

Proposition 6.2 The estimator $\hat{\tau} (\hat{\beta}_1,\hat{\beta}_0)$ in (6.4) equals the coefficient of $Z_{i}$ in the OLS fit of $Y_{i}$ on $(1,Z_{i},X_{i},Z_{i}\times X_{i})$ , which is Lin (2013)'s estimator $\hat{\tau}_{\mathrm{L}}$ introduced before.

I leave the proof of Proposition 6.2 to Problem 6.7, which is a pure linear algebra fact.

Based on the discussion above, a conservative variance estimator for $\hat{\tau}_{\mathrm{L}}$ is

$$
\begin{array}{l} \hat {V} (\hat {\beta} _ {1}, \hat {\beta} _ {0}) = \frac {1}{n _ {1} (n _ {1} - 1)} \sum_ {i = 1} ^ {n} Z _ {i} (Y _ {i} - \hat {\gamma} _ {1} - \hat {\beta} _ {1} ^ {\intercal} X _ {i}) ^ {2} \\ + \frac {1}{n _ {0} (n _ {0} - 1)} \sum_ {i = 1} ^ {n} (1 - Z _ {i}) \left(Y _ {i} - \hat {\gamma} _ {0} - \hat {\beta} _ {0} ^ {\mathrm {T}} X _ {i}\right) ^ {2}. \\ \end{array}
$$

Based on quite technical calculations, Lin (2013) further showed that the EHW standard error from the OLS in Proposition 6.2 is almost identical to $\hat{V} (\hat{\beta}_1,\hat{\beta}_0)$ which is a conservative estimator of the true standard error of $\hat{\tau}_{\mathrm{L}}$ under the CRE. Intuitively, this is because we do not assume that the linear model is correctly specified, and the EHW standard error is robust to model misspecification.

There is a subtle issue with the discussion above. The variance formula $\mathrm{var}\{\hat{\tau} (\beta_1,\beta_0)\}$ works for fixed $(\beta_{1},\beta_{0})$ , but the estimator $\hat{\tau} (\hat{\beta}_1,\hat{\beta}_0)$ uses two estimated coefficients $(\hat{\beta}_1,\hat{\beta}_0)$ . The additional uncertainty in the estimated coefficients may cause finite-sample bias in the final estimator. Lin (2013) showed that this issue goes away asymptotically because $\hat{\tau} (\hat{\beta}_1,\hat{\beta}_0)$ behaves similarly to $\hat{\tau} (\tilde{\beta}_1,\tilde{\beta}_0)$ , where $\tilde{\beta}_{1}$ and $\tilde{\beta}_{0}$ are the limit of $\hat{\beta}_{1}$ and $\hat{\beta}_{0}$ , respectively. Heuristically, the difference between $\hat{\tau} (\hat{\beta}_1,\hat{\beta}_0)$ and $\hat{\tau} (\tilde{\beta}_1,\tilde{\beta}_0)$ depends on

$$
(\hat {\beta} _ {z} - \tilde {\beta} _ {z}) ^ {\mathsf {T}} \hat {\tilde {X}} (z), \quad (z = 0, 1)
$$

which is a product of two terms of small order. As a warning, the asymptotic theory requires a large sample size and some regularity conditions on the potential outcomes and covariates. In finite samples, regression adjustment can be even harmful due to the additional uncertainty in the estimated coefficients $\hat{\beta}_{1}$ and $\hat{\beta}_{0}$ .

TABLE 6.1: Predicting the potential outcomes   

<table><tr><td>X</td><td>Z</td><td>Y(1)</td><td>Y(0)</td><td>Ŷ(1)</td><td>Ŷ(0)</td></tr><tr><td>X1</td><td>1</td><td>Y1(1)</td><td>?</td><td>μ1(X1)</td><td>μ0(X1)</td></tr><tr><td>Xn1</td><td>1</td><td>Yn1(1)</td><td>?</td><td>μ1(Xn1)</td><td>μ0(Xn1)</td></tr><tr><td>Xn1+1</td><td>0</td><td>?</td><td>Yn1+1(0)</td><td>μ1(Xn1+1)</td><td>μ0(Xn1+1)</td></tr><tr><td>Xn</td><td>0</td><td>?</td><td>Yn(0)</td><td>μ1(Xn)</td><td>μ0(Xn)</td></tr></table>

# 6.2.2.2 Understanding Lin (2013)'s estimator via predicting the potential outcomes

We can view Lin (2013)'s estimator as a predictive estimator based on OLS fits of the potential outcomes on the covariates. We build a prediction model for $Y(1)$ based on $X$ using the data from the treatment group:

$$
\hat {\mu} _ {1} (X) = \hat {\gamma} _ {1} + \hat {\beta} _ {1} ^ {\mathrm {T}} X. \tag {6.5}
$$

Similarly, we build a prediction model for $Y(0)$ based on $X$ using the data from the control group:

$$
\hat {\mu} _ {0} (X) = \hat {\gamma} _ {0} + \hat {\beta} _ {0} ^ {\mathrm {T}} X. \tag {6.6}
$$

Table 6.1 illustrates the prediction of the potential outcomes. If we predict the missing potential outcomes, then we have the following predictive estimator:

$$
\hat {\tau} _ {\text {p r e d}} = n ^ {- 1} \left\{\sum_ {Z _ {i} = 1} Y _ {i} + \sum_ {Z _ {i} = 0} \hat {\mu} _ {1} \left(X _ {i}\right) - \sum_ {Z _ {i} = 1} \hat {\mu} _ {0} \left(X _ {i}\right) - \sum_ {Z _ {i} = 0} Y _ {i} \right\}. \tag {6.7}
$$

We can verify that with (6.5) and (6.6), the predictive estimator equals Lin (2013)'s estimator:

$$
\hat {\tau} _ {\text {p r e d}} = \hat {\tau} _ {\mathrm {L}}. \tag {6.8}
$$

If we predict all potential outcomes even if they are observed, we have the following projective estimator:

$$
\hat {\tau} _ {\text {p r o j}} = n ^ {- 1} \sum_ {i = 1} ^ {n} \left\{\hat {\mu} _ {1} \left(X _ {i}\right) - \hat {\mu} _ {0} \left(X _ {i}\right) \right\}. \tag {6.9}
$$

We can verify that with (6.5) and (6.6), the projective estimator equals Lin (2013)'s estimator:

$$
\hat {\tau} _ {\text {p r o j}} = \hat {\tau} _ {\mathrm {L}}. \tag {6.10}
$$

I leave the proofs of (6.8) and (6.10) to Problem 6.8.

The terminology "predictive" and "projective" is from the survey sampling literature (Firth and Bennett, 1998; Ding and Li, 2018). The more general formulas (6.7) and (6.9) are well-defined with other predictors of the potential outcomes. To make connections with Lin (2013)'s estimator, I focus on the linear predictors here. The predictors $\hat{\mu}_1(X)$ and $\hat{\mu}_0(X)$ can be quite general, including much more complicated machine learning algorithms. However, constructing a point estimator is just the first step in analyzing the CRE. A more important second step is to quantify the uncertainty associated with the estimator, which depends on the properties of the predictors of the potential outcomes. Nevertheless, without doing additional theoretical analysis, we can always use (6.7) and (6.9) as the test statistics in the FRT.

# 6.2.2.3 Understanding Lin (2013)'s estimator via adjusting for covariate imbalance

The linearly adjusted estimator has an equivalent form

$$
\hat {\tau} \left(\beta_ {1}, \beta_ {0}\right) = \hat {\tau} - \gamma^ {\mathrm {T}} \hat {\tau} _ {X} \tag {6.11}
$$

where $\gamma = \frac{n_0}{n}\beta_1 + \frac{n_1}{n}\beta_0$ , so we can also write it as $\hat{\tau} (\gamma) = \hat{\tau} (\beta_{1},\beta_{0})$ . Similarly, Lin (2013)'s estimator has an equivalent form

$$
\hat {\tau} _ {\mathrm {L}} = \hat {\tau} - \hat {\gamma} ^ {\mathrm {T}} \hat {\tau} _ {X}, \tag {6.12}
$$

where $\hat{\gamma} = \frac{n_0}{n}\hat{\beta}_1 + \frac{n_1}{n}\hat{\beta}_0$ . I leave the proofs of (6.11) and (6.12) to Problem 6.9. The forms (6.11) and (6.12) are the mathematical statements of "adjusting for the covariate imbalance." They essentially subtract some linear combinations of the difference in means of the covariates. Since $\hat{\tau}$ and $\hat{\tau}_X$ are correlated under the CRE, the covariate adjustment with an appropriately chosen $\gamma$ reduces the variance of $\hat{\tau}$ . Another interesting feature of (6.11) and (6.12) is that the final estimators depend only on $\gamma$ or $\hat{\gamma}$ , so the choice of the $\beta$ -coefficients is not unique. Li and Ding (2020) pointed out this simple fact. Therefore, Lin (2013)'s estimator is just one of the optimal estimators. However, it can be easily implemented via the standard OLS with the EHW standard error. That's why this book focuses on it.

# 6.2.3 Some additional remarks on regression adjustment

# 6.2.3.1 Duality between ReM and regression adjustment

Li et al. (2018b) pointed out that ReM and Lin (2013)'s regression adjustment are duals in using covariates in the design and analysis stages of the experiment. To be more specific, when $a$ is small, the asymptotic distribution of $\hat{\tau}$ under ReM is almost identical to the asymptotic distribution of $\hat{\tau}_{\mathrm{L}}$ under the CRE. So ReM uses covariates in the design stage and Lin (2013)'s regression adjustment uses covariates in the analysis stage, achieving nearly the same asymptotic efficiency gain when $a$ is small.

# 6.2.3.2 Equivalence of regression adjustment and post-stratification

If we have discrete covariate $C_i$ with $K$ categories, we can create $K - 1$ centered dummy variables

$$
X _ {i} = \left(I (C _ {i} = 1) - \pi_ {[ 1 ]}, \dots , I (C _ {i} = K - 1) - \pi_ {[ K - 1 ]}\right)
$$

where $\pi_{[k]}$ equals the proportion of units with $C_i = k$ . In this case, Lin (2013)'s regression adjustment is equivalent to post-stratification, as summarized by the following proposition.

Proposition 6.3 $\hat{\tau}_{\mathrm{L}}$ based in $X_{i}$ is numerically identical to the poststratification estimator $\hat{\tau}_{\mathrm{PS}}$ based on $C_i$ (see Chapter 5.4).

I leave the proof of Proposition 6.3 as Problem 6.11.

# 6.2.3.3 Difference-in-difference as a special case of covariate adjustment $\hat{\tau} (\beta_1,\beta_0)$

An important covariate $X$ in many studies is the lagged outcome before the treatment. For instance, the covariate $X$ is the pre-test score if the outcome $Y$ is the post-test score in educational research; the covariate $X$ is the log wage before the job training program if the outcome $Y$ is the log wage after the job training program. With the lagged outcome $X$ as a covariate, a popular estimator is the gain score or difference-in-difference estimator with $\beta_{1} = \beta_{0} = 1$ in (6.2) and (6.3):

$$
\begin{array}{l} \hat {\tau} (1, 1) = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} (Y _ {i} - X _ {i}) - n _ {0} ^ {- 1} \sum_ {i = 1} ^ {n} (1 - Z _ {i}) (Y _ {i} - X _ {i}) \\ = \left\{\hat {\bar {Y}} (1) - \hat {\bar {Y}} (0) \right\} - \left\{\hat {\bar {X}} (1) - \hat {\bar {X}} (0) \right\}. \\ \end{array}
$$

The first form of $\hat{\tau}(1,1)$ justifies the name gain score because it is essentially the difference in means of the gain score $g_i = Y_i - X_i$ . The second form of $\hat{\tau}(1,1)$ justifies the name difference-in-difference because it is the difference between two differences in means. This estimator is different from Lin (2013)'s estimator: it fixes $\beta_1 = \beta_0 = 1$ in advance while Lin (2013)'s estimator involves two estimated $\beta$ 's. The $\hat{\tau}(1,1)$ is unbiased with a conservative variance estimator

$$
\begin{array}{l} \hat {V} (1, 1) = \frac {1}{n _ {1} (n _ {1} - 1)} \sum_ {i = 1} ^ {n} Z _ {i} \{g _ {i} - \hat {\bar {g}} (1) \} ^ {2} \\ + \frac {1}{n _ {0} (n _ {0} - 1)} \sum_ {i = 1} ^ {n} (1 - Z _ {i}) \{g _ {i} - \hat {\tilde {g}} (0) \} ^ {2}, \\ \end{array}
$$

where $\hat{\hat{g}}(1)$ and $\hat{\hat{g}}(0)$ are the sample means of the gain score $g_i = Y_i - X_i$ under the treatment and control, respectively. When the lagged outcome is a strong

predictor of the outcome, the gain score $g_{i} = Y_{i} - X_{i}$ often has a much smaller variance than the outcome itself. In this case, $\hat{\tau}(1,1)$ often greatly reduces the variance of the simple difference in means of the outcome. See Problem 6.12 for more details.

In theory, Lin (2013)'s estimator is always more efficient than $\hat{\tau}(1,1)$ with large samples. However, Lin (2013)'s estimator is biased in finite samples, whereas $\hat{\tau}(1,1)$ is always unbiased.

# 6.2.4 Extension to the SRE

It is possible that we have an experiment stratified on a discrete variable $C$ and we also observe additional covariates $X$ . If all strata are large, then we can obtain Lin (2013)'s estimators within strata $\hat{\tau}_{\mathrm{L},[k]}$ and obtain the final estimator as

$$
\hat {\tau} _ {\mathrm {L , S}} = \sum_ {k = 1} ^ {K} \pi_ {[ k ]} \hat {\tau} _ {\mathrm {L}, [ k ]}.
$$

A conservative variance estimator is

$$
\hat {V} _ {\mathrm {L}, \mathrm {S}} = \sum_ {k = 1} ^ {K} \pi_ {[ k ]} ^ {2} \hat {V} _ {\mathrm {E H W}, [ k ]},
$$

where $\hat{V}_{\mathrm{EHW},[k]}$ is the EHW variance estimator from the OLS fit of the outcome on the intercept, the treatment indicator, the covariates, and their interactions within stratum $k$ . Importantly, we need to center covariates by their stratum-specific means.

# 6.3 Unification, combination, and comparison

Li and Ding (2020) unified the literature and showed that we can combine rerandomization and regression adjustment. That is, if we rerandomize in the design stage, we can use Lin (2013)'s estimator with the EHW standard error in the analysis stage. The combination of rerandomization and regression adjustment improves covariate balance in the design stage and estimation efficiency in the analysis stage.

Table 6.2 summarizes the literature from Neyman (1923) to Li and Ding (2020). Arrow 1 illustrates the efficiency gain of covariate adjustment in the CRE: asymptotically, $\hat{\tau}_{\mathrm{L}}$ has a smaller variance than $\hat{\tau}$ . Arrow 2 illustrates the efficiency gain of ReM: asymptotically, $\hat{\tau}$ has narrower quantile ranges under the ReM than under the CRE. Arrows 3 and 4 illustrate the benefits of the combination of ReM and the CRE.

TABLE 6.2: Design and analysis of experiments   

<table><tr><td></td><td colspan="4">analysis</td></tr><tr><td rowspan="3">design</td><td>CRE</td><td>\( \hat{\tau} \) (Neyman, 1923)</td><td>\( \xrightarrow{1} \)</td><td>\( \hat{\tau}_{\mathrm {L}} \) (Lin, 2013)</td></tr><tr><td></td><td>\( 2\Big\downarrow \)</td><td></td><td>\( \Big\downarrow4 \)</td></tr><tr><td>ReM</td><td>\( \hat{\tau} \) (Li et al., 2018b)</td><td>\( \xrightarrow{3} \)</td><td>\( \hat{\tau}_{\mathrm {L}} \) (Li and Ding, 2020)</td></tr></table>

# 6.4 Simulation

Angrist et al. (2009) conducted an experiment to evaluate different strategies to improve academic performance among college freshmen in a Canadian university. Here I use a subset of the original data, focusing on the control group and the treatment group offered academic support services and financial incentives for good grades. The outcome is the GPA at the end of the first year. I impute the missing outcomes with the observed average which is somewhat arbitrary (see Problem 6.14). Two covariates are the gender and baseline GPA.

```txt
angrist = read.dta("star.dta")
angrist2 = subset(angrist, control == 1||sfsp == 1)
## imputing missing outcomes
y = angrist2$GPA_year1
mean = mean(y, na.rs = TRUE)
y = ifelse(is.na(y), mean, y)
z = angrist2$sfsp
x = angrist2[, c("female", "gpu0")] 
```

The following code gives the results based on the unadjusted and adjusted estimators.

```python
>>> unadjusted estimator
fit_unadj = lm(y ~ z)
>>> ace_unadj = coef(fit_unadj)[2]
>>> se_unadj = sqrt(hccm(fit_unadj, type = "hc2"))[2, 2])
>>> regression adjustment
x = scale(x)
>>> fit_adj = lm(y ~ z*x)
>>> ace_adj = coef(fit_adj)[2]
>>> se_adj = sqrt(hccm(fit_adj, type = "hc2"))[2, 2])
>>> res = c(ace_unadj, ace_adj, se_unadj, se_adj)
>>> dim(res) = c(2, 2)
>>> t.stat = res[, 1]/res[, 2]
>>> p.value = 2*pnorm(abs(t.stat), lower.tail = FALSE)
>>> res = cbind(res, t.stat, p.value) 
```

![](images/c105aec6e67aebba7e6f742cf91e8838217a476fb5404f1f840a3c38b2f9c78e.jpg)  
FIGURE 6.2: Simulation with 2000 Monte Carlo replicates and $a = 0.05$ for ReM

```julia
> rownames(res) = c("Neyman", "Lin")
> colnames(res) = c("estimate", "s.e.", "t-stat", "p-value")
> round(res, 3)
estimate s.e. t-stat p-value
Neyman 0.054 0.076 0.719 0.472
Lin 0.075 0.072 1.036 0.300 
```

The adjusted estimator has a smaller standard error although it gives the same insignificant result as the unadjusted estimator.

I also use this dataset to conduct simulation studies to evaluate the four design and analysis strategies summarized in Table 6.2. I fit quadratic functions of the outcome on the covariates and use them to impute all the missing potential outcomes, separately for the treated and control groups. To show the improvement of ReM and regression adjustment, I also rescale the error terms by 0.1 and 0.25 to increase the signal-to-noise ratio. With the imputed Science Table, I generate 2000 treatments, obtain the observed data, and calculate the estimators. In the simulation, the "true" outcome model is nonlinear, but we still use linear adjustment for estimation. By doing this, we can evaluate the properties of the estimators even when the linear model is misspecified.

Figure 6.2 shows the violin plots<sup>4</sup> of the four combinations, subtracting the true $\tau$ from the estimates. As predicted by the theory, all estimators are nearly unbiased, and both ReM and regression adjustment improve efficiency. They are more effective when the noise level is smaller.

# 6.5 Final remarks

ReM uses the Mahalanobis distance as the balance criterion. We can consider general rerandomization with the balance criterion defined as a function of $\mathbf{Z}$ and $\mathbf{X}$ . For example, we can use the following criterion based on marginal tests for all coordinates of $X_{i} = (x_{i1},\ldots ,x_{iK})^{\top}$ . We accept $\mathbf{Z}$ if and only if

$$
\left| \frac {\hat {\tau} _ {x k}}{\sqrt {\frac {n}{n _ {1} n _ {0}} S _ {x k} ^ {2}}} \right| \leq a \quad (k = 1, \dots , K) \tag {6.13}
$$

for some predetermined constant $a > 0$ , where $S_{xk}^2$ is the finite-population variance of covariate $x_{ik}$ . For example, $a$ is some upper quantile of a standard Normal distribution. See Zhao and Ding (2021b) for the theory for the rerandomization based on criterion (6.13) as well as other criteria.

With a continuous outcome, Fisher's ANCOVA has been the standard approach for many years. Lin (2013)'s improvement has better theoretical properties even when the linear model is misspecified. With a binary outcome, it is common to use the coefficient of the treatment in the logistic regression of the observed outcome on the intercept, the treatment indicator, and covariates to estimate the causal effects. However, Freedman (2008c) showed that this logistic regression does not have nice properties under the potential outcomes framework. Even if the logistic model is correct, the coefficient estimates the conditional odds ratio (see Chapter B.6) which may not be the parameter of interest; when the logistic model is incorrect, it is even harder to interpret the coefficient. From the discussion above, if the parameter of interest is the average causal effect, we can still use Lin (2013)'s estimator to analyze the binary outcome data in the CRE. Guo and Basse (2023) extend Lin (2013)'s theory to allow for using generalized linear models to construct estimators for the average causal effect under the potential outcomes framework.

Other extensions of Lin (2013)'s theory focus on high dimensional covariates. Bloniarz et al. (2016) focus on the regime with many covariates than the sample size, and suggest replacing the OLS fits with the least absolute shrinkage and selection operator (LASSO) fits (Tibshirani, 1996) of the outcome on the intercept, the treatment, covariates and their interactions. Lei and Ding (2021) focus on the regime with a diverging number of covariates without assuming sparsity, and under certain regularity conditions, they show that Lin (2013)'s estimator is still consistent and asymptotically Normal. Wager et al. (2016) propose to use machine learning methods to analyze high dimensional experimental data.

# 6.6 Homework Problems

# 6.1 FRT under ReM

Describe the FRT under ReM.

# 6.2 Invariance of the Mahalanobis Distance

Prove Lemma 6.1.

# 6.3 Bias of the difference-in-means estimator under rerandomization

Assume that we draw $\mathbf{Z} = (Z_{1},\ldots ,Z_{n})$ from a CRE and accept it if and only if $\phi (\mathbf{Z},\mathbf{X}) = 1$ , where $\phi$ is a predetermined balance criterion. Show that if $n_1 = n_0$ and

$$
\phi (\boldsymbol {Z}, \boldsymbol {X}) = \phi \left(\mathbf {1} _ {n} - \boldsymbol {Z}, \boldsymbol {X}\right), \tag {6.14}
$$

then $\hat{\tau}$ is unbiased for $\tau$ . Verify that rerandomization using the Mahalanobis distance satisfies (6.14) if $n_1 = n_0$ . Give a counterexample that $\hat{\tau}$ is biased for $\tau$ when these two conditions do not hold.

Remark: $\phi(\mathbf{Z},\mathbf{X})$ can be a general balance criterion in this problem. ReM is a special case with $\phi(\mathbf{Z},\mathbf{X}) = I(M \leq a)$ .

# 6.4 Equivalent form of $R^2$ in the CRE

Prove Proposition 6.1.

# 6.5 More on linear projections of the potential outcomes onto covariates

Show that

$$
S ^ {2} (1 \mid X) = S _ {Y (1) X} \left(S _ {X} ^ {2}\right) ^ {- 1} S _ {X Y (1)}
$$

where $S_{XY(1)}$ is the finite population covariance between $Y_{i}(1)$ 's and $X_{i}$ 's, $S_{Y(1)X} = S_{XY(1)}^{\mathsf{T}}$ , and $S_{X}^{2}$ is the finite population covariance matrix of $X_{i}$ 's. Find the analogous formulas for $S^{2}(0 \mid X)$ and $S^{2}(\tau \mid X)$ .

# 6.6 Comparing the true variances within the family of linearly adjusted estimator

Show that the variance $\hat{\tau} (\beta_1,\beta_0)$ decomposes into

$$
\operatorname {v a r} \{\hat {\tau} (\beta_ {1}, \beta_ {0}) \} = \operatorname {v a r} \{\hat {\tau} (\tilde {\beta} _ {1}, \tilde {\beta} _ {0}) \} + \operatorname {v a r} \{\hat {\tau} (\beta_ {1}, \beta_ {0}) - \hat {\tau} (\tilde {\beta} _ {1}, \tilde {\beta} _ {0}) \}
$$

where $\tilde{\beta}_{1}$ and $\tilde{\beta}_{0}$ are the coefficients of $X_{i}$ in the OLS projection of $Y_{i}(1)$ 's and $Y_{i}(0)$ 's onto $(1, X_{i})$ 's, respectively.

Remark: Li and Ding (2017, Example 9) derived the decomposition. It shows that based on the true variance, $\hat{\tau} (\tilde{\beta}_1,\tilde{\beta}_0)$ is an optimal choice within

the family of linearly adjusted estimator because $\mathrm{var}\{\hat{\tau} (\beta_1,\beta_0) - \hat{\tau} (\tilde{\beta}_1,\tilde{\beta}_0)\}$ is always non-negative.

# 6.7 Lin's estimator for covariate adjustment

Prove Proposition 6.2.

# 6.8 Predictive and projective estimators

Prove (6.8) and (6.10).

# 6.9 Equivalent form of the covariate-adjusted estimator

Prove (6.11) and (6.12).

# 6.10 ANCOVA also adjusts for covariate imbalance

This problem gives a result for ANCOVA that is similar to (6.12).

Show that

$$
\hat {\tau} _ {\mathrm {F}} = \hat {\tau} - \hat {\gamma} _ {\mathrm {F}} ^ {\mathrm {T}} \hat {\tau} _ {X},
$$

where $\hat{\gamma}_{\mathrm{F}}$ is the coefficient of $X_{i}$ in the OLS fit of $Y_{i}$ on $(1,Z_{i},X_{i})$

# 6.11 Regression adjustment / post-stratification of CRE

Prove Proposition 6.3.

Remark: Sometimes $\hat{\tau}_{\mathrm{PS}}$ or $\hat{\tau}_{\mathrm{L}}$ may not be well-defined. In those cases, we treat $\hat{\tau}_{\mathrm{PS}}$ and $\hat{\tau}_{\mathrm{L}}$ as equal. You can ignore this complexity in the proof.

# 6.12 More on the difference-in-difference estimator in the CRE

This problem gives more details for the difference-in-difference estimator in the CRE in Section 6.2.3.3.

Show that $\hat{\tau}(1,1)$ is unbiased for $\tau$ , calculate its variance, and show that $\hat{V}(1,1)$ is a conservative estimator for the true variance of $\hat{\tau}(1,1)$ . When does $E\{\hat{V}(1,1)\} = \mathrm{var}\{\hat{\tau}(1,1)\}$ hold?

Compare the variances of $\hat{\tau}(0,0)$ and $\hat{\tau}(1,1)$ to show that

$$
\operatorname {v a r} \{\hat {\tau} (0, 0) \} \geq \operatorname {v a r} \{\hat {\tau} (1, 1) \}
$$

if and only if

$$
2 \frac {n _ {0}}{n} \beta_ {1} + 2 \frac {n _ {1}}{n} \beta_ {0} \geq 1,
$$

where

$$
\beta_ {1} = \frac {\sum_ {i = 1} ^ {n} (X _ {i} - \bar {X}) \{Y _ {i} (1) - \bar {Y} (1) \}}{\sum_ {i = 1} ^ {n} (X _ {i} - \bar {X}) ^ {2}}, \quad \beta_ {0} = \frac {\sum_ {i = 1} ^ {n} (X _ {i} - \bar {X}) \{Y _ {i} (0) - \bar {Y} (0) \}}{\sum_ {i = 1} ^ {n} (X _ {i} - \bar {X}) ^ {2}}
$$

are the coefficients of $X_{i}$ in the OLS fits of $Y_{i}(1)$ and $Y_{i}(0)$ on $(1, X_{i})$ , respectively.

Remark: Gerber and Green (2012, page 28) discussed a special case of this problem with $n_1 = n_0$ .

# 6.13 Data re-analyses of the Penn Bonus Experiment

Re-analyze the Penn Bonus Experiment data. The analysis in Chapter 5 uses the treatment indicator, the outcome, and the block indicator. Now we want to use all other covariates.

Conduct regression adjustments within the strata of the experiment, and then combine these adjusted estimators to estimate the average causal effect. Report the point estimator, estimated standard error, and $95\%$ confidence interval. Compare them with those without regression adjustment.

# 6.14 Missing outcomes in randomized experiments

The data analysis in Section 6.4 uses a naive imputation method to deal with missing outcomes. It is somewhat arbitrary.

Impute the missing outcomes under the treatment and control, respectively, based on the observed means. Do the results change?

Impute the missing outcomes under the treatment and control, respectively, based on linear regressions of the observed outcomes on the covariates. Do the results change?

Do you have other ways to deal with missing outcomes? Justify them and implement them to analyze the dataset.

# 6.15 Recommended reading

The title of this chapter is the same as that of Li and Ding (2020), which studied the roles of rerandomization and regression adjustment in the design and analysis stages of randomized experiments, respectively.

# 7

# Matched-Pairs Experiment

The matched-pairs experiment (MPE) is the most extreme version of the SRE with only one treated unit and one control unit within each stratum. In this case, the strata are also called pairs. Although this type of experiment is a special case of the SRE discussed in Chapter 5, it has its own estimation and inference strategy. Moreover, it has many new features and it is closely related to the "matching" strategy in observational studies which will be covered in Chapter 15 later. So we discuss the MPE here, in its own chapter.

# 7.1 Design of the experiment and potential outcomes

Consider an experiment with $2n$ units. If we have predictive covariates to the outcomes, we can pair units based on the similarity of covariates. With a scalar covariate, we can order units based on this covariate and then form pairs based on the adjacent units. With many covariates, we can define pairwise distances between units and then form pairs based on these distances. In this case, pair matching can be done using a greedy algorithm or an optimal nonbipartite matching algorithm. The greedy algorithm pairs the two units with the smallest distance, drops them from the pool of units, pairs the two remaining units with the smallest distance, etc. The optimal nonbipartite matching algorithm divides the $2n$ units into $n$ pairs of two units to minimize the sum of the within-pair distances. See Greevy et al. (2004) for more details of the computational aspect of the MPE. In this chapter, we assume that the pairs are formed based on the covariates, and discuss the subsequent design and analysis issues.

Let $(i,j)$ index the unit $j$ in pair $i$ , where $i = 1,\dots,n$ and $j = 1,2$ . Unit $(i,j)$ has potential outcomes $Y_{ij}(1)$ and $Y_{ij}(0)$ under the treatment and control, respectively. Within each pair, we randomly assign one unit to receive the treatment and the other to receive the control. Let

$$
Z _ {i} = \left\{ \begin{array}{l l} 1, & \text {i f t h e f i r s t u n i t r e c e i v e s t h e t r a t e m e n t ,} \\ 0, & \text {i f t h e s e c o n d u n i t r e c e i v e s t h e t r a t e m e n t .} \end{array} \right.
$$

We can formally define MPE based on the treatment assignment mechanism.

Definition 7.1 (MPE) We have

$$
(Z _ {i}) _ {i = 1} ^ {n} \stackrel {\text {I I D}} {\sim} \text {B e r n o u l l i} (1 / 2). \tag {7.1}
$$

The observed outcomes within pair $i$ are

$$
Y _ {i 1} = Z _ {i} Y _ {i 1} (1) + (1 - Z _ {i}) Y _ {i 1} (0) = \left\{ \begin{array}{l l} Y _ {i 1} (1), & \text {i f} Z _ {i} = 1; \\ Y _ {i 1} (0), & \text {i f} Z _ {i} = 0; \end{array} \right.
$$

and

$$
Y _ {i 2} = Z _ {i} Y _ {i 2} (0) + (1 - Z _ {i}) Y _ {i 2} (1) = \left\{ \begin{array}{l l} Y _ {i 2} (0), & \text {i f} Z _ {i} = 1; \\ Y _ {i 2} (1), & \text {i f} Z _ {i} = 0. \end{array} \right.
$$

So the observed data are $(Z_{i},Y_{i1},Y_{i2})_{i = 1}^{n}$

# 7.2 FRT

Similar to the discussion before, we can always use the FRT to test the sharp null hypothesis:

$$
H _ {0 \mathrm {F}}: Y _ {i j} (1) = Y _ {i j} (0) \text {f o r a l l} i = 1, \dots n \text {a n d} j = 1, 2.
$$

When conducting the FRT, we need to simulate the distribution of $(Z_{1},\ldots ,Z_{n})$ from (7.1). I will discuss some canonical choices of test statistics based on the within-pair differences between the treated and control outcomes:

$$
\begin{array}{l} \hat {\tau} _ {i} = \text {o u t c o m e u n d e r t r a t e m e n t - o u t c o m e u n d e r c o n t r o l (w i t h i n p a i r} i) \\ = \left(2 Z _ {i} - 1\right) \left(Y _ {i 1} - Y _ {i 2}\right) \\ = S _ {i} \left(Y _ {i 1} - Y _ {i 2}\right), \\ \end{array}
$$

where the $S_{i} = 2Z_{i} - 1$ are IID random signs with mean 0 and variance 1, for $i = 1,\ldots ,n$ . Since the pairs with zero $\hat{\tau}_i$ 's do not contribute to the randomization distribution, we drop those pairs in the discussion of the FRT.

Example 7.1 (paired $t$ statistic) The average of the within-pair differences is

$$
\hat {\tau} = n ^ {- 1} \sum_ {i = 1} ^ {n} \hat {\tau} _ {i}.
$$

Under $H_{0\mathrm{F}}$

$$
E (\hat {\tau}) = 0
$$

and

$$
\operatorname {v a r} (\hat {\tau}) = n ^ {- 2} \sum_ {i = 1} ^ {n} \operatorname {v a r} (\hat {\tau} _ {i}) = n ^ {- 2} \sum_ {i = 1} ^ {n} \operatorname {v a r} (S _ {i}) (Y _ {i 1} - Y _ {i 2}) ^ {2} = n ^ {- 2} \sum_ {i = 1} ^ {n} \hat {\tau} _ {i} ^ {2}.
$$

Based on the CLT for the sum of independent random variables, we have the Normal approximation:

$$
\frac {\hat {\tau}}{\sqrt {n ^ {- 2} \sum_ {i = 1} ^ {n} \hat {\tau} _ {i} ^ {2}}} \to \mathrm {N} (0, 1)
$$

in distribution. We can use this Normal approximation to construct an asymptotic test. Many standard textbooks suggest using the following paired t statistic in the MPE:

$$
t _ {p a i r} = \frac {\hat {\tau}}{\sqrt {\{n (n - 1) \} ^ {- 1} \sum_ {i = 1} ^ {n} (\hat {\tau} _ {i} - \hat {\tau}) ^ {2}}},
$$

which is almost identical to $\hat{\tau}$ with large $n$ and small $\hat{\tau}$ under $H_{0\mathrm{F}}$ .

In classic statistics, the motivation for using $t_{\mathrm{pair}}$ is under a different framework. When $\hat{\tau}_i \stackrel{\mathrm{IID}}{\sim} \mathrm{N}(0, \sigma^2)$ , we can show that $t_{\mathrm{pair}} \sim t(n - 1)$ , i.e., the exact distribution of $t_{\mathrm{pair}}$ is $t$ with degrees of freedom $n - 1$ , which is close to $\mathrm{N}(0, 1)$ with a large $n$ . The R function $\mathbf{t} \cdot \mathbf{test}$ with paired=TRUE can implement this test. With a large $n$ , these procedures give similar results. The discussion in Example 7.1 gives another justification of the classic paired $t$ test without assuming the Normality of the data.

Example 7.2 (Wilcoxon sign-rank statistic) Based on the ranks $(R_{1},\ldots ,R_{n})$ of $(|\hat{\tau}_1|,\dots ,|\hat{\tau}_n|)$ , we can define a test statistic

$$
W = \sum_ {i = 1} ^ {n} I (\hat {\tau} _ {i} > 0) R _ {i}.
$$

Under $H_{0\mathrm{F}}$ , the $|\hat{\tau}_i|$ 's are fixed so the $R_i$ 's are also fixed, which implies that

$$
E (W) = \frac {1}{2} \sum_ {i = 1} ^ {n} R _ {i} = \frac {1}{2} \sum_ {i = 1} ^ {n} i = \frac {n (n + 1)}{4}
$$

and

$$
\operatorname {v a r} (W) = \frac {1}{4} \sum_ {i = 1} ^ {n} R _ {i} ^ {2} = \frac {1}{4} \sum_ {i = 1} ^ {n} i ^ {2} = \frac {n (n + 1) (2 n + 1)}{2 4}.
$$

The CLT for the sum of independent random variables ensures the following Normal approximation:

$$
\frac {W - n (n + 1) / 4}{\sqrt {n (n + 1) (2 n + 1) / 2 4}} \rightarrow \mathrm {N} (0, 1)
$$

in distribution. We can use this Normal approximation to construct an asymptotic test. The $R$ function wilcox.test with paired=TRUE can implement both the exact and asymptotic tests.

Example 7.3 (Kolmogorov-Smirnov-type statistic) Under $H_{0\mathrm{F}}$ , the absolute values $(\lvert\hat{\tau}_1\rvert,\dots,\lvert\hat{\tau}_n\rvert)$ are fixed but their signs are random. So $(\hat{\tau}_1,\dots,\hat{\tau}_n)$ and $-(\hat{\tau}_1,\dots,\hat{\tau}_n)$ should have the same distribution. Let

$$
\hat {F} (t) = n ^ {- 1} \sum_ {i = 1} ^ {n} I (\hat {\tau} _ {i} \leq t)
$$

be the empirical distribution of $(\hat{\tau}_1,\dots ,\hat{\tau}_n)$ , and

$$
1 - \hat {F} (- t -) = n ^ {- 1} \sum_ {i = 1} ^ {n} I (- \hat {\tau} _ {i} \leq t)
$$

be the empirical distribution of $-(\hat{\tau}_1, \dots, \hat{\tau}_n)$ , where $\hat{F}(-t-)$ is the left limit of the function $\hat{F}(\cdot)$ at $-t$ . A Kolmogorov-Smirnov-type statistic is then

$$
D = \max  _ {t} | \hat {F} (t) + \hat {F} (- t -) - 1 |.
$$

Butler (1969) proposed this test statistic and derived its exact and asymptotic distributions. Unfortunately, this is not implemented in standard software packages. Nevertheless, we can simulate its exact distribution and compute the $p$ -value based on the FRT.<sup>1</sup>

Example 7.4 (sign statistic) The sign statistic uses only the signs of the within-pair differences

$$
\Delta = \sum_ {i = 1} ^ {n} I (\hat {\tau} _ {i} > 0).
$$

Under $H_{0\mathrm{F}}$

$$
I (\hat {\tau} _ {i} > 0) \stackrel {{\mathrm {I I D}}} {{\sim}} \operatorname {B e r n o u l l i} (1 / 2)
$$

and therefore

$$
\Delta \sim \operatorname {B i n o m i a l} (n, 1 / 2).
$$

Based on this we have an exact Binomial test, which is implemented in the $R$ function binom.test with $p = 1/2$ . Using the CLT, we can also conduct a test based on the following Normal approximation of the Binomial distribution:

$$
\frac {\Delta - n / 2}{\sqrt {n / 4}} \to \mathrm {N} (0, 1)
$$

Therefore, $\hat{F}(t) + \hat{F}(-t-) - 1$ measures the deviation from the null hypothesis of symmetry, which motivates the definition of $D$ in Example 7.3. A naive definition of the Kolmogorov-Smirnov-type statistic is to compare the empirical distributions of the outcomes under treatment and control as in Example 3.4. Using that definition, we effectively break the pairs. Although it can still be used in the FRT for the MPE, it does not capture the matched-pairs structure of the experiment.

TABLE 7.1: Counts of four types of pairs   

<table><tr><td></td><td>control outcome 1</td><td>control outcome 0</td></tr><tr><td>treated outcome 1</td><td>m11</td><td>m10</td></tr><tr><td>treated outcome 0</td><td>m01</td><td>m00</td></tr></table>

in distribution.

Example 7.5 (McNemar's statistic for a binary outcome) If the outcome is binary, we can summarize the observed data from the MPE in a more compact way. Given a pair, the treated outcome can be either 1 or 0 and the control outcome can be either 1 or 0, yielding a two-by-two table as in Table 7.1.

Under $H_{0\mathrm{F}}$ , the numbers of concordant pairs $m_{11}$ and $m_{00}$ are fixed, and $m_{10} + m_{01}$ is also fixed. So the only random component is $m_{10}$ which has distribution

$$
m _ {1 0} \sim \mathrm {B i n o m i a l} (m _ {1 0} + m _ {0 1}, 1 / 2).
$$

This implies an exact test based on the Binomial distribution. The $R$ function mcnemar.test gives an asymptotic test based on the Normal approximation of the Binomial distribution:

$$
\frac {m _ {1 0} - \left(m _ {1 0} + m _ {0 1}\right) / 2}{\sqrt {\left(m _ {1 0} + m _ {0 1}\right) / 4}} = \frac {m _ {1 0} - m _ {0 1}}{\sqrt {m _ {1 0} + m _ {0 1}}} \rightarrow \mathrm {N} (0, 1)
$$

in distribution. Both the exact FRT and the asymptotic test do not depend on $m_{11}$ or $m_{00}$ . Only the numbers of discordant pairs matter in these tests.

# 7.3 Neymanian inference

The average causal effect within pair $i$ is

$$
\tau_ {i} = \frac {1}{2} \left\{Y _ {i 1} (1) + Y _ {i 2} (1) - Y _ {i 1} (0) - Y _ {i 2} (0) \right\},
$$

and the average causal effect for all units is

$$
\tau = n ^ {- 1} \sum_ {i = 1} ^ {n} \tau_ {i} = (2 n) ^ {- 1} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {2} \{Y _ {i j} (1) - Y _ {i j} (0) \}.
$$

It is intuitive that $\hat{\tau}_i$ is unbiased for $\tau_i$ , so $\hat{\tau}$ is unbiased for $\tau$ . We can also calculate the variance of $\hat{\tau}$ . I relegate the exact formula to Problem 7.1 because the MPE is just a special case of the SRE.

However, we cannot follow the strategy under the SRE to estimate the

variance of $\hat{\tau}$ under the MPE. The within-pair sample variances of the outcomes are not well defined because, within each pair, we have only one treated and one control unit. The data do not allow us to estimate the variance of $\hat{\tau}_i$ within pair $i$ .

Is it possible to estimate the variance of $\hat{\tau}$ in the MPE? Let us forget about the MPE and change the perspective to the classic IID sampling. If the $\hat{\tau}_i$ 's are IID with mean $\mu$ and $\sigma^2$ , then the variance of $\hat{\tau} = n^{-1}\sum_{i=1}^{n}\hat{\tau}_i$ is $\sigma^2/n$ . An unbiased estimator for $\sigma^2$ is the sample variance $(n-1)^{-1}\sum_{i=1}^{n}(\hat{\tau}_i - \hat{\tau})^2$ , so an unbiased estimator for $\mathrm{var}(\hat{\tau})$ is

$$
\hat {V} = \left\{n (n - 1) \right\} ^ {- 1} \sum_ {i = 1} ^ {n} \left(\hat {\tau} _ {i} - \hat {\tau}\right) ^ {2}. \tag {7.2}
$$

The discussion also extends to the independent but not IID setting; see Problem A.1 in Chapter A. The above discussion seems a digression from the MPE which has completely different statistical assumptions. But at least it motivates a variance estimator $\hat{V}$ , which uses the between-pair variance of $\hat{\tau}_i$ to estimate the variance of $\hat{\tau}$ . Of course, it is derived under different assumptions. Does it also work for the MPE? Theorem 7.1 below is a positive result.

Theorem 7.1 Under the MPE, $\hat{V}$ defined in (7.2) is a conservative estimator for the true variance of $\hat{\tau}$ :

$$
E (\hat {V}) - \operatorname {v a r} (\hat {\tau}) = \{n (n - 1) \} ^ {- 1} \sum_ {i = 1} ^ {n} (\tau_ {i} - \tau) ^ {2} \geq 0.
$$

If the $\tau_{i}$ 's are constant across pairs, then $E(\hat{V}) = \mathrm{var}(\hat{\tau})$ .

Theorem 7.1 states that under the MPE, $\hat{V}$ is a conservative variance estimator in general and becomes unbiased if the average causal effects are constant across pairs. It is somewhat surprising because $\hat{V}$ depends on the between-pair variance of the $\hat{\tau}_i$ 's whereas $\mathrm{var}(\hat{\tau})$ depends on the within-pair variance of each of $\hat{\tau}_i$ . The proof below might provide some insights into this surprising result.

Proof of Theorem 7.1: Recall the basic algebraic fact that $\sum_{i=1}^{n}(a_i - \bar{a})^2 = \sum_{i=1}^{n}a_i^2 - n\bar{a}^2$ which parallels the fact that $\operatorname{var}(W) = E(W^2) - (EW)^2$ for a

random variable $W$ . Use it in the following steps 2 and 5, we have

$$
\begin{array}{l} n (n - 1) E (\hat {V}) = E \left\{\sum_ {i = 1} ^ {n} (\hat {\tau} _ {i} - \hat {\tau}) ^ {2} \right\} \\ = E \left(\sum_ {i = 1} ^ {n} \hat {\tau} _ {i} ^ {2} - n \hat {\tau} ^ {2}\right) \\ = \sum_ {i = 1} ^ {n} \left\{\operatorname {v a r} \left(\hat {\tau} _ {i}\right) + \tau_ {i} ^ {2} \right\} - n \left\{\operatorname {v a r} \left(\hat {\tau}\right) + \tau^ {2} \right\} \\ = \sum_ {i = 1} ^ {n} \operatorname {v a r} \left(\hat {\tau} _ {i}\right) - n \operatorname {v a r} (\hat {\tau}) + \sum_ {i = 1} ^ {n} \tau_ {i} ^ {2} - n \tau^ {2} \\ = \quad n ^ {2} \operatorname {v a r} (\hat {\tau}) - n \operatorname {v a r} (\hat {\tau}) + \sum_ {i = 1} ^ {n} (\tau_ {i} - \tau) ^ {2}. \\ \end{array}
$$

Therefore,

$$
E (\hat {V}) = \operatorname {v a r} (\hat {\tau}) + \{n (n - 1) \} ^ {- 1} \sum_ {i = 1} ^ {n} \left(\tau_ {i} - \tau\right) ^ {2} \geq \operatorname {v a r} (\hat {\tau}).
$$

Similar to the discussions for other experiments, the Neymanian approach relies on the large-sample approximation:

$$
\frac {\hat {\tau} - \tau}{\sqrt {\operatorname {v a r} (\hat {\tau})}} \to \mathrm {N} (0, 1)
$$

in distribution if $n \to \infty$ and some regularity conditions hold. Due to the over-estimation of the variance, the Wald-type confidence interval

$$
\hat {\tau} \pm z _ {1 - \alpha / 2} \sqrt {\hat {V}}
$$

covers $\tau$ with probability at least $1 - \alpha$ .

Both the point estimator $\hat{\tau}$ and the variance estimator $\hat{V}$ can be conveniently obtained by OLS, as shown in the proposition below.

Proposition 7.1 $\hat{\tau}$ and $\hat{V}$ are identical to the coefficient and variance estimator of the intercept from the OLS fit of the vector $(\hat{\tau}_1, \dots, \hat{\tau}_n)^\top$ on the intercept only.

I leave the proof of Proposition 7.1 as Problem 7.3.

# 7.4 Covariate adjustment

Although we have matched on covariates in the design stage, it is possible that the matching is not perfect ( $X_{i1} \neq X_{i2}$ ) and sometimes we have additional

covariates beyond those used in the pair-matching stage. In those cases, we can adjust for the covariates to further improve estimation efficiency. Assume that each unit $(i,j)$ has covariates $X_{ij}$ . Similar to the discussion in the CRE, there are two general strategies of covariate adjustment in the MPE.

# 7.4.1 FRT

I start with the covariate-adjusted FRT in the MPE. In parallel with Definition 6.2, we can construct test statistics based on the residuals from a model fitting of the outcome on the covariates, since those residuals are fixed numbers under the sharp null hypothesis. A canonical choice is to fit OLS of all observed $Y_{ij}$ 's on $X_{ij}$ 's to obtain the residuals $\hat{\varepsilon}_{ij}$ 's. We can then construct test statistics pretending that the $\hat{\varepsilon}_{ij}$ 's are the observed outcomes. Rosenbaum (2002a) advocated this strategy in particular to the MPE.

In parallel with Definition 6.3, we can directly use some coefficients from model fitting as the test statistics. The discussion in the next subsection will suggest a choice of the test statistic for this strategy.

# 7.4.2 Regression adjustment

I now focus on estimating $\tau$ . We can compute the within-pair differences in covariates $\hat{\tau}_{X,i}$ and their average $\hat{\tau}_X$ in the same way as the outcome. We can show that

$$
E (\hat {\tau} _ {X, i}) = 0, \quad E (\hat {\tau} _ {X}) = 0,
$$

and

$$
\operatorname {c o v} \left(\hat {\tau} _ {X}\right) = n ^ {- 2} \sum_ {i = 1} ^ {n} \hat {\tau} _ {X, i} \hat {\tau} _ {X, i} ^ {\mathsf {T}}.
$$

In a realized MPE, $\operatorname{cov}(\hat{\tau}_X)$ is not zero unless all the $\hat{\tau}_{X,i}$ 's are zero. With an unlucky draw of $(Z_{1},\ldots,Z_{n})$ , it is possible that $\hat{\tau}_X$ differs substantially from zero. Similar to the discussion under the CRE in Chapter 6.2.2.3, adjusting for the imbalance of the covariate means is likely to improve estimation efficiency.

Similar to the discussion in Section 6.2.2.3, we can consider a class of estimators indexed by $\gamma$ :

$$
\hat {\boldsymbol {\tau}} (\gamma) = \hat {\boldsymbol {\tau}} - \boldsymbol {\gamma} ^ {T} \hat {\boldsymbol {\tau}} _ {X}
$$

which has mean 0 for any fixed $\gamma$ . We want to choose $\gamma$ to minimize the variance of $\hat{\tau}(\gamma)$ . Its variance is a quadratic function of $\gamma$ :

$$
\begin{array}{l} \operatorname {v a r} \{\hat {\tau} (\gamma) \} = \operatorname {v a r} (\hat {\tau} - \gamma^ {\mathsf {T}} \hat {\tau} _ {X}) \\ = \operatorname {v a r} (\hat {\tau}) + \gamma^ {\mathsf {T}} \operatorname {c o v} (\hat {\tau} _ {X}) \gamma - 2 \gamma^ {\mathsf {T}} \operatorname {c o v} (\hat {\tau} _ {X}, \hat {\tau}), \\ \end{array}
$$

which is minimized at

$$
\tilde {\gamma} = \operatorname {c o v} (\hat {\tau} _ {X}) ^ {- 1} \operatorname {c o v} (\hat {\tau} _ {X}, \hat {\tau}).
$$

We have obtained the formula for $\operatorname{cov}(\hat{\tau}_X)$ in the above, which can also be written as

$$
\operatorname {c o v} (\hat {\tau} _ {X}) = n ^ {- 2} \sum_ {i = 1} ^ {n} | \hat {\tau} _ {X, i} | | \hat {\tau} _ {X, i} | ^ {\mathsf {T}},
$$

where $|\cdot|$ denotes the component-wise absolute value of a vector. So $\operatorname{cov}(\hat{\tau}_X)$ is fixed and known from the observed data. However, $\operatorname{cov}(\hat{\tau}_X, \hat{\tau})$ depends on unknown potential outcomes. Fortunately, we can obtain an unbiased estimator for it, as shown in Theorem 7.2 below.

Theorem 7.2 An unbiased estimator for $\operatorname{cov}(\hat{\tau}_X, \hat{\tau})$ is

$$
\hat {\theta} = \{n (n - 1) \} ^ {- 1} \sum_ {i = 1} ^ {n} (\hat {\tau} _ {X, i} - \hat {\tau} _ {X}) (\hat {\tau} _ {i} - \hat {\tau}).
$$

The proof of Theorem 7.2 is similar to that of Theorem 7.1. I leave it to Problem 7.2.

Therefore, we can estimate the optimal coefficient $\tilde{\gamma}$ by

$$
\begin{array}{l} \hat {\gamma} = \left(n ^ {- 2} \sum_ {i = 1} ^ {n} \hat {\tau} _ {X, i} \hat {\tau} _ {X, i} ^ {\mathsf {T}}\right) ^ {- 1} \left\{\left\{n (n - 1) \right\} ^ {- 1} \sum_ {i = 1} ^ {n} \left(\hat {\tau} _ {X, i} - \hat {\tau} _ {X}\right) \left(\hat {\tau} _ {i} - \hat {\tau}\right) \right\} \\ \approx \left(\sum_ {i = 1} ^ {n} (\hat {\tau} _ {X, i} - \hat {\tau} _ {X}) (\hat {\tau} _ {X, i} - \hat {\tau} _ {X}) ^ {\mathsf {T}}\right) ^ {- 1} \sum_ {i = 1} ^ {n} (\hat {\tau} _ {X, i} - \hat {\tau} _ {X}) (\hat {\tau} _ {i} - \hat {\tau}), \\ \end{array}
$$

which is approximately the coefficient of the $\hat{\tau}_{X,i}$ in the OLS fit of the $\hat{\tau}_i$ 's on the $\hat{\tau}_{X,i}$ 's with an intercept. The final estimator is

$$
\hat {\tau} _ {\mathrm {a d j}} = \hat {\tau} (\hat {\gamma}) = \hat {\tau} - \hat {\gamma} ^ {\mathsf {T}} \hat {\tau} _ {X},
$$

which, by the property of OLS, is approximately the intercept in the OLS fit of the $\hat{\tau}_i$ 's on the $\hat{\tau}_{X,i}$ 's with an intercept.

A conservative variance estimator for $\hat{\tau}_{\mathrm{adj}}$ is then

$$
\begin{array}{l} \hat {V} _ {\mathrm {a d j}} = \hat {V} + \hat {\gamma} ^ {\mathsf {T}} \mathrm {c o v} (\hat {\tau} _ {X}) \hat {\gamma} - 2 \hat {\gamma} ^ {\mathsf {T}} \hat {\theta} \\ = \hat {V} - \hat {\theta} ^ {\mathsf {T}} \operatorname {c o v} (\hat {\tau} _ {X}) ^ {- 1} \hat {\theta}. \\ \end{array}
$$

A subtle technical issue is whether $\hat{\tau} (\hat{\gamma})$ has the same optimality as $\hat{\tau} (\tilde{\gamma})$ . We have encountered a similar issue in the discussion of Lin (2013)'s estimator. With large samples, we can show $\hat{\tau} (\hat{\gamma}) - \hat{\tau} (\tilde{\gamma}) = -(\hat{\gamma} -\tilde{\gamma})^{\mathrm{T}}\hat{\tau}_{X}$ is of higher order since it is the product of two "small" terms $\hat{\gamma} -\tilde{\gamma}$ and $\hat{\tau}_X$ .

Moreover, Fogarty (2018b) discussed the asymptotically equivalent regression formulation of the above covariate-adjusted procedure and gave a rigorous proof for the associated CLT. I summarize the regression formulation below without giving the regularity conditions.

Proposition 7.2 Under the MPE, the covariate-adjusted estimator $\hat{\tau}_{\mathrm{adj}}$ and the associated variance estimator $\hat{V}_{\mathrm{adj}}$ can be conveniently approximated by the intercept and the associated variance estimator from the OLS fit of the vector of the $\hat{\tau}_i$ 's on the 1's and the matrix of the $\hat{\tau}_{X,i}$ 's.

I leave the proof of Proposition 7.2 as Problem 7.3. Interestingly, neither Proposition 7.1 nor 7.2 requires the EHW correction of the variance estimator. See Fogarty (2018b) for more technical details. Because we reduce the data from the MPE to the within-pair differences, it is unnecessary to center the covariates, which is different from the implementation of Lin (2013)'s estimator under the CRE.

# 7.5 Examples

# 7.5.1 Darwin's data comparing cross-fertilizing and self-fertilizing on the height of corns

This is a classical example from Fisher (1935). It contains 15 pairs of corns with either cross-fertilizing or self-fertilizing, with the height being the outcome. The R package HistData provides the original data, where cross and self are the heights under cross-fertilizing and self-fertilizing, respectively, and diff denotes their difference.

```txt
> library("HistData")  
> ZeaMays  
pair pot cross self diff  
1 1 23.500 17.375 6.125  
2 2 1 12.000 20.375 -8.375  
3 3 1 21.000 20.000 1.000  
4 4 2 22.000 20.000 2.000  
5 5 2 19.125 18.375 0.750  
6 6 2 21.500 18.625 2.875  
7 7 3 22.125 18.625 3.500  
8 8 3 20.375 15.250 5.125  
9 9 3 18.250 16.500 1.750  
10 10 3 21.625 18.000 3.625  
11 11 3 23.250 16.250 7.000  
12 12 4 21.000 18.000 3.000  
13 13 4 22.125 12.750 9.375  
14 14 4 23.000 15.500 7.500  
15 15 4 12.000 18.000 -6.000 
```

In total, the MPE has $2^{15} = 32768$ possible treatment assignment which is a tractable number in $\mathbb{R}$ . The following function can enumerate all possible treatment assignments for the MPE:

# 7.5 Examples

MP enumerate $=$ function(i，n.pairs)   
{ if $(\mathrm{i} > 2^{\wedge}\mathrm{n}.)$ pairs）print("i is too large.") a $= 2^{\wedge}$ ((n.pairs-1):0) b $= 2^{*}\mathbf{a}$ 2*sapply(i-1, function(x) as(integer((x $\% \%$ b>=a))-1

So we enumerate all the treatment assignments and calculate the corresponding $\hat{\tau}$ 's and the one-sided exact $p$ -value.

```txt
> difference = ZeaMays$diff
> n.pairs = length(difference)
> abs.diff = abs(difference)
> t obs = mean(difference)
> t.ran = sapply(1:2^15,
+ function(x) {
+ sum(MP enumerate(x, 15)*abs.diff)
+ })/n.pairs
> pvalue = mean(t.ran >= t(obs)
> pvalue
[1] 0.02633667 
```

![](images/949ff4c732aefd8922f653d8285e13bbe4d775c3f87a74750290ddd9818622e8.jpg)  
Figure 7.1 shows the exact randomization distribution of $\hat{\tau}$ under $H_{0\mathrm{F}}$   
FIGURE 7.1: Exact randomization distribution of $\hat{\tau}$ using Darwin's data

# 7.5.2 Children's television workshop experiment data

I also re-analyze a subset of the data from the Children's Television Workshop experiment from Ball et al. (1973) which was also analyzed by Imbens and Rubin (2015, Chapter 10). It contains 8 pairs of classes, with one of the two classes randomly assigned to be shown The Electric Company show during the standard reading-class period. It contains the pre-test score (covariate) and the post-test score (outcome). The following table summarizes the within-pair covariates and outcomes, as well as their differences:

```txt
> dataxy = c(12.9, 12.0, 54.6, 60.6,
+ 15.1, 12.3, 56.5, 55.5,
+ 16.8, 17.2, 75.2, 84.8,
+ 15.8, 18.9, 75.6, 101.9,
+ 13.9, 15.3, 55.3, 70.6,
+ 14.5, 16.6, 59.3, 78.4,
+ 17.0, 16.0, 87.0, 84.2,
+ 15.8, 20.1, 73.7, 108.6)
> dataxy = matrix(dataxy, 8, 4, byrow = TRUE)
> diffx = dataxy[, 2] - dataxy[, 1]
> diffy = dataxy[, 4] - dataxy[, 3]
> dataxy = cbind(dataxy, diffx, diffy)
> rownames(dataxy) = 1:8
> colnames(dataxy) = c("x.control", "x.treatment",
+ "y.control", "y.treatment",
+ "diffx", "diffy")
> dataxy = as.data.frame(dataxy)
> dataxy
x.control x.treatment y.control y.treatment diffx
1 12.9 12.0 54.6 60.6 -0.9 6.0
2 15.1 12.3 56.5 55.5 -2.8 -1.0
3 16.8 17.2 75.2 84.8 0.4 9.6
4 15.8 18.9 75.6 101.9 3.1 26.3
5 13.9 15.3 55.3 70.6 1.4 15.3
6 14.5 16.6 59.3 78.4 2.1 19.1
7 17.0 16.0 87.0 84.2 -1.0 -2.8
8 15.8 20.1 73.7 108.6 4.3 34.9 
```

The following $\mathbb{R}$ code calculates $\hat{\tau}$ and $\hat{V}$ .

```txt
> n = dim(dataaxy)[1]
> tauhat = mean(dataaxy[, "diffy")]>
> what = var(dataaxy[, "diffy"]), n
> tauhat
[1] 13.425
> sqrt(vhat)
[1] 4.636337 
```

By Propositions 7.1 and 7.2, we can use the OLS to obtain the point estimators and standard errors. Adjusting for covariates, we have

# 7.6 Examples

```txt
> unadj = summary(lm(diffy ~ 1, data = dataxy)) $coef
> round(unadj, 3)
Estimate Std. Error t value Pr(>|t|)
(Intercept) 13.425 4.636 2.896 0.023 
```

Adjusting for covariates, we have

```txt
> adj = summary(lm(diffy ~ diffx, data = dataxy))$coef
> round(adj, 3)
Estimate Std. Error t value Pr(>|t|)
(Intercept) 8.994 1.410 6.381 0.001
diffx 5.371 0.599 8.964 0.000 
```

The above results assume large $n$ , and $p$ -values are justified if we believe the large- $n$ approximation. However, $n = 8$ is not large. In total, we have $2^8 = 256$ possible treatment assignments, so the smallest possible $p$ -value is $1 / 256 = 0.0039$ , which is much larger than the $p$ -value based on the Normal approximation of the covariate-adjusted estimator. In this example, it will be more reasonable to use the FRT with the studentized statistic, which is the $t$ value from the $1\text{m}$ function, to calculate exact $p$ -values<sup>2</sup>. The following R code calculates the $p$ -values based on two $t$ -statistics.

```diff
> t.ran = sapply(1:2^8, function(x){  
+ z.mpe = MP enumerate(x, 8)  
+ diffy.mpe = diffy*z.mpe  
+ diffx.mpe = diffx*z.mpe  
+ c.summary(1m(diffy.mpe ~ 1))$coef[1, 3],  
+ summary(1m(diffy.mpe ~ diffx.mpe))$coef[1, 3])  
+ })  
> p.unadj = mean(abs(t.ran[1, ]) >= abs(unadj[1, 3]))  
> p.unadj  
[1] 0.03125  
> p.adj = mean(abs(t.ran[2, ]) >= abs(adj[1, 3]))  
> p.adj  
[1] 0.0078125 
```

Figure 7.2 shows the exact distributions of the two studentized statistics, as well as the two-sided $p$ -values. The figure highlights the fact that the randomization distributions of the test statistics are discrete, taking at most 256 possible values. The Normal approximations are unlikely to be accurate, especially at the tails. We should report the $p$ -values based on the FRT.

![](images/a9ecbc4419d21d1955270f18cc494e953a9f78da7e8606739e44d043a8254c54.jpg)

![](images/f22baa9a63eafe1bf7e0e915f04edd936954c04efaa357699c4be90e190f6fe0.jpg)  
FIGURE 7.2: Exact randomization distributions of the studentized statistics in Section 7.5.2

# 7.6 Comparing the MPE and CRE

Imai (2008b) compared the MPE and CRE. Heuristically, the conclusion is that the MPE gives more precise estimators if the matching is well done and the covariates are predictive of the outcome. However, without the outcome data in the design stage, it is hard to decide whether this is true or not. In the FRT, if covariates are predictive of the outcome, the MPE usually gives more powerful tests compared with the CRE. Greevy et al. (2004) illustrated this using simulation based on the Wilcoxon sign-rank statistic. However, this can be a subtle issue with finite samples. Consider an experiment with $2n$ units, with $n$ units receiving the treatment and $n$ units receiving the control. If we test the sharp null hypothesis at level 0.05, then in the MPE, we need at least $2 \times 5 = 10$ units since the smallest $p$ -value is $1/2^5 = 1/32 < 0.05$ but $1/2^4 = 1/16 > 0.05$ , but in the CRE, we need at least $2 \times 4 = 8$ units since the smallest $p$ -value is $1/\binom{8}{4} = 1/70 < 0.05$ but $1/\binom{6}{3} = 1/20 = 0.05$ . So with 8 units, it is impossible to reject the sharp null hypothesis in the MPE but it is possible in the CRE. Even if the covariates are perfect predictors of the outcome, the MPE is not superior to the CRE based on the FRT.

# 7.7 Extension to the general matched experiment

It is straightforward to extend the MPE to the general matched experiment with varying numbers of control units. Assume that we have $n$ matched sets indexed by $i = 1, \ldots, n$ . For the matched set $i$ , we have $1 + M_i$ units. The $M_i$ 's can vary. The total number of experimental units is $N = n + \sum_{i=1}^{n} M_i$ . Let $ij$ index the unit $j$ within matched set $i$ ( $i = 1, \ldots, n$ and $j = 1, \ldots, M_i + 1$ ). Unit $ij$ has potential outcomes $Y_{ij}(1)$ and $Y_{ij}(0)$ under the treatment and control, respectively.

Within the matched set $i$ ( $i = 1, \dots, n$ ), the experimenter randomly selects exactly one unit to receive the treatment with the rest $M_i$ units receiving the control. This general matched experiment is also a special case of the SRE with $n$ strata of size $1 + M_i$ ( $i = 1, \dots, n$ ). Let $Z_{ij}$ be the treatment indicator for unit $ij$ , which reveals one of the potential outcomes as

$$
Y _ {i j} = Z _ {i j} Y _ {i j} (1) + (1 - Z _ {i j}) Y _ {i j} (0).
$$

The average causal effect within the matched set $i$ equals

$$
\tau_ {i} = (M _ {i} + 1) ^ {- 1} \sum_ {j = 1} ^ {1 + M _ {i}} \{Y _ {i j} (1) - Y _ {i j} (0) \}.
$$

Since the general matched experiment is a SRE, an unbiased estimator of $\tau_{i}$ is

$$
\hat {\tau} _ {i} = \sum_ {j = 1} ^ {M _ {i} + 1} Z _ {i j} Y _ {i j} - M _ {i} ^ {- 1} \sum_ {j = 1} ^ {M _ {i} + 1} (1 - Z _ {i j}) Y _ {i j}
$$

which is the difference in means of the outcomes within matched set $i$ .

Below we discuss the statistical inference with the general matched experiment.

# 7.7.1 FRT

As usual, we can always use the FRT to test the sharp null hypothesis

$$
H _ {0 \mathrm {F}}: Y _ {i j} (1) = Y _ {i j} (0) \text {f o r a l l} i = 1, \dots , n; j = 1, \dots , M _ {i} + 1.
$$

Because the general matched experiment is a special case of the SRE with many small strata, we can use the test statistics defined in Examples 5.4, 5.5, 7.2, 7.3, 7.4, as well as the estimators and the corresponding $t$ -statistics from the following two subsections.

# 7.7.2 Estimating the average of the within-strata effects

We first focus on estimating the average of the within-strata effects:

$$
\tau = n ^ {- 1} \sum_ {i = 1} ^ {n} \tau_ {i}.
$$

It has an unbiased estimator

$$
\hat {\tau} = n ^ {- 1} \sum_ {i = 1} ^ {n} \hat {\tau} _ {i}.
$$

Interestingly, we can show that Theorem 7.1 holds for the general matched experiment, and so are other results for the MPE. In particular, we can use the OLS fit of the $\hat{\tau}_i$ 's on the intercept to obtain the point and variance estimators for $\tau$ . With covariates, we can use the OLS fit of the $\hat{\tau}_i$ 's on the intercept and the $\hat{\tau}_{X,i}$ 's, where

$$
\hat {\tau} _ {X, i} = \sum_ {j = 1} ^ {M _ {i} + 1} Z _ {i j} X _ {i j} - M _ {i} ^ {- 1} \sum_ {j = 1} ^ {M _ {i} + 1} (1 - Z _ {i j}) X _ {i j}
$$

is the corresponding difference in means of the covariates within matched set $i$ .

# 7.7.3 A more general causal estimand

Importantly, the $\tau$ above is the average of the $\tau_{i}$ 's, which does not equal the average causal effect for the $N$ units in the experiment when the $M_{i}$ 's vary. The average causal effect equals

$$
\tau^ {\prime} = N ^ {- 1} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {1 + M _ {i}} \left\{Y _ {i j} (1) - Y _ {i j} (0) \right\} = \sum_ {i = 1} ^ {n} \frac {1 + M _ {i}}{N} \tau_ {i}.
$$

To unify the discussion, I consider the weighted causal effect

$$
\tau_ {w} = \sum_ {i = 1} ^ {n} w _ {i} \tau_ {i}
$$

with $\sum_{i=1}^{n} w_i = 1$ , which includes $\tau$ as a special case with $w_i = n^{-1}$ and $\tau'$ as a special case with $w_i = (1 + M_i) / N$ for $i = 1, \ldots, n$ . It is straightforward to obtain an unbiased estimator

$$
\hat {\tau} _ {w} = \sum_ {i = 1} ^ {n} w _ {i} \hat {\tau} _ {i},
$$

and calculate its variance

$$
\operatorname {v a r} (\hat {\tau} _ {w}) = \sum_ {i = 1} ^ {n} w _ {i} ^ {2} \operatorname {v a r} (\hat {\tau} _ {i}).
$$

However, estimating the variance of $\hat{\tau}_w$ is quite tricky because the $\hat{\tau}_i$ 's are independent random variables without any replicates. This is a famous problem in theoretical statistics studied by Hartley et al. (1969) and Rao (1970). Fogarty (2018a) also discussed this problem without recognizing these previous works. I will give the final form of the variance estimator without detailing the motivation:

$$
\hat {V} _ {w} = \sum_ {i = 1} ^ {n} c _ {i} (\hat {\tau} _ {i} - \hat {\tau} _ {w}) ^ {2}
$$

where

$$
c _ {i} = \frac {\frac {w _ {i} ^ {2}}{1 - 2 w _ {i}}}{1 + \sum_ {i = 1} ^ {n} \frac {w _ {i} ^ {2}}{1 - 2 w _ {i}}}.
$$

As a sanity check, $c_{i}$ reduces to $\{n(n - 1)\}^{-1}$ in the MPE with $M_{i} = 1$ and $w_{i} = n^{-1}$ . For simplicity, we focus on the case with $w_{i} < 1 / 2$ for all $i$ 's, that is, there is no matched set containing more than half of the total weights. The following theorem extends Theorem 7.1.

Theorem 7.3 Under the general matched experiment with varying $M_{i}$ 's, if $w_{i} < 1/2$ for all $i$ 's, then

$$
E (\hat {V} _ {w}) - \operatorname {v a r} (\hat {\tau} _ {w}) = \sum_ {i = 1} ^ {n} c _ {i} (\tau_ {i} - \tau_ {w}) ^ {2} \geq \operatorname {v a r} (\hat {\tau} _ {w}) \geq 0
$$

with equality holding if the $\tau_{i}$ 's are constant.

Although the theoretical motivation for $\hat{V}_w$ is quite complicated, it is not too difficult to verify Theorem 7.3 directly. I relegate the proof to Problem 7.9.

# 7.8 Homework Problems

# 7.1 The true variance of $\hat{\tau}$ in the MPE

Express $\operatorname{var}(\hat{\tau})$ in terms of the finite-population variances of the potential outcomes.

# 7.2 A covariance estimator

Prove Theorem 7.2.

# 7.3 Variance estimators via OLS

Prove Propositions 7.1 and 7.2.

# 7.4 Point and variance estimator with binary outcome

This problem extends Example 7.5 to Neymanian inference.

Express $\hat{\tau}$ and $\hat{V}$ in terms of the counts in Table 7.1.

# 7.5 Minimum sample size for the FRT

Extend the discussion in Section 7.6. Consider an experiment with $2n$ units, with $n$ units receiving the treatment and $n$ units receiving the control, and test the sharp null hypothesis at level 0.001. What is the minimum value of $n$ for an MPE so that the smallest $p$ -value does not exceed than 0.001, and what is the corresponding minimum value of $n$ for a CRE?

# 7.6 Re-analyzing Darwin's data

Chapter 7.5.1 analyzed Darwin's data using the FRT based on the test statistic $\hat{\tau}$ .

Re-analyze this dataset using the FRT with the Wilcoxon sign-rank statistic.

Re-analyze this dataset based on the Neymanian inference: report the unbiased point estimator, conservative variance estimator, and $95\%$ confidence interval.

# 7.7 Re-analyzing children's television workshop experiment data

Chapter 7.5.2 analyzed the data from based on Neymanian inference.

Re-analyze this dataset using the FRT with different test statistics.

Re-analyze this dataset using the FRT with covariate adjustment.

# 7.8 Re-analyzing Angrist and Lavy (2009)'s data

The original analysis of Angrist and Lavy (2009)' was quite complicated. For this problem, please focus only on Table A1 of the original paper and view the schools as the experimental units. Angrist and Lavy (2009) essentially conducted an MPE on the schools. Dropping pair 6 and all the pairs with noncompliance results in 14 complete pairs, with data shown below and also in AL2009.csv:

<table><tr><td></td><td>pair</td><td>z</td><td>pr99</td><td>pr00</td><td>pr01</td><td>pr02</td></tr><tr><td>1</td><td>1</td><td>0</td><td>0.046</td><td>0.000</td><td>0.091</td><td>0.185</td></tr><tr><td>2</td><td>1</td><td>1</td><td>0.036</td><td>0.051</td><td>0.000</td><td>0.047</td></tr><tr><td>3</td><td>2</td><td>0</td><td>0.054</td><td>0.094</td><td>0.184</td><td>0.034</td></tr><tr><td>4</td><td>2</td><td>1</td><td>0.050</td><td>0.108</td><td>0.110</td><td>0.095</td></tr><tr><td>5</td><td>3</td><td>0</td><td>0.114</td><td>0.000</td><td>0.056</td><td>0.075</td></tr><tr><td>6</td><td>3</td><td>1</td><td>0.098</td><td>0.054</td><td>0.030</td><td>0.068</td></tr></table>

# 7.8 Homework Problems

<table><tr><td>7</td><td>4</td><td>0</td><td>0.148</td><td>0.162</td><td>0.082</td><td>0.075</td></tr><tr><td>8</td><td>4</td><td>1</td><td>0.134</td><td>0.390</td><td>0.339</td><td>0.458</td></tr><tr><td>9</td><td>5</td><td>0</td><td>0.152</td><td>0.105</td><td>0.083</td><td>0.129</td></tr><tr><td>10</td><td>5</td><td>1</td><td>0.145</td><td>0.077</td><td>0.579</td><td>0.167</td></tr><tr><td>11</td><td>6</td><td>0</td><td>0.188</td><td>0.214</td><td>0.375</td><td>0.545</td></tr><tr><td>12</td><td>6</td><td>1</td><td>0.179</td><td>0.165</td><td>0.483</td><td>0.444</td></tr><tr><td>13</td><td>7</td><td>0</td><td>0.193</td><td>0.771</td><td>0.328</td><td>0.583</td></tr><tr><td>14</td><td>7</td><td>1</td><td>0.189</td><td>0.186</td><td>0.168</td><td>0.368</td></tr><tr><td>15</td><td>8</td><td>0</td><td>0.197</td><td>0.350</td><td>0.000</td><td>0.383</td></tr><tr><td>16</td><td>8</td><td>1</td><td>0.200</td><td>0.071</td><td>0.667</td><td>0.429</td></tr><tr><td>17</td><td>9</td><td>0</td><td>0.213</td><td>0.176</td><td>0.164</td><td>0.172</td></tr><tr><td>18</td><td>9</td><td>1</td><td>0.209</td><td>0.165</td><td>0.092</td><td>0.151</td></tr><tr><td>19</td><td>10</td><td>0</td><td>0.211</td><td>0.667</td><td>0.250</td><td>0.617</td></tr><tr><td>20</td><td>10</td><td>1</td><td>0.219</td><td>0.250</td><td>0.500</td><td>0.350</td></tr><tr><td>21</td><td>11</td><td>0</td><td>0.219</td><td>0.153</td><td>0.185</td><td>0.219</td></tr><tr><td>22</td><td>11</td><td>1</td><td>0.224</td><td>0.363</td><td>0.372</td><td>0.342</td></tr><tr><td>23</td><td>12</td><td>0</td><td>0.255</td><td>0.226</td><td>0.213</td><td>0.327</td></tr><tr><td>24</td><td>12</td><td>1</td><td>0.257</td><td>0.098</td><td>0.107</td><td>0.095</td></tr><tr><td>25</td><td>13</td><td>0</td><td>0.261</td><td>0.071</td><td>0.000</td><td>NA</td></tr><tr><td>26</td><td>13</td><td>1</td><td>0.263</td><td>0.441</td><td>0.448</td><td>0.435</td></tr><tr><td>27</td><td>14</td><td>0</td><td>0.286</td><td>0.161</td><td>0.126</td><td>0.181</td></tr><tr><td>28</td><td>14</td><td>1</td><td>0.285</td><td>0.389</td><td>0.353</td><td>0.309</td></tr></table>

The outcomes are the Bagrut passing rates in the years 2001 and 2002, with the Bagrut passing rates in 1999 and 2000 as pretreatment covariates. Re-analyze the data based on the Neymanian inference with and without covariates. In particular, how do you deal with the missing outcome in pair 25?

# 7.9 Variance estimation in the general matched experiment

This problem contains more details for Section 7.7.

First, prove Theorem 7.1 for the general matched experiment. Second, prove Theorem 7.3.

Remark: For the second part, we can first verify that $\hat{\tau}_i - \hat{\tau}_w$ has mean $\tau_i - \tau_w$ and variance

$$
\operatorname {v a r} \left(\hat {\tau} _ {i} - \hat {\tau} _ {w}\right) = \operatorname {v a r} \left(\hat {\tau} _ {w}\right) + (1 - 2 w _ {i}) \operatorname {v a r} \left(\hat {\tau} _ {i}\right).
$$

# 7.10 Recommended readings

Greevy et al. (2004) provided an algorithm to form matched pairs based on covariates. Imai (2008b) discussed the estimation of the average causal effect without covariates, and Fogarty (2018b) discussed covariate adjustment in MPEs.

# Unification of the Fisherian and Neymanian Inferences in Randomized Experiments

Chapters 3-7 cover both the Fisherian and Neymanian inferences for different types of experiments. The Fisherian perspective focuses on the finite-sample exact $p$ -values for testing the strong null hypothesis of no causal effects for any units whatsoever, whereas the Neymanian perspective focuses on unbiased estimation with a conservative large-sample confidence interval for the average causal effect. Both of them are justified by the physical randomization which is ensured by the design of the experiments. Because of this, they are both called randomization-based inference or design-based inference. Because they concern a finite population of units in the experiments, they are also called finite-population inference. They are related but also have distinct features.

In 1935, Neyman presented his seminal paper on randomization-based inference to the Royal Statistical Society. His paper (Neyman, 1935) was attacked by Fisher in the discussion session. Sabbaghi and Rubin (2014) reviewed this famous Neyman-Fisher controversy and presented some new results for this old problem. Instead of going to the philosophical issues, this chapter tries to provide a unified discussion.

# 8.1 Testing strong and weak null hypotheses in the CRE

Let us revisit the treatment-control CRE. The Fisherian perspective focuses on testing the strong null hypothesis

$$
H _ {0 \mathrm {F}}: Y _ {i} (1) = Y _ {i} (0) \text {f o r a l l u n i t s} i = 1, \dots , n.
$$

The FRT delivers a finite-sample exact $p_{\mathrm{FRT}}$ defined in (3.2).

By duality of the confidence interval and hypothesis testing, the Neymanian perspective gives a test for the weak null hypothesis

$$
H _ {0 \mathrm {N}}: \tau = 0 \Longleftrightarrow H _ {0 \mathrm {N}}: \bar {Y} (1) = \bar {Y} (0)
$$

based on

$$
t = \frac {\hat {\tau}}{\sqrt {\hat {V}}}.
$$

By the CLT of $\hat{\tau}$ and the conservativeness of the variance estimator, we have

$$
t = \sqrt {\frac {\mathrm {v a r} (\hat {\tau})}{\hat {V}}} \times \frac {\hat {\tau}}{\sqrt {\mathrm {v a r} (\hat {\tau})}} \to C \times \mathrm {N} (0, 1)
$$

in distribution, where $C$ is smaller than or equal to 1 but depends on the unknown potential outcomes. Using $\mathrm{N}(0,1)$ quantiles for the studentized statistic $t$ , we have a conservative large-sample test for $H_{0\mathrm{N}}$ .

Furthermore, Ding and Dasgupta (2017) show that the FRT with the studentized statistic $t$ has the dual guarantees:

1. $p_{\mathrm{FRT}}$ is finite-sample exact under $H_{0\mathrm{F}}$   
2. $p_{\mathrm{FRT}}$ is asymptotically conservative under $H_{0\mathrm{N}}$ .

Importantly, this is a feature of the studentized statistic $t$ . Ding and Das-gupta (2017) showed that the FRT with other test statistics may not have the dual guarantees. In particular, the FRT with $\hat{\tau}$ may be asymptotically anti-conservative under $H_{0\mathrm{N}}$ . I give some heuristics below to illustrate the importance of studentization in the FRT.

Under $H_{0\mathrm{N}}$ , we have

$$
\hat {\tau} \dot {\sim} \mathrm {N} \left(0, \frac {S ^ {2} (1)}{n _ {1}} + \frac {S ^ {2} (0)}{n _ {0}} - \frac {S ^ {2} (\tau)}{n}\right).
$$

The FRT pretends that the Science Table is $(Y_{i},Y_{i})_{i = 1}^{n}$ induced by $H_{0\mathrm{F}}$ , so the randomization distribution of $\hat{\tau}$ is

$$
(\hat {\tau}) ^ {\pi} \stackrel {\cdot} {\sim} \mathrm {N} \left(0, \frac {s ^ {2}}{n _ {1}} + \frac {s ^ {2}}{n _ {0}}\right),
$$

where $(\cdot)^{\pi}$ denotes the randomization distribution<sup>1</sup> and $s^2$ is the sample variance of the observed outcomes. Based on (3.7) in Chapter 3, we can approximate the asymptotic variance of $(\hat{\tau})^{\pi}$ under $H_{0\mathrm{F}}$ as

$$
\begin{array}{l} \frac {s ^ {2}}{n _ {1}} + \frac {s ^ {2}}{n _ {0}} = \frac {n}{n _ {1} n _ {0}} \left\{\frac {n _ {1} - 1}{n - 1} \hat {S} ^ {2} (1) + \frac {n _ {0} - 1}{n - 1} \hat {S} ^ {2} (0) + \frac {n _ {1} n _ {0}}{n (n - 1)} \hat {\tau} ^ {2} \right\} \\ \approx \frac {\hat {S} ^ {2} (1)}{n _ {0}} + \frac {\hat {S} ^ {2} (0)}{n _ {1}} \\ \approx \frac {S ^ {2} (1)}{n _ {0}} + \frac {S ^ {2} (0)}{n _ {1}}, \\ \end{array}
$$

which does not match the asymptotic variance of $\hat{\tau}$ . Ideally, we should compute the $p$ -value under $H_{0\mathrm{N}}$ based on the true distribution of $\hat{\tau}$ , which, however, depends on the unknown potential outcomes. In contrast, we use the FRT to compute the $p_{\mathrm{FRT}}$ based on the permutation distribution $(\hat{\tau})^{\pi}$ , which does not

match the true distribution of $\hat{\tau}$ under $H_{0\mathrm{N}}$ even with large samples. Therefore, the FRT with $\hat{\tau}$ may not control the type one error rate under $H_{0\mathrm{N}}$ even with large samples.

Fortunately, the undesired property of the FRT with $\hat{\tau}$ goes away if we replace the test statistic $\hat{\tau}$ with the studentized version $t$ . Under $H_{0\mathrm{N}}$ , we have

$$
t \dot {\sim} \mathrm {N} (0, C ^ {2})
$$

where $C^2 \leq 1$ with equality holding if $Y_{i}(1) - Y_{i}(0) = \tau$ for all units $i = 1, \ldots, n$ . The FRT pretends that $Y_{i}(1) = Y_{i}(0) = Y_{i}$ for all $i$ 's and generates the permutation distribution

$$
t ^ {\pi} \stackrel {\cdot} {\sim} \mathrm {N} (0, 1)
$$

where the variance equals 1 because the Science Table used by the FRT has zero individual causal effects. Under $H_{0\mathrm{N}}$ , because the true distribution of $t$ is more dispersed than the corresponding permutation distribution, the $p_{\mathrm{FRT}}$ based on $t$ is asymptotically conservative.

# 8.2 Covariate-adjusted FRTs in the CRE

Extending the discussion in Section 8.1 to the case with covariates, Zhao and Ding (2021a) recommend using the FRT with the studentized Lin (2013)'s estimator:

$$
t _ {\mathrm {L}} = \frac {\hat {\tau} _ {\mathrm {L}}}{\sqrt {\hat {V} _ {\mathrm {L}}}},
$$

which is the robust $t$ -statistic for the coefficient of $Z_{i}$ in the OLS fit of $Y_{i}$ on $(1, Z_{i}, X_{i}, Z_{i}X_{i})$ . They show that the FRT with $t_{\mathrm{L}}$ has multiple guarantees:

1. $p_{\mathrm{FRT}}$ is finite-sample exact under $H_{0\mathrm{F}}$   
2. $p_{\mathrm{FRT}}$ is asymptotically conservative under $H_{0\mathrm{N}}$   
3. $p_{\mathrm{FRT}}$ is asymptotically more powerful than the FRT with $t$ when $H_{0\mathrm{N}}$ does not hold and the covariates are predictive to the outcomes;   
4. the above properties hold even when the linear outcome model is misspecified.

Similarly, this is a feature of the studentized statistic $t_{\mathrm{L}}$ . Zhao and Ding (2021a) show that other covariate-adjusted FRTs reviewed in Section 6.2.1 may be either anti-conservative under $H_{0\mathrm{N}}$ or less powerful than the FRT with $t_{\mathrm{L}}$ when $H_{0\mathrm{N}}$ does not hold.

# 8.3 A simulation study

Now I use simulation to evaluate the finite-sample properties of the $p_{\mathrm{FRT}}$ 's under the weak null hypothesis. I will use the following twelve test statistics.

1. The first three test statistics are from the OLS implementation of Neyman (1923), including the coefficient of the treatment, the $t$ -statistic based on the classic standard error, and the $t$ -statistic based on the EHW standard error.   
2. The next three test statistics are based on the pseudo-outcome strategy in Definition 6.2, advocated by Rosenbaum (2002a). We first residualize the outcomes by regressing $Y_{i}$ on $(1,X_{i})$ , and then obtain the three test statistics similar to the first three.   
3. The next three test statistics are based on the OLS implementation of Fisher (1925), as discussed in Chapter 6.2.2.   
4. The final three test statistics are based on the OLS implementation of Lin (2013), as discussed in Chapter 6.2.2.

Consider a finite population of $n = 100$ units subjected to a CRE of size $(n_{1}, n_{0}) = (20, 80)$ . For each $i$ , we draw a univariate covariate $X_{i}$ from $\mathrm{Unif}(-1, 1)$ and generate potential outcomes as $Y_{i}(1) \sim \mathrm{N}(X_{i}^{3}, 1)$ and $Y_{i}(0) \sim \mathrm{N}(-X_{i}^{3}, 0.5^{2})$ . Center the $Y_{i}(1)$ 's and $Y_{i}(0)$ 's to ensure $\tau = 0$ . Fix $\{Y_{i}(1), Y_{i}(0), X_{i}\}_{i=1}^{n}$ in simulation. We draw a random permutation of $n_{1}$ 1's and $n_{0}$ 0's to obtain the observed outcomes and conduct FRTs. The procedure is repeated 500 times, with the $p$ -values approximated by 500 independent permutations of the treatment vector in each replication.

Figure 8.1 shows the $p$ -values under the weak null hypothesis. The four robust $t$ -statistics, as shown in the last row, are the only ones that preserve the correct type one error rates. In fact, they are conservative, which is coherent with the theory. All the other eight statistics yield type one error rates greater than the nominal levels and are thus not proper for testing the weak null hypothesis.

# 8.4 General recommendations

The recommendations for the SRE parallel those for the CRE if both the strong and weak null hypotheses are of interest. Recall the estimators in Chapters 5 and 6.2.4. Without additional covariates, Zhao and Ding (2021a)

![](images/bf7a86c5260cfb446a5e4cc2b15c0b9297f079d57cdd31c69ec510ca729d9e61.jpg)  
FIGURE 8.1: Histograms of $p_{\mathrm{FRT}}$ under the weak null hypothesis

recommend using the FRT with

$$
t _ {\mathrm {S}} = \frac {\hat {\tau} _ {\mathrm {S}}}{\sqrt {\hat {V} _ {\mathrm {S}}}};
$$

with additional covariates, they recommend using the FRT with

$$
t _ {\mathrm {L , S}} = \frac {\hat {\tau} _ {\mathrm {L , S}}}{\sqrt {\hat {V} _ {\mathrm {L , S}}}}.
$$

The analysis of ReM is trickier. Zhao and Ding (2021a) show that the FRT with $t$ does not have the dual guarantees in Section 8.1, but the FRT with $t_{\mathrm{L}}$ still has the guarantees in Section 8.2. This highlights the importance of both covariate adjustment and studentization in ReM.

Similar results hold for the MPE. Without covariates, we recommend using the FRT with the $t$ -statistic for the intercept in the OLS fit of $\hat{\tau}_i$ on 1; with covariates, we recommend using the FRT with the $t$ -statistic for the intercept in the OLS fit of $\hat{\tau}_i$ on 1 and $\hat{\tau}_{X,i}$ . Figure 7.2 in Chapter 7 are based on these recommended FRTs.

Overall, the FRTs with studentized statistics are safer choices. When the large-sample Normal approximations to the studentized statistics are accurate, the $p_{\mathrm{FRT}}$ 's are almost identical to the $p$ -values based on Normal approximations. When the large-sample approximations are inaccurate, the FRTs at least guarantee valid $p$ -values under the strong null hypotheses. This is the recommendation of this book.

# 8.5 A case study

Recall the SRE in Chong et al. (2016) analyzed in Chapter 5.4.2. I compare the "soccer" arm versus the "control" arm and the "physician" arm versus the "control" arm. We also compare the FRTs with and without using the covariate indicating the baseline anemia status. We use their dataset to illustrate the FRTs in the CRE and SRE. The ten subgroup analyses within the same class levels use the FRTs with $t$ and $t_{\mathrm{L}}$ for the CRE and the two overall analyses averaging over all class levels use the FRTs with $t_{\mathrm{S}}$ and $t_{\mathrm{L,S}}$ for the SRE.

Table 8.1 shows the point estimators, standard errors, the $p$ -value based on the Normal approximation of the robust $t$ -statistics, and the $p$ -value based on the FRTs. In most strata, covariate adjustment decreases the standard error since the baseline anemia status is predictive of the outcome. Table 8.1 also exhibits two exceptions: within class 2, covariate adjustment increases the standard error when comparing "soccer" and "control"; in class 4, covariate adjustment increases the standard error when comparing "physician" and

"control". This is due to the small group sizes within these strata, causing the asymptotic approximation inaccurate. Nevertheless, in these two scenarios, the differences in the standard error are in the third digit. The $p$ -values from the Normal approximation and the FRT are close with the latter being slightly larger in most cases. Based on the theory, the $p$ -values based on the FRT should be trusted since it has an additional guarantee of being finite-sample exact under the sharp null hypothesis. This becomes important in this example since the group sizes are quite small within strata.

Figure 8.2 compares the histograms of the randomization distributions of the robust $t$ -statistics with the asymptotic approximations. In the subgroup analysis, we can observe discrepancies between the randomization distributions and $\mathrm{N}(0,1)$ ; averaged over all class levels, the discrepancy becomes unnoticeable. Overall, in this application, the $p$ -values based on the Normal approximation do not differ substantially from those based on the FRTs. Two approaches yield coherent conclusions: the video with a physician telling the benefits of iron supplements improved academic performance and the effect was most significant among students in class 3; in contrast, the video with a famous soccer player telling the benefits of the iron supplements did not have any significant effect.

# 8.6 Homework Problems

# 8.1 Re-analyzing Angrist and Lavy (2009)'s data

This is the Fisherian counterpart of Problem 7.8. Report the $p_{\mathrm{FRT}}$ 's from the FRTs with studentized statistics.

# 8.2 Replication of Zhao and Ding (2021a)'s Figure 1

Zhao and Ding (2021a) use simulation to evaluate the finite-sample properties of the $p_{\mathrm{FRT}}$ 's from the FRTs with various test statistics. Based on their Figure 1, they recommend using the FRT with $t_{\mathrm{L,S}}$ to analyze the SRE. Replicate their Figure 1.

# 8.3 Recommended readings

Using the studentized statistics in permutation tests is not a new idea; see Janssen (1997) and Chung and Romano (2013). Under the design-based framework, Ding and Dasgupta (2017) and Wu and Ding (2021) made the recommendation for multiarmed experiments, and Zhao and Ding (2021a) extended the recommendation to covariate adjustment.

TABLE 8.1: Re-analyzing Chong et al. (2016)'s data. "N" corresponds to the unadjusted estimators and tests due to Neyman (1923), and "L" corresponds to the covariate-adjusted estimators and tests due to Lin (2013).   
(a) soccer versus control   
(b) physician versus control   

<table><tr><td></td><td>est</td><td>s.e.</td><td>pNormal</td><td>pFRT</td></tr><tr><td>class 1</td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>0.051</td><td>0.502</td><td>0.919</td><td>0.924</td></tr><tr><td>L</td><td>0.050</td><td>0.489</td><td>0.919</td><td>0.929</td></tr><tr><td>class 2</td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>-0.158</td><td>0.451</td><td>0.726</td><td>0.722</td></tr><tr><td>L</td><td>-0.176</td><td>0.452</td><td>0.698</td><td>0.700</td></tr><tr><td>class 3</td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>0.005</td><td>0.403</td><td>0.990</td><td>0.989</td></tr><tr><td>L</td><td>-0.096</td><td>0.385</td><td>0.803</td><td>0.806</td></tr><tr><td>class 4</td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>-0.492</td><td>0.447</td><td>0.271</td><td>0.288</td></tr><tr><td>L</td><td>-0.511</td><td>0.447</td><td>0.253</td><td>0.283</td></tr><tr><td>class 5</td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>0.390</td><td>0.369</td><td>0.291</td><td>0.314</td></tr><tr><td>L</td><td>0.443</td><td>0.318</td><td>0.164</td><td>0.186</td></tr><tr><td>all</td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>-0.051</td><td>0.204</td><td>0.802</td><td>0.800</td></tr><tr><td>L</td><td>-0.074</td><td>0.200</td><td>0.712</td><td>0.712</td></tr></table>

<table><tr><td></td><td>est</td><td>s.e.</td><td>pNormal</td><td>pFRT</td></tr><tr><td>class 1</td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>0.567</td><td>0.426</td><td>0.183</td><td>0.192</td></tr><tr><td>L</td><td>0.588</td><td>0.418</td><td>0.160</td><td>0.174</td></tr><tr><td>class 2</td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>0.193</td><td>0.438</td><td>0.659</td><td>0.666</td></tr><tr><td>L</td><td>0.265</td><td>0.409</td><td>0.517</td><td>0.523</td></tr><tr><td>class 3</td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>1.305</td><td>0.494</td><td>0.008</td><td>0.012</td></tr><tr><td>L</td><td>1.501</td><td>0.462</td><td>0.001</td><td>0.003</td></tr><tr><td>class 4</td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>-0.273</td><td>0.413</td><td>0.508</td><td>0.515</td></tr><tr><td>L</td><td>-0.313</td><td>0.417</td><td>0.454</td><td>0.462</td></tr><tr><td>class 5</td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>-0.050</td><td>0.379</td><td>0.895</td><td>0.912</td></tr><tr><td>L</td><td>-0.067</td><td>0.279</td><td>0.811</td><td>0.816</td></tr><tr><td>all</td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>0.406</td><td>0.202</td><td>0.045</td><td>0.047</td></tr><tr><td>L</td><td>0.463</td><td>0.190</td><td>0.015</td><td>0.017</td></tr></table>

![](images/fd00194163d735b61f99c18274d98317e124825c3c6ea6f7bd9f3a7ccdff70c9.jpg)  
8.6 Homework Problems

![](images/5175e0c1854c93c054bb7d2fbb3abef43593c6af4dcb97077036121e2d37f2a5.jpg)  
FIGURE 8.2: Re-analyzing Chong et al. (2016)'s data: randomization distributions with $5 \times 10^{4}$ Monte Carlo draws and the $\mathrm{N}(0,1)$ approximations

# 9

# Bridging Finite and Super Population Causal Inference

We have focused on the finite population perspective in randomized experiments. It treats all the potential outcomes as fixed numbers. Even if the potential outcomes are random variables, we can condition on them under the finite population perspective. The advantages of this perspective are

1. it focuses on the design of the experiments;   
2. it requires minimal assumptions on the data-generating process of the outcomes.

However, it is often criticized for having only internal validity but not necessarily external validity, with informal definitions below.

Definition 9.1 (internal validity) The statistical analysis is valid for the study samples at hand.

Definition 9.2 (external validity) The statistical analysis is valid for a broader population beyond the study samples.

Obviously, all experimenters want not only the internal validity but also the external validity of their experiments. Since all statistical properties are conditional on the potential outcomes for the units we have, the results are only about the observed units under the finite population perspective. Then a natural question arises: do the finite population results generalize to a bigger population?

This is a fair critique of the finite population framework conditional on the potential outcomes. However, this can be a philosophical question. What we observed is a finite population, so any experimental design and analysis directly give us information about this finite population. Randomization only ensures internal validity given the potential outcomes of these units. The external validity of the results depends on the sampling process of the units. If the finite population is a representative sample of a larger population we are interested in, then of course the experimental results also have external validity. Otherwise, the results based on randomization inference may not generalize. To rigorously discuss this issue, we need to have a framework with two levels of randomness, one due to the sampling process of the units and

the other due to the random assignment of the treatment. See Miratrix et al. (2018) and Abadie et al. (2020) for formal discussions of this idea. $^{1}$

For some statisticians, this is just a technical problem. We can change the statistical framework, assuming that the units are sampled from a superpopulation. Then all the statements are about the population of interest. This is a convenient framework, although it does not really solve the problem mentioned above. Below, I will introduce this framework for two purposes:

1. it gives a different perspective on randomized experiments;   
2. it serves as a bridge between Parts II and III of this book.

The latter purpose is more important since the superpopulation framework allows us to derive more fruitful results for observational studies in which the treatment is not randomly assigned.

# 9.1 CRE

Assume

$$
\{Z _ {i}, Y _ {i} (1), Y _ {i} (0), X _ {i} \} _ {i = 1} ^ {n} \stackrel {\mathrm {I I D}} {\sim} \{Z, Y (1), Y (0), X \}
$$

from a superpopulation. So we can drop the subscript $i$ for quantities of this population. With a little abuse of notation, we define the population average causal effect as

$$
\tau = E \{Y (1) - Y (0) \} = E \{Y (1) \} - E \{Y (0) \}.
$$

Under the superpopulation framework, we can formulate the CRE as below.

Definition 9.3 (CRE under the superpopulation framework) We have

$$
Z \bot \{Y (1), Y (0), X \}.
$$

Under Definition 9.3, the average causal effect can be written as

$$
\begin{array}{l} \tau = E \{Y (1) \mid Z = 1 \} - E \{Y (0) \mid Z = 0 \} \\ = E (Y \mid Z = 1) - E (Y \mid Z = 0), \tag {9.1} \\ \end{array}
$$

which equals the difference in expectations of the outcomes. The first line in (9.1) is the key step that leverages the value of randomization. Since $\tau$ can be expressed as a function of the distributions of the observables, it is non-parametrically identifiable<sup>2</sup>. The formula (9.1) immediately suggests a moment

estimator $\hat{\tau}$ , which is the difference in means of the outcomes defined before. Conditioning on $\mathbf{Z}$ , this is then a standard two-sample problem comparing the means of two independent samples. We have

$$
E (\hat {\tau} \mid \boldsymbol {Z}) = \tau
$$

and

$$
\operatorname {v a r} (\hat {\tau} \mid \boldsymbol {Z}) = \frac {\operatorname {v a r} \{Y (1) \}}{n _ {1}} + \frac {\operatorname {v a r} \{Y (0) \}}{n _ {0}}.
$$

Under IID sampling, the sample variances are unbiased for the population variances, so Neyman (1923)'s variance estimator is unbiased for $\operatorname{var}(\hat{\tau} \mid \mathbf{Z})$ . The conservativeness problem goes away under this superpopulation framework.

We can also discuss covariate adjustment. Based on the OLS decompositions (see Chapter B)

$$
Y (1) = \gamma_ {1} + \beta_ {1} ^ {\mathrm {T}} X + \varepsilon (1), \tag {9.2}
$$

$$
Y (0) = \gamma_ {0} + \beta_ {0} ^ {\mathrm {T}} X + \varepsilon (0), \tag {9.3}
$$

we have

$$
\begin{array}{l} \tau = E \{Y (1) - Y (0) \} \\ = \gamma_ {1} - \gamma_ {0} + \left(\beta_ {1} - \beta_ {0}\right) ^ {\top} E (X), \\ \end{array}
$$

since the residuals $\varepsilon(1)$ and $\varepsilon(0)$ have mean zero due to the inclusion of the intercepts. We can use the OLS with the treated and control data to estimate the coefficients in (9.2) and (9.3), respectively. The sample versions of the coefficients are $\hat{\gamma}_1, \hat{\beta}_1, \hat{\gamma}_0, \hat{\beta}_0$ , so a covariate-adjusted estimator for $\tau$ is

$$
\hat {\tau} _ {\mathrm {a d j}} = \hat {\gamma} _ {1} - \hat {\gamma} _ {0} + (\hat {\beta} _ {1} - \hat {\beta} _ {0}) ^ {\mathsf {T}} \bar {X}.
$$

If we center covariates with $\bar{X} = 0$ , the above estimator reduces to Lin (2013)'s estimator

$$
\hat {\tau} _ {\mathrm {L}} = \hat {\gamma} _ {1} - \hat {\gamma} _ {0},
$$

which equals the coefficient of $Z$ in the pooled regression with treatment-covariates interactions; see Proposition 6.2.

Unfortunately, the EHW variance estimator does not work for $\hat{\tau}_{\mathrm{L}}$ because of the additional uncertainty in the sample mean of covariates $\bar{X}$ under the super population framework. Berk et al. (2013), Negi and Wooldridge (2021) and Zhao and Ding (2021a) proposed a correction of the EHW variance estimator by adding an extra term

$$
\left(\hat {\beta} _ {1} - \hat {\beta} _ {0}\right) ^ {\mathsf {T}} S _ {X} ^ {2} \left(\hat {\beta} _ {1} - \hat {\beta} _ {0}\right) / n \tag {9.4}
$$

where $\hat{\beta}_1 - \hat{\beta}_0$ equals the coefficient of the interaction $Z_{i}X_{i}$ in obtaining Lin (2013)'s estimator and $S_X^2$ is the finite-population covariance matrix of the covariates. A conceptually simpler yet computationally intensive approach is to use the bootstrap to estimate the variance; see Chapter A.6 and Problem 9.2.

# 9.2 Simulation under the CRE: the super population perspective

The following linestimator function can compute Lin (2013)'s estimator, the EHW standard error, and the corrected standard error based on (9.4) for the super population.

library("car")   
linestimator $=$ function(Z,Y,X){ #standardize X X $=$ scale(X) n $=$ dim(X)[1] p $=$ dim(X)[2] #fully interacted OLS linreg $=$ lm(Y \~ Z\*X) est $=$ coef(linreg)[2] vehw $=$ hccm(linreg)[2,2] #super population correction inter $=$ coef(linreg)[(p+3):(2\*p+2)] vsuper $=$ vehw $^+$ sum(inter\*(cov(X)\%*%inter))/n c(est，sqrt(vehw)，sqrt(vsuper))   
}

I then use simulation to compare the EHW standard error and the corrected standard error. I choose sample size $n = 500$ and use 2000 Monte Carlo repetitions. The potential outcomes are nonlinear in covariates and the error terms are not Normal. The true average causal effect equals 0.

res $=$ replicate(2000，{n $= 500$ X $\equiv$ matrix(rnorm(n*2)，n，2)Y1 $= \mathrm{X}[[,1] + \mathrm{X}[[,1]\hat{\cdot}\mathrm{2} + \mathrm{runif}(\mathrm{n}, - 0.5,0.5)$ Y0 $= \mathrm{X}[[,2] + \mathrm{X}[[,2]\hat{\cdot}\mathrm{2} + \mathrm{runif}(\mathrm{n}, - 1,1)$ Z $= \mathrm{rbinom}(n,1,0.6)$ Y $= \mathrm{Z*Y1} + (1 - \mathrm{Z})*\mathrm{Y0}$ linestimator(Z，Y，X)}

The following results confirm the theory. First, Lin (2013)'s estimator is nearly unbiased. Second, the average EHW standard error is smaller than the empirical standard derivation, resulting in undercoverage of the $95\%$ confidence intervals. Third, the average corrected standard error for super population is nearly identical to the empirical standard derivation, resulting in more accurate coverage of the $95\%$ confidence intervals.

```txt
> ## bias
> mean(res[1,])
[1] -0.0001247585
> ## empirical standard deviation
> sd(res[1,])
[1] 0.1507773
> ## estimated EHW standard error
> mean(res[2,])
[1] 0.1388657
> ## coverage based on EHW standard error
> mean((res[1] - 1.96*res[2, ]) * (res[1,] + 1.96*res[2,]) <= 0)
[1] 0.927
> ## estimated super population standard error
> mean(res[3,])
[1] 0.1531519
> ## coverage based on population standard error
> mean((res[1] - 1.96*res[3, ]) * (res[1,] + 1.96*res[3,]) <= 0)
[1] 0.9525 
```

# 9.3 Extension to the SRE

We can extend the discussion in Section 9.1 to the SRE since it is equivalent to independent CREs within strata. The notation below will be slightly different from that in Chapter 5.

Assume that

$$
\left\{Z _ {i}, Y _ {i} (1), Y _ {i} (0), X _ {i} \right\} \stackrel {{\text {I I D}}} {{\sim}} \left\{Z, Y (1), Y (0), X \right\}.
$$

With a discrete covariate $X_{i} \in \{1, \dots, K\}$ , we can formulate the SRE as below.

Definition 9.4 (SRE under the super population framework) We have

$$
Z \sqcup \{Y (1), Y (0) \} \mid X.
$$

Under Definition 9.4, the conditional average causal effect can be rewritten as

$$
\begin{array}{l} \tau_ {[ k ]} = E \{Y (1) - Y (0) \mid X = k \} \\ = E (Y \mid Z = 1, X = k) - E (Y \mid Z = 0, X = k), \\ \end{array}
$$

so the average causal effect can be rewritten as

$$
\begin{array}{l} \tau = E \{Y (1) - Y (0) \} \\ = \sum_ {k = 1} ^ {K} \operatorname {p r} (X = k) E \{Y (1) - Y (0) \mid X = k \} \\ = \sum_ {k = 1} ^ {K} \operatorname {p r} (X = k) \tau_ {[ k ]}. \\ \end{array}
$$

The discussion in Section 9.1 holds within all strata, so we can derive the superpopulation analog for the SRE. When there are more than two treatment and control units within each stratum, we can use $\hat{V}_{\mathrm{S}}$ as the variance estimator for $\operatorname{var}(\hat{\tau}_{\mathrm{S}})$ .

We will see the exact form of Definition 9.4 in Part III later.

# 9.4 Homework Problems

# 9.1 OLS decomposition of the observed outcome under the CRE

Based on (9.2) and (9.3), show that the OLS decomposition of the observed outcome on the treatment, covariates, and their interaction is

$$
Y = \alpha_ {0} + \alpha_ {Z} Z + \alpha_ {X} ^ {\top} X + \alpha_ {Z X} ^ {\top} X Z + \varepsilon
$$

where

$$
\alpha_ {0} = \gamma_ {0}, \quad \alpha_ {Z} = \gamma_ {1} - \gamma_ {0}, \quad \alpha_ {X} = \beta_ {0}, \quad \alpha_ {Z X} = \beta_ {1} - \beta_ {0}
$$

and

$$
\varepsilon = Z \varepsilon (1) + (1 - Z) \varepsilon (0).
$$

That is,

$$
(\alpha_ {0}, \alpha_ {Z}, \alpha_ {X}, \alpha_ {Z X}) = \arg \min _ {a _ {0}, a _ {Z}, a _ {X}, a _ {Z X}} E (Y - a _ {0} - a _ {Z} Z - a _ {X} ^ {\top} X - a _ {Z X} ^ {\top} X Z) ^ {2}.
$$

# 9.2 Variance estimation of Lin (2013)'s estimator under the super population framework

Under the super population framework, simulate $\{X_i,Z_i,Y_i(1),Y_i(0)\}_{i = 1}^n$ with $\beta_{1}\neq \beta_{0}$ in (9.2) and (9.3). Calculate Lin (2013)'s estimator in each simulated dataset. Compare the true variance and the following estimated variances:

1. the EHW robust variance estimator;   
2. the EHW robust variance estimator with the correction term defined in (9.4);

# 9.4 Homework Problems

3. the bootstrap variance estimator, with covariates centered at the beginning but not re-centered for each bootstrap sample;   
4. the bootstrap variance estimator, with covariates re-centered for each bootstrap sample.

# 9.3 Recommended reading

Ding et al. (2017a) provide a unified discussion of the finite population and superpopulation inferences for the average causal effect.

# Part III

# Observational studies

# 10

# Observational Studies, Selection Bias, and Nonparametric Identification of Causal Effects

Cochran (1965) summarized two common characteristics of observational studies:

1. the objective is to elucidate cause-and-effect relationships;   
2. it is not feasible to use controlled experimentation.

The first characteristic is identical to that of randomized experiments discussed in Part II of this book, but the second differs fundamentally from randomized experiments.

Dorn (1953) suggested that the planner of an observational study should always ask the following question:

How would the study be conducted if it were possible to do it by controlled experimentation?

It is always helpful to follow Dorn (1953)'s suggestion because the potential outcomes framework has an intrinsic link to an experiment, either a real experiment or a thought experiment. Part III of this book will discuss causal inference with observational studies. It will clarify the fundamental differences between observational studies and randomized experiments. Nevertheless, many ideas of causal inference with observational studies are deeply connected to those with randomized experiments.

# 10.1 Motivating Examples

Example 10.1 (job training program) LaLonde (1986) was interested in the causal effect of a job training program on earnings. He compared the results based on a randomized experiment to the results based on observational studies. We have used the experimental data before, which is the lalonde dataset in the Matching package. We have also used an observational counterpart cps1re74.csv in Chapter 1.2.1 and Problem 1.4. LaLonde (1986) found that

many traditional statistical or econometric methods for observational studies gave quite different estimates compared with the estimates based on the experimental data. Dehejia and Wahba (1999) re-analyzed the data using methods motivated by causal inference, and found that those methods can recover the experimental gold standard well. Since then, this has become a canonical example in causal inference with observational studies.

Example 10.2 (smoking and homocysteine) Bazzano et al. (2003) compared the homocysteine levels in daily smokers and non-smokers based on the data from the National Health and Nutrition Examination Survey (NHANES) 2005-2006. Rosenbaum (2018) documented the data as homocyst in the packageSENstrat. The dataset has the following important covariates:

```txt
female 1=female, 0=male  
age3 three age categories: 20-39, 40-50, ≥60  
ed3 three education categories: < high school, high school, some college  
bmi3 three BMI categories: <30, [30,35), ≥ 35  
pov2 TRUE=income at least twice the poverty level, FALSE otherwise 
```

Example 10.3 (school meal program and body mass index) Chan et al. (2016) used a subsample of the data from NHANES 2007-2008 to study whether participation in school meal programs led to an increase in BMI for school children. They documented the data as $n$ hanes_bmi in the package ATE. The dataset has the following important covariates:

age Age  
ChildSex Sex (1: male, 0: female)  
black Race (1: black, 0: otherwise)  
mexam Race (1: Hispanic: 0 otherwise)  
pir200_plus Family above $200\%$ of the federal poverty level  
WIC Participation in the special supplemental nutrition program  
Food Stamp Participation in food stamp program  
fsdchbi Childhood food security  
AnyIns Any insurance  
RefSex Sex of the adult respondent (1: male, 0: female)  
RefAge Age of the adult respondent

A common feature of Examples 10.1-10.3 is that we are interested in estimating the causal effect of a nonrandomized treatment on an outcome. They are all from observational studies.

# 10.2 Causal effects and selection bias under the potential outcomes framework

For unit $i$ ( $i = 1, \dots, n$ ), we have pretreatment covariates $X_{i}$ , a binary treatment indicator $Z_{i}$ , and an observed outcome $Y_{i}$ with two potential outcomes $Y_{i}(1)$ and $Y_{i}(0)$ under the treatment and control, respectively. For simplicity, we assume

$$
\{X _ {i}, Z _ {i}, Y _ {i} (1), Y _ {i} (0) \} _ {i = 1} ^ {n} \stackrel {\mathrm {I I D}} {\sim} \{X, Z, Y (1), Y (0) \}.
$$

So we can drop the subscript $i$ for quantities of this population. The causal effects of interest are the average causal effect

$$
\tau = E \{Y (1) - Y (0) \},
$$

the average causal effect on the treated units

$$
\tau_ {\mathrm {T}} = E \{Y (1) - Y (0) \mid Z = 1 \},
$$

and the average causal effect on the control units:

$$
\tau_ {\mathrm {C}} = E \{Y (1) - Y (0) \mid Z = 0 \}.
$$

By the linearity of the expectation, we have

$$
\begin{array}{l} \tau_ {\mathrm {T}} = E \left\{Y (1) \mid Z = 1 \right\} - E \left\{Y (0) \mid Z = 1 \right\} \\ = E (Y \mid Z = 1) - E \{Y (0) \mid Z = 1 \} \\ \end{array}
$$

and

$$
\begin{array}{l} \tau_ {\mathrm {C}} = E \left\{Y (1) \mid Z = 0 \right\} - E \left\{Y (0) \mid Z = 0 \right\} \\ = E \{Y (1) \mid Z = 0 \} - E (Y \mid Z = 0). \\ \end{array}
$$

In the above two formulas of $\tau_{\mathrm{T}}$ and $\tau_{\mathrm{C}}$ , the quantities $E(Y \mid Z = 1)$ and $E(Y \mid Z = 0)$ are directly estimable from the data, but the quantities $E\{Y(0) \mid Z = 1\}$ and $E\{Y(1) \mid Z = 0\}$ are not. The latter two are counterfactuals because they are the means of the potential outcomes corresponding to the treatment level that is the opposite of the actual received treatment.

The simple difference in means, also known as the prima facie² causal effect,

$$
\begin{array}{l} \tau_ {\mathrm {P F}} = E (Y \mid Z = 1) - E (Y \mid Z = 0) \\ = E \{Y (1) \mid Z = 1 \} - E \{Y (0) \mid Z = 0 \} \\ \end{array}
$$

is generally biased for the causal effects defined above. For example,

$$
\tau_ {\mathrm {P F}} - \tau_ {\mathrm {T}} = E \{Y (0) \mid Z = 1 \} - E \{Y (0) \mid Z = 0 \}
$$

and

$$
\tau_ {\mathrm {P F}} - \tau_ {\mathrm {C}} = E \{Y (1) \mid Z = 1 \} - E \{Y (1) \mid Z = 0 \}
$$

are not zero in general, and they quantify the selection bias. They measure the differences in the means of the potential outcomes across the treatment and control groups.

Why is randomization so important? Rubin (1978) first used potential outcomes to quantify the benefit of randomization. We have used the fact in Chapter 9 that

$$
Z \bot \{Y (1), Y (0) \} \tag {10.1}
$$

in the CRE, which implies that the selection bias terms are both zero:

$$
\tau_ {\mathrm {P F}} - \tau_ {\mathrm {T}} = E \{Y (0) \mid Z = 1 \} - E \{Y (0) \mid Z = 0 \} = 0
$$

and

$$
\tau_ {\mathrm {P F}} - \tau_ {\mathrm {C}} = E \{Y (1) \mid Z = 1 \} - E \{Y (1) \mid Z = 0 \} = 0.
$$

So under the CRE in (10.1), we have

$$
\tau = \tau_ {\mathrm {T}} = \tau_ {\mathrm {C}} = \tau_ {\mathrm {P F}}. \tag {10.2}
$$

From the above discussion, the fundamental benefit of randomization is to balance the distributions of the potential outcomes across the treatment and control groups. This is a much stronger guarantee than balancing the distributions of the observed covariates.

Without randomization, the selection bias terms can be arbitrarily large, especially for unbounded outcomes. This highlights the fundamental difficulty of causal inference with observational studies.

# 10.3 Sufficient conditions for nonparametric identification of causal effects

# 10.3.1 Identification

Causal inference with observational studies is challenging. It relies on strong assumptions. A strategy is to use the information from the pretreatment covariates and assume that conditioning on the observed covariates $X$ , the selection bias terms are zero, that is,

$$
E \{Y (0) \mid Z = 1, X \} = E \{Y (0) \mid Z = 0, X \}, \tag {10.3}
$$

$$
E \{Y (1) \mid Z = 1, X \} = E \{Y (1) \mid Z = 0, X \}. \tag {10.4}
$$

# 10.3 Sufficient conditions for nonparametric identification of causal effects 143

The assumptions in (10.3) and (10.4) state that the differences in the means of the potential outcomes across the treatment and control groups are entirely due to the difference in the observed covariates. So given the same value of the covariates, the potential outcomes have the same means across the treatment and control groups. Mathematically, (10.3) and (10.4) ensure that the conditional versions of the effects in (10.2) are identical:

$$
\tau (X) = \tau_ {\mathrm {T}} (X) = \tau_ {\mathrm {C}} (X) = \tau_ {\mathrm {P F}} (X),
$$

where

$$
\tau (X) = E \{Y (1) - Y (0) \mid X \},
$$

$$
\tau_ {\mathrm {T}} (X) = E \{Y (1) - Y (0) \mid Z = 1, X \},
$$

$$
\tau_ {\mathrm {C}} (X) = E \{Y (1) - Y (0) \mid Z = 0, X \},
$$

$$
\tau_ {\mathrm {P F}} (X) = E (Y \mid Z = 1, X) - E (Y \mid Z = 0, X).
$$

In particular, $\tau(X)$ is often called the conditional average causal effect (CATE).

A key result in this chapter is that the average causal effect $\tau$ is nonparametrically identifiable under (10.3) and (10.4). The notion of nonparametrically identifiability does not appear frequently in classic statistics, but it is key to causal inference with observational studies. I first give an abstract definition below.

Definition 10.1 (identification) A parameter $\theta$ is identifiable if it can be written as a function of the distribution of the observed data under certain model assumptions. A parameter $\theta$ is nonparametrically identifiable if it can be written as a function of the distribution of the observed data without any parametric model assumptions.

Definition 10.1 is too abstract at the moment. I will use more concrete examples in later chapters to illustrate its meaning. It is often neglected in classic statistics problems. For instance, the mean $\theta = E(Y)$ is nonparametrically identifiable if we have IID draws of $Y_{i}$ 's; the Pearson correlation coefficient $\theta = \rho_{YX}$ is nonparametrically identifiable if we have IID draws of the pairs $(X_{i},Y_{i})$ 's. In those examples, the parameters are nonparametrically identifiable automatically. However, Definition 10.1 is fundamental in causal inference with observational studies. In particular, the parameter of interest $\tau = E\{Y(1) - Y(0)\}$ depends on some unobserved random variables, so it is unclear whether it is nonparametrically identifiable based on observed data. Under the assumptions in (10.3) and (10.4), it is nonparametrically identifiable, with details below.

Because $\tau_{\mathrm{PF}}(X)$ depends only on the observables, it is nonparametrically identified by definition. Moreover, (10.3) and (10.4) ensure that the three causal effects are the same as $\tau_{\mathrm{PF}}(X)$ , so $\tau(X)$ , $\tau_{\mathrm{T}}(X)$ , and $\tau_{\mathrm{C}}(X)$ are all nonparametrically identified. Consequently, the unconditional versions are also

nonparametrically identified under (10.3) and (10.4) due to the law of total expectation:

$$
\tau = E \{\tau (X) \}, \quad \tau_ {\mathrm {T}} = E \{\tau_ {\mathrm {T}} (X) \mid Z = 1 \}, \quad \tau_ {\mathrm {C}} = E \{\tau_ {\mathrm {C}} (X) \mid Z = 0 \}.
$$

From now on, I will focus on $\tau$ unless stated otherwise (Chapter 13 will be an exception). The following theorem summarizes the identification formulas of $\tau$ .

Theorem 10.1 Under (10.3) and (10.4), the average causal effect $\tau$ is identified by

$$
\begin{array}{l} \tau = E \{\tau (X) \} (10.5) \\ = E \left\{E (Y \mid Z = 1, X) - E (Y \mid Z = 0, X) \right\} (10.6) \\ = \int \left\{E (Y \mid Z = 1, X = x) - E (Y \mid Z = 0, X = x) \right\} f (x) d x. (10.7) \\ \end{array}
$$

The formula (10.6) was formally established by Rosenbaum and Rubin (1983b), which is also called the g-formula by Robins (see Hernán and Robins, 2020).

With a discrete covariate, we can write the identification formula in Theorem 10.1 as

$$
\begin{array}{l} \tau = \sum_ {x} E (Y \mid Z = 1, X = x) \operatorname * {p r} (X = x) \\ - \sum_ {x} E (Y \mid Z = 0, X = x) \Pr (X = x), \tag {10.8} \\ \end{array}
$$

and also the simple difference in means as

$$
\begin{array}{l} \tau_ {\mathrm {P F}} = \sum_ {x} E (Y \mid Z = 1, X = x) \Pr (X = x \mid Z = 1) \\ - \sum_ {x} E (Y \mid Z = 0, X = x) \Pr (X = x \mid Z = 0) \tag {10.9} \\ \end{array}
$$

by the law of total probability. Comparing (10.8) and (10.9), we can see that although both formulas compare the conditional expectations $E(Y \mid Z = 1, X = x)$ and $E(Y \mid Z = 0, X = x)$ , they average over different distributions of the covariates. The causal parameter $\tau$ averages the conditional expectations over the common distribution of the covariates, but the difference in means $\tau_{\mathrm{PF}}$ averages the conditional expectations over two different distributions of the covariates in the treated and control groups.

Usually, we impose a stronger assumption.

Assumption 10.1 (ignorability) We have

$$
Y (z) \bot Z \mid X \quad (z = 0, 1). \tag {10.10}
$$

# 10.3 Sufficient conditions for nonparametric identification of causal effects 145

Assumption 10.1 has many names:

1. $ignorability$ due to Rubin (1978) $^3$ ;   
2. unconfoundedness which is popular among epidemiologists;   
3. selection on observables which is popular among social scientists;   
4. conditional independence which is merely a description of the notation $\perp$ in the assumption.

Sometimes, we impose an even stronger assumption.

# Assumption 10.2 (strong ignorability) We have

$$
\{Y (1), Y (0) \} \bot Z \mid X. \tag {10.11}
$$

Assumption 10.2 is called strong ignorance (Rubin, 1978; Rosenbaum and Rubin, 1983b). If the parameter of interest is $\tau$ , then the stronger Assumptions 10.1 and 10.2 are just imposed for notational simplicity thanks to the conditional independence notation $\perp$ . They are not necessary for identifying $\tau$ . However, they can not be relaxed if the parameter of interest is the causal effects on other scales (for example, distribution, quantile, or some transformation of the outcome). The strong ignorance assumption requires that the potential outcomes vector be independent of the treatment given the covariates, but the ignorance assumption only requires each potential outcome be independent of the treatment given covariates. The former is stronger than the latter. However, their difference is rather technical and of pure theoretical interests; see Problem 10.5. In most reasonable statistical models, they both hold; see Section 10.3.2 below. We will not distinguish them in this book and will simply use ignorance to refer to both.

# 10.3.2 Plausibility of the ignorability assumption

A fundamental problem of causal inference with observational studies is the plausibility of the ignorance assumption. The discussion in Chapter 10.3.1 may seem too mathematical in the sense that the ignorance assumption serves as a sufficient condition to ensure the nonparametric identification of the average causal effect. What is its scientific meaning? Intuitively, it rules out all unmeasured covariates that affect the treatment and outcome simultaneously. Those "common causes" of the treatment and outcome are called confounders. That is why the ignorance assumption is also called the unconfoundedness assumption. More transparently, we can interpret the ignorance assumption

based on the outcome data-generating process. If

$$
\begin{array}{l} Y (1) = g _ {1} (X, V _ {1}), \\ Y (0) = g _ {0} (X, V _ {0}), \\ Z = 1 \{g (X, V) \geq 0 \} \\ \end{array}
$$

with $(V_{1}, V_{0}) \perp V$ , then both Assumptions 10.1 and 10.2 hold. In the above data-generating process, the "common causes" $X$ of the treatment and the outcome are all observed, and the remaining random components are independent. If the data-generating process changes to

$$
\begin{array}{l} Y (1) = g _ {1} (X, U, V _ {1}), \\ Y (0) = g _ {0} (X, U, V _ {0}), \\ Z = 1 \{g (X, U, V) \geq 0 \} \\ \end{array}
$$

with $(V_{1}, V_{0}) \perp V$ , then Assumptions 10.1 and 10.2 do not hold in general. The unmeasured "common cause" $U$ induces dependence between the treatment and the potential outcomes even conditional on the observed covariates $X$ . If we do not have access to $U$ and analyze the data based only on $(Z, X, Y)$ , the final estimator will be biased for the causal parameter in general. This type of bias is called the omitted variable bias in econometrics; see Problem 16.2 in a later chapter.

The ignorability assumption can be reasonable if we observe a rich set of covariates $X$ that affect the treatment and the outcome simultaneously. I start with this assumption to discuss identification and estimation strategies in Part III of this book. However, it is fundamentally untestable. We may justify it based on the scientific background knowledge, but we are often not sure whether it holds or not. Parts IV and V of this book will discuss other strategies when the ignorability assumption is not plausible.

# 10.4 Two simple estimation strategies and their limitations

# 10.4.1 Stratification or standardization based on discrete covariates

If the covariate $X_{i}\in \{1,\ldots ,K\}$ is discrete, then ignorability (10.10) reads as

$$
Y (z) \bot Z \mid X = k \quad (z = 0, 1; k = 1, \dots , K),
$$

which essentially assumes that the observational study is an SRE under the superpopulation framework in Chapter 9. Therefore, we can use the estimator

$$
\hat {\tau} = \sum_ {k = 1} ^ {K} \pi_ {[ k ]} \left\{\hat {\bar {Y}} _ {[ k ]} (1) - \hat {\bar {Y}} _ {[ k ]} (0) \right\},
$$

which is identical to the stratified or post-stratified estimator discussed in Chapter 5.

This method is still widely used in practice. Example 10.2 contains discrete covariates, and I relegate the analysis to Problem 10.4. However, there are several obvious difficulties in implementing this method. First, it works well for the case with small $K$ . For large $K$ , it is very likely that many strata have $n_{[k]1} = 0$ or $n_{[k]0} = 0$ , leading to the poorly defined $\hat{\tau}_{[k]}$ 's for those strata. This is related to the issue of overlap which will be discussed in Chapter 20 later. Second, it is not obvious how to apply this stratification method to multidimensional continuous or mixed covariates $X$ . A standard method is to create strata based on the initial covariates and then apply the stratification method. This may result in arbitrariness in the analysis.

# 10.4.2 Outcome regression

The most commonly used method based on outcome regression is to run the OLS with an additive model of the observed outcome on the treatment indicator and covariates, which assumes

$$
E (Y \mid Z, X) = \beta_ {0} + \beta_ {z} Z + \beta_ {x} ^ {\mathrm {T}} X.
$$

If the above linear model is correct, then we have

$$
\begin{array}{l} \tau (X) = E (Y \mid Z = 1, X) - E (Y \mid Z = 0, X) \\ = \left(\beta_ {0} + \beta_ {z} + \beta_ {x} ^ {\mathrm {T}} X\right) - \left(\beta_ {0} + \beta_ {x} ^ {\mathrm {T}} X\right) \\ = \beta_ {z}, \\ \end{array}
$$

which implies that the causal effect is homogeneous with respect to the covariates. This, coupled with ignorance, implies that

$$
\tau = E \{\tau (X) \} = \beta_ {z}.
$$

Therefore, if ignorability holds and the outcome model is linear, then the average causal effect equals the coefficient of $Z$ . This is one of the most important applications of the linear model. However, the causal interpretation of the coefficient of $Z$ is valid only under two strong assumptions: ignorability and the linear model.

We have discussed in Chapter 6, the above procedure is suboptimal even in CREs because it ignores the treatment effect heterogeneity induced by the covariates. If we assume

$$
E (Y \mid Z, X) = \beta_ {0} + \beta_ {z} Z + \beta_ {x} ^ {\mathrm {T}} X + \beta_ {z x} ^ {\mathrm {T}} X Z,
$$

we have

$$
\begin{array}{l} \tau (X) = E (Y \mid Z = 1, X) - E (Y \mid Z = 0, X) \\ = \left(\beta_ {0} + \beta_ {z} + \beta_ {x} ^ {\mathsf {T}} X + \beta_ {z x} ^ {\mathsf {T}} X\right) - \left(\beta_ {0} + \beta_ {x} ^ {\mathsf {T}} X\right) \\ = \beta_ {z} + \beta_ {z x} ^ {\mathsf {T}} X, \\ \end{array}
$$

which, coupled with ignorability, implies that

$$
\tau = E \{\tau (X) \} = E (\beta_ {z} + \beta_ {z x} ^ {\mathsf {T}} X) = \beta_ {z} + \beta_ {z x} ^ {\mathsf {T}} E (X).
$$

The estimator for $\tau$ is then $\hat{\beta}_z + \hat{\beta}_{zx}^{\mathrm{T}}\bar{X}$ , where $\hat{\beta}_z$ is the regression coefficient of $Z$ and $\bar{X}$ is the sample mean of $X$ . If we center the covariates to ensure $\bar{X} = 0$ , then the estimator is simply the regression coefficient of $Z$ . To simplify the procedure, we usually center the covariates at the beginning; also recall Lin (2013)'s estimator introduced in Chapter 6. Rosenbaum and Rubin (1983b) and Hirano and Imbens (2001) discussed this estimator.

In general, we can use other more complex models to estimate the causal effects. For example, if we build two predictors $\hat{\mu}_1(X)$ and $\hat{\mu}_0(X)$ based on the treated and control data, respectively, then we have an estimator for the conditional average causal effect

$$
\hat {\tau} (X) = \hat {\mu} _ {1} (X) - \hat {\mu} _ {0} (X)
$$

and an estimator for the average causal effect:

$$
\hat {\tau} ^ {\mathrm {r e g}} = n ^ {- 1} \sum_ {i = 1} ^ {n} \{\hat {\mu} _ {1} (X _ {i}) - \hat {\mu} _ {0} (X _ {i}) \}.
$$

The estimator $\hat{\tau}$ above has the same form as the projective estimator discussed in Chapter 6. It is sometimes called the outcome regression estimator. The OLS-based estimators above are special cases. We can use the nonparametric bootstrap (see Chapter A.6) to estimate the standard error of the outcome regression estimator.

I give another example for binary outcomes below.

Example 10.4 (outcome regression estimator for binary outcomes)

With a binary outcome, we may model $Y$ using a logistic model

$$
E (Y \mid Z, X) = \operatorname {p r} (Y = 1 \mid Z, X) = \frac {e ^ {\beta_ {0} + \beta_ {z} Z + \beta_ {x} ^ {\intercal} X}}{1 + e ^ {\beta_ {0} + \beta_ {z} Z + \beta_ {x} ^ {\intercal} X}},
$$

then based on the estimators of the coefficients $\hat{\beta}_0, \hat{\beta}_z, \hat{\beta}_x$ , we have the following estimator for the average causal effect:

$$
\hat {\tau} = n ^ {- 1} \sum_ {i = 1} ^ {n} \left\{\frac {e ^ {\hat {\beta} _ {0} + \hat {\beta} _ {z} + \hat {\beta} _ {x} ^ {\mathrm {T}} X _ {i}}}{1 + e ^ {\hat {\beta} _ {0} + \hat {\beta} _ {z} + \hat {\beta} _ {x} ^ {\mathrm {T}} X _ {i}}} - \frac {e ^ {\hat {\beta} _ {0} + \hat {\beta} _ {x} ^ {\mathrm {T}} X _ {i}}}{1 + e ^ {\hat {\beta} _ {0} + \hat {\beta} _ {x} ^ {\mathrm {T}} X _ {i}}} \right\}.
$$

This estimator is not simply the coefficient of the treatment in the logistic model. It is a nonlinear function of all the coefficients as well as the empirical distribution of the covariates. In econometrics, this estimator is called

the "average partial effect" or "average marginal effect" of the treatment in the logistic model. Many econometric software packages can report this estimator associated with the standard error. Similarly, we can also derive the corresponding estimator based on a fully interacted logistic model; see Problem 10.3.

The above predictors for the conditional means of the outcome can also be other machine learning tools. In particular, Hill (2011) championed the use of tree methods for estimating $\tau$ , and Wager and Athey (2018) proposed to use them also for estimating $\tau(X)$ . Wager and Athey (2018) also combined the tree methods with the idea of the propensity score in the next chapter. Since then, the intersection of machine learning and causal inference has been an active research area (e.g., Hahn et al., 2020; Künzel et al., 2019).

The biggest problem with the above approach based on outcome regressions is its sensitivity to the specification of the outcome model. Problem 1.4 gave such an example. Depending on the incentive of empirical research and publications, people might report their favorable causal effects estimates after searching over a wide set of candidate models, without confessing this model searching process. This is a major source of $p$ -hacking in causal inference. Problem 1.4 hinted at this issue. Leamer (1978) criticized this approach in empirical research.

# 10.5 Homework Problems

# 10.1 A simple identity

Show that $\tau = \operatorname{pr}(Z = 1)\tau_{\mathrm{T}} + \operatorname{pr}(Z = 0)\tau_{\mathrm{C}}$

# 10.2 Nonparametric identification of other causal effects

Underignorability,showthat

1. the distributional causal effect

$$
\mathrm {D C E} _ {y} = \operatorname {p r} \{Y (1) > y \} - \operatorname {p r} \{Y (0) > y \}
$$

is nonparametrically identifiable for all $y$ ;

2. the quantile causal effect

$$
\mathrm {Q C E} _ {q} = \operatorname {q u a n t i l e} _ {q} \{Y (1) \} - \operatorname {q u a n t i l e} _ {q} \{Y (0) \},
$$

is nonparametrically identifiable for all $q$ , where $\mathrm{quantile}_q\{\cdot\}$ is the $q$ th quantile of a random variable.

Remark: In probability theory, $\operatorname{pr}\{Y(z) \leq y\}$ is the cumulative distribution function and $\operatorname{pr}\{Y(z) > y\}$ is the survival function of the potential outcome $Y(z)$ . The distributional causal effect compares the survival functions of the potential outcomes under treatment and control.

The quantile causal effect compares the marginal quantiles of the potential outcomes, which is different from the quantile of the individual causal effect

$$
\tau_ {q} = \mathrm {q u a n t i l e} _ {q} \{Y (1) - Y (0) \}.
$$

In fact, $\tau_q$ is not identifiable in the sense that the marginal distributions $\operatorname{pr}\{Y(1) \leq y\}$ and $\operatorname{pr}\{Y(0) \leq y\}$ can not uniquely determine $\tau_q$ .

# 10.3 Outcome imputation estimator in the fully interacted logistic model

This problem extends Example 10.4.

Assume that a binary outcome follows a logistic model

$$
E (Y \mid Z, X) = \operatorname * {p r} (Y = 1 \mid Z, X) = \frac {e ^ {\beta_ {0} + \beta_ {z} Z + \beta_ {x} ^ {\intercal} X + \beta_ {x z} ^ {\intercal} X Z}}{1 + e ^ {\beta_ {0} + \beta_ {z} Z + \beta_ {x} ^ {\intercal} X + \beta_ {x z} ^ {\intercal} X Z}}.
$$

What is the corresponding outcome regression estimator for the average causal effect?

# 10.4 Data analysis: stratification and regression

Use the dataset homocyst in the package senstrat. The outcome is homocysteine, the homocysteine level, and the treatment is $\mathbf{z}$ , where $z = 1$ for a daily smoker and $z = 0$ for a never smoker. Covariates are female, age3, ed3, bmi3, pov2 with detailed explanations in the package, and st is a stratum indicator, defined by all the combinations of the discrete covariates.

1. How many strata have only treated or control units? What is the proportion of the units in these strata? Drop these strata and perform a stratified analysis of the observational study. Report the point estimator, variance estimator, and $95\%$ confidence interval for the average causal effect.   
2. Run the OLS of the outcome on the treatment indicator and covariates without interactions. Report the coefficient of the treatment and the robust standard error.

Drop the strata with only treated or control units. Re-run the OLS and report the result.

3. Apply Lin (2013)'s estimator of the average causal effect. Report the coefficient of the treatment and the robust standard error.

If you do not drop the strata with only treated or control units, what will happen?

4. Compare the results in the above three analyses. Which one is more credible?

# 10.5 Ignorability versus strong ignorance

Give an example such that the ignorability holds but the strong ignorability does not hold.

Remark: This is related to a classic probability problem of finding three random variables $A, B, C$ such that

$A\bot \bot C$ and $B\bot \bot C$ but $(A,B)\bot \bot C$

# 10.6 Recommended reading

Cochran (1965) is a classic reference on observational studies. It contains many useful insights but does not use the formal potential outcomes framework. Dylan Small founded a new journal called *Observational Studies* in 2015 (Small, 2015) and reprinted an old article "Observational Studies" by W. G. Cochran as Cochran (2015). Many leading researchers also made insightful comments on Cochran (2015).

# 11

# The Central Role of the Propensity Score in Observational Studies for Causal Effects

Rosenbaum and Rubin (1983b) proposed the key concept propensity score and discussed its role in causal inference with observational studies. It is one of the most cited papers in statistics, and Titterington (2013) listed it as the second most cited paper published in Biometrika during the past 100 years. Its number of citations has grown very fast in recent years.

Under the IID sampling assumption, we have four random variables associated with each unit: $\{X,Z,Y(1),Y(0)\}$ . Following the basic probability rules, we can factorize the joint distribution as

$$
\begin{array}{l} \operatorname {p r} \{X, Z, Y (1), Y (0) \} \\ = \operatorname {p r} (X) \times \operatorname {p r} \{Y (1), Y (0) \mid X \} \times \operatorname {p r} \{Z \mid X, Y (1), Y (0) \}, \\ \end{array}
$$

where

1. $\operatorname{pr}(X)$ is the covariate distribution,   
2. $\operatorname{pr}\{Y(1), Y(0) \mid X\}$ is the outcome distribution conditional on the covariates $X$ ,   
3. $\operatorname{pr}\{Z \mid X, Y(1), Y(0)\}$ is the treatment distribution conditional on the covariates $X$ , also known as the treatment assignment mechanism.

Usually, we do not want to model the covariates because they are background information happening before the treatment and outcome. If we want to go beyond the outcome model, then we must focus on the treatment assignment mechanism, which leads to the definition of the propensity score.

Definition 11.1 (propensity score) Define

$$
e (X, Y (1), Y (0)) = \operatorname {p r} \{Z = 1 \mid X, Y (1), Y (0) \}
$$

as the propensity score. Under strong ignorability, we have

$$
e (X, Y (1), Y (0)) = \operatorname {p r} \{Z = 1 \mid X, Y (1), Y (0) \} = \operatorname {p r} (Z = 1 \mid X),
$$

so the propensity score reduces to

$$
e (X) = \operatorname {p r} (Z = 1 \mid X),
$$

the conditional probability of receiving the treatment given the observed covariates.

Rosenbaum and Rubin (1983b) used $e(X) = \operatorname{pr}(Z = 1 \mid X)$ as the definition of the propensity score because they focused on observational studies under strong ignorability. It is sometimes helpful to view $e(X, Y(1), Y(0)) = \operatorname{pr}\{Z = 1 \mid X, Y(1), Y(0)\}$ as the general definition of the propensity score even when strong ignorability fails. See Problem 11.1 for more details.

Following Rosenbaum and Rubin (1983b), this chapter will demonstrate that $e(X)$ is a key quantity in causal inference with observational studies under ignorance.

# 11.1 The propensity score as a dimension reduction tool

# 11.1.1 Theory

Theorem 11.1 If $Z \perp \{Y(1), Y(0)\} \mid X$ , then $Z \perp \{Y(1), Y(0)\} \mid e(X)$ .

Theorem 11.1 states that if strong ignorance holds conditional on covariates $X$ , then it also holds conditional on the scalar propensity score $e(X)$ . The ignorance requires conditioning on many background characteristics $X$ of the units, but Theorem 11.1 implies that conditioning on the propensity score $e(X)$ removes all confounding induced by covariates $X$ . The original covariates $X$ can be general and have many dimensions, but the propensity score $e(X)$ is a one-dimensional scalar variable bounded between 0 and 1. Therefore, the propensity score reduces the dimension of the original covariates but still maintains the ignorance. As a statistical terminology, we can view the propensity score as a dimensional reduction tool. We will first prove Theorem 11.1 below and then give an application of the dimension reduction property of the propensity score.

Proof of Theorem 11.1: By the definition of conditional independence, we need to show that

$$
\operatorname {p r} \{Z = 1 \mid Y (1), Y (0), e (X) \} = \operatorname {p r} \{Z = 1 \mid e (X) \}. \tag {11.1}
$$

The left-hand side of (11.1) equals

$$
\begin{array}{l} \Pr \{Z = 1 \mid Y (1), Y (0), e (X) \} \\ = E \{Z \mid Y (1), Y (0), e (X) \} \\ = E \left[ E \{Z \mid Y (1), Y (0), e (X), X \} \mid Y (1), Y (0), e (X) \right] \quad (\text {t o w e r p r o p e r t y}; \text {s e e S e c t i o n A . 1 . 5}) \\ = E \left[ E \{Z \mid Y (1), Y (0), X \} \mid Y (1), Y (0), e (X) \right] \\ = E \left\{E (Z \mid X) \mid Y (1), Y (0), e (X) \right\} \quad (\text {s t r o n g i g n o r a b i l i t y}) \\ = E \left\{e (X) \mid Y (1), Y (0), e (X) \right\} \\ = e (X). \\ \end{array}
$$

The right-hand side of (11.1) equals

$$
\begin{array}{l} \Pr \left\{Z = 1 \mid e (X) \right\} \\ = E \{Z \mid e (X) \} \\ = E \left[ E \{Z \mid e (X), X \} \mid e (X) \right] \quad (\text {t o w e r p r o p e r t y}) \\ = E \left\{E (Z \mid X) \mid e (X) \right\} \\ = E \left\{e (X) \mid e (X) \right\} \\ = e (X). \\ \end{array}
$$

So the left-hand side of (11.1) equals the right-hand side of (11.1).

![](images/8eb7954bb5431e03443f957695400caabcab6fa96b200b1d8780f5a1e7c667e7.jpg)

# 11.1.2 Propensity score stratification

Theorem 11.1 motivates a simple method for estimating causal effects: propensity score stratification. Starting from the simple case, we assume that the propensity score is known and only takes $K$ possible values $\{e_1, \ldots, e_K\}$ with $K$ being much smaller than the sample size $n$ . Theorem 11.1 reduces to

$$
Z \sqcup \left\{Y (1), Y (0) \right\} \mid e (X) = e _ {k} \quad (k = 1, \dots , K).
$$

Therefore, we have an SRE, that is, we have $K$ independent CREs within strata of the propensity score. We can analyze the observational data in the same way as the SRE stratified on $e(X)$ .

In general, the propensity score is not known and is not discrete. We often fit a statistical model for $\operatorname{pr}(Z = 1 \mid X)$ (for example, a logistic model of the binary $Z$ given $X$ ) to obtain the estimated propensity score $\hat{e}(X)$ . This estimated propensity score can take as many values as the sample size, but we can discretize it to approximate the simple case above. For example, we can discretize the estimated propensity score by its $K$ quantiles to obtain $\hat{e}'(X)$ :

$\hat{e}^{\prime}(X_{i}) = e_{k}$ , the $k / K$ -th quantile of $\hat{e}(X)$ , if $\hat{e}(X_{i})$ is between the $(k - 1) / K$ -th and $k / K$ -th quantiles of the $\hat{e}(X_{i})$ 's. Then

$$
Z \perp \left\{Y (1), Y (0) \right\} \mid \hat {e} ^ {\prime} (X) = e _ {k} \quad (k = 1, \dots , K).
$$

holds approximately. So we can analyze the observational data in the same way as the SRE stratified on $\hat{e}^{\prime}(X)$ . The ignorability holds only approximately given $\hat{e}^{\prime}(X)$ . We can further use regression adjustment based on covariates to remove bias and improve efficiency. To be more specific, we can obtain Lin (2013)'s estimator within each stratum and construct the final estimator by a weighted average (see Chapter 6.2.4).

With an unknown propensity score, we need to fit a statistical model to obtain the estimated propensity score $\hat{e}(X)$ . This makes the final estimator dependent on the model specification. However, the propensity score stratification estimator only requires the correct ordering of the estimated propensity scores rather than their exact values, which makes it relatively robust compared with other methods. This robustness property of propensity score stratification appeared in many numerical examples but its rigorous quantification is still missing in the literature.

An important practical question is how to choose $K$ ? If $K$ is too small, then ignorability does not hold conditional on $\hat{e}^{\prime}(X)$ even approximately. If $K$ is too large, then we do not have enough units within each stratum of the estimated propensity score and many strata have only treated or control units. Therefore, we face a trade-off. Following Cochran (1968)'s heuristics, Rosenbaum and Rubin (1983b) and Rosenbaum and Rubin (1984) suggested $K = 5$ which removes a large amount of bias in many settings. However, with extremely large datasets, propensity score stratification leads to biased estimators with a fixed $K$ (Lunceford and Davidian, 2004). It is thus reasonable to increase $K$ as long as each stratum still has enough treated and control units. Wang et al. (2020) suggested a greedy choice of $K$ , which is the maximum number of strata such that the stratified estimator is well-defined. However, the rigorous theory for this procedure is not fully established.

Another important practical question is how to compute the standard errors of the estimators based on propensity score stratification. Some researchers have conditioned on the discretized propensity scores $\hat{e}^{\prime}(X)$ and reported standard errors based on the SRE. This effectively ignores the uncertainty in the estimated propensity scores. This often leads to an overestimation of the true variance since a surprising result in the literature is that using the estimated propensity scores decreases the asymptotic variance for estimating the average causal effect (Su et al., 2023). Other researchers bootstrapped the whole procedure to account for full uncertainty. However, the theory for the bootstrap is still unclear due to the discreteness of this estimator.

![](images/61ee476056f81ce6294376dcb08a4077955ffe590b8ab615f0399f5468e61c41.jpg)  
FIGURE 11.1: Histograms of the estimated propensity scores based on the nhanes_bmi data: white for the control group and grey for the treatment group

# 11.1.3 Application

To illustrate the propensity score stratification method, I revisited Example 10.3.

> nhanes_bmi = read.csv("nhanes_bmi.csv")[, -1]   
> z = nhanes_bmi$Schoolmeal   
> y = nhanes_bmi$BMI   
> x = as.matrix(nhanes_bmi[, -c(1, 2)])   
> x = scale(x)

Example 10.3 introduced the covariates in the dataset. The treatment Schoolmeal is the indicator for participation in the school meal plan, and the outcome BMI is the BMI.

Figure 11.1 shows the histograms of the estimated propensity scores with different numbers of bins ( $K = 5, 10, 30$ ). Based on propensity score stratification, we can calculate the point estimators and the standard errors for difference choice of $K \in \{5, 10, 20, 50, 80\}$ as follows (with the function Neyman_SRE defined in Chapter 5 for analyzing the SRE):

> pscore = glm(z ~ x, family = binomial)$fitted.values   
> n.strata = c(5, 10, 20, 50, 80)   
> strat.res = sapply(n.strata, FUN = function(nn){   
+ q.pscore = quantile(pscore, (1: (nn-1)) / nn)   
+ ps.strata = cut(pscore, breaks = c(0,q.pscore,1),   
+ labels = 1:nn)   
+Neyman_SRE(z，y，ps.strata)}  
>   
> rownames(strat.res) = c("est", "se")   
> colnames(strat.res) = n.strata

```txt
> round(strat.res, 3)  
5 10 20 50 80  
est -0.116 -0.178 -0.200 -0.265 -0.204  
se 0.283 0.282 0.279 0.272 NA 
```

Increasing $K$ from 5 to 50 reduces the standard error. However, we cannot go as extreme as $K = 80$ because the standard error is not well-defined in some strata with only one treated or one control unit. The above estimators show a negative but insignificant effect of the meal program on BMI.

We can also compare the above estimator with the three simple regression estimators: the one without adjusting for any covariates, and Fisher's and Lin's estimators.

```txt
> DiM = lm(y ~ z)
> Fisher = lm(y ~ z + x)
> Lin = lm(y ~ z + x + z*x)
> res.regression = c(coef(DiM)[2], hccm(DiM)[2, 2]~0.5,
+     coef(Fisher)[2], hccm(Fisher)[2, 2]~0.5,
+     coef(Lin)[2], hccm(Lin)[2, 2]~0.5)
> res.regression = matrix(res.regression,
+         nrow = 2, ncol = 3)
> rownames(res.regression) = c("est", "se")
> colnames(res.regression) = c("naive", "fisher", "lin")
> round(res.regression, 3)
    naïve fisher lin
est 0.534 0.061 -0.017
se 0.225 0.227 0.226 
```

The naive difference in means differs greatly from the other methods due to the large imbalance in covariates. Fisher's estimator still gives a positive point estimate although it is not significant. Lin's estimator and the propensity score stratification estimators give qualitatively the same results. The propensity score stratification estimators are stable across different choices of $K$ .

# 11.2 Propensity score weighting

# 11.2.1 Theory

Theorem 11.2 If $Z \perp \perp \{Y(1), Y(0)\} \mid X$ and $0 < e(X) < 1$ , then

$$
E \{Y (1) \} = E \left\{\frac {Z Y}{e (X)} \right\}, \quad E \{Y (0) \} = E \left\{\frac {(1 - Z) Y}{1 - e (X)} \right\},
$$

and

$$
\tau = E \{Y (1) - Y (0) \} = E \left\{\frac {Z Y}{e (X)} - \frac {(1 - Z) Y}{1 - e (X)} \right\}.
$$

Before proving Theorem 11.2, it is important to note the additional assumption $0 < e(X) < 1$ . It is called the overlap or positivity condition. The formulas in Theorem 11.2 become infinity if $e(X) = 0$ or 1 for some values of $X$ . It is not a requirement only for the identification formulas based on propensity score weighting. Although it was not stated explicitly in Theorem 10.1, the conditional expectations $E(Y \mid Z = 1, X)$ and $E(Y \mid Z = 0, X)$ in the identification formula of $\tau$ in (10.6) is well defined only if $0 < e(X) < 1$ . The overlap condition can be viewed as a technical condition to ensure that the formulas in Theorems 10.1 and 11.2 are well defined. It can also cause some philosophical issues for causal inference with observational studies. When unit $i$ has $e(X_i) = 1$ , we always observe its potential outcome under the treatment, $Y_i(1)$ , but can never observe its potential outcome under the control, $Y_i(0)$ . In this case, the potential outcome $Y_i(0)$ may not even be well defined, making the definition of the causal effect ambiguous for unit $i$ . King and Zeng (2006) called $Y_i(0)$ an extreme counterfactual when $e(X_i) = 1$ , and discussed their dangers in causal inference. A similar problem arises if unit $i$ has $e(X_i) = 0$ .

In sum, $Z \Downarrow \{Y(1), Y(0)\} \mid X$ requires adequate covariates to ensure the conditional independence of the treatment and potential outcomes, and $0 < e(X) < 1$ requires residual randomness in the treatment conditional on the covariates. In fact, Rosenbaum and Rubin (1983b)'s definition of strong ignorability includes both of these conditions. In modern literature, they are often stated separately.

Proof of Theorem 11.2: I only prove the result for $E\{Y(1)\}$ because the proof of the result for $E\{Y(0)\}$ is similar. We have

$$
\begin{array}{l} E \left\{\frac {Z Y}{e (X)} \right\} \\ = E \left\{\frac {Z Y (1)}{e (X)} \right\} \\ = E \left[ E \left\{\frac {Z Y (1)}{e (X)} \mid X \right\} \right] \quad (\text {t o w e r p r o p e r t y}) \\ = E \left[ \frac {1}{e (X)} E \left\{Z Y (1) \mid X \right\} \right] \\ = E \left[ \frac {1}{e (X)} E (Z \mid X) E \{Y (1) \mid X \} \right] (\mathrm {s t r o n g i g n o r a b i l i t y}) \\ = E \left[ \frac {1}{e (X)} e (X) E \{Y (1) \mid X \} \right] \\ = E \left[ E \left\{Y (1) \mid X \right\} \right] \\ = E \{Y (1) \}. \\ \end{array}
$$

# 11.2.2 Inverse propensity score weighting estimators

Theorem 11.2 motivates the following moment estimator for the average causal effect:

$$
\hat {\tau} ^ {\mathrm {h t}} = \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {Z _ {i} Y _ {i}}{\hat {e} (X _ {i})} - \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {(1 - Z _ {i}) Y _ {i}}{1 - \hat {e} (X _ {i})},
$$

where $\hat{e}(X_i)$ is the estimated propensity score. This is the inverse propensity score weighting (IPW) estimator, which is also called the Horvitz-Thompson (HT) estimator. Horvitz and Thompson (1952) proposed it in survey sampling and Rosenbaum (1987a) used in causal inference with observational studies.

However, the estimator $\hat{\tau}^{\mathrm{ht}}$ has many problems. In particular, it is not invariant to the location transformation of the outcome. Proposition 11.1 states this problem precisely, with the proof relegated to Problem 11.3.

Proposition 11.1 (lack of invariance for the HT estimator) If we change $Y_{i}$ to $Y_{i} + c$ with a constant $c$ , then the HT estimator $\hat{\tau}^{\mathrm{ht}}$ becomes $\hat{\tau}^{\mathrm{ht}} + c(\hat{1}_{\mathrm{T}} - \hat{1}_{\mathrm{C}})$ , where

$$
\hat {1} _ {\mathrm {T}} = \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {Z _ {i}}{\hat {e} (X _ {i})}, \quad \hat {1} _ {\mathrm {C}} = \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {(1 - Z _ {i})}{1 - \hat {e} (X _ {i})}
$$

can be viewed as two different estimates of the constant 1.

In Proposition 11.1, I use the funny notation $\hat{1}_{\mathrm{T}}$ and $\hat{1}_{\mathrm{C}}$ because with the true propensity score these two terms both have expectation 1; see Problem 11.3 for more details. In general, $\hat{1}_{\mathrm{T}} - \hat{1}_{\mathrm{C}}$ is not zero in finite samples. Since adding a constant to every outcome should not change the average causal effect, the HT estimator is not reasonable because of its dependence on $c$ . A simple fix to the problem is to normalize the weights by $\hat{1}_{\mathrm{T}}$ and $\hat{1}_{\mathrm{C}}$ respectively, resulting in the following estimator

$$
\hat {\tau} ^ {\mathrm {h a j e k}} = \frac {\sum_ {i = 1} ^ {n} \frac {Z _ {i} Y _ {i}}{\hat {e} (X _ {i})}}{\sum_ {i = 1} ^ {n} \frac {Z _ {i}}{\hat {e} (X _ {i})}} - \frac {\sum_ {i = 1} ^ {n} \frac {(1 - Z _ {i}) Y _ {i}}{1 - \hat {e} (X _ {i})}}{\sum_ {i = 1} ^ {n} \frac {1 - Z _ {i}}{1 - \hat {e} (X _ {i})}}.
$$

This is the Hajek estimator due to Hajek (1971) in the context of survey sampling with varying probabilities. We can verify that the Hajek estimator is invariant to the location transformation. That is, if we replace $Y_{i}$ by $Y_{i} + c$ , then $\hat{\tau}^{\mathrm{hajek}}$ remains the same; see Problem 11.3. Moreover, many numerical studies have found that $\hat{\tau}^{\mathrm{hajek}}$ is much more stable than $\hat{\tau}^{\mathrm{ht}}$ in finite samples.

# 11.2.3 A problem of IPW and a fundamental problem of causal inference

Many asymptotic analyses require a strong overlap condition

$$
0 <   \alpha_ {\mathrm {L}} \leq e (X) \leq \alpha_ {\mathrm {U}} <   1,
$$

that is, the true propensity score is bounded away from 0 and 1. However, D'Amour et al. (2021) pointed out that this is a rather strong assumption, especially with many covariates. Chapter 20 will discuss this problem in detail.

Even if the strong overlap condition holds for the true propensity score, the estimated propensity scores can be close to 0 or 1. When this happens, the weighting estimators blow up to infinity, which results in extremely unstable behavior in finite samples. We can either truncate the estimated propensity score by changing it to

$$
\max \left[ \alpha_ {\mathrm {L}}, \min \{\hat {e} (X _ {i}), \alpha_ {\mathrm {U}} \} \right],
$$

or trim the observations by dropping units with $\hat{e}(X_i)$ outside the interval $[\alpha_{\mathrm{L}}, \alpha_{\mathrm{U}}]$ . Crump et al. (2009) suggested $\alpha_{\mathrm{L}} = 0.1$ and $\alpha_{\mathrm{U}} = 0.9$ , and Kurth et al. (2005) suggested $\alpha_{\mathrm{L}} = 0.05$ and $\alpha_{\mathrm{U}} = 0.95$ . Yang and Ding (2018b) established some asymptotic theory for trimming. Overall, although trimming often stabilizes the IPW estimators, it also injects additional arbitrariness into the procedure.

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

Revisiting Example 10.3, we can obtain the IPW estimators based on different truncations of the estimated propensity scores. The following results are the two weighting estimators with the bootstrap standard errors, with truncations at (0,1), (0.01,0.99), (0.05,0.95), and (0.1,0.9):

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

Moreover, for any function $h(\cdot)$ , we have

$$
E \left\{\frac {Z h (X)}{e (X)} \right\} = E \left\{\frac {(1 - Z) h (X)}{1 - e (X)} \right\} \tag {11.2}
$$

provided the existence of the moments on both sides of (11.2).

Theorem 11.3 does not require the ignorability assumption. It is about the treatment $Z$ and covariates $X$ only. The first part of Theorem 11.3 states that conditional on the propensity score, the treatment indicator, and the covariates are independent. Therefore, within the same level of the propensity score, the covariate distributions are balanced across the treatment and control groups. The second part of Theorem 11.3 states that an equivalent form of covariate balance based on the weighting form. I give a proof of Theorem 11.3 below.

Proof of Theorem 11.3: First, we show $Z \perp X \mid e(X)$ , that is,

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

Second, we show (11.2). We can use similar steps as the proof of Theorem 11.2. But given Theorem 11.2, we have a simpler proof. If we view $h(X)$ as an outcome, then its two potential outcomes are identical and ignorability holds: $Z \perp \{h(X), h(X)\} \mid X$ . The difference between the left-hand and right-hand sides of (11.2) is the average causal effect of $Z$ on $h(X)$ , which is zero.

# 11.3.2 Covariate balance check

The proof of Theorem 11.3 is simple. But Theorem 11.3 has useful implications for the statistical analysis. Before getting access to the outcome data, we can check whether the propensity score model is specified well enough to ensure the covariate balance in the data. Rubin (2007) viewed this as the design stage of the observational study, and Rubin (2008) argued that this can result in more objective causal inference because the design stage does not involve the values of the outcomes.<sup>1</sup>

In the propensity score stratification, we have the discretized estimated propensity score $\hat{e}^{\prime}(X)$ and approximately

$$
Z \text {止} X \mid \hat {e} ^ {\prime} (X) = e _ {k} \quad (k = 1, \dots , K).
$$

Therefore, we can check whether the covariate distributions are the same across the treatment and control groups within each stratum of the discretized estimated propensity score.

In propensity score weighting, we can view $h(X)$ as a pseudo outcome and estimate the average causal effect on $h(X)$ . Because the true average causal effect on $h(X)$ is 0, the estimate should not be significantly different from 0. A canonical choice of $h(X)$ is $X$ .

Let us revisit Example 10.3 again. Based on propensity score stratification with $K = 5$ , all the covariates are well-balanced across the treatment and control groups. Similar results hold for the Hajek estimator. The only exception is Food Stamp, the 7th covariate in Figure 11.2. Figure 11.2 shows the balance-checking results.

# 11.4 Homework Problems

# 11.1 Another version of Theorem 11.1

Prove that

$$
Z \bot \{Y (1), Y (0), X \} \mid e (X, Y (1), Y (0)). \tag {11.4}
$$

Remark: This result holds without assuming strong ignorability. It implies that

$$
Z \perp \perp \{Y (1), Y (0) \} \mid \{X, e (X, Y (1), Y (0) \}.
$$

Rosenbaum (2020) and Rosenbaum and Rubin (2023) pointed out the result in (11.4) and called $e(X, Y(1), Y(0))$ the principal unobserved covariate.

![](images/3ee2414fb11dad45f928da0eba2ecc44a0460276253859e18882830133d60119.jpg)

![](images/62cdde7c8622b2586a0f337fc59f2dff4c57bdea844698ed15820e63faf8d677.jpg)  
FIGURE 11.2: Balance check: point estimates and $95\%$ confidence intervals of the average causal effect on covariates

TABLE 11.1: Table 1 of Rosenbaum and Rubin (1983a)   

<table><tr><td>stratum by e(X)</td><td>treatment</td><td>number of patients</td><td>proportion improved</td></tr><tr><td rowspan="2">1</td><td>Surgical</td><td>26</td><td>0.54</td></tr><tr><td>Medical</td><td>277</td><td>0.35</td></tr><tr><td rowspan="2">2</td><td>Surgical</td><td>68</td><td>0.70</td></tr><tr><td>Medical</td><td>235</td><td>0.40</td></tr><tr><td rowspan="2">3</td><td>Surgical</td><td>98</td><td>0.70</td></tr><tr><td>Medical</td><td>205</td><td>0.35</td></tr><tr><td rowspan="2">4</td><td>Surgical</td><td>164</td><td>0.71</td></tr><tr><td>Medical</td><td>139</td><td>0.30</td></tr><tr><td rowspan="2">5</td><td>Surgical</td><td>234</td><td>0.70</td></tr><tr><td>Medical</td><td>69</td><td>0.39</td></tr></table>

# 11.2 Another version of Theorem 11.1

Theorem 11.1 states a result under strong ignorability. An analogous result also holds under ignorability. That is, if ignorability holds conditional on covariates $X$ , then it also holds conditional on the scalar propensity score $e(X)$ .

Theorem 11.4 If $Z \perp Y(z) \mid X$ for $z = 0,1$ , then $Z \perp Y(z) \mid e(X)$ for $z = 0,1$ .

Prove Theorem 11.4.

# 11.3 More results on the IPW estimators

This is related to the discussion of the HT estimator in Section 11.2.2. First, prove Proposition 11.1. Second, prove

$$
E \left\{\frac {1}{n} \sum_ {i = 1} ^ {n} \frac {Z _ {i}}{e (X _ {i})} \right\} = 1, \quad E \left\{\frac {1}{n} \sum_ {i = 1} ^ {n} \frac {(1 - Z _ {i})}{1 - e (X _ {i})} \right\} = 1.
$$

Third, prove that if we add a constant $c$ to every observed outcome $Y_{i}$ , the Hajek estimator $\hat{\tau}^{\mathrm{hajek}}$ remains the same.

# 11.4 Re-analysis of Rosenbaum and Rubin (1983a)

Table 11.1 is from Rosenbaum and Rubin (1983a), which concerned the causal effect of the coronary artery bypass surgery compared with the medical therapy on the functional improvement 6 months after cardiac catheterization. They first estimated the propensity score based on 74 observed covariates and then formed 5 strata based on the discretized estimated propensity score. Because the treatment is binary and the outcome is also binary, they represented the data in a table. Based on Table 11.1, estimate the average causal effect, and report the $95\%$ confidence interval of the average causal effect.

Remark: If you are interested, you can read the whole paper of Rosenbaum

and Rubin (1983a) after reading Part IV of the book. It is a canonical paper on sensitivity analysis in causal inference.

# 11.5 Balancing score and propensity score: more theoretical results

Rosenbaum and Rubin (1983b) also introduced the notion of balancing score.

Definition 11.2 (balancing score) $b(X)$ is a balancing score if

$$
Z \perp \perp X \mid b (X).
$$

In Definition 11.2, $b(X)$ can be a scalar or a vector. An obvious balancing score is $b(X) = X$ , but it is not a useful one without any simplification of the original covariates. By Theorem 11.3, the propensity score is a special balancing score. More interestingly, Rosenbaum and Rubin (1983b) showed that the propensity score is the coarsest balancing score, as in Theorem 11.5 below which includes Theorem 11.3 as a special case.

Theorem 11.5 $b(X)$ is a balancing score if and only if $b(X)$ is finer than $e(X)$ in the sense that $e(X) = f(b(X))$ for some function $f(\cdot)$ .

Theorem 11.5 is relevant in subgroup analysis. In particular, we may be interested in not only the average causal effect $\tau$ but also the subgroup effects. For instance, we may want to estimate the average causal effects among boys and girls, respectively. Without loss of generality, assume the first component of $X$ is the indicator for girls, and we are interested in estimating

$$
\tau (x _ {1}) = E \{Y (1) - Y (0) \mid X _ {1} = x _ {1} \}, \quad (x _ {1} = 1, 0).
$$

Theorem 11.5 implies that under ignorability, we also have

$$
Z \perp \perp \{Y (1), Y (0) \} \mid e (X), X _ {1} \tag {11.5}
$$

because $b(X) = \{e(X), X_1\}$ is finer than $e(X)$ and thus a balancing score. The conditional independence in (11.5) ensures ignorability holds given the propensity score, within each level of $X_1$ . Therefore, we can perform the same analysis based on the propensity score, within each level of $X_1$ , yielding estimates for two subgroup effects.

With the above motivation in mind, now prove Theorem 11.5.

# 11.6 Some basics of subgroup effects

This problem is related to Problem 11.5, but you can work on it independently.

Consider a standard observational study with covariates $X = (X_{1},X_{2})$ , where $X_{1}$ denotes a binary subgroup indicator (e.g., statistics major or not statistics major) and $X_{2}$ contains the rest of the covariates. The parameter of interest is the subgroup causal effect

$$
\tau (x _ {1}) = E \{Y (1) - Y (0) \mid X _ {1} = x _ {1} \}, \quad (x _ {1} = 1, 0).
$$

Show that

$$
\tau (x _ {1}) = E \left\{\frac {1 (X _ {1} = x _ {1}) Z Y}{e (X)} - \frac {1 (X _ {1} = x _ {1}) (1 - Z) Y}{1 - e (X)} \right\} \Big / \operatorname * {p r} (X _ {1} = x _ {1})
$$

and give the corresponding HT and Hajek estimators for $\tau(x_1)$ .

# 11.7 Recommended reading

The title of this chapter is the same as the title of the classic paper by Rosenbaum and Rubin (1983b). Most results in this chapter are directly drawn from their original paper.

Rubin (2007) and Rubin (2008) highlighted the importance of the design stage of observational studies for more objective causal inference

# 12

# The Doubly Robust or the Augmented Inverse Propensity Score Weighting Estimator for the Average Causal Effect

Under ignorance $Z \sqcup \{Y(1), Y(0)\} \mid X$ and overlap $0 < e(X) < 1$ , Chapter 11 has shown two identification formulas of the average causal effect $\tau = E\{Y(1) - Y(0)\}$ . First, the outcome regression formula is

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

# 12.1 The doubly robust estimator

# 12.1.1 Population version

We posit a model for the conditional means of the outcome $\mu_1(X, \beta_1)$ and $\mu_0(X, \beta_0)$ , indexed by the parameters $\beta_1$ and $\beta_0$ . For example, if the conditional means are linear or logistic under the working model, then the parameters are just the regression coefficients. If the outcome model is correctly specified, then $\mu_1(X, \beta_1) = \mu_1(X)$ and $\mu_0(X, \beta_0) = \mu_0(X)$ . We posit a working model for the propensity score $e(X, \alpha)$ , indexed by the parameter $\alpha$ . For example, if the working model is logistic, then $\alpha$ is the regression coefficient. If the propensity score model is correctly specified, then $e(X, \alpha) = e(X)$ . In practice, both models may be misspecified. Sometimes, we call them working models due to the possibility of misspecification.

Define

$$
\tilde {\mu} _ {1} ^ {\mathrm {d r}} = E \left[ \frac {Z \{Y - \mu_ {1} (X , \beta_ {1}) \}}{e (X , \alpha)} + \mu_ {1} (X, \beta_ {1}) \right], \tag {12.3}
$$

$$
\tilde {\mu} _ {0} ^ {\mathrm {d r}} = E \left[ \frac {(1 - Z) \{Y - \mu_ {0} (X , \beta_ {0}) \}}{1 - e (X , \alpha)} + \mu_ {0} (X, \beta_ {0}) \right], \tag {12.4}
$$

which can also be written as

$$
\tilde {\mu} _ {1} ^ {\mathrm {d r}} = E \left[ \frac {Z Y}{e (X , \alpha)} - \frac {Z - e (X , \alpha)}{e (X , \alpha)} \mu_ {1} (X, \beta_ {1}) \right], \tag {12.5}
$$

$$
\tilde {\mu} _ {0} ^ {\mathrm {d r}} = E \left[ \frac {(1 - Z) Y}{1 - e (X , \alpha)} - \frac {e (X , \alpha) - Z}{1 - e (X , \alpha)} \mu_ {0} (X, \beta_ {0}) \right]. \tag {12.6}
$$

The formulas in (12.3) and (12.4) augment the outcome regression estimator by inverse propensity score weighting terms of the residuals. The formulas in (12.5) and (12.6) augment the IPW estimator by the imputed outcomes. For this reason, the doubly robust estimator is also called the augmented inverse propensity score weighting (AIPW) estimator.

The augmentation strengthens the theoretical properties in the following sense.

Theorem 12.1 Assume $\text{ignorability } Z \perp \{Y(1), Y(0)\} \mid X$ and overlap $0 < e(X) < 1$ .

1. If either $e(X, \alpha) = e(X)$ or $\mu_1(X, \beta_1) = \mu_1(X)$ , then $\tilde{\mu}_1^{\mathrm{dr}} = E\{Y(1)\}$ .   
2. If either $e(X, \alpha) = e(X)$ or $\mu_0(X, \beta_0) = \mu_0(X)$ , then $\tilde{\mu}_0^{\mathrm{dr}} = E\{Y(0)\}$ .   
3. If either $e(X, \alpha) = e(X)$ or $\{\mu_1(X, \beta_1) = \mu_1(X), \mu_0(X, \beta_0) = \mu_0(X)\}$ , then $\tilde{\mu}_1^{\mathrm{dr}} - \tilde{\mu}_0^{\mathrm{dr}} = \tau$ .

By Theorem 12.1, $\tilde{\mu}_1^{\mathrm{dr}} - \tilde{\mu}_0^{\mathrm{dr}}$ equals $\tau$ if either the propensity score model or the outcome model is correctly specified. That's why it is called the doubly robust estimator.

Proof of Theorem 12.1: I only prove the result for $\mu_1 = E\{Y(1)\}$ . The proof for the result for $\mu_0 = E\{Y(0)\}$ is similar.

We have the decomposition

$$
\begin{array}{l} \tilde {\mu} _ {1} ^ {\mathrm {d r}} - E \{Y (1) \} \\ = E \left[ \frac {Z \left\{Y (1) - \mu_ {1} (X , \beta_ {1}) \right\}}{e (X , \alpha)} - \left\{Y (1) - \mu_ {1} (X, \beta_ {1}) \right\} \right] \quad (\text {b y}) \\ = E \left[ \frac {Z - e (X , \alpha)}{e (X , \alpha)} \left\{Y (1) - \mu_ {1} (X, \beta_ {1}) \right\} \right] \quad (\text {c o m b i n i n g t e r m s}) \\ = E \left(E \left[ \frac {Z - e (X , \alpha)}{e (X , \alpha)} \left\{Y (1) - \mu_ {1} (X, \beta_ {1}) \right\} \mid X \right]\right) \quad (\text {t o w e r p r o p e r t y}) \\ = E \left[ E \left\{\frac {Z - e (X , \alpha)}{e (X , \alpha)} \mid X \right\} \times E \left\{Y (1) - \mu_ {1} (X, \beta_ {1}) \mid X \right\} \right] \quad (\text {i g n o r a b i l i t y}) \\ = E \left[ \frac {e (X) - e (X , \alpha)}{e (X , \alpha)} \times \left\{\mu_ {1} (X) - \mu_ {1} (X, \beta_ {1}) \right\} \right]. \\ \end{array}
$$

Therefore, $\tilde{\mu}_1^{\mathrm{dr}} - E\{Y(1)\} = 0$ if either $e(X,\alpha) = e(X)$ or $\mu_1(X,\beta_1) = \mu_1(X)$ .

# 12.1.2 Sample version

Based on the population versions of $\tilde{\mu}_1^{\mathrm{dr}}$ and $\tilde{\mu}_0^{\mathrm{dr}}$ , we can obtain their sample analogs to construct a doubly robust estimator for $\tau$ .

Definition 12.1 (doubly robust estimator for the average causal effect) Based on the data $(X_{i},Z_{i},Y_{i})_{i = 1}^{n}$ , we can obtain a doubly robust estimator for $\tau$ by the following steps:

1. obtain the fitted values of the propensity scores: $e(X_i, \hat{\alpha})$ ;

2. obtain the fitted values of the outcome means: $\mu_1(X_i, \hat{\beta}_1)$ and $\mu_0(X_i, \hat{\beta}_0)$ ;

3. construct the doubly robust estimator: $\hat{\tau}^{\mathrm{dr}} = \hat{\mu}_1^{\mathrm{dr}} - \hat{\mu}_0^{\mathrm{dr}}$ , where

$$
\hat {\mu} _ {1} ^ {\mathrm {d r}} = \frac {1}{n} \sum_ {i = 1} ^ {n} \left[ \frac {Z _ {i} \{Y _ {i} - \mu_ {1} (X _ {i} , \hat {\beta} _ {1}) \}}{e (X _ {i} , \hat {\alpha})} + \mu_ {1} (X _ {i}, \hat {\beta} _ {1}) \right]
$$

and

$$
\hat {\mu} _ {0} ^ {\mathrm {d r}} = \frac {1}{n} \sum_ {i = 1} ^ {n} \left[ \frac {(1 - Z _ {i}) \{Y _ {i} - \mu_ {0} (X _ {i} , \hat {\beta} _ {0}) \}}{1 - e (X _ {i} , \hat {\alpha})} + \mu_ {0} (X _ {i}, \hat {\beta} _ {0}) \right].
$$

By Definition 12.1, we can also write the doubly robust estimator as

$$
\hat {\tau} ^ {\mathrm {d r}} = \hat {\tau} ^ {\mathrm {r e g}} + \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {Z _ {i} \{Y _ {i} - \mu_ {1} (X _ {i} , \hat {\beta} _ {1}) \}}{e (X _ {i} , \hat {\alpha})} - \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {(1 - Z _ {i}) \{Y _ {i} - \mu_ {0} (X _ {i} , \hat {\beta} _ {0}) \}}{1 - e (X _ {i} , \hat {\alpha})}.
$$

Analogous to (12.5) and (12.6), we can also rewrite it as

$$
\hat {\tau} ^ {\mathrm {d r}} = \hat {\tau} ^ {\mathrm {i p w}} - \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {Z _ {i} - e (X _ {i} , \hat {\alpha})}{e (X _ {i} , \hat {\alpha})} \mu_ {1} (X _ {i}, \hat {\beta} _ {1}) + \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {e (X _ {i} , \hat {\alpha}) - Z _ {i}}{1 - e (X _ {i} , \hat {\alpha})} \mu_ {0} (X _ {i}, \hat {\beta} _ {0}).
$$

Funk et al. (2011) suggested to approximate the variance of $\hat{\tau}^{\mathrm{dr}}$ via the nonparametric bootstrap by resampling from $(Z_{i},X_{i},Y_{i})_{i = 1}^{n}$ .

# 12.2 More intuition and theory for the doubly robust estimator

Although the beginning of this chapter claims that the basic identification formulas based on outcome regression and IPW immediately yield infinitely many other identification formulas, the particular forms of the doubly robust estimators in (12.3) and (12.4) are not obvious to come up with. The original motivation for (12.3) and (12.4) was quite theoretical, and relied on something called the semiparametric efficiency theory in advanced mathematical statistics (Bickel et al., 1993). It is beyond the level of this book. Below I will give two intuitive perspectives to construct (12.3) and (12.4). Both Sections 12.2.1 and 12.2.2 below focus on the estimation of $E\{Y(1)\}$ since the estimation of $E\{Y(0)\}$ is similar by symmetry.

# 12.2.1 Reducing the variance of the IPW estimator

The IPW estimator for $\mu_{1}$ based on

$$
\mu_ {1} = E \left\{\frac {Z Y}{e (X)} \right\}
$$

completely ignores the outcome model of $Y$ . It has the advantage of being consistent without assuming any outcome model. However, if the covariates are predictive of the outcome, the residual based on a working outcome model usually has a smaller variance than the outcome even when this working outcome model is wrong. With a possibly misspecified outcome model $\mu_1(X, \beta_1)$ , a trivial decomposition holds:

$$
\mu_ {1} = E \{Y (1) \} = E \{Y (1) - \mu_ {1} (X, \beta_ {1}) \} + E \{\mu_ {1} (X, \beta_ {1}) \}.
$$

If we apply the IPW formula to the first term in the above formula viewing $Y(1) - \mu_1(X, \beta_1)$ as a "pseudo potential outcome" under the treatment, we can rewrite the above formula as

$$
\begin{array}{l} \mu_ {1} = E \left\{\frac {Z \left\{Y - \mu_ {1} (X , \beta_ {1}) \right\}}{e (X)} \right\} + E \left\{\mu_ {1} (X, \beta_ {1}) \right\} (12.7) \\ = E \left\{\frac {Z \{Y - \mu_ {1} (X , \beta_ {1}) \}}{e (X)} + \mu_ {1} (X, \beta_ {1}) \right\}, (12.8) \\ \end{array}
$$

which holds if the propensity score model is correct without assuming that the outcome model is correct. Using a working model to improve efficiency is an old idea from survey sampling. Little and An (2004) and Lumley et al. (2011) pointed out its connection with the doubly robust estimator.

# 12.2.2 Reducing the bias of the outcome regression estimator

The discussion in Section 12.2.1 starts with the IPW estimator and improves its efficiency based on a working outcome model. Alternatively, we can also start with an outcome regression estimator based on

$$
\tilde {\mu} _ {1} = E \left\{\mu_ {1} (X, \beta_ {1}) \right\}
$$

which may not be the same as $\mu_{1}$ since the outcome model may be wrong. The bias of this estimator is $E\{\mu_1(X,\beta_1) - Y(1)\}$ , which can be estimated by an IPW estimator

$$
B = E \left\{\frac {Z \left\{\mu_ {1} (X , \beta_ {1}) - Y \right\}}{e (X)} \right\}
$$

if the propensity score model is correct. So a de-biased estimator is $\tilde{\mu}_1 - B$ , which is identical to (12.8).

# 12.3 Examples

# 12.3.1 Summary of some canonical estimators for $\tau$

The following $\mathbb{R}$ code implements the outcome regression, HT, Hajek, and doubly robust estimators for $\tau$ . These estimators can be conveniently implemented based on the fitted values of the glm function. The default choice for the propensity score model is the logistic model, and the default choice for the outcome model is the linear model with out.family = gaussian². For binary outcomes, we can also specify out.family = binomial to fit the logistic model.

```r
OS_est = function(z, y, x, out.family = gaussian,
truncps = c(0, 1))
{
    ## fitted propensity score
    pscore = glm(z ~ x, family = binomial) $fitted.values
    pscore = pmax(truncps[1], Tmin(truncps[2], pscore))
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

It is tedious to calculate the analytic formulas for the variances of the above estimators. The bootstrap provides convenient approximations to the variances based on resampling from $\{Z_i, X_i, Y_i\}_{i=1}^n$ . Building upon the function $\mathsf{OS\_est}$ above, the following function returns point estimators as well as the bootstrap standard errors.

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

We set the sample size to be $n = 500$ and generate 500 independent data sets according to the data-generating processes above. In case 1,

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

The two weighting estimators are much larger than the other two estimators. Truncating the estimated propensity score at $[0.1, 0.9]$ , we obtain the following estimators and bootstrap standard errors:

<table><tr><td></td><td>reg</td><td>HT</td><td>Hajek</td><td>DR</td></tr><tr><td>est</td><td>-0.017</td><td>-0.713</td><td>-0.054</td><td>-0.043</td></tr><tr><td>se</td><td>0.223</td><td>0.422</td><td>0.235</td><td>0.231</td></tr></table>

The Hajek estimator becomes much closer to the outcome regression and doubly robust estimators, while the Horvitz-Thompson estimator is still an outlier.

# 12.4 Some further discussion

Recall the proof of Theorem 12.1, the key for the double robustness property is the product structure in

$$
\tilde {\mu} _ {1} ^ {\mathrm {d r}} - E \{Y (1) \} = E \left[ \frac {e (X) - e (X , \alpha)}{e (X , \alpha)} \times \{\mu_ {1} (X) - \mu_ {1} (X, \beta_ {1}) \} \right],
$$

which ensures that the estimation error is zero if either $e(X) = e(X, \alpha)$ or $\mu_1(X) = \mu_1(X, \beta_1)$ . This delicate structure renders the doubly robust estimator possibly doubly fragile when both the propensity score and the outcome models are misspecified. The product of two errors multiply to yield potentially much larger errors. The simulation in Chapter 12.3.2 confirms this point.

Kang and Schafer (2007) criticized the doubly robust estimator based on simulation studies. They found that the finite-sample performance of the doubly robust estimator can be even wilder than the simple outcome regression and IPW estimators. Despite the critique from Kang and Schafer (2007), the doubly robust estimator has been a standard strategy in causal inference since the seminal work of Scharfstein et al. (1999). Recently, it was resurrected in the theoretical statistics and econometrics literature with a fancier name "double machine learning" (Chernozhukov et al., 2018). The basic idea is to replace the working models for the propensity score and outcome with machine learning tools which can be viewed as more flexible models than the traditional parametric models.

# 12.5 Homework problems

# 12.1 A sanity check

Consider the case in which the covariate is discrete $X \in \{1, \ldots, K\}$ and the parameter of interest is $\tau$ . Without imposing any model assumptions, the estimated propensity score $\hat{e}(X)$ equals $\hat{e}_{[k]} = \hat{\mathrm{pr}}(Z = 1 \mid X = k)$ , the proportion of units receiving the treatment, and the estimated outcome means are the sample means of the outcomes $\hat{Y}_{[k]}(1) = \hat{E}(Y \mid Z = 1, X = k)$ and $\hat{Y}_{[k]}(0) = \hat{E}(Y \mid Z = 0, X = k)$ under treatment, within stratum $X = k$ ( $k = 1, \ldots, K$ ). Show that the stratified estimator, outcome regression estimator, HT estimator, Hajek estimator, and doubly robust estimator are all identical numerically.

# 12.2 An alternative form of the doubly robust estimator for $\tau$

Motivated by (12.7), we have an alternative form of the doubly robust estimator for $\mu_{1} = E\{Y(1)\}$ :

$$
\tilde {\mu} _ {1} ^ {\mathrm {d r 2}} = \frac {E \left[ \frac {Z \{Y - \mu_ {1} (X , \beta_ {1}) \}}{e (X , \alpha)} \right]}{E \left[ \frac {Z}{e (X , \alpha)} \right]} + E \{\mu_ {1} (X, \beta_ {1}) \}.
$$

Show that $\tilde{\mu}_1^{\mathrm{dr2}} = \mu_1$ if either $e(X, \alpha) = e(X)$ or $\mu_1(X, \beta_1) = \mu_1(X)$ . Give the analogous formula for estimating $\mu_0$ . Give the sample analog of the doubly robust estimator for $\tau$ based on these formulas.

Remark: This form of doubly robust estimator appeared in Robins et al. (2007).

# 12.3 An upper bound of the bias of the doubly robust estimator

Consider the population version of the doubly robust estimator $\tilde{\mu}_1^{\mathrm{dr}}$ for $E\{Y(1)\}$ . Show that

$$
| \tilde {\mu} _ {1} ^ {\mathrm {d r}} - E \{Y (1) \} | \leq \sqrt {E \left[ \frac {\{e (X) - e (X , \alpha) \} ^ {2}}{e (X , \alpha) ^ {2}} \right] \times E \left[ \{\mu_ {1} (X) - \mu_ {1} (X , \beta_ {1}) \} ^ {2} \right]}.
$$

Find the analogous upper bound for the bias of $\tilde{\mu}_0^{\mathrm{dr}}$ for $E\{Y(0)\}$ .

Remark: You may find Section A.1.4 useful for the proof.

# 12.4 Data analysis of Example 10.1

Analyze the dataset cps1re74.csv using the methods discussed so far.

# 12.5 Analyzing a dataset from the Karolinska Institute

Rubin (2008) used the dataset karolinska.txt to illustrate the ideas of causal inference in observational studies. The dataset has 158 cardia cancer patients diagnosed between 1988 and 1995 in Central and Northern Sweden, 79 diagnosed at large volume hospitals, defined as treating more than ten patients with cardia cancer during that period, and 79 diagnosed at the remaining small volume hospitals. The treatment $\mathbf{z}$ is the indicator of whether a patient was diagnosed at a large volume hospital. The outcome $\mathbf{y}$ is whether the patient survived longer than 1 year after the diagnosis. The covariates $\mathbf{x}$ contain information about age, whether a patient was from a rural area, and whether a patient was male.

```txt
karolinska = read.table("karolinska.txt", header = TRUE)  
z = karolinska$hvdiag  
y = 1 - (karolinska$year survived == 1)  
x = as.matrix(karolinska[, c(3, 4, 5)]) 
```

Analyze the dataset using the methods discussed so far.

# 12.6 Recommended reading

Lunceford and Davidian (2004) gave a review and comparison of many methods discussed in Chapters 11 and 12.

# The Average Causal Effect on the Treated Units and Other Estimands

Chapters 10-12 focused on the identification and estimation of the average causal effect $\tau = E\{Y(1) - Y(0)\}$ under the ignorability and overlap assumptions. Conceptually, it is straightforward to extend the discussion to the average causal effects on the treated and control units:

$$
\begin{array}{l} \tau_ {\mathrm {T}} = E \{Y (1) - Y (0) \mid Z = 1 \}, \\ \tau_ {\mathrm {C}} = E \{Y (1) - Y (0) \mid Z = 0 \}. \\ \end{array}
$$

If $\tau_{\mathrm{T}}$ and $\tau_{\mathrm{C}}$ differ from $\tau$ , then the average causal effects are heterogeneous across the treatment and control groups. Whether we should estimate $\tau_{\mathrm{T}}, \tau_{\mathrm{C}}$ or $\tau$ depends on the practical question of interest.

Because of the symmetry, this chapter focuses on $\tau_{\mathrm{T}}$ . Chapter 13.4 also discusses extensions to other estimands.

# 13.1 Nonparametric identification of $\tau_{\mathrm{T}}$

The average causal effect on the treated units equals

$$
\tau_ {\mathrm {T}} = E (Y \mid Z = 1) - E \{Y (0) \mid Z = 1 \},
$$

where the first term $E(Y \mid Z = 1)$ is directly identifiable from the data and the second term $E\{Y(0) \mid Z = 1\}$ is counterfactual. The key assumption to identify the second term is the following ignorability and overlap assumptions.

Assumption 13.1 $Z \bot Y(0) \mid X$ and $e(X) < 1$ .

Because the key is to identify $E\{Y(0) \mid Z = 1\}$ , we only need the "onesided" ignorability and overlap assumptions. Under Assumption 13.1, we have the following identification result for $\tau_{\mathrm{T}}$ .

Theorem 13.1 Under Assumption 13.1, we have

$$
\begin{array}{l} E \{Y (0) \mid Z = 1 \} = E \left\{E (Y \mid Z = 0, X) \mid Z = 1 \right\} \\ = \int E (Y \mid Z = 0, X = x) f (x \mid Z = 1) \mathrm {d} x. \\ \end{array}
$$

# 18213 The Average Causal Effect on the Treated Units and Other Estimands

By Theorem 13.1 the counterfactual mean $E\{Y(0) \mid Z = 1\}$ equals the conditional mean of the observed outcomes under the control, averaged over the distribution of the covariates under the treatment. It implies that $\tau_{\mathrm{T}}$ is nonparametrically identified by

$$
\tau_ {\mathrm {T}} = E (Y \mid Z = 1) - E \left\{E (Y \mid Z = 0, X) \mid Z = 1 \right\} \tag {13.1}
$$

Proof of Theorem 13.1: We have

$$
\begin{array}{l} E \{Y (0) \mid Z = 1 \} = E \left[ E \{Y (0) \mid Z = 1, X \} \mid Z = 1 \right] \\ = E \left[ E \{Y (0) \mid Z = 0, X \} \mid Z = 1 \right] \\ = E \left\{E (Y \mid Z = 0, X) \mid Z = 1 \right\} \\ = \int E (Y \mid Z = 0, X = x) f (x \mid Z = 1) \mathrm {d} x. \\ \end{array}
$$

![](images/927d764d20b9893ff071c0738b1ff49c8846638c2a3765ef1e6e6988c6d1eb6d.jpg)

With a discrete $X$ , the identification formula in Theorem 13.1 reduces to

$$
E \{Y (0) \mid Z = 1 \} = \sum_ {k = 1} ^ {K} E (Y \mid Z = 0, X = k) \Pr (X = k \mid Z = 1),
$$

motivating the following stratified estimator for $\tau_{\mathrm{T}}$

$$
\hat {\tau} _ {\mathrm {T}} = \hat {\bar {Y}} (1) - \sum_ {k = 1} ^ {K} \hat {\pi} _ {[ k ] | 1} \hat {\bar {Y}} _ {[ k ]} (0),
$$

where $\hat{\pi}_{[k]|1} = n_{[k]1} / n_1$ is the proportion of category $k$ of $X$ among the treated units.

For continuous $X$ , we need to fit an outcome model for $E(Y \mid Z = 0, X)$ using the control units. If the fitted values for the control potential outcomes are $\hat{\mu}_0(X_i)$ , then the outcome regression estimator is

$$
\hat {\tau} _ {\mathrm {T}} ^ {\mathrm {r e g}} = \hat {\bar {Y}} (1) - n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} \hat {\mu} _ {0} (X _ {i}) = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} \{Y _ {i} - \hat {\mu} _ {0} (X _ {i}) \}.
$$

Example 13.1 If we specify a linear model for all units

$$
E (Y \mid Z, X) = \beta_ {0} + \beta_ {z} Z + \beta_ {x} ^ {\mathrm {T}} X,
$$

then

$$
\begin{array}{l} \tau_ {\mathrm {T}} = E \left\{E (Y \mid Z = 1, X) - E (Y \mid Z = 0, X) \mid Z = 1 \right\} \\ = \beta_ {z}. \\ \end{array}
$$

If we run OLS to obtain $(\hat{\beta}_0, \hat{\beta}_z, \hat{\beta}_x)$ , then we can use $\hat{\beta}_z$ to estimate $\tau_{\mathrm{T}}$ . Section 10.4.2 shows that $\hat{\beta}_z$ is an estimator for $\tau$ , and this example further shows that $\hat{\beta}_z$ is an estimator for $\tau_{\mathrm{T}}$ . This is not surprising because the linear model assumes constant causal effects across units.

# 13.2 Inverse propensity score weighting and doubly robust estimation of $\tau_{\mathrm{T}}$ 183

Example 13.2 The identification formula depends only on $E(Y \mid Z = 0, X)$ , so we need only to specify a model for the control units. When this model is linear,

$$
E (Y \mid Z = 0, X) = \beta_ {0 | 0} + \beta_ {x | 0} ^ {\mathsf {T}} X,
$$

we have

$$
\begin{array}{l} \tau_ {\mathrm {T}} = E (Y \mid Z = 1) - E \left(\beta_ {0 | 0} + \beta_ {x | 0} ^ {\mathrm {T}} X \mid Z = 1\right) \\ = E (Y \mid Z = 1) - \beta_ {0 | 0} - \beta_ {x | 0} ^ {\mathsf {T}} E (X \mid Z = 1). \\ \end{array}
$$

If we run OLS with only the control units to obtain $(\hat{\beta}_{0|0},\hat{\beta}_{x|0})$ , then the estimator is

$$
\hat {\tau} _ {\mathrm {T}} = \hat {\bar {Y}} (1) - \hat {\beta} _ {0 | 0} - \hat {\beta} _ {x | 0} ^ {\mathsf {T}} \hat {\bar {X}} (1).
$$

Using the property of the OLS (see B.5), we have

$$
\hat {\tilde {Y}} (0) = \hat {\beta} _ {0 | 0} + \hat {\beta} _ {x | 0} ^ {\mathsf {T}} \hat {\tilde {X}} (0).
$$

Therefore, the above estimator reduces to

$$
\hat {\tau} _ {\mathrm {T}} = \left\{\hat {\bar {Y}} (1) - \hat {\bar {Y}} (0) \right\} - \beta_ {x | 0} ^ {\mathrm {T}} \left\{\hat {\bar {X}} (1) - \hat {\bar {X}} (0) \right\},
$$

which is similar to $(\ref{eq:1})$ with a different coefficient for the difference in means of the covariates.

As an algebraic fact, we can show that this estimator equals the coefficient of $Z$ in the OLS fit of the outcome on the treatment, covariates, and their interactions, with the covariates centered as $X_{i} - \hat{\bar{X}}(1)$ . See Problem 13.2 for more details.

# 13.2 Inverse propensity score weighting and doubly robust estimation of $\tau_{\mathrm{T}}$

Theorem 13.2 Under Assumption 13.1, we have

$$
E \{Y (0) \mid Z = 1 \} = E \left\{\frac {e (X)}{e} \frac {1 - Z}{1 - e (X)} Y \right\} \tag {13.2}
$$

and

$$
\tau_ {\mathrm {T}} = E (Y \mid Z = 1) - E \left\{\frac {e (X)}{e} \frac {1 - Z}{1 - e (X)} Y \right\}, \tag {13.3}
$$

where $e = \operatorname{pr}(Z = 1)$ is the marginal probability of the treatment.

Proof of Theorem 13.2: The left-hand side of (13.2) equals

$$
\begin{array}{l} E \{Y (0) \mid Z = 1 \} = E \{Z Y (0) \} / e \\ = E \left[ E (Z \mid X) E \{Y (0) \mid X \} \right] / e \\ = E \left[ e (X) E \{Y (0) \mid X \} \right] / e. \\ \end{array}
$$

The right-hand side of (13.2) equals

$$
\begin{array}{l} E \left\{\frac {e (X)}{e} \frac {1 - Z}{1 - e (X)} Y \right\} = E \left[ E \left\{\frac {e (X)}{e} \frac {1 - Z}{1 - e (X)} Y (0) \mid X \right\} \right] \\ = E \left[ \frac {e (X)}{e \left\{1 - e (X) \right\}} E \left\{(1 - Z) Y (0) \mid X \right\} \right] \\ = E \left[ \frac {e (X)}{e \{1 - e (X) \}} E (1 - Z \mid X) E \{Y (0) \mid X \} \right] \\ = E [ e (X) E \{Y (0) \mid X \} ] / e. \\ \end{array}
$$

So (13.2) holds.

We have two IPW estimators

$$
\hat {\tau} _ {\mathrm {T}} ^ {\mathrm {h t}} = \hat {\bar {Y}} (1) - n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} \hat {o} (X _ {i}) (1 - Z _ {i}) Y _ {i}
$$

and

$$
\hat {\tau} _ {\mathrm {T}} ^ {\mathrm {h a j e k}} = \hat {\bar {Y}} (1) - \frac {\sum_ {i = 1} ^ {n} \hat {o} (X _ {i}) (1 - Z _ {i}) Y _ {i}}{\sum_ {i = 1} ^ {n} \hat {o} (X _ {i}) (1 - Z _ {i})},
$$

where $\hat{o}(X_i) = \hat{e}(X_i) / \{1 - \hat{e}(X_i)\}$ is the fitted odds of the treatment given covariates.

We also have a doubly robust estimator for $E\{Y(0) \mid Z = 1\}$ which combines the propensity score and the outcome models. Define

$$
\tilde {\mu} _ {0 \mathrm {T}} ^ {\mathrm {d r}} = E [ o (X, \alpha) (1 - Z) \{Y - \mu_ {0} (X, \beta_ {0}) \} + Z \mu_ {0} (X, \beta_ {0}) ] / e, \tag {13.4}
$$

where $o(X,\alpha) = e(X,\alpha) / \{1 - e(X,\alpha)\}$ .

Theorem 13.3 Under Assumption 13.1, if either $e(X, \alpha) = e(X)$ or $\mu_0(X, \beta_0) = \mu_0(X)$ , then $\mu_{0\mathrm{T}}^{dr} = E\{Y(0) \mid Z = 1\}$ .

Proof of Theorem 13.3: We have the decomposition

$$
\begin{array}{l} e \left[ \tilde {\mu} _ {0 T} ^ {\mathrm {d r}} - E \{Y (0) \mid Z = 1 \} \right] \\ = E \left[ o (X, \alpha) (1 - Z) \left\{Y (0) - \mu_ {0} (X, \beta_ {0}) \right\} + Z \mu_ {0} (X, \beta_ {0}) \right] - E \left\{Z Y (0) \right\} \\ = E \left[ o (X, \alpha) (1 - Z) \left\{Y (0) - \mu_ {0} (X, \beta_ {0}) \right\} - Z \left\{Y (0) - \mu_ {0} (X, \beta_ {0}) \right\} \right] \\ = E \left[ \left\{o (X, \alpha) (1 - Z) - Z \right\} \left\{Y (0) - \mu_ {0} (X, \beta_ {0}) \right\} \right] \\ = E \left[ \frac {e (X , \alpha) - Z}{1 - e (X , \alpha)} \{Y (0) - \mu_ {0} (X, \beta_ {0}) \} \right] \\ = E \left[ E \left\{\frac {e (X , \alpha) - Z}{1 - e (X , \alpha)} \mid X \right\} \times E \{Y (0) - \mu_ {0} (X, \beta_ {0}) \mid X \} \right] \\ = E \left[ \frac {e (X , \alpha) - e (X)}{1 - e (X , \alpha)} \times \{\mu_ {0} (X) - \mu_ {0} (X, \beta_ {0}) \} \right]. \\ \end{array}
$$

Therefore, $\tilde{\mu}_{0\mathrm{T}}^{\mathrm{dr}} - E\{Y(0)\mid Z = 1\} = 0$ if either $e(X,\alpha) = e(X)$ or $\mu_0(X,\beta_0) = \mu_0(X)$ .

Based on the population versions of $\tilde{\mu}_{0\mathrm{T}}^{\mathrm{dr}}$ in (13.4), we can obtain its sample version to construct a doubly robust estimator for $\tau_{\mathrm{T}}$ .

Definition 13.1 (doubly robust estimator for $\tau_{\mathbf{T}}$ ) Based on the data $(X_{i},Z_{i},Y_{i})_{i = 1}^{n}$ , we can obtain a doubly robust estimator for $\tau_{\mathrm{T}}$ by the following steps:

1. obtain the fitted values of the propensity scores $e(X_i, \hat{\alpha})$ and then obtain the fitted values of the odds $o(X_i, \hat{\alpha}) = e(X_i, \hat{\alpha}) / (1 - e(X_i, \hat{\alpha}))$ ;

2. obtain the fitted values of the outcome mean under control $\mu_0(X_i, \hat{\beta}_0)$ ;

3.construct the doubly robust estimator: $\hat{\tau}_{\mathrm{T}}^{\mathrm{dr}} = \hat{Y} (1) - \hat{\mu}_{0\mathrm{T}}^{\mathrm{dr}}$ , where

$$
\hat {\mu} _ {0 \mathrm {T}} ^ {\mathrm {d r}} = \frac {1}{n _ {1}} \sum_ {i = 1} ^ {n} \left[ o (X _ {i}, \hat {\alpha}) (1 - Z _ {i}) \{Y _ {i} - \mu_ {0} (X _ {i}, \hat {\beta} _ {0}) \} + Z _ {i} \mu_ {0} (X _ {i}, \hat {\beta} _ {0}) \right].
$$

By Definition 13.1, we can rewrite $\hat{\tau}_{\mathrm{T}}^{\mathrm{dr}}$ as

$$
e (X _ {i}, \hat {\alpha}) = \hat {\tau} _ {\mathrm {T}} ^ {\mathrm {r e g}} - \frac {1}{n _ {1}} \sum_ {i = 1} ^ {n} o (X _ {i}, \hat {\alpha}) (1 - Z _ {i}) \{Y _ {i} - \mu_ {0} (X _ {i}, \hat {\beta} _ {0}) \}
$$

or

$$
e (X _ {i}, \hat {\alpha}) = \hat {\tau} _ {\mathrm {T}} ^ {\mathrm {h t}} - \frac {1}{n _ {1}} \sum_ {i = 1} ^ {n} \{o (X _ {i}, \hat {\alpha}) (1 - Z _ {i}) + Z _ {i} \} \mu_ {0} (X _ {i}, \hat {\beta} _ {0}).
$$

Similar to the discussion of $\hat{\tau}^{\mathrm{dr}}$ , we can estimate the variance of $\hat{\tau}_{\mathrm{T}}^{\mathrm{dr}}$ via the bootstrap by resampling from $(Z_{i},X_{i},Y_{i})_{i = 1}^{n}$ . Hahn (1998), Mercatanti and Li (2014), Shinozaki and Matsuyama (2015) and Yang and Ding (2018b) are references on the estimation of $\tau_{\mathrm{T}}$ .

# 13.3 An example

The following $\mathbb{R}$ function implements two outcome regression estimators, two IPW estimators, and the doubly robust estimator for $\tau_{\mathrm{T}}$ . To avoid extreme estimated propensity scores, we can also truncate them from the above.

```r
ATT.est = function(z, y, x, out.family = gaussian, Utruncps = 1) {
    ## sample size
    nn = length(z)
    nn1 = sum(z)
    ## fitted propensity score
    pscore = glm(z ~ x, family = binomial)$fitted.values
    pscore = Tmin(Utruncps, pscore)
    odds = pscore/(1 - pscore)
    ## fitted potential outcomes
    outcome0 = glm(y ~ x, weights = (1 - z),
                     family = out.family)$fitted.values
    ## outcome regression estimator
    ace.reg0 = lm(y ~ z + x)$coef[2]
    ace.reg = mean(y[z==1]) - mean(outcome0[z==1])
    ## propensity score weighting estimator
    ace.ipw0 = mean(y[z==1]) -
        mean(odds*(1 - z)*y)*nn/nn1
    ace.ipw = mean(y[z==1])
        mean(odds*(1 - z)*y)/mean(odds*(1 - z))
    # doubly robust estimator
    res0 = y - outcome0
    ace.dr = ace.reg - mean(odds*(1 - z)*res0)*nn/nn1
    return(c(ace.reg0, ace.reg, ace.ipw0, ace.ipw, ace.dr))
} 
```

The following $\mathbb{R}$ function further implements the bootstrap variance estimators.

```javascript
OS Att = function(z, y, x, n.boot = 10^2, out.family = gaussian, Utruncps = 1) { point.est = ATT.est(z, y, x, out.family, Utruncps) 
```

```r
## nonparametric bootstrap
n = length(z)
x = as.matrix(x)
boot.est = replicate(n.boot, {
    id.boot = sample(1:n, n, replace = TRUE) 
```

# 13.4 Other estimands

ATT.est(z[id.boot], y[id.boot], x[id.boot, ], out.family, Utruncps)   
})   
boot.se $=$ apply.boot.est,1,sd)   
res $=$ rbind(point.est,boot.se)   
rownames(res） $=$ c("est","se")   
colnames(res） $=$ c("reg0","reg","HT","Hajek","DR")   
return(res)   
}

Now we re-analyze the data in Example 10.3 to estimate $\tau_{\mathrm{T}}$ . We obtain

```txt
reg0 reg HT Hajek DR est 0.061 -0.351 -1.992 -0.351 -0.187 se 0.227 0.258 0.705 0.328 0.287 
```

without truncating the estimated propensity scores, and

```txt
reg0 reg HT Hajek DR est 0.061 -0.351 -0.597 -0.192 -0.230 se 0.223 0.255 0.579 0.302 0.276 
```

by truncating the estimated propensity scores from the above at 0.9. The HT estimator is sensitive to the truncation as expected. The regression estimator in Example 13.1 is quite different from other estimators. It imposes an unnecessary assumption that the regression functions in the treatment and control group share the same coefficient of $X$ . The regression estimator in Example 13.2 is much closer to the Hajek and doubly robust estimators. The estimates above are slightly different from those in Section 12.3.3, suggesting the existence of treatment effect heterogeneity across $\tau_{\mathrm{T}}$ and $\tau$ .

# 13.4 Other estimands

Li et al. (2018a) gave a unified discussion of the causal estimands in observational studies. Starting from the conditional average causal effect $\tau(X)$ , they proposed a general class of estimands

$$
\tau^ {h} = \frac {E \{h (X) \tau (X) \}}{E \{h (X) \}}
$$

indexed by a weighting function $h(X)$ with $E\{h(X)\} \neq 0$ . The normalization in the denominator is to ensure that a constant causal effect $\tau(X) = \tau$ averages to the same $\tau$ .

Underignorability,

$$
\tau^ {h} = \frac {E [ h (X) \{\mu_ {1} (X) - \mu_ {0} (X) \} ]}{E \{h (X) \}}
$$

which motivates the outcome regression estimator

$$
\hat {\tau} ^ {h} = \frac {\sum_ {i = 1} ^ {n} h (X _ {i}) \{\hat {\mu} _ {1} (X _ {i}) - \hat {\mu} _ {0} (X _ {i}) \}}{\sum_ {i = 1} ^ {n} h (X _ {i})}.
$$

Moreover, we can show that $\tau^h$ has the following weighting form:

Theorem 13.4 Under the ignorability and overlap assumption, we have

$$
\tau^ {h} = E \left\{\frac {Z Y h (X)}{e (X)} - \frac {(1 - Z) Y h (X)}{1 - e (X)} \right\} / E \{h (X) \}.
$$

The proof of Theorem 13.4 is similar to those of Theorems 11.2 and 13.2 which is relegated to Problem 13.9. Based on Theorem 13.4, we can construct the corresponding IPW estimator for $\tau^h$ .

By Theorem 13.4, each unit is associated with the weight due to the definition of the estimand as well as the weight due to the inverse of the propensity score. Finally, the treated units are weighted by $h(X) / e(X)$ and the control units are weighted by $h(X) / \{1 - e(X)\}$ . Li et al. (2018a, Table 1) summarized several estimands, and I present a part of it below:

<table><tr><td>population</td><td>h(X)</td><td>estimand</td><td>weights</td></tr><tr><td>combined</td><td>1</td><td>τ</td><td>1/e(X) and 1/{1-e(X)}</td></tr><tr><td>treated</td><td>e(X)</td><td>τT</td><td>1 and e(X)/{1-e(X)}</td></tr><tr><td>control</td><td>1-e(X)</td><td>τC</td><td>{1-e(X)}/e(X) and 1</td></tr><tr><td>overlap</td><td>e(X){1-e(X)}</td><td>τO</td><td>1-e(X) and e(X)</td></tr></table>

The overlap population and the corresponding estimand

$$
\tau_ {\mathrm {O}} = \frac {E [ e (X) \{1 - e (X) \} \tau (X) ]}{E [ e (X) \{1 - e (X) \} ]}
$$

is new to us. This estimand has the largest weight for units with $e(X) = 1/2$ and down weights the units with extreme propensity scores. A nice feature of this estimand is that its IPW estimator is stable without the possibly extremely small values of $e(X)$ and $1 - e(X)$ in the denominator. If $e(X) \perp \tau(X)$ including the special case of $\tau(X) = \tau$ , the parameter $\tau_{\mathrm{O}}$ reduces to $\tau$ . In general, however, the estimand $\tau_{\mathrm{O}}$ may cause controversy because it changes the initial population and depends on the propensity score which may be misspecified in practice. Li et al. (2018a) and Li et al. (2019) gave some justifications and numerical evidence. This estimand will appear again in Chapter 14.

We can also construct the doubly robust estimator for $\tau^h$ . I relegate the details to Problem 13.10.

# 13.5 Homework Problems

# 13.1 Comparing $\tau_{\mathrm{T}},\tau_{\mathrm{C}}$ ,and $\mathcal{T}$

Assume $Z \perp \{Y(1), Y(0)\} \mid X$ . Recall $e(X) = \operatorname{pr}(Z = 1 \mid X)$ is the propensity score, $e = \operatorname{pr}(Z = 1)$ is the marginal probability of the treatment, and $\tau(X) = E\{Y(1) - Y(0) \mid X\}$ is the CATE. Show that

$$
\tau_ {\mathrm {T}} - \tau = \frac {\operatorname {c o v} \{e (X) , \tau (X) \}}{e}, \quad \tau_ {\mathrm {C}} - \tau = - \frac {\operatorname {c o v} \{e (X) , \tau (X) \}}{1 - e}.
$$

Remark: The results above also imply that $\tau_{\mathrm{T}} - \tau_{\mathrm{C}} = \operatorname{cov}\{e(X), \tau(X)\} / \{e(1 - e)\}$ . So the differences among $\tau_{\mathrm{T}}, \tau_{\mathrm{C}}, \tau$ depend on the covariance between the propensity score and CATE. When $e(X)$ and $\tau(X)$ are uncorrelated, their differences are 0.

# 13.2 An algebraic fact about a regression estimator for $\tau_{\mathrm{T}}$

This problem provides more details for Example 13.2.

Show that if we center the covariates by $X_{i} - \hat{X}(1)$ for all units, then $\hat{\tau}_{\mathrm{T}}$ equals the coefficient of $Z$ in the OLS fit of the outcome on the intercept, the treatment, covariates, and their interactions.

# 13.3 Simulation for the average causal effect on the treated units

Chapter 12 ran some simulation studies for $\tau$ . Run similar simulation studies for $\tau_{\mathrm{T}}$ with either correct or incorrect propensity score or outcome models.

You can choose different model parameters, a larger number of simulation settings, and a larger number of bootstrap replicates. Report your findings, including at least the bias, variance, and variance estimator via the bootstrap. You can also report other properties of the estimators, for example, the asymptotic Normality and the coverage rates of the confidence intervals.

# 13.4 An alternative form of the doubly robust estimator for $\tau_{\mathrm{T}}$

Motivated by (13.4), we have an alternative form of doubly robust estimator for $E\{Y(0) \mid Z = 1\}$ :

$$
\tilde {\mu} _ {0 \mathrm {T}} ^ {\mathrm {d r 2}} = \frac {E [ o (X , \alpha) (1 - Z) \{Y - \mu_ {0} (X , \beta_ {0}) \} ]}{E [ o (X , \alpha) (1 - Z) ]} + E \{Z \mu_ {0} (X, \beta_ {0}) \} / e.
$$

Show that under Assumption 13.1, $\tilde{\mu}_{0\mathrm{T}}^{\mathrm{dr2}} = E\{Y(0)\mid Z = 1\}$ if either $e(X,\alpha) = e(X)$ or $\mu_0(X,\beta_0) = \mu_0(X)$ . Give the sample analog of the doubly robust estimator for $\tau_{\mathrm{T}}$ .

19013 The Average Causal Effect on the Treated Units and Other Estimands

# 13.5 Average causal effect on the control units

Prove the identification formulas for $\tau_{\mathrm{C}}$ , analogous to (13.1) and (13.3). Propose the doubly robust estimator for $\tau_{\mathrm{C}}$ .

# 13.6 Estimating individual effect and conditional average causal effect

Assume that $\{Z_i, X_i, Y_i(1), Y_i(0)\}_{i=1}^n \stackrel{\text{IID}}{\sim} \{Z, X, Y(1), Y(0)\}$ . The individual effect is $\tau_i = Y_i(1) - Y_i(0)$ and the conditional average causal effect is $\tau(X_i) = E\{Y_i(1) - Y_i(0) \mid X_i\}$ . Since we will discuss the individual effect, we do not drop the subscript $i$ since $\tau$ means the average causal effect, not the population version of $Y(1) - Y(0)$ .

1. Under randomization with $Z_{i} \sqcup \{Y_{i}(1), Y_{i}(0)\}$ and $e = \operatorname{pr}(Z_{i} = 1)$ ,

show that

$$
\delta_ {i} = \frac {Z _ {i} Y _ {i}}{e} - \frac {\left(1 - Z _ {i}\right) Y _ {i}}{1 - e}
$$

is an unbiased predictor of the individual effect in the sense that

$$
E (\delta_ {i} - \tau_ {i}) = 0 (i = 1, \dots , n).
$$

Further show that $E(\delta_i) = \tau$ for all $i = 1, \dots, n$ .

2. Under $\text{ignorability}$ with $Z_{i} \sqcup \{Y_{i}(1), Y_{i}(0)\} \mid X_{i}$ and $e(X_{i}) = \operatorname{pr}(Z_{i} = 1 \mid X_{i})$ , show that

$$
\delta_ {i} = \frac {Z _ {i} Y _ {i}}{e (X _ {i})} - \frac {(1 - Z _ {i}) Y _ {i}}{1 - e (X _ {i})}
$$

is an unbiased predictor of the individual effect and the conditional average causal effect in the sense that

$$
E \left(\delta_ {i} - \tau_ {i}\right) = 0, \quad E \left\{\delta_ {i} - \tau \left(X _ {i}\right) \right\} = 0, \quad (i = 1, \dots , n).
$$

Further show that $E(\delta_i) = \tau$ for all $i = 1, \dots, n$ .

# 13.7 General estimand and $(\tau_{\mathrm{T}},\tau_{\mathrm{C}})$

Assume unconfoundedness. Show that $\tau^h = \tau_{\mathrm{T}}$ if $h(X) = e(X)$ , and $\tau^h = \tau_{\mathrm{C}}$ if $h(X) = 1 - e(X)$ .

# 13.8 More on $\tau_{\mathrm{O}}$

Show that

$$
\tau_ {\mathrm {O}} = \frac {E [ \{1 - e (X) \} \tau (X) \mid Z = 1 ]}{E \{1 - e (X) \mid Z = 1 \}} = \frac {E \{e (X) \tau (X) \mid Z = 0 \}}{E \{e (X) \mid Z = 0 \}}.
$$

# 13.9 $IPW$ for the general estimand

Prove Theorem 13.4.

# 13.10 Doubly robust estimation for general estimand

For a given $h(X)$ , we have the following formulas for constructing the doubly robust estimator for $\tau^h$ :

$$
\tilde {\mu} _ {1} ^ {h, \mathrm {d r}} = E \left[ \frac {Z h (X) \{Y - \mu_ {1} (X , \beta_ {1}) \}}{e (X , \alpha)} + h (X) \mu_ {1} (X, \beta_ {1}) \right],
$$

$$
\tilde {\mu} _ {0} ^ {h, \mathrm {d r}} = E \left[ \frac {(1 - Z) h (X) \{Y - \mu_ {0} (X , \beta_ {0}) \}}{1 - e (X , \alpha)} + h (X) \mu_ {0} (X, \beta_ {0}) \right].
$$

Show that under ignorability and overlap,

1. if either $e(X, \alpha) = e(X)$ or $\mu_1(X, \beta_1) = \mu_1(X)$ , then $\tilde{\mu}_1^{h,\mathrm{dr}} = E\{h(X)Y(1)\}$ ;   
2. if either $e(X, \alpha) = e(X)$ or $\mu_0(X, \beta_0) = \mu_0(X)$ , then $\tilde{\mu}_0^{h,\mathrm{dr}} = E\{h(X)Y(0)\}$ ;   
3. if either $e(X, \alpha) = e(X)$ or $\{\mu_1(X, \beta_1) = \mu_1(X), \mu_0(X, \beta_0) = \mu_0(X)\}$ , then

$$
\frac {\tilde {\mu} _ {1} ^ {h , \mathrm {d r}} - \tilde {\mu} _ {0} ^ {h , \mathrm {d r}}}{E \{h (X) \}} = \tau^ {h}.
$$

Remark: Tao and Fu (2019) proved the above results. However, they hold only for a given $h(X)$ . The most interesting cases of $\tau_{\mathrm{T}}, \tau_{\mathrm{C}}$ and $\tau_{\mathrm{O}}$ all have weight depending on the propensity score $e(X)$ , which must be estimated in the first place. The above formulas do not apply to constructing the doubly robust estimators for $\tau_{\mathrm{T}}$ and $\tau_{\mathrm{C}}$ ; there does not exist a doubly robust estimator for $\tau_{\mathrm{O}}$ .

# 13.11 Analyzing a dataset from the Karolinska Institute

Revisit Problem 12.5. Estimate $\tau_{\mathrm{T}}$ based on the methods introduced in this Chapter.

# 13.12 Recommended reading

Shinozaki and Matsuyama (2015) focused on $\tau_{\mathrm{T}}$ , and Li et al. (2018a) discussed general $\tau^{h}$ .

# 14

# Using the Propensity Score in Regressions for Causal Effects

Since Rosenbaum and Rubin (1983b)'s seminal paper, many creative uses of the propensity score have appeared in the literature (e.g., Bang and Robins, 2005; Robins et al., 2007; Van der Laan and Rose, 2011; Vansteelandt and Daniel, 2014). This chapter discusses two simple methods to use the propensity score:

1. including the propensity score as a covariate in regressions;   
2. running regressions weighted by the inverse of the propensity score.

I choose to focus on these two methods because of the following reasons:

1. they are easy to implement, and involve only standard statistical software packages for regressions;   
2. their properties are comparable to many more complex methods;   
3. they can be easily extended to allow for flexible statistical models including machine learning algorithms.

# 14.1 Regressions with the propensity score as a covariate

By Theorem 11.1, if $\mathrm{ignorability}$ holds conditioning on $X$ , then it also holds conditioning on $e(X)$ :

$$
Z \bot \{Y (1), Y (0) \} \mid e (X).
$$

Analogous to (10.6), $\tau$ is also nonparametrically identified by

$$
\tau = E \Big [ E \{Y \mid Z = 1, e (X) \} - E \{Y \mid Z = 0, e (X) \} \Big ],
$$

which motivates methods based on regressions of $Y$ on $Z$ and $e(X)$ .

The simplest regression specification is the OLS fit of $Y$ on $\{1, Z, e(X)\}$ , with the coefficient of $Z$ as an estimator, denoted by $\tau_e$ . For simplicity, I will discuss the population OLS:

$$
\arg \min _ {a, b, c} E \{Y - a - b Z - c e (X) \} ^ {2}
$$

with $\tau_{e}$ defined as the coefficient of $Z$ . It is consistent for $\tau$ if we have a correct propensity score model and the outcome model is indeed linear in $Z$ and $e(X)$ . The more interesting result is that $\tau_{e}$ estimates $\tau_{0}$ introduced in Chapter 13.4 if we have a correct propensity score model even if the outcome model is completely misspecified.

Theorem 14.1 If $Z \perp \perp \{Y(1), Y(0)\} \mid X$ , then the coefficient of $Z$ in the population OLS fit of $Y$ on $\{1, Z, e(X)\}$ equals

$$
\tau_ {e} = \tau_ {\mathrm {O}} = \frac {E \{h _ {\mathrm {O}} (X) \tau (X) \}}{E \{h _ {\mathrm {O}} (X) \}},
$$

recalling that $h_{\mathrm{O}}(X) = e(X)\{1 - e(X)\}$ and $\tau (X) = E\{Y(1) - Y(0)\mid X\}$ .

An unusual feature of Theorem 14.1 is that the overlap condition is not needed anymore. Even if some units have propensity score $e(X)$ equaling 0 or 1, their associated weight $e(X)\{1 - e(X)\}$ is zero so they do not contribute anything to the final parameter $\tau_0$ .

Proof of Theorem 14.1: I will use the FWL theorem reviewed in Section B.3 to prove Theorem 14.1. By the FWL theorem, we can obtain $\tau_{e}$ in two steps:

1. we obtain the residual $\tilde{Z}$ from the OLS fit of $Z$ on $\{1, e(X)\}$ ;   
2. we obtain $\tau_{e}$ from the OLS fit of $Y$ on $\tilde{Z}$ .

We can use the result on covariance in Chapter A.1.5 to simplify the coefficient of $e(X)$ in the OLS fit of $Z$ on $\{1, e(X)\}$ is

$$
\begin{array}{l} \frac {\operatorname {c o v} \{Z , e (X) \}}{\operatorname {v a r} \{e (X) \}} = \frac {E [ \operatorname {c o v} \{Z , e (X) \mid X \} ] + \operatorname {c o v} \{E (Z \mid X) , e (X) \}}{\operatorname {v a r} \{e (X) \}} \\ = \frac {0 + \operatorname {v a r} \{e (X) \}}{\operatorname {v a r} \{e (X) \}} = 1, \\ \end{array}
$$

so the intercept is $E(Z) - E\{e(X)\} = 0$ and the residual is $\tilde{Z} = Z - e(X)$ . This makes sense since $Z - e(X)$ is uncorrelated with any function of $X$ .

Therefore, we can obtain $\tau_{e}$ from the univariate OLS fit of $Y$ on a centered variable $Z - e(X)$ :

$$
\tau_ {e} = \frac {\operatorname {c o v} \{Z - e (X) , Y \}}{\operatorname {v a r} \{Z - e (X) \}}.
$$

The denominator simplifies to

$$
\begin{array}{l} \operatorname {v a r} \{Z - e (X) \} = E \{Z - e (X) \} ^ {2} \\ = E \{Z + e (X) ^ {2} - 2 Z e (X) \} \\ = E \left\{e (X) + e (X) ^ {2} - 2 e (X) ^ {2} \right\} \\ = E \{h _ {\mathrm {O}} (X) \}. \\ \end{array}
$$

The numerator simplifies to

$$
\begin{array}{l} \operatorname {c o v} \{Z - e (X), Y \} \\ = E \left[ \left\{Z - e (X) \right\} Y \right] \\ = E [ \{Z - e (X) \} Z Y (1) ] + E [ \{Z - e (X) \} (1 - Z) Y (0) ] \\ (\text {b y} Y = Z Y (1) + (1 - Z) Y (0)) \\ = E [ \{Z - Z e (X) \} Y (1) ] - E [ e (X) (1 - Z) Y (0) ] \\ = E [ Z \{1 - e (X) \} Y (1) ] - E [ e (X) (1 - Z) Y (0) ] \\ = E [ e (X) \{1 - e (X) \} \mu_ {1} (X) ] - E [ e (X) \{1 - e (X) \} \mu_ {0} (X) ] \\ (t o w e r p r o p e r t y \quad i n d a g h i n a b i l i t y) \\ = E \{h _ {\mathrm {O}} (X) \tau (X) \}. \\ \end{array}
$$

The conclusion follows.

From the proof of Theorem 14.1, we can simply run the OLS of $Y$ on the centered treatment $Z - e(X)$ . Lee (2018) proposed this procedure. Moreover, we can also include $X$ in the OLS fit which may improve efficiency in finite samples. However, this does not change the estimand, which is still $\tau_{\mathrm{O}}$ . I summarize these two results in the corollary below.

Corollary 14.1 If $Z \perp \perp \{Y(1), Y(0)\} \mid X$ , then

(1) the coefficient of $Z - e(X)$ in the population OLS fit of $Y$ on $Z - e(X)$ or $\{1, Z - e(X)\}$ equals $\tau_{\mathrm{O}}$ ;   
(2) the coefficient of $Z$ in the population OLS fit of $Y$ on $\{1, Z, e(X), X\}$ equals $\tau_{\mathrm{O}}$ .

Proof of Corollary 14.1: (1) The first result is an intermediate step in the proof of Theorem 14.1. The second result holds because regressing $Y$ on $Z - e(X)$ or $\{1, Z - e(X)\}$ does not change the coefficient of $Z - e(X)$ since it has mean zero.

(2) We can use the FWL theorem again. We can first obtain the residual from the population OLS of $Z$ on $\{1, e(X), X\}$ , which is $Z - e(X)$ because

$$
Z - e (X) = Z - 0 - 1 \cdot e (X) - 0 ^ {\mathsf {T}} X
$$

and $Z - e(X)$ is uncorrelated with any functions of $X$ . Then the coefficient of $Z$ in the population OLS fit of $Y$ on $\{1, Z, e(X), X\}$ equals the coefficient of $Z$ in the population OLS fit of $Y$ on $Z - e(X)$ .

Theorem 14.1 motivates a two-step estimator for $\tau_{\mathrm{O}}$ :

1. fit a propensity score model to obtain $\hat{e}(X_i)$ ;   
2. run OLS of $Y_{i}$ on $(1, X_{i}, \hat{e}(X_{i}))$ to obtain the coefficient of $Z_{i}$ .

Corollary 14.1(1) motivates a two-step estimator for $\tau_{\mathrm{O}}$ :

1. fit a propensity score model to obtain $\hat{e}(X_i)$ ;

2. run OLS of $Y_{i}$ on $Z_{i} - \hat{e}(X_{i})$ to obtain the coefficient of $Z_{i}$ .

Corollary 14.1(1) motivates another two-step estimator for $\tau_{\mathrm{O}}$ :

1. fit a propensity score model to obtain $\hat{e}(X_i)$ ;   
2. run OLS of $Y_{i}$ on $(1,Z_{i},\hat{e}(X_{i}),X_{i})$ to obtain the coefficient of $Z_{i}$ .

Although OLS is convenient for obtaining point estimators, the corresponding standard errors are incorrect due to the uncertainty in the first step estimation of the propensity score. We can use the bootstrap to approximate the standard errors.

Robins et al. (1992) discussed many OLS estimators based on the propensity score. The above results seem special cases of their general theory although they did not point out the connection with the estimand under the overlap weight, which was resurrected by Li et al. (2018a). Lee (2018) proposed to regress $Y$ on $Z - e(X)$ from a different perspective without making connections to the existing results in Robins et al. (1992) and Li et al. (2018a).

Rosenbaum and Rubin (1983b) proposed to estimate the average causal effect based on the OLS fit of $Y$ on $\{1, Z, e(X), Ze(X)\}$ . When this outcome model is correct, their estimator is consistent for the average causal effect. However, when the model is incorrect, the corresponding estimator has a much more complicated interpretation. Little and An (2004) suggested constructing estimators based on the OLS of $Y$ on $Z$ and a flexible function<sup>1</sup> of $e(X)$ and showed it enjoys certain double robustness property. Due to the complexity of implementation, I omit the discussion.

# 14.2 Regressions weighted by the inverse of the propensity score

# 14.2.1 Average causal effect

We first re-examine the Hajek estimator of $\tau$ :

$$
\hat {\tau} ^ {\mathrm {h a j e k}} = \frac {\sum_ {i = 1} ^ {n} \frac {Z _ {i} Y _ {i}}{\hat {e} (X _ {i})}}{\sum_ {i = 1} ^ {n} \frac {Z _ {i}}{\hat {e} (X _ {i})}} - \frac {\sum_ {i = 1} ^ {n} \frac {(1 - Z _ {i}) Y _ {i}}{1 - \hat {e} (X _ {i})}}{\sum_ {i = 1} ^ {n} \frac {1 - Z _ {i}}{1 - \hat {e} (X _ {i})}},
$$

which equals the difference between the weighted means of the outcomes in the treatment and control groups. Numerically, it is identical to the coefficient of $Z_{i}$ in the following weighted least squares (WLS) of $Y_{i}$ on $(1,Z_{i})$ .

Proposition 14.1 $\hat{\tau}^{\mathrm{hajek}}$ equals $\hat{\beta}$ from the following WLS:

$$
(\hat {\alpha}, \hat {\beta}) = \arg \min _ {\alpha , \beta} \sum_ {i = 1} ^ {n} w _ {i} (Y _ {i} - \alpha - \beta Z _ {i}) ^ {2}
$$

with weights

$$
w _ {i} = \frac {Z _ {i}}{\hat {e} (X _ {i})} + \frac {1 - Z _ {i}}{1 - \hat {e} (X _ {i})} = \left\{ \begin{array}{l l} \frac {1}{\hat {e} (X _ {i})} & i f Z _ {i} = 1; \\ \frac {1}{1 - \hat {e} (X _ {i})} & i f Z _ {i} = 0. \end{array} \right. \tag {14.1}
$$

Imbens (2004) pointed out the result in Proposition 14.1. I leave it as a Problem 14.1. By Proposition 14.1, it is convenient to obtain $\hat{\tau}^{\mathrm{hajek}}$ based on WLS. However, due to the uncertainty in the estimated propensity score, the standard error reported by WLS is incorrect for the true standard error of $\hat{\tau}^{\mathrm{hajek}}$ . The bootstrap provides a convenient approximation to the true standard error.

Why does the WLS give a consistent estimator for $\tau$ ? Recall that in the CRE with a constant propensity score, we can simply use the coefficient of $Z_{i}$ in the OLS fit of $Y_{i}$ on $(1,Z_{i})$ to estimate $\tau$ . In observational studies, units have different probabilities of receiving the treatment and control, respectively. If we weight the treated units by $1 / e(X_{i})$ and the control units by $1 / \{1 - e(X_{i})\}$ , then both treated and control groups can represent the whole population. Thus, by weighting, we effectively have a pseudo-randomized experiment. Consequently, the difference between the weighted means is consistent for $\tau$ . The numerical equivalence of $\hat{\tau}^{\mathrm{hajek}}$ and WLS is not only a fun numerical fact itself but also useful for motivating more complex estimators with covariate adjustment. I give one extension below.

Recall that in the CRE, we can use the coefficient of $Z_{i}$ in the OLS fit of $Y_{i}$ on $(1,Z_{i},X_{i},Z_{i}X_{i})$ to estimate $\tau$ , where the covariates are centered with $\bar{X} = 0$ . This is Lin (2013)'s estimator which uses covariates to improve efficiency. A natural extension to observational studies is to estimate $\tau$ using the coefficient of $Z_{i}$ in the WLS fit of $Y_{i}$ on $(1,Z_{i},X_{i},Z_{i}X_{i})$ with weights defined in (14.1). Hirano and Imbens (2001) used this estimator in an application. The fully interacted linear model is equivalent to two separate linear models for the treated and control groups. If the linear models

$$
E (Y \mid Z = 1, X) = \beta_ {1 0} + \beta_ {1 x} ^ {\intercal} X, E (Y \mid Z = 0, X) = \beta_ {0 0} + \beta_ {0 x} ^ {\intercal} X,
$$

are correctly specified, then both OLS and WLS give consistent estimators for the coefficients and the estimators of the coefficient of $Z$ are consistent for $\tau$ . More interestingly, the estimator of the coefficient of $Z$ based on WLS is also consistent for $\tau$ if the propensity score model is correct and the outcome model is incorrect. That is, the estimator based on WLS is doubly robust. Robins et al. (2007) discussed this property and attributed this result to M. Joffe's unpublished paper. I will give more details below.

Let $e(X_i, \hat{\alpha})$ be the fitted propensity score and $(\mu_1(X_i, \hat{\beta}_1), \mu_0(X_i, \hat{\beta}_0))$ be

the fitted values of the outcome means based on the WLS. The outcome regression estimator is

$$
\hat {\tau} _ {\mathrm {w l s}} ^ {\mathrm {r e g}} = \frac {1}{n} \sum_ {i = 1} ^ {n} \mu_ {1} (X _ {i}, \hat {\beta} _ {1}) - \frac {1}{n} \sum_ {i = 1} ^ {n} \mu_ {0} (X _ {i}, \hat {\beta} _ {0})
$$

and the doubly robust estimator for $\tau$ is

$$
\hat {\tau} _ {\mathrm {w l s}} ^ {\mathrm {d r}} = \hat {\tau} _ {\mathrm {w l s}} ^ {\mathrm {r e g}} + \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {Z _ {i} \{Y _ {i} - \mu_ {1} (X _ {i} , \hat {\beta} _ {1}) \}}{e (X _ {i} , \hat {\alpha})} - \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {(1 - Z _ {i}) \{Y _ {i} - \mu_ {0} (X _ {i} , \hat {\beta} _ {0}) \}}{1 - e (X _ {i} , \hat {\alpha})}.
$$

An interesting result is that this doubly robust estimator equals the outcome regression estimator, which reduces to the coefficient of $Z_{i}$ in the WLS fit of $Y_{i}$ on $(1,Z_{i},X_{i},Z_{i}X_{i})$ if we use weights (14.1).

Theorem 14.2 If $\bar{X} = 0$ and $(\mu_1(X_i, \hat{\beta}_1), \mu_0(X_i, \hat{\beta}_0)) = (\hat{\beta}_{10} + \hat{\beta}_{1x}^{\top} X_i, \hat{\beta}_{00} + \hat{\beta}_{0x}^{\top} X_i)$ based on the WLS fit of $Y_i$ on $(1, Z_i, X_i, Z_i X_i)$ with weights (14.1), then

$$
\hat {\tau} _ {\mathrm {w l s}} ^ {\mathrm {d r}} = \hat {\tau} _ {\mathrm {w l s}} ^ {\mathrm {r e g}} = \hat {\beta} _ {1 0} - \hat {\beta} _ {0 0},
$$

which is the coefficient of $Z_{i}$ in the WLS fit.

Proof of Theorem 14.2: The WLS fit of $Y_{i}$ on $(1,Z_{i},X_{i},Z_{i}X_{i})$ is equivalent to two WLS fits based on the treated and control data. Both WLS fits include intercepts, so the weighted residuals have mean 0 (see (B.5)):

$$
\sum_ {i = 1} ^ {n} \frac {Z _ {i} (Y _ {i} - \hat {\beta} _ {1 0} - \hat {\beta} _ {1 x} ^ {\mathsf {T}} X _ {i})}{\hat {e} (X _ {i})} = 0
$$

and

$$
\sum_ {i = 1} ^ {n} \frac {(1 - Z _ {i}) (Y _ {i} - \hat {\beta} _ {0 0} - \hat {\beta} _ {0 x} ^ {\mathsf {T}} X _ {i})}{1 - \hat {e} (X _ {i})} = 0.
$$

So the difference between $\hat{\tau}^{\mathrm{dr}}$ and $\hat{\tau}^{\mathrm{reg}}$ is exactly zero. Both reduces to

$$
\begin{array}{l} \frac {1}{n} \sum_ {i = 1} ^ {n} (\hat {\beta} _ {1 0} + \hat {\beta} _ {1 x} ^ {\intercal} X _ {i}) - \frac {1}{n} \sum_ {i = 1} ^ {n} (\hat {\beta} _ {0 0} + \hat {\beta} _ {0 x} ^ {\intercal} X _ {i}) = \hat {\beta} _ {1 0} - \hat {\beta} _ {0 0} + (\hat {\beta} _ {1 x} - \hat {\beta} _ {0 x}) ^ {\intercal} \bar {X} \\ = \hat {\beta} _ {1 0} - \hat {\beta} _ {0 0} \\ \end{array}
$$

with centered covariates. So they both equal the coefficient of $Z_{i}$ in the WLS fit of $Y_{i}$ on $(1, Z_{i}, X_{i}, Z_{i}X_{i})$ .

Freedman and Berk (2008) discouraged the use of the WLS estimator above based on some simulation studies. They showed that when the outcome model is correct, the WLS estimator is worse than the OLS estimator since the WLS estimator has large variability in their simulation setting with homoskedastic outcomes. This may not be true in general. When the errors have variance

TABLE 14.1: Regression estimators in CREs and unconfounded observational studies. The weights $w_{i}$ 's are defined in (14.1). Assume covariates are centered at $\bar{X} = 0$ .   

<table><tr><td></td><td>CRE</td><td>unconfounded observational studies</td></tr><tr><td>without X</td><td>Yi ~ (1,Zi)</td><td>Yi ~ (1,Zi) with weights wi</td></tr><tr><td>with X</td><td>Yi ~ (1,Zi,Xi,ZiXi)</td><td>Yi ~ (1,Zi,Xi,ZiXi) with weights wi</td></tr></table>

proportional to the inverse of the propensity scores, the WLS estimator will be more efficient than the OLS estimator.

Freedman and Berk (2008) also showed that the estimated standard error based on the WLS fit is not consistent for the true standard error because it ignores the uncertainty in the estimated propensity score. This can be easily fixed by using the bootstrap to approximate the variance of the WLS estimator.

Nevertheless, Freedman and Berk (2008) found that "weighting may help under some circumstances" because when the outcome model is incorrect, the WLS estimator is still consistent if the propensity score model is correct.

I end this section with Table 14.1 summarizing the regression estimators for causal effects in both randomized experiments and observational studies.

# 14.2.2 Average causal effect on the treated units

The results for $\tau_{\mathrm{T}}$ parallel those for $\tau$ . First, the Hajek estimator for $\tau_{\mathrm{T}}$

$$
\hat {\tau} _ {\mathrm {T}} ^ {\mathrm {h a j e k}} = \hat {\bar {Y}} (1) - \frac {\sum_ {i = 1} ^ {n} \hat {\sigma} (X _ {i}) (1 - Z _ {i}) Y _ {i}}{\sum_ {i = 1} ^ {n} \hat {\sigma} (X _ {i}) (1 - Z _ {i})},
$$

with $\hat{o}(X_i) = \hat{e}(X_i) / \{1 - \hat{e}(X_i)\}$ , equals the coefficient of $Z_i$ in the following WLS fit $Y_i$ on $(1, Z_i)$ .

Proposition 14.2 $\hat{\tau}_{\mathrm{T}}^{hajek}$ is numerically identical to $\hat{\beta}$ in the following WLS:

$$
(\hat {\alpha}, \hat {\beta}) = \arg \min  _ {\alpha , \beta} \sum_ {i = 1} ^ {n} w _ {\mathrm {T i}} \left(Y _ {i} - \alpha - \beta Z _ {i}\right) ^ {2}
$$

with weights

$$
w _ {\mathrm {T} i} = Z _ {i} + \left(1 - Z _ {i}\right) \hat {o} \left(X _ {i}\right) = \left\{ \begin{array}{l l} 1 & \text {i f} Z _ {i} = 1; \\ \hat {o} \left(X _ {i}\right) & \text {i f} Z _ {i} = 0. \end{array} \right. \tag {14.2}
$$

Similar to Proposition 14.1, Proposition 14.2 is a pure linear algebra result. I relegate its proof to Problem 14.1.

Second, if we center covariates at $\bar{X}(1) = 0$ , then we can estimate $\tau_{\mathrm{T}}$ using

the coefficient of $Z_{i}$ in the WLS fit of $Y_{i}$ on $(1,Z_{i},X_{i},Z_{i}X_{i})$ with weights defined in (14.2). Similarly, this estimator equals the regression estimator

$$
\hat {\tau} _ {\mathrm {T , w l s}} ^ {\mathrm {r e g}} = \hat {\bar {Y}} (1) - \frac {1}{n _ {1}} \sum_ {i = 1} ^ {n} Z _ {i} \mu_ {0} (X _ {i}, \hat {\beta} _ {0}),
$$

which also equals the doubly robust estimator

$$
\hat {\tau} _ {\mathrm {T , w l s}} ^ {\mathrm {d r}} = \hat {\tau} _ {\mathrm {T , w l s}} ^ {\mathrm {r e g}} - \frac {1}{n _ {1}} \sum_ {i = 1} ^ {n} \hat {o} (X _ {i}) (1 - Z _ {i}) \{Y _ {i} - \mu_ {0} (X _ {i}, \hat {\beta} _ {0}) \}.
$$

Theorem 14.3 If $\hat{\bar{X}}(1) = 0$ and $\mu_0(X_i, \hat{\beta}_0) = \hat{\beta}_{00} + \hat{\beta}_{0x}^{\mathrm{T}} X_i$ based on the WLS fit of $Y_i$ on $(1, Z_i, X_i, Z_i X_i)$ with weights (14.2), then

$$
\hat {\tau} _ {\mathrm {T , w l s}} ^ {\mathrm {d r}} = \hat {\tau} _ {\mathrm {T , w l s}} ^ {\mathrm {r e g}} = \hat {\beta} _ {1 0} - \hat {\beta} _ {0 0},
$$

which is the coefficient of $Z_{i}$ in the WLS fit.

Proof of Theorem 14.3: Based on the WLS fits in the treatment and control groups, we have

$$
\sum_ {i = 1} ^ {n} Z _ {i} \left(Y _ {i} - \hat {\beta} _ {1 0} - \hat {\beta} _ {1 x} ^ {\mathrm {T}} X _ {i}\right) = 0, \tag {14.3}
$$

$$
\sum_ {i = 1} ^ {n} \hat {o} \left(X _ {i}\right) \left(1 - Z _ {i}\right) \left(Y _ {i} - \hat {\beta} _ {0 0} - \hat {\beta} _ {0 x} ^ {\mathrm {T}} X _ {i}\right) = 0. \tag {14.4}
$$

The second result (14.4) ensures that $\hat{\tau}_{\mathrm{T, wls}}^{\mathrm{dr}} = \hat{\tau}_{\mathrm{T, wls}}^{\mathrm{reg}}$ . Both reduces to

$$
\hat {\tilde {Y}} (1) - \frac {1}{n _ {1}} \sum_ {i = 1} ^ {n} Z _ {i} (\hat {\beta} _ {0 0} + \hat {\beta} _ {0 x} ^ {\mathsf {T}} X _ {i}) = \frac {1}{n _ {1}} \sum_ {i = 1} ^ {n} Z _ {i} (Y _ {i} - \hat {\beta} _ {0 0} - \hat {\beta} _ {0 x} ^ {\mathsf {T}} X _ {i}).
$$

With covariates centered at $\hat{\bar{X}}(1) = 0$ , the first result (14.3) implies that $\hat{\bar{Y}}(1) = \hat{\beta}_{10}$ which further simplifies the estimator to $\hat{\beta}_{10} - \hat{\beta}_{00}$ .

# 14.3 Homework problems

# 14.1 Hajek estimators as WLS estimators

Prove Propositions 14.1 and 14.2.

Remark: These are special cases of Problem B.3 on the univariate WLS.

# 14.2 Predictive estimator and doubly robust estimator

Another outcome regression estimator is the predictive estimator

$$
\hat {\tau} ^ {\mathrm {p r e d}} = \hat {\mu} _ {1} ^ {\mathrm {p r e d}} - \hat {\mu} _ {0} ^ {\mathrm {p r e d}}
$$

where

$$
\hat {\mu} _ {1} ^ {\text {p r e d}} = \frac {1}{n} \sum_ {i = 1} ^ {n} \left\{Z _ {i} Y _ {i} + (1 - Z _ {i}) \mu_ {1} \left(X _ {i}, \hat {\beta} _ {1}\right) \right\}
$$

and

$$
\hat {\mu} _ {0} ^ {\text {p r e d}} = \frac {1}{n} \sum_ {i = 1} ^ {n} \left\{Z _ {i} \mu_ {0} \left(X _ {i}, \hat {\beta} _ {1}\right) + \left(1 - Z _ {i}\right) Y _ {i} \right\}.
$$

It differs from the outcome regression estimator discussed before in that it only predicts the counterfactual outcomes but not the observed outcomes.

Show that the doubly robust estimator equals $\hat{\tau}^{\mathrm{pred}}$ if $(\mu_1(X_i,\hat{\beta}_1),\mu_0(X_i,\hat{\beta}_1)) = (\hat{\beta}_{10} + \hat{\beta}_{1x}^{\mathsf{T}}X_i,\hat{\beta}_{00} + \hat{\beta}_{0x}^{\mathsf{T}}X_i)$ are from the WLS fits of $Y_{i}$ on $(1,X_{i})$ based on the treated and control data, respectively, with weights

$$
w _ {i} = Z _ {i} / \hat {o} \left(X _ {i}\right) + \left(1 - Z _ {i}\right) \hat {o} \left(X _ {i}\right) = \left\{ \begin{array}{l l} \frac {1}{\hat {o} \left(X _ {i}\right)} = \frac {1 - \hat {e} \left(X _ {i}\right)}{\hat {e} \left(X _ {i}\right)} & \text {i f} Z _ {i} = 1; \\ \hat {o} \left(X _ {i}\right) = \frac {\hat {e} \left(X _ {i}\right)}{1 - \hat {e} \left(X _ {i}\right)} & \text {i f} Z _ {i} = 0. \end{array} \right. \tag {14.5}
$$

Remark: Cao et al. (2009) and Vermeulen and Vansteelandt (2015) motivated the weights in (14.5) from other more theoretical perspectives.

# 14.3 Weighted logistic regression with a binary outcome

With a binary outcome, we can replace linear outcome models with logistic outcome models. Show that with weights in the logistic regressions, the doubly robust estimators equal the outcome regression estimator. The result holds for both $\tau$ and $\tau_{\mathrm{T}}$ .

# 14.4 Causal inference with a misspecified linear regression

Define the population OLS of $Y$ on $(1,Z,X)$ as

$$
(\beta_ {0}, \beta_ {1}, \beta_ {2}) = \arg \min  _ {b _ {0}, b _ {1}, b _ {2}} E (Y - b _ {0} - b _ {1} Z - b _ {2} ^ {\top} X) ^ {2}.
$$

Recall that $e(X) = \operatorname{pr}(Z = 1 \mid X)$ is the propensity score, and define $\tilde{e}(X) = \gamma_0 + \gamma_1^\top X$ as the OLS projection of $Z$ on $X$ with

$$
\left(\gamma_ {0}, \gamma_ {1}\right) = \arg \min  _ {c _ {0}, c _ {1}} E \left(Z - c _ {0} - c _ {1} ^ {\top} X\right) ^ {2}.
$$

1. Show that

$$
\beta_ {1} = \frac {E [ \tilde {w} (X) \{\mu_ {1} (X) - \mu_ {0} (X) \} ]}{E \{\tilde {w} (X) \}} + \frac {E [ \{e (X) - \tilde {e} (X) \} \mu_ {0} (X) ]}{E \{\tilde {w} (X) \}}
$$

where $\tilde{w}(X) = e(X)\{1 - \tilde{e}(X)\}$ .

2. When $X$ contains the dummy variables for a discrete covariate, show that

$$
\beta_ {1} = \frac {E [ w (X) \{\mu_ {1} (X) - \mu_ {0} (X) \} ]}{E \{w (X) \}}
$$

where $w(X) = e(X)\{1 - e(X)\}$ is the overlap weight introduced in Chapter 13.4.

Remark: Vansteelandt and Dukes (2022) gave the formula in part 1 without a detailed proof. The result in part 2 was derived many times in the literature (e.g., Angrist, 1998; Ding, 2021).

# 14.5 Analyzing a dataset from the Karolinska Institute

Revisit Problem 12.5. Estimate $\tau_{\mathrm{O}}$ and $\tau$ based on the methods introduced in this Chapter.

# 14.6 Recommended reading

Kang and Schafer (2007) gave a critical review of the doubly robust estimator, using simulation to compare it with many other estimators. Robins et al. (2007) gave a very insightful comment on Kang and Schafer (2007).

# 15

# Matching in Observational Studies

Matching has a long history in empirical research. W. Cochran and D. Rubin popularized it in statistical causal inference. Cochran and Rubin (1973) is an early review paper. Rubin (2006b) collects Rubin's contributions to this topic. This chapter also discusses modern contributions by Abadie and Imbens (2006, 2008, 2011) based on the asymptotic analysis of matching estimators.

# 15.1 A simple starting point: many more control units

![](images/0d7f1a9a1d041e3ac4484f00530806c4b6925686e0bd3b48d2125d50e2cc8620.jpg)  
FIGURE 15.1: Illustration of matching in observational studies

Figure 15.1 illustrates the basic idea of matching in treatment-control observational studies. Consider a simple case with the number of control units $n_0$ being much larger than the number of treated units $n_1$ . For unit $i = 1, \ldots, n_1$ in the treated group, we find a unit $m(i)$ in the control group such that $X_i = X_{m(i)}$ . In the ideal case, we have exact matches. Therefore, the units within a matched pair have the same propensity score $e(X_i) = e(X_{m(i)})$ . Consequently, conditional on the event that one unit receives the treatment and the other receives the control, the probability of unit $i$ receiving the treatment and unit $m(i)$ receiving the control is

$$
\operatorname * {p r} (Z _ {i} = 1, Z _ {m (i)} = 0 \mid Z _ {i} + Z _ {m (i)} = 1, X _ {i}, X _ {m (i)}) = 1 / 2
$$

by a symmetry argument. $^{1}$ That is, the treatment assignment is identical to the MPE conditioning on the covariates and the event that each pair has a treated unit and a control unit. So we can analyze the exactly matched observational study as if it is an MPE, using either the FRT or the Neymanian approach in Chapter 7. This gives us inference on the causal effect on the treated units.

We can also find multiple control units for each treated unit. In general, we can find $M_{i}$ matched control units for the treated unit $i$ . When the $M_{i}$ 's vary, it is called the variable-ratio matching (Ming and Rosenbaum, 2000, 2001; Pimentel et al., 2015). With perfect matching, the treatment assignment mechanism is identical to the general matched experiment discussed in Section 7.7. We can use the analytic results in that section to analyze the matched observational study.

Rosenbaum (2002b) advocated the above analysis strategy. In most observational studies, however, $X_{i} = X_{m(i)}$ does not hold for all units. The above reasoning for FRT does not hold. Recently, Guo and Rothenhäsler (2022) reported negative results on the consequence of inexact matching in FRT. This is a warning of this strategy.

# 15.2 A more complicated but realistic scenario

Even if the control group is large, we often do not have exact matches. What we can achieve is that $X_{i} \approx X_{m(i)}$ or $X_{i} - X_{m(i)}$ is small under some distance metric. So we have only approximate matches. For example, we define

$$
m (i) = \arg \min _ {k: Z _ {k} = 0} d (X _ {i}, X _ {k}),
$$

where $d(X_{i},X_{k})$ measures the distance between $X_{i}$ and $X_{k}$ . Some canonical choices of the distance are the Euclidean distance

$$
d \left(X _ {i}, X _ {k}\right) = \left(X _ {i} - X _ {k}\right) ^ {\mathrm {T}} \left(X _ {i} - X _ {k}\right),
$$

and the Mahalanobis distance

$$
d (X _ {i}, X _ {k}) = \left(X _ {i} - X _ {k}\right) ^ {\top} \Omega^ {- 1} \left(X _ {i} - X _ {k}\right)
$$

with $\Omega$ being the sample covariance matrix of the $X_{i}$ 's from the whole population or only the control group.

I review some subtle issues about matching below. See Stuart (2010) for a review paper.

1. (one-to-one or one-to- $M$ matching) The above discussion focused on one-to-one matching. We can also extend the discussion to one-to- $M$ matching.   
2. I focus on matching with replacement but some practitioners prefer matching without replacement. If the pool of control units is large, these two methods will not differ too much for the final result. Matching with replacement is computationally more convenient, but matching without replacement involves computationally intensive discrete optimization. Matching with replacement usually gives matches of higher quality but it introduces dependence by using the same units multiple times. In contrast, the advantage of matching without replacement is the independence of matched units and the simplicity in the subsequent data analysis.   
3. Because of the residual covariate imbalance within matched pairs, it is crucial to use covariate adjustment when analyzing the data. In this case, covariate adjustment is not only for efficiency gain but also for bias correction.   
4. If $X$ is "high dimensional", it is likely that $d(X_{i},X_{k})$ is too large for some unit $i$ in the treated group and for all choices of the units in the control group. If this happens, we may have to drop some units that are hard to find matches. By doing this, we effectively change the study population of interest.

5. It is hard to avoid the above problem. For example, if $X_{i} \sim \mathrm{N}(0, I_{p}), X_{k} \sim \mathrm{N}(0, I_{p})$ , and $X_{i} \perp X_{k}$ , then

$$
\left(X _ {i} - X _ {k}\right) ^ {\mathsf {T}} \left(X _ {i} - X _ {k}\right) \sim 2 \chi_ {p} ^ {2}
$$

which has mean $2p$ and variance $8p$ (see Chapter A.1.3). Theory shows that with large $p$ , imperfect matching causes a large bias in causal effect estimation. This suggests that if $p$ is large, we must do some dimension reduction before matching. Rosenbaum and Rubin (1983b) proposed to use matching based on the propensity score. With the estimated propensity score, we find pairs of units $\{i,m(i)\}$ with small values of $|\hat{e}(X_i) - \hat{e}(X_{m(i)})|$ or $|\mathrm{logit}\{\hat{e}(X_i)\} - \mathrm{logit}\{\hat{e}(X_{m(i)})\}|^2$ , i.e., we have a one-dimensional matching problem.

# 15.3 Matching estimator for the average causal effect

In a sequence of papers, Abadie and Imbens (AI) rigorously characterized the asymptotic properties of the matching estimator and proposed the corresponding large-sample confidence intervals for the average causal effect. They chose the standard setup for observational studies with $\{X_{i},Z_{i},Y_{i}(1),Y_{i}(0)\}_{i = 1}^{n}\stackrel {\mathrm{IID}}{\sim}\{X,Z,Y(1),Y(0)\}$ .

# 15.3.1 Point estimation and bias correction

AI focused on $1 - M$ matching with replacement. For a treated unit $i$ , we can simply impute the potential outcome under the treatment as $\hat{Y}_i(1) = Y_i$ , and impute the potential outcome under the control as

$$
\hat {Y} _ {i} (0) = M ^ {- 1} \sum_ {k \in J _ {i}} Y _ {k},
$$

where $J_{i}$ is the set of matched units from the control group for unit $i$ . For example, we can compute $d(X_{i},X_{k})$ for all $k$ in the control group, and then define $J_{i}$ as the indices of $k$ with the $M$ smallest values of $d(X_{i},X_{k})$ .

For a control unit $i$ , we simply impute the potential outcome under the control as $\hat{Y}_i(0) = Y_i$ , and impute the potential outcome under the treatment as

$$
\hat {Y} _ {i} (1) = M ^ {- 1} \sum_ {k \in J _ {i}} Y _ {k},
$$

where $J_{i}$ is the set of matched units from the treatment group for unit $i$ .

The matching estimator is

$$
\hat {\tau} ^ {\mathrm {m}} = n ^ {- 1} \sum_ {i = 1} ^ {n} \{\hat {Y} _ {i} (1) - \hat {Y} _ {i} (0) \}.
$$

AI showed that $\hat{\tau}^{\mathrm{m}}$ has non-negligible bias especially when $X$ is multidimensional and the number of control units is comparable to the number of treated units. Through some technical derivations, they proposed the following estimator for the bias:

$$
\hat {B} = n ^ {- 1} \sum_ {i = 1} ^ {n} \hat {B} _ {i}
$$

where

$$
\hat {B} _ {i} = (2 Z _ {i} - 1) M ^ {- 1} \sum_ {k \in J _ {i}} \left\{\hat {\mu} _ {1 - Z _ {i}} \left(X _ {i}\right) - \hat {\mu} _ {1 - Z _ {i}} \left(X _ {k}\right) \right\}
$$

with $\{\hat{\mu}_1(X_i),\hat{\mu}_0(X_i)\}$ being the predicted outcomes by, for example, OLS fits. For a treated unit with $Z_{i} = 1$ , the estimated bias is

$$
\hat {B} _ {i} = M ^ {- 1} \sum_ {k \in J _ {i}} \{\hat {\mu} _ {0} (X _ {i}) - \hat {\mu} _ {0} (X _ {k}) \}
$$

which corrects the discrepancy in predicted control potential outcomes due to the mismatch in covariates; for a control unit with $Z_{i} = 0$ , the estimated bias is

$$
\hat {B} _ {i} = - M ^ {- 1} \sum_ {k \in J _ {i}} \left\{\hat {\mu} _ {1} \left(X _ {i}\right) - \hat {\mu} _ {1} \left(X _ {k}\right) \right\}
$$

which corrects the discrepancy in predicted treated potential outcomes due to the mismatch in covariates.

The final bias-corrected matching estimator is

$$
\hat {\tau} ^ {\mathrm {m b c}} = \hat {\tau} ^ {\mathrm {m}} - \hat {B},
$$

which has the following linear expansion.

Proposition 15.1 We have

$$
\hat {\tau} ^ {\mathrm {m b c}} = n ^ {- 1} \sum_ {i = 1} ^ {n} \hat {\psi} _ {i} \tag {15.1}
$$

where

$$
\hat {\psi} _ {i} = \hat {\mu} _ {1} (X _ {i}) - \hat {\mu} _ {0} (X _ {i}) + (2 Z _ {i} - 1) (1 + K _ {i} / M) \{Y _ {i} - \hat {\mu} _ {Z _ {i}} (X _ {i}) \}
$$

with $K_{i}$ being the times that unit $i$ is used as a match.

The linear expansion in Proposition 15.1 follows from simple but tedious algebra. I leave its proof as Problem 15.1. The linear expansion motivates a simple variance estimator

$$
\hat {V} ^ {\mathrm {m b c}} = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} (\hat {\psi} _ {i} - \hat {\tau} ^ {\mathrm {m b c}}) ^ {2},
$$

by viewing $\hat{\tau}^{\mathrm{mbc}}$ as sample averages of the $\hat{\psi}_i$ 's. Abadie and Imbens (2008) first showed that the simple bootstrap by resampling the original data does not work for estimating the variance of the matching estimators, but their proposed variance estimation procedure is not easy to implement. Otsu and Rai (2017) proposed to bootstrap the $\hat{\psi}_i$ 's in the linear expansion. However, Otsu and Rai (2017)'s bootstrap essentially yields the variance estimator $\hat{V}^{\mathrm{mbc}}$ , which is simple to calculate.

# 15.3.2 Connection with the doubly robust estimators

The bias-corrected matching estimators and the doubly robust estimators are closely related. They both equal the outcome regression estimator with some modifications based on the residuals

$$
\hat {R} _ {i} = \left\{ \begin{array}{l l} Y _ {i} - \hat {\mu} _ {1} (X _ {i}) & \text {i f} Z _ {i} = 1; \\ Y _ {i} - \hat {\mu} _ {0} (X _ {i}) & \text {i f} Z _ {i} = 0. \end{array} \right.
$$

For the average causal effect $\tau$ , recall the outcome regression estimator

$$
\hat {\tau} ^ {\mathrm {r e g}} = n ^ {- 1} \sum_ {i = 1} ^ {n} \{\hat {\mu} _ {1} (X _ {i}) - \hat {\mu} _ {0} (X _ {i}) \}
$$

and the doubly robust estimator

$$
\hat {\tau} ^ {\mathrm {d r}} = \hat {\tau} ^ {\mathrm {r e g}} + n ^ {- 1} \sum_ {i = 1} ^ {n} \left\{\frac {Z _ {i} \hat {R} _ {i}}{\hat {e} (X _ {i})} - \frac {(1 - Z _ {i}) \hat {R} _ {i}}{1 - \hat {e} (X _ {i})} \right\}.
$$

Furthermore, we can verify that $\hat{\tau}^{\mathrm{mbc}}$ has a form similar to $\hat{\tau}^{\mathrm{dr}}$ .

Proposition 15.2 The bias-corrected matching estimator for $\tau$ equals

$$
\hat {\tau} ^ {\mathrm {m b c}} = \hat {\tau} ^ {\mathrm {r e g}} + n ^ {- 1} \sum_ {i = 1} ^ {n} \left\{\left(1 + \frac {K _ {i}}{M}\right) Z _ {i} \hat {R} _ {i} - \left(1 + \frac {K _ {i}}{M}\right) (1 - Z _ {i}) \hat {R} _ {i} \right\}.
$$

I leave the proof of Proposition 15.2 as Problem 15.2. From Proposition 15.2, we can view matching as a nonparametric method to estimate the propensity score, and the resulting bias-corrected matching estimator as a doubly robust estimator. For instance, $1 + K_{i} / M$ should be close to $1 / \hat{e}(X_{i})$ . When a treated unit has a small $e(X_{i})$ , the resulting weight based on the

estimated propensity score $1 / \hat{e}(X_i)$ will be large, and at the same time, it will be matched to many control units, resulting in large $K_i$ and thus large $1 + K_i / M$ . However, this connection also raised an obvious question regarding matching. With a fixed $M$ , the estimator $1 + K_i / M$ for $1 / e(X_i)$ will be very noisy. Allowing $M$ to grow with the sampling size is likely to improve the matching-based nonparametric estimator for the propensity score and thus improve the asymptotic properties of the matching and bias-corrected matching estimators. Lin et al. (2023) provided a formal theory that once we allow $M$ to grow at a proper rate, the bias-corrected matching estimator $\hat{\tau}^{\mathrm{mbc}}$ can achieve similar properties as the doubly robust estimator.

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

corrects the bias due to the mismatch of covariates for a treated unit with $Z_{i} = 1$ .

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

I leave the proof to Problem 15.1. Motivated by Otsu and Rai (2017), we can view $\hat{\tau}_{\mathrm{T}}^{\mathrm{mbc}}$ as $n / n_{1}$ multiplied by the sample average of the $\hat{\psi}_{\mathrm{T},i}$ 's, so an intuitive variance estimator is

$$
\hat {V} _ {\mathrm {T}} ^ {\mathrm {m b c}} = \left(\frac {n}{n _ {1}}\right) ^ {2} \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} (\hat {\psi} _ {\mathrm {T}, i} - \hat {\tau} _ {\mathrm {T}} ^ {\mathrm {m b c}} n _ {1} / n) ^ {2} = \frac {1}{n _ {1} ^ {2}} \sum_ {i = 1} ^ {n} (\hat {\psi} _ {\mathrm {T}, i} - \hat {\tau} _ {\mathrm {T}} ^ {\mathrm {m b c}} n _ {1} / n) ^ {2}.
$$

Similar to the discussion in Section 15.3.2, we can compare the doubly robust and bias-corrected matching estimators with the outcome regression estimator. For the average causal effect on the treated units $\tau_{\mathrm{T}}$ , recall the outcome regression estimator

$$
\hat {\tau} _ {\mathrm {T}} ^ {\mathrm {r e g}} = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} \left\{Y _ {i} - \hat {\mu} _ {0} \left(X _ {i}\right) \right\},
$$

and the doubly robust estimator

$$
\hat {\tau} _ {\mathrm {T}} ^ {\mathrm {d r}} = \hat {\tau} _ {\mathrm {T}} ^ {\mathrm {r e g}} - n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} \frac {\hat {e} (X _ {i})}{1 - \hat {e} (X _ {i})} (1 - Z _ {i}) \hat {R} _ {i}.
$$

Furthermore, we can verify that $\hat{\tau}_{\mathrm{T}}^{\mathrm{mbc}}$ has a form similar to $\hat{\tau}_{\mathrm{T}}^{\mathrm{dr}}$ .

Proposition 15.4 The bias correction matching estimator for $\tau_{\mathrm{T}}$ equals

$$
\hat {\tau} _ {\mathrm {T}} ^ {\mathrm {m b c}} = \hat {\tau} _ {\mathrm {T}} ^ {\mathrm {r e g}} - n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} \frac {K _ {i}}{M} (1 - Z _ {i}) \hat {R} _ {i}.
$$

I leave the proof of Proposition 15.4 as Problem 15.3. Proposition 15.4 suggests that matching essentially uses $K_{i} / M$ to estimate the odds of the treatment given covariates.

# 15.5 A case study

# 15.5.1 Experimental data

Now I revisit the LaLonde data using Sekhon (2011)'s Matching package. We have used this package several times for the dataset 1alonde, and now we will use its key function Match. The experimental part gives us the following results:

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
Original number of observations.. 445   
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
> z = da $treat
> x = as.matrix(da[ , c("age", "educ", "black",
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

Matched number of observations. 185

Matched number of observations (unweighted). 248

Ignoring the ties in the matched data, we can also use the matched-pairs analysis, which again yields results similar to those based on the experimental data:

```txt
>diff = y[matchest\\(index.treated] - +y[matchest\\)index.control] > round (summary(lm(diff ~ 1))\\(coef [1, ], 2) Estimate Std. Error t value \)\operatorname*{Pr}(\text{>}|\text{t}|)$ 1581.44 558.55 2.83 0.01 > diff.x = x[matchest\\)index.treated, ] - +x[matchest\\(index.control, ] > round (summary(lm(diff ~ diff.x))\\)coef [1, ], 2) Estimate Std. Error t value \)\operatorname*{Pr}(\text{>}|\text{t}|)$ 1842.06 578.37 3.18 0.00 
```

# 15.5.3 Covariate balance checks

Moreover, we can use simple OLS to check covariate balance. Before matching, the covariates are highly imbalanced, signified by many stars associated with the coefficients.

>lm.before $\equiv$ lm(z\~x)

> summary(1m_before)

Residuals:   
```txt
Min 1Q Median 3Q Max -0.18508 -0.01057 0.00303 0.01018 1.01355
```

Coefficients:   
Estimate Std. Error t value $\mathrm{Pr}(|t|)$ (Intercept) 1.404e-03 6.326e-03 0.222 0.8243 xage -4.043e-04 8.512e-05 -4.750 2.05e-06 *** xeduc 3.220e-04 4.073e-04 0.790 0.4293 xblack 1.070e-01 2.902e-03 36.871 < 2e-16 *** xhispan 6.377e-03 3.103e-03 2.055 0.0399 * xmarried -1.525e-02 2.023e-03 -7.537 5.06e-14 *** xnodegree 1.345e-02 2.523e-03 5.331 9.89e-08 *** xre74 7.601e-07 1.806e-07 4.208 2.59e-05 *** xre75 -1.231e-07 1.829e-07 -0.673 0.5011 xu74 4.224e-02 3.271e-03 12.914 < 2e-16 *** xu75 2.424e-02 3.399e-03 7.133 1.02e-12 ***

However, after matching, the covariates are well-balanced, signified by the absence of stars for all coefficients.

>lm.after $= \mathrm{lm(z}$ ~x,

+ subset = c(matchest\ $index.treated, + matchest\$ index.control)) > summary(lm.after)

Residuals:

```txt
Min 1Q Median 3Q Max -0.66864 -0.49161 -0.03679 0.50378 0.65122
```

Coefficients:

```txt
Estimate Std. Error t value Pr(>|t|) (Intercept) 6.003e-01 2.427e-01 2.474 0.0137 * xage 3.199e-03 3.427e-03 0.933 0.3511 xeduc -1.501e-02 1.634e-02 -0.918 0.3590 xblack 6.141e-05 7.408e-02 0.001 0.9993 xhispan 1.391e-02 1.208e-01 0.115 0.9084 xmarried -1.328e-02 6.729e-02 -0.197 0.8437 xnodegree -3.023e-02 7.144e-02 -0.423 0.6723 xre74 6.754e-06 9.864e-06 0.685 0.4939 xre75 -9.848e-06 1.279e-05 -0.770 0.4417 xu74 2.179e-02 1.027e-01 0.212 0.8321 xu75 -2.642e-02 8.327e-02 -0.317 0.7512 
```

# 15.6 Discussion

With many covariates, matching based on the original covariates may suffer from the curse of dimensionality. Rosenbaum and Rubin (1983b) suggested to use matching based on the estimated propensity score. Abadie and Imbens (2016) provided a form theory for this strategy.

# 15.7 Homework Problems

15.1 Linear expansions of the bias-corrected estimators

Prove Propositions 15.1 and 15.3.

15.2 Doubly robust form of the bias-corrected matching estimator for $\tau$

Prove Proposition 15.2.

15.3 Doubly robust form of the bias-corrected matching estimator for $\tau_{\mathrm{T}}$

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

Part III of this book discusses causal inference with observational studies under two assumptions: unconfoundedness and overlap. Both are strong assumptions and are likely to be violated in practice. This chapter will discuss the difficulties of the unconfoundedness assumption. Chapters 17-19 will discuss various strategies for sensitivity analysis in observational studies with unmeasured confounding. Chapter 20 will discuss the difficulties of the overlap assumption.

# 16.1 Some basics of the causal diagram

Pearl (1995) introduced the causal diagram as a powerful tool for causal inference in empirical research. Pearl (2000) is a textbook on the causal diagram. Here I introduce the causal diagram as an intuitive tool for illustrating the causal relationships among variables.

For example, if we have the causal diagram

![](images/5ab54c7d19e9f188a0db28eda065b4f21c8cdee7b1e0f8752b44654d7cde68c9.jpg)

and focus on the causal effect of $Z$ on $Y$ , we can read it as the following data-generating process:

$$
\left\{ \begin{array}{l} X \sim F _ {X} (x), \\ Z = f _ {Z} (X, \varepsilon_ {Z}), \\ Y (z) = f _ {Y} (X, z, \varepsilon_ {Y} (z)), \end{array} \right.
$$

where $\varepsilon_Z\perp \varepsilon_Y(z)$ for both $z = 0,1$ . In the above, covariates $X$ are generated from a distribution $F_{X}(x)$ , the treatment assignment is a function of $X$ with a random error term $\varepsilon_{Z}$ , and the potential outcome $Y(z)$ is a function of $X$ , $z$ and a random error term $\varepsilon_{Y}(z)$ . We can easily read from the equations that $Z\perp Y(z)\mid X$ , i.e., the unconfoundedness assumption holds.

If we have a causal diagram

![](images/4c253bc521d043bd68c0b8419645a420cef38ab7fe7bd9c1368a56be399a2f11.jpg)

we can read it as the following data-generating process:

$$
\left\{ \begin{array}{l} X \sim F _ {X} (x), \\ U \sim F _ {U} (u), \\ Z = f _ {Z} (X, U, \varepsilon_ {Z}), \\ Y (z) = f _ {Y} (X, U, z, \varepsilon_ {Y} (z)), \end{array} \right.
$$

where $\varepsilon_{Z} \perp \perp \varepsilon_{Y}(z)$ for both $z = 0,1$ . We can easily read from the equations that $Z \perp Y(z) \mid (X,U)$ but $Z \not\perp Y(z) \mid X$ , i.e., the unconfoundedness assumption holds conditional on $(X,U)$ but does not hold conditional on $X$ only. In this case, $U$ is an unmeasured confounder. In this diagram, $U$ is called an unmeasured confounder.

# 16.2 Assessing the unconfoundedness assumption

The unconfoundedness assumption

$$
Z \bot Y (1) \mid X, \quad Z \bot Y (0) \mid X
$$

implies that

$$
\operatorname * {p r} \{Y (1) \mid Z = 1, X \} = \operatorname * {p r} \{Y (1) \mid Z = 0, X \},
$$

$$
\operatorname * {p r} \{Y (0) \mid Z = 1, X \} = \operatorname * {p r} \{Y (0) \mid Z = 0, X \}.
$$

So the unconfoundedness assumption basically requires that the counterfactual distribution $\operatorname{pr}\{Y(1) \mid Z = 0, X\}$ equals the observed distribution $\operatorname{pr}\{Y(1) \mid Z = 1, X\}$ , and the counterfactual distribution $\operatorname{pr}\{Y(0) \mid Z = 1, X\}$ equals the observed distribution $\operatorname{pr}\{Y(0) \mid Z = 0, X\}$ . Because the counterfactual distributions are not directly identifiable from the data, the unconfoundedness assumption is fundamentally untestable without additional assumptions. I will discuss two strategies to assess the unconfoundedness assumption. Here, "assess" is a weaker notion than "test". The former is referred to as supplementary analysis that supports or undermines the initial analysis, but the latter is referred to as formal statistical testing.

# 16.2.1 Using negative outcomes

Assume that $Y^{\mathrm{n}}$ is an outcome similar to $Y$ and ideally, shares the same confounding structure as $Y$ . If we believe $Z \bot Y(z) \mid X$ , then we also tend to believe $Z \bot Y^{\mathrm{n}}(z) \mid X$ . Moreover, we know, a priori, the effect of $Z$ on $Y^{\mathrm{n}}$ :

$$
\tau (Z \to Y ^ {\mathrm {n}}) = E \{Y ^ {\mathrm {n}} (1) - Y ^ {\mathrm {n}} (0) \}.
$$

An important example is that $\tau(Z \to Y^n) = 0$ . A causal diagram satisfying these requirements is below:

![](images/8a164b9422e91403f122b0d5962ad8fcaddb6c292ea5c39479b4de8b42806f49.jpg)

Example 16.1 Cornfield et al. (1959) studied the causal role of cigarette smoking on lung cancer based on observational studies. They controlled for many important background variables but it is still possible to have some unmeasured confounders biasing the observed effects. To strengthen the evidence for causation, they also reported the effect of cigarette smoking on car accidents, which was close to zero, the anticipated effect based on biology. So even if they could not rule out unmeasured confounding in the analysis, this supplementary analysis based on a negative outcome makes the evidence of the causal effect of cigarette smoking on lung cancer stronger.

Example 16.2 Imbens and Rubin (2015) suggested using the lagged outcome as a negative outcome. In most cases, it is reasonable to believe that the lagged outcome and the outcome have a similar confounding structure. Since the lagged outcome happens before the treatment, the average causal effect on it must be 0. However, their suggestion should be used with caution since in most studies we simply treat lagged outcomes as an observed confounder.

In some sense, the covariate balance check in Chapter 11 is a special case of using negative controls. Similar to the problem of using lagged outcomes as negative controls, those covariates are usually a part of the unconfoundedness assumption. Therefore, the failure of the covariate balance check does not really falsify the unconfoundedness assumption but rather the model specification of the propensity score.

Example 16.3 Observational studies of elderly persons have shown that vaccination against influenza remarkably reduces one's risk of pneumonia/influenza hospitalization and all-cause mortality in the following season, after adjustment for measured covariates. Jackson et al. (2006) were skeptical about the large magnitude and thus conducted supplementary analysis on negative outcomes. Vaccination often begins in the fall, but influenza transmission is often minimal until the winter. Based on biology, the effect of vaccination should be most prominent during influenza season. But Jackson et al. (2006)

found a greater effect before the influenza season, suggesting that the observed effect is due to unmeasured confounding.

Jackson et al. (2006) seems the most convincing one since the influenza-related outcomes before and during the influenza season should have similar confounding patterns. Cornfield et al. (1959)'s additional evidence seems weaker since car accidents and lung cancer have very different causal mechanisms with respect to cigarette smoking. In fact, Fisher (1957)'s critique was that the relationship between cigarette smoking on lung cancer may be due to an unobserved genetic factor (see Chapter 17). Such a genetic factor might affect cigarette smoking and lung cancer simultaneously, but it seems unlikely that it also affects car accidents.

Lipsitch et al. (2010) is a recent article on negative outcomes. Rosenbaum (1989) discussed the role of known effects in causal inference.

# 16.2.2 Using negative exposures

Negative exposures are duals of negative outcomes. Assume $Z^n$ is a treatment variable similar to $Z$ and shares the same confounding structure as $Z$ . If we believe $Z \bot Y(z) \mid X$ , then we tend to believe $Z^n \bot Y(z) \mid X$ . Moreover, we know, a priori, the effect of $Z^n$ on $Y$

$$
\tau (Z ^ {\mathrm {n}} \to Y) = E \{Y (1 ^ {\mathrm {n}}) - Y (0 ^ {\mathrm {n}}) \}.
$$

An important example is that $\tau(Z^n \to Y) = 0$ . A causal diagram satisfying these requirements is below:

![](images/0bb216ce88c5c03c11b1a8558fc093f4d061b6bfea3eda20b00ef32232e39110.jpg)

Example 16.4 Sanderson et al. (2017) give many examples of negative exposures in determining the effect of intrauterine exposure on later outcomes by comparing the association of maternal exposure during pregnancy with the outcome of interest, with the association of paternal exposure with the same outcome. They review studies on the effect of maternal and paternal smoking on offspring outcomes, and studies on the effect of maternal and paternal BMI on later offspring BMI and autism spectrum disorder. In these examples, we expect the association of maternal exposure with the outcome to be larger than that of paternal exposure with the outcome.

# 16.2.3 Summary

The unconfoundedness assumption is fundamentally untestable without additional assumptions. Although negative outcomes and negative controls in

observational studies cannot prove or disprove unconfoundedness, using them in supplementary analyses can strengthen the evidence for causation. However, it is often non-trivial to conduct this type of supplementary analysis because it involves more data and more importantly, a deeper understanding of the causal problems to find convincing negative outcomes and negative controls.

# 16.3 Problems of over-adjustment

We have discussed many methods for estimating causal effects under the unconfoundedness assumption:

$$
Z \text {止} \{Y (1), Y (0) \} \mid X.
$$

This is an assumption conditioning on $X$ . It is crucial to select the right set of $X$ that ensures the conditional independence. Rosenbaum (2002b) wrote that "there is no reason to avoid adjustment for a variable describing subjects before treatment." Similarly, Rubin (2007) wrote that "typically, the more conditional an assumption, the more acceptable it is." Both argued that we should control for all observed pretreatment covariates. VanderWeele and Shpitser (2011) called it the pretreatment criterion. Pearl disagreed with this recommendation and gave two counterexamples below.

# 16.3.1 M-bias

M-bias appears in the following causal diagram with an M-structure:

![](images/139276dabfcc29fc945b654873674fefa292b07c490e896f30525d12b6172d7e.jpg)

We can read from the diagram the data-generating process:

$$
\left\{ \begin{array}{l} U _ {1} \perp \perp U _ {2}, \\ X = f _ {X} (U _ {1}, U _ {2}, \varepsilon_ {X}), \\ Z = f _ {Z} (U _ {1}, \varepsilon_ {Z}), \\ Y = Y (z) = f _ {Y} (U _ {2}, \varepsilon_ {Y}), \end{array} \right.
$$

where $(\varepsilon_{X},\varepsilon_{Z},\varepsilon_{Y})$ are independent random error terms. In the above causal

diagram, $X$ is observed, but $U_{1}$ and $U_{2}$ are unobserved. If we change the value of $Z$ , the value of $Y$ will not change at all. So the true causal effect of $Z$ on $Y$ must be 0. From the data-generating equations, we can read that $Z \bot Y$ , so the association between $Z$ and $Y$ is 0, and, in particular,

$$
\tau_ {\mathrm {P F}} = E (Y \mid Z = 1) - E (Y \mid Z = 0) = 0.
$$

This means that without adjusting for the covariate $X$ , the simple estimator is unbiased for the true parameter.

However, if we condition on $X$ , then $U_1 \nsubseteq U_2 \mid X$ , and consequently, $Z \nsubseteq Y \mid X$ and

$$
\int \{E (Y \mid Z = 1, X = x) - E (Y \mid Z = 0, X = x) \} f (x) \mathrm {d} x \neq 0
$$

in general. To gain intuition, we consider the case with Normal linear models<sup>1</sup>:

$$
\left\{ \begin{array}{l} X = a U _ {1} + b U _ {2} + \varepsilon_ {X}, \\ Z = c U _ {1} + \varepsilon_ {Z}, \\ Y = Y (z) = d U _ {2} + \varepsilon_ {Y}, \end{array} \right.
$$

where $(U_{1},U_{2},\varepsilon_{X},\varepsilon_{Z},\varepsilon_{Y})\stackrel {\mathrm{IID}}{\sim}\mathrm{N}(0,1)$ . We have

$$
\operatorname {c o v} (Z, Y) = \operatorname {c o v} \left(c U _ {1} + \varepsilon_ {Z}, d U _ {2} + \varepsilon_ {Y}\right) = 0,
$$

but by the result in Problem 1.3, the partial correlation coefficient between $Z$ and $Y$ given $X$ is<sup>2</sup>

$$
\begin{array}{l} \rho_ {Z Y | X} = \frac {\rho_ {Z Y} - \rho_ {Z X} \rho_ {Y X}}{\sqrt {1 - \rho_ {Z X} ^ {2}} \sqrt {1 - \rho_ {Y X} ^ {2}}} \\ \propto - \rho_ {Z X} \rho_ {Y X} \\ \propto - \operatorname {c o v} (Z, X) \operatorname {c o v} (Y, X) \\ = - a b c d, \\ \end{array}
$$

the product of the coefficients on the path from $Z$ to $Y$ . So the unadjusted estimator is unbiased but the adjusted estimator has a bias proportional to abcd.

The following simple example illustrates M-bias.

> ## M bias with large sample size   
> n = 10^6   
> U1 = rnorm(n)   
>U2 = rnorm(n)

```latex
\(>\mathrm{X}=\mathrm{U1}+\mathrm{U2}+\mathrm{rnorm}(\mathrm{n})\)   
\(>\mathrm{Y}=\mathrm{U2}+\mathrm{rnorm}(\mathrm{n})\)   
\(>\) ## with a continuous treatment Z   
\(>\mathrm{Z}=\mathrm{U1}+\mathrm{rnorm}(\mathrm{n})\)   
\(>\) round (summary \((\mathrm{lm}(Y\sim Z))\\) coef[2,1],3)\) [1]0   
\(>\) round (summary \((\mathrm{lm}(Y\sim Z + X))\\) coef[2,1],3)\) [1]-0.2   
>   
\(>\) ## with a binary treatment Z   
\(>\mathrm{Z}=(\mathrm{Z}>=0)\)   
\(>\) round (summary \((\mathrm{lm}(Y\sim Z))\\) coef[2,1],3)\) [1]0.002   
\(>\) round (summary \((\mathrm{lm}(Y\sim Z + X))\\) coef[2,1],3)\) [1]-0.42 
```

# 16.3.2 Z-bias

Consider the following causal diagram:

![](images/f92c799b68bb8ec34bca17d7e5ea75d759837700a19b46c79db33a05bc080f50.jpg)

with the data generating process

$$
\left\{ \begin{array}{l} Z = a X + b U + \varepsilon_ {Z}, \\ Y (z) = \tau z + c U + \varepsilon_ {Y}, \end{array} \right.
$$

where $(U,X,\varepsilon_Z,\varepsilon_Y)$ are IID $\mathrm{N}(0,1)$ . In this data-generating process, we have $X\perp U$ , $X\not\perp Z$ , and $X$ affects $Y$ only through $Z$ .

The unadjusted estimator is

$$
\begin{array}{l} \tau_ {\text {u n a d j}} = \frac {\operatorname {c o v} (Z , Y)}{\operatorname {v a r} (Z)} \\ = \frac {\operatorname {c o v} (Z , \tau Z + c U)}{\operatorname {v a r} (Z)} \\ = \tau + \frac {c \operatorname {c o v} (a X + b U , U)}{\operatorname {v a r} (Z)} \\ = \tau + \frac {c b}{a ^ {2} + b ^ {2} + 1}, \\ \end{array}
$$

which has bias $bc / (a^2 + b^2 + 1)$ . The adjusted estimator from the OLS of $Y$ on $(Z, X)$ satisfies

$$
\left\{ \begin{array}{l} E \{Z (Y - \tau_ {\mathrm {a d j}} Z - \alpha X) \} = 0, \\ E \{X (Y - \tau_ {\mathrm {a d j}} Z - \alpha X) \} = 0. \end{array} \right.
$$

Solve the above linear system of $(\tau_{\mathrm{adj}},\alpha)$ to obtain the formula of $\tau_{\mathrm{adj}}$ :

$$
\tau_ {\mathrm {a d j}} = \tau + \frac {b c}{b ^ {2} + 1}, \tag {16.1}
$$

which has bias $bc / (b^2 + 1)$ . I relegate the details for solving the linear system of $(\tau_{\mathrm{adj}}, \alpha)$ as Problem 16.1.

So the unadjusted estimator has a smaller bias than the adjusted estimator. More interestingly, the stronger the association between $X$ and $Z$ is (measured by $a$ ), the larger the bias of the adjusted estimator is.

The mathematical derivation is not extremely hard. But this type of bias seems rather mysterious. Here is the intuition. The treatment is a function of $X$ , $U$ , and other random errors. If we condition on $X$ , it is merely a function of $U$ and other random errors. Therefore, conditioning on $X$ makes $Z$ less random, and more critically, makes the unmeasured confounder $U$ play a more important role in $Z$ . Consequently, the confounding bias due to $U$ is amplified by conditioning on $X$ . This idealized example illustrates the danger of overadjusting for some covariates.

Heckman and Navarro-Lozano (2004) observed this phenomenon in simulation studies. Wooldridge (2016, technical report in 2006) verified it in linear models. Pearl (2010a, 2011) explained it using causal diagrams. Ding et al. (2017b) provided a more general theory as well as some intuition for this phenomenon. This type of bias is called Z-bias because, in Pearl's original papers, he used the symbol $Z$ for our variable $X$ . Throughout the book, however, $Z$ is used for the treatment variable. In Part V of this book, we will call $Z$ an instrumental variable if it satisfies the causal diagram presented in this subsection. This justifies the instrumental variable bias as another name for this type of bias.

The following simple example illustrates Z-bias.

```txt
> ## Z bias with large sample size
> n = 10^6
> X = rnorm(n)
> U = rnorm(n)
> Z = X + U + rnorm(n)
> Y = U + rnorm(n)
>
> round.summary(1m(Y ~ Z)) $coef[2, 1], 3)
[1] 0.333
> round.summary(1m(Y ~ Z + X)) $coef[2, 1], 3)
[1] 0.501 
```

```txt
>>> stronger association between X and Z
>>> Z = 2*X + U + rnorm(n)
>>> round.summary(1m(Y ~ Z))$coef[2, 1], 3)
[1] 0.167
>>> round.summary(1m(Y ~ Z + X))$coef[2, 1], 3)
[1] 0.501
>>> stronger association between X and Z
>>> Z = 10*X + U + rnorm(n)
>>> round.summary(1m(Y ~ Z))$coef[2, 1], 3)
[1] 0.01
>>> summary(1m(Y ~ Z + X))$coef[2, 1], 3)
[1] 0.5 
```

# 16.3.3 What covariates should we adjust for in observational studies?

We never know the true underlying data-generating process which can be quite complicated. However, the following causal diagram helps to clarify many ideas. It already rules out the possibility of $M$ -bias discussed in Section 16.3.1.

![](images/2941f1cc054870515d1faaa9bd2230438b8be898e3f93fe14d1294c17914be26.jpg)  
$X_{R}$

The covariates above have different features:

1. $X$ affects both the treatment and the outcome. Conditioning on $X$ ensures the unconfoundedness assumption, so we should control for $X$ .   
2. $X_{R}$ is pure random noise not affecting either the treatment or the outcome. Including it in the analysis does not bias the estimate but introduces unnecessary variability in finite samples.

# 22816 Difficulties of Unconfoundedness in Observational Studies for Causal Effects

3. $X_Z$ is an instrumental variable that affects the outcome only through the treatment. In the diagram above, including it in the analysis does not bias the estimate but increases the variability of the estimate. However, with unmeasured confounding, including it in the analysis amplifies the bias as shown in Section 16.3.1.   
4. $X_{Y}$ affects the outcome only but not the treatment. Without conditioning on it, the unconfoundedness assumption still holds. Since they are predictive of the outcome, including them in analysis often improves precision.   
5. $X_{I}$ is affected by the treatment and outcome. It is a post-treatment variable, not a pretreatment covariate. We should not include it if the goal is to infer the effect of the treatment on the outcome. We will discuss issues with post-treatment variables in causal inference in Part VI of this book.

If we believe the above causal diagram, we should adjust for at least $X$ to remove bias and more ideally, further adjust for $X_{Y}$ to reduce variance.

# 16.4 Homework Problems

# 16.1 More details for the formula of $Z$ -bias

Verify (16.1).

# 16.2 Cochran's formula or the omitted variable bias formula

Sir David Cox calls the following result Cochran's formula (Cochran, 1938; Cox, 2007) and econometricians call it the omitted variable bias formula (Angrist and Pischke, 2008). A special case appeared in Fisher (1925). It is also a counterpart of the Frisch-Waugh-Lovell theorem in Chapter B.3.

The formula has two versions. All vectors below are column vectors.

1. (Population version) Assume $(y_{i},x_{1i},x_{2i})_{i = 1}^{n}$ are IID, where $y_{i}$ is a scalar, $x_{i1}$ has dimension $K$ , and $x_{i2}$ has dimension $L$ .

We have the following OLS decompositions of random variables

$$
y _ {i} = \beta_ {1} ^ {\mathrm {T}} x _ {i 1} + \beta_ {2} ^ {\mathrm {T}} x _ {2 i} + \varepsilon_ {i}, \tag {16.2}
$$

$$
y _ {i} = \gamma^ {\mathrm {T}} x _ {i 1} + e _ {i}, \tag {16.3}
$$

$$
x _ {i 2} = \delta^ {\mathsf {T}} x _ {i 1} + v _ {i}. \tag {16.4}
$$

Equation (16.2) is called the long regression, and Equation (16.3) is called the short regression. In Equation (16.4), $\delta$ is a matrix because

it is a regression of a vector on a vector. You can view (16.4) as regression of each component of $x_{i2}$ on $x_{i1}$ .

Show that $\gamma = \beta_{1} + \delta \beta_{2}$

2. (Sample version) We have an $n \times 1$ vector $Y$ , an $n \times K$ matrix $X_{1}$ , and an $n \times L$ matrix $X_{2}$ . We do not assume any randomness. All results below are purely linear algebra.

We can obtain the following OLS fits:

$$
\begin{array}{l} Y = X _ {1} \hat {\beta} _ {1} + X _ {2} \hat {\beta} _ {2} + \hat {\varepsilon}, \\ Y = X _ {1} \hat {\gamma} + \hat {e}, \\ X _ {2} = X _ {1} \hat {\delta} + \hat {v}, \\ \end{array}
$$

where $\hat{\varepsilon},\hat{e},\hat{v}$ are the residuals. Again, the last OLS fit means the OLS fit of each column of $X_{2}$ on $X_{1}$ , and therefore the residual $\hat{v}$ is an $n\times L$ matrix.

Show that $\hat{\gamma} = \hat{\beta}_1 + \hat{\delta}\hat{\beta}_2$

Remark: The product terms $\delta \beta_{2}$ and $\hat{\delta}\hat{\beta}_{2}$ are often referred to as the omitted-variable bias at the population level and sample level, respectively.

# 16.3 Recommended reading

Imbens (2020) reviews and compares the roles of potential outcomes and causal diagrams for causal inference.

# 17

# E-Value: Evidence for Causation in Observational Studies with Unmeasured Confounding

All the methods discussed in Part III rely crucially on the ignorability assumption. They require controlling for all confounding between the treatment and outcome. However, we cannot use the data to validate the ignorability assumption. Observational studies are often criticized due to the possibility of unmeasured confounding. The famous Yule-Simpson Paradox reviewed in Chapter 1 demonstrates that an unmeasured binary confounder can completely overturn an observed association between the treatment and outcome. However, to overturn a larger observed association, this unmeasured confounder must have a stronger association with the treatment and the outcome. In other words, not all observational studies are created equal. Some provide stronger evidence for causation than others.

The following three chapters will discuss various sensitivity analysis techniques that can quantify the evidence of causation based on observational studies in the presence of unmeasured confounding. This chapter starts with the E-value, introduced by VanderWeele and Ding (2017) based on the theory in Ding and VanderWeele (2016). It is more useful for observational studies using logistic regressions to estimate the conditional risk ratio of a treatment on a binary outcome. Chapter 18 discusses sensitivity analysis for the average causal effect based on outcome regression, IPW, and doubly robust estimation. Chapter 19 discusses Rosenbaum's framework for sensitivity analysis for matched observational studies.

# 17.1 Cornfield-type sensitivity analysis

Although we do not assume ignorability given $X$ :

$$
Z \nVdash \{Y (1), Y (0) \} \mid X,
$$

we still assume latent ignorability given $X$ and an unmeasured confounder $U$ :

$$
Z \sqcup \{Y (1), Y (0) \} \mid (X, U).
$$

The technique in this chapter works the best for a binary outcome $Y$ although it can be extended to other non-negative outcomes (Ding and VanderWeele, 2016). Focus on binary $Y$ now. The true conditional causal effect on the risk ratio scale is defined as

$$
\operatorname {R R} _ {Z Y | x} ^ {\text {t r u e}} = \frac {\operatorname* {p r} \left\{Y (1) = 1 \mid X = x \right\}}{\operatorname* {p r} \left\{Y (0) = 1 \mid X = x \right\}},
$$

and the observed conditional risk ratio equals

$$
\operatorname {R R} _ {Z Y | x} ^ {\mathrm {o b s}} = \frac {\operatorname* {p r} (Y = 1 \mid Z = 1 , X = x)}{\operatorname* {p r} (Y = 1 \mid Z = 0 , X = x)}.
$$

In general, with an unmeasured confounder $U$ , they are different:

$$
\mathrm {R R} _ {Z Y | x} ^ {\mathrm {t r u e}} \neq \mathrm {R R} _ {Z Y | x} ^ {\mathrm {o b s}}
$$

because

$$
\mathrm {R R} _ {Z Y | x} ^ {\mathrm {t r u e}} = \frac {\int \operatorname {p r} (Y = 1 \mid Z = 1 , X = x , U = u) f (u \mid X = x) \mathrm {d} u}{\int \operatorname {p r} (Y = 1 \mid Z = 0 , X = x , U = u) f (u \mid X = x) \mathrm {d} u}
$$

and

$$
\mathrm {R R} _ {Z Y | x} ^ {\mathrm {o b s}} = \frac {\int \operatorname {p r} (Y = 1 \mid Z = 1 , X = x , U = u) f (u \mid Z = 1 , X = x) \mathrm {d} u}{\int \operatorname {p r} (Y = 1 \mid Z = 0 , X = x , U = u) f (u \mid Z = 0 , X = x) \mathrm {d} u}
$$

areaveragedoverdifferentdistributionsof $U$

Historically, Doll and Hill (1950) found that the risk ratio of cigarette smoking on lung cancer was 9 even after adjusting for many observed covariates $X^{1}$ . Fisher (1957) criticized their result to be noncausal because it is possible that a hidden gene simultaneously causes cigarette smoking and lung cancer although the true causal effect of cigarette smoking on lung cancer is absent. This is the common cause hypothesis, also discussed by Reichenbach (1957). Cornfield et al. (1959) took a more constructive perspective and asked: how strong this unmeasured confounder must be to explain away the observed association between cigarette smoking and lung cancer? Below we will use Ding and VanderWeele (2016)'s general formulation of the problem.

Consider the following causal diagram:

![](images/595c7eb6964eadafa2519616b63b5c6b7bb47ad27017570695d0b32a6d907afd.jpg)

which conditions on $X$ . So $Z \perp Y \mid (X, U)$ . Conditioning on $X$ and $U$ , we

observe no association between $Z$ and $Y$ ; but conditioning on only $X$ , we observe an association between $Z$ and $Y$ . Although we can allow $U$ to be general as Ding and VanderWeele (2016), we assume that $U$ is binary to simplify the presentation.

Define two sensitivity parameters:

$$
\operatorname {R R} _ {Z U | x} = \frac {\operatorname* {p r} (U = 1 \mid Z = 1 , X = x)}{\operatorname* {p r} (U = 1 \mid Z = 0 , X = x)}
$$

measures the treatment-confounder association, and

$$
\operatorname {R R} _ {U Y | x} = \frac {\operatorname* {p r} (Y = 1 \mid U = 1 , X = x)}{\operatorname* {p r} (Y = 1 \mid U = 0 , X = x)},
$$

measures the confounder-outcome association, conditional on covariates $X = x$ . We can show the main result below.

Theorem 17.1 Under $Z \perp Y \mid (X, U)$ , assume

$$
\operatorname {R R} _ {Z Y | x} ^ {\mathrm {o b s}} > 1, \quad \operatorname {R R} _ {Z U | x} > 1, \quad \operatorname {R R} _ {U Y | x} > 1. \tag {17.1}
$$

We have

$$
\mathrm {R R} _ {Z Y | x} ^ {\mathrm {o b s}} \leq \frac {\mathrm {R R} _ {Z U | x} \mathrm {R R} _ {U Y | x}}{\mathrm {R R} _ {Z U | x} + \mathrm {R R} _ {U Y | x} - 1}.
$$

In Theorem 17.1, we assume (17.1) without loss of generality. If $\mathbb{R}\mathbb{R}_{ZY|x}^{\mathrm{obs}} < 1$ , we can relabel the treatment and control levels to ensure $\mathbb{R}\mathbb{R}_{ZY|x}^{\mathrm{obs}} > 1$ . If $\mathbb{R}\mathbb{R}_{ZU|x} < 1$ , we can redefine the unmeasured confounder $U$ as $1 - U$ to ensure $\mathbb{R}\mathbb{R}_{ZU|x} > 1$ . If $\mathbb{R}\mathbb{R}_{ZY|x}^{\mathrm{obs}} > 1$ and $\mathbb{R}\mathbb{R}_{ZU|x} > 1$ , then $\mathbb{R}\mathbb{R}_{UY|x} > 1$ holds automatically. I relegate this subtle technical detail to Problem 17.2.

Theorem 17.1 shows the upper bound of the observed risk ratio of the treatment on the outcome if the conditional independence $Z \perp Y \mid (X, U)$ holds. Under this conditional independence assumption, the association between the treatment and the outcome is purely due to the association between the treatment and the confounder $\mathrm{RR}_{ZU|x}$ , and the association between the confounder and the outcome, $\mathrm{RR}_{UY|x}$ . The upper bound equals $\mathrm{RR}_{ZU|x} \times \mathrm{RR}_{UY|x} / (\mathrm{RR}_{ZU|x} + \mathrm{RR}_{UY|x} - 1)$ . A similar inequality appeared in Lee (2011). It is also related to Cochran's formula or the omitted-variable bias formula for linear models, which was reviewed in Problem 16.2.

Reversely, to generate a certain value of the observed risk ratio $\mathrm{RR}_{ZY|x}^{\mathrm{obs}}$ , the two confounding measures $\mathrm{RR}_{ZU|x}$ and $\mathrm{RR}_{UY|x}$ cannot be arbitrary. Their function $\mathrm{RR}_{ZU|x} \times \mathrm{RR}_{UY|x} / (\mathrm{RR}_{ZU|x} + \mathrm{RR}_{UY|x} - 1)$ must be at least at large as $\mathrm{RR}_{ZY|x}^{\mathrm{obs}}$ .

I will give the proof of Theorem 17.1 below.

Proof of Theorem 17.1: Define

$$
f _ {1, x} = \operatorname {p r} (U = 1 \mid Z = 1, X = x), \quad f _ {0, x} = \operatorname {p r} (U = 1 \mid Z = 0, X = x).
$$

We can decompose $\mathrm{RR}_{ZY|x}^{\mathrm{obs}}$ as

$$
\begin{array}{l} \operatorname {R R} _ {Z Y | x} ^ {\mathrm {o b s}} \\ = \begin{array}{l} \operatorname {p r} (Y = 1 \mid Z = 1, X = x) \\ \hline \operatorname {p r} (Y = 1 \mid Z = 0, X = x) \end{array} \\ = \frac {\left[ \begin{array}{c} \operatorname {p r} (U = 1 \mid Z = 1 , X = x) \operatorname {p r} (Y = 1 \mid Z = 1 , U = 1 , X = x) \\ + \operatorname {p r} (U = 0 \mid Z = 1 , X = x) \operatorname {p r} (Y = 1 \mid Z = 1 , U = 0 , X = x) \end{array} \right]}{\left[ \begin{array}{c} \operatorname {p r} (U = 1 \mid Z = 0 , X = x) \operatorname {p r} (Y = 1 \mid Z = 0 , U = 1 , X = x) \\ + \operatorname {p r} (U = 0 \mid Z = 0 , X = x) \operatorname {p r} (Y = 1 \mid Z = 0 , U = 0 , X = x) \end{array} \right]} \\ = \frac {\left[ \begin{array}{c} \operatorname {p r} (U = 1 \mid Z = 1 , X = x) \operatorname {p r} (Y = 1 \mid U = 1 , X = x) \\ + \operatorname {p r} (U = 0 \mid Z = 1 , X = x) \operatorname {p r} (Y = 1 \mid U = 0 , X = x) \end{array} \right]}{\left[ \begin{array}{c} \operatorname {p r} (U = 1 \mid Z = 0 , X = x) \operatorname {p r} (Y = 1 \mid U = 1 , X = x) \\ + \operatorname {p r} (U = 0 \mid Z = 0 , X = x) \operatorname {p r} (Y = 1 \mid U = 0 , X = x) \end{array} \right]} \\ = \frac {f _ {1 , x} \mathrm {R R} _ {U Y | x} + 1 - f _ {1 , x}}{f _ {0 , x} \mathrm {R R} _ {U Y | x} + 1 - f _ {0 , x}} \\ = \frac {\left(\operatorname {R R} _ {U Y | x} - 1\right) f _ {1 , x} + 1}{\frac {\operatorname {R R} _ {U Y | x} - 1}{\operatorname {R R} _ {Z U | x}} f _ {1 , x} + 1}. \\ \end{array}
$$

We can verify that $\mathbb{R}\mathbb{R}_{ZY|x}^{\mathrm{obs}}$ is increasing in $f_{1,x}$ using the result in Problem 17.1. So letting $f_{1,x} = 1$ , we have

$$
\mathrm {R R} _ {Z Y | x} ^ {\mathrm {o b s}} \leq \frac {\left(\mathrm {R R} _ {U Y | x} - 1\right) + 1}{\frac {\mathrm {R R} _ {U Y | x} - 1}{\mathrm {R R} _ {Z U | x}} + 1} = \frac {\mathrm {R R} _ {Z U | x} \mathrm {R R} _ {U Y | x}}{\mathrm {R R} _ {Z U | x} + \mathrm {R R} _ {U Y | x} - 1}.
$$

In the proof of Theorem 17.1, we have obtain an identity

$$
\mathrm {R R} _ {Z Y | x} ^ {\mathrm {o b s}} = \frac {\left(\mathrm {R R} _ {U Y | x} - 1\right) f _ {1 , x} + 1}{\frac {\mathrm {R R} _ {U Y | x} - 1}{\mathrm {R R} _ {Z U | x}} f _ {1 , x} + 1}. \tag {17.2}
$$

But this identity involves three parameters

$$
\left\{f _ {1, x}, \operatorname {R R} _ {Z U | x}, \operatorname {R R} _ {U Y | x} \right\};
$$

see Problem 17.4 for a related formula. In contrast, the upper bound in Theorem 17.1 involves only two parameters

$$
\left\{\mathrm {R R} _ {Z U | x}, \mathrm {R R} _ {U Y | x} \right\}
$$

which measure the strength of the confounder. Mathematically, the identity 17.2 is stronger than the inequality in Theorem 17.1. However, 17.2 involves more sensitivity parameters compared with Theorem 17.1. Therefore, we face a trade-off of accuracy and convenience in sensitivity analysis.

# 17.2 E-value

Lemma 17.1 below is useful for deriving interesting corollaries of Theorem 17.1. I relegate its proof to Problem 17.3.

Lemma 17.1 Define $\beta (w_{1},w_{2}) = w_{1}w_{2} / (w_{1} + w_{2} - 1)$ for $w_{1} > 1$ and $w_{2} > 1$ .

$1.\beta (w_{1},w_{2})$ is symmetric in $w_{1}$ and $w_{2}$

$2\beta (w_{1},w_{2})$ is increasing in both $w_{1}$ and $w_{2}$

$3\beta (w_{1},w_{2})\leq w_{1}$ and $\beta (w_1,w_2)\leq w_2$

$4\beta (w_{1},w_{2})\leq w^{2} / (2w - 1)$ , where $w = \max (w_1,w_2)$

Using Theorem 17.1 and Lemma 17.1(3), we have

$$
\mathrm {R R} _ {Z U | x} \geq \mathrm {R R} _ {Z Y | x} ^ {\mathrm {o b s}}, \quad \mathrm {R R} _ {U Y | x} \geq \mathrm {R R} _ {Z Y | x} ^ {\mathrm {o b s}},
$$

or, equivalently,

$$
\min  \left(\mathrm {R R} _ {Z U | x}, \mathrm {R R} _ {U Y | x}\right) \geq \mathrm {R R} _ {Z Y | x} ^ {\mathrm {o b s}}.
$$

Therefore, to explain away the observed relative risk, both confounding measures $\mathrm{RR}_{ZU|x}$ and $\mathrm{RR}_{UY|x}$ must be at least as large as $\mathrm{RR}_{ZY|x}^{\mathrm{obs}}$ . Cornfield et al. (1959) first derived the inequality $\mathrm{RR}_{ZU|x} \geq \mathrm{RR}_{ZY|x}^{\mathrm{obs}}$ , also called the Cornfield inequality (Gastwirth et al., 1998). Schlesselman (1978) derived the inequality $\mathrm{RR}_{UY|x} \geq \mathrm{RR}_{ZY|x}^{\mathrm{obs}}$ . These are related to the data processing inequality in information theory<sup>2</sup>.

If we define $w = \max(\mathrm{RR}_{ZU|x}, \mathrm{RR}_{UY|x})$ , then we can use Theorem 17.1 and Lemma 17.1(4) to obtain

$$
\begin{array}{l} w ^ {2} / (2 w - 1) \geq \beta (\mathrm {R R} _ {Z U | x}, \mathrm {R R} _ {U Y | x}) \geq \mathrm {R R} _ {Z Y | x} ^ {\mathrm {o b s}} \\ \Longrightarrow \quad w ^ {2} - 2 \mathrm {R R} _ {Z Y | x} ^ {\mathrm {o b s}} w + \mathrm {R R} _ {Z Y | x} ^ {\mathrm {o b s}} \geq 0, \\ \end{array}
$$

which is a quadratic inequality. One root $\mathrm{RR}_{ZY|x}^{\mathrm{obs}} - \sqrt{\mathrm{RR}_{ZY|x}^{\mathrm{obs}}(\mathrm{RR}_{ZY|x}^{\mathrm{obs}} - 1)}$ is always smaller than or equal to 1, so we have

$$
w = \max (\mathrm {R R} _ {Z U | x}, \mathrm {R R} _ {U Y | x}) \geq \mathrm {R R} _ {Z Y | x} ^ {\mathrm {o b s}} + \sqrt {\mathrm {R R} _ {Z Y | x} ^ {\mathrm {o b s}} (\mathrm {R R} _ {Z Y | x} ^ {\mathrm {o b s}} - 1)}.
$$

Therefore, to explain away the observed relative risk, the maximum of the confounding measures $\mathrm{RR}_{ZU|x}$ and $\mathrm{RR}_{UY|x}$ must be at least as large as $\mathrm{RR}_{ZY|x}^{\mathrm{obs}} + \sqrt{\mathrm{RR}_{ZY|x}^{\mathrm{obs}}\left(\mathrm{RR}_{ZY|x}^{\mathrm{obs}} - 1\right)}$ . Based on this result, VanderWeele and Ding (2017) introduced the following notion of E-value for measuring the evidence of causation with observational studies.

Definition 17.1 (E-Value) With the observed conditional risk ratio $\mathrm{RR}_{ZY|x}^{\mathrm{obs}}$ , define the $E$ -Value as

$$
\mathrm {R R} _ {Z Y | x} ^ {\mathrm {o b s}} + \sqrt {\mathrm {R R} _ {Z Y | x} ^ {\mathrm {o b s}} (\mathrm {R R} _ {Z Y | x} ^ {\mathrm {o b s}} - 1)}.
$$

The E-value is defined for the parameter $\mathrm{RR}_{ZY|x}^{\mathrm{obs}}$ . In practice, $\mathrm{RR}_{ZY|x}^{\mathrm{obs}}$ is estimated with sampling error. We can calculate the E-value based on the estimated $\mathrm{RR}_{ZY|x}^{\mathrm{obs}}$ , as well as the corresponding E-values for the lower and upper confidence limits of $\mathrm{RR}_{ZY|x}^{\mathrm{obs}}$ .

Fisher's $p$ -value measures the evidence for causal effects in randomized experiments. We have discussed the $p$ -value based on the FRT in Part II of this book. However, in observational studies with large sample sizes, $p$ -values can be a poor measure of evidence for causal effects. Even if the true causal effects are 0, a tiny amount of unmeasured confounding can bias the estimate, which can result in extremely small $p$ -values given the small sampling uncertainty. The sampling uncertainty is usually secondary in observational studies with large sample sizes, but the uncertainty due to unmeasured confounding is often the first-order problem that does not diminish with increased sample sizes. VanderWeele and Ding (2017) argued that the E-value is a better measure of the evidence for causal effects in observational studies.

# 17.3 A classic example

I revisit a classic example below.

Example 17.1 Hammond and Horn (1958) used the U.S. population to study the cigarette smoking and lung cancer relationship. Ignoring covariates, their data can be represented by a two-by-two table below:

<table><tr><td></td><td>Lung cancer</td><td>No lung cancer</td></tr><tr><td>Smoker</td><td>397</td><td>78557</td></tr><tr><td>Non-smoker</td><td>51</td><td>108778</td></tr></table>

Based on the data, they obtained an estimate of the risk ratio 10.73 with a $95\%$ confidence interval [8.02, 14.36] (see Section A.3.2 for the formulas). To explain away the point estimate, the $E$ -value is

$$
1 0. 7 3 + \sqrt {1 0 . 7 3 \times (1 0 . 7 3 - 1)} = 2 0. 9 5;
$$

to explain away the lower confidence limit, the $E$ -value is

$$
8. 0 2 + \sqrt {8 . 0 2 \times (8 . 0 2 - 1)} = 1 5. 5 2.
$$

Figure 17.1 shows the joint values of the two confounding measures to explain away the point estimate and lower confidence limit of the risk ratio. In particular, to explain away the point estimate, they must lie in the area above the solid curve; to explain away the lower confidence limit, they must lie in the area above the dashed curve. $^3$

The simple R code below computes the numbers in Example 17.1:

```txt
> ## e-value based on RR
> evalue = function(rr)
+ {
+ rr + sqrt(rr * (rr - 1))
+ }
>
> p1 = 397 / (397 + 78557)
> p0 = 51 / (51 + 108778)
> rr = p1 / p0
> logrr = log(p1 / p0)
> se = sqrt(1 / 397 + 1 / 51 - 1 / (397 + 78557) - 1 / (51 + 108778))
> upper = exp(logrr + 1.96 * se)
> lower = exp(logrr - 1.96 * se)
>
> ## point estimate
> rr
[1] 10.72978
> ## lower CI
> lower
[1] 8.017414
> ## e-value based on rr
> evalue(rr)
[1] 20.94733
> ## e-value based on lower CI
> evalue(lower)
[1] 15.51818 
```

# 17.4 Extensions

# 17.4.1 E-value and Bradford Hill's criteria for causation

The E-value provides evidence for causation. But evidence is not a proof. With a larger E-value, we need a stronger unmeasured confounder to explain

![](images/828712c08e5c0f4fd5b8f04b314b14b41a4f57a8c348112ea3f0631debd94515.jpg)  
FIGURE 17.1: Magnitude of confounding to explain away the observed risk ratio based on the data from Hammond and Horn (1958)

away the observed risk ratio; the evidence for causation is stronger. With a smaller E-value, we need a weaker unmeasured confounder to explain away the observed risk ratio; the evidence for causation is weaker. Coupled with the discussion in Section 17.5.1, a larger observed risk ratio has stronger evidence for causation. This is closely related to Sir Bradford Hill's first criterion for causation: strength of the association (Bradford Hill, 1965). Theorem 17.1 provides a mathematical quantification of his heuristic argument.

In a famous paper, Bradford Hill (1965) proposed a set of nine criteria to provide evidence for causation between a presumed cause and outcome.

# Definition 17.2 Bradford Hill gave nine criteria for causation:

1. strength;   
2. consistency;   
3. specificity;   
4. temporality;

5. biological gradient;   
6. plausibility;   
7. coherence;   
8. experiment;   
9. analogy.

The E-value is a way to justify his first criterion. That is, stronger association often provides stronger evidence for causation because to explain away stronger association, we need stronger confounding measures. We have discussed randomized experiments in Part II, which corroborates his eighth criterion. Due to the space limit, I omit the detailed discussion of his other criteria and encourage the readers to read Bradford Hill (1965). Recently, this paper has been re-printed as Bradford Hill (2020) with insightful comments from many leading researchers in causal inference.

# 17.4.2 E-value after logistic regression

With a binary outcome, it is common for epidemiologists to use a logistic regression of the outcome $Y_{i}$ on the treatment indicator $Z_{i}$ and covariates $X_{i}$ :

$$
\operatorname * {p r} (Y _ {i} = 1 \mid Z _ {i}, X _ {i}) = \frac {e ^ {\beta_ {0} + \beta_ {1} Z _ {i} + \beta_ {2} ^ {\mathsf {T}} X _ {i}}}{1 + e ^ {\beta_ {0} + \beta_ {1} Z _ {i} + \beta_ {2} ^ {\mathsf {T}} X _ {i}}}.
$$

In the logistic model above, the coefficient of $Z_{i}$ is the log of the conditional odds ratio between the treatment and the outcome given the covariates:

$$
\beta_ {1} = \log \frac {\operatorname* {p r} (Y _ {i} = 1 \mid Z _ {i} = 1 , X _ {i} = x) / \operatorname* {p r} (Y _ {i} = 0 \mid Z _ {i} = 1 , X _ {i} = x)}{\operatorname* {p r} (Y _ {i} = 1 \mid Z _ {i} = 0 , X _ {i} = x) / \operatorname* {p r} (Y _ {i} = 0 \mid Z _ {i} = 0 , X _ {i} = x)}.
$$

Importantly, the logistic model assumes a common odds ratio across all values of the covariates. Moreover, when the outcome is rare in that $\operatorname{pr}(Y_i = 1 \mid Z_i = 1, X_i = x)$ and $\operatorname{pr}(Y_i = 1 \mid Z_i = 0, X_i = x)$ are close to 0, the conditional odds ratio approximates the conditional risk ratio (see Proposition 1.1(3)):

$$
\beta_ {1} \approx \log \frac {\operatorname * {p r} (Y _ {i} = 1 \mid Z _ {i} = 1 , X _ {i} = x)}{\operatorname * {p r} (Y _ {i} = 1 \mid Z _ {i} = 0 , X _ {i} = x)} = \log \mathrm {R R} _ {Z Y | x} ^ {\mathrm {o b s}}.
$$

Therefore, based on the estimated logistic regression coefficient and the corresponding confidence limits, we can calculate the E-value immediately. This is the leading application of the E-value.

Example 17.2 The NCHS2003.txt contains the National Center for Health Statistics birth certificate data, with the following binary indicator variables useful for us:

PTbirth pre-term birth  
preeclampsia pre-eclampsia  
ageabove35 an older mother with age $\geq 35$ (the treatment)  
somecollege college education  
mar marital status  
smoking smoking status  
drinking drinking status  
hispanic mother's ethnicity  
black mother's ethnicity  
nativeamerican mother's ethnicity  
asian mother's ethnicity

This version of the data is from Valeri and Vanderweele (2014). This example focuses on the outcome PTbirth and Problem 17.5 focuses on the outcome pre-eclampsia, a multisystem hypertensive disorder of pregnancy. The following R code computes the $E$ -values after fitting a logistic regression. Based on the $E$ -values, we conclude that to explain away the point estimate, the maximum confounding measure must be larger than 1.94, and to explain away the lower confidence limit, the maximum confounding measure must be larger than 1.91. Although these confounding measures are not as strong as those in Section 17.3, they appear to be fairly large in epidemiologic studies.

The simple R code below computes the numbers in Example 17.2:

```julia
> NCHS2003 = read.table("NCHS2003.txt", header = TRUE, sep = "\t")
> ## outcome: PTbirth
> y_logit = glm(PTbirth ~ ageabove35 +
+     mar + smoking + drinking + somecollege +
+     hispanic + black + nativeamerican + asian,
+     data = NCHS2003,
+     family = binomial)
> log_or = summary(y_logit)\\(coef[2, 1:2]
> est = exp(log_or[1])
> lower-ci = exp(log_or[1] - 1.96*log_or[2])
> est
Estimate
1.305982
> value(est)
Estimate
1.938127
> lower_ci
Estimate
1.294619
> value(lower_ci)
Estimate
1.912211 
```

# 17.4.3 Non-zero true causal effect

Theorem 17.1 assumes no true causal effect of the treatment on the outcome. Ding and VanderWeele (2016) proved a general theorem allowing for a nonzero true causal effect.

Theorem 17.2 Modify the definition of $\mathrm{RR}_{UY|x}$ as

$$
\operatorname {R R} _ {U Y | x} = \max  _ {z = 0, 1} \frac {\operatorname* {p r} (Y = 1 \mid Z = z , U = 1 , X = x)}{\operatorname* {p r} (Y = 1 \mid Z = z , U = 0 , X = x)}.
$$

Assume (17.1). We have

$$
\mathrm {R R} _ {Z Y | x} ^ {\mathrm {t r u e}} \geq \mathrm {R R} _ {Z Y | x} ^ {\mathrm {o b s}} \Bigg / \frac {\mathrm {R R} _ {Z U | x} \mathrm {R R} _ {U Y | x}}{\mathrm {R R} _ {Z U | x} + \mathrm {R R} _ {U Y | x} - 1}.
$$

Theorem 17.1 is a special case of Theorem 17.2 with $\mathrm{RR}_{ZY|x}^{\mathrm{true}} = 1$ . See the original paper of Ding and VanderWeele (2016) for the proof of Theorem 17.2. Without assuming any additional assumptions, Theorem 17.2 states a lower bound of the true risk ratio $\mathrm{RR}_{ZY|x}^{\mathrm{true}}$ given the observed risk ratio $\mathrm{RR}_{ZY|x}^{\mathrm{obs}}$ and the two sensitivity parameters $\mathrm{RR}_{ZU|x}$ and $\mathrm{RR}_{UY|x}$ .

When the treatment is apparently preventive to the outcome, the observed risk ratio is smaller than 1. In this case, Theorems 17.1 and 17.2 are not directly useful, and we must re-label the treatment levels and calculate the E-value based on $1 / \mathrm{RR}_{ZY|x}^{\mathrm{obs}}$ .

# 17.5 Critiques and responses

Since the original paper was published, the E-value has become a standard number reported in many epidemiologic studies. Nevertheless, it also attracted critiques (Ioannidis et al., 2019). I will review some limitations of E-values below.

# 17.5.1 E-value is just a monotone transformation of the risk ratio

From Figure 17.2, we can see that if the risk ratio is large, then the E-value $\mathrm{RR}_{ZY|x}^{\mathrm{obs}} + \sqrt{\mathrm{RR}_{ZY|x}^{\mathrm{obs}}\left(\mathrm{RR}_{ZY|x}^{\mathrm{obs}} - 1\right)}$ is nearly $2\mathrm{RR}_{ZY|x}^{\mathrm{obs}}$ which is linear in the risk ratio. For a small risk ratio, the E-value is more nonlinear in $\mathrm{RR}_{ZY|x}^{\mathrm{obs}}$ . Critics often say that the E-value is merely a monotone transformation of the point estimator or the confidence limits of the risk ratio. So it does not provide any additional information.

This is partially true. Indeed, the E-value is entirely based on the point

![](images/68d86efa621e6640fc132ca5786813249a888f86e8bfb6abd9cf12d1d093ee2e.jpg)

![](images/5a0452f2f5b0979e69d8b07295623e481bef6838349a269d24ead3fb39251401.jpg)

![](images/58dbefb50d13f4acf9040a1eb82d1f82e58e00f189e4cef5464678cac25c72a7.jpg)  
FIGURE 17.2: E-value as a monotone transformation of the risk ratio: three figures have different ranges of the risk ratio.

estimator or the confidence limits of the risk ratio. However, it has a meaningful interpretation based on Theorem 17.1: to explain away the observed risk ratio, the maximum of the confounding measures must be at least as large as the E-value.

# 17.5.2 Calibration of the E-value

The E-value equals the maximum value of the association between the confounder and the treatment and that between the confounder and the outcome to completely explain away an observed association. An obvious problem is that this confounder is fundamentally latent. So it is not trivial to decide whether a certain E-value is large or small. Another related problem is that the E-value depends on how many observed covariates $X$ we have controlled for since it quantifies the strength of the residual confounding given $X$ . Therefore, E-values across studies are not directly comparable. The E-value provides evidence for causation but this evidence should be assessed carefully based on background knowledge of the problem of interest.

The following leave-one-covariate-out approach is an intuitive approach to calibrating the E-value. With $X = (X_{1},\ldots ,X_{p})$ , we can pretend that the component $X_{j}$ were not observed and compute the $Z - X_{j}$ and $X_{j} - Y$ risk ratios given other observed covariates $(j = 1,\dots ,p)$ . These risk ratios provide the range for the confounding measures due to $U$ if we believe that the unmeasured $U$ is not as strong as some of the observed covariates. However, I am not aware of any formal justification for this approach.

# 17.5.3 It works the best for a binary outcome and the risk ratio

Theorem 17.1 works well for a binary outcome and the risk ratio. Ding and VanderWeele (2016) also proposed sensitivity analysis methods for other

causal parameters, including the risk difference for binary outcomes, the mean ratio for non-negative outcomes, and the hazard ratio for survival outcomes. However, they are not as elegant as the E-value for binary outcomes based on the risk ratio. The next chapter will propose a simple sensitivity analysis method for the average causal effect that can include the outcome regression, IPW, and doubly robust estimators in Part III as special cases.

# 17.6 Homework Problems

# 17.1 A technical lemma for the proof of Theorem 17.1

Show that

$$
f (x) = \frac {a x + 1}{b x + 1}
$$

is increasing in $x$ if $a > b$ and decreasing in $x$ is $a < b$ .

# 17.2 Technical assumption for Theorem 17.1

Revisit the proof of Theorem 17.1. Assume $Z \perp Y \mid (X, U)$ . Show that if $\mathbb{R}_{ZU|x} > 1$ but $\mathbb{R}_{UY|x} < 1$ , then $\mathbb{R}_{ZY|x}^{\mathrm{obs}} < 1$ .

Remark: This result is intuitive. Condition on $X$ . It says that if the $Z - U$ relationship is positive and the $U - Y$ relationship is negative, then the $Z - Y$ relationship is negative given the conditional independence of $Z$ and $Y$ given $U$ . Based on this result, if we assume $\mathbb{R}\mathbb{R}_{ZY|x}^{\mathrm{obs}} > 1$ and $\mathbb{R}\mathbb{R}_{ZU|x} > 1$ , then $\mathbb{R}\mathbb{R}_{UY|x} > 1$ must be true. Therefore, the third condition in (17.1) is in fact redundant.

# 17.3 Lemma 17.1

Prove Lemma 17.1.

# 17.4 Schlesselman (1978)'s formula

For simplicity, we condition on $X$ implicitly in this problem. Consider a binary treatment $Z$ , outcome $Y$ , and unmeasured confounder $U$ . Assume a common risk ratio of the treatment on the outcome within both $U = 0$ and $U = 1$ :

$$
\mathrm {R R} _ {Z Y | U = 0} = \mathrm {R R} _ {Z Y | U = 1},
$$

and also a common risk ratio of the confounder on the outcome within both $Z = 0$ and $Z = 1$ :

$$
\mathrm {R R} _ {U Y | Z = 0} = \mathrm {R R} _ {U Y | Z = 1}, \text {d e n o t e d b y} \gamma .
$$

Show that

$$
\frac {\mathrm {R R} _ {Z Y} ^ {\mathrm {o b s}}}{\mathrm {R R} _ {Z Y} ^ {\mathrm {t r u e}}} = \frac {1 + (\gamma - 1) \mathrm {p r} (U = 1 \mid Z = 1)}{1 + (\gamma - 1) \mathrm {p r} (U = 1 \mid Z = 0)}.
$$

Remark: First verify that if $\mathrm{RR}_{ZY|U = 0} = \mathrm{RR}_{ZY|U = 1}$ then

$$
\mathrm {R R} _ {Z Y} ^ {\text {t r u e}} = \mathrm {R R} _ {Z Y | U = 0} = \mathrm {R R} _ {Z Y | U = 1}.
$$

This identity shows the collapsibility of the risk ratio. In epidemiology, the risk ratio is a collapsible measure of association.

Schlesselman (1978)'s formula does not assume conditional independence $Z \bot Y \mid U$ , but assumes homogeneity of the $Z-Y$ and $U-Y$ risk ratios. It is a classic formula for sensitivity analysis. It is an identity that is simple to implement with pre-specified

$$
\{\gamma , \operatorname {p r} (U = 1 \mid Z = 1), \operatorname {p r} (U = 1 \mid Z = 0) \}.
$$

However, it involves more sensitivity parameters than Theorem 17.1. Even though Theorem 17.1 only gives an inequality, it is not a loose inequality compared to Schlesselman (1978)'s formula under stronger assumptions. With Theorem 17.1, Schlesselman (1978)'s formula is only of historical interest.

# 17.5 $E$ -value after logistic regression: data analysis

This problem uses the same dataset as Example 17.2.

Report the E-value for the outcome preeclampsia.

# 17.6 Cornfield-type inequalities for the risk difference

Consider binary $Z, Y, U$ , and condition on $X$ implicitly. Assume latent ignorability given $U$ . Show that under $Z \bot Y \mid U$ , we have

$$
\mathrm {R D} _ {Z Y} ^ {\mathrm {o b s}} = \mathrm {R D} _ {Z U} \times \mathrm {R D} _ {U Y} \tag {17.3}
$$

where $\mathrm{RD}_{ZY}^{\mathrm{obs}}$ is the observed risk difference of $Z$ on $Y$ , and $\mathrm{RD}_{ZU}$ and $\mathrm{RD}_{UY}$ are the treatment-confounder and confounder-outcome risk differences, respectively (recall the definition of the risk difference in Chapter 1.2.2).

Remark: Without loss of generality, assume that $\mathrm{RD}_{ZY}^{\mathrm{obs}},\mathrm{RD}_{ZU},\mathrm{RD}_{UY}$ are all positive. Then (17.3) implies that

$$
\min \bigl (\mathrm {R D} _ {Z U}, \mathrm {R D} _ {U Y} \bigr) \geq \mathrm {R D} _ {Z Y} ^ {\mathrm {o b s}}
$$

and

$$
\max  \left(\mathrm {R D} _ {Z U}, \mathrm {R D} _ {U Y}\right) \geq \sqrt {\mathrm {R D} _ {Z Y} ^ {\mathrm {o b s}}}.
$$

These are the Cornfield inequalities for the risk difference with a binary confounder. They show that for an unmeasured confounder to explain away an observed risk difference $\mathrm{RD}_{ZY}^{\mathrm{obs}}$ , the treatment-confounder and confounder-outcome risk differences must both be larger than $\mathrm{RD}_{ZY}^{\mathrm{obs}}$ , and the maximum of them must be larger than the square root of $\mathrm{RD}_{ZY}^{\mathrm{obs}}$ .

Cornfield et al. (1959) obtained, but did not appreciate the significance of (17.3). Gastwirth et al. (1998) and Poole (2010) discussed the first Cornfield

condition for the risk difference, and Ding and VanderWeele (2014) discussed the second.

Ding and VanderWeele (2014) also derived more general results without assuming a binary $U$ . Unfortunately, the results for a general $U$ are weaker than those above for a binary $U$ , that is, the inequalities become looser with more levels of $U$ . This motivated Ding and VanderWeele (2016) to focus on the Cornfield inequalities for the risk ratio, which do not deteriorate with more levels of $U$ .

# 17.7 Recommended reading

Ding and VanderWeele (2016) extended and unified the Cornfield-type sensitivity analysis, which is the theoretical basis for the notion of E-value.

# Sensitivity Analysis for the Average Causal Effect with Unmeasured Confounding

Cornfield-type sensitivity analysis works best for binary outcomes on the risk ratio scale, conditional on the observed covariates. Although Ding and VanderWeele (2016) also proposed Cornfield-type sensitivity analysis methods for the average causal effect, they are not general enough and are not convenient to apply. Below I give a more direct approach to sensitivity analysis based on the conditional expectations of the potential outcomes. The advantage of this approach is that it can deal with commonly used estimators for the average causal effect under the sensitivity analysis framework. The idea appeared in the early work of Robins (1999) and Scharfstein et al. (1999). This chapter is based on Lu and Ding (2023)'s recent formulation.

The approach is closely related to the idea of deriving worse-case bounds on the average potential outcomes. I will first review the simpler idea of bounds, and then extend the approach to sensitivity analysis.

# 18.1 Introduction

Recall the canonical setup of an observational study with $\{Z_i, X_i, Y_i(1), Y_i(0)\}_{i=1}^{n} \stackrel{\mathrm{~IID}}{\sim}\{Z, X, Y(1), Y(0)\}$ and focus on the average causal effect

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

TABLE 18.1: Science Table with bounded outcome $[\underline{y},\overline{y} ]$ , where $\underline{y}$ and $\overline{y}$ are two constants   

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

The second strategy in the next section assumes nothing except that the outcomes are bounded between $\underline{y}$ and $\overline{y}$ . This is natural for binary outcomes with $\underline{y} = 0$ and $\overline{y} = 1$ . With this assumption, the two counterfactual means are also bounded between $\underline{y}$ and $\overline{y}$ , which implies the worst-case bounds on $\tau$ . Table 18.1 illustrates the basic idea and Chapter 18.2 below reviews this strategy in more detail.

# 18.2 Manski-type worse-case bounds on the average causal effect without assumptions

Assume that the outcome is bounded between $\underline{y}$ and $\overline{y}$ . From the decomposition

$$
E \{Y (1) \} = E \{Y (1) \mid Z = 1 \} \Pr (Z = 1) + E \{Y (1) \mid Z = 0 \} \Pr (Z = 0),
$$

we can derive that $E\{Y(1)\}$ has lower bound

$$
E \{Y \mid Z = 1 \} \operatorname {p r} (Z = 1) + \underline {{y}} \operatorname {p r} (Z = 0)
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

we can derive that $E\{Y(0)\}$ has lower bound

$$
\underline {{y}} \operatorname {p r} (Z = 1) + E \{Y \mid Z = 0 \} \operatorname {p r} (Z = 0)
$$

and upper bound

$$
\overline {{y}} \mathrm {p r} (Z = 1) + E \{Y \mid Z = 0 \} \mathrm {p r} (Z = 0).
$$

Combining these bounds, we can derive that the average causal effect $\tau = E\{Y(1)\} - E\{Y(0)\}$ has the lower bound

$$
E \{Y \mid Z = 1 \} \mathrm {p r} (Z = 1) + \underline {{y}} \mathrm {p r} (Z = 0) - \bar {y} \mathrm {p r} (Z = 1) - E \{Y \mid Z = 0 \} \mathrm {p r} (Z = 0)
$$

and the upper bound

$$
E \{Y \mid Z = 1 \} \operatorname {p r} (Z = 1) + \bar {y} \operatorname {p r} (Z = 0) - \underline {{y}} \operatorname {p r} (Z = 1) - E \{Y \mid Z = 0 \} \operatorname {p r} (Z = 0).
$$

The length of the bounds is $\overline{y} - \underline{y}$ . The bounds are not informative but are better than the a priori bounds $[\underline{y} - \overline{y}, \overline{y} - \underline{y}]$ with length $2(\overline{y} - \underline{y})$ . Without further assumptions, the observed data distribution does not uniquely determine $\tau$ . In this case, we say that $\tau$ is partially identified, with the formal definition below.

Definition 18.1 (partial identification) A parameter $\theta$ is partially identified if the observed data distribution is compatible with multiple values of $\theta$ .

Compare Definitions 10.1 and 18.1. If the parameter $\theta$ is uniquely determined by the observed data distribution, then it is identifiable; otherwise, it is only partially identifiable. Therefore, $\tau$ is identifiable with the ignorability assumption, but only partially identifiable without the ignorability assumption.

Cochran (1953) used the idea of worse-case bounds in surveys with missing data but abandoned the idea because it often gives very conservative results. Similarly, the above worst-case bounds on $\tau$ are often uninteresting from a practical perspective because they often cover 0. Moreover, this strategy does not apply to the settings with unbounded outcomes.

Manski applied the idea to causal inference (Manski, 1990) and many other econometric models (Manski, 2003). This idea of bounding causal parameters with minimal assumptions is powerful when coupled with other qualitative

assumptions. Manski (2003) surveyed many strategies. For instance, we may believe that the treatment does not harm any units, so the monotonicity assumption holds: $Y(1) \geq Y(0)$ . Then the lower bound on $\tau$ is zero but the upper bound is unchanged. Another type of assumption is $Z = I\{Y(1) \geq Y(0)\}$ , that is, the treatment selection is based on the difference between the latent potential outcomes. This assumption can also improve the bounds on $\tau$ . A more detailed discussion of this approach is beyond the scope of this book.

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

which are the sensitivity parameters. For simplicity, we can further assume that they are constant independent of $X$ . In practice, we need to fix them or vary them in a pre-specified range. Recall that $\mu_1(X) = E(Y \mid Z = 1, X)$ and $\mu_0(X) = E(Y \mid Z = 0, X)$ are the conditional mean functions of the observed outcomes under treatment and control, respectively. We can identify the two counterfactual means and the average causal effect as follows.

Theorem 18.1 With known $\varepsilon_1(X)$ and $\varepsilon_0(X)$ , we have

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

The terminology "predictive" and "projective" is from the survey sampling literature (Firth and Bennett, 1998; Ding and Li, 2018); see also Chapter 6.2.2.2. The estimators $\hat{\tau}^{\mathrm{pred}}$ and $\hat{\tau}^{\mathrm{proj}}$ differ slightly: the former uses the observed outcomes when available, whereas the latter replaces the observed outcomes with the fitted values.

More interesting, we can also identify $\tau$ by an inverse probability weighting formula.

Theorem 18.2 With known $\varepsilon_1(X)$ and $\varepsilon_0(X)$ , we have

$$
E \{Y (1) \} = E \left\{w _ {1} (X) \frac {Z}{e (X)} Y \right\}, \quad E \{Y (0) \} = E \left\{w _ {0} (X) \frac {1 - Z}{1 - e (X)} Y \right\},
$$

where

$$
w _ {1} (X) = e (X) + \{1 - e (X) \} / \varepsilon_ {1} (X), \quad w _ {0} (X) = e (X) \varepsilon_ {0} (X) + 1 - e (X).
$$

I leave the proof of Theorem 18.2 to Problem 18.2. Theorem 18.2 modifies the classic IPW formulas with two extra factors $w_{1}(X)$ and $w_{0}(X)$ , which depend on both the propensity score and the sensitivity parameters. With the fitted propensity scores, Theorem 18.2 motivates the following estimators for $\tau$ :

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

That is, with known $\varepsilon_1(X_i)$ and $\varepsilon_0(X_i)$ , the estimator $\hat{\tau}^{\mathrm{dr}}$ is consistent for $\tau$ if either the propensity score model or the outcome model is correctly specified. We can use the bootstrap to approximate the variance of the above estimators. See Lu and Ding (2023) for technical details.

When $\varepsilon_1(X_i) = \varepsilon_0(X_i) = 1$ , the above estimators reduce to the predictive estimator, IPW estimator, and the doubly robust estimators introduced in Part III.

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

Table 18.2 presents the point estimates. The signs of the estimates are not sensitive to sensitivity parameters larger than 1, but they are quite sensitive to sensitivity parameters smaller than 1. When the participants of the meal plan tend to have higher BMI (that is, $\varepsilon_1(X) > 1$ and $\varepsilon_0(X) > 1$ ), the average causal effect of the meal plan on BMI is negative. However, this conclusion can be quite sensitive if the participants of the meal plan tend to have lower BMI.

TABLE 18.2: Sensitivity analysis for the average causal effect   

<table><tr><td></td><td>1/2</td><td>1/1.7</td><td>1/1.5</td><td>1/1.3</td><td>1</td><td>1.3</td><td>1.5</td><td>1.7</td><td>2</td></tr><tr><td>1/2</td><td>11.62</td><td>10.44</td><td>9.40</td><td>8.03</td><td>4.96</td><td>0.97</td><td>-1.69</td><td>-4.35</td><td>-8.34</td></tr><tr><td>1/1.7</td><td>9.22</td><td>8.05</td><td>7.00</td><td>5.64</td><td>2.57</td><td>-1.42</td><td>-4.08</td><td>-6.75</td><td>-10.74</td></tr><tr><td>1/1.5</td><td>7.63</td><td>6.45</td><td>5.41</td><td>4.05</td><td>0.97</td><td>-3.02</td><td>-5.68</td><td>-8.34</td><td>-12.33</td></tr><tr><td>1/1.3</td><td>6.03</td><td>4.86</td><td>3.81</td><td>2.45</td><td>-0.62</td><td>-4.61</td><td>-7.27</td><td>-9.94</td><td>-13.93</td></tr><tr><td>1</td><td>3.64</td><td>2.47</td><td>1.42</td><td>0.06</td><td>-3.01</td><td>-7.01</td><td>-9.67</td><td>-12.33</td><td>-16.32</td></tr><tr><td>1.3</td><td>1.80</td><td>0.63</td><td>-0.42</td><td>-1.78</td><td>-4.85</td><td>-8.85</td><td>-11.51</td><td>-14.17</td><td>-18.16</td></tr><tr><td>1.5</td><td>0.98</td><td>-0.19</td><td>-1.24</td><td>-2.60</td><td>-5.67</td><td>-9.66</td><td>-12.33</td><td>-14.99</td><td>-18.98</td></tr><tr><td>1.7</td><td>0.36</td><td>-0.82</td><td>-1.86</td><td>-3.23</td><td>-6.30</td><td>-10.29</td><td>-12.95</td><td>-15.61</td><td>-19.60</td></tr><tr><td>2</td><td>-0.35</td><td>-1.52</td><td>-2.57</td><td>-3.93</td><td>-7.00</td><td>-10.99</td><td>-13.65</td><td>-16.32</td><td>-20.31</td></tr></table>

# 18.4 Homework Problems

18.1 Proof of Theorem 18.1

Prove Theorem 18.1.

18.2 Proof of Theorem 18.2

Prove Theorem 18.2.

18.3 Standard errors in sensitivity analysis

Chapter 18.3.2 only presents the point estimates. Report the corresponding bootstrap standard errors.

18.4 Sensitivity analysis for the average causal effect on the treated units $\tau_{\mathrm{T}}$

This problem extends Chapter 13 to allow for unmeasured confounding for estimating

$$
\tau_ {\mathrm {T}} = E \{Y (1) - Y (0) \mid Z = 1 \} = E (Y \mid Z = 1) - E \{Y (0) \mid Z = 1 \}.
$$

We can easily estimate $E(Y \mid Z = 1)$ by the sample moment, $\hat{\mu}_{\mathrm{T1}} = \sum_{i=1}^{n} Z_i Y_i / \sum_{i=1}^{n} Z_i$ . The only counterfactual term is $E\{Y(0) \mid Z = 1\}$ . Therefore, we only need the sensitivity parameter $\varepsilon_0(X)$ . We have the following two identification formulas with a known $\varepsilon_0(X)$ .

Theorem 18.3 With known $\varepsilon_0(X)$ , we have

$$
\begin{array}{l} E \left\{Y (0) \mid Z = 1 \right\} = E \left\{Z \mu_ {0} (X) \varepsilon_ {0} (X) \right\} / e \\ = E \left\{e (X) \varepsilon_ {0} (X) \frac {1 - Z}{1 - e (X)} Y \right\} / e, \\ \end{array}
$$

where $e = \operatorname{pr}(Z = 1)$

Prove Theorem 18.3.

Remark: Theorem 18.3 motivates using $\hat{\tau}_{\mathrm{T}}^{*} = \hat{\mu}_{\mathrm{T1}} - \hat{\mu}_{\mathrm{T0}}^{*}$ to estimate $\tau_{\mathrm{T}}$ where

$$
\hat {\mu} _ {\mathrm {T 0}} ^ {\mathrm {r e g}} = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} \varepsilon_ {0} (X _ {i}) \hat {\mu} _ {0} (X _ {i}),
$$

$$
\hat {\mu} _ {\mathrm {T 0}} ^ {\mathrm {h t}} = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} \varepsilon_ {0} (X _ {i}) \hat {o} (X _ {i}) (1 - Z _ {i}) Y _ {i},
$$

$$
\hat {\mu} _ {\mathrm {T 0}} ^ {\mathrm {h a j}} = \sum_ {i = 1} ^ {n} \varepsilon_ {0} (X _ {i}) \hat {o} (X _ {i}) (1 - Z _ {i}) Y _ {i} / \sum_ {i = 1} ^ {n} \hat {o} (X _ {i}) (1 - Z _ {i}),
$$

with $\hat{o}(X_i) = \hat{e}(X_i) / \{1 - \hat{e}(X_i)\}$ being the estimated conditional odds of the treatment given the observed covariates. Moreover, we can construct the doubly robust estimator $\hat{\tau}_{\mathrm{T}}^{\mathrm{dr}} = \hat{\mu}_{\mathrm{T1}} - \hat{\mu}_{\mathrm{T0}}^{\mathrm{dr}}$ for $\tau_{\mathrm{T}}$ , where

$$
\hat {\mu} _ {\mathrm {T} 0} ^ {\mathrm {d r}} = \hat {\mu} _ {\mathrm {T} 0} ^ {\mathrm {h t}} - n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} \varepsilon_ {0} (X _ {i}) \frac {\hat {e} (X _ {i}) - Z}{1 - \hat {e} (X _ {i})} \hat {\mu} _ {0} (X _ {i}).
$$

Lu and Ding (2023) provide more details.

# 18.5 R code

Implement the estimators in Problem 18.4. Analyze the data used in Chapter 18.3.2.

# 18.6 Recommended reading

Rosenbaum and Rubin (1983a) and Imbens (2003) are two classic papers on sensitivity analysis which, however, involve more complicated procedures.

# 19

# Rosenbaum-Style $p$ -Values for Matched Observational Studies with Unmeasured Confounding

Rosenbaum (1987b) introduced a sensitivity analysis technique for matched observational studies. Although it works for general matched studies (Rosenbaum, 2002b), the theory is most elegant for one-to-one matching. Different from Chapters 17 and 18, Rosenbaum-type sensitivity analysis works best for matched observational studies for testing the sharp null hypothesis of no individual treatment effect.

# 19.1 A model for sensitivity analysis with matched data

Consider a matched observational study, with $(i,j)$ indexing unit $j$ in pair $i$ $(i = 1,\dots ,n;j = 1,2)$ . With exactly matched pairs, unit $(i,1)$ and unit $(i,2)$ have the same covariates $X_{i}$ . Assume IID sampling, and extend Definition 11.1 to define the propensity score as

$$
e _ {i j} = \operatorname * {p r} \left\{Z _ {i j} = 1 \mid X _ {i}, Y _ {i j} (1), Y _ {i j} (0) \right\}.
$$

Let $\mathbb{S}_i = \{Y_{i1}(1),Y_{i1}(0),Y_{i2}(1),Y_{i2}(0)\}$ denote the set of all potential outcomes within pair $i$ . Conditioning on the event that $Z_{i1} + Z_{i2} = 1$ , we have

$$
\begin{array}{l} \pi_ {i 1} = \Pr \left\{Z _ {i 1} = 1 \mid X _ {i}, \mathbb {S} _ {i}, Z _ {i 1} + Z _ {i 2} = 1 \right\} \\ = \frac {\operatorname* {p r} \left\{Z _ {i 1} = 1 , Z _ {i 2} = 0 \mid X _ {i} , \mathbb {S} _ {i} \right\}}{\operatorname* {p r} \left\{Z _ {i 1} + Z _ {i 2} = 1 \mid X _ {i} , \mathbb {S} _ {i} \right\}} \\ = \frac {\operatorname* {p r} \left\{Z _ {i 1} = 1 , Z _ {i 2} = 0 \mid X _ {i} , \mathbb {S} _ {i} \right\}}{\operatorname* {p r} \left\{Z _ {i 1} = 1 , Z _ {i 2} = 0 \mid X _ {i} , \mathbb {S} _ {i} \right\} + \operatorname * {p r} \left\{Z _ {i 1} = 0 , Z _ {i 2} = 1 \mid X _ {i} , \mathbb {S} _ {i} \right\}} \\ = \frac {e _ {i 1} \left(1 - e _ {i 2}\right)}{e _ {i 1} \left(1 - e _ {i 2}\right) + \left(1 - e _ {i 1}\right) e _ {i 2}} \\ \end{array}
$$

Define $o_{ij} = e_{ij} / (1 - e_{ij})$ as the odds of the treatment for unit $(i,j)$ , and we have

$$
\pi_ {i 1} = \frac {o _ {i 1}}{o _ {i 1} + o _ {i 2}}.
$$

Under ignorance, $e_{ij}$ is only a function of $X_{i}$ , and therefore, $e_{i1} = e_{i2}$ and $\pi_{i1} = 1/2$ . Thus the treatment assignment mechanism conditional on covariates and potential outcomes is equivalent to that from an MPE with equal treatment and control probabilities. This is a strategy to analyze matched observational studies we discussed in Chapter 15.1.

In general, $e_{ij}$ is also a function of the unobserved potential outcomes, and it can range from 0 to 1. Rosenbaum (1987b)'s model for sensitivity analysis imposes bounds on the odds ratio $o_{i1} / o_{i2}$ .

Assumption 19.1 (Rosenbaum's sensitivity analysis model) The odds ratios are bounded by

$$
o _ {i 1} / o _ {i 2} \leq \Gamma , \quad o _ {i 2} / o _ {i 1} \leq \Gamma , \quad (i = 1, \dots , n)
$$

for some pre-specified $\Gamma \geq 1$ . Equivalently,

$$
\frac {1}{1 + \Gamma} \leq \pi_ {i 1} \leq \frac {\Gamma}{1 + \Gamma} (i = 1, \dots , n)
$$

for some pre-specified $\Gamma \geq 1$ .

Under Assumption 19.1, we have a biased MPE with unequal and varying treatment and control probabilities across pairs. When $\Gamma = 1$ , we have $\pi_{i1} = 1/2$ and thus a standard MPE. Therefore, $\Gamma > 1$ measures the deviation from the ideal MPE due to the omitted variables in matching.

# 19.2 Worst-case $p$ -values under Rosenbaum's sensitivity analysis model

Consider testing the sharp null hypothesis

$$
H _ {0 \mathrm {F}}: Y _ {i j} (1) = Y _ {i j} (0) \text {f o r} i = 1, \dots , n \text {a n d} j = 1, 2
$$

based on the within-pair differences $\hat{\tau}_i = (2Z_{i1} - 1)(Y_{i1} - Y_{i2})$ ( $i = 1, \dots, n$ ). Under $H_{0\mathrm{F}}$ , $|\hat{\tau}_i|$ is fixed but $S_i = I(\hat{\tau}_i > 0)$ is random if $\hat{\tau}_i \neq 0$ . Consider the following class of test statistics:

$$
T = \sum_ {i = 1} ^ {n} S _ {i} q _ {i},
$$

where $q_{i} \geq 0$ is a function of $(|\hat{\tau}_1|, \dots, |\hat{\tau}_n|)$ . Special cases include the sign statistic, the pair $t$ statistic (up to some constant shift), and the Wilcoxon signed-rank statistic:

$$
T = \sum_ {i = 1} ^ {n} S _ {i}, \quad T = \sum_ {i = 1} ^ {n} S _ {i} | \hat {\tau} _ {i} |, \quad T = \sum_ {i = 1} ^ {n} S _ {i} R _ {i},
$$

where $(R_{1},\ldots ,R_{n})$ are the ranks of $(|\hat{\tau}_1|,\dots,|\hat{\tau}_n|)$

What is the null distribution of the test statistic $T$ under Assumption 19.1 with a general $\Gamma$ ? It can be quite complicated because Assumption 19.1 does not fully specify the exact values of the $\pi_{i1}$ 's. Fortunately, we do not need to know the exact distribution of $T$ but rather the worst-case distribution of $T$ that yields the largest $p$ -value under Assumption 19.1. This worst-case distribution corresponds to

$$
S _ {i} \stackrel {\text {I I D}} {\sim} \operatorname {B e r n o u l l i} \left(\frac {\Gamma}{1 + \Gamma}\right).
$$

The corresponding distribution of $T$ has mean

$$
E _ {\Gamma} (T) = \frac {\Gamma}{1 + \Gamma} \sum_ {i = 1} ^ {n} q _ {i},
$$

and variance

$$
\operatorname {v a r} _ {\Gamma} (T) = \frac {\Gamma}{(1 + \Gamma) ^ {2}} \sum_ {i = 1} ^ {n} q _ {i} ^ {2},
$$

with a Normal approximation

$$
\frac {T - \frac {\Gamma}{1 + \Gamma} \sum_ {i = 1} ^ {n} q _ {i}}{\sqrt {\frac {\Gamma}{(1 + \Gamma) ^ {2}} \sum_ {i = 1} ^ {n} q _ {i} ^ {2}}} \rightarrow \mathrm {N} (0, 1)
$$

in distribution. In practice, we can report a sequence of $p$ -values as a function of $\Gamma$ .

# 19.3 Examples

# 19.3.1 Revisiting the LaLonde data

We conduct Rosenbaum-style sensitivity analysis in the matched LaLonde data. Using the Matching package, we can construct the matched dataset.

library("Matching")
library("sensitivitymvm")
library("sensitivitymw")
dat <- read.table("cps1re74.csv", header=T)
dat\ $u74 <- as.numeric (dat\$ re74==0)
dat\ $u75 <- as.numeric (dat\$ re75==0)
y = dat\\(re78
z = dat\\)treat
x = as.matrix (dat[, c("age", "educ", "black",
"hispan", "married", "nodegree",

"re74", "re75", "u74", "u75")]  
matchest = Match(Y = y, Tr = z, X = x)  
ytreated = y[matchest\\(index.treated]  
ycontrol = y[matchest\\)index.control]  
datamatched = cbind(ytreated, ycontrol)

We consider using the test statistic $T = \sum_{i=1}^{n} S_i |\hat{\tau}_i|$ . Under the ideal MPE with $\Gamma = 1$ , we can simulate the distribution of $T$ and obtain the $p$ -value 0.002, as shown in the first subfigure in Figure 19.1. With a slightly larger $\Gamma = 1.1$ , the worst-case distribution of $T$ shifts to the right, and the $p$ -value increases to 0.011. If we further increase $\Gamma$ to 1.3, then the worst-case distribution of $T$ shifts further and the $p$ -value exceeds 0.05. Figure 19.2 shows the histogram of the $\hat{\tau}_i$ 's and the $p$ -value as a function of $\Gamma$ ; $\Gamma = 1.233$ measures the maximum confounding that we can still reject the null hypothesis at level 0.05.

We can also use the senmw function in the sensitivitymw package to obtain a sequence of $p$ -values against $\Gamma$ .

```txt
Gamma = seq(1, 1.4, 0.001)
Pvalue = Gamma
for (i in 1: length(Gamma))
{
    Pvalue[i] = senmw(matamatched, gamma = Gamma[i],
                    method = "t")$pval
} 
```

Figure 19.2 shows the plot of the $p$ -value against $\Gamma$ .

# 19.3.2 Two examples from Rosenbaum's packages

The erpcp dataset is from the R package sensitivitymw. It contains $n = 39$ matched pairs of a welder and a control, based on observed covariates age and smoking. The outcome is the DNA elution rate. Figure 19.3(a) shows the histogram of the within-pair differences of the outcomes and the $p$ -value against $\Gamma$ based on the pair $t$ -statistic. The following R code generates Figure 19.3a.

```r
par(mfrow = c(1, 2), mai = c(0.8, 0.8, 0.3, 0.3))  
data(erpcp)  
hist(erpcp[, 1] - erpcp[, 2], main = "erpcp", xlab = expression(hat(tau)[i]), freq = FALSE)  
Gamma = seq(1, 5, 0.005)  
Pvalue = Gamma  
for (i in 1:length(Gamma))  
{ Pvalue[i] = senmw(erpcp, gamma = Gamma[i], method = "t")$pval}  
gammastar = Gamma[which(Pvalue >= 0.05)[1]] 
```

![](images/9b79263dd32a878ea9dff68fcac72447faea52634819f520b19df8ce485da927.jpg)

![](images/7b15e3d6ed4d445413253fd0be7cae198b921887c750ad1239576cdc22eaffe8.jpg)

![](images/bb809039710d448da9ef841389074399b2ade17acfdb5f54facc39981c8bb884.jpg)  
FIGURE 19.1: The worst-case distributions of $T = \sum_{i=1}^{n} S_i |\hat{\tau}_i|$ with $S_i$ IID Bernoulli $(\Gamma / (1 + \Gamma))$ , based on the matched LaLonde data.

![](images/9ca150a40238c8831b0e8265f6065bf9e1d9ff3efe13ca5edc1a8e0503527162.jpg)

![](images/17b8b66b6447e5eb17be73bd988b659cf7d6c83fa08ea07766e3266f76d78462.jpg)  
FIGURE 19.2: $p$ -value as a function of $\Gamma$ , based on the matched LaLonde data.

gammastar plot(Pvalue \~ Gamma, type $=$ "xlab $=$ expression(Gamma), ylab $=$ "p-value") abline(h $= 0.05$ , lty $= 2$ ) abline(v $=$ gammastar, lty $= 2$

The lead250 dataset is from the R package sensitivitymw. It contains $n = 250$ matched pairs of a daily smoker and a control of nonsmoker, based on observed covariates gender, age, race education level, and household income from NHANES. The outcome is the blood lead level in $\mu g / l$ . Figure 19.3(b) shows the histogram of the within-pair differences of the outcomes and the $p$ -value against $\Gamma$ based on the pair $t$ -statistic. The following R code generates Figure 19.3b.

```r
par(mfrow = c(1, 2), mai = c(0.8, 0.8, 0.3, 0.3))  
data(lead250)  
hist(lead250[, 1] - lead250[, 2], main = "lead250", xlab = expression(hat(tau)[i]), freq = FALSE)  
Gamma = seq(1, 2.5, 0.001)  
Pvalue = Gamma  
for(i in 1:length(Gamma))  
{ Pvalue[i] = senmw(lead250, gamma = Gamma[i], method = "t")$pval}  
gammastar = Gamma[which(Pvalue >= 0.05)[1]]  
gammastar  
plot(Pvalue ~ Gamma, type = "l", xlab = expression(Gamma), ylab = "p-value")  
abline(h = 0.05, lty = 2)  
abline(v = gammastar, lty = 2) 
```

# 19.4 Homework Problems

19.1 A model for Assumption 19.1

Assumption 19.1 has the following equivalent form.

Assumption 19.2 The propensity score satisfies the following model

$$
\log \frac {\pi_ {i j}}{1 - \pi_ {i j}} = g (X _ {i}) + \gamma U _ {i j}, \quad (i = 1, \dots , n; j = 1, 2)
$$

![](images/7a68ea3eae1d941d3c64816bde8cc4b9787e852b78704c8333672b8dc1a73421.jpg)

![](images/75cdda81873c987e88773b9ff9bec0c7c318db2bb701fdadf5ca3acc20b6598c.jpg)

![](images/eea6829a236ede020a09ff90762ae02af84d8f4e1eb4ac0bb20bd044a8e45937.jpg)  
(a) erpcp data

![](images/63cdb596281893311616cf841ecc66473c8ab9e3295eca7182a8af56e050c41d.jpg)  
(b)ead250 data   
FIGURE 19.3: Two examples: histogram of the $\hat{\tau}_i$ 's and $p$ -value as a function of $\Gamma$

where $g(\cdot)$ is an unknown function and $U_{ij} \in [0,1]$ is a bounded unobserved covariate for unit $(i,j)$ .

Show that if Assumption 19.2 holds, then Assumption 19.1 must hold with $\Gamma = e^{\gamma}$ .

Remark: Rosenbaum (2002b, page 108) also shows that if Assumption 19.1 holds, then Assumption 19.2 must hold for some $U_{ij}$ 's. Assumption 19.2 may be easier to interpret because $\gamma$ measures the log of the conditional odds ratio of $U$ on the treatment; see Chapter B.6 for the interpretation of the coefficients in the logistic regression.

# 19.2 Application of Rosenbaum's approach

Re-analyze Example 10.3 using Rosenbaum's approach based on matching.

# 19.3 Recommended reading

Rosenbaum (2015) provides a tutorial for his two R packages for sensitivity analysis with matched observational studies.

# 20

# Overlap in Observational Studies: Difficulties and Opportunities

# 20.1 Implications of overlap

In Part III of this book, causal inference with observational studies relies on two critical assumptions: ignorability

$$
Z \bot \{Y (1), Y (0) \} \mid X
$$

and overlap

$$
0 <   e (X) <   1.
$$

D'Amour et al. (2021) pointed out the tension between these two assumptions: typically, more covariates make the ignorability assumption more plausible (ignoring M-bias discussed in Chapter 16.3.1), but more covariates make the overlap assumption less plausible because the treatment becomes more predictable given more covariates.

If some units have $e(X) = 0$ or $e(X) = 1$ , then we have philosophic difficulty in thinking about the counterfactual potential outcomes (King and Zeng, 2006). In particular, if a unit deterministically receives the treatment, then it may not be meaningful to conceive its potential outcome under the control; if a unit deterministically receives the control, then it may not be meaningful to conceive its potential outcome under the treatment. Even if the true propensity score is not exactly 0 or 1, the estimated propensity score can be very close to 0 or 1 in finite samples, which makes the estimators based on IPW numerically unstable. I have discussed this issue in Chapter 11.

Many statistical analyses in fact require a strict version of overlap:

Assumption 20.1 (strict overlap) $\eta \leq e(X) \leq 1 - \eta$ for some $\eta \in (0,1/2)$ .

However, D'Amour et al. (2021, Corollary 1) showed that Assumption 20.1 has very strong implications when the number of covariates is large. For simplicity, I present only one of their results. Let $X_{k}$ ( $k = 1, \ldots, p$ ) be the $k$ th component of the covariate $X = (X_{1}, \ldots, X_{p})$ , and

$$
e = \operatorname {p r} (Z = 1)
$$

be the proportion of the treated units.

Theorem 20.1 Assumption 20.1 implies that $\eta \leq e \leq 1 - \eta$ and

$$
\begin{array}{l} p ^ {- 1} \sum_ {k = 1} ^ {p} \left| E \left(X _ {k} \mid Z = 1\right) - E \left(X _ {k} \mid Z = 0\right) \right| \\ \leq p ^ {- 1 / 2} C ^ {1 / 2} \left\{e \lambda_ {1} ^ {1 / 2} + (1 - e) \lambda_ {0} ^ {1 / 2} \right\}, \tag {20.1} \\ \end{array}
$$

where

$$
C = \frac {(e - \eta) (1 - e - \eta)}{e ^ {2} (1 - e) ^ {2} \eta (1 - \eta)}
$$

is a positive constant depending only on $(e,\eta)$ , and $\lambda_{1}$ and $\lambda_{0}$ are the maximum eigenvalues of the covariance matrices $\operatorname{cov}(X\mid Z = 1)$ and $\operatorname{cov}(X\mid Z = 0)$ , respectively.

What is the order of the maximum eigenvalues in Theorem 20.1? D'Amour et al. (2021) showed that it is usually smaller than $O(p)$ unless the components of $X$ are highly correlated. If the components of $X$ are highly correlated, then some components are redundant after including other components. If the components of $X$ are not highly correlated, then the right-hand side converges to zero. So the average difference in means of the covariates is close to zero, that is, the treatment and control groups are nearly balanced in means averaged over all dimensions of the covariates. Mathematically, the left-hand side of (20.1) converging to zero rules out the possibility that all dimensions of $X$ have non-vanishing differences in means across the treatment and control groups. It is a strong requirement in observational studies with many covariates.

# 20.1.1 Trimming in the presence of limited overlap

When Assumption 20.1 does not hold, it is common to trim the units based on the estimated propensity scores (Crump et al., 2009; Yang and Ding, 2018b). Trimming drops units within regions of little overlap, which changes the population and estimand. The restrictive implications of overlap in Assumption 20.1 suggest that trimming must be employed more often and one may need to trim a large proportion of units to achieve desirable overlap in high dimensions.

# 20.1.2 Outcome modeling in the presence of limited overlap

The somewhat negative results in D'Amour et al. (2021) also highlight the limitation of focusing only on the propensity score in the presence of limited overlap. This in some sense challenges Rubin (2008)'s view that "for objective causal inference, design trumps analysis." Rubin (2008) argued strongly for the role of the "design" stage in observational studies. The "design" stage focuses on the propensity score which may not satisfy the overlap condition with many covariates.

With high dimensional covariates, outcome modeling becomes more important. In particular, if the outcome means only depend on a function of the original covariates in that

$$
E \{Y (z) \mid X \} = f _ {z} (r (X)), \quad (z = 0, 1)
$$

then it suffices to control for $r(X)$ , a lower-dimensional summary of the original covariates. See Problem 20.1 for more details. Due to the dimension reduction, the strict overlap condition on $r(X)$ can be much weaker than the strict overlap condition on $X$ . This is conceptually straightforward, but the corresponding theory and methods are missing.

# 20.2 Causal inference with no overlap: regression discontinuity

Let us start from the simple case with a univariate $X$ . An extreme treatment assignment mechanism is a deterministic one:

$$
Z = I (X \geq x _ {0}),
$$

where $x_0$ is a predetermined threshold. An interesting consequence of this assignment is that the ignorability assumption holds automatically:

$$
Z \perp \perp \{Y (1), Y (0) \} \mid X
$$

because $Z$ is a deterministic function of $X$ and a constant is independent of any random variables. However, the overlap assumption is violated by definition:

$$
e (X) = \operatorname {p r} (Z = 1 \mid X) = 1 (X \geq x _ {0}) = \left\{ \begin{array}{l l} 1 & \text {i f} X \geq x _ {0}, \\ 0 & \text {i f} X <   x _ {0}. \end{array} \right.
$$

So our analytic strategies discussed in Part IV are no longer applicable here. We must change our perspective.

The discussion above seems contrived, with a deterministic treatment assignment. Interestingly, it has many applications in practice and is called regression discontinuity. Below, I first review some canonical examples and then give a mathematical formulation of this type of study.

# 20.2.1 Examples and graphical diagnostics

Example 20.1 Thistlethwaite and Campbell (1960) first proposed the idea of regression-discontinuity analysis. Their motivating example was to study the effect of students' winning the Certificate of Merit on later career plans, where

![](images/15ee23572e0b379d87cdc31483c1b2797116137e32892febe357f4d1da5beb54.jpg)  
FIGURE 20.1: A graph from Thistlethwaite and Campbell (1960) with minor modifications of the unclear text in the original paper

the Certificate of Merit was determined by whether the Scholarship Qualifying Test score was above a certain threshold. Their initial analysis was mainly graphical. Figure 20.1 shows one of their graphs.

Example 20.2 Bor et al. (2014) used regression discontinuity to study the effect of when to start HIV patients with antiretroviral on their mortality, where the treatment is determined by whether the patients' $CD4$ counts were below 200 cells/μL (note that $CD4$ cells are white blood cells that fight infection.)

Example 20.3 Carpenter and Dobkin (2009) studied the effect of alcohol consumption on mortality, which leverages the minimum legal drinking age as a discontinuity for alcohol consumption. They derived mortality data from the National Center for Health Statistics, including the decedent's date of birth and date of death. They computed the age profile of deaths per

![](images/05e4eac80723d5fd90741e51f3ac622c1b40cbd3fbb55da01bea82d3371e3da9.jpg)  
FIGURE 20.2: Minimum legal drinking age example from Carpenter and Dobkin (2009)

100,000 person-years with outcomes measured by the following nine variables:

all all deaths, the sum of internal and external   
internal deaths due to internal causes   
external deaths due to external causes, the sum of the rest   
homicide homicides   
suicide suicides   
mva motor vehicle accidents   
alcohol deaths with a mention of alcohol   
drugs deaths with a mention of drug use   
externalother deaths due to other external causes

Figure 20.2 plots the number of deaths per 100,000 person-years for nine measures based on the data used by Angrist and Pischke (2014). From the jumps at age 21, it seems obvious that there is an increase in mortality at age 21, primarily due to motor vehicle accidents. I leave the formal analysis as Problem 20.4.

# 20.2.2 A mathematical formulation of regression discontinuity

The technical term for the variable $X$ that determines the treatment is the running variable. Intuitively, regression discontinuity can identify a local average causal effect at the cutoff point $x_0$ :

$$
\tau (x _ {0}) = E \{Y (1) - Y (0) \mid X = x _ {0} \}.
$$

In particular, for the potential outcome under treatment, we have

$$
\begin{array}{l} E \left\{Y (1) \mid X = x _ {0} \right\} = \lim  _ {\varepsilon \rightarrow 0 +} E \left\{Y (1) \mid X = x _ {0} + \varepsilon \right\} (20.2) \\ = \lim  _ {\varepsilon \rightarrow 0 +} E \{Y (1) \mid Z = 1, X = x _ {0} + \varepsilon \} (20.3) \\ = \lim  _ {\varepsilon \rightarrow 0 +} E (Y \mid Z = 1, X = x _ {0} + \varepsilon), (20.4) \\ \end{array}
$$

where (20.2) holds if $E\{Y(1) \mid X = x\}$ is continuous from the right at $x_0$ and (20.3) follows by the definition of $Z$ . Similarly, for the potential outcome under control, we have

$$
E \{Y (0) \mid X = x _ {0} \} = \lim  _ {\varepsilon \rightarrow 0 +} E (Y \mid Z = 0, X = x _ {0} - \varepsilon)
$$

if $E\{Y(0) \mid X = x\}$ is continuous from the left at $x_0$ . So the local average causal effect at $x_0$ can be identified by the difference of the two limits. I summarize the key identification result below.

Theorem 20.2 Assume that the treatment is determined by $Z = I(X \geq x_0)$ where $x_0$ is a predetermined threshold. Assume that $E\{Y(1) \mid X = x\}$ is continuous from the right at $x_0$ and $E\{Y(0) \mid X = x\}$ is continuous from the left at $x_0$ . Then the local average treatment effect at $X = x_0$ is identified by

$$
\tau (x _ {0}) = \lim  _ {\varepsilon \to 0 +} E (Y \mid Z = 1, X = x _ {0} + \varepsilon) - \lim  _ {\varepsilon \to 0 +} E (Y \mid Z = 0, X = x _ {0} - \varepsilon).
$$

Since the right-hand side of the above equation only involves observables, the parameter $\tau(x_0)$ is nonparametrically identified. However, the form of the identification formula is totally different from what we derived before. In particular, the identification formula involves limits of two conditional expectation functions.

# 20.2.3 Regressions near the boundary

If we are lucky, graphical diagnostics sometimes can clearly show the causal effect at the cutoff point. However, many outcomes are noisy so graphical diagnostics are not enough in finite samples. Figure 20.3 shows two simulated examples with obvious jumps at the cutoff point and two examples without obvious jumps, although the underlying data-generating processes all have discontinuities.

Assume that $E(Y \mid Z = 1, X = x) = \gamma_1 + \beta_1x$ and $E(Y \mid Z = 0, X = x) = \gamma_0 + \beta_0x$ are linear in $x$ . We can run OLS based on the treated and control data to obtain the fitted lines $\hat{\gamma}_1 + \hat{\beta}_1x$ and $\hat{\gamma}_0 + \hat{\beta}_0x$ , respectively. We can then estimate the average causal effect at the point $X = x_0$ as

$$
\hat {\tau} (x _ {0}) = (\hat {\gamma} _ {1} - \hat {\gamma} _ {0}) + (\hat {\beta} _ {1} - \hat {\beta} _ {0}) x _ {0}.
$$

Numerically, $\hat{\tau} (x_0)$ is identical to the coefficient of $Z_{i}$ in the OLS

$$
Y _ {i} \sim \left\{1, Z _ {i}, X _ {i} - x _ {0}, Z _ {i} \left(X _ {i} - x _ {0}\right) \right\}, \tag {20.5}
$$

![](images/770ffbf4b411774e0e7dd19fc359ba719a36221bdebcd33a422b3044cef1887b.jpg)

![](images/58153bfbed52775a163a88f66bb4373e1dd76b32db13494365bff49c0216af15.jpg)

![](images/7029786fb3057e1a9c47724cd85855a65fc88d66dd30ed5bb86e1baa22974acd.jpg)

![](images/880caeb8396fd0faa0da4acb8e510a71ac97b9a4ab01635801ea74416e690695.jpg)  
FIGURE 20.3: Examples of regression discontinuity. The black points are the observed outcomes whereas the grey points are the unobserved counterfactual outcomes. In the first column, the data-generating processes result in visible jumps at the cutoff points; in the second column, the jumps are not so visible. In the first row, the data generating processes have constant $\tau(x)$ ; in the second row, $\tau(x)$ varies with $x$ .

and it is also identical to the coefficient of $Z_{i}$ in the OLS

$$
Y _ {i} \sim \{1, Z _ {i}, R _ {i}, L _ {i} \}, \tag {20.6}
$$

where

$$
R _ {i} = \max  (X _ {i} - x _ {0}, 0), \quad L _ {i} = \min  (X _ {i} - x _ {0}, 0)
$$

indicate the right and left parts of $X_{i} - x_{0}$ , respectively. I leave the algebraic details to Problem 20.2.

However, this approach may be sensitive to the violation of the linear model assumption. Theory suggests running regression using only the local observations near the cutoff point<sup>1</sup>. However, the rules for choosing the "local points" are quite involved. Fortunately, the rdrobust function in the rdrobust package in R implements various choices of "local points." Since choosing the "local points" is the key to regression discontinuity, it seems more sensible to report estimates and confidence intervals based on various choices of the "local points." This can be viewed as a sensitivity analysis for regression discontinuity.

# 20.2.4 An example

Lee (2008) gave a famous example of using regression discontinuity to study the incumbency advantage in the U.S. House. He wrote that "incumbents are, by definition, those politicians who were successful in the previous election. If what makes them successful is somewhat persistent over time, they should be expected to be somewhat more successful when running for re-election." Therefore, this is a fundamentally challenging causal inference problem. The regression discontinuity is a clever study design to study this problem.

The running variable is the lagged vote in the previous election centered at 0, and the outcome is the vote in the current election, with units being the congressional districts. The treatment is the binary indicator for being the current incumbent party in a district, determined by the lagged vote. The following R code generates Figure 20.4 that shows the raw data.

house $=$ read.csv("house.csv")[, -1] plot(y \~ x, data $=$ house，pch $= 19$ ，cex $= 0.1$ ) abline(v $= 0$ ，col $=$ "grey")

The rdrobust function gives three sets of the point estimate and confidence intervals. They all suggest a positive incumbency advantage.

```prolog
> library(rdobust)
> RDDest = rdobust(house\(y, house\)x)
Warning message:
In rdobust(house\)y, house\)x):
Mass points detected in the running variable. 
```

![](images/e787f3685a0d8623480b36367d459a79d7ffc30d12ad80ff46232c29840f19d7.jpg)  
FIGURE 20.4: Raw data of Lee (2008)

```txt
>cbind(RDDest$coef, RDDest$ci) Coeff CI Lower CI Upper Conventional 0.06372533 0.04224798 0.08520269 Bias-Corrected 0.05937028 0.03789292 0.08084763 Robust 0.05937028 0.03481238 0.08392818 
```

We can also obtain the point estimates and the confidence intervals based on OLS with different choices of the local points defined by $|X| < h$ based on the following R code.

house\ $z = (house\$ x >= 0)
hh = seq(0.05, 1, 0.01)
local.lm = sapply(hh, function(h){
    Greg = lm(y ~ z + x + z*x, data = house,
                    subset = (abs(x) <= h))
    cbind(coef(Greg)[2], confint(Greg, 'zTRUE'))
})
plot(local.lm[1, ] ~ hh, type = "p",
                pch = 19, cex = 0.3,
               ylim = range(local.lm),
                xlab = "h",
                ylab = "point and interval estimates",
                main = "subset linear regression: |X|<h")
    lines(local.lm[2, ] ~ hh, type = "p",
                pch = 19, cex = 0.1)
    lines(local.lm[3, ] ~ hh, type = "p",
                pch = 19, cex = 0.1)

Figure 20.5 shows the point estimates and the confidence intervals as a function of $h$ . While the point estimates and the confidence intervals are sensitive to the choice of $h$ , the qualitative result remains the same as above.

![](images/9c7740832c3b17aa30146032a9b3c83d725bd66d4cc6fa8bf91af19e65d6e964.jpg)  
FIGURE 20.5: Estimates and confidence intervals based on local linear regressions

# 20.2.5 Problems of regression discontinuity

What can go wrong with the regression discontinuity analysis? The technical challenge is to specify the neighborhood near the cutoff point. We have discussed this issue above.

In addition, Theorem 20.2 holds under a continuity condition. It may be violated in practice. For instance, if the mortality rate jumps at the age of 21, then we may not be able to attribute the jumps in Figure 20.2 to the change in drinking behavior due to the legal drinking age. However, it is hard to check the violation of the continuity condition empirically.

McCrary (2008) proposed an indirect test for the validity of the regression discontinuity. He suggested checking the density of the running variable at the cutoff point. The discontinuity in the density of the running variable at the cutoff point may suggest that some units were able to manipulate their treatment status perfectly. The Ddensity function in the R package rdd implements this test. I omit the details.

# 20.3 Homework Problems

20.1 A theorem for the role of outcome modeling in the presence of limited overlap

This problem extends the discussion in Section 20.1.2. I state a formal theorem below.

Theorem 20.3 Assume

$$
Z \bot Y (z) \mid X, \quad (z = 0, 1)
$$

and

$$
E \left\{Y (z) \mid X \right\} = f _ {z} (r (X)), \quad (z = 0, 1)
$$

for some function $r(X)$ . The average causal effect $\tau = E\{Y(1) - Y(0)\}$ can be identified by

$$
\tau = E \left\{E (Y \mid Z = 1, r (X)) - E (Y \mid Z = 0, r (X)) \right\}
$$

or

$$
\tau = E \left\{\frac {Z Y}{e (r (X))} \right\} - E \left\{\frac {(1 - Z) Y}{1 - e (r (X))} \right\}
$$

where $e(r(X)) = \operatorname{pr}\{Z = 1 \mid r(X)\}$ .

Prove Theorem 20.3.

Remark: When $r(X) = X$ , Theorem 20.3 reduces to the standard IPW formula for the average causal effect. When $r(X)$ has a lower dimension than $X$ , Theorem 20.3 has broader applicability if the overlap condition on $e(X)$ fails whereas the overlap condition on $e(r(X))$ may still hold.

# 20.2 Linear potential outcome models

This problem gives more details for the numerical equivalence in Section 20.2.3.

Show that $\hat{\tau}(x_0)$ equals the coefficients of $Z_i$ in OLS fits (20.5) and (20.5).

Remark: It is helpful to start with the figures of $Z_{i}(X_{i} - x_{0})$ , $L_{i}$ , and $R_{i}$ with $X_{i}$ on the $x$ -axis. The conclusion holds by a reparametrization of the OLS regressions.

# 20.3 Simulation for regression discontinuity

In Figure 20.3, the potential outcomes are simulated from linear models. Change them to nonlinear models, and compare different point estimators and confidence intervals, including the biases and variances of the point estimators, and the coverage properties of confidence intervals.

# 20.4 Re-analysis of the data on the minimum legal drinking age

Figure 20.2 shows the jumps at the cutoff point. Analyze the data mlda.csv of Carpenter and Dobkin (2009).

# 20.5 Re-analysis of Lee (2008)'s data

Figure 20.5 plots the confidence intervals based on the standard errors assuming homoskedasticity. Generate a figure with confidence intervals based on the EHW standard errors in OLS.

# 20.6 Recommended reading

D'Amour et al. (2021) discussed the implications of overlap with high dimensional covariates.

Thistlethwaite and Campbell (1960)'s original paper on regression discontinuity was re-printed as Thistlewaite and Campbell (2016) with many insightful comments. Coincidentally, Thistlethwaite and Campbell (1960) and Rubin (1974) were both published in the Journal of Educational Psychology.

# Part V

# Instrumental variables

# 21

# An Experimental Perspective of the Instrumental Variable

The instrumental variable method has been a powerful tool in econometrics. It identifies causal effects in studies without unconfoundedness between the treatment and the outcome. It relies on an additional variable, called the instrumental variable (IV), that satisfies certain conditions. These conditions may not be easy to digest when you learn them for the first time. In some sense, the IV method is like magic. This chapter presents a not-so-magic perspective based on the encouragement design. This again echos Dorn (1953)'s suggestion that the planner of an observational study should always ask himself the following question:

How would the study be conducted if it were possible to do it by controlled experimentation?

The experimental analog of the IV method is noncompliance in the encouragement design (Zelen, 1979; Powers and Swinton, 1984; Holland, 1986).

# 21.1 Encouragement Design and Noncompliance

Consider an experiment with units indexed by $i = 1, \dots, n$ . Let $Z_{i}$ be the treatment assigned, with 1 for the treatment and 0 for the control. Let $D_{i}$ be the treatment received, with 1 for the treatment and 0 for the control. When $Z_{i} \neq D_{i}$ for some unit $i$ , the noncompliance problem arises. Noncompliance is a very common problem, especially in encouragement designs involving human beings as experimental units. In those cases, the experimenters cannot force the units to take the treatment but rather only encourage them to do so. Let $Y_{i}$ be the outcome of interest.

Consider complete randomization of $Z$ and ignore covariates $X$ for now. We have the potential values for the treatment received $\{D_i(1), D_i(0)\}$ and the potential values for the outcome $\{Y_i(1), Y_i(0)\}$ , all with respect to the treatment assignment levels 1 and 0. Their observed values are $D_i = Z_i D_i(1) + (1 - Z_i) D_i(0)$ and $Y_i = Z_i Y_i(1) + (1 - Z_i) Y_i(0)$ , respectively.

For notational simplicity, we assume $\{Z_i, D_i(1), D_i(0), Y_i(1), Y_i(0)\}_{i=1}^n \stackrel{\mathrm{IID}}{\sim}\{Z, D(1), D(0), Y(1), Y(0)\}$ and sometimes drop the subscript $i$ when it should not cause confusions.

We start with the CRE.

Assumption 21.1 (randomization) $Z \perp \perp \{D(1), D(0), Y(1), Y(0)\}$ .

Randomization allows for the identification of the average causal effects on $D$ and $Y$ :

$$
\tau_ {D} = E \{D (1) - D (0) \} = E (D \mid Z = 1) - E (D \mid Z = 0)
$$

and

$$
\tau_ {Y} = E \{Y (1) - Y (0) \} = E (Y \mid Z = 1) - E (Y \mid Z = 0).
$$

We can use simple difference-in-means estimators $\hat{\tau}_D$ and $\hat{\tau}_Y$ to estimate $\tau_{D}$ and $\tau_{Y}$ , respectively.

Reporting the estimate $\hat{\tau}_{Y}$ with the associated standard error is called the intention-to-treat (ITT) analysis. It estimates the effect of the treatment assignment on the outcome, and the CRE in Assumption 21.1 justifies this analysis. However, it may not answer the scientific question, that is, the causal effect of the treatment received on the outcome.

# 21.2 Latent Compliance Status and Effects

# 21.2.1 Nonparametric identification

Following Imbens and Angrist (1994) and Angrist et al. (1996), we stratify the population based on the joint potential values of $U_{i} = \{D_{i}(1), D_{i}(0)\}$ . Because $D$ is binary, we have four possible combinations:

$$
U _ {i} = \left\{ \begin{array}{l l} \text {a ,} & \text {i f} D _ {i} (1) = 1 \text {a n d} D _ {i} (0) = 1; \\ \text {c ,} & \text {i f} D _ {i} (1) = 1 \text {a n d} D _ {i} (0) = 0; \\ \text {d ,} & \text {i f} D _ {i} (1) = 0 \text {a n d} D _ {i} (0) = 1; \\ \text {n ,} & \text {i f} D _ {i} (1) = 0 \text {a n d} D _ {i} (0) = 0, \end{array} \right.
$$

where “a” is for “always taker,” “c” is for “complier,” “d” is for “defier,” and “n” is for “never taker.” Because we cannot observe $D_{i}(1)$ and $D_{i}(0)$ simultaneously, $U_{i}$ is a latent variable for the compliance behavior of unit $i$ .

Based on $U$ , we can use the law of total probability to decompose the average causal effect on $Y$ into four terms:

$$
\begin{array}{l} \tau_ {Y} = E \{Y (1) - Y (0) \mid U = a \} \Pr (U = a) \\ + E \{Y (1) - Y (0) \mid U = \mathrm {c} \} \Pr (U = \mathrm {c}) \\ + E \left\{Y (1) - Y (0) \mid U = \mathrm {d} \right\} \Pr (U = \mathrm {d}) \\ + E \left\{Y (1) - Y (0) \mid U = \mathrm {n} \right\} \Pr (U = \mathrm {n}). \tag {21.1} \\ \end{array}
$$

Therefore, $\tau_{Y}$ is a weighted average of four latent subgroup effects. We will look into more details of the latent groups below.

Assumption 21.2 below restricts the third term in (21.1) to be zero.

Assumption 21.2 (monotonicity) $\operatorname{pr}(U_i = \mathrm{d}) = 0$ or $D_{i}(1)\geq D_{i}(0)$ for all $i$ , that is, there are no defiers.

Assumption 21.2 holds automatically with one-sided noncompliance when the units assigned to the control arm have no access to the treatment, i.e., $D_{i}(0) = 0$ for all units. Under randomization, Assumption 21.2 has a testable implication that

$$
\Pr (D = 1 \mid Z = 1) \geq \Pr (D = 1 \mid Z = 0). \tag {21.2}
$$

But Assumption 21.2 is much stronger than the inequality (21.2). The former restricts $D_{i}(1)$ and $D_{i}(0)$ at the individual level whereas the latter restricts them only on average. Nevertheless, when the testable implication (21.2) holds, we cannot use the observed data to refute Assumption 21.2.

Assumption 21.3 below restricts the first and last terms in (21.1) to be zero based on the mechanism of the treatment assignment on the outcome through only the treatment received.

Assumption 21.3 (exclusion restriction) $Y_{i}(1) = Y_{i}(0)$ for always takers with $U_{i} = \mathrm{a}$ and never takers with $U_{i} = \mathrm{n}$ .

As equivalent statement of Assumption 21.3 is that $D_{i}(1) = D_{i}(0)$ must imply $Y_{i}(1) = Y_{i}(0)$ for all $i$ . It requires that the treatment assignment affects the outcome only if it affects the treatment received. In double-blind RCTs², it is biologically plausible because the outcome only depends on the actual treatment received. That is, if the treatment assignment does not change the treatment received, it does not change the outcome either. It can be violated if the treatment assignment has direct effects³ on the outcome, not through the treatment received. For example, some RCTs are not double-blinded, and the treatment assignment can have some unknown pathways to the outcome.

Under Assumptions 21.2 and 21.3, the decomposition (21.1) only has the second term:

$$
\tau_ {Y} = E \left\{Y (1) - Y (0) \mid U = c \right\} \Pr (U = c). \tag {21.3}
$$

Similarly, we can decompose the average causal effect on $D$ into four terms:

$$
\begin{array}{l} \tau_ {D} = E \{D (1) - D (0) \mid U = \mathrm {a} \} \Pr (U = \mathrm {a}) \\ + E \{D (1) - D (0) \mid U = c \} \Pr (U = c) \\ + E \{D (1) - D (0) \mid U = \mathrm {d} \} \Pr (U = \mathrm {d}) \\ + E \{D (1) - D (0) \mid U = \mathrm {n} \} \Pr (U = \mathrm {n}) \\ = 0 \times \Pr (U = a) + 1 \times \Pr (U = c) + (- 1) \times \Pr (U = d) + 0 \times \Pr (U = n), \\ \end{array}
$$

which, under Assumption 21.2, reduces to

$$
\tau_ {D} = \Pr (U = c). \tag {21.4}
$$

By (21.4), the proportion of the compliers $\pi_{\mathrm{c}} = \operatorname{pr}(U = \mathrm{c})$ equals the average causal effect of the treatment assigned on $D$ , an identifiable quantity under the CRE. Although we do not know all the compliers based on the observed data, we can identify their proportion in the whole population based on (21.4). Combining (21.3) and (21.4), we have the following result.

Theorem 21.1 Under Assumptions 21.2-21.3, we have

$$
E \{Y (1) - Y (0) \mid U = \mathrm {c} \} = \frac {\tau_ {Y}}{\tau_ {D}}
$$

if $\tau_{D} \neq 0$ .

Following Imbens and Angrist (1994) and Angrist et al. (1996), we define a new causal effect below.

Definition 21.1 (CACE or LATE) Define

$$
\tau_ {\mathrm {c}} = E \{Y (1) - Y (0) \mid U = \mathrm {c} \}
$$

as the "complier average causal effect (CACE)" or the "local average treatment effect (LATE)". It has alternative forms:

$$
\begin{array}{l} \tau_ {\mathrm {c}} = E \{Y (1) - Y (0) \mid D (1) = 1, D (0) = 0 \} \\ = E \{Y (1) - Y (0) \mid D (1) > D (0) \}. \\ \end{array}
$$

The CACE is the average causal effect of $Z$ on $Y$ among compliers with $D(1) = 1, D(0) = 0$ , or, equivalently, units with $D(1) > D(0)$ under the monotonicity. Based on Definition 21.1, we can rewrite Theorem 21.1 as

$$
\tau_ {c} = \frac {\tau_ {Y}}{\tau_ {D}},
$$

that is, the CACE or LATE equals the ratio of the average causal effects on $Y$ over that on $D$ . Under Assumption 21.1, we further identify the CACE below.

Corollary 21.1 Under Assumptions 21.1-21.3, we have

$$
\tau_ {\mathrm {c}} = \frac {E (Y \mid Z = 1) - E (Y \mid Z = 0)}{E (D \mid Z = 1) - E (D \mid Z = 0)}.
$$

Therefore, under CRE, monotonicity, and exclusion restriction, we can nonparametrically identify the CACE as the ratio of the difference in means of the outcome over the difference in means of the treatment received.

# 21.2.2 Estimation

Based on Corollary 21.1, we can estimate $\tau_{\mathrm{c}}$ by a simple ratio

$$
\hat {\tau} _ {c} = \frac {\hat {\tau} _ {Y}}{\hat {\tau} _ {D}},
$$

which is called the Wald estimator (Wald, 1940) or the IV estimator. In the above discussion, $Z$ acts as the IV for $D$ .

We can obtain the variance estimator based on the following heuristics (see Example A.3):

$$
\hat {\tau} _ {\mathrm {c}} - \tau_ {\mathrm {c}} = (\hat {\tau} _ {Y} - \tau_ {\mathrm {c}} \hat {\tau} _ {D}) / \hat {\tau} _ {D} \approx (\hat {\tau} _ {Y} - \tau_ {\mathrm {c}} \hat {\tau} _ {D}) / \tau_ {D} = \hat {\tau} _ {A} / \tau_ {D},
$$

where $\hat{\tau}_A$ is the difference-in-means of the adjusted outcome $A_{i} = Y_{i} - \tau_{\mathrm{c}}D_{i}$ . So the asymptotic variance of $\hat{\tau}_{\mathrm{c}}$ is close to the variance of $\hat{\tau}_A$ divided by $\tau_D^2$ . The variance estimation proceeds in the following steps:

1. obtain the adjusted outcomes $\hat{A}_i = Y_i - \hat{\tau}_{\mathrm{c}}D_i$ $(i = 1,\dots ,n)$   
2. obtain the Neyman-type variance estimate based on the adjusted outcomes:

$$
\hat {V} _ {\hat {A}} = \frac {\hat {S} _ {\hat {A}} ^ {2} (1)}{n _ {1}} + \frac {\hat {S} _ {\hat {A}} ^ {2} (0)}{n _ {0}},
$$

where $\hat{S}_{\hat{A}}^2 (1)$ and $\hat{S}_{\hat{A}}^2 (0)$ are the sample variances of the $\hat{A}_i$ 's under the treatment and control, respectively;

3. obtain the final variance estimator $\hat{V}_{\hat{A}} / \hat{\tau}_D^2$

See Problem 21.2 for the justification of the above variance estimator. Alternatively, we can also use the bootstrap to approximate the variance of $\hat{\tau}_{\mathrm{c}}$ . The following functions can calculate the point estimator $\hat{\tau}_{\mathrm{c}}$ and the standard error with the formula $\hat{V}_{\hat{A}}$ and the bootstrap.

```txt
## IV point estimator
IV_Wald = function(Z, D, Y)
{
    tau_D = mean(D[Z==1]) - mean(D[Z==0])
    tau_Y = mean(Y[Z==1]) - mean(Y[Z==0])
    CACE = tau_Y / tau_D 
```

c(tau_D, tau_Y, CACE)   
}   
## IV se via the delta method   
IV_WaldOTA $=$ function(Z,D,Y)   
{ est $=$ IV_Wald(Z,D,Y) AdjustedY $=$ Y - D\*est[3] VarAdj $=$ var(AdjustedY[Z==1])/sum(Z)+ var(AdjustedY[Z==0])/sum(1-Z) c(est[3],sqrt(VarAdj)/abs(est[1]))   
}   
##IV se via the bootstrap   
IV_Wald.bootstrap $=$ function(Z,D,Y,n.boot $= 200$ ）   
{ est $=$ IV_Wald(Z,D,Y)   
CACEboot $=$ replicate(n.boot,{ id.boot $=$ sample(1:length(Z)，replace $\equiv$ TRUE) IV_Wald(Z[id.boot],D[id.boot],Y[id.boot])[3] ））   
c(est[3],sd(CACEboot))   
}

Under the null hypothesis that $\tau_{\mathrm{c}} = 0$ , we can approximate the variance by $\hat{V}_Y / \hat{\tau}_D^2$ , where $\hat{V}_Y$ is the Neyman-type variance estimate for the difference in means of $Y$ . This variance estimator is inconsistent if the true $\tau_{\mathrm{c}}$ is not zero. Therefore, it works for testing but not for estimation. Nevertheless, it gives insights for the ITT estimator and the Wald estimator. The ITT estimator $\hat{\tau}_Y$ has estimated standard error $\sqrt{\hat{V}_Y}$ . The Wald estimator $\hat{\tau}_Y / \hat{\tau}_D$ essentially equals the ITT estimator multiplied by $1 / \hat{\tau}_D > 1$ , which is larger in magnitude but at the same time, its estimated standard error increases by the same factor. Based on the variance estimators $\hat{V}_Y$ and $\hat{V}_Y / \hat{\tau}_D^2$ , the confidence intervals for $\tau_Y$ and $\tau_{\mathrm{c}}$ are

$$
\hat {\tau} _ {Y} \pm z _ {1 - \alpha / 2} \sqrt {\hat {V} _ {Y}}
$$

and

$$
\hat {\tau} _ {Y} / \hat {\tau} _ {D} \pm z _ {1 - \alpha / 2} \sqrt {\hat {V} _ {Y}} / \hat {\tau} _ {D} = \left(\hat {\tau} _ {Y} \pm z _ {1 - \alpha / 2} \sqrt {\hat {V} _ {Y}}\right) / \hat {\tau} _ {D}
$$

respectively, where $z_{1 - \alpha /2}$ is the $1 - \alpha /2$ upper quantile of the standard Normal random variable. These confidence intervals give the same qualitative conclusions since they will both cover zero or not. In some sense, the IV analysis provides the same qualitative information as the ITT analysis of $Y$ although it involves more complicated procedures.

# 21.3 Covariates

# 21.3.1 Covariate adjustment in the CRE

We now consider completely randomized experiments with covariates and assume

$$
Z \perp \left\{D (1), D (0), Y (1), Y (0), X \right\}.
$$

With covariates $X$ , we can obtain Lin (2013)'s estimators $\hat{\tau}_{D,\mathrm{L}}$ and $\hat{\tau}_{Y,\mathrm{L}}$ for both $D$ and $Y$ , resulting in $\hat{\tau}_{\mathrm{c,L}} = \hat{\tau}_{Y,\mathrm{L}} / \hat{\tau}_{D,\mathrm{L}}$ . We can approximate the asymptotic variance of $\hat{\tau}_{\mathrm{c,L}}$ using the bootstrap. The following functions can calculate the point estimator $\hat{\tau}_{\mathrm{c,L}}p$ and the standard error based on the bootstrap.

```r
## covariate adjustment in IV analysis
IV_Lin = function(Z, D, Y, X)
{
    X = scale(as.matrix(X))
    tau_D = lm(D ~ Z + X + Z*X) $coef[2]
    tau_Y = lm(Y ~ Z + X + Z*X) $coef[2]
    CACE = tau_Y/tau_D
    c(tau_D, tau_Y, CACE)
}
## IV_adj se via the bootstrap
IV_Lin.bootstrap = function(Z, D, Y, X, n.boot = 200)
{
    X = scale(as.matrix(X))
    est = IV_Lin(Z, D, Y, X)
    CACEboot = replicate(n.boot, {
        id.boot = sample(1:length(Z), replace = TRUE)
        IV_Lin(Z{id.boot], D{id.boot], Y{id.boot], X{id.boot}, ]) [3])
    }
    c(est[3], sd(CACEboot))
} 
```

# 21.3.2 Covariates in conditional randomization or unconfounded observational studies

If randomization holds conditionally, i.e.,

$$
Z \bot \{D (1), D (0), Y (1), Y (0) \} \mid X,
$$

then we must adjust for covariates to avoid bias. The analysis is also straightforward since we already have discussed many estimators in Part III for estimating the effects of $Z$ on $D$ and $Y$ , respectively. We can just use them in the

ratio formula $\hat{\tau}_{\mathrm{c}} = \hat{\tau}_{Y} / \hat{\tau}_{D}$ and use the bootstrap to approximate the asymptotic variance. I do not implement the corresponding estimator and variance estimator but relegate it as Problem 21.8.

# 21.4 Weak IV

# 21.4.1 Some simulation

Even if $\tau_{D} > 0$ , there is a positive probability that $\hat{\tau}_{D}$ is zero, so the variance of $\hat{\tau}_{\mathrm{c}}$ is infinity (see Problem 21.1). The variance from the Normal approximation discussed before is not the variance of $\hat{\tau}_{\mathrm{c}}$ but rather the variance of its asymptotic distribution. This is a subtle technical point. When $\tau_{D}$ is close to 0, which is referred to as the weak IV case, the ratio estimator $\hat{\tau}_{\mathrm{c}} = \hat{\tau}_{Y} / \hat{\tau}_{D}$ has poor finite-sample properties. In this scenario, $\hat{\tau}_{\mathrm{c}}$ has finite-sample bias and non-Normal asymptotic distribution, and the corresponding Wald-type confidence intervals have poor coverage properties<sup>4</sup>. In the simple case with a binary outcome $Y$ , we know that $\tau_{Y}$ must be bounded between $-1$ and 1, but there is no guarantee that $\hat{\tau}_{\mathrm{c}}$ is bounded between $-1$ and 1.

Figures 21.1a and 21.1b show the histograms of $\hat{\tau}_{\mathrm{c}}$ and $\hat{\tau}_{\mathrm{c,L}}$ over simulation with different $\pi_{\mathrm{c}}$ . I leave the detailed data-generating processes to the R code. From the figures, the distributions of the estimators $\hat{\tau}_{\mathrm{c}}$ and $\hat{\tau}_{\mathrm{c,L}}$ are far from Normal when $\pi_{\mathrm{c}}$ equals 0.2 and 0.1. Statistical inference based on asymptotic Normality is unlikely to be reliable.

# 21.4.2 A procedure robust to weak IV

How do we deal with a weak IV? From a testing perspective, there is an easy solution. Because $\tau_{\mathrm{c}} = \tau_{Y} / \tau_{D}$ , so the following two null hypotheses are equivalent:

$$
H _ {0}: \tau_ {\mathrm {c}} = 0 \Longleftrightarrow H _ {0} ^ {\prime}: \tau_ {Y} = 0
$$

if $\tau_{D} > 0$ . Therefore, we simply test $H_0'$ , i.e., the average causal effect of $Z$ on $Y$ is zero. This echoes our discussion in Section 21.2.2 about the relationship between the ITT analysis and the IV analysis.

From an estimation perspective, we can focus on the confidence interval although the point estimator has poor finite-sample properties. Because $\tau_{\mathrm{c}} = \tau_{Y} / \tau_{D}$ , this is similar to the classical Fieller-Creasy problem in statistics. Below we discuss a strategy for constructing confidence intervals for $\tau_{\mathrm{c}}$

![](images/4f7fba7e4d3c78b0d009788e74a60d6cc16b151de12b07b8d1c395ad298144f0.jpg)

![](images/465d451ba4eb2d6c94fba7a03c118d5f5bd06ba7d3b0cb53c59c300f464f7f0a.jpg)

![](images/03224c896b80d2df761757ba464cc69142793424d14f8c327fba68180023e4ab.jpg)

![](images/efa6c19b62b211e1f2a77e9b7051a22d17e8b98b027b313d2d9bf41f77b16b3a.jpg)  
(a) Without covariate adjustment

![](images/81b3bf3656582ef6e7a218279fb0e60fffa55b1463ffc75d099ac63f160d6916.jpg)

![](images/853f4b2fda624839462a4f6ddbbf204d5ed74d7df91d08b1fa01f13cebc14aa2.jpg)  
(b) With covariate adjustment   
FIGURE 21.1: Simulation with strong and weak IVs

motivated by Fieller (1954); see Chapter A.4.2. By the duality between confidence intervals and hypothesis tests (See Chapter A.2.5), we can construct a confidence set for $\tau_{\mathrm{c}}$ by inverting a sequence of null hypotheses

$$
H _ {0} (b): \tau_ {\mathrm {c}} = b.
$$

Given the true value $\tau_{\mathrm{c}} = b$ we have

$$
\tau_ {Y} - b \tau_ {D} = 0.
$$

The null hypothesis $H_0(b)$ is equivalent to the null hypothesis of zero average causal effect on the outcome $A_i(b) = Y_i - bD_i$ :

$$
H _ {0} (b): \tau_ {A (b)} = 0.
$$

Let $\hat{\tau}_A(b)$ be a generic point estimator for $\tau_{A(b)}$ with the associated variance estimator $\hat{V}_A(b)$ . The point and variance estimators depend on the settings. In the CRE without covariates, $\hat{\tau}_A(b)$ is the difference in means of the outcome $A_i(b)$ and $\hat{V}_A(b)$ is the Neyman-type variance estimator. In the CRE with covariates, $\hat{\tau}_A(b)$ is Lin (2013)'s estimator for the outcome $A_i(b)$ and $\hat{V}_A(b)$ is the EHW variance estimator in the associated OLS fit of $Y_i - bD_i$ on $(Z_i,X_i,Z_iX_i)$ with the correction term<sup>5</sup> discussed in Chapter 9.1. In unconfounded observational studies, we can obtain the estimator for the average causal effect on $A_i(b)$ and the associated variance estimator based on many existing strategies in Part III of the book.

Based on $\hat{\tau}_A(b)$ and $\hat{V}_A(b)$ , we can construct a Wald-type test for $H_0(b)$ . Inverting tests, we can construct the following confidence set for $\tau_{\mathrm{c}}$ :

$$
\left\{b: \frac {\hat {\tau} _ {A} ^ {2} (b)}{\hat {V} _ {A} (b)} \leq z _ {1 - \alpha / 2} ^ {2} \right\}
$$

where $z_{1 - \alpha /2}$ is the $1 - \alpha /2$ upper quantile of the standard Normal random variable. This is close to the Anderson-Rubin-type confidence interval in econometrics (Anderson and Rubin, 1950). Due to its connection to Fieller (1954), I will call it the Fieller-Anderson-Rubin (FAR) confidence interval. These weak-IV confidence intervals reduce to the asymptotic confidence intervals when the IV is strong. But they have additional guarantees when the IV is weak. I recommend using them in practice.

Example 21.1 To gain intuition about the FAR confidence interval, we look into the simple case of the CRE without covariates. The quadratic inequality in the confidence interval reduces to

$$
\begin{array}{l} (\hat {\tau} _ {Y} - b \hat {\tau} _ {D}) ^ {2} \\ \leq z _ {1 - \alpha / 2} \left[ n _ {1} ^ {- 1} \left\{\hat {S} _ {Y} ^ {2} (1) + b ^ {2} \hat {S} _ {D} ^ {2} (1) - 2 b \hat {S} _ {Y D} (1) \right\} \right. \\ \left. \right.\left. + n _ {0} ^ {- 1} \left\{\hat {S} _ {Y} ^ {2} (0) + b ^ {2} \hat {S} _ {D} ^ {2} (0) - 2 b \hat {S} _ {Y D} (0) \right\}\right], \\ \end{array}
$$

where $\{\hat{S}_Y^2 (1),\hat{S}_D^2 (1),\hat{S}_{YD}(1)\}$ and $\{\hat{S}_Y^2 (0),\hat{S}_D^2 (0),\hat{S}_{YD}(0)\}$ are the sample variances and covariances of $Y$ and $D$ under the treatment and control, respectively. The confidence set can be a close interval, two disconnected intervals, an empty set, or the whole real line. I relegate the detailed discussion to Problem 21.4.

# 21.4.3 Implementation and simulation

The following functions can compute a sequence of $p$ -values as a function of $b$ . The function FARci does not use covariates, and the function FARciX uses covariates which relies on the function linestimator defined in Chapter 9.2.

FARci $=$ function(Z，D，Y，Lower，Upper，grid)   
{ CIrange $\equiv$ seq(Lower，Upper，grid) Pvalue $\equiv$ sapply(CIrange，function(t){ Y_t $\equiv$ Y-t*D Tauadj $\equiv$ mean(Y_t[Z==1]）-mean(Y_t[Z==0]) VarAdj $\equiv$ var(Y_t[Z==1])/sum(Z)+ var(Y_t[Z==0])/sum(1-Z) Tstat $\equiv$ Tauadj/sqrt(VarAdj) (1-pnorm(abs(Tstat))\*2 }） return(list(CIrange $\equiv$ CIrange，Pvalue $\equiv$ Pvalue))   
}   
FARciX $=$ function(Z，D，Y，X，Lower，Upper，grid) { CIrange $\equiv$ seq(Lower，Upper，grid) X $\equiv$ scale(X) Pvalue $\equiv$ sapply(CIrange，function(t){ Y_t $\equiv$ Y-t*D linest $\equiv$ linestimator(Z，Y_t,X) Tstat $\equiv$ linest[1]/linest[3] (1-pnorm(abs(Tstat)))\*2 }） return(list(CIrange $\equiv$ CIrange，Pvalue $\equiv$ Pvalue))

Figure 21.2 displays the $p$ -value as a function of $b$ in simulated data with different $\pi_{\mathrm{c}}$ . Figures 21.2a and 21.2b are based on two realizations of the same data-generating process, with details relegated to the R code. In Figure 21.2a, the FAR confidence sets are all closed intervals, whereas, in Figure 21.2b, the confidence sets are not closed intervals with $\pi_{\mathrm{c}} = 0.2$ and $\pi_{\mathrm{c}} = 0.1$ . The shapes of the confidence sets remain stable across two realizations with $\pi_{\mathrm{c}} = 0.5$ .

![](images/2f2c3a693e4c4ddefd24c82136409345da216a98c6ffc730352cfe840f96731a.jpg)

![](images/6461f1da3c0b574817fd51f6555843ef61680475c2fe738ef235170dc59be89e.jpg)

![](images/29bd2174fdbe9f15a80a034cc5b94fff91e193bfa78f30fd18a8f2990685f5a3.jpg)

![](images/5f0b208e0e781edfa4e4b50ff7c43d02d037f9e960e9e6b3973bbc5257b1c4c1.jpg)

![](images/411403455865081c642d745cc09f983045c1f35792c4fea2e6c0fe58cd9d8a79.jpg)

![](images/8fb65ea8e0b3fac4ba274081b6e7cf68965044a0f8a750ba663f72d98e4c16ba.jpg)  
(a) Realization 1   
(b) Realization 2   
FIGURE 21.2: FAR confidence interval based on simulated data with different $\pi_{\mathrm{c}}$ : two realizations

# 21.5 Application

The mediation package contains a dataset jobs from the Job Search Intervention Study (JOBS II), which was a randomized field experiment that investigated the efficacy of a job training intervention on unemployed workers. The variable treat is the indicator for whether a participant was randomly selected for the JOBS II training program, and the variable comply is the indicator for whether a participant actually participated in the JOBS II program. An outcome of interest is job-seeking for measuring the level of job-search self-efficacy with values from 1 to 5. Covariates include sex, age, marital, nonwhite, educ, and income.

```haskell
> jobsdata = read.csv("jobsdata.csv")
> Z = jobsdata\(treat
> D = jobsdata\)comply
> Y = jobsdata\)job Seek
> getX = lm(treat ~ sex + age + marital +
+ + nonwhite + educ + income,
+ data = jobsdata)
> X = model.matrix(getX)[-, -1] 
```

We can estimate $\tau_{\mathrm{c}}$ by $\hat{\tau}_{\mathrm{c}}$ and obtain the standard error based on $\hat{V}_{\hat{A}}$ and the bootstrap. We can further conduct covariate adjustment to obtain $\hat{\tau}_{\mathrm{c,L}}$ and obtain the standard error based on the bootstrap. The results are below. The point estimator and the standard error are stable across methods.

```julia
> # without covariates
> res = rbind(IV_WaldOTA(Z, D, Y), + IV_Wald.bootstrap(Z, D, Y, n.boot = 10^3))
> # with covariates
> res = rbind(res, + IV_Lin.bootstrap(Z, D, Y, X, n.boot = 10^3))
> res = cbind(res, res[, 1] - 1.96*res[, 2], + res[, 1] + 1.96*res[, 2])
> row names(res) = c("delta", "bootstrap", "with covariates")
> colnames(res) = c("est", "se", "lower CI", "upper CI")
> round(res, 3)
est se lower CI upper CI
delta 0.109 0.081 -0.050 0.268
bootstrap 0.109 0.083 -0.054 0.271
with covariates 0.118 0.082 -0.042 0.278 
```

We can also construct the FAR confidence sets by inverting tests. They are similar to the confidence intervals above.

```txt
lower CI upper CI  
without covariates -0.050 0.267  
with covariates -0.047 0.282 
```

![](images/156139aff2908252e84034375accd32b80df369a28cbc849f153426a37080327.jpg)  
Figure 21.3 plots the $p$ -values for a sequence of tests.

![](images/8ef7e57b7c1e14233811ca72e9112d92cceae1ec7d6983136566951a32843deb.jpg)  
FIGURE 21.3: Confidence interval of $\tau_{\mathrm{c}}$ by inverting tests: upper panel without covariate adjustment, and lower panel with covariate adjustment

# 21.6 Interpreting the CACE

The notation for potential outcomes $\{D(1), D(0), Y(1), Y(0)\}$ is with respect to the hypothetical intervention of the treatment assigned $Z$ . So $\tau_{\mathrm{c}}$ is the average causal effect of the treatment assigned on the outcome for compliers. Fortunately, $D = Z$ for compliers, so we can also interpret $\tau_{\mathrm{c}}$ as the average

causal effect of the treatment received on the outcome for compliers. This partially answers the scientific question.

Some papers use different notation. For instance, Angrist et al. (1996) use $Y_{i}(z,d)$ for the potential outcome of unit $i$ under a two-by-two factorial experiment with the treatment assigned $z$ and treatment received $d$ . Angrist (2022, Section 3.1) comments on the intellectual history of this choice of notation. With the notation, the exclusion restriction assumption then has the following form.

Assumption 21.4 (exclusion restriction) $Y_{i}(z,d) = Y_{i}(d)$ for all $i$ , that is, the potential outcome is only a function of $d$ .

Based on the causal diagram below, Assumption 21.4 rules out the direct arrow from $Z$ to $Y$ . In such a case, $Z$ is an IV for $D$ .

![](images/14cfa6aba0ced0da12c9120711f88ab848a16582d762f5c1c716431cbcf1ab44.jpg)

Under Assumption 21.4, the augmented notation $Y_{i}(z,d)$ reduces to $Y_{i}(d)$ which justifies the name of "exclusion restriction." Therefore, $Y_{i}(1,d) = Y_{i}(0,d)$ for $d = 0,1$ , which, coupled with Assumption 21.2, implies that

$$
\begin{array}{l} Y _ {i} (z = 1) - Y _ {i} (z = 0) \quad = \quad Y _ {i} (1, D _ {i} (1)) - Y _ {i} (0, D _ {i} (0)) \\ = \left\{ \begin{array}{l l} 0, & \text {i f} U _ {i} = \mathrm {a}, \\ 0, & \text {i f} U _ {i} = \mathrm {n}, \\ Y _ {i} (d = 1) - Y _ {i} (d = 0), & \text {i f} U _ {i} = \mathrm {c}. \end{array} \right. \\ \end{array}
$$

In the above, I emphasize the potential outcomes are with respect to $z$ , $d$ , or both, to avoid confusion. The previous decomposition of $\tau_{Y}$ holds and we have the following result from Imbens and Angrist (1994) and Angrist et al. (1996).

Recall the average causal effect on $D$ , $\tau_{D} = E\{D(1) - D(0)\}$ , define the average causal effect on $Y$ as $\tau_{Y} = E\{Y(D(1)) - Y(D(0))\}$ , and define the complier average causal effect as

$$
\tau_ {\mathrm {c}} = E \{Y (d = 1) - Y (d = 0) \mid U = \mathrm {c} \}.
$$

Theorem 21.2 Under Assumptions 21.2-21.4, we have

$$
Y (D (1)) - Y (D (0)) = \{D (1) - D (0) \} \times \{Y (d = 1) - Y (d = 0) \}
$$

and $\tau_{\mathrm{c}} = \tau_{Y} / \tau_{D}$

The proof is almost identical to the proof of Theorem 21.1 with modifications of the notation. I leave it as Problem 21.3. From the notation $Y_{i}(d)$ , it is more convenient to interpret $\tau_{c}$ as the average causal effect of the treatment received on the outcome for compliers.

# 21.7 Homework problems

# 21.1 Variance of the Wald estimator

Show that $\operatorname{var}(\hat{\tau}_{\mathrm{c}}) = \infty$

# 21.2 Asymptotic variance of the Wald estimator and its estimation

Consider the large-sample regime with $n\to \infty$ . First show that $\sqrt{n} (\hat{\tau}_{\mathrm{c}} - \tau_{\mathrm{c}})\rightarrow$ $\mathrm{N}(0,V)$ in distribution and find $V$ . Then show that $\hat{V}_{\hat{A}} / V\rightarrow 1$ in probability.

# 21.3 Proof of the main theorem of Imbens and Angrist (1994) and Angrist et al. (1996)

Prove Theorem 21.2.

# 21.4 More on the FAR confidence set

The confidence set in Example 21.1 can be a close interval, two disconnected intervals, an empty set, or the whole real line. Find the precise condition for each case.

# 21.5 More simulation for the FAR confidence set

Figure 21.2 shows the FAR confidence sets without using covariates. Conduct parallel simulation for the FAR confidence sets adjusting for covariates in CRE.

# 21.6 Binary IV and ordinal treatment received

Angrist and Imbens (1995) discussed a more general setting with a binary IV $Z$ , an ordinal treatment received $D \in \{0, 1, \dots, J\}$ , and an outcome $Y$ . The ordinal treatment received has potential outcomes $D(1)$ and $D(0)$ with respect to the binary IV, and the outcome has potential outcomes $Y(z, d)$ with respect to both the binary IV and the ordinal treatment received. Extend the discussion in Section 21.6 and the corresponding IV assumptions as below.

Assumption 21.5 We have (1) randomization that $Z \perp \{D(z), Y(z, d) : z = 0, 1; d = 0, 1, \ldots, J\}$ ; (2) monotonicity that $D(1) \geq D(0)$ ; and (3) exclusion restriction that $Y(z, d) = Y(d)$ for all $z = 0, 1$ and $d = 0, 1, \ldots, J$ .

They proved Theorem 21.3 below.

Theorem 21.3 Under Assumption 21.5, we have

$$
\frac {E (Y \mid Z = 1) - E (Y \mid Z = 0)}{E (D \mid Z = 1) - E (D \mid Z = 0)} = \sum_ {j = 1} ^ {J} w _ {j} E \left\{Y (j) - Y (j - 1) \mid D (1) \geq j > D (0) \right\}
$$

where

$$
w _ {j} = \frac {\operatorname* {p r} \{D (1) \geq j > D (0) \}}{\sum_ {j ^ {\prime} = 1} ^ {J} \operatorname* {p r} \{D (1) \geq j ^ {\prime} > D (0) \}}.
$$

Prove Theorem 21.3.

Remark: When $J = 1$ , Theorem 21.3 reduces to Theorem 21.2. With a general $J$ , it states that the standard IV formula identifies a weighted average of some latent subgroup effects. The weights are proportional to the probability of the latent groups defined by $D(1) \geq j > D(0)$ , and the latent subgroup effect $E\{Y(j) - Y(j - 1) \mid D(1) \geq j > D(0)\}$ compares the adjacent levels of the treatment received. However, this weighted average may not be easy to interpret because the latent groups overlap.

The proof can be tedious. A trick is to write the treatment received and outcome under treatment assignment $z$ as

$$
D (z) = \sum_ {j = 0} ^ {J} j 1 \{D (z) = j \}, \quad Y (D (z)) = \sum_ {j = 0} ^ {J} Y (j) 1 \{D (z) = j \}
$$

to obtain

$$
D (1) - D (0) = \sum_ {j = 0} ^ {J} j [ 1 \{D (1) = j \} - 1 \{D (0) = j \} ]
$$

and

$$
Y (D (1)) - Y (D (0)) = \sum_ {j = 0} ^ {J} Y (j) [ 1 \{D (1) = j \} - 1 \{D (0) = j \} ].
$$

Then use the following Abel's lemma, also called summation by parts:

$$
\sum_ {j = 0} ^ {J} f _ {j} \left(g _ {j + 1} - g _ {j}\right) = f _ {J} g _ {J + 1} - f _ {0} g _ {0} - \sum_ {j = 1} ^ {J} g _ {j} \left(f _ {j} - f _ {j - 1}\right)
$$

for appropriately specified sequences $(f_j)$ and $(g_j)$ .

21.7 Data analysis: a flu shot encouragement design (McDonald et al., 1992)

The dataset in fludata.txt is from a randomized encouragement design of McDonald et al. (1992), which was also re-analyzed by Hirano et al. (2000). It contains the following variables:

```txt
assign binary encouragement to receive the flu shot  
receive binary indicator for receiving the flu shot  
outcome binary outcome for flu-related hospitalization  
age age of the patient  
sex sex of the patient  
race race of the patient  
copd chronic obstructive pulmonary disease  
dm diabetes  
heartd heart disease  
renal renal disease  
liverd liver disease 
```

Analyze the data with and without adjusting for the covariates.

# 21.8 IV estimation conditional on covariates

Implement the estimators and corresponding variance estimators mentioned in Chapter 21.3.2 in R.

Remark: The problem is useful for Problem 21.9.

# 21.9 Data analysis: the Karolinska data

Revisit Problem 12.5. Rubin (2008) used the Karolinska data as an example for the IV method. In karolinska.txt, whether a patient was diagnosed at a large volume hospital can be viewed as an IV for whether a patient was treated at a large volume hospital. This is plausible conditional on other observed covariates. See Rubin (2008)'s analysis for more details.

Re-analyze the data assuming that the IV is randomly assigned conditional on observed covariates.

# 21.10 Data analysis: a job training program

The file jobtraining.rtf contains the description of the data files X.csv and Y.csv.

The dataset X.csv contains the pretreatment covariates. You can view the sampling weight variable wgt as a covariate too. Many previous analyses made this simplification although this is always a controversial issue in statistical analysis of survey data. Conduct analyses with and without covariates.

The dataset Y.csv contains the sampling weight, treatment assigned, treatment received, and many post-treatment variables. Therefore, this dataset contains many outcomes depending on your questions of interest. The data also have many complications. First, some outcomes are missing. Second, unemployed individuals do not have wages. Third, the outcomes are repeatedly observed over time. When you analyze the data, please give details about your choice of the questions of interest and estimators.

Remark: Schochet et al. (2008) analyzed the original data. Frumento et al. (2012) provided a more sophisticated analysis based on the framework in Chapter 26 later.

# 21.11 Recommended reading

Angrist et al. (1996) bridged the econometric IV perspective and statistical causal inference based on potential outcomes and demonstrated its usefulness with an application.

Some other early references on IV are Permutt and Hebel (1989), Sommer and Zeger (1991), Baker and Lindeman (1994), and Cuzick et al. (1997).

# 22

# Disentangle Mixture Distributions and Instrumental Variable Inequalities

The IV model in Chapter 21 imposes Assumptions 21.1-21.3:

1. $Z \perp \{D(1), D(0), Y(1), Y(0)\}$ ;   
2. $\operatorname{pr}(U = \mathrm{d}) = 0$ ;   
3. $Y(1) = Y(0)$ for $U = \mathrm{a}$ or $\mathrm{n}$ .

Table 22.1 summarizes the observed groups and the corresponding latent groups under the monotonicity assumption.

TABLE 22.1: Observed groups and latent groups under Assumption 21.2   

<table><tr><td>Z</td><td>D</td><td>D(1)</td><td>latent groups</td></tr><tr><td>Z = 1</td><td>D = 1</td><td>D(1) = 1</td><td>U = c or a</td></tr><tr><td>Z = 1</td><td>D = 0</td><td>D(1) = 0</td><td>U = n</td></tr><tr><td>Z = 0</td><td>D = 1</td><td>D(0) = 1</td><td>U = a</td></tr><tr><td>Z = 0</td><td>D = 0</td><td>D(0) = 0</td><td>U = c or n</td></tr></table>

Interestingly, Assumptions 21.1-21.3 together have some testable implications. Balke and Pearl (1997) called them the instrumental variable inequalities. This chapter will give an intuitive derivation of a special case of these inequalities. The proof is a direct consequence of identifying the means of the potential outcomes for all latent groups defined by $U$ .

# 22.1 Disentangle Mixture Distributions

We summarize the main results in Theorem 22.1 below. Define

$$
\pi_ {u} = \Pr (U = u) \quad (u = \mathrm {a}, \mathrm {n}, \mathrm {c})
$$

as the proportion of type $U = u$ , and

$$
\mu_ {z u} = E \{Y (z) \mid U = u \} \quad (z = 0, 1; u = \mathrm {a}, \mathrm {n}, \mathrm {c}).
$$

as the mean of the potential outcome $Y(z)$ for type $U = u$ . Exclusion restriction implies that $\mu_{1\mathrm{n}} = \mu_{0\mathrm{n}}$ and $\mu_{1\mathrm{a}} = \mu_{0\mathrm{a}}$ . Let $\mu_{\mathrm{n}}$ and $\mu_{\mathrm{a}}$ denote them, respectively.

Theorem 22.1 Under Assumptions 21.1-21.3, we can identify the proportions of the latent types by

$$
\pi_ {n} = \operatorname * {p r} (D = 0 \mid Z = 1),
$$

$$
\pi_ {\mathrm {a}} = \operatorname * {p r} (D = 1 \mid Z = 0),
$$

$$
\pi_ {\mathrm {c}} = E (D \mid Z = 1) - E (D \mid Z = 0),
$$

and the type-specific means of the potential outcomes by

$$
\mu_ {\mathrm {n}} = E (Y \mid Z = 1, D = 0),
$$

$$
\mu_ {\mathrm {a}} = E (Y \mid Z = 0, D = 1),
$$

$$
\mu_ {1 c} = \pi_ {c} ^ {- 1} \left\{E (D Y \mid Z = 1) - E (D Y \mid Z = 0) \right\},
$$

$$
\mu_ {0 c} = \pi_ {c} ^ {- 1} \left[ E \{(1 - D) Y \mid Z = 0 \} - E \{(1 - D) Y \mid Z = 1 \} \right].
$$

Proof of Theorem 22.1: Part I: We first identify the proportions of the latent compliance types. We can identify the proportion of the never takers by

$$
\begin{array}{l} \operatorname {p r} (D = 0 \mid Z = 1) = \operatorname {p r} (U = \mathrm {n} \mid Z = 1) \\ = \operatorname {p r} (U = \mathrm {n}) \\ = \pi_ {\mathrm {n}}, \\ \end{array}
$$

and the proportion of the always takers by

$$
\begin{array}{l} \operatorname {p r} (D = 1 \mid Z = 0) = \operatorname {p r} (U = \mathrm {a} \mid Z = 0) \\ = \operatorname {p r} (U = \mathrm {a}) = \pi_ {\mathrm {a}}. \\ \end{array}
$$

Therefore, the proportion of compliers is

$$
\begin{array}{l} \pi_ {\mathrm {c}} = \operatorname {p r} (U = \mathrm {c}) \\ = 1 - \pi_ {\mathrm {n}} - \pi_ {\mathrm {a}} \\ = 1 - \operatorname {p r} (D = 0 \mid Z = 1) - \operatorname {p r} (D = 1 \mid Z = 0) \\ = E (D \mid Z = 1) - E (D \mid Z = 0) \\ = \tau_ {D}, \\ \end{array}
$$

which is coherent with our previous discussion. Although we do not know individual latent compliance types for all units, we can identify the proportions of never-takers, always-takers, and compliers.

Part II: We then identify the means of the potential outcomes within latent compliance types. The observed group $(Z = 1, D = 0)$ only has never takers, so

$$
E (Y \mid Z = 1, D = 0) = E \{Y (1) \mid Z = 1, U = \mathrm {n} \} = E \{Y (1) \mid U = \mathrm {n} \} = \mu_ {\mathrm {n}}.
$$

The observed group $(Z = 0, D = 1)$ only has always takers, so

$$
E (Y \mid Z = 0, D = 1) = E \{Y (0) \mid Z = 0, U = \mathrm {a} \} = E \{Y (0) \mid U = \mathrm {a} \} = \mu_ {\mathrm {a}}.
$$

The observed group $(Z = 1, D = 1)$ has both compliers and always takers, so

$$
\begin{array}{l} E (Y \mid Z = 1, D = 1) = E \{Y (1) \mid Z = 1, D (1) = 1 \} \\ = E \{Y (1) \mid D (1) = 1 \} \\ = \operatorname {p r} \{D (0) = 1 \mid D (1) = 1 \} E \{Y (1) \mid D (1) = 1, D (0) = 1 \} \\ + \Pr \left\{D (0) = 0 \mid D (1) = 1 \right\} E \left\{Y (1) \mid D (1) = 1, D (0) = 0 \right\} \\ { = } { \frac { \pi _ { \mathrm { c } } } { \pi _ { \mathrm { c } } + \pi _ { \mathrm { a } } } \mu _ { 1 \mathrm { c } } + \frac { \pi _ { \mathrm { a } } } { \pi _ { \mathrm { c } } + \pi _ { \mathrm { a } } } \mu _ { \mathrm { a } } . } \\ \end{array}
$$

Solve the linear equation above to obtain

$$
\begin{array}{l} \mu_ {1 c} = \pi_ {c} ^ {- 1} \left\{\left(\pi_ {c} + \pi_ {a}\right) E (Y \mid Z = 1, D = 1) - \pi_ {a} E (Y \mid Z = 0, D = 1) \right\} \\ = \pi_ {c} ^ {- 1} \left\{\operatorname {p r} (D = 1 \mid Z = 1) E (Y \mid Z = 1, D = 1) \right. \\ - \operatorname {p r} (D = 1 \mid Z = 0) E (Y \mid Z = 0, D = 1) \} \\ = \pi_ {\mathrm {c}} ^ {- 1} \left\{E (D Y \mid Z = 1) - E (D Y \mid Z = 0) \right\}. \\ \end{array}
$$

The observed group $(Z = 0, D = 0)$ has both compliers and never takers, so

$$
\begin{array}{l} E (Y \mid Z = 0, D = 0) = E \{Y (0) \mid Z = 0, D (0) = 0 \} \\ = E \{Y (0) \mid D (0) = 0 \} \\ = \operatorname {p r} \{D (1) = 1 \mid D (0) = 0 \} E \{Y (0) \mid D (1) = 1, D (0) = 0 \} \\ + \Pr \left\{D (1) = 0 \mid D (0) = 0 \right\} E \left\{Y (0) \mid D (1) = 0, D (0) = 0 \right\} \\ = \frac {\pi_ {\mathrm {c}}}{\pi_ {\mathrm {c}} + \pi_ {\mathrm {n}}} \mu_ {0 \mathrm {c}} + \frac {\pi_ {\mathrm {n}}}{\pi_ {\mathrm {c}} + \pi_ {\mathrm {n}}} \mu_ {\mathrm {n}}. \\ \end{array}
$$

Solve the linear equation above to obtain

$$
\begin{array}{l} \mu_ {0 c} = \pi_ {c} ^ {- 1} \left\{\left(\pi_ {c} + \pi_ {n}\right) E (Y \mid Z = 0, D = 0) - \pi_ {n} E (Y \mid Z = 1, D = 0) \right\} \\ = \pi_ {c} ^ {- 1} \left\{\operatorname {p r} (D = 0 \mid Z = 0) E (Y \mid Z = 0, D = 0) \right. \\ - \operatorname {p r} (D = 0 \mid Z = 1) E (Y \mid Z = 1, D = 0) \} \\ = \pi_ {\mathrm {c}} ^ {- 1} \left[ E \{(1 - D) Y \mid Z = 0 \} - E \{(1 - D) Y \mid Z = 1 \} \right]. \\ \end{array}
$$

□

Based on the formulas of $\mu_{1\mathrm{c}}$ and $\mu_{0\mathrm{c}}$ in Theorem 22.1, we can simplify $\tau_{\mathrm{c}} = \mu_{1\mathrm{c}} - \mu_{0\mathrm{c}}$ as

$$
\tau_ {\mathrm {c}} = \left\{E (Y \mid Z = 1) - E (Y \mid Z = 0) \right\} / \pi_ {\mathrm {c}},
$$

which is the same as the formula in Theorem 21.1 before.

Theorem 22.1 focuses on identifying the means of the potential outcomes, $\mu_{zu}$ . Imbens and Rubin (1997) derived more general identification formulas for the distribution of the potential outcomes; I leave the details to Problem 22.3.

# 22.2 Testable implications: Instrumental Variable Inequalities

Is there any additional value of the detour to derive the formula of $\tau_{\mathrm{c}}$ through Theorem 22.1? The answer is yes. For binary outcome, the following inequalities must be true:

$$
0 \leq \mu_ {1 c} \leq 1, \quad 0 \leq \mu_ {0 c} \leq 1,
$$

which implies four inequalities

$$
E (D Y \mid Z = 1) - E (D Y \mid Z = 0) \geq 0,
$$

$$
E (D Y \mid Z = 1) - E (D Y \mid Z = 0) \leq E (D \mid Z = 1) - E (D \mid Z = 0),
$$

$$
E \{(1 - D) Y \mid Z = 0 \} - E \{(1 - D) Y \mid Z = 1 \} \geq 0,
$$

$$
E \{(1 - D) Y \mid Z = 0 \} - E \{(1 - D) Y \mid Z = 1 \} \leq E (D \mid Z = 1) - E (D \mid Z = 0).
$$

Rearranging terms, we obtain the following unified inequalities.

Theorem 22.2 (Instrumental Variable Inequalities) With a binary outcome $Y$ , Assumptions 21.1-21.3 imply

$$
E (Q \mid Z = 1) - E (Q \mid Z = 0) \geq 0, \tag {22.1}
$$

where $Q = DY, D(1 - Y), (D - 1)Y$ and $D + Y - DY$ .

Under the IV assumptions 21.1-21.3, the difference in means for $Q = DY, D(1 - Y), (D - 1)Y$ and $D + Y - DY$ must all be non-negative. Importantly, these implications only involve the distribution of the observed variables. Rejection of the IV inequalities leads to rejection of the IV assumptions.

Balke and Pearl (1997) derived more general IV inequalities with and without assuming monotonicity. The proving strategy above is due to Jiang and Ding (2020) for a slightly more complex setting. Theorem 22.2 states the testable implications only for a binary outcome. Problem 22.4 gives an equivalent form, and Problem 22.5 gives the result for a general outcome.

# 22.3 Examples

For a binary outcome, we can estimate all the parameters by the method of moments below.

IVbinary $=$ function(n111，n110，n101，n100， n011，n010，n001，n000){

# 22.3 Examples

```txt
n_tr = n111 + n110 + n101 + n100  
n_co = n011 + n010 + n001 + n000  
n = n_tr + n_co  
## proportions of the latent strata  
pi_n = (n101 + n100) / n_tr  
pi_a = (n011 + n010) / n_co  
pi_c = 1 - pi_n - pi_a  
## four observed means of the outcomes (Z=z, D=d)  
mean_y_11 = n111 / (n111 + n110)  
mean_y_10 = n101 / (n101 + n100)  
mean_y_01 = n011 / (n011 + n010)  
mean_y_00 = n001 / (n001 + n000)  
## means of the outcomes of two strata  
mu_n1 = mean_y_10  
mu_a0 = mean_y_01  
## ER implies the following two means  
mu_n0 = mu_n1  
mu_a1 = mu_a0  
## stratum (Z=1, D=1) is a mixture of c and a  
mu_c1 = ((pi_c + pi_a)*mean_y_11 - pi_a*mu_a1) / pi_c  
## stratum (Z=0, D=0) is a mixture of c and n  
mu_c0 = ((pi_c + pi_n)*mean_y_00 - pi_n*mu_n0) / pi_c  
## identifiable quantities from the observed data  
list(pi_c = pi_c,  
    pi_n = pi_n,  
    pi_a = pi_a,  
    mu_c1 = mu_c1,  
    mu_c0 = mu_c0,  
    mu_n1 = mu_n1,  
    mu_n0 = mu_n0,  
    mu_a1 = mu_a1,  
    mu_a0 = mu_a0,  
    tau_c = mu_c1 - mu_c0) 
```

We then re-visit two canonical examples with binary data.

Example 22.1 Investigators et al. (2014) assess the effectiveness of the emergency endovascular versus the open surgical repair strategies for patients with a clinical diagnosis of ruptured aortic aneurism. Patients are randomized to either the emergency endovascular or the open repair strategy. The primary outcome is the survival status after 30 days. Let $Z$ be the treatment assigned, with $Z = 1$ for the endovascular strategy and $Z = 0$ for the open repair. Let $D$ be the treatment received. Let $Y$ be the survival status, with $Y = 1$ for dead,

# 30622 Disentangle Mixture Distributions and Instrumental Variable Inequalities

and $Y = 0$ for alive. Table 22.2a summarizes the observed data. Using the IVbinary function above, we can obtain the following estimates:

```perl
> investigators_analysis = IVbinary(n111 = 107, + n110 = 42, + n101 = 68, + n100 = 42, + n011 = 24, + n010 = 8, + n001 = 131, + n000 = 79) > > investigators_analysis $pi_c [1] 0.4430582 $pi_n [1] 0.4247104 $pi_a [1] 0.1322314 $mu_c1 [1] 0.7086064 $mu_c0 [1] 0.6292042 $mu_n1 [1] 0.6181818 $mu_n0 [1] 0.6181818 $mu_a1 [1] 0.75 $mu_a0 [1] 0.75 $tau_c [1] 0.07940223 
```

There is no evidence of violating the IV assumptions.

Example 22.2 In Hirano et al. (2000), physicians are randomly selected to receive a letter encouraging them to inoculate patients at risk for flu. The treatment is the actual flu shot, and the outcome is an indicator of flu-related hospital visits. However, some patients do not comply with their assignments. Let $Z_{i}$ be the indicator of encouragement to receive the flu shot, with $Z = 1$ if

the physician receives the encouragement letter, and $Z = 0$ otherwise. Let $D$ be the treatment received. Let $Y$ be the outcome, with $Y = 0$ if for a flu-related hospitalization during the winter, and $Y = 1$ otherwise. See Problem 21.7 for more details of the data. Table 22.2b summarizes the observed data. Using the IVbinary function above, we can obtain the following estimates:

```c
> flu_analysis = IVbinary(n111 = 31,
+ n110 = 422,
+ n101 = 84,
+ n100 = 935,
+ n011 = 30,
+ n010 = 233,
+ n001 = 99,
+ n000 = 1027)
>
flu_analysis
$ pi_c
[1] 0.1183997 
```

```txt
$ pi_n
[1] 0.6922554 
```

```txt
$ pi_a
[1] 0.1893449 
```

```txt
$ mu_c1
[1] -0.004548064 
```

```txt
$ mu_c0
[1] 0.1200094 
```

```txt
$ mu_n1
[1] 0.08243376 
```

```txt
$ mu_n0
[1] 0.08243376 
```

```txt
$ mu_a1
[1] 0.1140684 
```

```txt
$ mu_a0
[1] 0.1140684 
```

```txt
$ tau_c
[1] -0.1245575 
```

Since $\hat{\mu}_{1c} < 0$ , there is evidence of violating the IV assumptions.

TABLE 22.2: Binary data and IV inequalities   
(a) Investigators et al. (2014)'s study   

<table><tr><td></td><td colspan="2">Z=1</td><td colspan="2">Z=0</td></tr><tr><td></td><td>D=1</td><td>D=0</td><td>D=1</td><td>D=0</td></tr><tr><td>Y=1</td><td>107</td><td>68</td><td>24</td><td>131</td></tr><tr><td>Y=0</td><td>42</td><td>42</td><td>8</td><td>79</td></tr></table>

(b) Hirano et al. (2000)'s study   

<table><tr><td></td><td colspan="2">Z = 1</td><td colspan="2">Z = 0</td></tr><tr><td></td><td>D = 1</td><td>D = 0</td><td>D = 1</td><td>D = 0</td></tr><tr><td>Y = 1</td><td>31</td><td>85</td><td>30</td><td>99</td></tr><tr><td>Y = 0</td><td>424</td><td>944</td><td>237</td><td>1041</td></tr></table>

# 22.4 Homework problems

# 22.1 More detailed data analysis

Examples 22.1 and 22.2 ignored the uncertainty in the estimates. Calculate the confidence intervals for the true parameters.

# 22.2 Risk ratio for compliers

With a binary outcome, we can define the risk ratio for compliers as

$$
\mathrm {R R} _ {\mathrm {c}} = \frac {\operatorname* {p r} \{Y (1) = 1 \mid U = \mathrm {c} \}}{\operatorname* {p r} \{Y (0) = 1 \mid U = \mathrm {c} \}}.
$$

Show that under Assumptions 21.1-21.3, we can identify it by

$$
\mathrm {R R} _ {\mathrm {c}} = \frac {E (D Y \mid Z = 1) - E (D Y \mid Z = 0)}{E \{(D - 1) Y \mid Z = 1 \} - E \{(D - 1) Y \mid Z = 0 \}}.
$$

Remark: Using Theorem 22.1, we can identify any comparisons between $E\{Y(1) \mid U = \mathrm{c}\}$ and $E\{Y(0) \mid U = \mathrm{c}\}$ .

# 22.3 Disentangle the mixtures: distributional results

This problem extends Theorem 22.1. Define

$$
f _ {z u} (y) = \Pr \left\{Y (z) = y \mid U = u \right\}, \quad (z = 0, 1; u = \mathrm {a}, \mathrm {n}, \mathrm {c})
$$

as the density of $Y(z)$ for latent stratum $U = u$ , and define

$$
g _ {z d} (y) = \operatorname * {p r} (Y = y \mid Z = z, D = d)
$$

as the density of the outcome within the observed group $(Z = z, D = d)$ . Exclusion restriction implies that $f_{\mathrm{1n}}(y) = f_{0\mathrm{n}}(y)$ and $f_{\mathrm{1a}}(y) = f_{0\mathrm{a}}(y)$ . Let $f_{\mathrm{n}}(y)$ and $f_{\mathrm{a}}(y)$ denote them, respectively.

Prove Theorem 22.3 below.

Theorem 22.3 Under Assumptions 21.1-21.3, we can identify the type-specific densities of the potential outcomes by

$$
f _ {\mathrm {n}} (y) = g _ {1 0} (y),
$$

$$
f _ {\mathrm {a}} (y) = g _ {0 1} (y),
$$

$$
f _ {1 c} (y) = \pi_ {c} ^ {- 1} \left\{\Pr (D = 1 \mid Z = 1) g _ {1 1} (y) - \Pr (D = 1 \mid Z = 0) g _ {0 1} (y) \right\},
$$

$$
f _ {0 c} (y) = \pi_ {c} ^ {- 1} \{\operatorname * {p r} (D = 0 \mid Z = 0) g _ {0 0} (y) - \operatorname * {p r} (D = 0 \mid Z = 1) g _ {1 0} (y) \}.
$$

# 22.4 Alternative form of Theorem 22.2

The inequalities in (22.1) can be re-written as

$$
\operatorname {p r} (D = 1, Y = y \mid Z = 1) \geq \operatorname {p r} (D = 1, Y = y \mid Z = 0),
$$

$$
\operatorname {p r} (D = 0, Y = y \mid Z = 0) \geq \operatorname {p r} (D = 0, Y = y \mid Z = 1)
$$

for both $y = 0,1$

# 22.5 IV inequalities for a general outcome

For a general outcome $Y$ , show that Assumptions 21.1-21.3 imply

$$
\operatorname {p r} (D = 1, Y \geq y \mid Z = 1) \geq \operatorname {p r} (D = 1, Y \geq y \mid Z = 0),
$$

$$
\operatorname {p r} (D = 1, Y <   y \mid Z = 1) \geq \operatorname {p r} (D = 1, Y <   y \mid Z = 0),
$$

$$
\operatorname {p r} (D = 0, Y \geq y \mid Z = 0) \geq \operatorname {p r} (D = 0, Y \geq y \mid Z = 1),
$$

$$
\Pr (D = 0, Y <   y \mid Z = 0) \geq \Pr (D = 0, Y <   y \mid Z = 1)
$$

for all $y$ .

Remark: Imbens and Rubin (1997) and Kitagawa (2015) discussed similar results. We can test the first inequality based on an analog of the Kolmogorov-Smirnov statistic:

$$
\mathrm {K S} _ {1} = \max _ {y} \Big | \frac {\sum_ {i = 1} ^ {n} Z _ {i} D _ {i} 1 (Y _ {i} \leq y)}{\sum_ {i = 1} ^ {n} Z _ {i} D _ {i}} - \frac {\sum_ {i = 1} ^ {n} (1 - Z _ {i}) D _ {i} 1 (Y _ {i} \leq y)}{\sum_ {i = 1} ^ {n} (1 - Z _ {i}) D _ {i}} \Big |.
$$

# 22.6 Example for the IV inequalities

Give an example in which all the IV inequalities hold and another example in which not all the IV inequalities hold. You need to specify the joint distribution of $(Z, D, Y)$ with binary variables.

# 22.7 Violations of the key assumptions

Theorem 21.1 relies on randomization, monotonicity, and exclusion restriction. The latter two are not testable even in randomized experiments. When they are violated, the IV estimator no longer identifies the CACE. This problem gives two cases below, which are restatements of Propositions 2 and 3 in Angrist et al. (1996). Recall $\pi_u = \mathrm{pr}(U = u)$ and $\tau_{u} = E\{Y(1) - Y(0)\mid U = u\}$ for $u = \mathrm{a,n,c,d}$ .

Theorem 22.4 (a) Under Assumptions 21.1 and 21.2 without the exclusion restriction, we have

$$
\frac {E (Y \mid Z = 1) - E (Y \mid Z = 0)}{E (D \mid Z = 1) - E (D \mid Z = 0)} - \tau_ {\mathrm {c}} = \frac {\pi_ {\mathrm {a}} \tau_ {\mathrm {a}} + \pi_ {\mathrm {n}} \tau_ {\mathrm {n}}}{\pi_ {\mathrm {c}}}.
$$

(b) Under Assumptions 21.1 and 21.3 without the monotonicity, we have

$$
\frac {E (Y \mid Z = 1) - E (Y \mid Z = 0)}{E (D \mid Z = 1) - E (D \mid Z = 0)} - \tau_ {\mathrm {c}} = \frac {\pi_ {\mathrm {d}} (\tau_ {\mathrm {c}} + \tau_ {\mathrm {d}})}{\pi_ {\mathrm {c}} - \pi_ {\mathrm {d}}}.
$$

Prove Theorem 22.4.

# 22.8 Problems of other analyses

In the process of deriving the IV inequalities in Section 22.1, we disentangled the mixture distributions by identifying the proportions of the latent strata as well as the conditional means of their potential outcomes. These results help to understand the drawbacks of other seemingly reasonable analyses. I review three estimators below and suppose Assumptions 21.1-21.3 hold.

1. The as-treated analysis compares the means of the outcomes among units receiving the treatment and control, yielding

$$
\tau_ {\mathrm {A T}} = E (Y \mid D = 1) - E (Y \mid D = 0).
$$

Show that

$$
\tau_ {\mathrm {A T}} = \frac {\pi_ {\mathrm {a}} \mu_ {\mathrm {a}} + \operatorname * {p r} (Z = 1) \pi_ {\mathrm {c}} \mu_ {\mathrm {1 c}}}{\operatorname * {p r} (D = 1)} - \frac {\pi_ {\mathrm {n}} \mu_ {\mathrm {n}} + \operatorname * {p r} (Z = 0) \pi_ {\mathrm {c}} \mu_ {\mathrm {0 c}}}{\operatorname * {p r} (D = 0)}.
$$

2. The per-protocol analysis compares the units that comply with the treatment assigned in treatment and control groups, yielding

$$
\tau_ {\mathrm {P P}} = E (Y \mid Z = 1, D = 1) - E (Y \mid Z = 0, D = 0).
$$

Show that

$$
\tau_ {\mathrm {P P}} = \frac {\pi_ {\mathrm {a}} \mu_ {\mathrm {a}} + \pi_ {\mathrm {c}} \mu_ {\mathrm {1 c}}}{\pi_ {\mathrm {a}} + \pi_ {\mathrm {c}}} - \frac {\pi_ {\mathrm {n}} \mu_ {\mathrm {n}} + \pi_ {\mathrm {c}} \mu_ {\mathrm {0 c}}}{\pi_ {\mathrm {n}} + \pi_ {\mathrm {c}}}.
$$

3. We may also want to compare the outcomes among units receiving the treatment and control, conditioning on their treatment assignment, yielding

$$
\begin{array}{l} \tau_ {Z = 1} = E (Y \mid Z = 1, D = 1) - E (Y \mid Z = 1, D = 0), \\ \tau_ {Z = 0} \quad = \quad E (Y \mid Z = 0, D = 1) - E (Y \mid Z = 0, D = 0). \\ \end{array}
$$

Show that they reduce to

$$
\tau_ {Z = 1} = \frac {\pi_ {\mathrm {a}} \mu_ {\mathrm {a}} + \pi_ {\mathrm {c}} \mu_ {\mathrm {1 c}}}{\pi_ {\mathrm {a}} + \pi_ {\mathrm {c}}} - \mu_ {\mathrm {n}}, \quad \tau_ {Z = 0} = \mu_ {\mathrm {a}} - \frac {\pi_ {\mathrm {n}} \mu_ {\mathrm {n}} + \pi_ {\mathrm {c}} \mu_ {\mathrm {0 c}}}{\pi_ {\mathrm {n}} + \pi_ {\mathrm {c}}}.
$$

# 22.9 Bounds on the average causal effect on the whole population

Extend the discussion in Section 22.1 based on the notation in Section 21.6. With the potential outcome $Y(d)$ , define the average causal effect of the treatment received on the outcome as

$$
\delta = E \{Y (d = 1) - Y (d = 0) \},
$$

and modify the definition of $\mu_{zu}$ as

$$
m _ {d u} = E \{Y (d) \mid U = u \}, \quad (z = 0, 1; u = \mathrm {a}, \mathrm {n}, \mathrm {c})
$$

due to the change of the notation. They satisfy

$$
\delta = \sum_ {u = \mathrm {a}, \mathrm {n}, \mathrm {c}} \pi_ {u} \left(m _ {1 u} - m _ {0 u}\right).
$$

Section 22.1 identifies $\pi_{\mathrm{a}}$ , $\pi_{\mathrm{n}}$ , $\pi_{\mathrm{c}}$ , $m_{1\mathrm{a}} = \mu_{1\mathrm{a}}$ , $m_{0\mathrm{n}} = \mu_{0\mathrm{n}}$ , $m_{1\mathrm{c}} = \mu_{1\mathrm{c}}$ and $m_{0\mathrm{c}} = \mu_{0\mathrm{c}}$ . But the data do not contain any information about $m_{0\mathrm{a}}$ and $m_{1\mathrm{n}}$ . Therefore, we cannot identify $\delta$ . With a bounded outcome, we can bound $\delta$ .

Theorem 22.5 Under Assumptions 21.2-21.4 with a bounded outcome in $[y, \overline{y}]$ , we have $\underline{\delta} \leq \delta \leq \overline{\delta}$ , where

$$
\underline {{\delta}} = \delta^ {\prime} - \bar {y} \operatorname {p r} (D = 1 \mid Z = 0) + \underline {{y}} \operatorname {p r} (D = 0 \mid Z = 1)
$$

and

$$
\bar {\delta} = \delta^ {\prime} - y \Pr (D = 1 \mid Z = 0) + \bar {y} \Pr (D = 0 \mid Z = 1)
$$

with $\delta' = E(DY \mid Z = 1) - E(Y - DY \mid Z = 0)$ .

Prove Theorem 22.5.

Remark: In the special case with a binary outcome, the bounds simplify to

$$
\underline {{\delta}} = E (D Y \mid Z = 1) - E (D + Y - D Y \mid Z = 0)
$$

and

$$
\bar {\delta} = E (D Y + 1 - D \mid Z = 1) - E (Y - D Y \mid Z = 0).
$$

# 22.10 One-sided noncompliance and statistical inference

Consider a randomized encouragement design where the units assigned to the control have no access to the treatment. For unit $i$ , let $Z_{i}$ be the binary treatment assigned, $D_{i}$ be the binary treatment received, and $Y_{i}$ be the outcome of interest. One-sided noncompliance happens when

$$
Z _ {i} = 0 \Longrightarrow D _ {i} = 0 (i = 1, \dots , n).
$$

Suppose that Assumption 21.1 holds.

1. Does monotonicity Assumption 21.2 hold in this case? How many latent strata defined by $\{D_i(1), D_i(0)\}$ are there in this problem? How do we identify their proportions by the observed data distribution?   
2. State the assumption of exclusion restriction. Under exclusion restriction, show that $E\{Y(z) \mid U = u\}$ can be identified by the observed data distributions. Give the formulas for all possible values of $z$ and $u$ . How do we identify the CACE in this case?   
3. If we observe pretreatment covariates $X_{i}$ for all units $i$ , how do we use the covariate information to improve the estimation efficiency of the CACE?   
4. Under Assumption 21.1, the exclusion restriction Assumption 21.3 has testable implications, which are the IV inequalities for one-sided noncompliance. State the IV inequalities.   
5. Sommer and Zeger (1991) provided the following dataset:

<table><tr><td></td><td colspan="2">Z = 1</td><td colspan="2">Z = 0</td></tr><tr><td></td><td>D = 1</td><td>D = 0</td><td>D = 1</td><td>D = 0</td></tr><tr><td>Y = 1</td><td>9663</td><td>2385</td><td>0</td><td>11514</td></tr><tr><td>Y = 0</td><td>12</td><td>34</td><td>0</td><td>74</td></tr></table>

The treatment assigned $Z$ is whether or not the child was assigned to the vitamin A supplement, the treatment received indicator $D$ is whether or not the child received the vitamin A supplement, and the binary outcome $Y$ is the survival indicator. The original RCT was conducted in Indonesia. Re-analyze the data.

Remark: Bloom (1984) first discussed one-sided noncompliance and proposed the estimator $\hat{\tau}_{c} = \hat{\tau}_{Y} / \hat{\tau}_{D}$ , which is sometimes called the Bloom estimator. Bloom (1984)'s notation is different from this chapter.

# 22.11 One-sided noncompliance with partial adherence

Sanders and Karim (2021, Table 3) reported the following data from an RCT aiming to estimate the efficacy of smoking cessation interventions among individuals with psychotic disorders.

22.4 Homework problems   

<table><tr><td>group assigned</td><td>treatment received</td><td>group size</td><td># positive outcomes</td></tr><tr><td>Control</td><td>None</td><td>151</td><td>25</td></tr><tr><td>Treatment</td><td>None</td><td>35</td><td>7</td></tr><tr><td>Treatment</td><td>Partial</td><td>42</td><td>17</td></tr><tr><td>Treatment</td><td>Full</td><td>70</td><td>40</td></tr></table>

Three tiers of treatment received are defined as follows: "full" treatment corresponds to attending all 8 treatment sessions, "partial" corresponds to attending 5 to 7 sessions, and "none" corresponds to $< 5$ sessions. The outcome is defined as the binary indicator of smoking reduction of $50\%$ or greater relative to baseline, measured at three months.

In this problem, the treatment assignment $Z$ is binary but the treatment received $D$ takes three values 0, 0.5, 1 for "none", "partial", and "full." The three-leveled $D$ causes complications, but it can only be 0 under the control assignment. How many latent strata $U = \{D(1), D(0)\}$ do we have in this problem? Can we identify their proportions?

How do we extend the exclusion restriction to this problem? What can be the causal effects of interest? Can we identify them?

Analyze the data based on the questions above.

# 22.12 Recommended reading

Balke and Pearl (1997) derived more general IV inequalities.

# An Econometric Perspective of the Instrumental Variable

Chapters 21 and 22 discuss the IV method from the experimental perspective. Figure 23.1 illustrates the intuition behind the discussion.

![](images/f2b9ffcf944e01c4ccf32f8f309cc0e4a9f196e2dacb071907b56b6d3c422deb.jpg)  
FIGURE 23.1: Causal diagram for IV

In an encouragement design with noncompliance, $Z$ is randomized, so it is independent of the confounder $U$ between the treatment received $D$ and the outcome $Y$ . Importantly, the treatment assignment $Z$ does not have any direct effect on the outcome $Y$ . It acts as an IV for the treatment received $D$ in the sense that it affects the outcome $Y$ only through the treatment received $D$ . This IV is generated by the experimenter.

In many applications, randomization is infeasible. Then how can we draw causal inference in the presence of unmeasured confounding between the treatment $D$ and outcome $Y$ ? A clever idea from econometrics is to find natural experiments to mimic the setting of encouragement designs. To identify the causal effect of $D$ on $Y$ with unmeasured confounding, we can find another variable $Z$ that satisfies the assumptions of the diagram in Figure 23.1. The variable $Z$ must satisfy the following conditions:

1. it should be close to being randomized so that it is independent of the unmeasured confounding $U$ ;   
2. it should change the distribution of $D$ ;   
3. it should affect the outcome $Y$ only indirectly through $D$ but not directly.

If all these conditions hold, then $Z$ is a valid IV for estimating the effect of $D$ on $Y$ .

This chapter will provide the traditional econometrics perspective on IV. It is based on linear regression. Imbens and Angrist (1994) and Angrist et al. (1996) made a fundamental contribution by clarifying the connection between

this perspective and the experimental perspective in Chapters 21 and 22. I will start with examples and then give more algebraic details.

# 23.1 Examples of studies with IVs

Finding IV for causal inference is more an art than a science. The algebraic details in later sections are not the most complicated ones in statistics. However, it is fundamentally challenging to find IVs in empirical research. Below are some famous examples.

Example 23.1 In an encouragement design, $Z$ is the randomly assigned treatment, $D$ is the final treatment received, and $Y$ is the outcome. The IV assumptions encoded by Figure 23.1 are plausible in double-blind RCTs as discussed in Chapter 21. This is the ideal case for IV.

Example 23.2 Hearst et al. (1986) reported that men with low lottery numbers in the Vietnam Era draft lottery had higher mortality rates afterward. They attributed this to the negative effect of military service. Angrist (1990) further reported that men with low lottery numbers in the Vietnam Era draft lottery had lower subsequent earnings. He attributed this to the negative effect of military service. These explanations are plausible because the lottery numbers were randomly generated, men with low lottery numbers were more likely to have military service, and the lottery numbers were unlikely to affect the subsequent mortality or earnings. That is, Figure 23.1 is plausible. Angrist et al. (1996) reanalyzed the data using the IV framework. Here, the lottery number is the IV, military service is the treatment, and mortality or earnings is the outcome.

Example 23.3 Angrist and Krueger (1991) studied the return of schooling in years on earnings, using the quarter of birth as an IV. This IV is plausible because of the pseudo-randomization of the quarter of birth. It affected the years of schooling because (1) most states in the U.S. required the students to enter school in the calendar year in which they turned six, and (2) compulsory schooling laws typically required students to remain in school before their sixteenth birthday. More importantly, it is plausible that the quarter of birth did not affect earnings directly.

Example 23.4 Angrist and Evans (1998) studied the effect of family size on mothers' employment and work, using the sibling sex composition as an IV. This IV is plausible because of the pseudo-randomization of the sibling sex composition. Moreover, parents in the U.S. with two children of the same sex are more likely to have a third child than those parents with two children of different sex. It is also plausible that the sibling sex composition does not affect the mother's employment and work directly.

Example 23.5 Card (1993) studied the effect of schooling on wages, using the geographic variation in college proximity as an IV. In particular, $Z$ contains dummy variables for whether a subject grew up near a two-year college or a four-year college. Although this study is classic, it might be a poor example for IV because parents' choices of where to live might not be random, and moreover, where a subject grew up might matter for the subsequent wage.

Example 23.6 Voight et al. (2012) studied the causal effect of plasma high-density lipoprotein (HDL) cholesterol on the risk of heart attack based on Mendelian randomization. They used some single-nucleotide polymorphisms (SNPs) as genetic IV for HDL, which are random with respect to the unmeasured confounders between HDL and heart attack by Mendel's second law, and affect heart attack only through HDL. I will give more details of Mendelian randomization in Chapter 25.

# 23.2 Brief Review of the Ordinary Least Squares

Before discussing the econometric view of IV, I will first review the OLS (see Chapter B). This is a standard topic in statistics. However, it has different mathematical formulations, and the choice of formulation matters for the interpretation.

The first view is based on projection. Given a random variable $Y$ and a random variable or vector $D$ with finite second moments, define the population OLS coefficient as

$$
\begin{array}{l} \beta = \arg \min  _ {b} E (Y - D ^ {\mathsf {T}} b) ^ {2} \\ = E (D D ^ {\intercal}) ^ {- 1} E (D Y), \\ \end{array}
$$

and then define the population residual as $\varepsilon = Y - D^{\top}\beta$ . By definition, $Y$ decomposes into

$$
Y = D ^ {\mathsf {T}} \beta + \varepsilon , \tag {23.1}
$$

which must satisfy

$$
E (D \varepsilon) = 0.
$$

Based on $(D_i,Y_i)_{i=1}^n \stackrel{\mathrm{IID}}{\sim} (D,Y)$ , the OLS estimator of $\beta$ is the moment estimator

$$
\hat {\beta} = \left(\sum_ {i = 1} ^ {n} D _ {i} D _ {i} ^ {\mathsf {T}}\right) ^ {- 1} \sum_ {i = 1} ^ {n} D _ {i} Y _ {i}.
$$

Because

$$
\begin{array}{l} \hat {\beta} = \left(\sum_ {i = 1} ^ {n} D _ {i} D _ {i} ^ {\mathsf {T}}\right) ^ {- 1} \sum_ {i = 1} ^ {n} D _ {i} \left(D _ {i} ^ {\mathsf {T}} \beta + \varepsilon_ {i}\right) \\ = \beta + \left(\sum_ {i = 1} ^ {n} D _ {i} D _ {i} ^ {\mathsf {T}}\right) ^ {- 1} \sum_ {i = 1} ^ {n} D _ {i} \varepsilon_ {i}, \\ \end{array}
$$

we can show that $\hat{\beta}$ is consistent for $\beta$ by the law of large numbers and the fact $E(\varepsilon D) = 0$ . The classic EHW robust variance estimator for $\operatorname{cov}(\hat{\beta})$ is

$$
\hat {V} _ {\mathrm {E H W}} = \left(\sum_ {i = 1} ^ {n} D _ {i} D _ {i} ^ {\mathsf {T}}\right) ^ {- 1} \left(\sum_ {i = 1} ^ {n} \hat {\varepsilon} _ {i} ^ {2} D _ {i} D _ {i} ^ {\mathsf {T}}\right) \left(\sum_ {i = 1} ^ {n} D _ {i} D _ {i} ^ {\mathsf {T}}\right) ^ {- 1}
$$

where $\hat{\varepsilon}_i = Y_i - D_i^\top \hat{\beta}$ is the residual.

The second view is to treat

$$
Y = D ^ {\mathsf {T}} \beta + \varepsilon , \tag {23.2}
$$

as a true model for the data-generating process. That is, given the random variables $(D,\varepsilon)$ , we generate $Y$ based on the linear equation (23.2). Importantly, in the data-generating process, $\varepsilon$ and $D$ may be correlated with $E(D\varepsilon) \neq 0$ . Figure 23.2 gives such an example. This is the fundamental difference compared with the first view where $E(\varepsilon D) = 0$ holds by the definition of the population OLS. Consequently, the OLS estimator can be inconsistent:

$$
\hat {\beta} \rightarrow \beta + E (D D ^ {\intercal}) ^ {- 1} E (D \varepsilon) \neq \beta
$$

in probability, as the sample size $n$ approaches infinity.

I end this section with definitions of endogenous and exogenous regressors based on (23.2), although their definitions are not unique in econometrics.

Definition 23.1 When $E(\varepsilon D) \neq 0$ , the regressor $D$ is called endogenous; when $E(\varepsilon D) = 0$ , the regressor $D$ is called exogenous.

The terminology in Definition 23.1 is standard in econometrics. When $E(\varepsilon D) \neq 0$ , we also say that we have endogeneity; when $E(\varepsilon D) = 0$ , we also say that we have exogeneity.

In the first view of OLS, the notions of endogeneity and exogeneity do not play any roles because $E(\varepsilon D) = 0$ by definition. Statisticians holding the first view usually find the notions of endogeneity and exogeneity strange, and consequently, find the idea of IV unnatural. To understand the econometric view of IV, we must switch to the second view of OLS.

![](images/6072e0ec2ab4c481dff80357851521fbb7a30545d233b1986463e20f76f2f50e.jpg)

![](images/43e2ff3ca3696f824ed8dc387397e022650973edbb5779e5e42b75d345f30226.jpg)  
(a) $E(D\varepsilon)\neq 0$   
(b) marginalized over $\varepsilon$   
FIGURE 23.2: Different representations of the endogenous regressor $D$ . In the upper panel, $U$ represents unmeasured common causes of $D$ and $\varepsilon$ .

# 23.3 Linear Instrumental Variable Model

When $D$ is endogenous, the OLS estimator is inconsistent. We must use additional information to construct a consistent estimator for $\beta$ . I will focus on the following linear IV model:

Definition 23.2 (linear IV model) We have

$$
Y = D ^ {\mathsf {T}} \beta + \varepsilon ,
$$

with

$$
E (\varepsilon Z) = 0. \tag {23.3}
$$

The linear IV model in Definition 23.2 can be illustrated by the following causal graph:

![](images/bf426edf51fb25fcd07fa6b5bcad9056519aedca429bbdf7e8b03ff0f60687c7.jpg)

The above linear IV model allows that $E(\varepsilon D) \neq 0$ but requires an alternative moment condition (23.3). With $E(\varepsilon) = 0$ by incorporating the intercept, the new condition states that $Z$ is uncorrelated with the error term $\varepsilon$ . But any randomly generated noise is uncorrelated with $\varepsilon$ , so an additional condition must hold to ensure that $Z$ is useful for estimating $\beta$ . Intuitively, the additional condition requires that $Z$ is correlated to $D$ , with more technical details stated below.

The mathematical requirement (23.3) seems simple. However, it is a key challenge in empirical research to find such a variable $Z$ that satisfies (23.3). Since the condition (23.3) involves the unobservable $\varepsilon$ , it is generally untestable.

# 23.4 The Just-Identified Case

We first consider the case in which $Z$ and $D$ have the same dimension and $E(ZD^{\mathsf{T}})$ has full rank. The condition $E(\varepsilon Z) = 0$ implies that

$$
E \{Z (Y - D ^ {\intercal} \beta) \} = 0.
$$

Solve the linear equations to obtain

$$
E (Z Y) = E (Z D ^ {\mathsf {T}}) \beta \Longrightarrow \beta = E (Z D ^ {\mathsf {T}}) ^ {- 1} E (Z Y)
$$

if $E(ZD^{\mathsf{T}})$ is not degenerate. The OLS is a special case if $E(\varepsilon D) = 0$ , i.e., $D$ acts as an IV for itself. The resulting moment estimator is

$$
\hat {\beta} _ {\mathrm {I V}} = \left(\sum_ {i = 1} ^ {n} Z _ {i} D _ {i} ^ {\top}\right) ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} Y _ {i}. \tag {23.4}
$$

It can be insightful to work out the details for the case with a scalar $D$ and $Z$ . See Example 23.7 below.

Example 23.7 In the simple case with an intercept and scalar $D$ and $Z$ , we have the model

$$
\left\{ \begin{array}{l} Y = \alpha + \beta D + \varepsilon , \\ E (\varepsilon) = 0, \quad \operatorname {c o v} (\varepsilon , Z) = 0, \end{array} \right.
$$

Under this model, we have

$$
\operatorname {c o v} (Z, Y) = \beta \operatorname {c o v} (Z, D)
$$

which implies

$$
\beta = \frac {\operatorname {c o v} (Z , Y)}{\operatorname {c o v} (Z , D)}.
$$

Standardize the numerator and denominator by $\operatorname{var}(Z)$ to obtain

$$
\beta = \frac {\operatorname {c o v} (Z , Y) / \operatorname {v a r} (Z)}{\operatorname {c o v} (Z , D) / \operatorname {v a r} (Z)},
$$

which equals the ratio between the coefficients of $Z$ in the OLS fits of $Y$ and $D$ .

on $Z$ . If $Z$ is binary, these coefficients are differences in means (see Problem B.2), and $\beta$ reduces to

$$
\beta = \frac {E (Y \mid Z = 1) - E (Y \mid Z = 0)}{E (D \mid Z = 1) - E (D \mid Z = 0)}.
$$

This is identical to the identification formula in Theorem 21.1. That is, with a binary $IVZ$ and a binary treatment $D$ , the IV estimator recovers the CACE under the potential outcomes framework. This is a key result in Imbens and Angrist (1994) and Angrist et al. (1996).

# 23.5 The Over-Identified Case

The discussion in Section 23.4 focuses on the just-identified case. When $Z$ has a lower dimension than $D$ and $E(ZD^{\mathsf{T}})$ does not have full column rank, the equation $E(ZY) = E(ZD^{\mathsf{T}})\beta$ has infinitely many solutions. This is the under-identified case in which the coefficient $\beta$ cannot be uniquely determined even with $Z$ . It is a challenging case beyond the scope of this book. To ensure identifiability, we need at least as many IVs as the endogenous regressors.

When $Z$ has a higher dimension than $D$ and $E(ZD^{\mathsf{T}})$ has full column rank, we have many ways to determine $\beta$ from $E(ZY) = E(ZD^{\mathsf{T}})\beta$ . What is more, the sample analog

$$
n ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} Y _ {i} = n ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} D _ {i} ^ {\mathrm {T}} \beta
$$

may not have any solution because the number of equations is larger than the number of unknown parameters.

A computational trick for the over-identified case is the two-stage least squares (TSLS) estimator (Theil, 1953; Basmann, 1957). It is a clever computational trick, which has two steps.

Definition 23.3 (Two-stage least squares) Define the TSLS estimator of the coefficient of $D$ with $Z$ being the IV as follows.

1. Run OLS of $D$ on $Z$ , and obtain the fitted value $\hat{D}_i$ ( $i = 1, \dots, n$ ). If $D_i$ is a vector, then we need to run component-wise OLS to obtain $\hat{D}_i$ . Put the fitted vectors in a matrix $\hat{D}$ with rows $\hat{D}_i^\top$ ;   
2. Run OLS of $Y$ on $\hat{D}$ , and obtain the coefficient $\hat{\beta}_{\mathrm{TSLS}}$ .

To see why TSLS works, we need more algebra. Write it more explicitly as

$$
\begin{array}{l} \hat {\beta} _ {\text {T S L S}} = \left(\sum_ {i = 1} ^ {n} \hat {D} _ {i} \hat {D} _ {i} ^ {\mathrm {T}}\right) ^ {- 1} \sum_ {i = 1} ^ {n} \hat {D} _ {i} Y _ {i} \tag {23.5} \\ = \left(\sum_ {i = 1} ^ {n} \hat {D} _ {i} \hat {D} _ {i} ^ {\mathsf {T}}\right) ^ {- 1} \sum_ {i = 1} ^ {n} \hat {D} _ {i} \left(D _ {i} ^ {\mathsf {T}} \beta + \varepsilon_ {i}\right) \\ = \left(\sum_ {i = 1} ^ {n} \hat {D} _ {i} \hat {D} _ {i} ^ {\mathsf {T}}\right) ^ {- 1} \sum_ {i = 1} ^ {n} \hat {D} _ {i} D _ {i} ^ {\mathsf {T}} \beta + \left(\sum_ {i = 1} ^ {n} \hat {D} _ {i} \hat {D} _ {i} ^ {\mathsf {T}}\right) ^ {- 1} \sum_ {i = 1} ^ {n} \hat {D} _ {i} \varepsilon_ {i}. \\ \end{array}
$$

The first stage OLS fit ensures $D_{i} = \hat{D}_{i} + \check{D}_{i}$ with orthogonal fitted values and residuals, that is,

$$
\sum_ {i = 1} ^ {n} \hat {D} _ {i} \check {D} _ {i} ^ {\mathrm {T}} = 0 \tag {23.6}
$$

is a zero square matrix with the same dimension as $D_{i}$ . The orthogonality (23.6) implies

$$
\sum_ {i = 1} ^ {n} \hat {D} _ {i} D _ {i} ^ {\intercal} = \sum_ {i = 1} ^ {n} \hat {D} _ {i} \hat {D} _ {i} ^ {\intercal},
$$

which further implies that

$$
\hat {\beta} _ {\text {T S L S}} = \beta + \left(\sum_ {i = 1} ^ {n} \hat {D} _ {i} \hat {D} _ {i} ^ {\mathrm {T}}\right) ^ {- 1} \sum_ {i = 1} ^ {n} \hat {D} _ {i} \varepsilon_ {i}. \tag {23.7}
$$

The first stage OLS fit also ensures

$$
\hat {D} _ {i} = \hat {\Gamma} ^ {\mathsf {T}} Z _ {i} \tag {23.8}
$$

which implies that

$$
\hat {\beta} _ {\mathrm {T S L S}} = \beta + \left\{\hat {\Gamma} ^ {\mathrm {T}} \left(n ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} Z _ {i} ^ {\mathrm {T}}\right) \hat {\Gamma} \right\} ^ {- 1} \hat {\Gamma} ^ {\mathrm {T}} \left(n ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} \varepsilon_ {i}\right). \tag {23.9}
$$

Based on (23.9), we can see the consistency of the TSLS estimator by the law of large numbers and the fact that the term $n^{-1} \sum_{i=1}^{n} Z_i \varepsilon_i$ has probability limit $E(Z\varepsilon) = 0$ . We can also use (23.9) to show that when $Z$ and $D$ have the same dimension, $\hat{\beta}_{\mathrm{TSLS}}$ is numerically identical to $\hat{\beta}_{\mathrm{IV}}$ defined in Section 23.4, which is left as Problem 23.1.

Based on (23.7), we can obtain the standard error as follows. We first obtain the residual $\hat{\varepsilon}_i = Y_i - \hat{\beta}_{\mathrm{TSLS}}^{\mathsf{T}}D_i$ , and then obtain the robust variance estimator as

$$
\hat {V} _ {\mathrm {T S L S}} = \left(\sum_ {i = 1} ^ {n} \hat {D} _ {i} \hat {D} _ {i} ^ {\mathsf {T}}\right) ^ {- 1} \left(\sum_ {i = 1} ^ {n} \hat {\varepsilon} _ {i} ^ {2} \hat {D} _ {i} \hat {D} _ {i} ^ {\mathsf {T}}\right) \left(\sum_ {i = 1} ^ {n} \hat {D} _ {i} \hat {D} _ {i} ^ {\mathsf {T}}\right) ^ {- 1}.
$$

Importantly, the $\hat{\varepsilon}_i$ 's are not the residual from the second stage OLS $Y_{i} - \hat{\beta}_{\mathrm{TSLS}}^{\mathsf{T}}\hat{D}_{i}$ , so $\hat{V}_{\mathrm{TSLS}}$ differs from the robust variance estimator from the second stage OLS.

# 23.6 A Special Case: A Single IV for a Single Endogenous Treatment

This section focuses on a simple case with a single IV and a single endogenous treatment. It has wide applications. Consider the following structural equations:

$$
\left\{ \begin{array}{l} Y _ {i} = \beta_ {0} + \beta_ {1} D _ {i} + \beta_ {2} ^ {\mathrm {T}} X _ {i} + \varepsilon_ {i}, \\ D _ {i} = \gamma_ {0} + \gamma_ {1} Z _ {i} + \gamma_ {2} ^ {\mathrm {T}} X _ {i} + \varepsilon_ {2 i}, \end{array} \right. \tag {23.10}
$$

where $D_{i}$ is a scalar endogenous regressor representing the treatment variable of interest (i.e., $E(\varepsilon_iD_i)\neq 0$ ), $Z_{i}$ is a scalar IV for $D_{i}$ (i.e., $E(\varepsilon_iZ_i) = 0$ ), and $X_{i}$ contains other exogenous regressors (i.e., $E(\varepsilon_iX_i) = 0$ ). This is a special case with $D$ replaced by $(1,D,X)$ and $Z$ replaced by $(1,Z,X)$ .

# 23.6.1 Two-stage least squares

The TSLS estimator in Definition 23.3 simplifies to the following form.

Definition 23.4 (TSLS with a single endogenous regressor) Based on (23.10), the TSLS estimator has the following two steps.

1. Run OLS of $D$ on $(1, Z, X)$ , obtain the fitted values $\hat{D}_i$ ( $i = 1, \ldots, n$ ), and vectorize them as $\hat{D}$ ;   
2. Run OLS of $Y$ on $(1, \hat{D}, X)$ , and obtain the coefficient $\hat{\beta}_{\mathrm{TSLS}}$ and in particular, $\hat{\beta}_{1,\mathrm{TSLS}}$ , the coefficient of $\hat{D}$ .

# 23.6.2 Indirect least squares

The structural equation (23.10) implies

$$
\begin{array}{l} Y _ {i} = \beta_ {0} + \beta_ {1} (\gamma_ {0} + \gamma_ {1} Z _ {i} + \gamma_ {2} ^ {\mathbf {T}} X _ {i} + \varepsilon_ {2 i}) + \beta_ {2} ^ {\mathbf {T}} X _ {i} + \varepsilon_ {i} \\ = \left(\beta_ {0} + \beta_ {1} \gamma_ {0}\right) + \beta_ {1} \gamma_ {1} Z _ {i} + \left(\beta_ {2} + \beta_ {1} \gamma_ {2}\right) ^ {\mathsf {T}} X _ {i} + \left(\varepsilon_ {i} + \beta_ {1} \varepsilon_ {2 i}\right). \\ \end{array}
$$

Define $\Gamma_0 = \beta_0 + \beta_1\gamma_0, \Gamma_1 = \beta_1\gamma_1, \Gamma_2 = \beta_2 + \beta_1\gamma_2$ , and $\varepsilon_{1i} = \varepsilon_i + \beta_1\varepsilon_{2i}$ . We have the following equations

$$
\left\{ \begin{array}{l} Y _ {i} = \Gamma_ {0} + \Gamma_ {1} Z _ {i} + \Gamma_ {2} ^ {\top} X _ {i} + \varepsilon_ {1 i}, \\ D _ {i} = \gamma_ {0} + \gamma_ {1} Z _ {i} + \gamma_ {2} ^ {\top} X _ {i} + \varepsilon_ {2 i}, \end{array} \right. \tag {23.11}
$$

which is called the reduced form, in contrast to the structural form in (23.10). The parameter of interest equals the ratio of two coefficients

$$
\beta_ {1} = \Gamma_ {1} / \gamma_ {1}.
$$

In the reduced form, the left-hand side are dependent variables $Y$ and $D$ , and the right-hand side are the exogenous variable $Z$ and $X$ satisfying

$$
E (Z \varepsilon_ {1 i}) = E (Z \varepsilon_ {2 i}) = 0, \quad E (X \varepsilon_ {1 i}) = E (X \varepsilon_ {2 i}) = 0.
$$

More importantly, OLS gives consistent estimators for the coefficients in the reduced form (23.11).

The reduced form (23.11) suggests that the ratio of two OLS coefficients $\hat{\Gamma}_1$ and $\hat{\gamma}_1$ is a reasonable estimator for $\beta_1$ . This is called the indirect least squares (ILS) estimator:

$$
\hat {\beta} _ {1, \mathrm {I L S}} = \hat {\Gamma} _ {1} / \hat {\gamma} _ {1}.
$$

Interestingly, it is numerically identical to the TSLS estimator under (23.10).

Theorem 23.1 With a single endogenous treatment and a single IV in (23.10), we have

$$
\hat {\beta} _ {1, \mathrm {I L S}} = \hat {\beta} _ {1, \mathrm {T S L S}}.
$$

Theorem 23.1 is an algebraic fact. Imbens (2014, Section A.3) pointed it out without giving a proof. I relegate its proof to Problem 23.2. The ratio formula makes it clear that the TSLS estimator has poor finite sample properties with a weak instrument variable, i.e., $\gamma_{1}$ is close to zero.

# 23.6.3 Weak IV

The following inferential procedure is simpler, more transparent, and more robust to weak IV. It is more computationally intensive though. The reduced form (23.11) also implies that

$$
Y _ {i} - b D _ {i} = (\Gamma_ {0} - b \gamma_ {0}) + (\Gamma_ {1} - b \gamma_ {1}) Z _ {i} + (\Gamma_ {2} - b \gamma_ {2}) ^ {\mathsf {T}} X _ {i} + (\varepsilon_ {1 i} - b \varepsilon_ {2 i}) (2 3. 1 2)
$$

for any $b$ . At the true value $b = \beta_{1}$ , the coefficient of $Z_{i}$ must be 0. This simple fact suggests a confidence interval for $\beta_{1}$ by inverting tests for $H_{0}(b):\beta_{1} = b$ :

$$
\left\{b: | t _ {Z} (b) | \leq z _ {1 - \alpha / 2} \right\},
$$

where $t_Z(b)$ is the $t$ -statistic for the coefficient of $Z$ based on the OLS fit of (23.12) with the EHW standard error, and $z_{1 - \alpha / 2}$ is the $1 - \alpha / 2$ upper quantile of the standard Normal random variable. This confidence interval is more robust than the Wald-type confidence interval based on the TSLS estimator. It is similar to the FAR confidence set discussed in Chapter 21. This procedure makes the TSLS estimator unnecessary. What is more, we only need to run the OLS fit of $Y$ based on the reduced form if the goal is to test $\beta_1 = 0$ under (23.10).

# 23.7 Application

Revisit Example 23.5. Card (1993) used the National Longitudinal Survey of Young Men to estimate the causal effect of education on earnings. The data set contains 3010 men with ages between 14 and 24 in the year 1966, and Card (1993) leveraged the geographic variation in college proximity as an IV for education. Here, $Z$ is the indicator of growing up near a four-year college, $D$ measures the years of education, and the outcome $Y$ is the log wage in the year 1976, ranging from 4.6 to 7.8. Additional covariates are race, age, and squared age, a categorical variable indicating living with both parents, single mom, or both parents, and variables summarizing the living areas in the past.

```txt
> library("car")
> ## Card Data
> card.data = read.csv("card1995.csv")
> Y = card.data[, "lwage"]
> D = card.data[, "educ"]
> Z = card.data[, "nearc4"]
> X = card.data[, c("exper", "expersq", "black", "south",
+     "smsa", "reg661", "reg662", "reg663",
+     "reg664", "reg665", "reg666",
+     "reg667", "reg668", "smsa66")] 
```

Based on TSLS, we can obtain the following the point estimator and $95\%$ confidence interval.

```txt
> Dhat = lm(D ~ Z + X) $fitted.values
> tslsreg = lm(Y ~ Dhat + X)
> tslsest = coef(tslsreg)[2]
> ## correct se by changing the residuals
> res.correct = Y - cbind(1, D, X) %*%coef(tslsreg)
> tslsreg$residuals = as.vector(res.correct)
> tslsse = sqrt(hccm(tslsreg, type = "hc0") [2, 2])
> res = c(tslsest, tslsest - 1.96*tlsse, tslsest + 1.96*tlsse)
> names(res) = c("TSLS", "lower CI", "upper CI")
> round(res, 3)
TSLS lower CI upper CI
0.132 0.026 0.237 
```

Using the strategy of the FAR confidence set, we can compute $p$ -value as a function of $b$ .

```txt
> BetaAR = seq(-0.1, 0.4, 0.001)  
> PvalueAR = sapply(BetaAR, function(b){ + Y_b = Y - b*D + ARreg = lm(Y_b ~ Z + X) + coefZ = coef(ARreg)[2] + seZ = sqrt(hccm(ARreg)[2, 2]) 
```

```txt
+ Tstat = coefZ/seZ
+ (1 - pnorm(abs(Tstat))) * 2
+ }) 
```

Figure 23.3 shows the $p$ -values for a sequence of tests for the coefficient of $D$ based on following R code:

```txt
> plot(PvalueAR ~ BetaAR, type = "l",
+ xlab = "coefficient of D",
+ ylab = "p-value",
+ main = "Fieller-Anderson-Rubin interval based on Card's data")
> point.est = BetaAR[which.max(PvalueAR)]
> abline(h = 0.05, lty = 2, col = "grey")
> abline(v = point.est, lty = 2, col = "grey")
> ARCI = range(BetaAR[PvalueAR >= 0.05])
> abline(v = ARCI[1], lty = 2, col = "grey")
> abline(v = ARCI[2], lty = 2, col = "grey") 
```

We report the point estimate as the value of $b$ with the largest $p$ -value as well as the confidence interval as the region of $b$ with $p$ -values larger than 0.05.

```txt
> FARres = c(point.est, ARCI)  
> names(FARres) = c("FAR est", "lower CI", "upper CI")  
> round(FARres, 3)  
    FAR est lower CI upper CI
0.132 0.028 0.282 
```

Comparing the TSLS and FAR methods, the lower confidence limits are very close but the upper confidence limits are slightly different due to the possibly heavy right tail of the distribution of the TSLS estimator. Overall, the TSLS and FAR methods give similar results in this example because the IV is not weak.

# 23.8 Homework

23.1 More algebra for TSLS in Section 23.5

1. Show that the $\hat{\Gamma}$ in (23.8) equals

$$
\hat {\Gamma} = \left(\sum_ {i = 1} ^ {n} Z _ {i} Z _ {i} ^ {\mathrm {T}}\right) ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} D _ {i} ^ {\mathrm {T}}.
$$

2. Show $\hat{\beta}_{\mathrm{TSLS}}$ defined in (23.5) reduces to $\hat{\beta}_{\mathrm{IV}}$ defined in (23.4) if $Z$ and $D$ have the same dimension and

$$
n ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} Z _ {i} ^ {\mathsf {T}}, \quad n ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} D _ {i} ^ {\mathsf {T}}
$$

![](images/4ab8d804458f28f99e001d04c337e31c36dda5acc9546f06be09b770cbc83eae.jpg)  
Fieller-Anderson-Rubin interval based on Card's data   
FIGURE 23.3: Re-analysis of Card (1993)'s data by inverting tests

are both invertible.

# 23.2 Equivalence between TSLS and ILS

Prove Theorem 23.1.

Remark: Use the FWL theorem in Chapter B.

# 23.3 Control function in the linear instrumental variable model

Definition 23.5 below parallels Definition 23.3 above.

Definition 23.5 (control function) Define the control function estimator $\hat{\beta}_{\mathrm{CF}}$ as follows.

1. Run OLS of $D$ on $Z$ , and obtain the residuals $\check{D}_i$ ( $i = 1, \dots, n$ ). If $D_i$ is a vector, then we need to run component-wise OLS to obtain $\check{D}_i$ . Put the residual vectors in a matrix $\check{D}$ with rows $\check{D}_i^\top$ ;   
2. Run OLS of $Y$ on $D$ and $\tilde{D}$ , and obtain the coefficient of $D$ , $\hat{\beta}_{\mathrm{CF}}$ .

Show that $\hat{\beta}_{\mathrm{CF}} = \hat{\beta}_{\mathrm{TLS}}$

Remark: To prove the result, you can use the results in Problems B.4 and B.5. In Definition 23.5, $\check{D}$ from Step 1 is called the control function for Step 2. Hausman (1978) pointed out this result. Wooldridge (2015) provided a more general discussion of the control function methods in more complex models.

# 23.4 Data analysis: Efron and Feldman (1991)

Efron and Feldman (1991) was one of the early studies dealing with noncompliance under the potential outcomes framework. The original randomized experiment, the Lipid Research Clinics Coronary Primary Prevention Trial (LRC-CPPT), was designed to evaluate the effect of the drug cholestyramine on cholesterol levels. In the dataset EF.csv, the first column contains the binary indicators for treatment and control, the second column contains the proportions of the nominal cholestyramine dose actually taken, and the last three columns are cholesterol levels. Note that the individuals did not know whether they were assigned to cholestyramine or to the placebo, but differences in adverse side effects could induce differences in compliance behavior by treatment status. All individuals were assigned the same nominal dose of the drug or placebo, for the same time period. Column 3, $C_3$ , was taken before communication about the benefits of a low-cholesterol diet, Column 4, $C_4$ , was taken after this suggestion, but before the random assignment to cholestyramine or placebo, and Column 5, $C_5$ , an average of post-randomization cholesterol readings, averaged over two-month readings for a period of time averaging 7.3 years for all the individuals in the study. Efron and Feldman (1991) used the change in cholesterol level as the final outcome of interest, defined as $C_5 - 0.25C_3 - 0.75C_4$ . Their original paper contains more detailed descriptions.

The data structure here is more complicated than the noncompliance problem discussed in Chapters 21 and 22. Jin and Rubin (2008) re-analyzed the data based on the idea in Chapter 26 later. You can analyze the data based on your understanding of the problem, but you need to justify your choice of the method. There is no gold-standard solution for this problem.

# 23.5 Recommended reading

Imbens (2014) gave an econometrician's perspective of IV.

# Application of the Instrumental Variable Method: Fuzzy Regression Discontinuity

The regression discontinuity method introduced in Chapter 20 and the IV method introduced in Chapters 21-23 are two important examples of natural experiments. The study designs are not as ideal as randomized experiments in Part II, but they have features similar to randomized experiments. That's why they are called natural experiments.

Compounding the regression discontinuity method with the IV method yields the fuzzy regression discontinuity method, another important natural experiment. I will start with examples and then provide a mathematical formulation.

# 24.1 Motivating examples

Chapter 20 introduces the regression discontinuity method. The following three examples are slightly different because the treatments received are not deterministic functions of the running variables. Rather, the running variables discontinuously change the probabilities of the treatments received at the cutoff points.

Example 24.1 In 2000, the Government of India launched the Prime Minister's Village Road Program, and by 2015, this program had funded the construction of all-weather roads to nearly 200,000 villages. Based on village-level data, Asher and Novosad (2020) use the regression discontinuity method to estimate the effect of new feeder roads on various economic variables. The national program guidelines prioritized larger villages according to arbitrary thresholds based on the 2001 Population Census. The treatment variable equals 1 if the village received a new road before the year in which the outcomes were measured. The difference between the population size of a village and the threshold did not determine the treatment variable but affected its probability discontinuously at the cutoff point 0.

Example 24.2 Li et al. (2015) used the data on the first-year students enrolled in 2004 to 2006 from two Italian universities to evaluate the causal effect

of a university grant on the dropout rate. The students were eligible for this grant if their standardized family income was below 15,000 euros. For simplicity, we use the running variable defined as 15,000 minus the standardized family income. To receive this grant, the students must apply first. Therefore, the eligibility and the application status jointly determined the final treatment status. The running variable alone did not determine the treatment status although it changed the treatment probability at the cutoff point 0.

Example 24.3 Amarante et al. (2016) estimated the impact of in-utero exposure to a social assistance program on children's birth outcomes. They used a regression discontinuity induced by the Uruguayan Plan de Atencion Nacional a la Emergencia Social. It was a temporary social assistance program targeted to the poorest 10 percent of households, implemented between April 2005 and December 2007. Households with a predicted low-income score below a predetermined threshold were assigned to the program. The predicted income score did not determine whether the mother received at least one program transfer during the pregnancy but it changed the probability of the final treatment received. The birth outcomes included birth weight, weeks of gestation, etc.

The above examples are called fuzzy regression discontinuity in contrast to the (sharp) regression discontinuity in Chapter 20. I will analyze the data in Examples 24.1 and 24.2 in Chapter 24.3 below.

# 24.2 Mathematical formulation

Let $X_{i}$ denote the running variable which determines

$$
Z _ {i} = I (X _ {i} \geq x _ {0})
$$

with the cutoff point $x_0$ . The treatment received $D_i$ may not equal $Z_i$ , but $\operatorname{pr}(D_i = 1 \mid X_i = x)$ has a jump at $x_0$ . Figure 24.1 compares the treatment received probabilities of the sharp regression discontinuity and fuzzy regression discontinuity. It shows a special case of fuzzy regression discontinuity with $\operatorname{pr}(D = 1 \mid X < x_0) = 0$ , which is coherent to Example 24.2.

Let $Y_{i}$ denote the outcome of interest. Viewing $Z_{i}$ as the treatment assigned, we can define potential outcomes $\{D_{i}(1), D_{i}(0), Y_{i}(1), Y_{i}(0)\}$ . The sharp regression discontinuity of $Z$ allows for the identification of

$$
\begin{array}{l} \tau_ {D} (x _ {0}) = E \{D (1) - D (0) \mid X = x _ {0} \} \\ = \lim  _ {\varepsilon \rightarrow 0 +} E (D \mid Z = 1, X = x _ {0} + \varepsilon) - \lim  _ {\varepsilon \rightarrow 0 +} E (D \mid Z = 0, X = x _ {0} - \varepsilon) \\ \end{array}
$$

and

$$
\begin{array}{l} \tau_ {Y} (x _ {0}) = E \{Y (1) - Y (0) \mid X = x _ {0} \} \\ = \lim  _ {\varepsilon \rightarrow 0 +} E (Y \mid Z = 1, X = x _ {0} + \varepsilon) - \lim  _ {\varepsilon \rightarrow 0 +} E (Y \mid Z = 0, X = x _ {0} - \varepsilon) \\ \end{array}
$$

![](images/71477e534d616128261cf8ffc46e95c2d2fe34c7043059c72d78650960e10927.jpg)

![](images/c8ad06c50466b219d9bdc76ae75c3a60a7b884d01fabd87e33fb846fe3799983.jpg)  
FIGURE 24.1: The treatment assignments of sharp regression discontinuity (left) and fuzzy regression discontinuity (right)

based on Theorem 20.2. Using $Z$ as an IV for $D$ and imposing the IV assumptions at $X = x_0$ , we can identify the local complier average causal effect by applying Theorem 21.1.

Theorem 24.1 Assume that the treatment is determined by $Z = I(X \geq x_0)$ where $x_0$ is a predetermined threshold. Assume monotonicity

$$
D _ {i} (1) \geq D _ {i} (0)
$$

and exclusion restriction

$$
D _ {i} (1) = D _ {i} (0) \Longrightarrow Y _ {i} (1) = Y _ {i} (0)
$$

in the infinitesimal neighborhood of $x_0$ . The local complier average causal effect, defined as

$$
\tau_ {\mathrm {c}} (x _ {0}) = E \left\{Y (1) - Y (0) \mid D (1) > D (0), X = x _ {0} \right\},
$$

can be identified by

$$
\tau_ {\mathrm {c}} (x _ {0}) = \frac {E \{Y (1) - Y (0) \mid X = x _ {0} \}}{E \{D (1) - D (0) \mid X = x _ {0} \}}.
$$

Further assume that $E\{D(1) \mid X = x\}$ and $E\{Y(1) \mid X = x\}$ are continuous from the right at $x = x_0$ , and $E\{D(0) \mid X = x\}$ and $E\{Y(0) \mid X = x\}$ are continuous from the left at $x = x_0$ . The local complier average causal effect can be identified by

$$
\tau_ {\mathrm {c}} (x _ {0}) = \frac {\lim  _ {\varepsilon \rightarrow 0 +} E (Y \mid Z = 1 , X = x _ {0} + \varepsilon) - \lim  _ {\varepsilon \rightarrow 0 +} E (Y \mid Z = 0 , X = x _ {0} - \varepsilon)}{\lim  _ {\varepsilon \rightarrow 0 +} E (D \mid Z = 1 , X = x _ {0} + \varepsilon) - \lim  _ {\varepsilon \rightarrow 0 +} E (D \mid Z = 0 , X = x _ {0} - \varepsilon)}
$$

if $E(D \mid X = x)$ has a non-zero jump at $x = x_0$ .

Theorem 24.1 is a superposition of Theorems 20.2 and 21.1. I leave its proof as Problem 24.1.

# 33224 Application of the Instrumental Variable Method: Fuzzy Regression Discontinuity

In both sharp and fuzzy regression discontinuity, the key is to specify the neighborhood around the cutoff point. Practically, a smaller neighborhood leads to a smaller bias but a larger variance, while a larger neighborhood leads to a larger bias but a smaller variance. That is, we face a bias-variance trade-off. Some automatic procedures exist based on some statistical criteria, which rely on some strong conditions. It seems wiser to conduct sensitivity analysis over a range of the choice of the neighborhood.

Assume that we have specified the neighborhood of $x_0$ determined by a bandwidth $h$ . For data with $X_i \in [x_0 - h, x_0 + h]$ , we can estimate $\tau_D(x_0)$ by

$\hat{\tau}_D(x_0) =$ the coefficient of $Z_{i}$ in the OLS fit of $D_{i}$ on $\{1,Z_i,R_i,L_i\}$

and estimate $\tau_{Y}(x_{0})$

$\hat{\tau}_{Y}(x_{0}) =$ the coefficient of $Z_{i}$ in the OLS fit of $Y_{i}$ on $\{1,Z_i,R_i,L_i\}$

recalling the definitions $R_{i} = \max (X_{i} - x_{0},0)$ and $L_{i} = \min (X_{i} - x_{0},0)$ . Then we can estimate the local complier average causal effect by

$$
\hat {\tau} _ {\mathrm {c}} (x _ {0}) = \hat {\tau} _ {Y} (x _ {0}) / \hat {\tau} _ {D} (x _ {0}).
$$

This is an indirect least squares estimator. By Theorem 23.1, it is numerically identical to

the coefficient of $D_{i}$ in the TSLS fit of $Y_{i}$ on $\{1, D_{i}, R_{i}, L_{i}\}$

with $D_{i}$ instrumented by $Z_{i}$ . In sum, after specifying $h$ , the estimation of $\tau_{\mathrm{c}}(x_0)$ reduces to a TSLS procedure with the local data around the cutoff point.

# 24.3 Application

# 24.3.1 Re-analyzing Asher and Novosad (2020)'s data

Revisit Example 24.1. We can compute the point estimates and standard errors for a sequence of $h$ based on the outcome occupation_index_andrsn.

library("car")
road_dat = read.csv("indianroad.csv")
table(road_dat\ $t, road_dat\$ r2012)
road_dat\$runv $=$ road_dat\$left + road_dat\$right
## sensitivity analysis
seq.h $=$ seq(10, 80, 1)
frd.sa $=$ lapply(seq.h, function(h){road_sub $=$ subset(road_dat, abs(runv) $<=h)$ road_sub\$r2012hat $=$ lm(r2012 ~ t + left + right,

# 24.3 Application

```txt
data = road_sub)\\(fitted.values
tslsreg \(=\) lm(occupation_index_andrsn ~ r2012hat + left + right,
	data \(=\) road_sub)
res \(=\) with(road_sub,
{
	occupation_index_andrsn -
	embed(1, r2012, left, right) \(\% \%\) coef(tslsreg)
})
tslsreg\\(residuals \(=\) as.vector(res)
c(coef(tslsreg)[2],
	sqrt(hccm(tslsreg, type \(=\) "hc2")[2, 2]),
length(res))
}
frd.sa \(=\) do.call(rbind, frd.sa) 
```

Figure 24.2 shows the results. The treatment effect is not significant unless $h$ is large.

The package rdrobust selects the bandwidth automatically. The results suggest that receiving a new road did not affect the outcome significantly.

```diff
> library("rdrobust")
> frd_road = with(road_dat,
+     {
+         rdrobust(y = occupation_index_andrsn,
+             x = runv,
+                 c = 0,
+                 fuzzy = r2012)
+         }) > res = cbind(frd_road$coef, frd_road$se)
> round(res, 3)
Coeff Std. Err.
Conventional -0.253 0.301
Bias-Corrected -0.283 0.301
Robust -0.283 0.359 
```

# 24.3.2 Re-analyzing Li et al. (2015)'s data

Revisit Example 24.2. Recall that the running variable is 15,000 minus the standardized income. In the analysis, I restrict the data to a subset with this running between $[-5,000,5,000]$ , and then divide the running variable by 5,000 so that the running variable is bounded between $[-1,1]$ at cutoff point zero. We can compute the point estimates and standard errors for a sequence of $h$ .

```txt
library("car")
italy = read.csv("italy.csv")
italy\(left = pmin(italy\)rv0, 0)
italy\)right = pmax(italy\)rv0, 0) 
```

![](images/1d94f4eae0d6ecfd7096d5904da141185b243af86c085e3d9b3db96a71197304.jpg)

![](images/c5a18b79df1bfc25ca52cb96a824ac6f1ba086854c96426e9e86788fcb9cbf2f.jpg)  
FIGURE 24.2: Re-analyzing Asher and Novosad (2020)'s data, with point estimates and standard errors from TSLS.

24.4 Discussion   
```r
## sensitivity analysis
seq.h = seq(0.1, 1, 0.01)
frd(sa = lapply(seq.h, function(h) {
    italy_sub = subset(italy, abs(rv0) <= h)
    italy_sub$Dhat = lm(D ~ Z + left + right,
        data = italy_sub)$fitted.values
    tslsreg = lm(outcome ~ Dhat + left + right,
        data = italy_sub)
    res = with(italy_sub,
        {
            outcome -
                cbind(1, D, left, right) %**coef(tslsreg))
        }
    tslsreg$residuals = as.vector(res)
    c(coef(tslsreg)[2],
        sqrt(hccm(tslsreg, type = "hc2") [2, 2]),
        length(res))
}) 
frd(sa = do.call(rbind, frd(sa) 
```

Figure 24.3 shows the results and suggests that the university grant did not affect the dropout rate significantly.

The results based on the package rdrobust reach the same conclusion.

```txt
> library("rdrobust")
> frd_italy = with(italy, + { + rdrobust(y = outcome, + x = rv0, + c = 0, + fuzzy = D) + }) > res = cbind(frd_italy$coef, frd_italy$se) > round(res, 3) Coeff Std. Err. Conventional -0.149 0.101 Bias-Corrected -0.155 0.101 Robust -0.155 0.121 
```

# 24.4 Discussion

Both Chapter 20 and this chapter formulate regression discontinuity based on the continuity of the conditional expectations of the potential outcomes given the running variables. This perspective is mathematically simpler but it only

![](images/d9fae0ae85291a3f51e0bf8e15e84922cb9d9cbb80d1d51932f54aded8f53091.jpg)

![](images/6ed5980e73904276286c444f4acb6c9a9c785519fb99f432bb3be2723e58b175.jpg)  
FIGURE 24.3: Re-analyzing Li et al. (2015)'s data, with point estimates and standard errors from TSLS.

identifies the local effects precisely at the cutoff point of the running variable. Hahn et al. (2001) started this line of literature.

An alternative, not so dominant perspective is based on local randomization (Cattaneo et al., 2015; Li et al., 2015). If we view the running variable as a noisy measure of some underlying truth and the cutoff point is somewhat arbitrarily chosen, the units near the cutoff point do not differ systematically. This suggests that in a small neighborhood of the cutoff point, the units receive the treatment and the control in a random fashion just as in a randomized experiment. Similar to the issue of choosing $h$ in the first perspective, it is crucial to decide how local should the randomized experiment be under the regression discontinuity. It is not easy to quantify the intuition mathematically, and again conducting sensitivity analysis with a range of $h$ seems a reasonable approach in the second perspective as well.

See Sekhon and Titiunik (2017) for a more conceptual discussion of regression discontinuity.

# 24.5 Homework Problems

# 24.1 Proof of Theorem 24.1

Prove Theorem 24.1.

# 24.2 Data analysis

Section 24.3.1 reports the estimate of the effect on occupation_index_andrsn. Four other outcome variables are transport_index_andrsn, firms_index_andrsn, consumption_index_andrsn, and agriculture_index_andrsn, with meanings defined in the original paper. Estimate the effects on these outcomes.

# 24.3 Reflection on the analysis of Li et al. (2015)'s data

In Li et al. (2015), a key variable determining the treatment status is the binary application status $A$ , which has potential outcomes $A(1)$ and $A(0)$ corresponding to the treatment $Z = 1$ and control $Z = 0$ . By definition,

$$
D (1) = A (1), \quad D (0) = 0,
$$

so the compliers $\{D(1), D(0)\} = (1, 0)$ is equivalent to $A(1) = 1$ . So

$$
\tau_ {\mathrm {c}} (x _ {0}) = E \left\{Y (1) - Y (0) \mid A (1) = 1, X = x _ {0} \right\}.
$$

Section 24.3.2 used the whole data set to estimate $\tau_{\mathrm{c}}(x_0)$

An alternative analysis is to use the units with $A = 1$ only. Then the treatment status is determined by $X$ . However, this analysis can be problematic

# 33824 Application of the Instrumental Variable Method: Fuzzy Regression Discontinuity

because

$$
\begin{array}{l} \lim  _ {\varepsilon \rightarrow 0 +} E \left\{Y \mid A = 1, X = x _ {0} + \varepsilon \right\} - \lim  _ {\varepsilon \rightarrow 0 +} E \left\{Y \mid A = 1, X = x _ {0} - \varepsilon \right\} \\ = E \left\{Y (1) \mid A (1) = 1, X = x _ {0} \right\} - E \left\{Y (0) \mid A (0) = 1, X = x _ {0} \right\}. \tag {24.1} \\ \end{array}
$$

Prove (24.1) and explain why this analysis can be problematic.

Remark: The left-hand side of (24.1) is the identification formula of the local average treatment effect at $X = x_0$ , conditional on $A = 1$ . The right-hand side of (24.1) is the difference in means of the potential outcomes for the subgroups of units with $(A(1) = 1, X = x_0)$ and $(A(0) = 1, X = x_0)$ , respectively. See Chapter 26 later for related discussions.

# 24.4 Recommended reading

Imbens and Lemieux (2008) gave practical guidance to regression discontinuity based on the potential outcomes framework. Lee and Lemieux (2010) reviewed regression discontinuity and its applications in economics.

# Application of the Instrumental Variable Method: Mendelian Randomization

Katan (1986) was concerned with the observational studies suggesting that low serum cholesterol levels were associated with the risk of cancer. As we have discussed, however, observational studies suffer from unmeasured confounding. Consequently, it is difficult to interpret the observed association as causality. In the particular problem studied by Katan (1986), it is even possible that early stages of cancer reversely cause low serum cholesterol levels. Disentangling the causal effect of the serum cholesterol level on cancer seems a hard problem using standard epidemiologic studies. Katan (1986) argued that Apolipoprotein E genes are associated with serum cholesterol levels but do not directly affect the cancer status. So if low serum cholesterol levels cause cancer, we should observe differences in cancer risks among people with and without the genotype that leads to different serum cholesterol levels. Using our language for causal inference, Katan (1986) proposed to use Apolipoprotein E genes as IVs.

Katan (1986) did not conduct any data analysis but just proposed a conceptual design that could address not only unmeasured confounding but also reverse causality. Since then, more complicated and sophisticated studies have been conducted thanks to the modern genome-wide association studies. These studies used genetic information as IVs for exposures in epidemiologic studies to estimate the causal effects of exposures on outcomes. They were all motivated by Mendel's second law, the law of random assortment, which suggests that the inheritance of one trait is independent of the inheritance of other traits. Therefore, the method of using genetic information as IV is called Mendelian Randomization (MR).

# 25.1 Background and motivation

Graphically, Figure 25.1 shows the causal diagram on the treatment $D$ , outcome $Y$ , unmeasured confounder $U$ , as well as the genetic IVs $G_{1},\ldots ,G_{p}$ . In many MR studies, the genetic IVs are single nucleotide polymorphisms

![](images/a0e4352e618836b40ec63ce8c8c0b40f86ef3617f3b315d2b80729c1267a51a6.jpg)  
FIGURE 25.1: Causal graph for MR

(SNPs). Because of pleiotropy, ${}^{1}$ it is possible that the genetic IVs have a direct effect on the outcome of interest, so Figure 25.1 also allows for the violation of the exclusion restriction assumption.

The standard linear IV model assumes away the direct effect of the IVs on the outcome. Definition 25.1 below gives both the structural and reduced forms.

Definition 25.1 (linear IV model) The standard linear IV model

$$
Y = \beta_ {0} + \beta D + \beta_ {u} U + \varepsilon_ {Y}, \tag {25.1}
$$

$$
D = \gamma_ {0} + \gamma_ {1} G _ {1} + \dots + \gamma_ {p} G _ {p} + \gamma_ {u} U + \varepsilon_ {D}, \tag {25.2}
$$

has reduced form

$$
Y = \beta_ {0} + \beta \gamma_ {0} + \beta \gamma_ {1} G _ {1} + \dots + \beta \gamma_ {p} G _ {p} + \left(\beta_ {u} + \beta_ {0} \gamma_ {u}\right) U + \varepsilon_ {Y}, \tag {25.3}
$$

$$
D = \gamma_ {0} + \gamma_ {1} G _ {1} + \dots + \gamma_ {p} G _ {p} + \gamma_ {u} U + \varepsilon_ {D}, \tag {25.4}
$$

Definition 25.2 below allows for the violation of exclusion restriction. Then, $G_{1}, \ldots, G_{p}$ are not valid IVs.

Definition 25.2 (linear model with possibly invalid IVs) The linear model

$$
Y = \beta_ {0} + \beta D + \alpha_ {1} G _ {1} + \dots + \alpha_ {p} G _ {p} + \beta_ {u} U + \varepsilon_ {Y}, \tag {25.5}
$$

$$
D = \gamma_ {0} + \gamma_ {1} G _ {1} + \dots + \gamma_ {p} G _ {p} + \gamma_ {u} U + \varepsilon_ {D}, \tag {25.6}
$$

has reduced form

$$
\begin{array}{l} Y = (\beta_ {0} + \beta \gamma_ {0}) + (\alpha_ {1} + \beta \gamma_ {1}) G _ {1} + \dots + (\alpha_ {p} + \beta \gamma_ {p}) G _ {p} \\ + \left(\beta_ {u} + \beta \gamma_ {u}\right) U + \varepsilon_ {Y}, \tag {25.7} \\ \end{array}
$$

$$
D = \gamma_ {0} + \gamma_ {1} G _ {1} + \dots + \gamma_ {p} G _ {p} + \gamma_ {u} U + \varepsilon_ {D}. \tag {25.8}
$$

Definitions 25.1 and 25.2 are slightly different from the linear IV model in Chapter 23. They include the confounder $U$ explicitly. But this slight difference does not change the discussion fundamentally.

In Definition 25.1 with exclusion restriction, we have

$$
\Gamma_ {j} = \beta \gamma_ {j}, \quad (j = 1, \dots , p).
$$

In Definition 25.2 without exclusion restriction, we have

$$
\Gamma_ {j} = \alpha_ {j} + \beta \gamma_ {j}, \quad (j = 1, \dots , p).
$$

If we have individual data, we can apply the classic TSLS estimator to estimate $\beta$ under the linear IV model in Definition 25.1. However, most MR studies do not have individual data but rather summary statistics from multiple genome-wide association studies. A canonical MR study with summary statistics has the following data structure.

Assumption 25.1 (MR study with summary statistics) (a) We have the regression coefficients of the treatment on the genetic IVs $\hat{\gamma}_1, \dots, \hat{\gamma}_p$ as well as the standard errors $\mathrm{se}_{D1}, \dots, \mathrm{se}_{Dp}$ . Assume

$$
\hat {\gamma} _ {1} \rightarrow \gamma_ {1}, \dots , \hat {\gamma} _ {p} \rightarrow \gamma_ {p} \tag {25.9}
$$

in probability, and ignore the uncertainty in the standard errors.

(b) We have the regression coefficients of the outcome on the genetic IVs $\hat{\Gamma}_1, \dots, \hat{\Gamma}_p$ as well as with standard errors $\mathrm{se}_{Y1}, \dots, \mathrm{se}_{Yp}$ . Assume

$$
\hat {\Gamma} _ {1} \rightarrow \Gamma_ {1}, \dots , \hat {\Gamma} _ {p} \rightarrow \Gamma_ {p} \tag {25.10}
$$

in probability, and ignore the uncertainty in the standard errors.

(c) Assume $\hat{\gamma}_1, \dots, \hat{\gamma}_p, \hat{\Gamma}_1, \dots, \hat{\Gamma}_p$ are jointly Normal and independent.

The asymptotic Normality of the regression coefficients can be justified by the CLT. The standard errors are accurate estimates of the true standard errors in large samples. Therefore, the only subtle assumption is the joint independence of the regression coefficients. The independence of the $\hat{\gamma}_j$ 's and the $\hat{\Gamma}_j$ 's are reasonable because they are often calculated based on different samples.

The independence among the $\hat{\gamma}_j$ 's can be reasonable if the $G_{j}$ 's are independent and the true linear model for $D$ holds with homoskedastic error terms. See Chapter B.4. However, this assumption can be tricky if the error

term of the linear model is heteroskedastic. Without the independence of the $G_{j}$ 's, it is hard to justify the independence. If the regression coefficients are from nonlinear models, then it is even harder to justify the independence. The independence among the $\hat{\Gamma}_{j}$ 's follows from a similar argument.

This chapter focuses on the statistical inference of $\beta$ based on the above summary statistics in Assumption 25.1.

# 25.2 MR based on summary statistics

# 25.2.1 Fixed-effect estimator

Under Definition 25.1, $\alpha_{j} = 0$ which implies that $\beta = \Gamma_{j} / \gamma_{j}$ for all $j$ . A simple approach is based on the so-called meta-analysis (Bowden et al., 2018), that is, combining multiple estimates $\hat{\beta}_{j} = \hat{\Gamma}_{j} / \hat{\gamma}_{j}$ for the common parameter $\beta$ , also called the fixed effect. Using delta method (see Example A.3), the ratio estimator $\hat{\beta}_{j}$ has approximate squared standard error

$$
\mathrm {s e} _ {j} ^ {2} = (\mathrm {s e} _ {Y j} ^ {2} + \hat {\beta} _ {j} ^ {2} \mathrm {s e} _ {D j} ^ {2}) / \hat {\gamma} _ {j} ^ {2}.
$$

Therefore, the best linear combination to estimate $\beta$ is the Fisher weighting based on the inverses of the variances (see Problem A.6):

$$
\hat {\beta} _ {\mathrm {f i s h e r 0}} = \frac {\sum_ {j = 1} ^ {p} \hat {\beta} _ {j} / \mathrm {s e} _ {j} ^ {2}}{\sum_ {j = 1} ^ {p} 1 / \mathrm {s e} _ {j} ^ {2}}
$$

which has variance $\left(\sum_{j=1}^{p} 1 / \mathrm{se}_j^2\right)^{-1}$ . Ignoring the uncertainty due to $\hat{\gamma}_j$ quantified by $\mathrm{se}_{Dj}$ , the estimator reduces to

$$
\hat {\beta} _ {\mathrm {f i s h e r 1}} = \frac {\sum_ {j = 1} ^ {p} \hat {\beta} _ {j} \hat {\gamma} _ {j} ^ {2} / \mathrm {s e} _ {Y j} ^ {2}}{\sum_ {j = 1} ^ {p} \hat {\gamma} _ {j} ^ {2} / \mathrm {s e} _ {Y j} ^ {2}} = \frac {\sum_ {j = 1} ^ {p} \hat {\Gamma} _ {j} \hat {\gamma} _ {j} / \mathrm {s e} _ {Y j} ^ {2}}{\sum_ {j = 1} ^ {p} \hat {\gamma} _ {j} ^ {2} / \mathrm {s e} _ {Y j} ^ {2}},
$$

which has variance $(\sum_{j=1}^{p} \hat{\gamma}_{j}^{2} / \mathrm{se}_{Yj}^{2})^{-1}$ . Inference based on $\hat{\beta}_{\mathrm{fisher1}}$ is suboptimal although it is more widely used in practice (Bowden et al., 2018). Both $\hat{\beta}_{\mathrm{fisher0}}$ and $\hat{\beta}_{\mathrm{fisher1}}$ are called the fixed-effect estimators.

Focus on the suboptimal yet simpler estimator $\hat{\beta}_{\mathrm{fisher1}}$ . Under Definition 25.2, we can show that

$$
\hat {\beta} _ {\mathrm {f i s h e r 1}} \rightarrow \frac {\sum_ {j = 1} ^ {p} \Gamma_ {j} \gamma_ {j} / \mathrm {s e} _ {Y j} ^ {2}}{\sum_ {j = 1} ^ {p} \gamma_ {j} ^ {2} / \mathrm {s e} _ {Y j} ^ {2}} = \beta + \frac {\sum_ {j = 1} ^ {p} \alpha_ {j} \gamma_ {j} / \mathrm {s e} _ {Y j} ^ {2}}{\sum_ {j = 1} ^ {p} \gamma_ {j} ^ {2} / \mathrm {s e} _ {Y j} ^ {2}}
$$

in probability. If $\alpha_{j} = 0$ for all $j$ , $\hat{\beta}_{\mathrm{fisher1}}$ is consistent. Even if this does not hold, it is still possible that $\hat{\beta}_{\mathrm{fisher1}}$ is consistent as long as the inner product between $\alpha_{j}$ and $\gamma_{j}$ weighted by $1 / \mathrm{se}_{Yj}^{2}$ is zero. This holds if we have many genetic instruments and violation of the exclusion restriction, captured by $\alpha_{j}$ , is an independent random draw from a distribution with mean zero.

# 25.2.2 Egger regression

Start with Definition 25.1. With the true parameters, we have

$$
\Gamma_ {j} = \beta \gamma_ {j} \quad (j = 1, \dots , p);
$$

with the estimates, the above identity holds only approximately

$$
\hat {\Gamma} _ {j} \approx \beta \hat {\gamma} _ {j} \quad (j = 1, \dots , p).
$$

This seems a classic least-squares problem of $\{\hat{\Gamma}_j\}_{j=1}^p$ on $\{\hat{\gamma}_j\}_{j=1}^p$ . We can fit a WLS of $\hat{\Gamma}_j$ on $\hat{\gamma}_j$ , with or without an intercept, possibly weighted by $w_j$ , to estimate $\beta$ . The following results hold thanks to the algebraic properties of the WLS reviewed in Chapter B.5.

Without an intercept, the coefficient of $\hat{\gamma}_j$ is

$$
\hat {\beta} _ {\mathrm {e g g e r 1}} = \frac {\sum_ {j = 1} ^ {p} \hat {\gamma} _ {j} \hat {\Gamma} _ {j} w _ {j}}{\sum_ {j = 1} ^ {p} \hat {\gamma} _ {j} ^ {2} w _ {j}},
$$

which reduces to $\hat{\beta}_{\mathrm{fisher1}}$ if $w_{j} = 1 / \mathrm{se}_{Yj}^{2}$ . The WLS is called the Egger regression. It is more general than the fixed-effect estimators in Section 25.2.1. With an intercept, the coefficient of $\hat{\gamma}_j$ is

$$
\hat {\beta} _ {\mathrm {e g g e r 0}} = \frac {\sum_ {j = 1} ^ {p} (\hat {\gamma} _ {j} - \hat {\gamma} _ {w}) (\hat {\Gamma} _ {j} - \hat {\Gamma} _ {w}) w _ {j}}{\sum_ {j = 1} ^ {p} (\hat {\gamma} _ {j} - \hat {\gamma} _ {w}) ^ {2} w _ {j}}
$$

where $\hat{\gamma}_w = \sum_{j=1}^p \hat{\gamma}_j w_j / \sum_{j=1}^p w_j$ and $\hat{\Gamma}_w = \sum_{j=1}^p \hat{\Gamma}_j w_j / \sum_{j=1}^p w_j$ are the weighted averages of the $\hat{\gamma}_j$ 's and $\hat{\Gamma}_j$ 's, respectively.

Even without assuming that all $\gamma_{j}$ 's are zero under Definition 25.2, we have

$$
\hat {\beta} _ {\mathrm {e g g e r 0}} \rightarrow \frac {\sum_ {j = 1} ^ {p} (\gamma_ {j} - \gamma_ {w}) (\Gamma_ {j} - \Gamma_ {w}) w _ {j}}{\sum_ {j = 1} ^ {p} (\gamma_ {j} - \gamma_ {w}) ^ {2} w _ {j}} = \beta + \frac {\sum_ {j = 1} ^ {p} (\gamma_ {j} - \gamma_ {w}) (\alpha_ {j} - \alpha_ {w}) w _ {j}}{\sum_ {j = 1} ^ {p} (\gamma_ {j} - \gamma_ {w}) ^ {2} w _ {j}}
$$

in probability, where $\gamma_w, \Gamma_w$ and $\alpha_w$ are the corresponding weighted averages of the true parameters. So $\hat{\beta}_{\mathrm{egger0}}$ is consistent for $\beta$ as long as the WLS coefficient of $\alpha_j$ on $\gamma_j$ is zero. This is weaker than $\alpha_j = 0$ for all $j$ . This weaker assumption holds if $\gamma_j$ and $\alpha_j$ are realizations of independent random variables, which is called the Instrument Strength Independent of Direct Effect (InSIDE) assumption (Bowden et al., 2015). More interestingly, the intercept from the Egger regression is

$$
\hat {\alpha} _ {\text {e g g e r 0}} = \hat {\Gamma} _ {w} - \hat {\beta} _ {\text {e g g e r 0}} \hat {\gamma} _ {w},
$$

which, under the InSIDE assumption, converges to

$$
\Gamma_ {w} - \beta \gamma_ {w} = \alpha_ {w}
$$

in probability. So the intercept estimates the weighted average of the direct effects.

# 25.3 An example

First, the following function can implement Fisher weighting.

```r
fisher.weight = function(est, se)  
{  
    n = sum(est/se^2)  
    d = sum(1/se^2)  
    res = c(n/d, sqrt(1/d))  
    names(res) = c("est", "se")  
    res  
} 
```

I use the bmi.sbp data in the mr.raps package (Zhao et al., 2020) to illustrate the Fisher weighting based on different variance estimates. The results based on $\hat{\beta}_{\mathrm{fisher0}}$ and $\hat{\beta}_{\mathrm{fisher1}}$ are similar.

```txt
>bmisbp = read.csv("mr_bmisbp.csv")
>bmisbp\\(iv = with(bmisbp, betaoutcome/beta.exposure)
>bmisbp\\)se.iv = with(bmisbp, seoutcome/beta.exposure)
>bmisbp\\(se.iv1 = with(bmisbp,
+ sqrt(seoutcome^2 + iv^2*se.exposure^2)/beta.exposure)
>fisher.weight(bmisbp\\)iv, bmisbp\\(se.iv)
est se
0.31727680 0.05388827
>fisher.weight(bmisbp\\)iv, bmisbp\\(se.iv1)
est se
0.31576007 0.05893783 
```

The Egger regressions with or without the intercept also give very similar results. But the standard errors are quite different from those based on Fisher weighting.

```txt
> mr.egger = lm(beta.output ~ 0 + beta.exposure,
+ data = bmisbp,
+ weights = 1/seoutcome^2)
> summary(mr.egger)$coef
Estimate Std. Error t value Pr(>|t|)
beta.exposure 0.3172768 0.1105994 2.868704 0.004681659
>
> mr.egger.w = lm(beta.output ~ beta.exposure,
+ data = bmisbp,
+ weights = 1/seoutcome^2)
> summary(mr.egger.w)$coef
Estimate Std. Error t value Pr(>|t|)
(Intercept) 0.0001133328 0.002079418 0.05450217 0.956603931
beta.exposure 0.3172989306 0.110948506 2.85987564 0.004811017 
```

Figure 25.2 shows the raw data as well as the fitted Egger regression line with the intercept.

![](images/37cb7c42b44d36344c67fbcb29a678311dee7bd235a45e75c5d8b7675273e545.jpg)  
FIGURE 25.2: Scatter plot proportional to the inverse of the variance, with the Egger regression line

# 25.4 Critiques of the analysis based on MR

MR is an application of the idea of IV. It relies on strong assumptions. I provide three sets of critiques from the conceptual, biological, and technical perspectives.

Conceptually, the treatments in most studies based on MR are not well defined from the potential outcomes perspective. For instance, the treatments are often defined as the cholesterol level or the BMI. They are composite variables and can correspond to complex, non-unique definitions of the hypothetical experiments. The SUTVA often does not hold for these treatments. Recall the discussion in Chapter 2.

Biologically, the fundamental assumptions for the IV analysis may not hold. Mendel's second law ensures that the inheritances of different traits are independent. However, it does not ensure that the candidate IVs are independent of the hidden confounders between the treatment and the outcome. It is possible that these IVs have direct effects on the confounders. It is also possible that some unmeasured genes affect both the IVs and the confounders. Mendel's second law does not ensure the exclusion restriction assumption either. It is possible that the IVs have other causal pathways to the outcome, beyond the pathway through the treatment of interest.

Technically, the statistical assumptions for MR are quite strong. Clearly, the linear IV model is a strong modeling assumption. The independence of the $\hat{\gamma}_j$ 's and the $\hat{\Gamma}_j$ 's is also quite strong. Other issues in the data-collecting process can further complicate the interpretation of the IV assumptions. For instance, the treatments and outcomes are often measured with errors, and the genome-wide associate studies are often based on the case-control design with the samples conditional on the outcomes (see Chapter B.6.3).

VanderWeele et al. (2014) is an excellent review paper that discusses the methodological challenges in MR.

# 25.5 Homework Problems

# 25.1 Data analysis

Analyze the bmi.bmi data in the R package mr.raps. See the package and Zhao et al. (2020, Section 7.2) for more details.

# 25.2 Recommended reading

Davey Smith and Ebrahim (2003) reviewed the potentials and limitations of MR.

# Part VI

# Causal Mechanisms with Post-Treatment Variables

# Principal Stratification

Parts II-V of this book focus on the causal effects of a treatment on an outcome, possibly adjusting for some observed pretreatment covariates. Many applications also have some post-treatment variable $M$ which happens after the treatment and is related to the outcome. An important question is how to use the post-treatment variable $M$ appropriately. I will start with several motivating examples and then introduce Frangakis and Rubin (2002)'s formulation of this problem based on potential outcomes.

# 26.1 Motivating Examples

Example 26.1 (noncompliance) In randomized experiments with noncompliance, we can use $M$ to represent the treatment received, which is affected by the treatment assignment $Z$ and affects the outcome $Y$ . In this example, $M$ has the same meaning as $D$ in Chapter 21.

Example 26.2 (truncation by death) In randomized experiments to patients with severe diseases, some patients may die before the measurement of the outcome $Y$ , e.g., the quality of life. The post-treatment variable $M$ in this example is the binary indicator of the survival status.

Example 26.3 (unemployment) In job training programs, units are randomly assigned to treatment and control groups, and report their employment status $M$ and wage $Y$ . Then the post-treatment variable is the binary indicator of the employment status $M$ .

Example 26.4 (surrogate endpoint) In clinical trials, the outcomes of interest (e.g., 30 years of survival) require a long and costly follow-up. Practitioners instead collect data on some other variables early in the follow-up that are easy to measure. These variables are called the "surrogate endpoints." A concrete example is from clinical trials on HIV patients, where the candidate surrogate endpoint $M$ is the CD4 cell count (recall that CD4 cells are white blood cells that fight infection).

Examples 26.1-26.4 above have the similarity that a variable $M$ occurs

after the treatment and is related to the outcome. It is possible that $M$ is on the causal pathway from $Z$ to $Y$ . Figure 26.1(a) illustrates this mechanism. Example 26.1 corresponds to Figure 26.1(a). It is also possible that $M$ is not on the causal pathway from $Z$ to $Y$ . Figure 26.1(b) illustrates this mechanism. Examples 26.2 and 26.3 correspond to Figure 26.1(b). Example 26.4 can correspond to Figure 26.1(a) or (b), depending on the choice of the surrogate endpoint.

![](images/9293eb135cf411fe6227da02e4ee2d5b4358296df9b54446fa178a3176d5ecc2.jpg)

(a) $M$ is on the causal pathway from $Z$ to $Y$ , with $Z$ randomized and $U$ representing unmeasured confounding

![](images/69addd70c2a80d338eff1fea722cdb4dddc5ea9e75778ed7d0095c2afe9eb69c.jpg)  
FIGURE 26.1: Causal diagrams with a post-treatment variable $M$

(b) $M$ is not on the causal pathway from $Z$ to $Y$ , with $Z$ randomized and $U$ representing unmeasured confounding

In practice, the underlying causal diagrams can be much more complex than those in Figure 26.1. This chapter follows Frangakis and Rubin (2002)'s formulation which does not assume the underlying causal diagrams.

# 26.2 The Problem of Conditioning on the Post-Treatment Variable

A naive method to deal with the post-treatment variable $M$ is to condition on its observed value as if it were a pretreatment covariate. However, $M$ is fundamentally different from $X$ , because $M$ is affected by the treatment in general whereas $X$ is not. It is also a "rule of thumb" that data analyzers should not condition on any post-treatment variables in evaluating the average causal effect of the treatment on the outcome (Cochran, 1957; Rosenbaum, 1984). Based on potential outcomes, Frangakis and Rubin (2002) gave the following insightful explanation.

For simplicity, we focus on the CRE in this chapter.

Assumption 26.1 (CRE with an intermediate variable) We have

$$
Z \text {止} \{M (1), M (0), Y (1), Y (0), X \}.
$$

Conditioning on $M = m$ , we compare

$$
\Pr (Y \mid Z = 1, M = m) \tag {26.1}
$$

and

$$
\Pr (Y \mid Z = 0, M = m). \tag {26.2}
$$

This comparison seems intuitive because it measures the difference in the outcome distributions in the treated and control groups given the same value of the post-treatment variable. When $M$ is a pre-treatment covariate, this comparison yields a reasonable subgroup effect. However, when $M$ is a post-treatment variable, the interpretation of this comparison is problematic. Under Assumption 26.1, we can re-write the probabilities in (26.1) and (26.2) as

$$
\begin{array}{l} \operatorname {p r} (Y \mid Z = 1, M = m) = \operatorname {p r} \{Y (1) \mid Z = 1, M (1) = m \} \\ = \Pr \{Y (1) \mid M (1) = m \} \\ \end{array}
$$

and

$$
\begin{array}{l} \operatorname {p r} (Y \mid Z = 0, M = m) = \operatorname {p r} \{Y (0) \mid Z = 0, M (0) = m \} \\ = \operatorname {p r} \{Y (0) \mid M (0) = m \}. \\ \end{array}
$$

Therefore, under CRE, comparing (26.1) and (26.2) is equivalent to comparing the distributions of $Y(1)$ and $Y(0)$ for different subsets of units because the units with $M(1) = m$ are different from the units with $M(0) = m$ if the $Z$ affects $M$ . Consequently, the comparison conditioning on $M = m$ does not have a causal interpretation in general unless $M(1) = M(0)$ .<sup>1</sup>

Revisit Example 26.1. Comparing $\operatorname{pr}(Y \mid Z = 1, M = 1)$ and $\operatorname{pr}(Y \mid Z = 0, M = 1)$ is equivalent to comparing the treated potential outcomes for compliers and always-takers with the control potential outcomes for always-takers, under the monotonicity assumption that $M(1) \geq M(0)$ . Part 3 of Problem 22.8 has pointed out the drawbacks of this analysis.

Revisit Example 26.2. If the treatment improves the survival status, the treatment can save more weak patients than the control. In this case, units with $M(1) = 1$ are weaker than units with $M(0) = 1$ , so the naive comparison gives biased results that are in favor of the control.

# 26.3 Conditioning on the Potential Values of the Post-Treatment Variable

Frangakis and Rubin (2002) proposed to condition on the joint potential value of the post-treatment variable $U = \{M(1), M(0)\}$ and compare

$$
\Pr \left\{Y (1) \mid M (1) = m _ {1}, M (0) = m _ {0} \right\}
$$

and

$$
\Pr \{Y (0) \mid M (1) = m _ {1}, M (0) = m _ {0} \}
$$

for some $(m_1, m_0)$ . This is a comparison of the potential outcomes under treatment and control for the same subset of units with $M(1) = m_1$ and $M(0) = m_0$ . Frangakis and Rubin (2002) called this strategy principal stratification, viewing $\{M(1), M(0)\}$ as a pre-treatment covariate. Based on this idea, we can define

$$
\tau \left(m _ {1}, m _ {0}\right) = E \left\{Y (1) - Y (0) \mid M (1) = m _ {1}, M (0) = m _ {0} \right\}
$$

as the principal stratification average causal effect for the subgroup with $M(1) = m_{1}, M(0) = m_{0}$ . For a binary $M$ , we have four subgroups

$$
\left\{ \begin{array}{r c l} \tau (1, 1) & = & E \left\{Y (1) - Y (0) \mid M (1) = 1, M (0) = 1 \right\}, \\ \tau (1, 0) & = & E \left\{Y (1) - Y (0) \mid M (1) = 1, M (0) = 0 \right\}, \\ \tau (0, 1) & = & E \left\{Y (1) - Y (0) \mid M (1) = 0, M (0) = 1 \right\}, \\ \tau (0, 0) & = & E \left\{Y (1) - Y (0) \mid M (1) = 0, M (0) = 0 \right\}. \end{array} \right. \tag {26.3}
$$

Since $\{M(1), M(0)\}$ is unaffected by the treatment, it is a covariate so $\tau(m_1, m_0)$ is a subgroup causal effect. For subgroups with $M(1) = M(0)$ , the treatment does not change the intermediate variable, so $\tau(1, 1)$ and $\tau(0, 0)$ measure the dissociative effects. For other subgroups with $m_1 \neq m_0$ , the principal stratification average causal effects $\tau(m_1, m_0)$ measure the associative effects. The terminology is from Frangakis and Rubin (2002), which does not assume that $M$ is on the causal pathway from $Z$ to $Y$ . When we have Figure 26.1(a), we can interpret the dissociative effects as direct effects of $Z$ on $Y$ that act independent of $M$ , although we cannot simply interpret the associative effects as direct or indirect effects of $Z$ on $Y$ .

Example 26.1 (noncompliance) With noncompliance, (26.3) consists of the average causal effects for always takers, compliers, defiers, and never takers (Imbens and Angrist, 1994; Angrist et al., 1996).

Example 26.2 (truncation by death) Because the outcome is well-defined only if the patient survives, three subgroup causal effects in (26.3) are not meaningful, and the only well-defined subgroup effect is

$$
\tau (1, 1) = E \left\{Y (1) - Y (0) \mid M (1) = 1, M (0) = 1 \right\}. \tag {26.4}
$$

It is called the survivor average causal effect (Rubin, 2006a). It is the average causal effect of the treatment on the outcome for those units who survive regardless of the treatment status.

Example 26.3 (unemployment) The unemployment problem is isomorphic to the truncation-by-death problem because the wage is well-defined only if the unit is employed in the first place. Therefore, the only well-defined subgroup effect is (26.4), the employed average causal effect. Previously, Heckman (1979) proposed a model, now called the Heckman Selection Model, to deal with unemployment in modeling the wage, viewing the wages of those unemployed as missing values<sup>2</sup>. However, Zhang and Rubin (2003) and Zhang et al. (2009) argued that $\tau(1,1)$ is a more meaningful quantity under the potential outcomes framework.

Example 26.4 (surrogate endpoint) Intuitively, we want to assess the effect of the treatment on the outcome via the effect of the treatment on the surrogate endpoint. Therefore, a good surrogate endpoint should satisfy two conditions: first, if the treatment does not affect the surrogate, then it does not affect the outcome either; second, if the treatment affects the surrogate, then it affects the outcome too. The first condition is called the "causal necessity" by Frangakis and Rubin (2002), and the second condition is called the "causal sufficiency" by Gilbert and Hudgens (2008). Based on (26.3) for a binary surrogate endpoint, causal necessity requires that $\tau(1,1)$ and $\tau(0,0)$ are zero, and causal sufficiency requires that $\tau(1,0)$ and $\tau(0,1)$ are not zero.

# 26.4 Statistical Inference and Its Difficulty

In Example 26.1, if we have randomization, monotonicity, and exclusion restriction, then we can identify the complier average causal effect $\tau(1,0)$ . This is the key result derived in Chapter 21.

However, in other examples, we cannot impose the exclusion restriction assumption. For instance, $\tau(1,1)$ is the main parameter of interest in Examples 26.2 and 26.3, and $\tau(1,1)$ and $\tau(0,0)$ are both of interest in Example 26.4.

2Heckman won the Nobel prize of economics in 2000 "for his development of theory and methods for analyzing selective samples." His model contains two stages. First, the employment status is determined by a latent linear model

$$
M _ {i} = 1 (X _ {i} ^ {\mathsf {T}} \beta + u _ {i} \geq 0).
$$

Second, the latent log wage is determined by a linear model

$$
Y _ {i} ^ {*} = W _ {i} ^ {\top} \gamma + v _ {i}
$$

and $Y_{i}^{*}$ is observed as $Y_{i}$ only if $M_{i} = 1$ . In his two-stage model, the covariates $X_{i}$ and $W_{i}$ may differ, and the errors $(u_{i}, v_{i})$ are correlated bivariate Normal.

Without the exclusion restriction assumption, it is very challenging to identify the principal stratification average causal effect. Sometimes, we cannot even impose the monotonicity assumption, and thus cannot identify the proportions of the latent strata in the first place.

# 26.4.1 Special case: truncation by death with binary outcome

I use the simple setting with a binary treatment, binary survival status, and binary outcome to illustrate the idea and especially the difficulty of statistical inference based on principal stratification.

In addition to Assumption 26.1, we impose the monotonicity.

# Assumption 26.2 (monotonicity) $M(1)\geq M(0)$

Theorem 22.1 demonstrates that under Assumptions 26.1 and 26.2, we can identify the proportions of the three latent strata by

$$
\begin{array}{l} \pi_ {(1, 1)} = \operatorname {p r} (M = 1 \mid Z = 0), \\ \pi_ {(0, 0)} = \operatorname {p r} (M = 0 \mid Z = 1), \\ \pi_ {(1, 0)} = \operatorname {p r} (M = 1 \mid Z = 1) - \operatorname {p r} (M = 1 \mid Z = 0). \\ \end{array}
$$

Our goal is to identify the survivor average causal effect $\tau(1,1)$ . First, we can easily identify $E\{Y(0) \mid M(1) = 1, M(0) = 1\}$ because the observed group $(Z = 0, M = 1)$ consists of only survivors:

$$
E \left\{Y (0) \mid M (1) = 1, M (0) = 1 \right\} = E (Y \mid Z = 0, M = 1).
$$

The key is then to identify $E\{Y(1) \mid M(1) = 1, M(0) = 1\}$ . The observed group $(Z = 1, M = 1)$ is a mixture of two strata $(1, 1)$ and $(1, 0)$ , therefore we have

$$
\begin{array}{l} E (Y \mid Z = 1, M = 1) = \frac {\pi_ {(1 , 1)}}{\pi_ {(1 , 1)} + \pi_ {(1 , 0)}} E \{Y (1) \mid M (1) = 1, M (0) = 1 \} \\ + \frac {\pi_ {(1 , 0)}}{\pi_ {(1 , 1)} + \pi_ {(1 , 0)}} E \{Y (1) \mid M (1) = 1, M (0) = 0 \}. \tag {26.5} \\ \end{array}
$$

We have two unknown parameters but only one equation in (26.5). So we cannot uniquely determine $E\{Y(1) \mid M(1) = 1, M(0) = 1\}$ from the above equation (26.5). Nevertheless, (26.5) contains some information about the quantity of interest. That is, $E\{Y(1) \mid M(1) = 1, M(0) = 1\}$ is partially identified by Definition 18.1.

For a binary outcome $Y$ , we know that $E\{Y(1) \mid M(1) = 1, M(0) = 0\}$ is bounded between 0 and 1, and consequently, $E\{Y(1) \mid M(1) = 1, M(0) = 1\}$ .

is bounded between the solutions to the following two equations:

$$
\begin{array}{l} E (Y \mid Z = 1, M = 1) = \frac {\pi_ {(1 , 1)}}{\pi_ {(1 , 1)} + \pi_ {(1 , 0)}} E \{Y (1) \mid M (1) = 1, M (0) = 1 \} \\ + \frac {\pi_ {(1 , 0)}}{\pi_ {(1 , 1)} + \pi_ {(1 , 0)}} \\ \end{array}
$$

and

$$
E (Y \mid Z = 1, M = 1) = \frac {\pi_ {(1 , 1)}}{\pi_ {(1 , 1)} + \pi_ {(1 , 0)}} E \{Y (1) \mid M (1) = 1, M (0) = 1 \}.
$$

Therefore, $E\{Y(1) \mid M(1) = 1, M(0) = 1\}$ has lower bound

$$
\frac {\{\pi_ {(1 , 1)} + \pi_ {(1 , 0)} \} E (Y \mid Z = 1 , M = 1) - \pi_ {(1 , 0)}}{\pi_ {(1 , 1)}},
$$

and upper bound

$$
\frac {\{\pi_ {(1 , 1)} + \pi_ {(1 , 0)} \} E (Y \mid Z = 1 , M = 1)}{\pi_ {(1 , 1)}}.
$$

We can then derive the bounds on $\tau(1, 1)$ , summarized in Theorem 26.1 below.

Theorem 26.1 Under Assumptions 26.1 and 26.2 with a binary $Y$ , we have

$$
\begin{array}{l} \frac {\{\pi_ {(1 , 1)} + \pi_ {(1 , 0)} \} E (Y \mid Z = 1 , M = 1) - \pi_ {(1 , 0)}}{\pi_ {(1 , 1)}} - E (Y \mid Z = 0, M = 1) \\ \leq \tau (1, 1) \\ \leq \frac {\left\{\pi_ {(1 , 1)} + \pi_ {(1 , 0)} \right\} E (Y \mid Z = 1 , M = 1)}{\pi_ {(1 , 1)}} - E (Y \mid Z = 0, M = 1). \\ \end{array}
$$

We can use Imbens and Manski (2004)'s confidence interval for $\tau(1,1)$ which involves two steps: first, we obtain the estimated lower and upper bounds $[\hat{l},\hat{u}]$ with estimated standard errors $(\mathrm{se}_l,\mathrm{se}_u)$ ; second, we construct the confidence interval as $[\hat{l} -z_{1 - \alpha}\mathrm{se}_l,\hat{u} +z_{1 - \alpha}\mathrm{se}_u]$ , where $z_{1 - \alpha}$ is the $1 - \alpha$ quantile of the standard Normal distribution. The validity of Imbens and Manski (2004)'s confidence interval relies on some regularity conditions. In most truncation by death problems, those conditions hold because the lower and upper bounds are quite different, and they are bounded away from the extreme values $-1$ and $1$ . I omit the technical details here.

To summarize, this is a challenging problem since we cannot identify the parameter based on the observed data even with an infinite sample size. We can derive large-sample bounds for $\tau(1,1)$ but the statistical inference based on the bounds is not standard. If we do not have monotonicity, the large-sample bounds have even more complex forms; see Zhang and Rubin (2003) and Jiang et al. (2016, Appendix A).

TABLE 26.1: Data truncated by death with * indicating the outcomes for dead patients   

<table><tr><td colspan="4">Treatment Z = 1</td><td colspan="4">Control Z = 0</td></tr><tr><td></td><td>Y = 1</td><td>Y = 0</td><td>total</td><td></td><td>Y = 1</td><td>Y = 0</td><td>total</td></tr><tr><td>M = 1</td><td>54</td><td>268</td><td>322</td><td>M = 1</td><td>59</td><td>218</td><td>277</td></tr><tr><td>M = 0</td><td>*</td><td>*</td><td>109</td><td>M = 0</td><td>*</td><td>*</td><td>152</td></tr></table>

# 26.4.2 An application

I use the data in Yang and Small (2016) from the Acute Respiratory Distress Syndrome Network study which involves 861 patients with lung injury and acute respiratory distress syndrome. Patients were randomized to receive mechanical ventilation with either lower tidal volumes or traditional tidal volumes. The outcome is the binary indicator for whether patients could breathe without assistance by day 28. Table 26.1 summarizes the observed data.

We first obtain the point estimators of the latent strata:

$$
\hat {\pi} _ {(1, 1)} = \frac {2 7 7}{2 7 7 + 1 5 2} = 0. 6 4 6,
$$

$$
\hat {\pi} _ {(0, 0)} = \frac {1 0 9}{1 0 9 + 3 2 2} = 0. 2 5 3,
$$

$$
\hat {\pi} _ {(1, 0)} = 1 - 0. 6 4 6 - 0. 2 5 3 = 0. 1 0 1.
$$

The sample means of the outcome for surviving patients are

$$
\hat {E} (Y \mid Z = 1, M = 1) = \frac {5 4}{3 0 2} = 0. 1 6 8,
$$

$$
\hat {E} (Y \mid Z = 0, M = 1) = \frac {5 9}{2 7 7} = 0. 2 1 3.
$$

The estimates for the bounds on $E\{Y(1) \mid M(1) = 1, M(0) = 1\}$ are

$$
\left[ \frac {(0 . 6 4 6 + 0 . 1 0 1) \times 0 . 1 6 8 - 0 . 1 0 1}{0 . 1 0 1}, \frac {(0 . 6 4 6 + 0 . 1 0 1) \times 0 . 1 6 8}{0 . 1 0 1} \right] = [ 0. 0 3 7, 0. 1 9 4 ],
$$

so the bounds on $\tau (1,1)$ are

$$
[ 0. 0 3 7 - 0. 2 1 3, 0. 1 9 4 - 0. 2 1 3 ] = [ - 0. 1 7 6, - 0. 0 1 9 ].
$$

Incorporating the sampling uncertainty based on the bootstrap, the confidence interval based on Imbens and Manski (2004)'s method is $[-0.267, 0.039]$ , which covers 0.

# 26.4.3 Extensions

Zhang and Rubin (2003) started the literature of large-sample bounds. Imai

(2008a) and Lee (2009) were two follow-up papers. Cheng and Small (2006) derived the bounds with multiple treatment arms. Yang and Small (2016) used a secondary outcome and Yang and Ding (2018a) used detailed survival information to sharpen the bounds on the survivor average causal effect.

# 26.5 Principal score method

Without additional assumptions, we can only derive bounds on the causal effects within principal strata, but cannot identify them in general. We must impose additional assumptions to achieve nonparametric identification of the $\tau(m_1, m_0)$ 's. There is no consensus on the choice of the assumptions. Those additional assumptions are not testable, and their plausibility depends on the application.

A line of research based on the principal score under the principal ignorance assumption parallels causal inference with unconfounded observational studies. For simplicity, I focus on the case with strong monotonicity.

# 26.5.1 Principal score method under strong monotonicity

Assumption 26.3 (strong monotonicity) $M(0) = 0$ .

Similar to the ignorance assumption, we now assume the principal ignorance assumption.

Assumption 26.4 (principal ignorability) We have

$$
E \{Y (0) \mid M (1) = 1, X \} = E \{Y (0) \mid M (1) = 0, X \}.
$$

Assumption 26.4 implies that $E\{Y(0) \mid M(1), X\} = E\{Y(0) \mid X\}$ or, equivalently,

$$
E \{Y (0) M (1) \mid X \} = E \{Y (0) \mid X \} E \{M (1) \mid X \}, \tag {26.6}
$$

that is, $Y(0)$ and $M(1)$ are mean independent (or uncorrelated) given $X$ .

Assumptions 26.1, 26.3 and 26.4 ensure nonparametric identification of the causal effects within principal strata, as summarized by Theorem 26.2 below.

Theorem 26.2 Under Assumptions 26.1, 26.3 and 26.4,

1.the conditional and marginal probabilities of $M(1)$ , $\pi(X) = \operatorname{pr}\{M(1) = 1 \mid X\}$ and $\pi = \operatorname{pr}\{M(1) = 1\}$ , can be identified by

$$
\pi (X) = \operatorname {p r} (M = 1 \mid Z = 1, X)
$$

and

$$
\pi = \operatorname {p r} (M = 1 \mid Z = 1)
$$

respectively;

2.the principal stratification average causal effects can be identified by

$$
\tau (1, 0) = E (Y \mid Z = 1, M = 1) - E \{\pi (X) Y \mid Z = 0 \} / \pi
$$

and

$$
\tau (0, 0) = E (Y \mid Z = 1, M = 0) - E \{(1 - \pi (X)) Y \mid Z = 0 \} / (1 - \pi).
$$

The conditional probability $\pi(X) = \operatorname{pr}\{M(1) = 1 \mid X\}$ is called the principal score. Theorem 26.2 states that $\tau(1,0)$ and $\tau(0,0)$ can be identified by the difference in means with appropriate weights depending on the principal score.

Proof of Theorem 26.2: I will only prove the result for $\tau(1,0)$ . We have

$$
E (Y \mid Z = 1, M = 1) = E \{Y (1) \mid Z = 1, M (1) = 1 \} = E \{Y (1) \mid M (1) = 1 \}.
$$

Moreover,

$$
\begin{array}{l} E \{\pi (X) Y \mid Z = 0 \} / \pi \\ = E \left\{\pi (X) Y (0) \mid Z = 0 \right\} / \pi \\ = E \left\{\pi (X) Y (0) \right\} / \pi \quad (\text {A s s u m p t i o n 2 6 . 1}) \\ = E \left[ E \left\{\pi (X) Y (0) \mid X \right\} \right] / \pi \quad \text {(t o w e r p r o p e r t y)} \\ = E [ \pi (X) E \{Y (0) \mid X \} ] / \pi \\ = E \left[ E \{M (1) \mid X \} E \{Y (0) \mid X \} \right] / \pi \\ = E \left[ E \{M (1) Y (0) \mid X \} \right] / \pi \quad (\text {b y} (2 6. 6)) \\ = E \{M (1) Y (0) \} / \pi \\ = E \{Y (0) \mid M (1) = 1 \}. \\ \end{array}
$$

I relegate the proof of the result for $\tau(0,0)$ as Problem 26.1.

Theorem 26.2 motivates the following simple estimators for $\tau(1,0)$ and $\tau(0,0)$ , respectively:

1. fit a logistic regression of $M$ on $X$ using only data from the treated group to obtain $\hat{\pi}(X_i)$ ;   
2. estimate $\pi$ by $\hat{\pi} = \sum_{i=1}^{n} Z_i M_i / \sum_{i=1}^{n} Z_i$ ;   
3. obtain moment estimators:

$$
\hat {\tau} (1, 0) = \frac {\sum_ {i = 1} ^ {n} Z _ {i} M _ {i} Y _ {i}}{\sum_ {i = 1} ^ {n} Z _ {i} M _ {i}} - \frac {\sum_ {i = 1} ^ {n} (1 - Z _ {i}) \hat {\pi} (X _ {i}) Y _ {i}}{\hat {\pi} \sum_ {i = 1} ^ {n} (1 - Z _ {i})}
$$

and

$$
\hat {\tau} (0, 0) = \frac {\sum_ {i = 1} ^ {n} Z _ {i} (1 - M _ {i}) Y _ {i}}{\sum_ {i = 1} ^ {n} Z _ {i} (1 - M _ {i})} - \frac {\sum_ {i = 1} ^ {n} (1 - Z _ {i}) (1 - \hat {\pi} (X _ {i}) \} Y _ {i}}{(1 - \hat {\pi}) \sum_ {i = 1} ^ {n} (1 - Z _ {i})};
$$

4. use the bootstrap to approximate the variances of $\hat{\tau}(1,0)$ and $\hat{\tau}(0,0)$ .

# 26.5.2 An example

The following function can compute the point estimates of $\hat{\tau}(1,0)$ and $\hat{\tau}(0,0)$ .

```txt
psw = function(Z, M, Y, X) {
    ## probabilities of 10 and 00
    pi.10 = mean(M[Z==1])
    pi.00 = 1 - pi.10
    #
    # conditional probabilities of 10 and 00
    ps.10 = glm(M ~ X, family = binomial,
                    weights = Z)$fitted.values
    ps.00 = 1 - ps.10
    #
    PCEs 10 and 00
    tau.10 = mean(Y[Z==1&M==1]) - mean(Y[Z==0]*ps.10[Z==0])/pi.10
    tau.00 = mean(Y[Z==1&M==0]) - mean(Y[Z==0]*ps.00[Z==0])/pi.00
    c(tau.10, tau.00)
} 
```

The following function can compute the point estimators as well as the bootstrap standard errors.

psw.boot $=$ function(Z,M,Y,X,n.boot $= 500$ { ## point estimates point.est $=$ psw(Z,M,Y,X) #bootstrap standard errors n $=$ length(Z) boot.est $=$ replicate(n.boot,{ id.boot $=$ sample(1:n,n,replace $\equiv$ TRUE) psw(Z[id.boot],M[id.boot],Y[id.boot],X[id.boot，]) }） boot.se $=$ apply.boot.est,1,sd) ## results res $=$ rbind(point.est,boot.se) rnames(res) $=$ c("est","se") colnames(res) $=$ c("tau10","tau00") return(res)   
}

Revisit the data used in Chapter 21.5. Previously, we assumed exclusion restriction for the IV analysis. Now, we drop the exclusion restriction but assume principal ignorability. The results are below.

```txt
> jobsdata = read.csv("jobsdata.csv")
> getX = lm(treat ~ sex + age + marital
+ + nonwhite + educ + income,
+ data = jobsdata)
> X = model.matrix(getX)[-, -1]
> Z = jobsdata$treat
> M = jobsdata$comply
> Y = jobsdata$job-seeking 
```

```txt
> table(Z, M)  
M  
Z 0 1  
0 299 0  
1 228 372  
> psw.boot(Z, M, Y, X)  
tau10 tau00  
est 0.1694979 -0.09904909  
se 0.1042405 0.15612983
```

The point estimator $\hat{\tau}(1,0)$ does not differ much from the one based on the IV analysis. The point estimator $\hat{\tau}(0,0)$ is close to zero with a large standard error. In this example, exclusion restriction seems a reasonable assumption.

# 26.5.3 Extensions

Follmann (2000), Hill et al. (2002), Jo and Stuart (2009), Jo et al. (2011) and Stuart and Jo (2015) started the literature of using the principal score to identify causal effects within principal strata. Ding and Lu (2017) provided a theoretical foundation for this strategy. They proved Theorem 26.2 as well as a more general version under monotonicity; see Problem 26.2.

# 26.6 Other methods

To estimate principal stratification average causal effects without the exclusion restriction assumption, Zhang et al. (2009) proposed to use the Normal mixture models. However, the inference based on the Normal mixture models can be quite fragile. A strategy is to use additional information to improve the inference under some restrictions (Ding et al., 2011; Mealli and Pacini, 2013; Mattei et al., 2013; Jiang et al., 2016).

Conceptually, the principal stratification framework works for general $M$ . A multi-valued $M$ generates many latent principal strata, and a continuous $M$ generates infinitely many latent principal strata. In those cases, identifying the probability of the principal strata is non-trivial in the first place let alone identifying the principal stratification average causal effects. Jiang and Ding (2021) reviewed some useful strategies.

# 26.7 Homework problems

26.1 Complete the proof of Theorem 26.2

Prove the result for $\tau(0,0)$ in Theorem 26.2.

26.2 Principal score method under monotonicity

This problem extends Theorem 26.2, with Assumption 26.3 replaced by Assumption 26.2 and Assumption 26.4 replaced by Assumption 26.5 below.

Assumption 26.5 (principal ignorability) We have

$$
E \{Y (1) \mid M (1) = 1, M (0) = 0, X \} = E \{Y (1) \mid M (1) = 1, M (0) = 1, X \}
$$

and

$$
E \{Y (0) \mid M (1) = 1, M (0) = 0, X \} = E \{Y (0) \mid M (1) = 0, M (0) = 0, X \}.
$$

Theorem 26.3 Under Assumptions 26.1, 26.2 and 26.5,

1.the conditional and marginal principal scores can be identified by

$$
\pi_ {(0, 0)} (X) = \operatorname * {p r} (M = 0 \mid Z = 1, X),
$$

$$
\pi_ {(1, 1)} (X) = \operatorname * {p r} (M = 1 \mid Z = 0, X),
$$

$$
\pi_ {(1, 0)} (X) = \operatorname * {p r} (M = 1 \mid Z = 1, X) - \operatorname * {p r} (M = 1 \mid Z = 0, X).
$$

and

$$
\pi_ {(0, 0)} = \operatorname {p r} (M = 0 \mid Z = 1),
$$

$$
\pi_ {(1, 1)} = \operatorname {p r} (M = 1 \mid Z = 0),
$$

$$
\pi_ {(1, 0)} = \operatorname {p r} (M = 1 \mid Z = 1) - \operatorname {p r} (M = 1 \mid Z = 0)
$$

respectively;

2.the principal stratification average causal effects can be identified by

$$
\begin{array}{l} \tau (1, 0) = E \left\{w _ {1, (1, 0)} (X) Y \mid Z = 1, M = 1 \right\} \\ - E \left\{w _ {0, (1, 0)} (X) Y \mid Z = 0, M = 0 \right\}, \\ \end{array}
$$

$$
\tau (0, 0) = E (Y \mid Z = 1, M = 0) - E \left\{w _ {0, (0, 0)} (X) Y \mid Z = 0, M = 0 \right\},
$$

$$
\tau (1, 1) = E \left\{w _ {1, (1, 1)} (X) Y \mid Z = 1, M = 1 \right\} - E (Y \mid Z = 0, M = 1)
$$

with

$$
w _ {1, (1, 0)} (X) = \frac {\pi_ {(1 , 0)} (X)}{\pi_ {(1 , 0)} (X) + \pi_ {(1 , 1)} (X)} \Big / \frac {\pi_ {(1 , 0)}}{\pi_ {(1 , 0)} + \pi_ {(1 , 1)}},
$$

$$
w _ {0, (1, 0)} (X) = \frac {\pi_ {(1 , 0)} (X)}{\pi_ {(1 , 0)} (X) + \pi_ {(0 , 0)} (X)} \Big / \frac {\pi_ {(1 , 0)}}{\pi_ {(1 , 0)} + \pi_ {(0 , 0)}},
$$

$$
w _ {0, (0, 0)} (X) = \frac {\pi_ {(0 , 0)} (X)}{\pi_ {(1 , 0)} (X) + \pi_ {(0 , 0)} (X)} \Big / \frac {\pi_ {(0 , 0)}}{\pi_ {(1 , 0)} + \pi_ {(0 , 0)}},
$$

$$
w _ {1, (1, 1)} (X) = \frac {\pi_ {(1 , 1)} (X)}{\pi_ {(1 , 0)} (X) + \pi_ {(1 , 1)} (X)} \Big / \frac {\pi_ {(1 , 1)}}{\pi_ {(1 , 0)} + \pi_ {(1 , 1)}}.
$$

Remark: Based on Theorem 26.3, we can construct weighting estimators. Theorem 26.3 is Proposition 2 in Ding and Lu (2017), which also provided more details for the estimation.

# 26.3 Principal score method in observational studies

This problem extends Theorem 26.2, with Assumption 26.1 replaced by the ignorability assumption below.

Assumption 26.6 $Z \perp \{M(1), M(0), Y(1), Y(0)\} \mid X$ .

Recall the definition of the propensity score $e(X) = \operatorname{pr}(Z = 1 \mid X)$ . We have the following identification result.

Theorem 26.4 Under Assumptions 26.6, 26.3 and 26.4,

1.the conditional and marginal probabilities of $M(1)$ , $\pi(X) = \operatorname{pr}\{M(1) = 1 \mid X\}$ and $\pi = \operatorname{pr}\{M(1) = 1\}$ , can be identified by

$$
\pi (X) = \operatorname {p r} (M = 1 \mid Z = 1, X)
$$

and

$$
\pi = E \left\{\operatorname {p r} (M = 1 \mid Z = 1, X) \right\}
$$

respectively;

2.the principal stratification average causal effects can be identified by

$$
\tau (1, 0) = E \left\{\frac {M}{\pi} \frac {Z}{e (X)} Y \right\} - E \left\{\frac {\pi (X)}{\pi} \frac {1 - Z}{1 - e (X)} Y \right\}
$$

and

$$
\tau (0, 0) = E \left\{\frac {1 - M}{1 - \pi} \frac {Z}{e (X)} Y \right\} - E \left\{\frac {1 - \pi (X)}{1 - \pi} \frac {1 - Z}{1 - e (X)} Y \right\}.
$$

Prove Theorem 26.4.

# 26.4 General principal score method

Extend Theorems 26.3 and 26.4 under Assumptions 26.6, 26.2 and 26.5. Remark: See Jiang et al. (2022).

# 26.5 Recommended reading

Frangakis and Rubin (2002) proposed the principal stratification framework. Zhang and Rubin (2003) derived large-sample bounds on the survivor average causal effect. Jiang and Ding (2021) reviewed various strategies to identify the causal effects within principal strata. Jiang et al. (2022) gave a unified discussion of this strategy for observational studies and proposed multiply robust estimators for causal effects within principal strata.

# Mediation Analysis: Natural Direct and Indirect Effects

With an intermediate variable $M$ between the treatment $Z$ and outcome $Y$ , the causal effects within principal strata defined by $U = \{M(1), M(0)\}$ can assess the treatment effect heterogeneity across latent groups $U$ . When $M$ is indeed on the causal pathway from $Z$ to $Y$ , causal effects within some principal strata, $\tau(1,1)$ and $\tau(0,0)$ , can give information about the direct effect of $Z$ on $Y$ . However, these direct effects are only for two latent groups. The causal effects within the other two principal strata, $\tau(1,0)$ and $\tau(0,1)$ , contain both direct and indirect effects. Fundamentally, principal stratification does not provide any information about the indirect effect of $Z$ on $Y$ through $M$ because it does not even assume that $M$ can be intervened.

In the above discussion, I use the notions of "direct effect" and "indirect effect" in a casual way. When $M$ lies on the pathway from $Z$ to $Y$ , researchers often want to assess the extent to which the effect of $Z$ on $Y$ is through $M$ and the extent to which the effect is through other pathways. This is called mediation analysis. It is the topic of this chapter.

# 27.1 Motivating Examples

In mediation analysis, we have a treatment $Z$ , an outcome $Y$ , a mediator $M$ and some background covariates $X$ . Figure 27.1 illustrates their relationship. Below we give some concrete examples.

![](images/7a750eca6f6f38d134e7122ef0a4ef19055cc9e1f7e92cd51d0ff918c47b526d.jpg)  
FIGURE 27.1: Causal diagram for mediation analysis

Example 27.1 VanderWeele et al. (2012) conducted mediation analysis to assess the extent to which the effect of variants on chromosome 15q25.1 on lung cancer is mediated through smoking and the extent to which it operates through other causal pathways<sup>1</sup>. The exposure levels correspond to changes from 0 to $2C$ alleles, smoking intensity is measured by the square root of cigarettes per day, and the outcome is the lung cancer indicator. VanderWeele et al. (2012)'s study contained many sociodemographic covariates.

Example 27.2 Rudolph et al. (2018) studied the causal mechanism from neighborhood poverty to adolescent substance use, mediated by the school and peer environment. They used data from the National Comorbidity Survey Replication Adolescent Supplement, a nationally representative survey of U.S. adolescents conducted during 2001-2004. The treatment is the binary indicator of neighborhood disadvantage, defined as living in the lowest tertile of neighborhood socioeconomic status based on data from the 2000 U.S. Census. Four binary mediators are measures of school and peer environments, and six binary outcomes are measures of substance use. Baseline covariates included the adolescent's sex, age, race, immigration generation, family income, etc.

Example 27.3 The mediation package in $R$ contains a dataset called jobs, which is from JOBS II, a randomized field experiment that investigates the efficacy of a job training intervention on unemployed workers. We used this dataset in Chapter 21.5. The program is designed to not only increase reemployment among the unemployed but also enhance the mental health of the job seekers. It is therefore of interest to assess the indirect effect of the intervention on mental health through job search efficacy and its direct effect acting through other pathways. We will revisit this example in Chapter 27.4.2 later.

# 27.2 Nested Potential Outcomes

# 27.2.1 Natural Direct and Indirect Effects

Below we drop the index $i$ for unit $i$ and assume all random variables are IID draws from a superpopulation. For simplicity, we focus on a binary treatment $Z$ .

We first consider the hypothetical intervention on $z$ and define potential mediators and outcomes corresponding to the intervention on $z$ :

$$
\{M (z), Y (z): z = 0, 1 \}.
$$

We then consider hypothetical intervention on both $z$ and $m$ and define po

tential outcomes corresponding to the interventions on $z$ and $m$ :

$$
\{Y (z, m): z = 0, 1; m \in \mathcal {M} \},
$$

where $\mathcal{M}$ contains all possible values of $m$ . Robins and Greenland (1992) and Pearl (2001) further consider the nested potential outcomes corresponding to intervention on $z$ and $m = M(z')$ :

$$
\left\{Y \left(z, M _ {z ^ {\prime}}\right): z = 0, 1; z ^ {\prime} = 0, 1 \right\}
$$

where I write $M(z')$ as $M_{z'}$ to avoid excessive parentheses. The notation $Y(z, M_{z'})$ is the hypothetical outcome if the treatment were set at level $z$ and the mediator were set at its potential level $M(z')$ under treatment $z'$ . Importantly, $z$ and $z'$ can be different. With a binary treatment, we have four nested potential outcomes in total:

$$
\{Y (1, M _ {1}), Y (1, M _ {0}), Y (0, M _ {1}), Y (0, M _ {0}) \}.
$$

The nested potential outcome $Y(1, M_1)$ is the hypothetical outcome if the treatment were set at $z = 1$ and the mediator were set at what would happen under $z = 1$ . Similarly, $Y(0, M_0)$ is the outcome if the treatment were set at $z = 0$ and the mediator were set at what would happen under $z = 0$ . It would be surprising if $Y(1, M_1) \neq Y(1)$ or $Y(0, M_0) \neq Y(0)$ . Therefore, we make the following composition assumption throughout this chapter.

Assumption 27.1 (composition) $Y(z, M_z) = Y(z)$ for $z = 0, 1$ .

The composition assumption cannot be proved. It is indeed an assumption. Without causing philosophical debates, we can even define $Y(1)$ as $Y(1, M_1)$ , and define $Y(0)$ as $Y(0, M_0)$ . Then by definition, Assumption 27.1 holds.

The nested potential outcome $Y(1, M_0)$ is the hypothetical outcome if the unit received treatment 1 but its mediator were set at its natural value $M_0$ without the treatment. Similarly, $Y(0, M_1)$ is the hypothetical outcome if the unit received control 0 but its mediator were set at its natural value $M_1$ under the treatment. They are two cross-world counterfactual terms and are useful for defining the direct and indirect effects.

Definition 27.1 (total, direct and indirect effects) Define the total effect of the treatment on the outcome as

$$
\tau = E \{Y (1) - Y (0) \}.
$$

Define the natural direct effect as

$$
\mathrm {N D E} = E \left\{Y \left(1, M _ {0}\right) - Y \left(0, M _ {0}\right) \right\}.
$$

Define the natural indirect effect as

$$
\mathrm {N I E} = E \left\{Y \left(1, M _ {1}\right) - Y \left(1, M _ {0}\right) \right\}.
$$

The total effect is the standard average causal effect of $Z$ on $Y$ . The natural direct effect measures the effect of the treatment on the outcome if the mediator were set at the natural value $M_0$ without the intervention. The natural indirect effect measures the effect of the treatment through changing the mediator if the treatment itself were set at $z = 1$ . Under the composition assumption, the natural direct and indirect effects reduce to

$$
\mathrm {N D E} = E \{Y (1, M _ {0}) - Y (0) \}, \quad \mathrm {N I E} = E \{Y (1) - Y (1, M _ {0}) \},
$$

and therefore, we can decompose the total effect as the sum of the natural direct and indirect effects.

Proposition 27.1 By Definition 27.1 and Assumption 27.1, we have

$$
\tau = \mathrm {N D E} + \mathrm {N I E}.
$$

Mathematically, we can also define the natural indirect effect as $E\{Y(0,M_1) - Y(0,M_0)\}$ where the treatment is fixed at 0. However, this definition does not lead to the decomposition in Proposition 27.1.

Unfortunately, the nest potential outcome $Y(1, M_0)$ is not an easy quantity to understand due to the cross-world nature of the interventions: the treatment is set at $z = 1$ but the mediator is set at its natural value $M_0$ under treatment $z = 0$ . Clearly, these two interventions on the treatment cannot simultaneously happen in any realized experiment. To understand the cross-world potential outcome $Y(1, M_0)$ , we need to imagine the existence of parallel worlds as shown in Figure 27.2. Let's focus on $Y(1, M_0)$ . When the treatment is set at $z = 1$ , the mediator must take value $M_1$ . If at the same time, we want to set the mediator at $m = M_0$ , we must know the value of $M_0$ for the same unit from another experiment in the parallel world. This can be an unrealistic physical experiment because it requires that the same unit is intervened at two different levels of the treatment. Under some strong assumptions about the homogeneity of units, we may use another unit's mediator value under control as a proxy for $M_0$ .

# 27.2.2 Metaphysics or Science

Causal inference is hard, and there is no agreement even on its mathematical notation. Robins and Greenland (1992) and Pearl (2001) used the nested potential outcomes to define the natural direct and indirect effects. However, Frangakis and Rubin (2002) called $Y(1,M_0)$ and $Y(0,M_1)$ a priori counterfactuals because we can not observe them in any physical experiments. In this sense, they do not exist a priori. According to Popper (1963), a way to distinguish science and metaphysics is the falsifiability of the statements. That is, if a statement is not falsifiable based on any physical experiments or observations, then it is not a scientific but rather a metaphysical statement. Because we can not observe $Y(1,M_0)$ and $Y(0,M_1)$ in any experiments, we can not

falsify any statements involving them except for the trivial ones (e.g., some outcomes are binary, or continuous, or bounded). Therefore, a strict Popperian statistician would view mediation analysis as metaphysics.

More strikingly, Dawid (2000) criticized the potential outcomes framework to be metaphysical, and he called Rubin's "Science Table" defined in Chapter 2.2 a "metaphysical array." This is a critique on not only the a priori counterfactuals $Y(1, M_0)$ and $Y(0, M_1)$ but also the simpler potential outcomes $Y(1)$ and $Y(0)$ . Dawid (2000) argued that because we can never observe $Y(1)$ and $Y(0)$ jointly, then introducing the notation $\{Y(1), Y(0)\}$ is a metaphysical activity. He is correct about the metaphysical nature of the joint distribution of $\operatorname{pr}\{Y(1), Y(0)\}$ , but he is incorrect about the marginal distributions. Based on the observed data, we indeed can falsify some statements about the marginal distributions, although we cannot falsify any statements about the joint distribution. Therefore, even according to Popper (1963), Rubin's Science Table is not metaphysical because it has some nontrivial falsifiable implications although not all implications are falsifiable. This is the fundamental difference between $\{Y(1), Y(0)\}$ and $\{Y(1, M_0), Y(0, M_1)\}$ .

![](images/588d7631fd73615f7b0cbb182c61bd55111caeebe2310175808db3bfc6b53442.jpg)  
FIGURE 27.2: Cross-world potential outcomes $Y(1, M_0)$ and $Y(0, M_1)$

This is often a loose inequality. Unfortunately, we do not have any information beyond this inequality without imposing additional assumptions.

# 27.3 The Mediation Formula

Pearl (2001)'s mediation formula relies on the following four assumptions. The first three essentially assume that the treatment and the mediator are both randomized conditional on observed covariates.

Assumption 27.2 There is no treatment-outcome confounding:

$$
Z \bot Y (z, m) \mid X
$$

for all $z$ and $m$ .

Assumption 27.3 There is no mediator-outcome confounding:

$$
M \bot Y (z, m) \mid (X, Z)
$$

for all $z$ and $m$ .

Assumptions 27.2 and 27.3 together are often called sequential ignorance. They are equivalent to the assumption that $(Z,M)$ are jointly randomized conditioning on $X$ :

$$
(Z, M) \perp Y (z, m) \mid X \tag {27.1}
$$

for all $z$ and $m$ . I leave the proof of (27.1) as Problem 27.2.

Assumption 27.4 There is no treatment-mediator confounding:

$$
Z \bot M (z) \mid X
$$

for all $z$ .

The last assumption is the cross-world independence.

Assumption 27.5 There is no cross-world independence between the potential outcomes and potential mediators:

$$
Y (z, m) \bot M \left(z ^ {\prime}\right) \mid X
$$

for all $z, z'$ and $m$ .

Assumptions 27.2-27.4 are very strong, but at least they hold under experiments with randomized treatment and mediator. Assumption 27.5 is stronger because no physical experiment can ensure it. Because we can never observe $Y(z,m)$ and $M(z^{\prime})$ in any experiment if $z\neq z^{\prime}$ , Assumption 27.5 can never be validated so it is fundamentally metaphysical.

I give an example below in which Assumptions 27.2-27.5 all hold.

Example 27.4 Given $X$ , we generate

$$
Z = 1 \{g _ {Z} (X, \varepsilon_ {Z}) \geq 0 \},
$$

$$
M (z) = 1 \{g _ {M} (X, z, \varepsilon_ {M}) \geq 0 \},
$$

$$
Y (z, m) = g _ {Y} (X, z, m, \varepsilon_ {Y}),
$$

for $z, m = 0,1$ , where $\varepsilon_Z, \varepsilon_M, \varepsilon_Y$ are all independent random errors. Consequently, we generate the observed values of $M$ and $Y$ from

$$
M = M (Z) = 1 \{g _ {M} (X, Z, \varepsilon_ {M}) \geq 0 \},
$$

$$
Y = Y (Z, M) = g _ {Y} (X, Z, M, \varepsilon_ {Y}).
$$

We can verify that Assumptions 27.2-27.5 hold under this data-generating process. On the contrary, if we allow $\varepsilon_{M}$ and $\varepsilon_{Y}$ to be $\varepsilon_{M}(z)$ and $\varepsilon_{Y}(z,m)$ , then Assumptions 27.2-27.5 can fail. See Problem 27.3 for more details.

Pearl (2001) proved the following key result for mediation analysis.

Theorem 27.1 Under Assumptions 27.2-27.5, we have

$$
E \left\{Y \left(z, M _ {z ^ {\prime}}\right) \mid X = x \right\} = \sum_ {m} E (Y \mid Z = z, M = m, X = x) \Pr (M = m \mid Z = z ^ {\prime}, X = x)
$$

and therefore,

$$
\begin{array}{l} E \left\{Y \left(z, M _ {z ^ {\prime}}\right) \right\} \\ = \sum_ {x} E \left\{Y \left(z, M _ {z ^ {\prime}}\right) \mid X = x \right\} \Pr (X = x) \\ = \sum_ {x} \sum_ {m} E (Y \mid Z = z, M = m, X = x) \Pr (M = m \mid Z = z ^ {\prime}, X = x) \Pr (X = x). \\ \end{array}
$$

Theorem 27.1 assumes that both $M$ and $X$ are discrete. With general $M$ and $X$ , the mediation formulas become

$$
E \left\{Y \left(z, M _ {z ^ {\prime}}\right) \mid X = x \right\} = \int E (Y \mid Z = z, M = m, X = x) f (m \mid Z = z ^ {\prime}, X = x) d m
$$

and

$$
\begin{array}{l} E \{Y (z, M _ {z ^ {\prime}}) \} \\ = \int E \left\{Y \left(z, M _ {z ^ {\prime}}\right) \mid X = x \right\} f (x) d x \\ = \int \int E (Y \mid Z = z, M = m, X = x) f (m \mid Z = z ^ {\prime}, X = x) f (x) \mathrm {d} m \mathrm {d} x. \\ \end{array}
$$

From Theorem 27.1, the identification formulas for the means of the nested potential outcomes depend on the conditional mean of the outcome given the

treatment, mediator, and covariates, as well as the conditional mean of the mediator given the treatment and covariates. We need to evaluate these two conditional means at different treatment levels if the nested potential outcome involves cross-world interventions.

If we drop the cross-world independence assumption, we can modify the definition of the natural direct and indirect effects and the same formulas hold. See Problem 27.11 for more details.

I give the proof below.

Proof of Theorem 27.1: By the tower property, $E\{Y(z,M_{z'})\} = E[E\{Y(z,M_{z'}) \mid X\}]$ , so we need only to prove the formula for $E\{Y(z,M_{z'}) \mid X = x\}$ . Starting with the law of total probability, we have

$$
\begin{array}{l} E \left\{Y \left(z, M _ {z ^ {\prime}}\right) \mid X = x \right\} \\ = \sum_ {m} E \left\{Y \left(z, M _ {z ^ {\prime}}\right) \mid M _ {z ^ {\prime}} = m, X = x \right\} \Pr \left(M _ {z ^ {\prime}} = m \mid X = x\right) \\ = \sum_ {m} E \left\{Y (z, m) \mid M _ {z ^ {\prime}} = m, X = x \right\} \Pr \left(M _ {z ^ {\prime}} = m \mid X = x\right) \\ = \sum_ {m} \underbrace {E \left\{Y (z , m) \mid X = x \right\}} _ {\text {A s s u m p t i o n 2 7 . 5}} \underbrace {\operatorname {p r} \left(M = m \mid Z = z ^ {\prime} , X = x\right)} _ {\text {A s s u m p t i o n 2 7 . 4}} \\ = \sum_ {m} \underbrace {E (Y \mid Z = z , M = m , X = x)} _ {\text {A s s u m p t i o n s 2 7 . 2 a n d 2 7 . 3}} \operatorname * {p r} (M = m \mid Z = z ^ {\prime}, X = x). \\ \end{array}
$$

![](images/5f62998d98531e5bb647a64a8fdad88b500a3a88cb93767cfe8e1e571411771a.jpg)

The above proof is trivial from a mathematical perspective. It illustrates the necessity of Assumptions 27.2-27.5.

Conditional on $X = x$ , the mediation formulas for $Y(1, M_1)$ and $Y(0, M_0)$ simplify to

$$
\begin{array}{l} E \{Y (1, M _ {1}) \mid X = x \} \\ = \sum_ {m} E (Y \mid Z = 1, M = m, X = x) \Pr (M = m \mid Z = 1, X = x) \\ = E (Y \mid Z = 1, X = x) \\ \end{array}
$$

and

$$
\begin{array}{l} E \{Y (0, M _ {0}) \mid X = x \} \\ = \sum_ {m} E (Y \mid Z = 0, M = m, X = x) \Pr (M = m \mid Z = 0, X = x) \\ = E (Y \mid Z = 0, X = x) \\ \end{array}
$$

based on the law of total probability; the mediation formula for $Y(1, M_0)$ simplifies to

$$
\begin{array}{l} E \{Y (1, M _ {0}) \mid X = x \} \\ = \sum_ {m} E (Y \mid Z = 1, M = m, X = x) \operatorname {p r} (M = m \mid Z = 0, X = x), \\ \end{array}
$$

where the conditional expectation of the outcome is given $Z = 1$ but the conditional distribution of the mediator is given $Z = 0$ . This leads to the identification formulas of the natural direct and indirect effects.

Corollary 27.1 Under Assumptions 27.2-27.5, the conditional natural direct and indirect effects are identified by

$$
\begin{array}{l} \mathrm {N D E} (x) = E \left\{Y \left(1, M _ {0}\right) - Y \left(0, M _ {0}\right) \mid X = x \right\} \\ = \sum_ {m} \left\{E (Y \mid Z = 1, M = m, X = x) - E (Y \mid Z = 0, M = m, X = x) \right\} \\ \times \Pr (M = m \mid Z = 0, X = x) \\ \end{array}
$$

and

$$
\begin{array}{l} \operatorname {N I E} (x) = E \left\{Y \left(1, M _ {1}\right) - Y \left(1, M _ {0}\right) \mid X = x \right\} \\ = \sum_ {m} E (Y \mid Z = 1, M = m, X = x) \\ \times \left\{\operatorname {p r} (M = m \mid Z = 1, X = x) - \operatorname {p r} (M = m \mid Z = 0, X = x) \right\}; \\ \end{array}
$$

the unconditional ones can be identified by $\mathrm{NDE} = \sum_{x}\mathrm{NDE}(x)\mathrm{pr}(X = x)$ and $\mathrm{NIE} = \sum_{x}\mathrm{NIE}(x)\mathrm{pr}(X = x)$ .

As a special case, with a binary $M$ , the formula of the NIE reduces to a product form below.

Corollary 27.2 Under Assumptions 27.2-27.5, for a binary mediator $M$ , we have

$$
\operatorname {N I E} (x) = \tau_ {Z \rightarrow M} (x) \tau_ {M \rightarrow Y} (1, x)
$$

and $\mathrm{NIE} = E\{\mathrm{NIE}(X)\}$ , where

$$
\tau_ {Z \rightarrow M} (x) = \operatorname * {p r} (M = 1 \mid Z = 1, X = x) - \operatorname * {p r} (M = 1 \mid Z = 0, X = x).
$$

and

$$
\tau_ {M \rightarrow Y} (z, x) = E (Y \mid Z = z, M = 1, X = x) - E (Y \mid Z = z, M = 0, X = x)
$$

I leave the proof of Corollary 27.2 as Problem 27.6. Corollary 27.2 gives a simple formula in the case of a binary $M$ . With randomized $Z$ conditional on $X$ , we can view $\tau_{Z \to M}(x)$ as the conditional average causal effect of $Z$ on $M$ . With randomized $M$ conditional on $(X, Z)$ , we can view $\tau_{M \to Y}(z, x)$ as the conditional average causal effect of $M$ on $Y$ . The conditional natural indirect effect equals their product. This is coherent with our intuition that the indirect effect acts from $Z$ to $M$ and then from $M$ to $Y$ .

# 27.4 The Mediation Formula Under Linear Models

Theorem 27.1 gives the nonparametric identification formula for mediation analysis. It allows us to derive various formulas for mediation analysis under different models. I will introduce the famous Baron-Kenny method under linear models below. VanderWeele (2015) gives explicit formulas for the natural direct and indirect effects for many commonly used models. I relegate the details of other models to Section 27.6.

# 27.4.1 The Baron-Kenny Method

![](images/a4fdbb57cd0e6a293c77b3eaa77bf0ea8465903a4dbfae77b735245c6dcd6378.jpg)  
FIGURE 27.3: The Baron-Kenny method for mediation under linear models

indirect effect: $\beta_{1}\theta_{2}$

direct effect: $\theta_{1}$

The Baron-Kenny method assumes the following linear models for the mediator and outcome given the treatment and covariates.

Assumption 27.6 (linear models for the Baron-Kenny method) Both the mediator and outcome follow linear models:

$$
\left\{ \begin{array}{r c l} E (M \mid Z, X) & = & \beta_ {0} + \beta_ {1} Z + \beta_ {2} ^ {\mathsf {T}} X, \\ E (Y \mid Z, M, X) & = & \theta_ {0} + \theta_ {1} Z + \theta_ {2} M + \theta_ {4} ^ {\mathsf {T}} X. \end{array} \right.
$$

Under these linear models, the formulas for the natural direct and indirect effects simplify to functions of the coefficients.

Corollary 27.3 (Baron-Kenny formulas for mediation) Under Assumptions 27.2-27.5 and 27.6, we have

$$
\mathrm {N D E} = \theta_ {1}, \quad \mathrm {N I E} = \theta_ {2} \beta_ {1}.
$$

The formulas in Corollary 27.3 are intuitive based on Figure 27.3. The

direct effect equals the coefficient on the path $Z \to Y$ , and the indirect effect equals the product of the coefficients on the path $Z \to M \to Y$ . I give the proof below based on Theorem 27.1.

Proof of Corollary 27.3: The conditional NDE equals

$$
\mathrm {N D E} (x) = \sum_ {m} \theta_ {1} \operatorname {p r} (M = m \mid Z = 0, X = x) = \theta_ {1}
$$

and the conditional NIE equals

$$
\begin{array}{l} \operatorname {N I E} (x) = \sum_ {m} \left(\theta_ {0} + \theta_ {1} + \theta_ {2} m + \theta_ {4} ^ {\top} x\right) \\ \times \left\{\operatorname {p r} (M = m \mid Z = 1, X = x) - \operatorname {p r} (M = m \mid Z = 0, X = x) \right\} \\ = \theta_ {2} \left\{E (M = m \mid Z = 1, X = x) - E (M = m \mid Z = 0, X = x) \right\} \\ = \theta_ {2} \beta_ {1}, \\ \end{array}
$$

which do not depend on $x$ . Therefore, they are also the formulas for the unconditional natural direct and indirect effects.

If we obtain OLS estimators of these coefficients, we can estimate the direct and indirect effects by

$$
\mathrm {N} \hat {\mathrm {D E}} = \hat {\theta} _ {1}, \qquad \mathrm {N} \hat {\mathrm {I E}} = \hat {\theta} _ {2} \hat {\beta} _ {1},
$$

which is called the Baron-Kenny method (Judd and Kenny, 1981; Baron and Kenny, 1986) although it had several antecedents (e.g., Hyman, 1955; Alwin and Hauser, 1975; Judd and Kenny, 1981; Sobel, 1982).

Standard software packages report the standard error of NDE from OLS. Sobel (1982, 1986) used the delta method to obtain the standard error of NIE. Based on the formula in Example A.2, the asymptotic variance of $\hat{\theta}_2\hat{\beta}_1$ equals $\mathrm{var}(\hat{\theta}_2)\beta_1^2 +\theta_2^2\mathrm{var}(\hat{\beta}_1)$ . So the estimated variance is

$$
\hat {\operatorname {v a r}} (\hat {\theta} _ {2}) \hat {\beta} _ {1} ^ {2} + \hat {\theta} _ {2} ^ {2} \hat {\operatorname {v a r}} (\hat {\beta} _ {1}).
$$

Testing the null hypothesis of NIE based on $\hat{\theta}_2\hat{\beta}_1$ and the estimated variance above is called Sobel's test in the literature of mediation analysis.

# 27.4.2 An Example

We can easily implement the Baron-Kenny method via the following code.

```r
library("car")   
BKmediation \(=\) function(Z,M,Y,X)   
{   
#two regressions and coefficients mediator.reg \(\equiv\) lm(M\~Z+X) mediator.Zcoef \(\equiv\) mediator.reg\\(coef[2] mediator.Zse \)\equiv\( sqrt(hccm(mediator.reg)[2,2]) 
```

```txt
outcome.reg = lm(Y ~ Z + M + X)
outcome.Zcoef = outcome.reg$coef[2]
outcome.Zse = sqrt(hccm(outcome.reg)[2, 2])
outcome.Mcoef = outcome.reg$coef[3]
outcome.Mse = sqrt(hccm(outcome.reg)[3, 3])
# # Baron-Kenny point estimates
NDE = outcome.Zcoef
NIE = outcome.Mcoef*mediator.Zcoef
# # Sobel's variance estimate based the delta method
NDE.se = outcome.Zse
NIE.se = sqrt(outcome.Mse^2*mediator.Zcoef^2 +
		int outcome.Mcoef^2*mediator.Zse^2)
res = matrix(c(NDE, NIE,
				NDE.se, NIE.se,
				NDE/NDE.se, NIE/NIE.se),
				2, 3)
rownames(res) = c("NDE", "NIE")
colnames(res) = c("est", "se", "t")
res 
```

Revisiting Example 27.3, we obtain the following estimates for the direct and indirect effects:

```txt
> jobsdata = read.csv("jobsdata.csv")
> Z = jobsdata\(treat
> M = jobsdata\)job Seek
> Y = jobsdata\)depress2
> getX = lm(treat ~ econ-hard + depress1 +
+ sex + age + occp + marital +
+ nonwhite + educ + income,
+ data = jobsdata)
> X = model.matrix(getX)[, -1]
> res = BKmediation(Z, M, Y, X)
> round(res, 3)
est se t
NDE -0.037 0.042 -0.885
NIE -0.014 0.009 -1.528 
```

Both the estimates for the direct and indirect effects are negative although they are insignificant.

# 27.5 Sensitivity analysis

Mediation analysis relies on strong and untestable assumptions. One crucial assumption is that there is no unmeasured confounding among the treatment, mediator, and outcome. Various sensitivity analysis methods appeared in the literature. In particular, Ding and Vanderweele (2016) proposed Cornfield-type sensitivity bounds, and Zhang and Ding (2022) proposed a sensitivity analysis method tailored to the Baron-Kenny method based on linear structural equation models. These are beyond the scope of this book.

# 27.6 Homework problems

27.1 Robins and Greenland (1992)'s clarification of the units based on nested potential outcomes

Assume $(Z,M,Y)$ are all binary. Based on the joint value of

$$
M (1), M (0), Y (1, M _ {1}), Y (1, M _ {0}), Y (0, M _ {1}), Y (0, M _ {0}),
$$

how many types of units do we have?

If we assume monotonicity of $Z$ on $M$ , that is,

$$
M (1) \geq M (0),
$$

then how many types of units do we have?

If we further assume monotonicity of $Z$ and $M$ on $Y$ , that is,

$$
Y (1, m) \geq Y (0, m), \quad Y (z, 1) \geq Y (z, 0)
$$

for all $z$ and $m$ , then how many types of units do we have?

27.2 Sequential randomization and joint randomization

Show (27.1) is equivalent to Assumptions 27.2 and 27.3.

27.3 Verifying the assumptions for mediation analysis

Show that Assumptions 27.2-27.5 hold under the data generating process in Example 27.4. Also show that if we allow $\varepsilon_{M}$ and $\varepsilon_{Y}$ to be $\varepsilon_{M}(z)$ and $\varepsilon_{Y}(z,m)$ , then Assumptions 27.2-27.5 can fail.

27.4 Another set of assumptions for the mediation formula

Imai et al. (2010) invoked the following set of assumptions to derive the mediation formula.

Assumption 27.7 We have

$$
\{Y (z, m), M \left(z ^ {\prime}\right) \} \bot Z \mid X
$$

and

$$
Y (z, m) \bot M \left(z ^ {\prime}\right) \mid \left(Z = z ^ {\prime}, X\right)
$$

for all $z, z', m$ .

Theorem 27.2 Under Assumption 27.7, the mediation formula in Theorem 27.1 holds.

Prove Theorem 27.2.

27.5 Difference method and product method are identical

In the main text, we first obtain the OLS fits

$$
\left\{ \begin{array}{r c l} \hat {M} _ {i} & = & \hat {\beta} _ {0} + \hat {\beta} _ {1} Z _ {i} + \hat {\beta} _ {2} ^ {\mathsf {T}} X _ {i}, \\ \hat {Y} _ {i} & = & \hat {\theta} _ {0} + \hat {\theta} _ {1} Z _ {i} + \hat {\theta} _ {2} M _ {i} + \hat {\theta} _ {4} ^ {\mathsf {T}} X _ {i}. \end{array} \right.
$$

The estimate for the NIE is the product $\hat{\theta}_2\hat{\beta}_1$ , which is called the product method.

Alternatively, we can first obtain OLS fits:

$$
\left\{ \begin{array}{l c l} \hat {Y _ {i}} & = & \hat {\alpha} _ {0} + \hat {\alpha} _ {1} Z _ {i} + \hat {\alpha} _ {1} ^ {\mathsf {T}} X _ {i}, \\ \hat {Y _ {i}} & = & \hat {\theta} _ {0} + \hat {\theta} _ {1} Z _ {i} + \hat {\theta} _ {2} M _ {i} + \hat {\theta} _ {4} ^ {\mathsf {T}} X _ {i}. \end{array} \right.
$$

Another estimate for the NIE is the difference $\hat{\alpha}_1 - \hat{\theta}_1$ , which is called the difference method.

Show that $\hat{\alpha}_{1} - \hat{\theta}_{1} = \hat{\theta}_{2}\hat{\beta}_{1}$

Remark: Recall Cochran's formula in Problem 16.2.

27.6 Natural indirect effect with a binary mediator

Prove Corollary 27.2.

27.7 With treatment-outcome interaction on the outcome

VanderWeele (2015) suggested using the following linear models:

$$
\left\{ \begin{array}{r c l} E (M \mid Z, X) & = & \beta_ {0} + \beta_ {1} Z + \beta_ {2} ^ {\mathsf {T}} X, \\ E (Y \mid Z, M, X) & = & \theta_ {0} + \theta_ {1} Z + \theta_ {2} M + \theta_ {3} Z M + \theta_ {4} ^ {\mathsf {T}} X, \end{array} \right.
$$

where the outcome model has the interaction term between the treatment and the mediator.

Under the above linear models, show that

$$
\mathrm {N D E} = \theta_ {1} + \theta_ {3} \left\{\beta_ {0} + \beta_ {2} ^ {\top} E (X) \right\}, \qquad \mathrm {N I E} = \left(\theta_ {2} + \theta_ {3}\right) \beta_ {1}.
$$

How do we estimate NDE and NIE with IID data?

Remark: Consider the simple case with a binary $Z$ and binary $M$ . Under the linear models, the average causal effect of $Z$ of $M$ equals $\beta_{1}$ , and the average causal effect of $M$ on $Y$ equals $\theta_{2} + \theta_{3}E(Z)$ . Therefore, it is possible that both of these effects are positive, but the natural indirect effect is negative. For instance:

$$
\beta_ {1} = 1, \quad \theta_ {2} = 1, \quad \theta_ {3} = - 1. 5, \quad E (Z) = 0. 5.
$$

This is somewhat paradoxical and can be called the mediator paradox. Chen et al. (2007) reported a related surrogate endpoint paradox or intermediate variable paradox.

# 27.8 Mediation analysis with continuous mediator and binary outcome

Consider the following Normal linear model for the mediator and logistic model for the binary outcome:

$$
\left\{ \begin{array}{r c l} M \mid Z, X & \sim & \mathrm {N} (\beta_ {0} + \beta_ {1} Z + \beta_ {2} ^ {\mathsf {T}} X, \sigma_ {M} ^ {2}), \\ \operatorname {l o g i t} \{\operatorname * {p r} (Y = 1 \mid Z, M, X) \} & = & \theta_ {0} + \theta_ {1} Z + \theta_ {2} M + \theta_ {4} ^ {\mathsf {T}} X, \end{array} \right.
$$

where $\mathrm{logit}(w) = \log \left\{w / (1 - w)\right\}$ with inverse $\mathrm{expit}(w) = (1 + e^{-w})^{-1}$ . Express NDE and NIE in terms of the model parameters and the distribution of $X$ . How do we estimate NDE and NIE with IID data?

# 27.9 Mediation analysis with binary mediator and continuous outcome

Consider the following logistic model for the binary mediator and linear model for the outcome:

$$
\left\{ \begin{array}{r c l} \operatorname {l o g i t} \{\operatorname * {p r} (M = 1 \mid Z, X) \} & = & \beta_ {0} + \beta_ {1} Z + \beta_ {2} ^ {\mathsf {T}} X, \\ E (Y \mid Z, M, X) & = & \theta_ {0} + \theta_ {1} Z + \theta_ {2} M + \theta_ {4} ^ {\mathsf {T}} X. \end{array} \right.
$$

Under these models, show that

$$
\mathrm {N D E} = \theta_ {1}, \qquad \mathrm {N I E} = \theta_ {2} E \left\{\operatorname {e x p i t} \left(\beta_ {0} + \beta_ {1} + \beta_ {2} ^ {\mathsf {T}} X\right) - \operatorname {e x p i t} \left(\beta_ {0} + \beta_ {2} ^ {\mathsf {T}} X\right) \right\}.
$$

How do we estimate NDE and NIE with IID data?

# 27.10 Mediation analysis with binary mediator and outcome

Consider the following logistic models for the binary mediator and outcome:

$$
\left\{ \begin{array}{r c l} \operatorname {l o g i t} \{\operatorname * {p r} (M = 1 \mid Z, X) \} & = & \beta_ {0} + \beta_ {1} Z + \beta_ {2} ^ {\mathsf {T}} X, \\ \operatorname {l o g i t} \{\operatorname * {p r} (Y = 1 \mid Z, M, X) \} & = & \theta_ {0} + \theta_ {1} Z + \theta_ {2} M + \theta_ {4} ^ {\mathsf {T}} X. \end{array} \right.
$$

Express NDE and NIE in terms of the model parameters and the distribution of $X$ . How do we estimate NDE and NIE with IID data?

# 27.11 Modify the definitions to drop the cross-world independence

Define

$$
Y (z, F _ {M _ {z ^ {\prime}} \mid X}) = \int Y (z, m) f (M _ {z ^ {\prime}} = m \mid X) \mathrm {d} m
$$

as the potential outcome under treatment $z$ and a random draw from the distribution of $M_{z'} \mid X$ . With a discrete $M$ , the definition simplifies to

$$
Y (z, F _ {M _ {z ^ {\prime}} | X}) = \sum_ {m} Y (z, m) \operatorname * {p r} (M _ {z ^ {\prime}} = m \mid X).
$$

The key difference between $Y(z, M_{z'})$ and $Y(z, F_{M_{z'}|X})$ is that $M_{z'}$ is the potential mediator for the same unit whereas $F_{M_{z'}|X}$ is a random draw from the conditional distribution of the potential mediator in the whole population. Define the natural direct and indirect effects as

$$
\mathrm {N D E} = E \left\{Y \left(1, F _ {M _ {0} | X}\right) - Y \left(0, F _ {M _ {0} | X}\right) \right\}, \quad \mathrm {N I E} = E \left\{Y \left(1, F _ {M _ {1} | X}\right) - Y \left(1, F _ {M _ {0} | X}\right) \right\}.
$$

Show that under Assumptions 27.2-27.4, the identification formulas for NDE and NIE remain the same as in the main text.

Remark: Modifying the definitions of the nested potential outcomes allows us to relax the strong cross-world independence assumption but weakens the interpretation of the natural direct and indirect effects. See VanderWeele (2015) for more discussion and VanderWeele and Tchetgen Tchetgen (2017) for an application to a more complex setting with time-varying treatment and mediator.

# 27.12 Connections between principal stratification and mediation analysis

VanderWeele (2008) and Forastiere et al. (2018) reviewed and compared principal stratification and mediation analysis.

# Controlled Direct Effect

The formulation of mediation analysis in Chapter 27 relies on the nested potential outcomes, and fundamentally, some nested potential outcomes are not observable in any physical experiments. If we stick to the Popperian philosophy of science reviewed in Chapter 27.2.2, we should only define causal parameters in terms of quantities that are observable under some experiments. This chapter discusses an alternative view of causal inference with an intermediate variable. In this view, we only define the direct effect but can not define the indirect effect.

# 28.1 Definition of the controlled direct effect

We view $Z$ and $M$ as two treatment factors that can be manipulated, and define potential outcomes $Y(z,m)$ for $z = 0,1$ and $m \in \mathcal{M}$ . Based on these potential outcomes, we can define the controlled direct effect (CDE) below.

Definition 28.1 (CDE) Define

$$
\mathrm {C D E} (m) = E \{Y (1, m) - Y (0, m) \}.
$$

By definition, $\mathrm{CDE}(m)$ is the average causal effect of the treatment if the intermediate variable is fixed at $m$ . The parameter $\mathrm{CDE}(m)$ can capture the direct effect of the treatment holding the mediator at $m$ . However, this formulation cannot capture the indirect effect. In particular, the parameter $E\{Y(z,1) - Y(z,0)\}$ only measures the effect of the mediator on the outcome holding the treatment at $z$ . This is not a meaningful definition of the indirect effect.

# 28.2 Identification and estimation of the controlled direct effect

To identify $\mathrm{CDE}(m)$ , we need the following assumption, which requires that $Z$ and $M$ are jointly randomized given $X$ .

Assumption 28.1 Sequential ignorance requires

$$
Z \bot Y (z, m) \mid X, \quad M \bot Y (z, m) \mid (Z, X)
$$

or, equivalently (see Problem 27.2),

$$
(Z, M) \bot Y (z, m) \mid X.
$$

I will focus on the case with a binary $Z$ and $M$ . Mathematically, we can just view this problem as an observational study with four treatment levels

$$
(z, m) \in \{(0, 0), (0, 1), (1, 0), (1, 1) \}.
$$

The following theorem extends the results for observational studies with a binary treatment, identifying

$$
\mu_ {z m} = E \{Y (z, m) \}
$$

based on outcome regression, IPW, and doubly robust estimation.

Define

$$
\mu_ {z m} (x) = E (Y \mid Z = z, M = m, X = x)
$$

as the outcome mean conditional on the treatment, mediator, and covariates. Define

$$
\begin{array}{l} e _ {z m} (x) = \operatorname * {p r} (Z = z, M = m \mid X = x) \\ = \operatorname {p r} (Z = z \mid X = x) \operatorname {p r} (M = m \mid Z = z, X = x) \\ \end{array}
$$

as the probability of the joint value of $Z$ and $M$ conditional on the covariates.

Theorem 28.1 Under Assumption 28.1, we have

$$
\mu_ {z m} = E \{\mu_ {z m} (X) \} = E \left\{\frac {I (Z = z , M = m) Y}{e _ {z m} (X)} \right\}.
$$

Moreover, based on the working models $e_{zm}(X,\alpha)$ and $\mu_{zm}(X,\beta)$ for $e_{zm}(X)$ and $\mu_{zm}(X)$ , respectively, we have the doubly robust formula

$$
\mu_ {z m} ^ {\mathrm {d r}} = E \{\mu_ {z m} (X, \beta) \} + E \left[ \frac {I (Z = z , M = m) \{Y - \mu_ {z m} (X , \beta) \}}{e _ {z m} (X , \alpha)} \right],
$$

which equals $\mu_{zm}$ if either $e_{zm}(X,\alpha) = e_{zm}(X)$ or $\mu_{zm}(X,\beta) = \mu_{zm}(X)$ .

The proof of Theorem 28.1 is similar to those for the standard unconfounded observational studies. Problem 28.2 gives a general result. Based on the outcome mean model, we can obtain $\hat{\mu}_{zm}(x)$ for $\mu_{zm}(x)$ . Based on the treatment model, we can obtain $\hat{e}_z(x)$ for $\operatorname{pr}(Z = z \mid X = x)$ ; based on the

intermediate variable model, we can obtain $\hat{e}_m(z,x)$ for $\operatorname{pr}(M = m \mid Z = z, X = x)$ . We can then estimate $\mu_{zm}$ by outcome regression

$$
\hat {\mu} _ {z m} ^ {\mathrm {r e g}} = n ^ {- 1} \sum_ {i = 1} ^ {n} \hat {\mu} _ {z m} (X _ {i}),
$$

by IPW

$$
\hat {\mu} _ {z m} ^ {\mathrm {h t}} = n ^ {- 1} \sum_ {i = 1} ^ {n} \frac {I (Z _ {i} = z , M _ {i} = m) Y _ {i}}{\hat {e} _ {z} (X _ {i}) \hat {e} _ {m} (z , X _ {i})},
$$

$$
\hat {\mu} _ {z m} ^ {\mathrm {h a j}} = \sum_ {i = 1} ^ {n} \frac {I (Z _ {i} = z , M _ {i} = m) Y _ {i}}{\hat {e} _ {z} (X _ {i}) \hat {e} _ {m} (z , X _ {i})} / \sum_ {i = 1} ^ {n} \frac {I (Z _ {i} = z , M _ {i} = m)}{\hat {e} _ {z} (X _ {i}) \hat {e} _ {m} (z , X _ {i})},
$$

or by augmented IPW

$$
\hat {\mu} _ {z m} ^ {\mathrm {d r}} = \hat {\mu} _ {z m} ^ {\mathrm {r e g}} + n ^ {- 1} \sum_ {i = 1} ^ {n} \frac {I (Z _ {i} = z , M _ {i} = m) \{Y _ {i} - \hat {\mu} _ {z m} (X _ {i}) \}}{\hat {e} _ {z} (X _ {i}) \hat {e} _ {m} (z , X _ {i})}.
$$

We can then estimate $\mathrm{CDE}(m)$ by $\hat{\mu}_{1m}^{*} - \hat{\mu}_{0m}^{*}$ ( $* = \mathrm{reg, ht, haj, dr})$ and use the bootstrap to approximate the standard error.

If we are willing to assume a linear outcome model, the controlled direct effect simplifies to the coefficient of the treatment. Example 28.1 below gives the details.

Example 28.1 Under Assumption 28.1 and a linear outcome model,

$$
E (Y \mid Z, M, X) = \theta_ {0} + \theta_ {1} Z + \theta_ {2} M + \theta_ {4} ^ {\mathrm {T}} X,
$$

we can show that $\mathrm{CDE}(m)$ equals the coefficient $\theta_{1}$ , which coincides with the natural direct effect in the Baron-Kenny method. I relegate the proof to Problem 28.3.

# 28.3 Discussion

The formulation of the controlled direct effect does not involve nested or a priori counterfactual potential outcomes, and its identification does not require the cross-world counterfactual independence assumption. The parameter $\mathrm{CDE}(m)$ can capture the direct effect of the treatment holding the mediator at $m$ . However, this formulation cannot capture the indirect effect. I summarize the causal frameworks for intermediate variables in Table 28.1.

The mediation analysis framework can decompose the total effect into natural direct and indirect effects, but it requires nested potential outcomes

TABLE 28.1: Causal frameworks for intermediate variables   

<table><tr><td>chapter</td><td>framework</td><td>direct effect</td><td>indirect effect</td></tr><tr><td>26</td><td>principal stratification</td><td>τ(1,1), τ(0,0)</td><td>?</td></tr><tr><td>27</td><td>mediation analysis</td><td>NDE</td><td>NIE</td></tr><tr><td>28</td><td>controlled direct effect</td><td>CDE(m)</td><td>?</td></tr></table>

and cross-world independence. The principal stratification and controlled direct effect frameworks cannot define indirect effects but they do not involve nested potential outcomes and cross-world independence. Moreover, the principal stratification framework does not necessarily require that $M$ lies on the causal pathway from the treatment to the outcome. However, its identification and estimation involves disentangling mixture distributions, which is a nontrivial task in statistics.

# 28.4 Homework problems

# 28.1 CDE and NDE

Show that under cross-world independence $Y(z, m) \perp M(z') \mid X$ for all $z, z'$ and $m$ , the conditional controlled direct effect $\mathrm{CDE}(m \mid x) = E\{Y(1, m) - Y(0, m) \mid X = x\}$ and the conditional natural direct effect $\mathrm{NDE}(x) = E\{Y(1, M_0) - Y(0, M_0) \mid X = x\}$ have the following relationship:

$$
\mathrm {N D E} (x) = \sum_ {m} \mathrm {C D E} (m \mid x) \Pr \left(M _ {0} = m \mid X = x\right)
$$

for a discrete $M$ . Without the cross-world independence, does this relationship still hold in general?

# 28.2 Observational studies with a multi-valued treatment

Theorem 28.1 is a special case of the following theorem for unconfounded observational studies with multiple treatment levels (Imai and Van Dyk, 2004; Cattaneo, 2010). Below, I state the general problem and theorem.

Consider an observational study with a multi-valued treatment $Z \in \{1, \ldots, K\}$ , covariates $X$ , and outcome $Y$ . Unit $i$ has $K$ potential outcomes $Y_{i}(1), \ldots, Y_{i}(K)$ corresponding to the $K$ treatment levels. In general, we can define causal effect in terms of contrasts of the potential outcomes:

$$
\tau_ {C} = \sum_ {k = 1} ^ {K} C _ {k} E \{Y (k) \}
$$

where $\sum_{k=1}^{K} C_k = 0$ . The canonical choice of the pairwise comparison

$$
\tau_ {k, k ^ {\prime}} = E \left\{Y (k) - Y \left(k ^ {\prime}\right) \right\}.
$$

Therefore, the key is to identify and estimate the means of the potential outcomes $\mu_{k} = E\{Y(k)\}$ under the ignorability and overlap assumptions below based on IID data of $(Z_{i},X_{i},Y_{i})_{i = 1}^{n}$ .

Assumption 28.2 $Z \perp \{Y(1), \ldots, Y(K)\} \mid X$ and $\operatorname{pr}(Z = k \mid X) > 0$ for $k = 1, \ldots, K$ .

Define the generalized propensity score as

$$
e _ {k} (X) = \operatorname * {p r} (Z = k \mid X),
$$

and define the conditional outcome mean as

$$
\mu_ {k} (X) = E (Y \mid Z = k, X)
$$

for $k = 1,\ldots ,K$ . We have the following theorem.

Theorem 28.2 Under Assumption 28.2, we have

$$
\mu_ {k} = E \left\{\mu_ {k} (X) \right\} = E \left\{\frac {I (Z = k) Y}{e _ {k} (X)} \right\}.
$$

Moreover, based on the working models $e_k(X, \alpha)$ and $\mu_k(X, \beta)$ for $e_k(X)$ and $\mu_k(X)$ , respectively, we have the doubly robust formula

$$
\mu_ {k} ^ {\mathrm {d r}} = E \{\mu_ {k} (X, \beta) \} + E \left[ \frac {I (Z = k) \{Y - \mu_ {k} (X , \beta) \}}{e _ {k} (X , \alpha)} \right],
$$

which equals $\mu_{k}$ if either $e_k(X,\alpha) = e_k(X)$ or $\mu_{k}(X,\beta) = \mu_{k}(X)$ .

Prove Theorem 28.2.

Remark: Theorem 28.1 is a special case of Theorem 28.2 if we view the $(Z,M)$ in Theorem 28.1 as a treatment with four levels. The $\mathrm{CDE}(m)$ is a special case of $\tau_{C}$ .

# 28.3 CDE in the linear outcome model

Show that under Assumption 28.1, if $E(Y \mid Z, M, X) = \theta_0 + \theta_1 Z + \theta_2 M + \theta_4^{\mathrm{T}} X$ , then

$$
\mathrm {C D E} (m) = \theta_ {1}
$$

for all $m$ ; if $E(Y \mid Z, M, X) = \theta_0 + \theta_1Z + \theta_2M + \theta_3ZM + \theta_4^\top X$ , then

$$
\mathrm {C D E} (m) = \theta_ {1} + \theta_ {3} m.
$$

# 28.4 CDE in the logistic outcome model

Show that for a binary outcome, under Assumption 28.1, if

$$
\operatorname {l o g i t} \{\operatorname * {p r} (Y = 1 \mid Z, M, X) \} = \theta_ {0} + \theta_ {1} Z + \theta_ {2} M + \theta_ {4} ^ {\mathsf {T}} X,
$$

then

$$
\mathrm {C D E} (m) = E \{\exp \mathrm {i t} (\theta_ {0} + \theta_ {1} + \theta_ {2} m + \theta_ {4} ^ {\intercal} X) - \exp \mathrm {i t} (\theta_ {0} + \theta_ {2} m + \theta_ {4} ^ {\intercal} X) \};
$$

if

$$
\operatorname {l o g i t} \left\{\Pr (Y = 1 \mid Z, M, X) \right\} = \theta_ {0} + \theta_ {1} Z + \theta_ {2} M + \theta_ {3} Z M + \theta_ {4} ^ {\mathrm {T}} X,
$$

then

$$
\mathrm {C D E} (m) = E \left\{\operatorname {e x p i t} \left(\theta_ {0} + \theta_ {1} + \theta_ {2} m + \theta_ {3} m + \theta_ {4} ^ {\top} X\right) - \operatorname {e x p i t} \left(\theta_ {0} + \theta_ {2} m + \theta_ {4} ^ {\top} X\right) \right\}.
$$

# 28.5 Recommended reading

Nguyen et al. (2021) provided a friendly review of the topics in Chapters 27 and 28.

# Time-Varying Treatment and Confounding

Studies with time-varying treatments are common in biomedical and social sciences. James Robins championed the research in biostatistics. A classic example is that HIV patients may take azidothymidine, an antiretroviral medication, on and off over time (Robins et al., 2000; Hernán et al., 2000). Similar problems also exist in other fields. In education, a classic example is that students may receive different types of instructions over time (Hong and Raudenbush, 2008). In political science, a classic example is that candidates continuously recalibrate their campaign strategy based on time-varying polls and opponent actions (Blackwell, 2013).

Causal inference with time-varying treatments is not a simple extension of causal inference with a treatment at a single time point. The main challenge is time-varying confounding. Even if we assume all time-varying confounders are observed, we still face statistical challenges in adjusting for those confounders. On the one hand, we should stratify on these confounders to adjust for confounding; on the other hand, stratifying on post-treatment variables will cause bias. Due to these two conflicting goals, causal inference with time-varying treatments and confounding requires more sophisticated statistical methods. It is the main topic of this chapter.

To minimize the notational burden, I will use the setting with treatments at two time points to convey the most important ideas. Extensions to treatments at multiple time points can be conceptually straightforward although technical complexities will arise in finite samples. I will discuss the complexities and relegate general results to Problems 29.7-29.10.

# 29.1 Basic setup and sequential ignorability

Start with treatments at two time points. The temporal order (not the causal diagram) of the variables with two time points is below:

$$
X _ {0} \to Z _ {1} \to X _ {1} \to Z _ {2} \to Y
$$

where

- $X_0$ denotes the baseline pre-treatment covariates;

![](images/459dbc58690d9628af6d939aa356592d4e8b8cb35fc3ee47e5565a443dbc8cbb.jpg)

FIGURE 29.1: Assumption 29.1 holds without unmeasured confounding $U$ between $X_{1}$ and $Y$ . The causal diagram conditions on the pre-treatment covariates $X_{0}$ .

- $Z_{1}$ denotes the treatment at time point 1;   
- $X_{1}$ denotes the time-varying covariates between the treatments at time points 1 and 2;   
- $Z_{2}$ denotes the treatment at time point 2;   
- $Y$ denotes the outcome.

With binary treatments $(Z_{1},Z_{2})$ , each unit has four potential outcomes

$$
Y \left(z _ {1}, z _ {2}\right) \text {f o r} z _ {1}, z _ {2} = 0, 1.
$$

The observed outcome equals

$$
Y = Y (Z _ {1}, Z _ {2}) = \sum_ {z _ {1} = 0, 1} \sum_ {z _ {2} = 0, 1} 1 (Z _ {1} = z _ {1}) 1 (Z _ {2} = z _ {2}) Y (z _ {1}, z _ {2}).
$$

I will focus on the canonical setting with sequential ignorability, that is, the treatments are sequentially randomized given the observed history.

Assumption 29.1 (sequential ignorability) (1) $Z_{1}$ is randomized given $X_{0}$ :

$$
Z _ {1} \bot Y (z _ {1}, z _ {2}) \mid X _ {0} f o r z _ {1}, z _ {2} = 0, 1.
$$

(2) $Z_{2}$ is randomized given $(Z_{1},X_{1},X_{0})$

$$
Z _ {2} \text {山} Y (z _ {1}, z _ {2}) \mid (Z _ {1}, X _ {1}, X _ {0}) f o r z _ {1}, z _ {2} = 0, 1.
$$

Figure 29.1 is a simple causal diagram corresponding to Assumption 29.1, which does not contain any unmeasured confounding.

Figure 29.2 is a more complex causal diagram corresponding to Assumption 29.1. Sequential ignorance rules out only the confounding between the treatment $(Z_{1}, Z_{2})$ and the outcome $Y$ , but allows for unmeasured confounding between the time-varying covariate $X_{1}$ and the outcome $Y$ . The possible existence of $U$ causes many subtle issues even under sequential ignorance.

![](images/fc451469204f8bd2d7424c5f6866f5dbc15053027ff863c8de6b79850192c746.jpg)  
FIGURE 29.2: Assumption 29.1 holds with unmeasured confounding between $X_{1}$ and $Y$ . The causal diagram conditions on the pre-treatment covariates $X_{0}$ .

# 29.2 g-formula and outcome modeling

Recall the outcome-based identification formula with a treatment at a single time point:

$$
E \{Y (z) \} = E \{E (Y \mid Z = z, X) \}.
$$

With discrete $X$ , it reduces to

$$
E \{Y (z) \} = \sum_ {x} E (Y \mid Z = z, X = x) \mathrm {p r} (X = x);
$$

with continuous $X$ , it reduces to

$$
E \{Y (z) \} = \int E (Y \mid Z = z, X = x) f (x) \mathrm {d} x.
$$

The following result extends it to the setting with treatments at two time points.

Theorem 29.1 Under Assumption 29.1,

$$
E \left\{Y \left(z _ {1}, z _ {2}\right) \right\} = E \left[ E \left\{E \left(Y \mid z _ {2}, z _ {1}, X _ {1}, X _ {0}\right) \mid z _ {1}, X _ {0} \right\} \right]. \tag {29.1}
$$

In Theorem 29.1, I simplify the notation $Z_{2} = z_{2}$ to $z_{2}$ . To void complex formulas in this chapter, I will use the lowercase letter to represent the event that the random variable takes the corresponding value. With discrete $X_{0}$ and $X_{1}$ , the identification formula (29.1) reduces to

$$
E \left\{Y \left(z _ {1}, z _ {2}\right) \right\} = \sum_ {x _ {0}} \sum_ {x _ {1}} E \left(Y \mid z _ {2}, z _ {1}, x _ {1}, x _ {0}\right) \Pr \left(x _ {1} \mid z _ {1}, x _ {0}\right) \Pr \left(x _ {0}\right); \tag {29.2}
$$

with continuous $X_0$ and $X_{1}$ , the identification formula (29.1) reduces to

$$
E \left\{Y \left(z _ {1}, z _ {2}\right) \right\} = \iint E \left(Y \mid z _ {2}, z _ {1}, x _ {1}, x _ {0}\right) f \left(x _ {1} \mid z _ {1}, x _ {0}\right) f \left(x _ {0}\right) \mathrm {d} x _ {1} \mathrm {d} x _ {0}. \tag {29.3}
$$

Compare (29.2) with the formula based on the law of total probability to gain more insights:

$$
\begin{array}{l} E (Y) = \sum_ {x _ {0}} \sum_ {z _ {1}} \sum_ {x _ {1}} \sum_ {z _ {2}} E (Y \mid z _ {2}, z _ {1}, x _ {1}, x _ {0}) \\ \Pr \left(z _ {2} \mid z _ {1}, x _ {1}, x _ {0}\right) \Pr \left(x _ {1} \mid z _ {1}, x _ {0}\right) \Pr \left(z _ {1} \mid x _ {0}\right) \Pr \left(x _ {0}\right). \tag {29.4} \\ \end{array}
$$

Erasing the probabilities of $Z_{2}$ and $Z_{1}$ in (29.4), we can obtain the formula (29.3). This is intuitive because the potential outcome $Y(z_{1},z_{2})$ has the meaning of fixing $Z_{1}$ and $Z_{2}$ at $z_{1}$ and $z_{2}$ , respectively.

Robins called (29.2) and (29.3) the g-formulas. Now I will prove Theorem 29.1.

Proof of Theorem 29.1: By the tower property,

$$
E \{Y (z _ {1}, z _ {2}) \} = E \left[ E \{Y (z _ {1}, z _ {2}) \mid X _ {0} \} \right],
$$

so I will focus on $E\{Y(z_1,z_2)\mid X_0\}$ . By Assumption 29.1(1) and the tower property,

$$
\begin{array}{l} E \left\{Y \left(z _ {1}, z _ {2}\right) \mid X _ {0} \right\} = E \left\{Y \left(z _ {1}, z _ {2}\right) \mid z _ {1}, X _ {0} \right\} \\ { = } { E \Big [ E \{ Y ( z _ { 1 } , z _ { 2 } ) \mid z _ { 1 } , X _ { 1 } , X _ { 0 } \} \mid z _ { 1 } , X _ { 0 } \Big ] . } \\ \end{array}
$$

By Assumption 29.1(2),

$$
\begin{array}{l} E \{Y (z _ {1}, z _ {2}) \mid X _ {0} \} = E \left[ E \{Y (z _ {1}, z _ {2}) \mid z _ {2}, z _ {1}, X _ {1}, X _ {0} \} \mid z _ {1}, X _ {0} \right] \\ { = } { E \Big [ E \{ Y \mid z _ { 2 } , z _ { 1 } , X _ { 1 } , X _ { 0 } \} \mid z _ { 1 } , X _ { 0 } \Big ] . } \\ \end{array}
$$

The formula (29.1) follows.

![](images/d80fda25855185c6036de61bb059563d2e4466de4918531367cb95158cb93ffb.jpg)

# 29.2.1 Plug-in estimation based on outcome modeling

The g-formulas (29.2) and (29.3) suggest that to estimate the means of the potential outcomes, we need to model $E(Y \mid z_2, z_1, x_1, x_0)$ , $\operatorname{pr}(x_1 \mid z_1, x_0)$ and $\operatorname{pr}(x_0)$ . With these fitted models, we can plug them into the g-formulas.

With some special functional forms, this task can be simplified. Example 29.1 below gives the results under a linear model for the outcome.

Example 29.1 Assume a linear outcome model

$$
E \left(Y \mid z _ {2}, z _ {1}, x _ {1}, x _ {0}\right) = \beta_ {0} + \beta_ {1} z _ {2} + \beta_ {2} z _ {1} + \beta_ {3} x _ {1} + \beta_ {4} x _ {0}.
$$

We can verify that

$$
\begin{array}{l} E \{Y (z _ {1}, z _ {2}) \} = \sum_ {x _ {0}} \sum_ {x _ {1}} (\beta_ {0} + \beta_ {1} z _ {2} + \beta_ {2} z _ {1} + \beta_ {3} x _ {1} + \beta_ {4} x _ {0}) \Pr (x _ {1} \mid z _ {1}, x _ {0}) \Pr (x _ {0}) \\ = \beta_ {0} + \beta_ {1} z _ {2} + \beta_ {2} z _ {1} + \beta_ {3} \sum_ {x _ {0}} E (X _ {1} \mid z _ {1}, x _ {0}) \Pr (x _ {0}) + \beta_ {4} E (X _ {0}). \\ \end{array}
$$

Define

$$
E \left\{X _ {1} \left(z _ {1}\right) \right\} = \sum_ {x _ {0}} E \left(X _ {1} \mid z _ {1}, x _ {0}\right) \Pr \left(x _ {0}\right) \tag {29.5}
$$

to simplify the formula as

$$
E \left\{Y \left(z _ {1}, z _ {2}\right) \right\} = \beta_ {0} + \beta_ {1} z _ {2} + \beta_ {2} z _ {1} + \beta_ {3} E \left\{X _ {1} \left(z _ {1}\right) \right\} + \beta_ {4} E \left(X _ {0}\right).
$$

In (29.5), I introduce the potential outcome of $X_{1}$ under the treatment $Z_{1} = z_{1}$ at time point 1. It is reasonable because the right-hand side of (29.5) is the identification formula of $E\{X_{1}(z_{1})\}$ under ignorance $X_{1}(z_{1}) \bot Z_{1} \mid X_{0}$ for $z_{1} = 0,1$ . We do not really need the potential outcome $X_{1}(z_{1})$ and the ignorance, but it is a convenient notation and matches our previous discussion.

Define $\tau_{Z_1\to X_1} = E\{X_1(1) - X_1(0)\}$ . We can verify that

$$
E \left\{Y (1, 0) - Y (0, 0) \right\} = \beta_ {2} + \beta_ {3} \tau_ {Z _ {1} \rightarrow X _ {1}},
$$

$$
E \left\{Y (0, 1) - Y (0, 0) \right\} = \beta_ {1},
$$

$$
E \left\{Y (1, 1) - Y (0, 0) \right\} = \beta_ {1} + \beta_ {2} + \beta_ {3} \tau_ {Z _ {1} \rightarrow X _ {1}}.
$$

Therefore, we can estimate the effect of $(Z_{1}, Z_{2})$ on $Y$ based on the above formulas by first estimating the regression coefficients $\beta s$ and the average causal effect of $Z_{1}$ on $X_{1}$ using standard methods.

If we further assume a linear model for $X_{1}$

$$
E \left(X _ {1} \mid Z _ {1}, X _ {0}\right) = \gamma_ {0} + \gamma_ {1} z _ {1} + \gamma_ {2} x _ {0},
$$

then $\tau_{Z_1\to X_1} = \gamma_1$ and

$$
E \left\{Y (1, 0) - Y (0, 0) \right\} = \beta_ {2} + \beta_ {3} \gamma_ {1}, \tag {29.6}
$$

$$
E \left\{Y (0, 1) - Y (0, 0) \right\} = \beta_ {1}, \tag {29.7}
$$

$$
E \{Y (1, 1) - Y (0, 0) \} = \beta_ {1} + \beta_ {2} + \beta_ {3} \gamma_ {1}. \tag {29.8}
$$

The formulas in (29.6)-(29.8) are intuitive based on Figure 29.3 with regression coefficients on the arrows. In (29.6), the effect of $Z_{1}$ equals the sum of the coefficients on the paths $Z_{1} \to Y$ and $Z_{1} \to X_{1} \to Y$ ; in (29.7), the effect of $Z_{2}$ equals the coefficient on the path $Z_{2} \to Y$ ; in (29.8), the total effect of $(Z_{1}, Z_{2})$ equals the sum of the coefficients on the paths $Z_{1} \to Y$ , $Z_{1} \to X_{1} \to Y$ and $Z_{2} \to Y$ .

However, Robins and Wasserman (1997) pointed out a surprising drawback of the plug-in estimation based on outcome modeling. They showed that with model misspecification in this strategy, data analyzers may falsely reject the null hypothesis of zero causal effect of $(Z_{1}, Z_{2})$ on $Y$ even when the true effect is zero in the data-generating process. They called it the $g$ -null paradox. Perhaps surprisingly, they show that the $g$ -null paradox may even arise in the simple linear outcome model in Example 29.1. McGrath et al. (2021) revisited this paradox. See Problem 29.1 for more details.

![](images/713d1ba2f50c0527a6a7759f58f6e5942115a4ac9b2746ad7874cc5347518c86.jpg)  
FIGURE 29.3: A linear causal diagram with coefficients on the arrows, conditional on the pre-treatment covariates $X_0$ .

# 29.2.2 Recursive estimation based on outcome modeling

The plug-in estimation in Section 29.2.1 involves modeling the time-varying confounder $X_{1}$ and causes the unpleasant g-null paradox. It is not a desirable method.

Recall the outcome regression estimator with a treatment at a single time based on $E\{Y(z)\} = E\{E(Y \mid Z = z, X)\}$ . We first fit a model of $Y$ on $X$ using the subset of the data with $Z = z$ , and obtain the fitted values $\hat{Y}_i(z)$ for all units. We then obtain the estimator

$$
\hat {E} \{Y (z) \} = n ^ {- 1} \sum_ {i = 1} ^ {n} \hat {Y} _ {i} (z).
$$

Similarly, the recursive expectation formula in (29.1) motivates a simpler method for estimation. Start from the inner conditional expectation, denoted by

$$
\tilde {Y} _ {2} \left(z _ {1}, z _ {2}\right) = E \left(Y \mid Z _ {2} = z _ {2}, Z _ {1} = z _ {1}, X _ {1}, X _ {0}\right).
$$

We can fit a model of $Y$ on $(X_{1}, X_{0})$ using the subset of the data with $(Z_{2} = z_{2}, Z_{1} = z_{1})$ , and obtain the fitted values $\dot{Y}_{2i}(z_{1}, z_{2})$ for all units. Move on to outer conditional expectation, denoted by

$$
\tilde {Y} _ {1} \left(z _ {1}, z _ {2}\right) = E \left\{\tilde {Y} _ {2} \left(z _ {1}, z _ {2}\right) \mid Z _ {1} = z _ {1}, X _ {0} \right\}.
$$

We can fit a model of $\hat{Y}_2(z_1,z_2)$ on $X_0$ using the subset of data with $Z_{1} = z_{1}$ , and obtain the fitted values $\hat{Y}_{1i}(z_1,z_2)$ for all units. The final estimator for $E\{Y(z_1,z_2)\}$ is then

$$
\hat {E} \{Y (z _ {1}, z _ {2}) \} = n ^ {- 1} \sum_ {i = 1} ^ {n} \hat {Y} _ {1 i} (z _ {1}, z _ {2}).
$$

The above recursive estimation does not involve fitting a model for $X_{1}$ and avoids the g-null paradox. See Problem 29.2 for a special case. However, the estimator based on recursive regression is not easy to implement because it involves modeling variables that do not correspond to the natural structure of the causal diagram, e.g., $\tilde{Y}_{2}(z_{1},z_{2})$ .

# 29.3 Inverse propensity score weighting

Recall the IPW identification formula with a treatment at a single time point:

$$
E \{Y (z) \} = E \left\{\frac {1 (Z = z) Y}{\operatorname* {p r} (Z = z \mid X)} \right\}.
$$

The following result extends it to the setting with a treatment at two time points. Define

$$
e \left(z _ {1}, X _ {0}\right) = \operatorname {p r} \left(Z _ {1} = z _ {1} \mid X _ {0}\right)
$$

and

$$
e \left(z _ {2}, Z _ {1}, X _ {1}, X _ {0}\right) = \Pr \left(Z _ {2} = z _ {2} \mid Z _ {1}, X _ {1}, X _ {0}\right)
$$

as the propensity scores at time points 1 and 2, respectively.

Theorem 29.2 Under Assumption 29.1,

$$
E \left\{Y \left(z _ {1}, z _ {2}\right) \right\} = E \left\{\frac {1 \left(Z _ {1} = z _ {1}\right) 1 \left(Z _ {2} = z _ {2}\right) Y}{e \left(z _ {1} , X _ {0}\right) e \left(z _ {2} , Z _ {1} , X _ {1} , X _ {0}\right)} \right\}. \tag {29.9}
$$

Theorem 29.2 reveals the omitted overlap assumption:

$$
0 <   e \left(z _ {1}, X _ {0}\right) <   1, \quad 0 <   e \left(z _ {2}, Z _ {1}, X _ {1}, X _ {0}\right) <   1
$$

for all $z_{1}$ and $z_{2}$ . If some propensity scores are 0 or 1, then the identification formula (29.9) blows up to infinity.

Proof of Theorem 29.2: Conditioning on $(Z_{1},X_{1},X_{0})$ and using Assumption 29.1(2), we can simplify the right-hand side of (29.9) as

$$
\begin{array}{l} E \left\{\frac {1 \left(Z _ {1} = z _ {1}\right) 1 \left(Z _ {2} = z _ {2}\right) Y \left(z _ {1} , z _ {2}\right)}{\operatorname* {p r} \left(Z _ {1} = z _ {1} \mid X _ {0}\right) \operatorname* {p r} \left(Z _ {2} = z _ {2} \mid Z _ {1} , X _ {1} , X _ {0}\right)} \right\} \\ = E \left\{\frac {1 \left(Z _ {1} = z _ {1}\right) \operatorname {p r} \left(Z _ {2} = z _ {2} \mid Z _ {1} , X _ {1} , X _ {0}\right) E \left(Y \left(z _ {1} , z _ {2}\right) \mid Z _ {1} , X _ {1} , X _ {0}\right)}{\operatorname {p r} \left(Z _ {1} = z _ {1} \mid X _ {0}\right) \operatorname {p r} \left(Z _ {2} = z _ {2} \mid Z _ {1} , X _ {1} , X _ {0}\right)} \right\} \\ = E \left\{\frac {1 \left(Z _ {1} = z _ {1}\right)}{\operatorname* {p r} \left(Z _ {1} = z _ {1} \mid X _ {0}\right)} E \left(Y \left(z _ {1}, z _ {2}\right) \mid Z _ {1}, X _ {1}, X _ {0}\right) \right\} \\ = E \left\{\frac {1 \left(Z _ {1} = z _ {1}\right)}{\operatorname* {p r} \left(Z _ {1} = z _ {1} \mid X _ {0}\right)} Y \left(z _ {1}, z _ {2}\right) \right\}, \tag {29.10} \\ \end{array}
$$

where (29.10) follows from the tower property.

Conditioning on $X_0$ and using Assumption 29.1(1), we can simplify the right-hand side of (29.10) as

$$
\begin{array}{l} E \left\{\frac {\operatorname* {p r} (Z _ {1} = z _ {1} \mid X _ {0})}{\operatorname* {p r} (Z _ {1} = z _ {1} \mid X _ {0})} E (Y (z _ {1}, z _ {2}) \mid X _ {0}) \right\} \\ = E \left\{E \left(Y \left(z _ {1}, z _ {2}\right) \mid X _ {0}\right) \right\} \\ = E \left\{Y \left(z _ {1}, z _ {2}\right) \right\}, \\ \end{array}
$$

where, again, the last line follows from the tower property.

The estimator based on IPW is much simpler which only involves modeling two binary treatment indicators. First, we can fit a model of $Z_{1}$ on $X_{0}$ to obtain the fitted values $\hat{e}_1(z_1,X_{0i})$ and fit a model of $Z_{2}$ on $(Z_{1},X_{1},X_{0})$ to obtain the fitted values $\hat{e}_2(z_2,Z_{1i},X_{1i},X_{0i})$ for all units. Then, we obtain the following IPW estimator:

$$
\hat {E} ^ {\mathrm {h t}} \{Y (z _ {1}, z _ {2}) \} = n ^ {- 1} \sum_ {i = 1} ^ {n} \frac {1 (Z _ {1 i} = z _ {1}) 1 (Z _ {2 i} = z _ {2}) Y _ {i}}{\hat {e} _ {1} (z _ {1} , X _ {0 i}) \hat {e} _ {2} (z _ {2} , Z _ {1 i} , X _ {1 i} , X _ {0 i})}.
$$

Similar to the discussion in Chapter 11, the HT estimator is not invariant to the location shift of the outcome and suffers from instability in finite samples. A modified Hajek-type estimator is $\hat{E}^{\mathrm{haj}}\{Y(z_1,z_2)\} = \hat{E}^{\mathrm{ht}}\{Y(z_1,z_2)\} /\hat{1}^{\mathrm{ht}}(z_1,z_2)$ , where

$$
\hat {1} ^ {\mathrm {h t}} (z _ {1}, z _ {2}) = n ^ {- 1} \sum_ {i = 1} ^ {n} \frac {1 (Z _ {1 i} = z _ {1}) 1 (Z _ {2 i} = z _ {2})}{\hat {e} _ {1} (z _ {1} , X _ {0 i}) \hat {e} _ {2} (z _ {2} , Z _ {1 i} , X _ {1 i} , X _ {0 i})}.
$$

# 29.4 Multiple time points

Extending the estimation strategies in Sections 29.2 and 29.3 is not immediate with multiple time points. Even with a binary treatment and $K$ time points, the number of treatment combinations grows exponentially with $K$ (for example, $2^{5} = 32$ and $2^{10} = 1024$ ). Consequently, the outcome regression and IPW estimators in Sections 29.2 and 29.3 are not feasible in finite samples because they require enough data for every combination of the treatment levels.

# 29.4.1 Marginal structural model

A powerful approach is based on the marginal structural model (MSM) (Robins et al., 2000; Hernán et al., 2000). For simplicity of notation, I will only present the MSM with $K = 2$ although its main use is in the general case.

Definition 29.1 (MSM) The marginal mean of $Y(z_{1},z_{2})$ equals

$$
E \{Y (z _ {1}, z _ {2}) \} = f (z _ {1}, z _ {2}; \beta).
$$

A leading example of Definition 29.1 is $E\{Y(z_1, z_2)\} = \beta_0 + \beta_1 z_1 + \beta_2 z_2$ . It is also straightforward to include the baseline covariates in the model. Definition 29.2 below extends Definition 29.1.

Definition 29.2 (MSM with baseline covariates) The mean of $Y(z_{1},z_{2})$ conditional on $X_0$ equals

$$
E \left\{Y \left(z _ {1}, z _ {2}\right) \mid X _ {0} \right\} = f \left(z _ {1}, z _ {2}, X _ {0}; \beta\right).
$$

A leading example of Definition 29.2 is

$$
E \left\{Y \left(z _ {1}, z _ {2}\right) \mid X _ {0} \right\} = \beta_ {0} + \beta_ {1} z _ {1} + \beta_ {2} z _ {2} + \beta_ {3} ^ {\mathrm {T}} X _ {0}. \tag {29.11}
$$

If we observe all the potential outcomes, we can solve $\beta$ from the following minimization problem:

$$
\beta = \arg \min  _ {b} \sum_ {z _ {2}} \sum_ {z _ {1}} E \left\{Y \left(z _ {1}, z _ {2}\right) - f \left(z _ {1}, z _ {2}, X _ {0}; b\right) \right\} ^ {2}. \tag {29.12}
$$

For simplicity, I focus on the least squares formulation. We can also extend the discussion to general models; see Problem 29.4 for an example of the logistic model.

Under sequential ignorance, we can solve $\beta$ from the following minimization problem that only involves observables.

Theorem 29.3 (IPW under MSM) Under Assumption 29.1 and Definition 29.2, the $\beta$ in (29.12) equals

$$
\beta = \arg \min _ {b} \sum_ {z _ {2}} \sum_ {z _ {1}} E \left[ \frac {1 (Z _ {1} = z _ {1}) 1 (Z _ {2} = z _ {2})}{e (z _ {1} , X _ {0}) e (z _ {2} , Z _ {1} , X _ {1} , X _ {0})} \{Y - f (z _ {1}, z _ {2}, X _ {0}; b) \} ^ {2} \right].
$$

The proof of Theorem 29.3 is similar to that of Theorem 29.2. I relegate it to Problem 29.3.

Theorem 29.3 implies a simple estimation strategy based on weighted regressions. For instance, under (29.11), we can fit WLS of $Y_{i}$ on $(1,Z_{1i},Z_{2i},X_{0i})$ with weights $\hat{e}_1^{-1}(Z_{1i},X_{0i})\hat{e}_{2i}^{-1}(Z_{2i},Z_{i1},X_{1i},X_{0i})$ .

# 29.4.2 Structural nested model

A key problem of IPW is that it is not applicable if the overlap assumption is violated. To address this challenge, Robins proposed the structural nested model. Again, to simplify the presentation, I only review the version with two time points.

Definition 29.3 (structural nested model) The conditional effect at time point 1 is

$$
E \left\{Y \left(z _ {1}, 0\right) - Y (0, 0) \mid Z _ {1} = z _ {1}, X _ {0} \right\} = g _ {1} \left(z _ {1}, X _ {0}; \beta\right)
$$

for all $z_{1}$ , and the conditional effect at time point 2 is

$$
E \left\{Y \left(z _ {1}, z _ {2}\right) - Y \left(z _ {1}, 0\right) \mid Z _ {2} = z _ {2}, Z _ {2} = z _ {1}, X _ {1}, X _ {0} \right\} = g _ {2} \left(z _ {2}, z _ {1}, X _ {1}, X _ {0}; \beta\right)
$$

for all $z_{1},z_{2}$

In Definition 29.3, two logical restrictions are

$$
g _ {1} (0, X _ {0}; \beta) = 0
$$

and

$$
g _ {2} \left(0, z _ {1}, X _ {1}, X _ {0}; \beta\right) = 0 \text {f o r a l l} z _ {1}.
$$

Two leading choices of Definition 29.3 are below.

Example 29.2 Assume

$$
\left\{ \begin{array}{l} g _ {1} (z _ {1}, X _ {0}; \beta) = \beta_ {1} z _ {1}, \\ g _ {2} (z _ {2}, z _ {1}, X _ {1}, X _ {0}; \beta) = (\beta_ {2} + \beta_ {3} z _ {1}) z _ {2}. \end{array} \right.
$$

Example 29.3 Assume

$$
\left\{ \begin{array}{l} g _ {1} (z _ {1}, X _ {0}; \beta) = (\beta_ {1} + \beta_ {2} ^ {\mathsf {T}} X _ {0}) z _ {1}, \\ g _ {2} (z _ {2}, z _ {1}, X _ {1}, X _ {0}; \beta) = (\beta_ {3} + \beta_ {4} z _ {1} + \beta_ {5} ^ {\mathsf {T}} X _ {1}) z _ {2}. \end{array} \right.
$$

Compare Definitions 29.2 and 29.3. The structural nested model allows for adjusting for the baseline covariates as well as the time-varying covariates whereas the marginal structural model only allows for adjusting for the baseline covariates. The estimation under Definition 29.3 is more involved. A strategy is to estimate the parameter based on estimating equations.

I first introduce two important building blocks for discussing the estimation. Define

$$
U _ {2} (\beta) = Y - g _ {2} \left(Z _ {2}, Z _ {1}, X _ {1}, X _ {0}; \beta\right)
$$

and

$$
U _ {1} (\beta) = Y - g _ {2} \left(Z _ {2}, Z _ {1}, X _ {1}, X _ {0}; \beta\right) - g _ {1} \left(Z _ {1}, X _ {0}; \beta\right).
$$

They are not directly computable from the data because they depend on the true value of the parameter $\beta$ . At the true value, they have the following properties.

Lemma 29.1 Under Assumption 29.1 and Definition 29.3, we have

$$
\begin{array}{l} E \left\{U _ {2} (\beta) \mid Z _ {2}, Z _ {1}, X _ {1}, X _ {0} \right\} = E \left\{U _ {2} (\beta) \mid Z _ {1}, X _ {1}, X _ {0} \right\} \\ = E \left\{Y \left(Z _ {1}, 0\right) \mid Z _ {1}, X _ {1}, X _ {0} \right\} \\ \end{array}
$$

and

$$
\begin{array}{l} E \left\{U _ {1} (\beta) \mid Z _ {1}, X _ {0} \right\} = E \left\{U _ {1} (\beta) \mid X _ {0} \right\} \\ = E \{Y (0, 0) \mid X _ {0} \}. \\ \end{array}
$$

Lemma 29.1 involves a subtle notation $Y(Z_{1},0)$ because $Z_{1}$ is random. It should be read as $Y(Z_{1},0) = Z_{1}Y(1,0) + (1 - Z_{1})Y(0,0)$ . Based on the definitions and Lemma 29.1, $U_{1}(\beta)$ acts as the control potential outcome before

receiving any treatment and $U_{2}(\beta)$ acts as the control potential outcome after receiving the treatment at time point 1.

Proof of Lemma 29.1: Part 1. We have

$$
\begin{array}{l} E \left\{U _ {2} (\beta) \mid Z _ {2} = 1, Z _ {1}, X _ {1}, X _ {0} \right\} \\ = E \left\{Y \left(Z _ {1}, 1\right) - g _ {2} \left(1, Z _ {1}, X _ {1}, X _ {0}; \beta\right) \mid Z _ {2} = 1, Z _ {1}, X _ {1}, X _ {0} \right\} \\ = E \left\{Y \left(Z _ {1}, 0\right) \mid Z _ {2} = 1, Z _ {1}, X _ {1}, X _ {0} \right\} \\ \end{array}
$$

and

$$
\begin{array}{l} E \left\{U _ {2} (\beta) \mid Z _ {2} = 0, Z _ {1}, X _ {1}, X _ {0} \right\} \\ = E \left\{Y \left(Z _ {1}, 0\right) - g _ {2} \left(0, Z _ {1}, X _ {1}, X _ {0}; \beta\right) \mid Z _ {2} = 0, Z _ {1}, X _ {1}, X _ {0} \right\} \\ = E \left\{Y \left(Z _ {1}, 0\right) \mid Z _ {2} = 0, Z _ {1}, X _ {1}, X _ {0} \right\} \\ \end{array}
$$

so

$$
\begin{array}{l} E \left\{U _ {2} (\beta) \mid Z _ {2}, Z _ {1}, X _ {1}, X _ {0} \right\} = E \left\{Y \left(Z _ {1}, 0\right) \mid Z _ {2}, Z _ {1}, X _ {1}, X _ {0} \right\} \\ = E \left\{Y \left(Z _ {1}, 0\right) \mid Z _ {1}, X _ {1}, X _ {0} \right\} \\ \end{array}
$$

where the last identity follows from sequential ignorability. Since the last term does not depend on $Z_{2}$ , we also have

$$
E \left\{U _ {2} (\beta) \mid Z _ {2}, Z _ {1}, X _ {1}, X _ {0} \right\} = E \left\{U _ {2} (\beta) \mid Z _ {1}, X _ {1}, X _ {0} \right\}.
$$

Part 2. Using the above results, we have

$$
\begin{array}{l} E \left\{U _ {1} (\beta) \mid Z _ {1}, X _ {0} \right\} \\ = E \left\{U _ {2} (\beta) - g _ {1} \left(Z _ {1}, X _ {0}; \beta\right) \mid Z _ {1}, X _ {0} \right\} \quad \text {(D e f i n i t i o n 2 9 . 3)} \\ = E \left[ E \left\{U _ {2} (\beta) - g _ {1} \left(Z _ {1}, X _ {0}; \beta\right) \mid X _ {1}, Z _ {1}, X _ {0} \right\} \mid Z _ {1}, X _ {0} \right] \quad \text {(t o w e r p r o p e r t y)} \\ = E \left[ E \left\{Y \left(Z _ {1}, 0\right) - g _ {1} \left(Z _ {1}, X _ {0}; \beta\right) \mid X _ {1}, Z _ {1}, X _ {0} \right\} \mid Z _ {1}, X _ {0} \right] \quad \text {(p a r t 1)} \\ = E \left\{Y \left(Z _ {1}, 0\right) - g _ {1} \left(Z _ {1}, X _ {0}; \beta\right) \mid Z _ {1}, X _ {0} \right\} \quad \text {(t o w e r p r o p e r t y)} \\ = E \left\{Y (0, 0) \mid Z _ {1}, X _ {0} \right\} \quad (\text {D e f i n i t i o n} 2 9. 3) \\ = E \left\{Y (0, 0) \mid X _ {0} \right\} \quad (\text {s e q u e n t i a l i g n o r a b i l i t y}). \\ \end{array}
$$

Since the last term does not depend on $Z_{1}$ , we also have

$$
E \left\{U _ {1} (\beta) \mid Z _ {1}, X _ {0} \right\} = E \left\{U _ {1} (\beta) \mid X _ {0} \right\}.
$$

With Lemma 29.1, we can prove Theorem 29.4 below.

Theorem 29.4 Under Assumption 29.1 and Definition 29.3,

$$
E \left[ h _ {2} \left(Z _ {1}, X _ {1}, X _ {0}\right) \left\{Z _ {2} - e \left(1, Z _ {1}, X _ {1}, X _ {0}\right) \right\} U _ {2} (\beta) \right] = 0
$$

and

$$
E \left[ h _ {1} \left(X _ {0}\right) \left\{Z _ {1} - e \left(1, X _ {0}\right) \right\} U _ {1} (\beta) \right] = 0.
$$

for any functions $h_1$ and $h_2$ , provided that the moments exist.

Proof of Theorem 29.2: Use the tower property by conditioning on $(Z_{2}, Z_{1}, X_{1}, X_{0})$ and Lemma 29.1 to obtain

$$
\begin{array}{l} E \left[ h _ {2} \left(Z _ {1}, X _ {1}, X _ {0}\right) \left\{Z _ {2} - e \left(1, Z _ {1}, X _ {1}, X _ {0}\right) \right\} E \left\{U _ {2} (\beta) \mid Z _ {2}, Z _ {1}, X _ {1}, X _ {0} \right\} \right] \\ = E \left[ h _ {2} \left(Z _ {1}, X _ {1}, X _ {0}\right) \left\{Z _ {2} - e \left(1, Z _ {1}, X _ {1}, X _ {0}\right) \right\} E \left\{U _ {2} (\beta) \mid Z _ {1}, X _ {1}, X _ {0} \right\} \right]. \\ \end{array}
$$

Use the tower property by conditioning on $(Z_{1},X_{1},X_{0})$ to show that the last identity equals 0 because $E\{Z_2 - e(1,Z_1,X_1,X_0)\mid Z_1,X_1,X_0\} = 0$

Similarly, use the tower property by conditioning on $(Z_{1},X_{0})$ and Lemma 29.1 to obtain

$$
\begin{array}{l} E \left[ h _ {1} \left(X _ {0}\right) \left\{Z _ {1} - e (1, X _ {0}) \right\} E \left\{U _ {1} (\beta) \mid Z _ {1}, X _ {0} \right\} \right] \\ = E \left[ h _ {1} \left(X _ {0}\right) \left\{Z _ {1} - e \left(1, X _ {0}\right) \right\} E \left\{U _ {1} (\beta) \mid X _ {0} \right\} \right]. \\ \end{array}
$$

Use the tower property by conditioning on $X_0$ to show that the last identity equals 0 because $E\{Z_1 - e(1, X_0) \mid X_0\} = 0$ .

To use Theorem 29.4, we must specify $h_1$ and $h_2$ to ensure that there are enough equations for solving $\beta$ . Example 29.4 below revisits Example 29.2.

Example 29.4 Under Example 29.2, we can choose $h_1 = 1$ and $h_2 = (1, Z_1)$ to obtain

$$
\begin{array}{l} E \left[ \left\{Z _ {2} - e \left(1, Z _ {1}, X _ {1}, X _ {0}\right) \right\} \left\{Y - \left(\beta_ {2} + \beta_ {3} Z _ {1}\right) Z _ {2} \right\} \right] = 0, \\ E \left[ Z _ {1} \left\{Z _ {2} - e \left(1, Z _ {1}, X _ {1}, X _ {0}\right) \right\} \left\{Y - \left(\beta_ {2} + \beta_ {3} Z _ {1}\right) Z _ {2} \right\} \right] = 0, \\ E \left[ \left\{Z _ {1} - e (1, X _ {0}) \right\} \left\{Y - \left(\beta_ {2} + \beta_ {3} Z _ {1}\right) Z _ {2} - \beta_ {1} Z _ {1} \right\} \right] = 0. \\ \end{array}
$$

We can then solve for the $\beta$ 's from the above linear equations; see Problem 29.6. A natural question is whether alternative choices of $(h_1, h_2)$ can lead to more efficient estimators. The answer is yes. For example, we can choose many $(h_1, h_2)$ and use the generalized method of moment (Hansen, 1982). The technical details are beyond this book.

Naimi et al. (2017) and Vansteelandt and Joffe (2014) provided tutorials on the structural nested models.

# 29.5 Homework problems

# 29.1 $g$ -null paradox

Consider the simple causal diagram in Figure 29.4 without pre-treatment covariates $X_0$ and without the arrows from $(Z_1, Z_2)$ to $Y$ . So the effect of $(Z_1, Z_2)$ on $Y$ is zero.

Revisit Example 29.1. Show that the expectation $E\{Y(z_1, z_2)\}$ does not depend on $(z_1, z_2)$ if

$$
\beta_ {1} = \beta_ {2} = 0 \text {a n d} \beta_ {3} = 0
$$

![](images/b149b6e2ac51afbe5ee4b01f662a91b8cf0b841a3ba6daa1a1c7bfbf5d63baa4.jpg)  
FIGURE 29.4: With unmeasured confounding between $X_{1}$ and $Y$ . The causal diagram ignores the pre-treatment covariates $X_{0}$ .

or

$$
\beta_ {1} = \beta_ {2} = 0 \text {a n d} E \left\{X _ {1} \left(z _ {1}\right) \right\} \text {d o e s n o t p e n d e n o n} z _ {1}.
$$

holds.

Remark: However, $\beta_{3} = 0$ in the first condition rules out the dependence of $Y$ on $X_{1}$ , contradicting the existence of unmeasured confounder $U$ between $X_{1}$ and $Y$ ; the independence of $E\{X_{1}(z_{1})\}$ on $z_{1}$ rules out the dependence of $X_{1}$ on $Z_{1}$ , contradicting with the existence of the arrow from $Z_{1}$ on $X_{1}$ . That is, if there is an unmeasured confounder $U$ between $X_{1}$ and $Y$ and there is an arrow from $Z_{1}$ on $X_{1}$ , then the formula of $E\{Y(z_{1}, z_{2})\}$ in Example 29.1 must depend on $(z_{1}, z_{2})$ , which leads to a contradiction with the absence of arrows from $(Z_{1}, Z_{2})$ to $Y$ .

# 29.2 Recursive estimation under the null model

Consider the recursive estimation method in 29.2.2 under the causal diagram in Problem 29.1. Show that based on linear models, the estimator converges to 0.

# 29.3 IPW under MSM

Prove Theorem 29.3.

# 29.4 A nonlinear example of Definition 29.2

Another leading example of Definition 29.2 is

$$
\operatorname {l o g i t} \left[ \Pr \left\{Y \left(z _ {1}, z _ {2}\right) = 1 \mid X _ {0} \right\} \right] = \beta_ {0} + \beta_ {1} z _ {1} + \beta_ {2} z _ {2} + \beta_ {3} ^ {\mathsf {T}} X _ {0}. \tag {29.13}
$$

If we observe all potential outcomes, we can solve $\beta$ by minimizing the expectation of the negative log-likelihood function (see Chapter B.6.2 for a simpler version):

$$
\beta = \arg \min  _ {b} \sum_ {z _ {2}} \sum_ {z _ {1}} E \left\{\log \left(1 + e ^ {\ell}\right) - Y \left(z _ {1}, z _ {2}\right) \ell \right\} \tag {29.14}
$$

where $\ell = \beta_0 + \beta_1z_1 + \beta_2z_2 + \beta_3^{\mathrm{T}}X_0$ . Under sequential ignorability, we can solve $\beta$ from the following minimization problem that only involves observables.

Theorem 29.5 (IPW under MSM) Under Assumption 29.1 and Definition 29.2, the $\beta$ in (29.14) equals

$$
\beta = \arg \min _ {b} \sum_ {z _ {2}} \sum_ {z _ {1}} E \left[ \frac {1 (Z _ {1} = z _ {1}) 1 (Z _ {2} = z _ {2})}{e (z _ {1} , X _ {0}) e (z _ {2} , Z _ {1} , X _ {1} , X _ {0})} \left\{\log (1 + e ^ {\ell}) - Y (z _ {1}, z _ {2}) \ell \right\} \right].
$$

Prove Theorem 29.5.

Remark: Theorem 29.5 implies a simple estimation strategy based on weighted regressions. For instance, under (29.13), we can fit weighted logistic regression of $Y_{i}$ on $(1,Z_{1i},Z_{2i},X_{0i})$ with weights $\hat{e}_1^{-1}(Z_{1i},X_{0i})\hat{e}_{2i}^{-1}(Z_{2i},Z_{1i},X_{1i},X_{0i})$ .

# 29.5 Structural nested model with a single time point

Recall the standard setting of observational studies with IID data drawn from $\{X,Z,Y(1),Y(0)\}$ . Define the propensity score as $e(X) = \operatorname{pr}(Z = 1 \mid X)$ . Assume

$$
Z \bot Y (0) \mid X
$$

and the following structural nested model.

Definition 29.4 (structural nested model with a single time point) The conditional mean of the individual effect is

$$
E \left\{Y (z) - Y (0) \mid Z = z, X \right\} = g (z, X; \beta).
$$

In Definition 29.4, a logical restriction is $g(0,X;\beta) = 0$ . Prove the following results.

1. We have

$$
E \{Y - g (Z, X; \beta) \mid X, Z \} = E \{Y - g (Z, X; \beta) \mid X \} = E \{Y (0) \mid X \}.
$$

2. We have

$$
E \left[ h (X) \{Z - e (X) \} \{Y - g (Z, X; \beta) \} \right] = 0 \tag {29.15}
$$

for any function $h$ , provided that the moment exists.

Remark: Equation (29.15) is the basis for parameter estimation. Consider a special case of Definition 29.4 with $g(z, X; \beta) = \beta z$ . Choose $h(X) = 1$ to obtain

$$
E \{(Z - e (X)) (Y - \beta Z) \} = 0.
$$

Solve for $\beta$ to obtain

$$
\beta = \frac {E \left\{\left(Z - e (X)\right) Y \right\}}{E \left\{\left(Z - e (X)\right) Z \right\}}.
$$

Therefore, $\beta$ equals the coefficient of $Z$ in the TSLS of $Y$ on $Z$ with $Z - e(X)$ being the IV for $Z$ . With some basic calculations, we can also show that

$$
\beta = \frac {\operatorname {c o v} \{Z - e (X) , Y \}}{\operatorname {c o v} \{Z - e (X) \}}.
$$

Therefore, $\beta$ equals the coefficient of $Z - e(X)$ in the OLS of $Y$ on $Z - e(X)$ , which appeared in Chapter 14.1 before.

Consider another special case of Definition 29.4 with $g(z, X; \beta) = (\beta_0 + \beta_1^{\mathsf{T}}X)z$ . Choose $h(X) = (1, X)$ to obtain

$$
E \left\{\binom {Z - e (X)} {(Z - e (X)) X} (Y - \beta_ {0} Z - \beta_ {1} ^ {\intercal} X Z) \right\} = 0.
$$

That is, $(\beta_0,\beta_1)$ equal the coefficients in the TSLS of $Y$ on $(Z,XZ)$ with $(Z - e(X),(Z - e(X))X)$ being the IV for $(Z,XZ)$ .

# 29.6 Estimation under Example 29.4

We can estimate the $\beta$ 's by solving the empirical version of the estimating equations in Example 29.4. We first estimate the two propensity scores and obtain the centered treatment

$$
\tilde {Z} _ {1 i} = Z _ {1 i} - \hat {e} (1, X _ {0 i})
$$

at time point 1 and

$$
\tilde {Z} _ {2 i} = Z _ {2 i} - \hat {e} (1, Z _ {1 i}, X _ {1 i}, X _ {0 i})
$$

at time point 2.

Show that we can estimate $\beta_{2}$ and $\beta_{3}$ by running TSLS of $Y_{i}$ on $(Z_{2i}, Z_{1i}Z_{2i})$ with $(\check{Z}_{2i}, Z_{1i}\check{Z}_{2i})$ as the IV for $(Z_{2i}, Z_{1i}Z_{2i})$ , and then we can estimate $\beta_{1}$ by running TSLS of $Y_{i} - (\hat{\beta}_{2} + \hat{\beta}_{3}Z_{1i})Z_{2i}$ on $Z_{1i}$ with $\check{Z}_{1i}$ as the IV for $Z_{1i}$ .

# 29.7 $g$ -formula with a treatment at multiple time points

Extend the discussion to the setting with $K$ time points. The temporal ordering (but not the causal diagram) of the variables is

$$
X _ {0} \rightarrow Z _ {1} \rightarrow X _ {1} \rightarrow Z _ {2} \rightarrow \dots \rightarrow X _ {K - 1} \rightarrow Z _ {K}.
$$

Introduce the notation $\overline{Z}_k = (Z_1, \ldots, Z_k)$ and $\overline{X}_k = (X_0, X_1, \ldots, X_k)$ with lower case $\overline{z}_k$ and $\overline{x}_k$ denoting the corresponding realized values. With $k = 0$ , we have $\overline{X}_0 = X_0$ and $\overline{Z}_0$ is empty. Each unit has $2^K$ potential outcomes:

$$
Y (\bar {z} _ {K}) \text {f o r a l l} z _ {1}, \dots , z _ {K} = 0, 1.
$$

Assume sequential ignorability below.

Assumption 29.2 (sequential ignorability at multiple time points) We have

$$
Z _ {k} \perp Y (\bar {z} _ {K}) \mid (\bar {Z} _ {k - 1}, \bar {X} _ {k - 1})
$$

for all $k = 1,\ldots ,K$ and all $z_{1},\dots ,z_{K} = 0,1$

Prove Theorem 29.6 below.

Theorem 29.6 (g-formula with multiple time points) Under Assumption 29.2,

$$
E \{Y (\bar {z} _ {K}) \} = E \left[ \dots E \{E (Y | \bar {z} _ {K}, \overline {{X}} _ {K - 1}) | \bar {z} _ {K - 1}, \overline {{X}} _ {K - 2} \} \dots | z _ {1}, X _ {0} \right].
$$

Remark: In Theorem 29.6, I use the simplified notation “ $\overline{z}_k$ ” for “ $\overline{Z}_k = \overline{z}_k$ .” With discrete $X$ , Theorem 29.6 reduces to

$$
\begin{array}{l} E \left\{Y \left(\bar {z} _ {K}\right) \right\} = \sum_ {x _ {0}} \sum_ {x _ {1}} \dots \sum_ {x _ {K - 1}} E \left(Y \mid \bar {z} _ {K}, \bar {x} _ {K - 1}\right) \\ \cdot \Pr (x _ {K - 1} \mid \bar {z} _ {K - 1}, \bar {x} _ {K - 2}) \dots \Pr (x _ {1} \mid z _ {1}, x _ {0}) \Pr (x _ {0}); \\ \end{array}
$$

with continuous $X$ , Theorem 29.6 reduces to

$$
\begin{array}{l} E \{Y (\bar {z} _ {K}) \} = \int E (Y \mid \bar {z} _ {K}, \bar {x} _ {K - 1}) \\ \cdot f (x _ {K - 1} \mid \bar {z} _ {K - 1}, \bar {x} _ {K - 2}) \dots f (x _ {1} \mid z _ {1}, x _ {0}) f (x _ {0}) \mathrm {d} \bar {x} _ {K - 1}. \\ \end{array}
$$

# 29.8 IPW with treatments at multiple time points

Inherit the setting of Problem 29.7. Define the propensity score at $K$ time points as

$$
e (z _ {1}, X _ {0}) = \operatorname * {p r} (Z _ {1} = z _ {1} \mid X _ {0}),
$$

：

$$
{e (z _ {k}, \overline {{Z}} _ {k - 1}, \overline {{X}} _ {k - 1})} = {\operatorname * {p r} (Z _ {k} = z _ {k} \mid \overline {{Z}} _ {k - 1}, \overline {{X}} _ {k - 1}),}
$$

中

$$
e (z _ {K}, \overline {{Z}} _ {K - 1}, \overline {{X}} _ {K - 1}) = \operatorname * {p r} (Z _ {K} = z _ {K} \mid \overline {{Z}} _ {K - 1}, \overline {{X}} _ {K - 1}).
$$

Prove Theorem 29.8 below assuming overlap implicitly.

Theorem 29.7 (IPW with multiple time points) Under Assumption 29.2,

$$
E \{Y (\overline {{z}} _ {K}) \} = E \left\{\frac {1 (Z _ {1} = z _ {1}) \cdots 1 (Z _ {K} = z _ {K}) Y}{e (z _ {1} , X _ {0}) \cdots e (z _ {K} , \overline {{Z}} _ {K - 1} , \overline {{X}} _ {K - 1})} \right\}.
$$

Based on Theorem 29.8, construct the Horvitz-Thompson and Hajek estimators.

# 29.9 MSM with treatments at multiple time points

The number of potential outcomes grows exponentially with $K$ . The formulas in Problems 29.7 and 29.8 are not directly applicable in finite samples. We can impose the following structural assumptions on the potential outcomes.

Definition 29.5 (MSM with multiple time points) Assume

$$
E \left\{Y \left(\bar {z} _ {K}\right) \mid X _ {0} \right\} = f \left(\bar {z} _ {K}, X _ {0}; \beta\right).
$$

Two leading examples of Definition 29.5 are

$$
E \left\{Y \left(\bar {z} _ {K}\right) \mid X _ {0} \right\} = \beta_ {0} + \beta_ {1} \sum_ {k = 1} ^ {K} z _ {k} + \beta_ {2} ^ {\mathsf {T}} X _ {0}
$$

and

$$
E \{Y (\bar {z} _ {K}) \mid X _ {0} \} = \beta_ {0} + \sum_ {k = 1} ^ {K} \beta_ {k} z _ {k} + \beta_ {K + 1} ^ {\mathsf {T}} X _ {0}.
$$

If we know all the potential outcomes, we can solve $\beta$ from the following minimization problem:

$$
\beta = \arg \min _ {b} \sum_ {\overline {{z}} _ {K}} E \{Y (\overline {{z}} _ {K}) - f (\overline {{z}} _ {K}, X _ {0}; \beta) \} ^ {2}.
$$

Theorem 29.8 below shows that under Assumption 29.2, we can solve $\beta$ from a minimization problem that only involves observables.

Theorem 29.8 (IPW for MSM with multiple time points) Under Assumption 29.2,

$$
\beta = \arg \min _ {b} \sum_ {\overline {{z}} _ {K}} E \left[ \frac {1 (Z _ {1} = z _ {1}) \cdots 1 (Z _ {K} = z _ {K})}{e (z _ {1} , X _ {0}) \cdots e (z _ {K} , \overline {{Z}} _ {K - 1} , \overline {{X}} _ {K - 1})} \{Y - f (\overline {{z}} _ {K}, X _ {0}; \beta) \} ^ {2} \right].
$$

29.10 Structural nested model with treatments at multiple time points

Inherit the setting from Problem 29.7 and the notation from Problem 29.8. This problem presents a general structural nested model.

Definition 29.6 (structural nested model with multiple time points)

The conditional effect at time $k$ is

$$
E \left\{Y \left(\bar {z} _ {k}, 0\right) - Y \left(\bar {z} _ {k - 1}, 0\right) \mid \bar {z} _ {k}, \bar {X} _ {k - 1} \right\} = g _ {k} \left(\bar {z} _ {k}, \bar {X} _ {k - 1}; \beta\right)
$$

for all $\overline{z}_k$ and all $k = 1,\ldots ,K$ .

In Definition 29.6, a logical restriction is

$$
g _ {k} \left(0, \bar {z} _ {k - 1}, \bar {X} _ {k - 1}; \beta\right) = 0
$$

for all $\overline{z}_{k - 1}$ and all $k = 1,\ldots ,K$

Define

$$
U _ {k} (\beta) = Y - \sum_ {s = 1} ^ {k} g _ {s} \left(\bar {Z} _ {s}, \bar {X} _ {s - 1}; \beta\right)
$$

for all $k = 1,\ldots ,K$ . Theorem 29.9 below extends Theorem 29.4.

Theorem 29.9 Under Assumption 29.2 and Definition 29.6, we have

$$
E \left[ h _ {k} \left(\bar {Z} _ {k - 1}, \bar {X} _ {k - 1}\right) \left\{Z _ {k} - e \left(1, \bar {Z} _ {k - 1}, \bar {X} _ {k - 1}\right) \right\} U _ {k} (\beta) \right] = 0
$$

for any functions $h_k$ ( $k = 1, \dots, K$ ), provided that the moment exists.

Remark: Choosing appropriate $h_k$ 's, we can estimate $\beta$ by solving the empirical version of Theorem 29.9.

# 29.11 Recommended reading

Robins et al. (2000) reviewed the MSM. Naimi et al. (2017) reviewed the g-methods.

# Part VII

# Appendices

# A

# Probability and Statistics

This book assumes that the readers have basic knowledge of probability theory and statistical inference. Therefore, this chapter is not a comprehensive review of probability and statistics. For easy reference, I review the key concepts that are crucial for the main text.

# A.1 Probability

# A.1.1 Pearson correlation coefficient and squared multiple correlation coefficient

For two random variables $Y$ and $X$ , define the Pearson correlation coefficient as

$$
\rho_ {Y X} = \frac {\operatorname {c o v} (Y , X)}{\sqrt {\operatorname {v a r} (Y) \operatorname {v a r} (X)}}
$$

which measures the linear dependence of $Y$ on $X$ . The definition is symmetric in $Y$ and $X$ in that

$$
\rho_ {Y X} = \rho_ {X Y}.
$$

With a random variable $Y$ and a random vector $X$ , define the squared multiple correlation coefficient as

$$
R _ {Y X} ^ {2} = \operatorname {c o r r} ^ {2} (Y, X) = \frac {\operatorname {c o v} (Y , X) \operatorname {c o v} (X) ^ {- 1} \operatorname {c o v} (X , Y)}{\operatorname {v a r} (Y)}
$$

where $\operatorname{cov}(Y, X)$ is a row vector and $\operatorname{cov}(X, Y)$ is a column vector. It also measures the linear dependence of $Y$ on $X$ . But this definition is not symmetric in $Y$ and $X$ .

# A.1.2 Multivariate Normal random vector

A multivariate Normal random vector $\mathrm{N}(\mu, \Sigma)$ is determined by its mean vector $\mu$ and covariance matrix $\Sigma$ . Partition it into two parts:

$$
\left( \begin{array}{c} Y _ {1} \\ Y _ {2} \end{array} \right) \sim \mathrm {N} \left(\left( \begin{array}{c} \mu_ {1} \\ \mu_ {2} \end{array} \right), \left( \begin{array}{c c} \Sigma_ {1 1} & \Sigma_ {1 2} \\ \Sigma_ {2 1} & \Sigma_ {2 2} \end{array} \right)\right).
$$

First, the marginal distributions are Normal:

$$
Y _ {1} \sim \mathrm {N} \left(\mu_ {1}, \Sigma_ {1 1}\right), \quad Y _ {2} \sim \mathrm {N} \left(\mu_ {2}, \Sigma_ {2 2}\right).
$$

Second, if $\Sigma_{22}$ is positive definite, then the conditional distribution is also Normal:

$$
Y _ {1} \mid Y _ {2} = y _ {2} \sim \mathrm {N} \left(\mu_ {1} + \Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1} (y _ {2} - \mu_ {2}), \Sigma_ {1 1} - \Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1} \Sigma_ {2 1}\right).
$$

# A.1.3 $\chi^2$ and $t$ distributions

Assume $X_{1},\ldots ,X_{n}$ are IID $\mathbf{N}(0,1)$ . Then

$$
\sum_ {i = 1} ^ {n} X _ {i} ^ {2}
$$

follows a $\chi_n^2$ distribution with degrees of freedom $n$ . The $\chi_n^2$ distribution has mean $n$ and variance $2n$ .

Assume $X\sim \mathrm{N}(0,1),Q_n\sim \chi_n^2$ and $X\bot Q_{n}$ . Then

$$
\frac {X}{\sqrt {Q _ {n} / n}}
$$

follows a $t_n$ distribution with degrees of freedom $n$ . The $t_n$ distribution has mean 0 if $n > 1$ . When $n = 1$ , the $t_1$ distribution is also called the Cauchy distribution, which does not have a finite mean.

# A.1.4 Cauchy-Schwarz inequality

The Cauchy-Schwarz inequality has many forms. With two random variables $A$ and $B$ , we have

$$
| E (A B) | \leq \sqrt {E (A ^ {2}) E (B ^ {2})}
$$

with equality holding when $B = \beta A$ for some $\beta$ . Centering $A$ and $B$ to have mean 0, we have

$$
| \operatorname {c o v} (A, B) | \leq \sqrt {\operatorname {v a r} (A) \operatorname {v a r} (B)}
$$

with equality holding when $B = \alpha +\beta A$ for some $\alpha$ and $\beta$

When $A$ and $B$ are uniform random variables over finite sets $\{a_1, \ldots, a_n\}$ and $\{b_1, \ldots, b_n\}$ respectively, we have

$$
\left| \sum_ {i = 1} ^ {n} a _ {i} b _ {i} \right| \leq \sqrt {\sum_ {i = 1} ^ {n} a _ {i} ^ {2} \sum_ {i = 1} ^ {n} b _ {i} ^ {2}}
$$

with equality holding if there exists $\beta$ such that $b_{i} = \beta a_{i}$ for all $i$ 's.

# A.1.5 Tower property and variance decomposition

Given random variables or vectors $A, B, C$ , we have

$$
E (A) = E \{E (A \mid B) \}
$$

and

$$
E (A \mid C) = E \{E (A \mid B, C) \mid C \}.
$$

Given a random variable $A$ and random variables or vectors $B, C$ , we have

$$
\operatorname {v a r} (A) = E \left\{\operatorname {v a r} (A \mid B) \right\} + \operatorname {v a r} \{E (A \mid B) \}
$$

and

$$
\operatorname {v a r} (A \mid C) = E \left\{\operatorname {v a r} (A \mid B, C) \mid C \right\} + \operatorname {v a r} \{E (A \mid B, C) \mid C \}.
$$

When I was in graduate school, my professors Carl Morris and Joe Blitzstein called this formula the Eve's Law due to the "EVVE" form of the formula. They then went back to call the first tower property the Adam's Law.

Similarly, we can decompose the covariance as

$$
\operatorname {c o v} \left(A _ {1}, A _ {2}\right) = E \left\{\operatorname {c o v} \left(A _ {1}, A _ {2} \mid B\right) \right\} + \operatorname {c o v} \left\{E \left(A _ {1} \mid B\right), E \left(A _ {2} \mid B\right) \right\}
$$

and

$$
\operatorname {c o v} \left(A _ {1}, A _ {2} \mid C\right) = E \left\{\operatorname {c o v} \left(A _ {1}, A _ {2} \mid B, C\right) \mid C \right\} + \operatorname {c o v} \left\{E \left(A _ {1} \mid B, C\right), E \left(A _ {2} \mid B, C\right) \mid C \right\}.
$$

# A.1.6 Limiting theorems

Definition A.1 (convergence in probability) A sequence of random variables $(X_{n})_{n\geq 1}$ converges to $X$ in probability, if for every $\varepsilon >0$ , we have

$$
\Pr \left(\left| X _ {n} - X \right| > \varepsilon\right)\rightarrow 0
$$

$$
a s n \rightarrow \infty .
$$

Definition A.2 (convergence in distribution) A sequence of random variables $(X_{n})_{n\geq 1}$ converges to $X$ in distribution, if

$$
\operatorname {p r} \left(X _ {n} \leq x\right)\rightarrow \operatorname {p r} (X \leq x)
$$

for all continuity point $x$ of $\operatorname{pr}(X \leq x)$ , as $n \to \infty$ .

Convergence in probability is stronger than convergence in distribution. Definitions A.1 and A.2 are useful for stating the following two fundamental theorems on the sample average of independent and identically distributed (IID) random variables.

Theorem A.1 (law of large numbers) If $X_{1},\ldots ,X_{n}\stackrel {\mathrm{IIID}}{\sim}X$ with $E|X| < \infty$ , then $\bar{X} = n^{-1}\sum_{i = 1}^{n}X_{i}\to E(X)$ in probability.

The law of large numbers in Theorem A.1 states that the sample average is close to the population mean in the limit.

Theorem A.2 (central limit theorem (CLT)) If $X_{1},\ldots ,X_{n}\stackrel {\mathrm{IID}}{\sim}X$ with $\operatorname {var}(X) <   \infty$ , then

$$
\frac {\bar {X} - E (X)}{\sqrt {\operatorname {v a r} (X) / n}} \to \mathrm {N} (0, 1)
$$

in distribution.

The CLT in Theorem A.2 states that the standardized sample average is close to a standard Normal random variable in the limit.

Theorems A.1 and A.2 assume IID random variables for convenience. There are also many laws of large numbers and CLTs for the sample mean of independent or weakly dependent random variable (e.g., Durrett, 2019).

# A.1.7 Delta method

The delta method is a power tool to derive the asymptotic Normality of nonlinear functions of an asymptotically Normal random vector. I review a special case of the delta method below.

Theorem A.3 (delta method) Assume $\sqrt{n} (X_n - \mu) \to \mathrm{N}(0, \Sigma)$ in distribution and the function $g(x)$ has non-zero derivative $\nabla g(\mu)$ at $\mu$ . Then

$$
\sqrt {n} \{g (X _ {n}) - g (\mu) \} \rightarrow \mathrm {N} (0, (\nabla g (\mu)) ^ {\mathsf {T}} \Sigma \nabla g (\mu))
$$

in distribution.

I will omit the proof of Theorem A.3. It is intuitive based on the first-order Taylor expansion:

$$
g (X _ {n}) - g (\mu) \approx (\nabla g (\mu)) ^ {\intercal} (X _ {n} - \mu).
$$

So $\sqrt{n}\{g(X_n) - g(\mu)\}$ is close to the linear transformation of $\mathrm{N}(0,\Sigma)$ , which is $\mathrm{N}(0,(\nabla g(\mu))^{\mathsf{T}}\Sigma \nabla g(\mu))$ .

As illustrations, we can use the delta method to obtain the asymptotic Normality of the ratio and product.

Example A.1 (asymptotic Normality for the ratio) Assume

$$
\sqrt {n} \binom {Y _ {n} - \mu_ {Y}} {X _ {n} - \mu_ {X}} \rightarrow \mathrm {N} \left(\binom {0} {0}, \binom {\sigma_ {Y} ^ {2}} {\sigma_ {Y X}} \binom {\sigma_ {Y X}} {\sigma_ {X} ^ {2}}\right) \tag {A.1}
$$

in distribution with $\mu_X \neq 0$ . Apply Theorem A.3 to obtain that

$$
\sqrt {n} \left(\frac {Y _ {n}}{X _ {n}} - \frac {\mu_ {Y}}{\mu_ {X}}\right)\rightarrow \mathrm {N} \left(0, \frac {\sigma_ {Y} ^ {2}}{\mu_ {X} ^ {2}} + \frac {\mu_ {Y} ^ {2} \sigma_ {X} ^ {2}}{\mu_ {X} ^ {4}} - \frac {2 \mu_ {Y} \sigma_ {Y X}}{\mu_ {X} ^ {3}}\right) \tag {A.2}
$$

in distribution. In the special case that $X_{n}$ and $Y_{n}$ are asymptotically independent with $\sigma_{YX} = 0$ , the asymptotic variance of $Y_{n} / X_{n}$ simplifies to $\sigma_Y^2 /\mu_X^2 +\mu_Y^2\sigma_X^2 /\mu_X^4$ . I leave the details to Problem A.2.

The asymptotic variance in Example A.1 is a little cumbersome. An easier way to memorize it is based on the following approximation:

$$
\frac {Y _ {n}}{X _ {n}} - \frac {\mu_ {Y}}{\mu_ {X}} = \frac {Y _ {n} - \mu_ {Y} / \mu_ {X} \cdot X _ {n}}{X _ {n}} \approx \frac {Y _ {n} - \mu_ {Y} / \mu_ {X} \cdot X _ {n}}{\mu_ {X}}, \tag {A.3}
$$

so the asymptotic variance of the ratio equals the asymptotic variance of

$$
\frac {Y _ {n} - \mu_ {Y} / \mu_ {X} \cdot X _ {n}}{\mu_ {X}},
$$

which is a linear combination of $Y_{n}$ and $X_{n}$ . Slutsky's theorem can make the approximation in (A.3) rigorous but it is beyond this book.

Example A.2 (asymptotic Normality for the product) Assume (A.1). Apply Theorem A.3 to obtain that

$$
\sqrt {n} \left(X _ {n} Y _ {n} - \mu_ {X} \mu_ {Y}\right)\rightarrow \mathrm {N} \left(0, \mu_ {Y} ^ {2} \sigma_ {X} ^ {2} + \mu_ {X} ^ {2} \sigma_ {Y} ^ {2} + 2 \mu_ {X} \mu_ {Y} \sigma_ {X Y}\right) \tag {A.4}
$$

in distribution. In the special case that $X_{n}$ and $Y_{n}$ are asymptotically independent with $\sigma_{YX} = 0$ , the asymptotic variance of $X_{n}Y_{n}$ simplifies to $\mu_Y^2\sigma_X^2 +\mu_X^2\sigma_Y^2$ . I leave the details to Problem A.3.

# A.2 Statistical inference

# A.2.1 Point estimation

Assume that $\theta$ is the parameter of interest. Oftentimes, the problem also contains other parameters not of interest, denoted by $\eta$ . Statisticians call $\eta$ the nuisance parameter. Based on the data, we can compute an estimator $\hat{\theta}$ . Throughout this book, we take the frequentist's perspective by assuming that $\theta$ is a fixed number and $\hat{\theta}$ is random due to the randomness of data. Two basic requirements for an estimator are below.

Definition A.3 (unbiasedness) The estimator $\hat{\theta}$ is unbiased for $\theta$ if

$$
E (\hat {\theta}) = \theta
$$

for all possible values of $\theta$ and $\eta$ .

Definition A.4 (consistency) The estimator $\hat{\theta}$ is consistent for $\theta$ if

$$
\hat {\theta} \rightarrow \theta
$$

in probability as the sample size approaches to infinity, for all possible values of $\theta$ and $\eta$ .

Unbiasedness requires that the mean of the estimator is identical to the parameter of interest. Consistency requires that the estimator is close to the true parameter in the limit. Unbiasedness does not imply consistency, and consistency does not imply unbiasedness either. Unbiasedness can be restrictive because it is impossible even in some simple statistics problems. Consistency is often the basic requirement in most statistics problems.

# A.2.2 Confidence interval

A point estimator $\hat{\theta}$ is a random variable that differs from the true parameter $\theta$ . Statisticians are often interested in finding an interval that covers the true parameter with a certain given probability. This interval is computed based on the data, and it is random.

Definition A.5 (confidence interval) A data-dependent interval $[\hat{\theta}_{\mathrm{L}},\hat{\theta}_{\mathrm{U}}]$ is a confidence interval for $\theta$ with coverage probability at least $1 - \alpha$ if

$$
\Pr \left(\hat {\theta} _ {\mathrm {L}} \leq \theta \leq \hat {\theta} _ {\mathrm {U}}\right) \geq 1 - \alpha
$$

for all possible values of $\theta$ and $\eta$ .

Definition A.6 (asymptotic confidence interval) A data-dependent interval $[\hat{\theta}_{\mathrm{L}},\hat{\theta}_{\mathrm{U}}]$ is an asymptotic confidence interval for $\theta$ with coverage probability at least $1 - \alpha$ if

$$
\Pr \left(\hat {\theta} _ {\mathrm {L}} \leq \theta \leq \hat {\theta} _ {\mathrm {U}}\right)\rightarrow 1 - \alpha^ {\prime}, \quad a s n \rightarrow \infty
$$

with $\alpha' \leq \alpha$ , for all possible values of $\theta$ and $\eta$ .

A standard choice is $\alpha = 0.05$ . In Definitions A.5 and A.6, the coverage probabilities can be larger than the nominal level $1 - \alpha$ . That is, the definitions allow for over-coverage but do not allow for under-coverage. With over-coverage, we say that the confidence interval is conservative. Of course, we hope the confidence interval to be as narrow as possible. Otherwise, the definition of the confidence interval can be arbitrary.

# A.2.3 Hypothesis testing

Many applied problems can be formulated as testing a hypothesis:

$$
H _ {0}: \theta = 0.
$$

The decision rule $\phi$ is a binary function of the data: $\phi = 1$ if we reject $H_0$ ; $\phi = 0$ if we fail to reject $H_0$ . The type one error rate of the test is the probability of rejection if the null hypothesis holds. I review the definition below.

Definition A.7 (type one error rate) When $H_0$ holds, define the type one error rate of the test $\phi$ as the maximum value of the probability

$$
\operatorname * {p r} (\phi = 1)
$$

over all possible values of $\theta$ and $\eta$ .

A standard choice is to make sure that the type one error rate is below $\alpha = 0.05$ . The type two error rate of the test is the probability of no rejection if the null hypothesis does not hold. I review the definition below.

Definition A.8 (type two error rate) When $H_0$ does not hold, define the type two error rate of the test $\phi$ as the maximum value of the probability

$$
\operatorname {p r} (\phi = 0)
$$

over all possible values of $\theta$ and $\eta$ .

Given the control of the type one error rate under $H_0$ , we hope the type two error rate is as low as possible when $H_0$ does not hold.

# A.2.4 Wald-type confidence interval and test

Many statistics problems have the following structure. The parameter of interest is $\theta$ . We first find a consistent estimator $\hat{\theta}$ that converges in probability to $\theta$ , and show that it is asymptotically Normal with mean $\theta$ and variance $v$ which may depend on $\theta$ as well as the nuisance parameter $\eta$ . We then find a consistent estimator $\hat{v}$ for $v$ , based on analytic formulas or the bootstrap reviewed in Chapter A.6 later. The square root of $\hat{v}$ is called the standard error. We finally construct the Wald-type confidence interval for $\theta$ as

$$
\hat {\theta} \pm z _ {1 - \alpha / 2} \sqrt {\hat {v}}
$$

where $z_{1 - \alpha /2}$ is the $1 - \alpha /2$ upper quantile of the standard Normal random variable. It covers $\theta$ with probability approximately $1 - \alpha$ . When this interval excludes a particular $c$ , for example, $c = 0$ , we reject the null hypothesis $H_0(c):\theta = c$ , which is called the Wald test.

# A.2.5 Duality between constructing confidence sets and testing null hypotheses

Consider the statistical inference problem for a scalar parameter $\theta$ . A fundamental result in statistics is that constructing confidence sets for $\theta$ is equivalent to testing null hypotheses about $\theta$ . This is often called the duality between constructing confidence sets and testing null hypotheses.

Section A.2.4 has reviewed the duality based on the Wald-type confidence

interval and test. The duality also holds in general. Assume that $\hat{\Theta}$ is a $(1 - \alpha)$ -level confidence set for $\theta$ :

$$
\operatorname {p r} (\theta \in \hat {\Theta}) \geq 1 - \alpha .
$$

Then we can reject the null hypothesis $H_0(c) : \theta = c$ if $c$ is not in the set $\hat{\Theta}$ . This is a valid test because when $\theta$ indeed equals $c$ , we have the correct type one error rate $\operatorname{pr}(\theta \notin \hat{\Theta}) \leq \alpha$ . Conversely, if we test a sequence of null hypotheses $H_0(c) : \theta = c$ , we can obtain the corresponding $p$ -values, $p(c)$ , as a function of $c$ . Then the values of $c$ that we fail to reject at level $\alpha$ form a confidence set for $\theta$ :

$$
\hat {\Theta} = \{c: p (c) \geq \alpha \} = \{c: \text {f a i l t o r e j e c t} H _ {0} (c) \text {a t l e v e l} \alpha \}.
$$

It is a valid confidence set because

$$
\operatorname {p r} (\theta \in \hat {\Theta}) = \operatorname {p r} \{\text {f a i l t o r e j e c t} H _ {0} (\theta) \text {a t l e v e l} \alpha \} \geq 1 - \alpha .
$$

Here I use "confidence set" instead of "confidence interval" because $\hat{\Theta}$ based on inverting tests may not be an interval. See the use of the duality in Chapters A.4.2 and 3.6.1.

# A.3 Inference with two-by-two tables

# A.3.1 Fisher's exact test

Fisher proposed an exact test for $H_0: p_1 = p_0$ under the statistical model:

$$
n _ {1 1} \sim \operatorname {B i n o m i a l} \left(n _ {1}, p _ {1}\right), \quad n _ {0 1} \sim \operatorname {B i n o m i a l} \left(n _ {0}, p _ {0}\right), \quad n _ {1 1} \perp n _ {0 1}.
$$

The table below summarizes the data.

<table><tr><td></td><td>1</td><td>0</td><td>row sum</td></tr><tr><td>sample 1</td><td>n11</td><td>n10</td><td>n1</td></tr><tr><td>sample 0</td><td>n01</td><td>n00</td><td>n0</td></tr><tr><td>column sum</td><td>n.1</td><td>n.0</td><td>n</td></tr></table>

He argued that the sums $n_{11} + n_{01} = n \cdot 1$ and $n_{10} + n_{00} = n \cdot 0$ contain little information about the difference between $p_1$ and $p_0$ , and conditional on them, $n_{11}$ follows a Hypergeometric distribution that does not depend on the unknown parameter $p_1 = p_0$ under $H_0$ :

$$
\operatorname * {p r} (n _ {1 1} = k) = \frac {\binom {n _ {\cdot 1}} {k} \binom {n - n _ {\cdot 1}} {n _ {1} - k}}{\binom {n} {n _ {1}}}.
$$

In R, the function fisher.test implements this test.

# A.3.2 Estimation with two-by-two tables

Based on the model in Section A.3.1, we can estimate the parameters $p_1$ and $p_0$ by sample frequencies:

$$
\hat {p} _ {1} = \frac {n _ {1 1}}{n _ {1}}, \quad \hat {p} _ {0} = \frac {n _ {0 1}}{n _ {0}}.
$$

Therefore, we can estimate the risk difference, log risk ratio, and log odds ratio

$$
\begin{array}{r c l} \text {R D} & = & p _ {1} - p _ {0}, \end{array}
$$

$$
\log \mathrm {R R} = \log \frac {p _ {1}}{p _ {0}},
$$

$$
\log \operatorname {O R} = \log \frac {p _ {1} / (1 - p _ {1})}{p _ {0} / (1 - p _ {0})}
$$

by the sample analogs

$$
\begin{array}{r c l} \mathrm {R D} & = & \hat {p} _ {1} - \hat {p} _ {0}, \end{array}
$$

$$
\log \mathrm {R} \hat {\mathrm {R}} = \log \frac {\hat {p} _ {1}}{\hat {p} _ {0}},
$$

$$
\log \hat {\mathrm {O R}} = \log \frac {\hat {p} _ {1} / (1 - \hat {p} _ {1})}{\hat {p} _ {0} / (1 - \hat {p} _ {0})} = \log \frac {n _ {1 1} n _ {0 0}}{n _ {1 0} n _ {0 1}}.
$$

Based on the asymptotic approximation (see Problem A.5), the estimated variance for the above parameters are

$$
\frac {\hat {p} _ {1} (1 - \hat {p} _ {1})}{n _ {1}} + \frac {\hat {p} _ {0} (1 - \hat {p} _ {0})}{n _ {0}},
$$

$$
\frac {1 - \hat {p} _ {1}}{n _ {1} \hat {p} _ {1}} + \frac {1 - \hat {p} _ {0}}{n _ {0} \hat {p} _ {0}},
$$

$$
\frac {1}{n _ {1} \hat {p} _ {1} (1 - \hat {p} _ {1})} + \frac {1}{n _ {0} \hat {p} _ {0} (1 - \hat {p} _ {0})},
$$

respectively. The log transformation above yields better Normal approximations because the risk ratio and odds ratio are always positive.

# A.4 Two famous problems in statistics

# A.4.1 Behrens-Fisher problem

Consider the two-sample problem with $n_1$ units under the treatment and $n_0$ units under the control, respectively. Assume the outcomes under the treatment $\{Y_i : Z_i = 1\}$ are IID from $\mathrm{N}(\mu_1, \sigma_1^2)$ and the outcomes under the

control $\{Y_{i}:Z_{i} = 0\}$ are IID from $\mathrm{N}(\mu_0,\sigma_0^2)$ , respectively. The goal is to test $H_0:\mu_1 = \mu_0$

Start with the easier case with $\sigma_1^2 = \sigma_0^2$ . Coherent with Chapter 3, let

$$
\hat {\tilde {Y}} (1) = n _ {1} ^ {- 1} \sum_ {Z _ {i} = 1} Y _ {i}, \quad \hat {\tilde {Y}} (0) = n _ {0} ^ {- 1} \sum_ {Z _ {i} = 0} Y _ {i}
$$

denote the sample means of the outcomes under the treatment and control, respectively. A standard result is that

$$
t _ {\mathrm {e q u a l}} = \frac {\hat {\bar {Y}} (1) - \hat {\bar {Y}} (0)}{\sqrt {\frac {n}{n _ {1} n _ {0} (n - 2)} \left[ \sum_ {Z _ {i} = 1} \{Y _ {i} - \hat {\bar {Y}} (1) \} ^ {2} + \sum_ {Z _ {i} = 0} \{Y _ {i} - \hat {\bar {Y}} (0) \} ^ {2} \right]}} \sim t _ {n - 2}.
$$

Based on $t_{\mathrm{equal}}$ , we can construct a test for $H_0$ .

Now consider the more difficult case with possibly different $\sigma_1^2$ and $\sigma_0^2$ . The distribution of $t_{\mathrm{equal}}$ is no longer $t_{n - 2}$ . Estimating the variances separately, we can also define

$$
t _ {\mathrm {u n e q u a l}} = \frac {\hat {\bar {Y}} (1) - \hat {\bar {Y}} (0)}{\sqrt {\frac {\hat {S} ^ {2} (1)}{n _ {1}} + \frac {\hat {S} ^ {2} (0)}{n _ {0}}}},
$$

where

$$
\hat {S} ^ {2} (1) = (n _ {1} - 1) ^ {- 1} \sum_ {Z _ {i} = 1} \{Y _ {i} - \hat {\bar {Y}} (1) \} ^ {2}, \quad \hat {S} ^ {2} (0) = (n _ {0} - 1) ^ {- 1} \sum_ {Z _ {i} = 0} \{Y _ {i} - \hat {\bar {Y}} (0) \} ^ {2}
$$

are the sample variances of the outcomes under the treatment and control, respectively. Unfortunately, the exact distribution of $t_{\mathrm{unequal}}$ depends on the known variances. Testing $H_0$ without assuming equal variances is the famous Behrens-Fisher problem. With large sample sizes $n_1$ and $n_0$ , the CLT ensures that $t_{\mathrm{unequal}}$ is approximately $\mathrm{N}(0,1)$ . So we can construct an approximate test for $H_0$ . By duality, a large-sample Wald-type confidence interval for $\mu_1 - \mu_0$ is

$$
\hat {\tilde {Y}} (1) - \hat {\tilde {Y}} (0) \pm z _ {1 - \alpha / 2} \sqrt {\frac {\hat {S} ^ {2} (1)}{n _ {1}} + \frac {\hat {S} ^ {2} (0)}{n _ {0}}}
$$

where $z_{1 - \alpha /2}$ is the $1 - \alpha /2$ upper quantile of the standard Normal random variable.

# A.4.2 Fieller-Creasy problem

Consider the two-sample problem with $n_1$ units under the treatment and $n_0$ units under the control, respectively. Assume the outcomes under the treatment $\{Y_i:Z_i = 1\}$ are IID from $\mathrm{N}(\mu_1,1)$ and the outcomes under the control $\{Y_i:Z_i = 0\}$ are IID from $\mathrm{N}(\mu_0,1)$ , respectively. The goal is to estimate

$\gamma = \mu_1 / \mu_0$ . We can use $\hat{\gamma} = \hat{\bar{Y}}(1) / \hat{\bar{Y}}(0)$ to estimate $\gamma$ . However, the point estimator has a complicated distribution, which does not yield a simple procedure to construct the confidence interval for $\gamma$ .

Fieller's confidence interval can be formulated as inverting tests for a sequence of null hypotheses: $H_0(c) : \gamma = c$ . Under $H_0(c)$ , we have

$$
\frac {\hat {\tilde {Y}} (1) - c \hat {\tilde {Y}} (0)}{\sqrt {1 / n _ {1} + c ^ {2} / n _ {0}}} \sim \mathrm {N} (0, 1)
$$

which motivates the confidence interval

$$
\left\{c: \left| \frac {\hat {\tilde {Y}} (1) - c \hat {\tilde {Y}} (0)}{\sqrt {1 / n _ {1} + c ^ {2} / n _ {0}}} \right| \leq z _ {1 - \alpha / 2} \right\}
$$

where $z_{1 - \alpha /2}$ is the $1 - \alpha /2$ upper quantile of the standard Normal random variable.

# A.5 Monte Carlo method in statistics

The Monte Carlo method is a powerful tool in statistics. I will review its basic use in approximating expectations or averages, which is fundamental in understanding the idea of FRT introduced in Chapter 3.

If our goal is to calculate $\theta = E\{g(Y)\}$ with $Y$ being a random variable, we can simply draw IID samples $Y_{1},\ldots ,Y_{n}$ from the distribution of $Y$ and obtain the moment estimator for $\theta$ :

$$
\hat {\theta} = n ^ {- 1} \sum_ {i = 1} ^ {n} g (Y _ {i}).
$$

As a special case, $Y$ is a uniform distribution over $\{y_1, \ldots, y_N\}$ and $\theta = N^{-1} \sum_{i=1}^{N} g(y_i)$ . We can draw $n$ IID samples $\{Y_1, \ldots, Y_n\}$ from $\{y_1, \ldots, y_N\}$ to obtain the moment estimator $\hat{\theta}$ defined above. This is called sampling with replacement, which is different from sampling without replacement reviewed in Chapter C.

# A.6 Bootstrap

It is often very tedious to derive the variance formulas for complex estimators. Efron (1979) proposed the bootstrap as a general tool for variance estimation.

There are many versions of the bootstrap (Davison and Hinkley, 1997). In this book, we only need the most basic one: the nonparametric bootstrap, which will be simply called the bootstrap.

Consider the generic setting with

$$
Y _ {1}, \ldots , Y _ {n} \stackrel {{\text {I I D}}} {{\sim}} Y,
$$

where $Y_{i}$ can be a general random element denoting the observed data for unit $i$ . An estimator $\hat{\theta}$ is a function of the observed data: $\hat{\theta} = T(Y_1, \ldots, Y_n)$ . When $T$ is a complex function, it may not be easy to obtain the variance or asymptotic variance of $\hat{\theta}$ .

The uncertainty of $\hat{\theta}$ is driven by the IID sampling of $Y_{1},\ldots ,Y_{n}$ from the true distribution. Although the true distribution is unknown, it can be well approximated by its empirical version

$$
\hat {F} _ {n} (y) = n ^ {- 1} \sum_ {i = 1} ^ {n} I \left(Y _ {i} \leq y\right),
$$

when the sample size $n$ is large. If we believe this approximation, we can simulate $\hat{\theta}$ by sampling

$$
\left(Y _ {1} ^ {*}, \ldots , Y _ {n} ^ {*}\right) \stackrel {\mathrm {I I D}} {\sim} \hat {F} _ {n} (y).
$$

Because $\hat{F}_n(y)$ is a discrete distribution with mass $1 / n$ on each observed data point, the simulation of $\hat{\theta}$ reduces to the following procedure:

1. sample $(Y_1^*,\ldots ,Y_n^*)$ from $\{Y_{1},\dots ,Y_{n}\}$ with replacement;   
2. compute $\hat{\theta}^{*} = T(Y_{1}^{*},\dots ,Y_{n}^{*})$   
3. repeat the above two steps $B$ times to obtain the bootstrap replicates $\{\hat{\theta}_1^*, \dots, \hat{\theta}_B^*\}$ .

We can then approximate the (asymptotic) variance of $\hat{\theta}$ by the sample variance of the bootstrap replicates:

$$
\hat {V} _ {\mathrm {b o o t}} = (B - 1) ^ {- 1} \sum_ {b = 1} ^ {B} (\hat {\theta} _ {b} ^ {*} - \bar {\theta} ^ {*}) ^ {2},
$$

where $\bar{\theta}^{*} = B^{-1}\sum_{b = 1}^{B}\hat{\theta}_{b}^{*}$ . The bootstrap confidence interval based on the Normal approximation is then

$$
\hat {\theta} \pm z _ {1 - \alpha / 2} \sqrt {\hat {V} _ {\mathrm {b o o t}}},
$$

where $z_{1 - \alpha /2}$ is the $1 - \alpha /2$ upper quantile of the standard Normal random variable.

I use the following simple example to illustrate the idea of the bootstrap.

With $n = 100$ IID observations $Y_{i}$ 's from $\mathrm{N}(1,1)$ , the sample mean should be close to 1 with variance $1 / 100 = 0.01$ . Over 500 simulations, the classic variance estimator and the bootstrap variance estimator with $B = 200$ both have average values close to 0.01.

```diff
>>> sample size
n = 100
>>> number of Monte Carlo simulations
MC = 500
>>> number of bootstrap replicates B
n.boot = 200
>>> simulation = replicate(MC, {
+ Y = rnorm(n, 1, 1)
+ boot(mu.hat = replicate(n.boot, {
+ index = sample(1:n, n, replace = TRUE)
+ mean(Y[index])
+ })\)
+ c(mean(Y), var(Y)/n, var.boot(mu.hat))
+})
>>> summarize the results
>> apply(simulation, 1, mean)
[1] 0.997602961 0.010006303 0.009921895 
```

# A.7 Homework problems

# A.1 Independent but not IID data

Assume that the $Y_{i}$ 's are independent with mean $\mu_{i}$ and variances $\sigma_{i}^{2}$ for $i = 1,\ldots ,n$ . The parameter of interest is $\mu = n^{-1}\sum_{i = 1}^{n}\mu_{i}$ . Show that $\hat{\mu} = n^{-1}\sum_{i = 1}^{n}Y_{i}$ is unbiased for $\mu$ and find its variance. Show that the usual variance estimator for IID data

$$
\hat {v} = \{n (n - 1) \} ^ {- 1} \sum_ {i = 1} ^ {n} \left(Y _ {i} - \hat {\mu}\right) ^ {2}
$$

is a conservative estimator for the variance of $\hat{\mu}$ in the sense that

$$
E (\hat {v}) - \operatorname {v a r} (\hat {\mu}) = \{n (n - 1) \} ^ {- 1} \sum_ {i = 1} ^ {n} \left(\mu_ {i} - \mu\right) ^ {2} \geq 0.
$$

Remark: Consider a simpler case with $\mu_{i} = \mu$ and $\sigma_i^2 = \sigma^2$ for all $i = 1,\ldots ,n$ . The sample mean is unbiased for $\mu$ with variance $\sigma^2 /n$ . Moreover, an unbiased estimator for the variance $\sigma^2 /n$ is $\hat{\sigma}^2 /n = \hat{v}$ , where $\hat{\sigma}^2 = (n - 1)^{-1}\sum_{i = 1}^{n}(Y_i - \hat{\mu})^2$ . This problem states a more general result for the case with independent but not identically distributed observations. The result has

an important implication for Theorem 7.1 for the matched-pairs experiment discussed in Chapter 7.

A.2 Asymptotic Normality of ratio

Prove (A.2).

A.3 Asymptotic Normality of product

Prove (A.4).

A.4 Product of two independent Normals

Assume $X\sim \mathrm{N}(\mu_X,\sigma_X^2),Y\sim \mathrm{N}(\mu_Y,\sigma_Y^2)$ and $X\bot Y$ . Show that

$$
\mathrm {v a r} (X Y) = \sigma_ {X} ^ {2} \sigma_ {Y} ^ {2} + \mu_ {X} ^ {2} \sigma_ {Y} ^ {2} + \mu_ {Y} ^ {2} \sigma_ {X} ^ {2}.
$$

Remark: This problem gives a non-asymptotic form of Example A.2.

A.5 Variance estimators in two-by-two tables

Use the delta method to show the variance estimators in Section A.3.2.

A.6 Fisher weighting

Assume that we have $p$ independent unbiased estimators $\hat{\theta}_1, \dots, \hat{\theta}_p$ for a common parameter $\theta$ :

$$
E (\hat {\theta} _ {j}) = \theta , \quad (j = 1, \dots , p).
$$

The estimator $\hat{\theta}_j$ has variance $v_{j}$ $(j = 1,\dots ,p)$

Construct a new estimator

$$
\hat {\theta} = \sum_ {j = 1} ^ {p} w _ {j} \hat {\theta} _ {j}
$$

with nonrandom constants $w_{j}$ 's. Show that $\hat{\theta}$ is unbiased for estimating $\theta$ if $\sum_{j=1}^{p} w_{j} = 1$ . Show that the optimal $w_{j}$ 's such that $\hat{\theta}$ has the smallest variance under the constraint $\sum_{j=1}^{p} w_{j} = 1$ are

$$
w _ {j} ^ {*} = \frac {1 / v _ {j}}{\sum_ {j ^ {\prime} = 1} ^ {p} 1 / v _ {j ^ {\prime}}}, (j = 1, \ldots , p).
$$

Show that the resulting estimator $\hat{\theta}^{*} = \sum_{j=1}^{p} w_{j}^{*}\hat{\theta}_{j}$ has variance

$$
\operatorname {v a r} \left(\hat {\theta} ^ {*}\right) = \frac {1}{\sum_ {j = 1} ^ {p} 1 / v _ {j}}.
$$

Remark: This is called Fisher weighting. The optimal weights are proportional to the inverses of the variances.

# B

# Linear and Logistic Regressions

# B.1 Population ordinary least squares

Assume that $(x_{i},y_{i})_{i = 1}^{n}\stackrel {\mathrm{IID}}{\sim}(x,y)$ , where $x$ is a $p$ -dimensional random scalar or vector and $y$ is a random scalar. Below I will use $(x,y)$ to denote a general observation, dropping the subscript $i$ for simplicity. Define the population ordinary least squares (OLS) coefficient as

$$
\beta = \arg \min  _ {b} E \left\{\left(y - x ^ {\top} b\right) ^ {2} \right\}.
$$

The objective function is quadratic in $b$ , so we can show that the minimizer is

$$
\beta = \left\{E \left(x x ^ {\top}\right) \right\} ^ {- 1} E (x y)
$$

if the moments exist and $E(xx^{\mathsf{T}})$ is invertible.

With $\beta$ , we can define $x^{\mathsf{T}}\beta$ as the linear projection of $y$ on $x$ , and define

$$
\varepsilon = y - x ^ {\mathsf {T}} \beta \tag {B.1}
$$

as the population residual. By the definition of $\beta$ , we can verify that

$$
E (x \varepsilon) = E \left\{x \left(y - x ^ {\mathsf {T}} \beta\right) \right\} = E (x y) - E \left(x x ^ {\mathsf {T}}\right) \beta = 0.
$$

Example B.1 (population OLS with the intercept) If we include 1 as a component of $x$ , then

$$
E (\varepsilon) = E (y - x ^ {\top} \beta) = 0
$$

which further implies that $\operatorname{cov}(x, \varepsilon) = 0$ . So with an intercept in $\beta$ , the mean of the population residual must be zero, and it is uncorrelated with other covariates by construction.

Example B.2 (univariate population OLS with the intercept) An important special case is that for scalars $x$ and $y$ , we can define

$$
(\alpha , \beta) = \arg \min  _ {a, b} E \left\{(y - a - b x) ^ {2} \right\}
$$

which have explicit formulas

$$
\beta = \frac {\operatorname {c o v} (x , y)}{\operatorname {v a r} (x)}, \quad \alpha = E (y) - \beta E (x).
$$

Example B.3 (univariate population OLS without an intercept) Without intercept, we can define

$$
\gamma = \arg \min  _ {c} E \left\{\left(y - c x\right) ^ {2} \right\}
$$

which equals

$$
\gamma = \frac {E (x y)}{E \left(x ^ {2}\right)}.
$$

When $x$ has mean zero, $\gamma$ equals the $\beta$ in Example B.2.

We can also rewrite (B.1) as

$$
y = x ^ {\mathrm {T}} \beta + \varepsilon , \tag {B.2}
$$

which holds by the definition of the population OLS coefficient and residual without any modeling assumption. We call (B.2) the population OLS decomposition.

# B.2 Sample ordinary least squares

Based on data $(x_{i},y_{i})_{i = 1}^{n}\stackrel {\mathrm{~IID}}{\sim}(x,y)$ , we can easily obtain the moment estimator for the population OLS coefficient

$$
\hat {\beta} = \left(n ^ {- 1} \sum_ {i = 1} ^ {n} x _ {i} x _ {i} ^ {\mathsf {T}}\right) ^ {- 1} \left(n ^ {- 1} \sum_ {i = 1} ^ {n} x _ {i} y _ {i}\right),
$$

and the residuals $\hat{\varepsilon}_i = y_i - x_i^\top \hat{\beta}$ . This is called the sample OLS or simply the OLS. The OLS coefficient $\hat{\beta}$ minimizes the residual sum of squares

$$
\hat {\beta} = \arg \min  _ {b} n ^ {- 1} \sum_ {i = 1} ^ {n} \left(y _ {i} - x _ {i} ^ {\top} b\right) ^ {2},
$$

so it must satisfy

$$
\sum_ {i = 1} ^ {n} x _ {i} \left(y _ {i} - x _ {i} ^ {\mathsf {T}} \hat {\beta}\right) = 0,
$$

which is sometimes called the Normal equation. The fitted values, also called the linear projections of $y_{i}$ on $x_{i}$ , equal

$$
\hat {y} _ {i} = x _ {i} ^ {\mathsf {T}} \hat {\beta} \quad (i = 1, \dots , n).
$$

Using the matrix notation

$$
X = \left( \begin{array}{c} x _ {1} ^ {\mathsf {T}} \\ \vdots \\ x _ {n} ^ {\mathsf {T}} \end{array} \right), \quad Y = \left( \begin{array}{c} y _ {1} \\ \vdots \\ y _ {n} \end{array} \right),
$$

we can write the OLS coefficient as

$$
\hat {\beta} = \left(X ^ {\mathsf {T}} X\right) ^ {- 1} X ^ {\mathsf {T}} Y
$$

and the fitted vector as

$$
\hat {Y} = X \hat {\beta} = X (X ^ {\intercal} X) ^ {- 1} X ^ {\intercal} Y.
$$

Define the hat matrix as

$$
H = X (X ^ {\intercal} X) ^ {- 1} X ^ {\intercal}.
$$

Then we also have $\hat{Y} = HY$ , justifying the name "hat matrix." The diagonal elements of $H$ , $h_{ii}$ 's, are often called the leverage scores.

Assuming finite fourth moments of $(x,y)$ , we can use the law of large numbers and the CLT to show that

$$
\sqrt {n} (\hat {\beta} - \beta) \rightarrow \mathrm {N} (0, V)
$$

in distribution with $V = B^{-1}MB^{-1}$ , where $B = E(xx^{\mathsf{T}})$ and $M = E(\varepsilon^{2}xx^{\mathsf{T}})$ . So a moment estimator for the asymptotic variance of $\hat{\beta}$ is

$$
\hat {V} _ {\mathrm {E H W}} = n ^ {- 1} \left(n ^ {- 1} \sum_ {i = 1} ^ {n} x _ {i} x _ {i} ^ {\mathsf {T}}\right) ^ {- 1} \left(n ^ {- 1} \sum_ {i = 1} ^ {n} \hat {\varepsilon} _ {i} ^ {2} x _ {i} x _ {i} ^ {\mathsf {T}}\right) \left(n ^ {- 1} \sum_ {i = 1} ^ {n} x _ {i} x _ {i} ^ {\mathsf {T}}\right) ^ {- 1}, \tag {B.3}
$$

which is called the Eicker-Huber-White (EHW) robust covariance estimator (Eicker, 1967; Huber, 1967; White, 1980). We can show that $n\hat{V}_{\mathrm{EHW}} \to V$ in probability. Based on $\hat{\beta}$ and $\hat{V}_{\mathrm{EHW}}$ , we can make inference about the population OLS coefficient $\beta$ .

There are many variants of the EHW robust covariance estimator based on the leverage scores (Long and Ervin, 2000). In particular, the HC1 variant modifies $\hat{\varepsilon}_i^2$ to $\hat{\varepsilon}_i^2 / (n - p)$ , the HC2 variant modifies $\hat{\varepsilon}_i^2$ to $\hat{\varepsilon}_i^2 / (1 - h_{ii})$ , and the HC3 variant modifies $\hat{\varepsilon}_i^2$ to $\hat{\varepsilon}_i^2 / (1 - h_{ii})^2$ , in the definition of $\hat{V}_{\mathrm{EHW}}$ .

# B.3 Frisch-Waugh-Lovell Theorem

The Frisch-Waugh-Lovell (FWL) theorem has two versions: one at the population level and the other at the sample level. It reduces multivariate OLS to univariate OLS and therefore facilitates the understanding and calculation of the OLS coefficients. Below I will present special cases of the FWL theorem which are enough for this book.

Theorem B.1 (population FWL) The coefficient of $x_{1}$ in the OLS fit of $y$ on $(x_{1}, x_{2}, \ldots, x_{p})$ equals the coefficient of $\tilde{x}_{1}$ in the OLS fit of $y$ or $\tilde{y}$ on $\tilde{x}_{1}$ , where $\tilde{y}$ is the residual from the OLS fit of $y$ on $(x_{2}, \ldots, x_{p})$ and $\tilde{x}_{1}$ is the residual from the OLS fit of $x_{1}$ on $(x_{2}, \ldots, x_{p})$ .

In Theorem B.1, residualizing $x_{1}$ is crucial but residualizing $y$ is not.

Theorem B.2 (sample FWL) With data $(Y, X_1, X_2, \ldots, X_p)$ containing column vectors, the coefficient of $X_1$ in the OLS fit of $Y$ on $(X_1, X_2, \ldots, X_p)$ equals the coefficient of $\tilde{X}_1$ in the OLS fit of $Y$ or $\tilde{Y}$ on $\tilde{X}_1$ , where $\tilde{Y}$ is the residual vector from the OLS fit of $Y$ on $(X_2, \ldots, X_p)$ and $\tilde{X}_1$ is the residual vector from the OLS fit of $X_1$ on $(X_2, \ldots, X_p)$ .

Again, in Theorem B.2, residualizing $X_{1}$ is crucial but residualizing $Y$ is not. Ding (2021) gives more numerical properties related to the sample FWL theorem.

# B.4 Linear model

Sometimes, we impose a stronger model assumption which requires the conditional mean of $y$ given $x$ is linear:

$$
E (y \mid x) = x ^ {\top} \beta
$$

or, equivalently,

$$
y = x ^ {\top} \beta + \varepsilon \qquad \text {w i t h} \qquad E (\varepsilon \mid x) = 0,
$$

which is called the restricted mean model. Under this model, the population OLS coefficient is the true parameter of interest:

$$
\begin{array}{l} \left\{E \left(x x ^ {\top}\right) \right\} ^ {- 1} E (x y) = \left\{E \left(x x ^ {\top}\right) \right\} ^ {- 1} E \left\{x E (y \mid x) \right\} \\ = \left\{E \left(x x ^ {\top}\right) \right\} ^ {- 1} E \left(x x ^ {\top} \beta\right) \\ = \beta . \\ \end{array}
$$

Moreover, the population OLS coefficient does not depend on the distribution of $x$ . The asymptotic inference in Section B.1 applies to this model too.

In the special case with $\operatorname{var}(\varepsilon \mid x) = \sigma^2$ , the asymptotic variance of the OLS coefficient reduces to

$$
V = \sigma^ {2} \{E (x x ^ {\intercal}) \} ^ {- 1}
$$

so a simpler moment estimator for the asymptotic variance of $\hat{\beta}$ is

$$
\hat {V} _ {\mathrm {O L S}} = \hat {\sigma} ^ {2} \left(\sum_ {i = 1} ^ {n} x _ {i} x _ {i} ^ {\top}\right) ^ {- 1} \tag {B.4}
$$

where $\hat{\sigma}^2 = (n - p)^{-1}\sum_{i = 1}^{n}\hat{\varepsilon}_i^2$ is an unbiased estimator for $\sigma^2$ , recalling that $n$

denotes the sample size and $p$ denotes the dimension of $x$ . This is the standard covariance estimator from the 1m function.

Based on the BostonHousing data, we first obtain the standard output from the $1\text{m}$ function.

```julia
> library("mlbench")
> data(BostonHousing)
> ols.fit = lm(medv ~ ., data = BostonHousing)
> summary(ols.fit) 
```

```txt
Call:  
lm(formula = medv ~ ., data = BostonHousing) 
```

```batch
Residuals: Min 1Q Median 3Q Max -15.595 -2.730 -0.518 1.777 26.199 
```

Coefficients: Estimate Std. Error t value $\mathrm{Pr}(|t|)$ (Intercept) 3.646e+01 5.103e+00 7.144 3.28e-12 *** crim -1.080e-01 3.286e-02 -3.287 0.001087 ** zn 4.642e-02 1.373e-02 3.382 0.000778 *** indus 2.056e-02 6.150e-02 0.334 0.738288 chas1 2.687e+00 8.616e-01 3.118 0.001925 ** nox -1.777e+01 3.820e+00 -4.651 4.25e-06 *** rm 3.810e+00 4.179e-01 9.116 < 2e-16 *** age 6.922e-04 1.321e-02 0.052 0.958229 dis -1.476e+00 1.995e-01 -7.398 6.01e-13 *** rad 3.060e-01 6.635e-02 4.613 5.07e-06 *** tax -1.233e-02 3.760e-03 -3.280 0.001112 ** ptratio -9.527e-01 1.308e-01 -7.283 1.31e-12 *** b 9.312e-03 2.686e-03 3.467 0.000573 *** lstat -5.248e-01 5.072e-02 -10.347 < 2e-16 ***

In $\mathbb{R}$ , the $\mathbf{lm}$ function can compute $\hat{\beta}$ , and the hccm function in the package car can compute $\hat{V}_{\mathrm{EHW}}$ as well as its variants. Below we compare the $t$ -statistics based on different choices of the standard errors. In this example, the EHW standard errors differ a lot for some regression coefficients.

> library("car")
> ols.fit.hc0 = sqrt(diag(hccm(ols.fit, type = "hc0)))
> ols.fit.hc1 = sqrt(diag(hccm(ols.fit, type = "hc1)))
> ols.fit.hc2 = sqrt(diag(hccm(ols.fit, type = "hc2)))
> ols.fit.hc3 = sqrt(diag(hccm(ols.fit, type = "hc3)))
> tvalues = summary(ols.fit)\\(coef [,1]/
+ cbind.summary(ols.fit)\\)coef [,2],
+ ols.fit.hc0,
+ ols.fit.hc1,
+ ols.fit.hc2,
+ ols.fit.hc3)

<table><tr><td colspan="6">&gt; colnames(tvalues) = c(&quot;ols&quot;, &quot;hc0&quot;, &quot;hc1&quot;, &quot;hc2&quot;, &quot;hc3&quot;)</td></tr><tr><td colspan="6">&gt; round(tvalues, 2)</td></tr><tr><td></td><td>ols</td><td>hc0</td><td>hc1</td><td>hc2</td><td>hc3</td></tr><tr><td>(Intercept)</td><td>7.14</td><td>4.62</td><td>4.56</td><td>4.48</td><td>4.33</td></tr><tr><td>crime</td><td>-3.29</td><td>-3.78</td><td>-3.73</td><td>-3.48</td><td>-3.17</td></tr><tr><td>zn</td><td>3.38</td><td>3.42</td><td>3.37</td><td>3.35</td><td>3.27</td></tr><tr><td>indus</td><td>0.33</td><td>0.41</td><td>0.41</td><td>0.41</td><td>0.40</td></tr><tr><td>chas1</td><td>3.12</td><td>2.11</td><td>2.08</td><td>2.05</td><td>2.00</td></tr><tr><td>nox</td><td>-4.65</td><td>-4.76</td><td>-4.69</td><td>-4.64</td><td>-4.53</td></tr><tr><td>rm</td><td>9.12</td><td>4.57</td><td>4.51</td><td>4.43</td><td>4.28</td></tr><tr><td>age</td><td>0.05</td><td>0.04</td><td>0.04</td><td>0.04</td><td>0.04</td></tr><tr><td>dis</td><td>-7.40</td><td>-6.97</td><td>-6.87</td><td>-6.81</td><td>-6.66</td></tr><tr><td>rad</td><td>4.61</td><td>5.05</td><td>4.98</td><td>4.91</td><td>4.76</td></tr><tr><td>tax</td><td>-3.28</td><td>-4.65</td><td>-4.58</td><td>-4.54</td><td>-4.43</td></tr><tr><td>p ratio</td><td>-7.28</td><td>-8.23</td><td>-8.11</td><td>-8.06</td><td>-7.89</td></tr><tr><td>b</td><td>3.47</td><td>3.53</td><td>3.48</td><td>3.44</td><td>3.34</td></tr><tr><td>lstat</td><td>-10.35</td><td>-5.34</td><td>-5.27</td><td>-5.18</td><td>-5.01</td></tr></table>

# B.5 Weighted least squares

Assuming that $(w_{i},x_{i},y_{i})\stackrel {\mathrm{IID}}{\sim}(w,x,y)$ with $w\neq 0$ . At the population level, we can define the weighted least squares (WLS) coefficient as

$$
\beta_ {w} = \arg \min  _ {b} E \{w (y - x ^ {\intercal} b) ^ {2} \},
$$

which satisfies

$$
E \{w x (y - x ^ {\top} \beta_ {w}) \} = 0
$$

and thus equals

$$
\beta_ {w} = \left\{E \left(w x x ^ {\mathsf {T}}\right) \right\} ^ {- 1} E (w x y)
$$

if $E(wxx^{\top})$ is invertible.

At the sample level, we can define the WLS coefficient as

$$
\hat {\beta} _ {w} = \arg \min  _ {b} \sum_ {i = 1} ^ {n} w _ {i} \left(y _ {i} - x _ {i} ^ {\top} b\right) ^ {2},
$$

which satisfies

$$
\sum_ {i = 1} ^ {n} w _ {i} x _ {i} \left(y _ {i} - x _ {i} ^ {\top} \hat {\beta} _ {w}\right) = 0
$$

and thus equals

$$
\hat {\beta} _ {w} = \left(n ^ {- 1} \sum_ {i = 1} ^ {n} w _ {i} x _ {i} x _ {i} ^ {\intercal}\right) ^ {- 1} \left(n ^ {- 1} \sum_ {i = 1} ^ {n} w _ {i} x _ {i} y _ {i}\right)
$$

if $\sum_{i=1}^{n} w_i x_i x_i^\top$ is invertible.

In R, we can specify weights in the lm function to implement WLS.

# B.6 Logistic regression

# B.6.1 Model

Technically, we can apply the OLS procedure even if the outcome $y$ is binary. However, it is a little awkward to have predicted probabilities outside the range of [0, 1]. This motivates us to consider the following model:

$$
\operatorname * {p r} (y _ {i} = 1 \mid x _ {i}) = g (x _ {i} ^ {\intercal} \beta),
$$

where $g(\cdot):\mathbb{R}\to [0,1]$ is a monotone function, and its inverse is often called the link function. The $g(\cdot)$ function can be any distribution function of a random variable, but we will focus on the logistic form:

$$
g (z) = \frac {e ^ {z}}{1 + e ^ {z}} = (1 + e ^ {- z}) ^ {- 1}.
$$

We can also write the logistic model as

$$
\Pr \left(y _ {i} = 1 \mid x _ {i}\right) = \frac {e ^ {x _ {i} ^ {\top} \beta}}{1 + e ^ {x _ {i} ^ {\top} \beta}},
$$

or, equivalently, with the definition $\operatorname{logit}(z) = \log \frac{z}{1 - z}$ , we have

$$
\operatorname {l o g i t} \left\{\operatorname * {p r} \left(y _ {i} = 1 \mid x _ {i}\right) \right\} = x _ {i} ^ {\mathsf {T}} \beta .
$$

Assume that $x_{i1}$ is binary. Under the logistic model, we have

$$
\begin{array}{l} \beta_ {1} = \operatorname {l o g i t} \left\{\operatorname {p r} \left(y _ {i} = 1 \mid x _ {i 1} = 1, \dots\right) \right\} - \operatorname {l o g i t} \left\{\operatorname {p r} \left(y _ {i} = 1 \mid x _ {i 1} = 0, \dots\right) \right\} \\ = \log \frac {\operatorname* {p r} (y _ {i} = 1 \mid x _ {i 1} = 1 , \ldots) / \operatorname* {p r} (y _ {i} = 0 \mid x _ {i 1} = 1 , \ldots)}{\operatorname* {p r} (y _ {i} = 1 \mid x _ {i 1} = 0 , \ldots) / \operatorname* {p r} (y _ {i} = 0 \mid x _ {i 1} = 0 , \ldots)}, \\ \end{array}
$$

where ... contains all other regressor $x_{i2}, \ldots, x_{ip}$ . Therefore, the coefficient $\beta_1$ equals the log of the odds ratio of $x_{i1}$ on $y_i$ conditional on other regressors.

# B.6.2 Maximum likelihood estimate

Let $\operatorname{pr}(y_i = 1 \mid x_i) = \pi(x_i, \beta)$ . To estimate the parameter $\beta$ , we can maximize the following likelihood function:

$$
\begin{array}{l} L (\beta) = \prod_ {i = 1} ^ {n} \left\{\pi \left(x _ {i}, \beta\right) \right\} ^ {y _ {i}} \left\{1 - \pi \left(x _ {i}, \beta\right) \right\} ^ {1 - y _ {i}} \\ = \prod_ {i = 1} ^ {n} \left\{\frac {\pi (x _ {i} , \beta)}{1 - \pi (x _ {i} , \beta)} \right\} ^ {y _ {i}} \{1 - \pi (x _ {i}, \beta) \} \\ = \prod_ {i = 1} ^ {n} \left(e ^ {x _ {i} ^ {\intercal} \beta}\right) ^ {y _ {i}} \frac {1}{1 + e ^ {x _ {i} ^ {\intercal} \beta}} \\ = \prod_ {i = 1} ^ {n} \frac {e ^ {y _ {i} x _ {i} ^ {\intercal} \beta}}{1 + e ^ {x _ {i} ^ {\intercal} \beta}}. \\ \end{array}
$$

Let $\hat{\beta}$ denote the maximizer, which is called the maximum likelihood estimate (MLE). Taking the log of $L(\beta)$ and differentiating it with respect to $\beta$ , we can show that the MLE must satisfy the first-order condition:

$$
\sum_ {i = 1} ^ {n} x _ {i} \{y _ {i} - \pi (x _ {i}, \hat {\beta}) \} = 0.
$$

If $x_{i}$ contains the intercept, the MLE must satisfy

$$
\sum_ {i = 1} ^ {n} \left\{y _ {i} - \pi \left(x _ {i}, \hat {\beta}\right) \right\} = 0,
$$

that is, the average of the observed $y_{i}$ 's must be identical to the average of the fitted probabilities $\pi (x_i,\hat{\beta})$ 's.

Using the general theory for the MLE, we can show that it is consistent for the true parameter $\beta$ and is asymptotically Normal:

$$
\sqrt {n} (\hat {\beta} - \beta) \rightarrow \mathrm {N} (0, V)
$$

in distribution, where $V = E[\pi(x_i, \beta) \{1 - \pi(x_i, \beta)\} xx^{\mathsf{T}}]$ . So we can approximate the covariance matrix of $\hat{\beta}$ by

$$
n ^ {- 1} \sum_ {i = 1} ^ {n} \pi (x _ {i}, \hat {\beta}) \{1 - \pi (x _ {i}, \hat {\beta}) \} x _ {i} x _ {i} ^ {\intercal}.
$$

In R, the glm function can find the MLE and report the estimated covariance matrix. We use the lalonde data to illustrate the logistic regression with the binary outcome indicating positive real earnings in 1978.

> library(Matching)

```txt
> data(lalonde)  
> logit.re78 = glm(I(re78 > 0) ~ ., family = binomial, + data = lalonde)  
> summary(logit.re78)  
Call: glm(formula = I(re78 > 0) ~ ., family = binomial, data = lalonde)  
Deviance Residuals:  
Min 1Q Median 3Q Max -2.1789 -1.3170 0.7568 0.9413 1.0882  
Coefficients: Estimate Std. Error z value Pr(>|z|) (Intercept) 1.910e+00 1.241e+00 1.539 0.1238 age -2.812e-03 1.533e-02 -0.183 0.8545 educ -2.179e-02 7.831e-02 -0.278 0.7808 black -1.060e+00 5.041e-01 -2.103 0.0354 * hisp 2.741e-01 6.967e-01 0.393 0.6940 married 7.577e-02 3.057e-01 0.248 0.8042 nodegr -1.984e-01 3.460e-01 -0.573 0.5664 re74 7.857e-06 3.173e-05 0.248 0.8044 re75 4.016e-05 6.058e-05 0.663 0.5074 u74 -6.177e-02 4.095e-01 -0.151 0.8801 u75 1.505e-02 3.518e-01 0.043 0.9659 treat 5.412e-01 2.222e-01 2.435 0.0149 * 
```

# B.6.3 Extension to the case-control study

In case-control studies, sampling is conditional on the binary outcome, that is, units with outcomes $y_{i} = 1$ and $y_{i} = 0$ are sampled with different probabilities. Let $s_i$ be the sampling indicator. In case-control studies, we have

$$
\Pr \left(s _ {i} = 1 \mid x _ {i}, y _ {i}\right) = \Pr \left(s _ {i} = 1 \mid y _ {i}\right)
$$

as a function of $y_{i}$ , and we only observe units with $s_i = 1$ .

Based on the model and the sampling mechanism of the case-control study, it does not seem obvious whether or not we can still use logistic regression to estimate the coefficients. Nevertheless, Prentice and Pyke (1979) proved a positive result. In case-control studies, logistic regression can still consistently estimate all the coefficients except for the intercept.

# B.6.4 Logistic regression with weights

Sometimes, unit $i$ has weight $w_{i}$ . Then we can fit a weighted logistic regression by solving

$$
\sum_ {i = 1} ^ {n} w _ {i} x _ {i} \{y _ {i} - \pi (x _ {i}, \hat {\beta}) \} = 0.
$$

In R, we can specify weights in the glm function to implement weighted logistic regression.

# B.7 Homework problems

# B.1 Sample WLS with the intercept

Assume the regressor $x_{i}$ contains the intercept. Show that

$$
\bar {y} _ {w} = \bar {x} _ {w} ^ {\mathsf {T}} \hat {\beta} _ {w} \tag {B.5}
$$

where $\bar{x}_w = \sum_{i=1}^n w_i x_i / \sum_{i=1}^n w_i$ and $\bar{y}_w = \sum_{i=1}^n w_i y_i / \sum_{i=1}^n w_i$ are the weighted averages of the $x_i$ 's and $y_i$ 's.

# B.2 Population OLS with a binary regressor

Assume $x$ is binary. Define the population OLS:

$$
(\alpha , \beta) = \arg \min  _ {(a, b)} E \{(y - a - b x) ^ {2} \}.
$$

Show that $\beta = E(y\mid x = 1) - E(y\mid x = 0)$ and $\alpha = E(y\mid x = 0)$ .

# B.3 Univariate WLS

As a special case of WLS, define

$$
(\hat {\alpha} _ {w}, \hat {\beta} _ {w}) = \arg \min  _ {(a, b)} \sum_ {i = 1} ^ {n} w _ {i} (y _ {i} - a - b x _ {i}) ^ {2}
$$

where $w_{i}\geq 0$ . Show that

$$
\hat {\beta} _ {w} = \frac {\sum_ {i = 1} ^ {n} w _ {i} \left(x _ {i} - \bar {x} _ {w}\right) \left(y _ {i} - \bar {y} _ {w}\right)}{\sum_ {i = 1} ^ {n} w _ {i} \left(x _ {i} - \bar {x} _ {w}\right) ^ {2}} \tag {B.6}
$$

and

$$
\hat {\alpha} _ {w} = \bar {y} _ {w} - \hat {\beta} _ {w} \bar {x} _ {w}, \tag {B.7}
$$

where $\bar{x}_w = \sum_{i=1}^{n} w_i x_i / \sum_{i=1}^{n} w_i$ and $\bar{y}_w = \sum_{i=1}^{n} w_i y_i / \sum_{i=1}^{n} w_i$ are the weighted averages of the $x_i$ 's and $y_i$ 's.

Further assume that the $x_{i}$ 's are binary. Show that

$$
\hat {\beta} _ {w} = \frac {\sum_ {i = 1} ^ {n} w _ {i} x _ {i} y _ {i}}{\sum_ {i = 1} ^ {n} w _ {i} x _ {i}} - \frac {\sum_ {i = 1} ^ {n} w _ {i} (1 - x _ {i}) y _ {i}}{\sum_ {i = 1} ^ {n} w _ {i} (1 - x _ {i})}. \tag {B.8}
$$

That is, if the regressor is binary in the univariate WLS, the coefficient of the regressor equals the difference in the weighted means.

Remark: To prove (B.8), use an appropriate reparametrization of the WLS problem. Otherwise, the derivation can be tedious.

# B.4 OLS with orthogonal regressors

Consider sample OLS fit of an $n$ -vector $Y$ on an $n \times p$ matrix $X$ , with coefficient $\hat{\beta}$ . Partition $X$ into $X = (X_{1}, X_{2})$ , where $X_{1}$ is an $n \times k$ matrix and $X_{2}$ is an $n \times l$ matrix, with $p = k + l$ . Correspondingly, partition $\hat{\beta}$ into

$$
\hat {\beta} = \left( \begin{array}{c} \hat {\beta} _ {1} \\ \hat {\beta} _ {2} \end{array} \right).
$$

Assume $X_{1}$ and $X_{2}$ are orthogonal, that is, $X_{1}^{\mathrm{T}}X_{2} = 0$ . Show that $\hat{\beta}_{1}$ equals the coefficient from OLS of $Y$ on $X_{1}$ and $\hat{\beta}_{2}$ equals the coefficient from OLS of $Y$ on $X_{2}$ , respectively.

# B.5 OLS with a non-degenerate transformation of the regressors

Define $\hat{\beta}$ as the coefficient from the sample OLS fit of an $n$ -vector $Y$ on an $n\times p$ matrix $X$ . Let $\Gamma$ be a $p\times p$ non-degenerate matrix, and define $X' = X\Gamma$ . Define $\hat{\beta}'$ as the coefficient from the sample OLS fit of $Y$ on $X'$ .

Show that

$$
\hat {\beta} = \Gamma \hat {\beta} ^ {\prime}.
$$

# B.6 Variances of the OLS estimator

Assume $(x_{i},y_{i})_{i = 1}^{n}\stackrel {\mathrm{IID}}{\sim}(x,y)$ and

$$
E (y \mid x) = x ^ {\intercal} \beta , \quad \operatorname {v a r} (y \mid x) = \sigma^ {2} (x).
$$

Show that the OLS estimator $\hat{\beta}$ has conditional mean

$$
E (\hat {\beta} \mid x _ {1}, \dots , x _ {n}) = \beta
$$

and conditional variance

$$
\operatorname {v a r} \left(\hat {\beta} \mid x _ {1}, \dots , x _ {n}\right) = \left(\sum_ {i = 1} ^ {n} x _ {i} x _ {i} ^ {\mathsf {T}}\right) ^ {- 1} \left(\sum_ {i = 1} ^ {n} \sigma^ {2} (x _ {i}) x _ {i} x _ {i} ^ {\mathsf {T}}\right) \left(\sum_ {i = 1} ^ {n} x _ {i} x _ {i} ^ {\mathsf {T}}\right) ^ {- 1}.
$$

Remark: This problem may provide some intuition for the variance estimators (B.3) and (B.4).

# C

# Some Useful Lemmas for Simple Random Sampling From a Finite Population

# C.1 Lemmas

Simple random sampling is a basic topic in standard survey sampling textbooks (e.g., Cochran, 1953). Below I review some results for simple random sampling that are useful for design-based inference in the CRE in Chapters 3 and 4. I define simple random sampling based on the distribution of the inclusion indicators.

Definition C.1 (simple random sampling) A simple random sample of size $n_1$ consists of a subset from a finite population of $n$ units indexed by $i = 1, \ldots, n$ . Let $Z = (Z_1, \ldots, Z_n)$ be the inclusion indicators of the $n$ units with $Z_i = 1$ if unit $i$ is sampled and $Z_i = 0$ otherwise. The vector $Z$ can take $\binom{n}{n_1}$ possible permutations of a vector of $n_1$ 1's and $n_0$ 0's, and each has equal probability.

By Definition C.1, simple random sampling is a special form of sampling without replacement because it does not allow for repeatedly sampling the same unit. Lemma C.1 below summarizes the first two moments of the inclusion indicators.

Lemma C.1 Under simple random sampling, we have

$$
E (Z _ {i}) = \frac {n _ {1}}{n}, \quad \mathrm {v a r} (Z _ {i}) = \frac {n _ {1} n _ {0}}{n ^ {2}}, \quad \mathrm {c o v} (Z _ {i}, Z _ {j}) = - \frac {n _ {1} n _ {0}}{n ^ {2} (n - 1)}.
$$

In more compact forms, we have

$$
E (\boldsymbol {Z}) = \frac {n _ {1}}{n} \mathbf {1} _ {n}, \quad \operatorname {c o v} (\boldsymbol {Z}) = \frac {n _ {1} n _ {0}}{n (n - 1)} \boldsymbol {P} _ {n},
$$

where $\mathbf{1}_n$ is a $n$ -dimensional vector of 1's, and $\pmb{P}_n = \pmb{I}_n - n^{-1}\mathbf{1}_n\mathbf{1}_n^\top$ is the $n \times n$ projection matrix orthogonal to $\mathbf{1}_n$ .

Let $\{c_1, \ldots, c_n\}$ be a finite population with mean $\bar{c} = \sum_{i=1}^{n} c_i / n$ and variance

$$
S _ {c} ^ {2} = (n - 1) ^ {- 1} \sum_ {i = 1} ^ {n} (c _ {i} - \bar {c}) ^ {2};
$$

let $\{d_1, \ldots, d_n\}$ be another finite population with mean $\bar{d} = \sum_{i=1}^{n} d_i / n$ and variance

$$
S _ {d} ^ {2} = (n - 1) ^ {- 1} \sum_ {i = 1} ^ {n} (d _ {i} - \bar {d}) ^ {2};
$$

their covariance is

$$
S _ {c d} = (n - 1) ^ {- 1} \sum_ {i = 1} ^ {n} (c _ {i} - \bar {c}) (d _ {i} - \bar {d}).
$$

Under simple random sampling, the sample means are

$$
\hat {\bar {c}} = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} c _ {i}, \quad \hat {\bar {d}} = n _ {1} ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} d _ {i};
$$

sample variances are

$$
\hat {S} _ {c} ^ {2} = (n _ {1} - 1) ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} (c _ {i} - \hat {\bar {c}}) ^ {2}, \quad \hat {S} _ {d} ^ {2} = (n _ {1} - 1) ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} (d _ {i} - \hat {\bar {d}}) ^ {2};
$$

the sample covariance is

$$
\hat {S} _ {c d} = (n _ {1} - 1) ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} (c _ {i} - \hat {\bar {c}}) (d _ {i} - \hat {\bar {d}}).
$$

Lemma C.2 below gives the moments of the sample means $\hat{\bar{c}}$ and $\hat{\bar{d}}$ .

Lemma C.2 Under simple random sampling, the sample means are unbiased for the population means:

$$
E (\hat {\bar {c}}) = \bar {c}, E (\hat {\bar {d}}) = \bar {d}.
$$

Theirvariancesandcovarianceare

$$
\operatorname {v a r} \left(\hat {\bar {c}}\right) = \frac {n _ {0}}{n n _ {1}} S _ {c} ^ {2}, \quad \operatorname {v a r} \left(\hat {\bar {d}}\right) = \frac {n _ {0}}{n n _ {1}} S _ {d} ^ {2}, \quad \operatorname {c o v} \left(\hat {\bar {c}}, \hat {\bar {d}}\right) = \frac {n _ {0}}{n n _ {1}} S _ {c d}.
$$

In the variance formulas in Lemma C.2, the coefficient $n_0 / (nn_1) = 1 / n_1 \times (1 - n_1 / n)$ in Lemma C.2 is different from $1 / n_1$ under IID sampling. The additional term $1 - n_1 / n = n_0 / n$ is called the finite population correction factor.

Lemma C.3 below gives the unbiasedness of the sample variances and covariance for estimating the population analogs.

Lemma C.3 Under simple random sampling, the sample variances and covariance are unbiased for their population versions:

$$
E (\hat {S} _ {c} ^ {2}) = S _ {c} ^ {2}, \quad E (\hat {S} _ {d} ^ {2}) = S _ {d} ^ {2}, \quad E (\hat {S} _ {c d}) = S _ {c d}.
$$

An important practical question is to make inference about $\bar{c}$ based on the simple random sample. This requires a more precise characterization of the distribution of its unbiased estimator $\hat{\bar{c}}$ . The finite-sample exact distribution of $\hat{\bar{c}}$ depends on the whole finite population $\{c_1, \ldots, c_n\}$ , which is unknown. The following finite population CLT characterizes the asymptotic distribution of $\hat{\bar{c}}$ based on its first two moments.

Lemma C.4 (finite population CLT) Under Under simple random sampling, as $n \to \infty$ , if

$$
\frac {\max _ {1 \leq i \leq n} (c _ {i} - \bar {c}) ^ {2}}{\min (n _ {1} , n _ {0}) S _ {c} ^ {2}} \to 0,
$$

then

$$
\frac {\hat {\overline {{c}}} - \bar {c}}{\sqrt {\frac {n _ {0}}{n n _ {1}} S _ {c} ^ {2}}} \to \mathrm {N} (0, 1)
$$

in distribution, and $\hat{S}_c^2 / S_c^2 \to 1$ in probability.

Lemma C.4 justifies the Wald-type $1 - \alpha$ confidence interval for $\bar{c}$ :

$$
\hat {\bar {c}} \pm z _ {1 - \alpha / 2} \sqrt {\frac {n _ {0}}{n n _ {1}} \hat {S} _ {c} ^ {2}}
$$

where $z_{1 - \alpha /2}$ is the $1 - \alpha /2$ upper quantile of the standard Normal random variable.

# C.2 Proofs

Proof of Lemma C.1: By symmetry, the $Z_{i}$ 's have the same mean, so

$$
n _ {1} = \sum_ {i = 1} ^ {n} Z _ {i} = E \left(\sum_ {i = 1} ^ {n} Z _ {i}\right) = n E (Z _ {i}) \Longrightarrow E (Z _ {i}) = n _ {1} / n.
$$

Because $Z_{i}$ is a Bernoulli random variable, its variance is

$$
\operatorname {v a r} \left(Z _ {i}\right) = \frac {n _ {1}}{n} \left(1 - \frac {n _ {1}}{n}\right) = \frac {n _ {1} n _ {0}}{n ^ {2}}.
$$

By symmetry again, the $Z_{i}$ 's have the same variance and the pairs $(Z_{i}, Z_{j})$ 's have the same covariance, so

$$
0 = \operatorname {v a r} \left(\sum_ {i = 1} ^ {n} Z _ {i}\right) = n \operatorname {v a r} (Z _ {i}) + n (n - 1) \operatorname {c o v} (Z _ {i}, Z _ {j})
$$

which implies that

$$
\operatorname {c o v} (Z _ {i}, Z _ {j}) = - \frac {n _ {1} n _ {0}}{n ^ {2} (n - 1)} \quad (i \neq j).
$$

Proof of Lemma C.2: The unbiasedness of the sample mean follows from linearity. For example,

$$
E (\hat {\bar {c}}) = E \left(\frac {1}{n _ {1}} \sum_ {i = 1} ^ {n} Z _ {i} c _ {i}\right) = \frac {1}{n _ {1}} \sum_ {i = 1} ^ {n} E (Z _ {i}) c _ {i} = \bar {c}.
$$

The covariance of the sample means is

$$
\begin{array}{l} \operatorname {c o v} (\hat {\hat {c}}, \hat {\hat {d}}) \\ = \operatorname {c o v} \left\{\frac {1}{n _ {1}} \sum_ {i = 1} ^ {n} Z _ {i} \left(c _ {i} - \bar {c}\right), \frac {1}{n _ {1}} \sum_ {i = 1} ^ {n} Z _ {\bar {i}} \left(d _ {i} - \bar {d}\right) \right\} \\ = \frac {1}{n _ {1} ^ {2}} \left[ \sum_ {i = 1} ^ {n} \operatorname {v a r} \left(Z _ {i}\right) \left(c _ {i} - \bar {c}\right) \left(d _ {i} - \bar {d}\right) + \sum_ {i \neq j} \operatorname {c o v} \left(Z _ {i}, Z _ {j}\right) \left(c _ {i} - \bar {c}\right) \left(d _ {j} - \bar {d}\right) \right] \\ { = } { \frac { 1 } { n _ { 1 } ^ { 2 } } \left[ \frac { n _ { 1 } n _ { 0 } } { n ^ { 2 } } \sum _ { i = 1 } ^ { n } ( c _ { i } - \bar { c } ) ( d _ { i } - \bar { d } ) - \frac { n _ { 1 } n _ { 0 } } { n ^ { 2 } ( n - 1 ) } \sum _ { i \neq j } ( c _ { i } - \bar { c } ) ( d _ { j } - \bar { d } ) \right] . } \\ \end{array}
$$

Because

$$
0 = \sum_ {i = 1} ^ {n} (c _ {i} - \bar {c}) \sum_ {i = 1} ^ {n} (d _ {i} - \bar {d}) = \sum_ {i = 1} ^ {n} (c _ {i} - \bar {c}) (d _ {i} - \bar {d}) + \sum_ {i \neq j} (c _ {i} - \bar {c}) (d _ {j} - \bar {d}),
$$

the covariance of the sample means reduces to

$$
\begin{array}{l} \operatorname {c o v} (\hat {\hat {c}}, \hat {\hat {d}}) \\ = \frac {1}{n _ {1} ^ {2}} \left[ \frac {n _ {1} n _ {0}}{n ^ {2}} \sum_ {i = 1} ^ {n} (c _ {i} - \bar {c}) (d _ {i} - \bar {d}) + \frac {n _ {1} n _ {0}}{n ^ {2} (n - 1)} \sum_ {i = 1} ^ {n} (c _ {i} - \bar {c}) (d _ {i} - \bar {d}) \right] \\ { = } { \frac { n _ { 0 } } { n n _ { 1 } } S _ { c d } . } \\ \end{array}
$$

The variance formulas are just special cases with $\hat{\bar{c}} = \hat{\bar{d}}$ .

Proof of Lemma C.3: We prove only the sample covariance term because the formulas for sample variances are special cases. We have the following

decomposition:

$$
\begin{array}{l} (n _ {1} - 1) \hat {S} _ {c d} = \sum_ {i = 1} ^ {n} Z _ {i} (c _ {i} - \hat {\bar {c}}) (d _ {i} - \hat {\bar {d}}) \\ = \sum_ {i = 1} ^ {n} Z _ {i} \left\{\left(c _ {i} - \bar {c}\right) - \left(\hat {\bar {c}} - \bar {c}\right) \right\} \left\{\left(d _ {i} - \bar {d}\right) - \left(\hat {\bar {d}} - \bar {d}\right) \right\} \\ = \sum_ {i = 1} ^ {n} Z _ {i} (c _ {i} - \bar {c}) (d _ {i} - \bar {d}) - n _ {1} (\hat {\bar {c}} - \bar {c}) (\hat {\bar {d}} - \bar {d}). \\ \end{array}
$$

Taking expectations on both sides, we have

$$
\begin{array}{l} E \left\{\left(n _ {1} - 1\right) \hat {S} _ {c d} \right\} = \sum_ {i = 1} ^ {n} E \left(Z _ {i}\right) \left(c _ {i} - \bar {c}\right) \left(d _ {i} - \bar {d}\right) - n _ {1} E \left\{\left(\hat {\bar {c}} - \bar {c}\right) \left(\hat {\bar {d}} - \bar {d}\right) \right\} \\ = \frac {n _ {1}}{n} \sum_ {i = 1} ^ {n} \left(c _ {i} - \bar {c}\right) \left(d _ {i} - \bar {d}\right) - n _ {1} \frac {n _ {0}}{n n _ {1}} S _ {c d} \\ = S _ {c d} \left\{\frac {n _ {1} (n - 1)}{n} - \frac {n _ {0}}{n} \right\} \\ = \quad (n _ {1} - 1) S _ {c d}, \\ \end{array}
$$

and the conclusion follows by dividing both sides by $n_1 - 1$ .

Proof of Lemma C.4: Hajek (1960) gave a proof of the CLT for simple random sampling, and Lehmann (1975) gave a more accessible version of the proof. Li and Ding (2017) modified the CLT as presented in Lemma C.4, and proved the consistency of the sample variance. Due to the technical complexities, I omit the proof. $\square$

# C.3 Comments on the literature

Survey sampling and experimental design have been deeply connected ever since Neyman (1934, 1935)'s seminal work. Li and Ding (2017) and Mukerjee et al. (2018) made many theoretical ties between these two areas.

# C.4 Homework Problems

# C.1 Sampling without replacement and the Hypergeometric distribution

Consider a special case of Lemma C.2 with $c_i$ 's being binary. Assume the total number of 1's equals $T$ so the total number of 0's equals $n - T$ . Let $t = \sum_{i=1}^{n} Z_i c_i$ denote the total number of 1's in the sample of size $n_1$ .

Find the distribution, mean, and variance of $t$ .

Remark: $t$ follows a Hypergeometric distribution.

# C.2 Vector form of Lemma C.2

Assume the $c_{i}$ 's are vectors and define

$$
S _ {c} ^ {2} = (n - 1) ^ {- 1} \sum_ {i = 1} ^ {n} (c _ {i} - \bar {c}) (c _ {i} - \bar {c}) ^ {\mathsf {T}}, \quad \hat {S} _ {c} ^ {2} = (n _ {1} - 1) ^ {- 1} \sum_ {i = 1} ^ {n} Z _ {i} (c _ {i} - \hat {\bar {c}}) (c _ {i} - \hat {\bar {c}}) ^ {\mathsf {T}}.
$$

Show that

$$
E (\hat {\bar {c}}) = \bar {c}, \quad \mathrm {c o v} (\hat {\bar {c}}) = \frac {n _ {0}}{n n _ {1}} S _ {c} ^ {2}, \quad E (\hat {S} _ {c} ^ {2}) = S _ {c} ^ {2}.
$$

# Bibliography

Abadie, A., Athey, S., Imbens, G. W., and Wooldridge, J. M. (2020). Sampling-based versus design-based uncertainty in regression analysis. *Econometrica*, 88:265-296.   
Abadie, A. and Imbens, G. W. (2006). Large sample properties of matching estimators for average treatment effects. *Econometrica*, 74:235-267.   
Abadie, A. and Imbens, G. W. (2008). On the failure of the bootstrap for matching estimators. *Econometrica*, 76:1537-1557.   
Abadie, A. and Imbens, G. W. (2011). Bias-corrected matching estimators for average treatment effects. Journal of Business and Economic Statistics, 29:1-11.   
Abadie, A. and Imbens, G. W. (2016). Matching on the estimated propensity score. *Econometrica*, 84:781-807.   
Alwin, D. F. and Hauser, R. M. (1975). The decomposition of effects in path analysis. American Sociological Review, 40:37-47.   
Amarante, V., Manacorda, M., Miguel, E., and Vigorito, A. (2016). Do cash transfers improve birth outcomes? evidence from matched vital statistics, program, and social security data. *American Economic Journal: Economic Policy*, 8:1-43.   
Anderson, T. W. and Rubin, H. (1950). The asymptotic properties of estimates of the parameters of a single equation in a complete system of stochastic equations. Annals of Mathematical Statistics, 21:570-582.   
Angrist, J., Lang, D., and Oreopoulos, P. (2009). Incentives and services for college achievement: Evidence from a randomized trial. *American Economic Journal: Applied Economics*, 1:136–163.   
Angrist, J. and Lavy, V. (2009). The effects of high stakes high school achievement awards: Evidence from a randomized trial. *American Economic Review*, 99:1384-1414.   
Angrist, J. D. (1990). Lifetime earnings and the Vietnam era draft lottery: evidence from social security administrative records. *American Economic Review*, 80:313-336.

Angrist, J. D. (1998). Estimating the labor market impact of voluntary military service using social security data on military applicants. *Econometrica*, 66:249-288.   
Angrist, J. D. (2022). Empirical strategies in economics: Illuminating the path from cause to effect. *Econometrica*, 90:2509-2539.   
Angrist, J. D. and Evans, W. N. (1998). Children and their parents' labor supply: Evidence from exogenous variation in family size. *American Economic Review*, 88:450-477.   
Angrist, J. D. and Imbens, G. W. (1995). Two-stage least squares estimation of average causal effects in models with variable treatment intensity. Journal of the American Statistical Association, 90:431-442.   
Angrist, J. D., Imbens, G. W., and Rubin, D. B. (1996). Identification of causal effects using instrumental variables (with discussion). Journal of the American Statistical Association, 91:444-455.   
Angrist, J. D. and Krueger, A. B. (1991). Does compulsory school attendance affect schooling and earnings? Quarterly Journal of Economics, 106:979-1014.   
Angrist, J. D. and Pischke, J.-S. (2008). Mostly Harmless Econometrics: An Empiricist's Companion. Princeton: Princeton University Press.   
Angrist, J. D. and Pischke, J.-S. (2014). Mastering'Metrics: The Path from Cause to Effect. Princeton: Princeton University Press.   
Aronow, P. M., Green, D. P., and Lee, D. K. K. (2014). Sharp bounds on the variance in randomized experiments. Annals of Statistics, 42:850-871.   
Asher, S. and Novosad, P. (2020). Rural roads and local economic development. *American Economic Review*, 110:797-823.   
Baker, S. G. and Lindeman, K. S. (1994). The paired availability design: a proposal for evaluating epidural analgesia during labor. *Statistics in Medicine*, 13:2269-2278.   
Balke, A. and Pearl, J. (1997). Bounds on treatment effects from studies with imperfect compliance. Journal of the American Statistical Association, 92:1171-1176.   
Ball, S., Bogatz, G., Rubin, D., and Beaton, A. (1973). Reading with television: An evaluation of the electric company. a report to the children's television workshop. volumes 1 and 2.   
Bang, H. and Robins, J. M. (2005). Doubly robust estimation in missing data and causal inference models. Biometrics, 61:962-973.

# C.4 Bibliography

Barnard, G. A. (1947). Significance tests for $2 \times 2$ tables. *Biometrika*, 34:123-138.   
Baron, R. M. and Kenny, D. A. (1986). The moderator-mediator variable distinction in social psychological research: Conceptual, strategic, and statistical considerations. Journal of Personality and Social Psychology, 51:1173-1182.   
Basmann, R. L. (1957). A generalized classical method of linear estimation of coefficients in a structural equation. *Econometrica*, 25:77-83.   
Bazzano, L. A., He, J., Muntner, P., Vupputuri, S., and Whelton, P. K. (2003). Relationship between cigarette smoking and novel risk factors for cardiovascular disease in the United States. Annals of Internal Medicine, 138:891-897.   
Berk, R., Pitkin, E., Brown, L., Buja, A., George, E., and Zhao, L. (2013). Covariance adjustments for the analysis of randomized field experiments. Evaluation Review, 37:170-196.   
Bertrand, M. and Mullainathan, S. (2004). Are Emily and Greg more employable than Lakisha and Jamal? A field experiment on labor market discrimination. *American Economic Review*, 94:991-1013.   
Bickel, P. J., Hammel, E. A., and O'Connell, J. W. (1975). Sex bias in graduate admissions: Data from Berkeley. Science, 187:398-404.   
Bickel, P. J., Klaassen, C. A. J., Ritov, Y., and Wellner, J. A. (1993). Efficient and Adaptive Estimation for Semiparametric Models. Baltimore: Johns Hopkins University Press.   
Bind, M.-A. C. and Rubin, D. B. (2020). When possible, report a fisher-exact p value and display its underlying null randomization distribution. Proceedings of the National Academy of Sciences of the United States of America, 117:19151-19158.   
Blackwell, M. (2013). A framework for dynamic causal inference in political science. American Journal of Political Science, 57:504-520.   
Bloniarz, A., Liu, H., Zhang, C. H., Sekhon, J., and Yu, B. (2016). Lasso adjustments of treatment effect estimates in randomized experiments. Proceedings of the National Academy of Sciences of the United States of America, 113:7383-7390.   
Bloom, H. S. (1984). Accounting for no-shows in experimental evaluation designs. Evaluation Review, 8:225-246.   
Bor, J., Moscoe, E., Mutevedzi, P., Newell, M.-L., and Bärnighausen, T. (2014). Regression discontinuity designs in epidemiology: causal inference without randomized trials. *Epidemiology*, 25:729.

Bowden, J., Davey Smith, G., and Burgess, S. (2015). Mendelian randomization with invalid instruments: effect estimation and bias detection through Egger regression. International Journal of Epidemiology, 44:512-525.   
Bowden, J., Spiller, W., Del Greco M, F., Sheehan, N., Thompson, J., Minelli, C., and Davey Smith, G. (2018). Improving the visualization, interpretation and analysis of two-sample summary data mendelian randomization via the radial plot and radial regression. International Journal of Epidemiology, 47:1264-1278.   
Box, G. E. P. (1979). Robustness in the strategy of scientific model building. In Launer, R. L. and Wilkinson, G. N., editors, *Robustness in Statistics*, pages 201-236. New York: Academic Press, Inc.   
Box, G. E. P., Hunter, W. H., and Hunter, S. (1978). Statistics for Experimenters: An Introduction to Design, Data Analysis, and Model Building. New York: John Wiley and Sons.   
Bradford Hill, A. (1965). The environment and disease: association or causation? Proceedings of the Royal Society of Medicine, 58:295-300.   
Bradford Hill, A. (2020). The environment and disease: association or causation? (with discussion). *Observational Studies*, 6:1-65.   
Bruhn, M. and McKenzie, D. (2009). In pursuit of balance: Randomization in practice in development field experiments. *American Economic Journal: Applied Economics*, 1:200-232.   
Brumback, B. A. (2022). Fundamentals of Causal Inference: With R. New York: Chapman & Hall.   
Butler, C. C. (1969). A test for symmetry using the sample distribution function. Annals of Mathematical Statistics, 40:2209-2210.   
Cao, W., Tsiatis, A. A., and Davidian, M. (2009). Improving efficiency and robustness of the doubly robust estimator for a population mean with incomplete data. Biometrika, 96:723-734.   
Card, D. (1993). Using geographic variation in college proximity to estimate the return to schooling. Technical report, National Bureau of Economic Research.   
Carpenter, C. and Dobkin, C. (2009). The effect of alcohol consumption on mortality: regression discontinuity evidence from the minimum drinking age. *American Economic Journal: Applied Economics*, 1:164-182.   
Cattaneo, M. D. (2010). Efficient semiparametric estimation of multi-valued treatment effects under ignorance. Journal of Econometrics, 155:138-154.

# C.4 Bibliography

Cattaneo, M. D., Frandsen, B. R., and Titiunik, R. (2015). Randomization inference in the regression discontinuity design: An application to party advantages in the US Senate. Journal of Causal Inference, 3:1-24.   
Chan, K. C. G., Yam, S. C. P., and Zhang, Z. (2016). Globally efficient nonparametric inference of average treatment effects by empirical balancing calibration weighting. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 78:673-700.   
Charig, C. R., Webb, D. R., Payne, S. R., and Wickham, J. E. (1986). Comparison of treatment of renal calculi by open surgery, percutaneous nephrolithotomy, and extracorporeal shockwave lithotripsy. *British Medical Journal*, 292:879-882.   
Chen, H., Geng, Z., and Jia, J. (2007). Criteria for surrogate end points. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 69:919-932.   
Cheng, J. and Small, D. S. (2006). Bounds on causal effects in three-arm trials with non-compliance. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 68:815-836.   
Chernozhukov, V., Chetverikov, D., Demirer, M., Duflo, E., Hansen, C., Newey, W., and Robins, J. (2018). Double/debiased machine learning for treatment and structural parameters. *Econometrics Journal*, 21:C1-C68.   
Chong, A., Cohen, I., Field, E., Nakasone, E., and Torero, M. (2016). Iron deficiency and schooling attainment in peru. *American Economic Journal: Applied Economics*, 8:222-55.   
Chung, E. and Romano, J. (2013). Exact and asymptotically robust permutation tests. Annals of Statistics, 41:484-507.   
Cochran, W. G. (1938). The omission or addition of an independent variate in multiple linear regression. Supplement to the Journal of the Royal Statistical Society, 5:171-176.   
Cochran, W. G. (1953). Sampling Techniques. New York: Wiley.   
Cochran, W. G. (1957). Analysis of covariance: its nature and uses. Biometrics, 13:261-281.   
Cochran, W. G. (1965). The planning of observational studies of human populations (with discussion). Journal of the Royal Statistical Society: Series A (General), 128:234-266.   
Cochran, W. G. (1968). The effectiveness of adjustment by subclassification in removing bias in observational studies. *Biometrics*, 24:295-313.

Cochran, W. G. (2015). Observational studies. *Observational Studies*, 1:126-136.   
Cochran, W. G. and Rubin, D. B. (1973). Controlling bias in observational studies: A review. *Sankhya*, 35:417-446.   
Cornfield, J., Haenszel, W., Hammond, E. C., Lilienfeld, A. M., Shimkin, M. B., and Wynder, E. L. (1959). Smoking and lung cancer: recent evidence and a discussion of some questions. Journal of the National Cancer Institute, 22:173-203.   
Cox, D. R. (1982). Randomization and concomitant variables in the design of experiments. In G. Kallianpur, P. R. K. and Ghosh, J. K., editors, Statistics and Probability: Essays in Honor of C. R. Rao, pages 197-202. North-Holland, Amsterdam.   
Cox, D. R. (2007). On a generalization of a result of W. G. Cochran. Biometrika, 94:755-759.   
Crump, R. K., Hotz, V. J., Imbens, G. W., and Mitnik, O. A. (2009). Dealing with limited overlap in estimation of average treatment effects. *Biometrika*, 96:187-199.   
Cunningham, S. (2021). Causal Inference: The Mixtape. New Haven: Yale University Press.   
Cuzick, J., Edwards, R., and Segnan, N. (1997). Adjusting for non-compliance and contamination in randomized clinical trials. *Statistics in Medicine*, 16:1017-1029.   
D'Amour, A., Ding, P., Feller, A., Lei, L., and Sekhon, J. (2021). Overlap in observational studies with high-dimensional covariates. Journal of Econometrics, 221:644-654.   
Dasgupta, T., Pillai, N. S., and Rubin, D. B. (2015). Causal inference from $2^{K}$ factorial designs by using potential outcomes. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 77:727-753.   
Davey Smith, G. and Ebrahim, S. (2003). "Mendelian randomization": can genetic epidemiology contribute to understanding environmental determinants of disease? International Journal of Epidemiology, 32:1-22.   
Davison, A. C. and Hinkley, D. V. (1997). Bootstrap Methods and Their Application. Cambridge: Cambridge University Press.   
Dawid, A. P. (1979). Conditional independence in statistical theory. Journal of the Royal Statistical Society: Series B (Methodological), 41:1-15.   
Dawid, A. P. (2000). Causal inference without counterfactuals (with discussion). Journal of the American Statistical Association, 95:407-424.

# C.4 Bibliography

Dehejia, R. H. and Wahba, S. (1999). Causal effects in nonexperimental studies: Reevaluating the evaluation of training programs. Journal of the American statistical Association, 94:1053-1062.   
Ding, P. (2016). A paradox from randomization-based causal inference (with discussion). Statistical Science, 32:331-345.   
Ding, P. (2021). The Frisch-Waugh-Lovell theorem for standard errors. Statistics and Probability Letters, 168:108945.   
Ding, P. and Dasgupta, T. (2016). A potential tale of two by two tables from completely randomized experiments. Journal of American Statistical Association, 111:157-168.   
Ding, P. and Dasgupta, T. (2017). A randomization-based perspective on analysis of variance: a test statistic robust to treatment effect heterogeneity. *Biometrika*, 105:45-56.   
Ding, P., Feller, A., and Miratrix, L. (2016). Randomization inference for treatment effect variation. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 78:655-671.   
Ding, P., Feller, A., and Miratrix, L. (2019). Decomposing treatment effect variation. Journal of the American Statistical Association, 114:304-317.   
Ding, P., Geng, Z., Yan, W., and Zhou, X.-H. (2011). Identifiability and estimation of causal effects by principal stratification with outcomes truncated by death. Journal of the American Statistical Association, 106:1578-1591.   
Ding, P. and Li, F. (2018). Causal inference: A missing data perspective. Statistical Science, 33:214-237.   
Ding, P., Li, X., and Miratrix, L. W. (2017a). Bridging finite and super population causal inference. Journal of Causal Inference, 5:20160027.   
Ding, P. and Lu, J. (2017). Principal stratification analysis using principal scores. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 79:757-777.   
Ding, P. and Miratrix, L. W. (2015). To adjust or not to adjust? Sensitivity analysis of M-bias and butterfly-bias. Journal of Causal Inference, 3:41-57.   
Ding, P. and VanderWeele, T. J. (2014). Generalized Cornfield conditions for the risk difference. *Biometrika*, 101:971-977.   
Ding, P. and VanderWeele, T. J. (2016). Sensitivity analysis without assumptions. *Epidemiology*, 27:368-377.   
Ding, P. and Vanderweele, T. J. (2016). Sharp sensitivity bounds for mediation under unmeasured mediator-outcome confounding. *Biometrika*, 103:483-490.

Ding, P., VanderWeele, T. J., and Robins, J. M. (2017b). Instrumental variables as bias amplifiers with general outcome and confounding. *Biometrika*, 104:291-302.   
Doll, R. and Hill, A. B. (1950). Smoking and carcinoma of the lung. *British Medical Journal*, 2:739.   
Dorn, H. F. (1953). Philosophy of inferences from retrospective studies. American Journal of Public Health and the Nations Health, 43:677-683.   
Durrett, R. (2019). *Probability: Theory and Examples*. Cambridge: Cambridge University Press.   
Efron, B. (1979). Bootstrap methods: Another look at the jackknife. The Annals of Statistics, 7:1-26.   
Efron, B. and Feldman, D. (1991). Compliance as an explanatory variable in clinical trials (with discussion). Journal of the American Statistical Association, 86:9-17.   
Eicker, F. (1967). Limit theorems for regressions with unequal and dependent errors. In Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability, volume 1, pages 59-82. Berkeley, CA: University of California Press.   
Fan, J. and Gijbels, I. (1996). Local Polynomial Modelling and Its Applications. New York: Chapman and Hall/CRC.   
Fieller, E. C. (1954). Some problems in interval estimation. Journal of the Royal Statistical Society: Series B (Methodological), 16:175-185.   
Firth, D. and Bennett, K. E. (1998). Robust models in probability sampling (with discussion). Journal of the Royal Statistical Society: Series B (Statistical Methodology), 60:3-21.   
Fisher, R. A. (1925). Statistical Methods for Research Workers. Edinburgh by Oliver and Boyd, 1st edition.   
Fisher, R. A. (1935). The Design of Experiments. Edinburgh, London: Oliver and Boyd, 1st edition.   
Fisher, R. A. (1957). Dangers of cigarette smoking [letter]. *British Medical Journal*, 2:297-298.   
Fogarty, C. B. (2018a). On mitigating the analytical limitations of finely stratified experiments. Journal of the Royal Statistical Society. Series B (Statistical Methodology), 80:1035-1056.   
Fogarty, C. B. (2018b). Regression assisted inference for the average treatment effect in paired experiments. *Biometrika*, 105:994–1000.

# C.4 Bibliography

Follmann, D. A. (2000). On the effect of treatment among would-be treatment compliers: An analysis of the multiple risk factor intervention trial. Journal of the American Statistical Association, 95:1101-1109.   
Forastiere, L., Mattei, A., and Ding, P. (2018). Principal ignorance in mediation analysis: through and beyond sequential ignorance. *Biometrika*, 105:979-986.   
Frangakis, C. E. and Rubin, D. B. (2002). Principal stratification in causal inference. Biometrics, 58:21-29.   
Freedman, D. A. (2008a). On regression adjustments in experiments with several treatments. Annals of Applied Statistics, 2:176-196.   
Freedman, D. A. (2008b). On regression adjustments to experimental data. Advances in Applied Mathematics, 40:180-193.   
Freedman, D. A. (2008c). Randomization does not justify logistic regression. *Statistical Science*, 23:237-249.   
Freedman, D. A. and Berk, R. A. (2008). Weighting regressions by propensity scores. *Evaluation Review*, 32:392-409.   
Frumento, P., Mealli, F., Pacini, B., and Rubin, D. B. (2012). Evaluating the effect of training on wages in the presence of noncompliance, nonemployment, and missing outcome data. Journal of the American Statistical Association, 107:450-466.   
Funk, M. J., Westreich, D., Wiesen, C., Stürmer, T., Brookhart, M. A., and Davidian, M. (2011). Doubly robust estimation of causal effects. *American Journal of Epidemiology*, 173:761-767.   
Gastwirth, J. L., KRIEGER, A. M., and ROSENBAUM, P. R. (1998). Cornfield's inequality. In Armitage, P. and Colton, T., editors, Encyclopedia of Biostatistics. New York: Wiley.   
Gerber, A. S. and Green, D. P. (2012). Field Experiments: Design, Analysis, and Interpretation. WW Norton.   
Gerber, A. S., Green, D. P., and Larimer, C. W. (2008). Social pressure and voter turnout: Evidence from a large-scale field experiment. *American Political Science Review*, 102:33-48.   
Gilbert, P. B. and Hudgens, M. G. (2008). Evaluating candidate principal surrogate endpoints. Biometrics, 64:1146-1154.   
Gould, A. L. (1998). Multi-centre trial analysis revisited. Statistics in Medicine, 17:1779-1797.   
Greevy, R., Lu, B., Silber, J. H., and Rosenbaum, P. (2004). Optimal multivariate matching before randomization. *Biostatistics*, 5:263-275.

Guo, K. and Basse, G. (2023). The generalized Oaxaca-Blinder estimator. Journal of American Statistical Association, 118:524-536.   
Guo, K. and Rothenhausler, D. (2022). On the statistical role of inexact matching in observational studies. *Biometrika*.   
Hahn, J. (1998). On the role of the propensity score in efficient semiparametric estimation of average treatment effects. *Econometrica*, 66:315-331.   
Hahn, J., Todd, P., and Van der Klaauw, W. (2001). Identification and estimation of treatment effects with a regression-discontinuity design. *Econometrica*, 69:201-209.   
Hahn, P. R., Murray, J. S., and Carvalho, C. M. (2020). Bayesian regression tree models for causal inference: regularization, confounding, and heterogeneous effects. *Bayesian Analysis*, 15:965–1056.   
Hainmueller, J. (2012). Entropy balancing for causal effects: A multivariate reweighting method to produce balanced samples in observational studies. *Political Analysis*, 20:25-46.   
Hajek, J. (1960). Limiting distributions in simple random sampling from a finite population. *Publications of the Mathematics Institute of the Hungarian Academy of Science*, 5:361-74.   
Hajek, J. (1971). Comment on "an essay on the logical foundations of survey sampling, part one". The foundations of survey sampling, 236.   
Hammond, E. C. and Horn, D. (1958). Smoking and death rates: report on forty four months of follow-up of 187,783 men. Journal of the American Medical Association, 166:1159-1172, 1294-1308.   
Hansen, L. P. (1982). Large sample properties of generalized method of moments estimators. *Econometrica*, 50:1029-1054.   
Hartley, H. O., Rao, J. N. K., and Kiefer, G. (1969). Variance estimation with one unit per stratum. Journal of the American Statistical Association, 64:841-851.   
Hausman, J. A. (1978). Specification tests in econometrics. *Econometrica*, 46:1251-1271.   
Hearst, N., Newman, T. B., and Hulley, S. B. (1986). Delayed effects of the military draft on mortality. New England Journal of Medicine, 314:620-624.   
Heckman, J. and Navarro-Lozano, S. (2004). Using matching, instrumental variables, and control functions to estimate economic choice models. Review of Economics and Statistics, 86:30-57.   
Heckman, J. J. (1979). Sample selection bias as a specification error. *Econometrica*, 47:153-161.

# C.4 Bibliography

Hennessy, J., Dasgupta, T., Miratrix, L., Pattanayak, C., and Sarkar, P. (2016). A conditional randomization test to account for covariate imbalance in randomized experiments. Journal of Causal Inference, 4:61-80.   
Hernán, M. Á., Brumback, B., and Robins, J. M. (2000). Marginal structural models to estimate the causal effect of zidovudine on the survival of HIV-positive men. *Epidemiology*, 11:561-570.   
Hernán, M. A. and Robins, J. M. (2020). Causal Inference: What If. Boca Raton: Chapman & Hall/CRC.   
Hill, J., Waldfogel, J., and Brooks-Gunn, J. (2002). Differential effects of high-quality child care. Journal of Policy Analysis and Management, 21:601-627.   
Hill, J. L. (2011). Bayesian nonparametric modeling for causal inference. Journal of Computational and Graphical Statistics, 20:217-240.   
Hirano, K. and Imbens, G. W. (2001). Estimation of causal effects using propensity score weighting: An application to data on right heart catheterization. *Health Services and Outcomes Research Methodology*, 2:259-278.   
Hirano, K., Imbens, G. W., Rubin, D. B., and Zhou, X. H. (2000). Assessing the effect of an influenza vaccine in an encouragement design. *Biostatistics*, 1:69-88.   
Ho, D. E., Imai, K., King, G., and Stuart, E. A. (2007). Matching as nonparametric preprocessing for reducing model dependence in parametric causal inference. *Political Analysis*, 15:199-236.   
Ho, D. E., Imai, K., King, G., and Stuart, E. A. (2011). Matchit: nonparametric preprocessing for parametric causal inference. Journal of Statistical Software, 42:1-28.   
Hodges, J. L. and Lehmann, E. L. (1962). Rank methods for combination of independent experiments in analysis of variance. Annals of Mathematical Statistics, 33:482-497.   
Holland, P. W. (1986). Statistics and causal inference (with discussion). Journal of the American Statistical Association, 81:945-960.   
Hong, G. and Raudenbush, S. W. (2008). Causal inference for time-varying instructional treatments. Journal of Educational and Behavioral Statistics, 33:333-362.   
Horvitz, D. G. and Thompson, D. J. (1952). A generalization of sampling without replacement from a finite universe. Journal of the American statistical Association, 47:663-685.   
Huber, M. (2023). Causal analysis: Impact evaluation and Causal Machine Learning with applications in $R$ . Cambridge: MIT Press.

Huber, P. J. (1967). The behavior of maximum likelihood estimates under nonstandard conditions. In Cam, L. M. L. and Neyman, J., editors, Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability, volume 1, pages 221-233. Berkeley, California: University of California Press.   
Hudgens, M. G. and Halloran, M. E. (2008). Toward causal inference with interference. Journal of the American Statistical Association, 103:832-842.   
Huntington-Klein, N. (2022). The effect: An introduction to research design and causality. New York: Chapman & Hall.   
Hyman, H. H. (1955). Survey Design and Analysis: Principles, Cases, and Procedures. Glencoe, IL: Free Press.   
Imai, K. (2008a). Sharp bounds on the causal effects in randomized experiments with "truncation-by-death". *Statistics and Probability Letters*, 78:144-149.   
Imai, K. (2008b). Variance identification and efficiency analysis in randomized experiments under the matched-pair design. *Statistics in Medicine*, 27:4857-4873.   
Imai, K., Keele, L., and Yamamoto, T. (2010). Identification, inference and sensitivity analysis for causal mediation effects. Statistical Science, 25:51-71.   
Imai, K. and Van Dyk, D. A. (2004). Causal inference with general treatment regimes: Generalizing the propensity score. Journal of the American Statistical Association, 99:854-866.   
Imbens, G. (2020). Potential outcome and directed acyclic graph approaches to causality: Relevance for empirical practice in economics. Journal of Economic Literature, 58:1129-1179.   
Imbens, G. W. (2003). Sensitivity to exogeneity assumptions in program evaluation. *American Economic Review*, 93:126-132.   
Imbens, G. W. (2004). Nonparametric estimation of average treatment effects under exogeneity: A review. Review of Economics and Statistics, 86:4-29.   
Imbens, G. W. (2014). Instrumental variables: An econometrician's perspective. Statistical Science, 29:323-358.   
Imbens, G. W. (2015). Matching methods in practice: Three examples. Journal of Human Resources, 50:373-419.   
Imbens, G. W. and Angrist, J. D. (1994). Identification and estimation of local average treatment effects. *Econometrica*, 62:467-475.

# C.4 Bibliography

Imbens, G. W. and Lemieux, T. (2008). Regression discontinuity designs: A guide to practice. Journal of Econometrics, 142:615-635.   
Imbens, G. W. and Manski, C. F. (2004). Confidence intervals for partially identified parameters. *Econometrica*, 72:1845-1857.   
Imbens, G. W. and Rubin, D. B. (1997). Estimating outcome distributions for compliers in instrumental variables models. Review of Economic Studies, 64:555-574.   
Imbens, G. W. and Rubin, D. B. (2015). Causal Inference for Statistics, Social, and Biomedical Sciences: An Introduction. Cambridge: Cambridge University Press.   
Investigators, I. T. et al. (2014). Endovascular or open repair strategy for ruptured abdominal aortic aneurysm: 30 day outcomes from improve randomised trial. *British Medical Journal*, 348:f7661.   
Ioannidis, J. P. A., Tan, Y. J., and Blum, M. R. (2019). Limitations and misinterpretations of E-values for sensitivity analyses of observational studies. Annals of Internal Medicine, 170:108-111.   
Jackson, L. A., Jackson, M. L., Nelson, J. C., Neuzil, K. M., and Weiss, N. S. (2006). Evidence of bias in estimates of influenza vaccine effectiveness in seniors. International Journal of Epidemiology, 35:337-344.   
Janssen, A. (1997). Studentized permutation tests for non-iid hypotheses and the generalized Behrens-Fisher problem. Statistics and Probability Letters, 36:9-21.   
Jiang, Z. and Ding, P. (2020). Measurement errors in the binary instrumental variable model. Biometrika, 107:238-245.   
Jiang, Z. and Ding, P. (2021). Identification of causal effects within principal strata using auxiliary variables. Statistical Science, 36:493-508.   
Jiang, Z., Ding, P., and Geng, Z. (2016). Principal causal effect identification and surrogate end point evaluation by multiple trials. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 78:829-848.   
Jiang, Z., Yang, S., and Ding, P. (2022). Multiply robust estimation of causal effects under principal ignorability. Journal of the Royal Statistical Society - Series B (Statistical Methodology), 84:1423-1445.   
Jin, H. and Rubin, D. B. (2008). Principal stratification for causal inference with extended partial compliance. Journal of the American Statistical Association, 103:101-111.   
Jo, B. and Stuart, E. A. (2009). On the use of propensity scores in principal causal effect estimation. *Statistics in Medicine*, 28:2857-2875.

Jo, B., Stuart, E. A., MacKinnon, D. P., and Vinokur, A. D. (2011). The use of propensity scores in mediation analysis. Multivariate Behavioral Research, 46:425-452.   
Judd, C. M. and Kenny, D. A. (1981). Process analysis estimating mediation in treatment evaluations. *Evaluation Review*, 5:602-619.   
Kang, J. D. Y. and Schafer, J. L. (2007). Demystifying double robustness: A comparison of alternative strategies for estimating a population mean from incomplete data. Statistical Science, 22:523-539.   
Katan, M. B. (1986). Apoupoprotein E isoforms, serum cholesterol, and cancer. Lancet, 327:507-508.   
King, G. and Zeng, L. (2006). The dangers of extreme counterfactuals. Political Analysis, 14:131-159.   
Kitagawa, T. (2015). A test for instrument validity. *Econometrica*, 83:2043-2063.   
Koenker, R. and Xiao, Z. (2002). Inference on the quantile regression process. *Econometrica*, 70:1583-1612.   
Künzel, S. R., Sekhon, J. S., Bickel, P. J., and Yu, B. (2019). Metaleaders for estimating heterogeneous treatment effects using machine learning. Proceedings of the National Academy of Sciences of the United States of America, 116:4156-4165.   
Kurth, T., Walker, A. M., Glynn, R. J., Chan, K. A., Gaziano, J. M., Berger, K., and Robins, J. M. (2005). Results of multivariable logistic regression, propensity matching, propensity adjustment, and propensity-based weighting under conditions of nonuniform effect. *American Journal of Epidemiology*, 163:262-270.   
LaLonde, R. J. (1986). Evaluating the econometric evaluations of training programs with experimental data. *American Economic Review*, 76:604-620.   
Leamer, E. (1978). Specification Searches: Ad Hoc Inference with Nonexperimental Data. John Wiley and Sons.   
Lee, D. S. (2008). Randomized experiments from non-random selection in US House elections. Journal of Econometrics, 142:675-697.   
Lee, D. S. (2009). Training, wages, and sample selection: Estimating sharp bounds on treatment effects. Review of Economic Studies, 76:1071-1102.   
Lee, D. S. and Lemieux, T. (2010). Regression discontinuity designs in economics. Journal of Economic Literature, 48:281-355.   
Lee, M.-J. (2018). Simple least squares estimator for treatment effects using propensity score residuals. *Biometrika*, 105:149-164.

# C.4 Bibliography

Lee, W.-C. (2011). Bounding the bias of unmeasured factors with confounding and effect-modifying potentials. *Statistics in Medicine*, 30:1007-1017.   
Lehmann, E. L. (1975). Nonparametrics: Statistical Methods Based on Ranks. California: Holden-Day, Inc.   
Lei, L. and Ding, P. (2021). Regression adjustment in completely randomized experiments with a diverging number of covariates. *Biometrika*, 108:815-828.   
Lewis, D. (1973). Causation. Journal of Philosophy, 70:556-567.   
Li, F., Ding, P., and Mealli, F. (2023). Bayesian causal inference: a critical review. *Philosophical Transactions of the Royal Society A*, 381:20220153.   
Li, F., Mattei, A., and Mealli, F. (2015). Evaluating the causal effect of university grants on student dropout: evidence from a regression discontinuity design using principal stratification. Annals of Applied Statistics, 9:1906-1931.   
Li, F., Morgan, K. L., and Zaslavsky, A. M. (2018a). Balancing covariates via propensity score weighting. Journal of the American Statistical Association, 113:390-400.   
Li, F., Thomas, L. E., and Li, F. (2019). Addressing extreme propensity scores via the overlap weights. *American Journal of Epidemiology*, 188:250-257.   
Li, X. and Ding, P. (2016). Exact confidence intervals for the average causal effect on a binary outcome. *Statistics in Medicine*, 35:957-960.   
Li, X. and Ding, P. (2017). General forms of finite population central limit theorems with applications to causal inference. Journal of the American Statistical Association, 112:1759-1769.   
Li, X. and Ding, P. (2020). *Rerandomization and regression adjustment*. Journal of the Royal Statistical Society, Series B (Statistical Methodology), 82:241-268.   
Li, X., Ding, P., and Rubin, D. B. (2018b). Asymptotic theory of rerandomization in treatment-control experiments. Proceedings of the National Academy of Sciences of the United States of America, 115:9157-9162.   
Lin, W. (2013). Agnostic notes on regression adjustments to experimental data: Reexamining Freedman's critique. Annals of Applied Statistics, 7:295-318.   
Lin, Z., Ding, P., and Han, F. (2023). Estimation based on nearest neighbor matching: from density ratio to average treatment effect. *Econometrica*.

Lind, J. (1753). A treatise of the scurvy. Three Parts. Containing an Inquiry into the Nature, Causes and Cure, of that Disease. Together with a Critical and Chronological View of what has been Published on the Subject.   
Lipsitch, M., Tchetgen Tchetgen, E., and Cohen, T. (2010). Negative controls: a tool for detecting confounding and bias in observational studies. *Epidemiology*, 21:383-388.   
Little, R. and An, H. (2004). Robust likelihood-based analysis of multivariate data with missing values. Statistica Sinica, 14:949-968.   
Liu, H. and Yang, Y. (2020). Regression-adjusted average treatment effect estimates in stratified randomized experiments. *Biometrika*, 107:935-948.   
Long, J. S. and Ervin, L. H. (2000). Using heteroscedasticity consistent standard errors in the linear regression model. American Statistician, 54:217-224.   
Lu, S. and Ding, P. (2023). Flexible sensitivity analysis for causal inference in observational studies subject to unmeasured confounding. https://arxiv.org/abs/2305.17643.   
Lumley, T., Shaw, P. A., and Dai, J. Y. (2011). Connections between survey calibration estimators and semiparametric models for incomplete data. International Statistical Review, 79:200-220.   
Lunceford, J. K. and Davidian, M. (2004). Stratification and weighting via the propensity score in estimation of causal treatment effects: a comparative study. Statistics in Medicine, 23:2937-2960.   
Luo, X., Dasgupta, T., Xie, M., and Liu, R. Y. (2021). Leveraging the fisher randomization test using confidence distributions: Inference, combination and fusion learning. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 83:777-797.   
Manski, C. F. (1990). Nonparametric bounds on treatment effects. *American Economic Review*, 2:319-323.   
Manski, C. F. (2003). *Partial Identification of Probability Distributions*. New York: Springer.   
Mattei, A., Li, F., and Mealli, F. (2013). Exploiting multiple outcomes in bayesian principal stratification analysis with application to the evaluation of a job training program. Annals of Applied Statistics, 7:2336-2360.   
McCrary, J. (2008). Manipulation of the running variable in the regression discontinuity design: A density test. Journal of Econometrics, 142:698-714.   
McDonald, C. J., Hui, S. L., and Tierney, W. M. (1992). Effects of computer reminders for influenza vaccination on morbidity during influenza epidemics. MD Computing: Computers in Medical Practice, 9:304-312.

# C.4 Bibliography

McGrath, S., Young, J. G., and Hernán, M. A. (2021). Revisiting the g-null paradox. *Epidemiology*, 33:114-120.   
Mealli, F. and Pacini, B. (2013). Using secondary outcomes to sharpen inference in randomized experiments with noncompliance. Journal of the American Statistical Association, 108:1120-1131.   
Meinert, C. L., Knatterud, G. L., Prout, T. E., and Klimt, C. R. (1970). A study of the effects of hypoglycemic agents on vascular complications in patients with adult-onset diabetes. ii. mortality results. Diabetes, 19:Suppl-789.   
Mercatanti, A. and Li, F. (2014). Do debit cards increase household spending? evidence from a semiparametric causal analysis of a survey. Annals of Applied Statistics, 8:2485-2508.   
Ming, K. and Rosenbaum, P. R. (2000). Substantial gains in bias reduction from matching with a variable number of controls. *Biometrics*, 56:118-124.   
Ming, K. and Rosenbaum, P. R. (2001). A note on optimal matching with variable controls using the assignment algorithm. Journal of Computational and Graphical Statistics, 10:455-463.   
Miratrix, L. W., Sekhon, J. S., Theodoridis, A. G., and Campos, L. F. (2018). Worth weighting? how to think about and use weights in survey experiments. *Political Analysis*, 26:275-291.   
Miratrix, L. W., Sekhon, J. S., and Yu, B. (2013). Adjusting treatment effect estimates by post-stratification in randomized experiments. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 75:369-396.   
Morgan, K. L. and Rubin, D. B. (2012). Rerandomization to improve covariate balance in experiments. Annals of Statistics, 40:1263-1282.   
Morgan, S. L. and Winship, C. (2015). Counterfactuals and Causal Inference. Cambridge: Cambridge University Press.   
Mukerjee, R., Dasgupta, T., and Rubin, D. B. (2018). Using standard tools from finite population sampling to improve causal inference for complex experiments. Journal of the American Statistical Association, 113:868-881.   
Naimi, A. I., Cole, S. R., and Kennedy, E. H. (2017). An introduction to g methods. International Journal of Epidemiology, 46:756-762.   
Negi, A. and Wooldridge, J. M. (2021). Revisiting regression adjustment in experiments with heterogeneous treatment effects. *Econometric Reviews*, 40:504-534.   
Neyman, J. (1923). On the application of probability theory to agricultural experiments. essay on principles (with discussion). section 9 (translated). reprinted ed. Statistical Science, 5:465-472.

Neyman, J. (1934). On the two different aspects of the representative method: the method of stratified sampling and the method of purposive selection (with discussion). Journal of the Royal Statistical Society, 97:558-625.   
Neyman, J. (1935). Statistical problems in agricultural experimentation (with discussion). Supplement to the Journal of the Royal Statistical Society, 2:107-180.   
Nguyen, T. Q., Schmid, I., Ogburn, E. L., and Stuart, E. A. (2021). Clarifying causal mediation analysis for the applied researcher: Effect identification via three assumptions and five potential outcomes. *Psychological Methods*, 26:255-271.   
Otsu, T. and Rai, Y. (2017). Bootstrap inference of matching estimators for average treatment effects. Journal of the American Statistical Association, 112:1720-1732.   
Pearl, J. (1995). Causal diagrams for empirical research (with discussion). Biometrika, 82:669-688.   
Pearl, J. (2000). Causality: Models, Reasoning and Inference. Cambridge: Cambridge University Press.   
Pearl, J. (2001). Direct and indirect effects. In Breese, J. S. and Koller, D., editors, Proceedings of the 17th Conference on Uncertainty in Artificial Intelligence, pages 411-420. pp. 411-420. San Francisco: Morgan Kaufmann Publishers Inc.   
Pearl, J. (2010a). On a class of bias-amplifying variables that endanger effect estimates. In Grunwald, P. and Spirtes, P., editors, Proceedings of the Twenty-Sixth Conference on Uncertainty in Artificial Intelligence (UAI 2010), Corvallis, OR: 425-432. Association for Uncertainty in Artificial Intelligence.   
Pearl, J. (2010b). On the consistency rule in causal inference: axiom, definition, assumption, or theorem? Epidemiology, 21:872-875.   
Pearl, J. (2011). Invited commentary: Understanding bias amplification. American Journal of Epidemiology, 174:1223-1227.   
Pearl, J. (2018). Does obesity shorten life? Or is it the soda? On non-manipulable causes. Journal of Causal Inference, 6:20182001.   
Pearl, J. and Baireinboim, E. (2014). External validity: From do-calculus to transportability across populations. Statistical Science, 29:579-595.   
Pearl, J. and Mackenzie, D. (2018). The Book of Why: The New Science of Cause and Effect. Basic Books.

# C.4 Bibliography

Permutt, T. and Hebel, J. R. (1989). Simultaneous-equation estimation in a clinical trial of the effect of smoking on birth weight. *Biometrics*, 45:619-622.   
Phipson, B. and Smyth, G. K. (2010). Permutation p-values should never be zero: calculating exact p-values when permutations are randomly drawn. Statistical Applications in Genetics and Molecular Biology, 9:Article39.   
Pimentel, S. D., Yoon, F., and Keele, L. (2015). Variable-ratio matching with fine balance in a study of the Peer Health Exchange. *Statistics in Medicine*, 34:4070-4082.   
Poole, C. (2010). On the origin of risk relativism. *Epidemiology*, 21:3-9.   
Popper, K. (1963). Conjectures and Refutations: The Growth of Scientific Knowledge. Routledge.   
Powers, D. E. and Swinton, S. S. (1984). Effects of self-study for coachable test item types. Journal of Educational Psychology, 76:266-278.   
Prentice, R. L. and Pyke, R. (1979). Logistic disease incidence models and case-control studies. Biometrika, 66:403-411.   
Rao, C. R. (1970). Estimation of heteroscedastic variances in linear models. Journal of the American Statistical Association, 65:161-172.   
Reichenbach, H. (1957). The Direction of Time. University of California Press.   
Rigdon, J. and Hudgens, M. G. (2015). Randomization inference for treatment effects on a binary outcome. *Statistics in Medicine*, 34:924-935.   
Robins, J., Sued, M., Lei-Gomez, Q., and Rotnitzky, A. (2007). Comment: Performance of double-robust estimators when inverse probability weights are highly variable. Statistical Science, 22:544-559.   
Robins, J. M. (1999). Association, causation, and marginal structural models. Synthese, 121:151-179.   
Robins, J. M. and Greenland, S. (1992). Identifiability and exchangeability for direct and indirect effects. *Epidemiology*, 3:143-155.   
Robins, J. M., Hernan, M. A., and Brumback, B. (2000). Marginal structural models and causal inference in epidemiology. *Epidemiology*, 11:550-560.   
Robins, J. M., Mark, S. D., and Newey, W. K. (1992). Estimating exposure effects by modelling the expectation of exposure conditional on confounders. *Biometrics*, 48:479-495.   
Robins, J. M. and Wasserman, L. A. (1997). Estimation of effects of sequential treatments by reparameterizing directed acyclic graphs. In Proceedings of the Thirteenth conference on Uncertainty in artificial intelligence, volume 409-420.

Rosenbaum, P. R. (1984). The consequences of adjustment for a concomitant variable that has been affected by the treatment. Journal of the Royal Statistical Society. Series A, 147:656-666.   
Rosenbaum, P. R. (1987a). Model-based direct adjustment. Journal of the American Statistical Association, 82:387-394.   
Rosenbaum, P. R. (1987b). Sensitivity analysis for certain permutation inferences in matched observational studies. *Biometrika*, 74:13-26.   
Rosenbaum, P. R. (1989). The role of known effects in observational studies. *Biometrics*, 45:557-569.   
Rosenbaum, P. R. (2002a). Covariance adjustment in randomized experiments and observational studies (with discussion). *Statistical Science*, 17:286-327.   
Rosenbaum, P. R. (2002b). Observational Studies. Springer, 2nd edition.   
Rosenbaum, P. R. (2010). Design of Observational Studies. New York: Springer.   
Rosenbaum, P. R. (2015). Two R packages for sensitivity analysis in observational studies. *Observational Studies*, 1:1-17.   
Rosenbaum, P. R. (2018). Sensitivity analysis for stratified comparisons in an observational study of the effect of smoking on homocysteine levels. Annals of Applied Statistics, 12:2312-2334.   
Rosenbaum, P. R. (2020). Modern algorithms for matching in observational studies. Annual Review of Statistics and Its Application, 7:143-176.   
Rosenbaum, P. R. and Rubin, D. B. (1983a). Assessing sensitivity to an unobserved binary covariate in an observational study with binary outcome. Journal of the Royal Statistical Society - Series B (Statistical Methodology), 45:212-218.   
Rosenbaum, P. R. and Rubin, D. B. (1983b). The central role of the propensity score in observational studies for causal effects. *Biometrika*, 70:41-55.   
Rosenbaum, P. R. and Rubin, D. B. (1984). Reducing bias in observational studies using subclassification on the propensity score. Journal of the American statistical Association, 79:516-524.   
Rosenbaum, P. R. and Rubin, D. B. (2023). Propensity scores in the design of observational studies for causal effects. Biometrika, 110:1-13.   
Rothman, K. J., Greenland, S., Lash, T. L., et al. (2008). Modern epidemiology, volume 3. Wolters Kluwer Health/Lippincott Williams & Wilkins Philadelphia.

# C.4 Bibliography

Rubin, D. B. (1974). Estimating causal effects of treatments in randomized and nonrandomized studies. Journal of Educational Psychology, 66:688-701.   
Rubin, D. B. (1975). Bayesian inference for causality: The importance of randomization. In *The Proceedings of the social statistics section of the American Statistical Association*, volume 233, page 239. American Statistical Association Alexandria, VA.   
Rubin, D. B. (1978). Bayesian inference for causal effects: The role of randomization. Annals of Statistics, 6:34-58.   
Rubin, D. B. (1980). Comment on "Randomization analysis of experimental data: the Fisher randomization test" by D. Basu. Journal of American Statistical Association, 75:591-593.   
Rubin, D. B. (2001). Comment: Self-experimentation for causal effects. _CHANCE_, 14:16-17.   
Rubin, D. B. (2005). Causal inference using potential outcomes: Degisn, modeling, decisions. Journal of American Statistical Association, 100:322-331.   
Rubin, D. B. (2006a). Causal inference through potential outcomes and principal stratification: application to studies with "censoring" due to death (with discussion). *Statistical Science*, 21:299-309.   
Rubin, D. B. (2006b). Matched Sampling for Causal Effects. Cambridge: Cambridge University Press.   
Rubin, D. B. (2007). The design versus the analysis of observational studies for causal effects: parallels with the design of randomized trials. *Statistics in Medicine*, 26:20-36.   
Rubin, D. B. (2008). For objective causal inference, design trumps analysis. Annals of Applied Statistics, 2:808-840.   
Rudolph, K. E., Goin, D. E., Paksarian, D., Crowder, R., Merikangas, K. R., and Stuart, E. A. (2018). Causal mediation analysis with observational data: considerations and illustration examining mechanisms linking neighborhood poverty to adolescent substance use. *American Journal of Epidemiology*, 188:598-608.   
Sabbaghi, A. and Rubin, D. B. (2014). Comments on the Neyman-Fisher controversy and its consequences. Statistical Science, 29:267-284.   
Salsburg, D. (2001). The Lady Tasting Tea: How Statistics Revolutionized Science in the Twentieth Century. Henry Holt and Company.   
Sanders, E. Gustafson, P. and Karim, M. E. (2021). Incorporating partial adherence into the principal stratification analysis framework. *Statistics in Medicine*, 40:3625-3644.

Sanderson, E., Macdonald-Wallis, C., and Davey Smith, G. (2017). Negative control exposure studies in the presence of measurement error: implications for attempted effect estimate calibration. International Journal of Epidemiology, 47:587-596.   
Scharfstein, D. O., Rotnitzky, A., and Robins, J. M. (1999). Adjusting for nonignorable drop-out using semiparametric nonresponse models. Journal of the American Statistical Association, 94:1096-1120.   
Schlesselman, J. J. (1978). Assessing effects of confounding variables. American Journal of Epidemiology, 108:3-8.   
Schochet, P. Z., Burghardt, J., and McConnell, S. (2008). Does job corps work? impact findings from the national job corps study. American Economic Review, 98:1864-1886.   
Sekhon, J. S. (2009). Opiates for the matches: Matching methods for causal inference. Annual Review of Political Science, 12:487-508.   
Sekhon, J. S. (2011). Multivariate and propensity score matching software with automated balance optimization: The matching package for R. Journal of Statistical Software, 47:1-52.   
Sekhon, J. S. and Titiunik, R. (2017). On interpreting the regression discontinuity design as a local experiment. In Regression Discontinuity Designs, volume 38. Emerald Publishing Limited.   
Shinozaki, T. and Matsuyama, Y. (2015). Doubly robust estimation of standardized risk difference and ratio in the exposed population. *Epidemiology*, 26:873-877.   
Small, D. S. (2015). Introduction to Observational Studies and the Reprint of Cochran's paper "Observational Studies" and Comments. *Observational Studies*, 1:124-125.   
Sobel, M. E. (1982). Asymptotic confidence intervals for indirect effects in structural equation models. Sociological Methodology, 13:290-312.   
Sobel, M. E. (1986). Some new results on indirect effects and their standard errors in covariance structure models. *Sociological Methodology*, 16:159-186.   
Sommer, A. and Zeger, S. L. (1991). On estimating efficacy from clinical trials. Statistics in Medicine, 10:45-52.   
Stuart, E. A. (2010). Matching methods for causal inference: A review and a look forward. Statistical Science, 25:1-21.   
Stuart, E. A. and Jo, B. (2015). Assessing the sensitivity of methods for estimating principal causal effects. Statistical Methods in Medical Research, 24:657-674.

# C.4 Bibliography

Su, F., Mou, W., Ding, P., and Wainwright, M. (2023). When is the estimated propensity score better? High-dimensional analysis and bias correction. arXiv preprint arXiv:2303.17102.   
Tao, Y. and Fu, H. (2019). Doubly robust estimation of the weighted average treatment effect for a target population. *Statistics in Medicine*, 38:315-325.   
Theil, H. (1953). Estimation and simultaneous correlation in complete equation systems. central planning bureau. Technical report, Mimeo, The Hague.   
Thistlethwaite, D. L. and Campbell, D. T. (1960). Regression-discontinuity analysis: An alternative to the ex post facto experiment. Journal of Educational Psychology, 51:309.   
Thistlewaite, D. L. and Campbell, D. T. (2016). Regression-discontinuity analysis: An alternative to the ex-post facto experiment (with discussion). *Observational Studies*, 2:119–209.   
Tibshirani, R. (1996). Regression shrinkage and selection via the lasso. Journal of the Royal Statistical Society: Series B (Methodological), 58:267-288.   
Titterington, D. (2013). Biometrika highlights from volume 28 onwards. Biometrika, 100:17-73.   
Valeri, L. and Vanderweele, T. J. (2014). The estimation of direct and indirect causal effects in the presence of misclassified binary mediator. *Biostatistics*, 15:498-512.   
Van der Laan, M. J. and Rose, S. (2011). Targeted Learning: Causal Inference for Observational and Experimental Data. New York: Springer.   
Van der Vaart, A. W. (2000). Asymptotic Statistics. Cambridge: Cambridge University Press.   
Van Elteren, P. (1960). On the combination of independent two-sample tests of wilcoxon. Bulletin of the Institute of International Statistics, 37:351-361.   
VanderWeele, T. J. (2008). Simple relations between principal stratification and direct and indirect effects. *Statistics and Probability Letters*, 78:2957-2962.   
VanderWeele, T. J. (2015). Explanation in Causal Inference: Methods for Mediation and Interaction. Oxford: Oxford University Press.   
VanderWeele, T. J., Asomaning, K., and Tchetgen Tchetgen, E. J. (2012). Genetic variants on 15q25.1, smoking, and lung cancer: An assessment of mediation and interaction. American Journal of Epidemiology, 175:1013-1020.

VanderWeele, T. J. and Ding, P. (2017). Sensitivity analysis in observational research: introducing the E-value. Annals of Internal Medicine, 167:268-274.   
VanderWeele, T. J. and Shpitser, I. (2011). A new criterion for confounder selection. Biometrics, 67:1406-1413.   
VanderWeele, T. J. and Tchetgen Tchetgen, E. J. (2017). Mediation analysis with time varying exposures and mediators. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 79:917-938.   
VanderWeele, T. J., Tchetgen Tchetgen, E. J., Cornelis, M., and Kraft, P. (2014). Methodological challenges in Mendelian randomization. *Epidemiology*, 25:427.   
Vansteelandt, S. and Daniel, R. M. (2014). On regression adjustment for the propensity score. Statistics in Medicine, 33:4053-4072.   
Vansteelandt, S. and Dukes, O. (2022). Assumption-lean inference for generalised linear model parameters (with discussion). Journal of the Royal Statistical Society, Series B (Statistical Methodology), 84:657-685.   
Vansteelandt, S. and Joffe, M. (2014). Structural nested models and G-estimation: the partially realized promise. Statistical Science, 29:707-731.   
Vermeulen, K. and Vansteelandt, S. (2015). Bias-reduced doubly robust estimation. Journal of the American Statistical Association, 110:1024-1036.   
Voight, B. F., Peloso, G. M., Orho-Melander, M., Frikke-Schmidt, R., Barbalic, M., Jensen, M. K., Hindy, G., Holm, H., Ding, E. L., and Johnson, T. (2012). Plasma HDL cholesterol and risk of myocardial infarction: a Mendelian randomisation study. The Lancet, 380:572-580.   
Wager, S. and Athey, S. (2018). Estimation and inference of heterogeneous treatment effects using random forests. Journal of the American Statistical Association, 113:1228-1242.   
Wager, S., Du, W., Taylor, J., and Tibshirani, R. J. (2016). High-dimensional regression adjustments in randomized experiments. Proceedings of the National Academy of Sciences of the United States of America, 113:12673-12678.   
Wald, A. (1940). The fitting of straight lines if both variables are subject to error. Annals of Mathematical Statistics, 11:284-300.   
Wang, L., Zhang, Y., Richardson, T. S., and Zhou, X.-H. (2020). Robust estimation of propensity score weights via subclassification. arXiv preprint arXiv:1602.06366.

# C.4 Bibliography

Wang, Y. and Li, X. (2022). *Rerandomization with diminishing covariate imbalance and diverging number of covariates*. *Annals of Statistics*, 50:3439-3465.   
White, H. (1980). A heteroskedasticity-consistent covariance matrix estimator and a direct test for heteroskedasticity. *Econometrica*, 48:817-838.   
Wooldridge, J. (2016). Should instrumental variables be used as matching variables? Research in Economics, 70:232-237.   
Wooldridge, J. M. (2015). Control function methods in applied econometrics. Journal of Human Resources, 50:420-445.   
Wu, J. and Ding, P. (2021). Randomization tests for weak null hypotheses in randomized experiments. Journal of the American Statistical Association, 116:1898-1913.   
Yang, F. and Ding, P. (2018a). Using survival information in truncation by death problems without the monotonicity assumption. *Biometrics*, 74:1232-1239.   
Yang, F. and Small, D. S. (2016). Using post-outcome measurement information in censoring-by-death problems. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 78:299-318.   
Yang, S. and Ding, P. (2018b). Asymptotic causal inference with observational studies trimmed by the estimated propensity scores. *Biometrika*, 105:487-493.   
Zelen, M. (1979). A new design for randomized clinical trials. New England Journal of Medicine, 300:1242-1245.   
Zhang, J. L. and Rubin, D. B. (2003). Estimation of causal effects via principal stratification when some outcomes are truncated by "death". Journal of Educational and Behavioral Statistics, 28:353-368.   
Zhang, J. L., Rubin, D. B., and Mealli, F. (2009). Likelihood-based analysis of causal effects of job-training programs using principal stratification. Journal of the American Statistical Association, 104:166-176.   
Zhang, M. and Ding, P. (2022). Interpretable sensitivity analysis for the baron-kenny approach to mediation with unmeasured confounding. arXiv preprint arXiv:2205.08030.   
Zhao, A. and Ding, P. (2021a). Covariate-adjusted Fisher randomization tests for the average treatment effect. Journal of Econometrics, 225:278-294.   
Zhao, A. and Ding, P. (2021b). No star is good news: A unified look at rerandomization based on $p$ -values from covariate balance tests. arXiv preprint arXiv:2112.10545.

Zhao, Q., Wang, J., Hemani, G., Bowden, J., and Small, D. (2020). Statistical inference in two-sample summary-data Mendelian randomization using robust adjusted profile score. Annals of Statistics, 48:1742-1769.