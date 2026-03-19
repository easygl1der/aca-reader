# Logit Standardization in Knowledge Distillation

Shangquan Sun $^{1,2}$ , Wenqi Ren $^{3\dagger}$ , Jingzhi Li $^{1}$ , Rui Wang $^{1,2}$ , Xiaochun Cao $^{3}$

$^{1}$ Institute of Information Engineering, Chinese Academy of Sciences

$^{2}$ School of Cyber Security, University of Chinese Academy of Sciences

$^{3}$ School of Cyber Science and Technology, Sun Yat-sen University, Shenzhen Campus

{sunshangquan,lijingzhi,wangrui}@iie.ac.cn,{renwq3,caoxiaochun}@mail.sysu.edu.cn

# Abstract

Knowledge distillation involves transferring soft labels from a teacher to a student using a shared temperature-based softmax function. However, the assumption of a shared temperature between teacher and student implies a mandatory exact match between their logits in terms of logit range and variance. This side-effect limits the performance of student, considering the capacity discrepancy between them and the finding that the innate logit relations of teacher are sufficient for student to learn. To address this issue, we propose setting the temperature as the weighted standard deviation of logit and performing a plug-and-play $\mathcal{Z}$ -score pre-process of logit standardization before applying softmax and Kullback-Leibler divergence. Our preprocess enables student to focus on essential logit relations from teacher rather than requiring a magnitude match, and can improve the performance of existing logit-based distillation methods. We also show a typical case where the conventional setting of sharing temperature between teacher and student cannot reliably yield the authentic distillation evaluation; nonetheless, this challenge is successfully alleviated by our $\mathcal{Z}$ -score. We extensively evaluate our method for various student and teacher models on CIFAR100 and ImageNet, showing its significant superiority. The vanilla knowledge distillation powered by our pre-process can achieve favorable performance against state-of-the-art methods, and other distillation variants can obtain considerable gain with the assistance of our pre-process. The codes, pre-trained models and logs are released on Github.

# 1. Introduction

The development of deep neural networks (DNN) has revolutionized the field of computer vision in the past decade. However, with increasing performance and capacity, the model size and computational cost of DNN have also

![](images/1b817e95e40e708ef5004f224256829c152e1e1747afc7e026f07aef5c595ff8.jpg)  
(a) Vanilla KD

![](images/beadeff672678607d2f517c8ff071916273fb5967fdf13d5f8f136427565a8c1.jpg)  
(b) KD w/ our logit standardization   
Figure 1. Vanilla knowledge distillation implicitly enforces an exact match between the magnitudes of teacher and student logits. It is an unnecessary side-effect because it is found sufficient to preserve the innate relations between their logits. Given the capacity gap between them, it is also challenging for a lightweight student to produce logits with the same magnitude as a cumbersome teacher. In contrast, the proposed $\mathcal{Z}$ -score logit standardization pre-process mitigates the side-effect. The standardized student logits have arbitrary magnitude suitable for the student's capacity while preserving the essential relations learned from the teacher.

been expanding. Despite of a tendency that larger models have greater capacity, many efforts have been made by researchers to cut down model size without sacrificing much accuracy. In addition to designing lightweight models, knowledge distillation (KD) has emerged as a new approach to achieve this goal. It involves transferring the knowledge of a pre-trained heavy model, known as the teacher network, to a small target model, known as the student network.

Hinton et al. [13] firstly proposes distilling a teacher's knowledge into a student by minimizing a Kullback-Leibler (KL) divergence between their predictions. A scaling factor

of the softmax function in this context, called temperature $\mathcal{T}$ , is introduced to soften the predicted probabilities. Traditionally, the temperature is set globally beforehand as a hyper-parameter and remains fixed throughout training. CTKD [24] adopts an adversarial learning module to predict sample-wise temperatures, adapting to varying sample difficulties. However, existing logit-based KD approaches still assume that the teacher and student should share temperatures, neglecting the possibility of distinct temperature values in the KL divergence. In this work, we demonstrate that the general softmax expression in both classification and KD is derived from the principle of entropy maximization in information theory. During this derivation, Lagrangian multipliers appear and take the form of temperatures, based on which we establish the irrelevance between the temperatures of teacher and student, as well as the irrelevance among temperatures for different samples. The proof supports our motivation to allocate distinct temperatures between teacher and student and across samples.

Compared to an exact match of logit prediction, it is found that the inter-class relations of predictions are sufficient for student to achieve performance similar to teacher [15]. A lightweight student faces challenges in predicting logits with a comparable range and variance as a cumbersome teacher, given the capacity gap between them [7, 28, 35]. However, we demonstrate that the conventional practice of sharing temperatures in KL divergence still implicitly enforces an exact match between the student and teacher's logits. Existing logit-based KD methods, unaware of this issue, commonly fall in the pitfall, resulting in a general performance drop. To address this, we propose using weighted logit standard deviation as an adaptive temperature and present a $\mathcal{Z}$ -score logit standardization as a pre-processing step before applying softmax. This preprocessing maps arbitrary range of logits into a bounded range, allowing student logits to possess arbitrary ranges and variances while efficiently learning and preserving only the innate relationships of teacher logits. We present a typical case where the KL divergence loss under the setting of sharing temperatures in softmax may be misleading and cannot reliably measure the performance of distilled students. In contrast, with our $\mathcal{Z}$ -score pre-process, the issue of the shared temperatures in the case is eliminated.

In summary, our contributions are in three folds

- Based on the entropy maximization principle in information theory, we use Lagrangian multipliers to derive the general expression of softmax in logit-based KD. We show that the temperature comes from the derived multipliers, allowing it to be selected differently for various samples and distinctly for student and teacher.   
- To address the issues of the conventional logit-based KD pipeline caused by shared temperatures, including an implicit mandatory logit match and an inauthentic indica

tion of student performance, we propose a pre-process of logit distillation to adaptively allocate temperatures between teacher and student and across samples, capable of facilitating existing logit-based KD approaches.

- We conduct extensive experiments with various teacher and student models on CIFAR-100 [18] and ImageNet [32] and demonstrate the superior advantages of our method as a plug-and-play pre-process.

# 2. Related Work

Knowledge distillation [13] is designed to transfer the "dark" knowledge from a cumbersome teacher model to a lightweight student model. By learning from the soft labels of teacher, student can achieve better performance than training on hard labels only. The traditional method trains a student by minimizing a difference such as KL divergence between its predicted probability and the teacher's. The prediction of probability is commonly approximated by the softmax of logit output. KD algorithms can be classified into three types, i.e., logit-based [3, 13, 17, 22, 28, 47, 49, 50], feature-based [1, 4, 5, 10, 12, 23, 25, 27, 31, 37, 44], and relation-based [15, 19, 29, 30, 39, 43] methods.

A temperature is introduced to flatten the probabilities in logit-based methods. Several works [2, 13, 26] explore its properties and effects. They reach an identical conclusion that temperature controls how much attention student pays on those logits more negative than average. A very low temperature makes student ignore other logits and instead mainly focus on the largest logit of teacher. However, they do not discuss why teacher and student share a globally predefined temperature. It was unknown whether temperature can be determined in an instance-wise level until CTKD [24] proposed predicting sample-wise temperatures by leveraging adversarial learning. However, it assumes that teacher and student should share temperatures. It was still undiscovered whether teacher and student can have divergent temperatures. ATKD [9] proposes a sharpness metric and chooses adaptive temperature by reducing the gap between teacher and student. However, their assumption of a zero logit mean relies on numerical approximation and limits its performance. Additionally, they do not thoroughly discuss where the temperature is derived from and whether distinct temperatures can be assigned. In this work, we provide an analytical derivation based on the entropy-maximization principle, demonstrating that students and teachers do not necessarily share a temperature. It is also found sufficient to preserve the innate relationship of prediction, instead of exact logit values of teacher [15]. However, the existing logit-based KD pipelines still implicitly mandate an exact match between teacher and student logits. We thus define the temperature to be the weighted standard deviation of logit to alleviate the issue and facilitate the existing logit-based KD approaches.

# 3. Background and Notation

Suppose we have a transfer dataset $\mathcal{D}$ containing totally $N$ samples $\{\mathbf{x}_n, y_n\}_{n=1}^N$ , where $\mathbf{x}_n \in \mathbb{R}^{H \times W}$ and $y_n \in [1, K]$ are the image and label respectively for the $n$ -th sample. The notations of $H$ , $W$ and $K$ are image height, width and the number of classes. Given an input $\{\mathbf{x}_n, y_n\}$ , teacher $f_T$ and student $f_S$ respectively predict logit vectors $\mathbf{v}_n$ and $\mathbf{z}_n \in \mathbb{R}^{1 \times K}$ . Namely, $\mathbf{z}_n = f_S(\mathbf{x}_n)$ and $\mathbf{v}_n = f_T(\mathbf{x}_n)$ .

It is widely accepted that a softmax function involving a temperature $\mathcal{T}$ is used to convert the logit to probability vectors $q(\mathbf{z}_n)$ or $q(\mathbf{v}_n)$ such that their $k$ -th items have

$$
q \left(\mathbf {z} _ {n}\right) ^ {(k)} = \frac {\exp \left(\mathbf {z} _ {n} ^ {(k)} / \mathcal {T}\right)}{\sum_ {m = 1} ^ {K} \exp \left(\mathbf {z} _ {n} ^ {(m)} / \mathcal {T}\right)}, \tag {1}
$$

$$
q \left(\mathbf {v} _ {n}\right) ^ {(k)} = \frac {\exp \left(\mathbf {v} _ {n} ^ {(k)} / \mathcal {T}\right)}{\sum_ {m = 1} ^ {K} \exp \left(\mathbf {v} _ {n} ^ {(m)} / \mathcal {T}\right)}, \tag {2}
$$

where $\mathbf{z}_n^{(k)}$ and $\mathbf{v}_n^{(k)}$ are the $k$ -th item of $\mathbf{z}_n$ and $\mathbf{v}_n$ respectively. A knowledge distillation process is essentially letting $q(\mathbf{z}_n)^{(k)}$ mimic $q(\mathbf{v}_n)^{(k)}$ for any class and all samples. The objective is realized by minimizing KL divergence

$$
\mathcal {L} _ {\mathrm {K L}} \left(q (\mathbf {v} _ {n}) | | q (\mathbf {z} _ {n})\right) = \sum_ {k = 1} ^ {K} q (\mathbf {v} _ {n}) ^ {(k)} \log \left(\frac {q (\mathbf {v} _ {n}) ^ {(k)}}{q (\mathbf {z} _ {n}) ^ {(k)}}\right),
$$

which is theoretically equivalent to a cross-entropy loss when optimizing solely on $\mathbf{z}$

$$
\mathcal {L} _ {\mathrm {C E}} \left(q \left(\mathbf {v} _ {n}\right), q \left(\mathbf {z} _ {n}\right)\right) = - \sum_ {k = 1} ^ {K} q \left(\mathbf {v} _ {n}\right) ^ {(k)} \log q \left(\mathbf {z} _ {n}\right) ^ {(k)}. \tag {3}
$$

Note that they are empirically nonequivalent as their gradients diverge due to the negative entropy term of $q(\mathbf{v}_n)$ .

# 4. Methodology

It is widely accepted that $\mathcal{T}$ is shared for teacher and student in Eq. 1 and Eq. 2. In contrast, in Sec. 4.1, we show the irrelevance between the temperatures of teacher and student, as well as across different samples. Guaranteed that temperatures can be different between teacher and student and among sample, we further show two side-effect drawbacks of shared-temperatures setting in conventional KD pipelines in Sec. 4.2. In Sec. 4.3, we propose leveraging logit standard deviation as a factor in temperature and derive a preprocess of logit standardization.

# 4.1. Irrelevance between Temperatures

In Sec. 4.1.1 and 4.1.2, we first give a derivation of the temperature-involved softmax function in classification and KD based on the entropy-maximization principle in information theory. This implies the temperatures of student and teacher can be distinct and sample-wisely different.

# 4.1.1 Derivation of softmax in Classification

The softmax function in classification can be proved to be the unique solution of maximizing entropy subject to the normalization condition of probability and a constraint on

the expectation of states in information theory [16]. The derivation is also leveraged in confidence calibration to formulate temperature scaling [8]. Suppose we have the following constrained entropy-maximization optimization,

$$
\max  _ {q} \mathcal {L} _ {1} = - \sum_ {n = 1} ^ {N} \sum_ {k = 1} ^ {K} q \left(\mathbf {v} _ {n}\right) ^ {(k)} \log q \left(\mathbf {v} _ {n}\right) ^ {(k)}
$$

$$
\begin{array}{l} s. t. \left\{ \begin{array}{l} \sum_ {k = 1} ^ {K} q \left(\mathbf {v} _ {n}\right) ^ {(k)} = 1, \quad \forall n \\ \mathbb {E} _ {q} [ \mathbf {v} _ {n} ] = \sum_ {k = 1} ^ {K} \mathbf {v} _ {n} ^ {(k)} q \left(\mathbf {v} _ {n}\right) ^ {(k)} = \mathbf {v} _ {n} ^ {\left(y _ {n}\right)}, \quad \forall n. \end{array} \right. \end{array} \tag {4}
$$

The first constraint holds due to the requirement of discrete probability density, while the second constraint controls the scope of the distribution such that model accurately predicts the target class. Suppose $\hat{q}_n$ to be the one-hot hard probability distribution whose values are all zero except at the target index $\hat{q}_n^{(y_n)} = 1$ . The second constraint is then actually $\mathbb{E}_q[\mathbf{v}_n] = \sum_{k=1}^K \mathbf{v}_n^{(k)} \hat{q}_n^{(k)} = \mathbf{v}_n^{(y_n)}$ . This is equivalent to making model predict the correct label $y_n$ . By applying Lagrangian multipliers $\{\alpha_{1,i}\}_{i=1}^N$ and $\{\alpha_{2,i}\}_{i=1}^N$ , it gives

$$
\begin{array}{l} \mathcal {L} _ {T} = \mathcal {L} _ {1} + \sum_ {n = 1} ^ {N} \alpha_ {1, n} \left(\sum_ {k = 1} ^ {K} q (\mathbf {v} _ {n}) ^ {(k)} - 1\right) \\ + \sum_ {n = 1} ^ {N} \alpha_ {2, n} \left(\sum_ {k = 1} ^ {K} \mathbf {v} _ {n} ^ {(k)} q \left(\mathbf {v} _ {n}\right) ^ {(k)} - \mathbf {v} _ {n} ^ {\left(y _ {n}\right)}\right). \\ \end{array}
$$

Taking the partial derivative with respective to $\alpha_{1,n}$ and $\alpha_{2,n}$ yields back the constraints. In contrast, taking the derivative with respective to $q(\mathbf{v}_n)^{(k)}$ gives

$$
\frac {\partial \mathcal {L} _ {T}}{\partial q (\mathbf {v} _ {n}) ^ {(k)}} = - 1 - \log q (\mathbf {v} _ {n}) ^ {(k)} + \alpha_ {1, n} + \alpha_ {2, n} \mathbf {v} _ {n} ^ {(k)}, \tag {5}
$$

which leads to a solution by making the derivative zero:

$$
q \left(\mathbf {v} _ {n}\right) ^ {(k)} = \exp \left(\alpha_ {2, n} \mathbf {v} _ {n} ^ {(k)}\right) / Z _ {T}, \tag {6}
$$

where $Z_{T} = \exp (1 - \alpha_{1,n}) = \sum_{m = 1}^{K}\exp \left(\alpha_{2,n}\mathbf{v}_{n}^{(m)}\right)$ is the partition function to fulfill the normalization condition.

# 4.1.2 Derivation of softmax in KD

Following the idea, we define a problem of entropy-maximization to formulate the softmax in KD. Given a well-trained teacher and its prediction $q(\mathbf{v}_n)$ , we have the objective function for the prediction of student as follows,

$$
\begin{array}{l} \max  _ {q} \mathcal {L} _ {2} = - \sum_ {n = 1} ^ {N} \sum_ {k = 1} ^ {K} q \left(\mathbf {z} _ {n}\right) ^ {(k)} \log q \left(\mathbf {z} _ {n}\right) ^ {(k)} \\ \begin{array}{l} s. t. \left\{ \begin{array}{l} \sum_ {k = 1} ^ {K} q \left(\mathbf {z} _ {n}\right) ^ {(k)} = 1, \quad \forall n \\ \sum_ {k = 1} ^ {K} \mathbf {z} _ {n} ^ {(k)} q \left(\mathbf {z} _ {n}\right) ^ {(k)} = \mathbf {z} _ {n} ^ {(y _ {n})}, \quad \forall n \\ \sum_ {k = 1} ^ {K} \mathbf {z} _ {n} ^ {(k)} q \left(\mathbf {z} _ {n}\right) ^ {(k)} = \sum_ {k = 1} ^ {K} \mathbf {z} _ {n} ^ {(k)} q \left(\mathbf {v} _ {n}\right) ^ {(k)}, \quad \forall n. \end{array} \right. \end{array} \tag {7} \\ \end{array}
$$

By applying Lagrangian multipliers $\beta_{1,n},\beta_{2,n}$ and $\beta_{3,n}$

$$
\begin{array}{l} \mathcal {L} _ {S} = \mathcal {L} _ {2} + \sum_ {n = 1} ^ {N} \beta_ {1, n} \left(\sum_ {k = 1} ^ {K} q \left(\mathbf {z} _ {n}\right) ^ {(k)} - 1\right) \\ + \sum_ {n = 1} ^ {N} \beta_ {2, n} \left(\sum_ {k = 1} ^ {K} \mathbf {z} _ {n} ^ {(k)} q \left(\mathbf {z} _ {n}\right) ^ {(k)} - \mathbf {z} _ {n} ^ {\left(y _ {n}\right)}\right) \\ + \sum_ {n = 1} ^ {N} \beta_ {3, n} \sum_ {k = 1} ^ {K} \mathbf {z} _ {n} ^ {(k)} \left(q \left(\mathbf {z} _ {n}\right) ^ {(k)} - q \left(\mathbf {v} _ {n}\right) ^ {(k)}\right). \\ \end{array}
$$

Taking its derivative with respect to $q(\mathbf{z}_n)^{(k)}$ gives

$$
\frac {\partial \mathcal {L} _ {S}}{\partial q (\mathbf {z} _ {n}) ^ {(k)}} = - 1 - \log q (\mathbf {z} _ {n}) ^ {(k)} + \beta_ {1, n} + \beta_ {2, n} \mathbf {z} _ {n} ^ {(k)} + \beta_ {3, n} \mathbf {z} _ {n} ^ {(k)}.
$$

Suppose $\beta_{n} = \beta_{2,n} + \beta_{3,n}$ for simplicity and it gives

$$
q \left(\mathbf {z} _ {n}\right) ^ {(k)} = \exp \left(\beta_ {n} \mathbf {z} _ {n} ^ {(k)}\right) / Z _ {S}, \tag {8}
$$

where $Z_{S} = \exp (1 - \beta_{1,n}) = \sum_{k = 1}^{K}\exp (\beta_{n}\mathbf{z}_{n}^{(k)})$ holds because of the normalization condition of probability density. The formulation in Eq. 8 has the same structure as Eq. 6.

Distinct Temperatures. Note that the partial derivatives of $\mathcal{L}_T$ with respective to $\alpha_{1,n}$ and $\alpha_{2,n}$ lead back to the two constraints respectively in Eq. 4 and the constraints are irrelevant to $\alpha_{1,n}$ and $\alpha_{2,n}$ . A similar case holds for Eq. 7. As a result, no explicit expression of them can be given and thus their values can be manually defined. If we set $\beta_n = \alpha_{2,n} = 1 / T$ , Eq. 6 and 8 turn to the expressions in KD involving a shared temperature for both student and teacher. When $\beta_n = \alpha_{2,n} = 1$ , the formulations revert to the traditional softmax function commonly used in classification. Eventually, we can choose $\beta_n \neq \alpha_{2,n}$ , indicating that students and teachers can have distinct temperatures.

Sample-wisely different Temperatures. It is common to define a global temperature for all samples. Namely for any $n$ , $\alpha_{2,n}$ and $\beta_{n}$ are defined as a constant value. In contrast, they could vary across different samples due to the lack of restrictions on them. It lacks a foundation to choose a global constant value as temperature. As a result, adopting sample-wise varying temperatures is allowed.

# 4.2. Drawbacks of Shared Temperatures

In this section, we show two shortcomings of the shared temperatures setting in conventional KD pipeline. We first rewrite the softmax in Eq. 8 in a general formulation by introducing two hyper-parameters $a_{S}$ and $b_{S}$ ,

$$
q \left(\mathbf {z} _ {n}; a _ {S}, b _ {S}\right) ^ {(k)} = \frac {\exp \left[ \left(\mathbf {z} _ {n} ^ {(k)} - a _ {S}\right) / b _ {S} \right]}{\sum_ {m = 1} ^ {K} \exp \left[ \left(\mathbf {z} _ {n} ^ {(m)} - a _ {S}\right) / b _ {S} \right]},
$$

where $a_{S}$ can be cancelled out and does not violate the equality. When $a_{S} = 0, b_{S} = 1 / \beta_{n}$ , it yields back the special case in Eq. 8. The similar equation for the case of teacher can be written by introducing $a_{T}$ and $b_{T}$ .

For a finally well-distilled student, we assume the KL divergence loss reaches minimum and its predicted prob

ability density matches that of teacher, i.e., $\forall k\in [1,K]$ $q(\mathbf{z}_n;a_S,b_S)^{(k)} = q(\mathbf{v}_n;a_T,b_T)^{(k)}$ . Then for arbitrary pair of indices $i,j\in [1,K]$ , it can easily lead to

$$
\begin{array}{l} \frac {\exp \left[ (\mathbf {z} _ {n} ^ {(i)} - a _ {S}) / b _ {S} \right]}{\exp \left[ (\mathbf {z} _ {n} ^ {(j)} - a _ {S}) / b _ {S} \right]} = \frac {\exp \left[ (\mathbf {v} _ {n} ^ {(i)} - a _ {T}) / b _ {T} \right]}{\exp \left[ (\mathbf {v} _ {n} ^ {(j)} - a _ {T}) / b _ {T} \right]} \\ \Rightarrow \left(\mathbf {z} _ {n} ^ {(i)} - \mathbf {z} _ {n} ^ {(j)}\right) / b _ {S} = \left(\mathbf {v} _ {n} ^ {(i)} - \mathbf {v} _ {n} ^ {(j)}\right) / b _ {T}. \\ \end{array}
$$

By taking a summation across $j$ from 1 to $K$ , we have

$$
\left(\mathbf {z} _ {n} ^ {(i)} - \overline {{\mathbf {z}}} _ {n}\right) / b _ {S} = \left(\mathbf {v} _ {n} ^ {(i)} - \overline {{\mathbf {v}}} _ {n}\right) / b _ {T}, \tag {9}
$$

where $\overline{\mathbf{z}}_n$ and $\overline{\mathbf{v}}_n$ are the mean of the student and teacher logit vectors respectively, i.e., $\overline{\mathbf{z}}_n = \frac{1}{K}\sum_{m=1}^{K}\mathbf{z}_n^{(m)}$ (similar and omitted for $\overline{\mathbf{v}}_n$ ). By taking the summation of the squared Eq. 9 across $i$ from 1 to $K$ , we can obtain

$$
\frac {\sigma \left(\mathbf {z} _ {n}\right) ^ {2}}{\sigma \left(\mathbf {v} _ {n}\right) ^ {2}} = \frac {\frac {1}{K} \sum_ {i = 1} ^ {K} \left(\mathbf {z} _ {n} ^ {(i)} - \overline {{\mathbf {z}}} _ {n}\right) ^ {2}}{\frac {1}{K} \sum_ {i = 1} ^ {K} \left(\mathbf {v} _ {n} ^ {(i)} - \overline {{\mathbf {v}}} _ {n}\right) ^ {2}} = \frac {b _ {S} ^ {2}}{b _ {T} ^ {2}}, \tag {10}
$$

where $\sigma$ is the function of standard deviation for an input vector. From Eq.9 and 10, we can describe two properties of a well-distilled student in terms of the logit shift and variance matching.

Logit shift. From Eq.9, it can be found that a constant shift exists between the logits of student and teacher in arbitrary index under the traditional setting of shared temperature $(b_{S} = b_{T})$ , i.e.,

$$
\mathbf {z} _ {n} ^ {(i)} = \mathbf {v} _ {n} ^ {(i)} + \Delta_ {n}, \tag {11}
$$

where $\Delta_{n} = \overline{\mathbf{z}}_{n} - \overline{\mathbf{v}}_{n}$ can be considered as constant for the $n$ -th sample. This implies in the traditional KD approach, student is forced to strictly mimic the shifted logit of teachers. Considering the gap of their model size and capacity, student may be unable to produce as wide logit range as teacher [7, 28, 35]. In contrast, a student can be considered excellent enough when its logit rank matches teacher [15], i.e., given the indices that sorts the teacher logits $t_1, \ldots, t_K \in [1, K]$ such that $\mathbf{v}_n^{(t_1)} \leq \dots \leq \mathbf{v}_n^{(t_K)}$ , then $\mathbf{z}_n^{(t_1)} \leq \dots \leq \mathbf{z}_n^{(t_K)}$ holds. The logit relation is the essential knowledge that makes student predict as excellently as teacher. Such a logit shift is thus a side-effect in conventional KD pipeline and a shackle compelling student to generate unnecessarily difficult results.

Variance match. From Eq. 10, we come into a conclusion that the ratio between the temperatures of student and teacher equals the ratio between the standard deviations of their predicted logits for a well-distilled student, i.e.,

$$
\sigma \left(\mathbf {z} _ {n}\right) / \sigma \left(\mathbf {v} _ {n}\right) = b _ {S} / b _ {T}. \tag {12}
$$

In the setting of temperature sharing in vanilla KD, the student is forced to predict logit such that $\sigma (\mathbf{z}_n) = \sigma (\mathbf{v}_n)$ . This is another shackle applied to student restricting the standard deviation of its predicted logits. In contrast, since the hyper-parameter comes from Lagrangian multiplier and is flexible to tune, we can define $b_{S}^{*}\propto \sigma (\mathbf{z}_{n})$ and $b_{T}^{*}\propto$

Algorithm 1: Weighted $\mathcal{Z}$ -score function.

Input: Input vector $\mathbf{x}$ and Base temperature $\tau$

Output: Standardized vector $\mathcal{Z}(\mathbf{x};\tau)$

$$
\begin{array}{l} \mathbf {1} \overline {{\mathbf {x}}} \leftarrow \frac {1}{K} \sum_ {k = 1} ^ {K} \mathbf {x} ^ {(k)} \\ 2 \sigma (\mathbf {x}) \leftarrow \sqrt {\frac {1}{K} \sum_ {k = 1} ^ {K} \left(\mathbf {x} ^ {(k)} - \overline {{\mathbf {x}}}\right) ^ {2}} \\ 3 \operatorname {r e t u r n} (\mathbf {x} - \overline {{\mathbf {x}}}) / \sigma (\mathbf {x}) / \tau \\ \end{array}
$$

Algorithm 2: $\mathcal{Z}$ -score logit standardization pre-process in knowledge distillation.

Input: Transfer set $\mathcal{D}$ with image-label sample pair $\{\mathbf{x}_n,y_n\}_{n = 1}^N$ , Base Temperature $\tau$ , Teacher $f_{T}$ , Student $f_{S}$ , Loss $\mathcal{L}_{\mathrm{KD}}$ (e.g., $\mathcal{L}_{\mathrm{KL}}$ ), loss weight $\lambda$ , and $\mathcal{Z}$ -score function $\mathcal{Z}$ in Algo. 1

Output: Trained student model $f_{S}$

1 foreach $(\mathbf{x}_n,y_n)$ in $\mathcal{D}$ do   
2 $\mathbf{v}_n\gets f_T(\mathbf{x}_n),\mathbf{z}_n\gets f_S(\mathbf{x}_n)$   
3 $q(\mathbf{v}_n)\gets \mathrm{softmax}[\mathcal{Z}(\mathbf{v}_n;\tau)]$   
4 $q(\mathbf{z}_n)\gets \mathrm{softmax}[\mathcal{Z}(\mathbf{z}_n;\tau)]$   
5 $q^{\prime}(\mathbf{z}_n)\gets \mathrm{softmax}(\mathbf{z}_n)$   
6 Update $f_{S}$ towards minimizing

$$
\lambda_ {\mathrm {C E}} \mathcal {L} _ {\mathrm {C E}} (y _ {n}, q ^ {\prime} (\mathbf {z} _ {n})) + \lambda_ {\mathrm {K D}} \tau^ {2} \mathcal {L} (q (\mathbf {v} _ {n}), q (\mathbf {z} _ {n}))
$$

7 end

$\sigma (\mathbf{v}_n)$ . In that way, the equation in Eq. 12 always holds.

# 4.3. Logit Standardization

To break the two shackles, we therefore propose setting the hyper-parameters $a_{S}, b_{S}, a_{T}$ and $b_{S}$ to be the mean and the weighted standard deviation of their logits respectively, i.e.,

$$
q \left(\mathbf {z} _ {n}; \overline {{\mathbf {z}}} _ {n}, \sigma (\mathbf {z} _ {n})\right) ^ {(k)} = \frac {\exp \left(\mathcal {Z} (\mathbf {z} _ {n} ; \tau) ^ {(k)}\right)}{\sum_ {m = 1} ^ {K} \exp \left(\mathcal {Z} (\mathbf {z} _ {n} ; \tau) ^ {(m)}\right)},
$$

where $\mathcal{Z}$ is the $\mathcal{Z}$ -score function in Algo. 1. The case for teacher logit is similar and omitted. A base temperature $\tau$ is introduced and shared for both teacher and student models. The $\mathcal{Z}$ -score standardization has at least four advantageous properties, i.e., zero mean, finite standard deviation, monotonicity and boundedness.

Zero mean. The mean of standardized vector can be easily shown to be zero. In previous works [9, 13], a zero mean is assumed and usually empirically violated. In contrast, the $\mathcal{Z}$ -score function intrinsically guarantees a zero mean.

Finite standard deviation. The standard deviation of the weighted $\mathcal{Z}$ -score output $\mathcal{Z}(\mathbf{z}_n; \tau)$ can be shown equal to $1 / \tau$ . The property makes the standardized student and teacher logit map to an identical Gaussian-like distribution with zero mean and definite standard deviation. The mapping of standardization is many-to-one, meaning that its reverse is indefinite. The variance and value range of original student logit vector $\mathbf{z}_n$ is thereby free of restriction.

Monotonicity. It is easy to show that $\mathcal{Z}$ -score is a linear transformation function and thus lies in monotonic func

![](images/6b143e3bdf55d68c70366176f5644dbb75c2cf40c7384e7b2c1cc79acd9b9523.jpg)  
Figure 2. A toy case where two students, $S_{1}$ and $S_{2}$ , learning from the same teacher with an identical temperature (assumed 1 for simplicity). Student $S_{1}$ generates the logits much closer to the teacher's in terms of magnitude and thus has lower loss of 0.1749, but it returns a wrong prediction of "bird". In contrast, Student $S_{2}$ outputs the logits far from the teacher's and yields greater loss value of 0.3457, but it returns the correct prediction of "dog". After the proposed logit standardization, the issue is addressed.

tions. This property ensures that the transformed student logit remains the same rank as the original one. The necessary innate relation within teacher logit can thus be preserved and transferred to student.

Boundedness. The standardized logit can be shown bounded within $\left[-\sqrt{K - 1} / \tau, \sqrt{K - 1} / \tau\right]$ . Compared to traditional KD, it is feasible to control the logit range and avoid extremely large exponential value. To this end, we define a base temperature to control the range.

The pseudo-code of the proposed logit standardization pre-process is illustrated in Algo. 2.

# 4.3.1 Toy Case

Fig. 2 shows a typical case where the conventional logit-based KD setting of shared temperature may lead to an inauthentic evaluation of student performance. The first student $S_{1}$ predicts logits closer to the teacher $T$ in terms of magnitude, while the second student $S_{2}$ preserves the same innate logit relations as the teacher. As a result, $S_{1}$ obtains lower KL divergence loss of 0.1749, much better than the second student $S_{2}$ (0.3457). However, $S_{1}$ has a wrong prediction of "Bird" while $S_{2}$ predicts "Dog" correctly, which contradicts the loss comparison. By applying our $Z$ -score, all logits are re-scaled and the relations among logits instead of their magnitudes are emphasized in the evaluation. Namely, $S_{2}$ gets a loss of 0, much better than $S_{1}$ of 0.0995, which is in line with the observed predictions.

# 5. Experiments

Datasets. We conduct experiments on CIFAR-100 [18] and ImageNet [32]. CIFAR-100 [18] is a common dataset

Table 1. The Top-1 Accuracy (%) of different knowledge distillation methods on the validation set of CIFAR-100 [18]. The teacher and student have distinct architectures. The KD methods are sorted by the types, i.e., feature-based and logit-based. We apply our logit standardization to the existing logit-based methods and use $\Delta$ to show its performance gain. The values in blue denote slight enhancement and those in red non-trivial enhancement no less than 0.15. The best and second best results are emphasized in bold and underlined cases.   

<table><tr><td rowspan="4">Type</td><td>Teacher</td><td>ResNet32×4</td><td>ResNet32×4</td><td>ResNet32×4</td><td>WRN-40-2</td><td>WRN-40-2</td><td>VGG13</td><td>ResNet50</td></tr><tr><td rowspan="3">Student</td><td>79.42</td><td>79.42</td><td>79.42</td><td>75.61</td><td>75.61</td><td>74.64</td><td>79.34</td></tr><tr><td>SHN-V2</td><td>WRN-16-2</td><td>WRN-40-2</td><td>ResNet8×4</td><td>MN-V2</td><td>MN-V2</td><td>MN-V2</td></tr><tr><td>71.82</td><td>73.26</td><td>75.61</td><td>72.50</td><td>64.60</td><td>64.60</td><td>64.60</td></tr><tr><td rowspan="8">Feature</td><td>FitNet [31]</td><td>73.54</td><td>74.70</td><td>77.69</td><td>74.61</td><td>68.64</td><td>64.16</td><td>63.16</td></tr><tr><td>AT [46]</td><td>72.73</td><td>73.91</td><td>77.43</td><td>74.11</td><td>60.78</td><td>59.40</td><td>58.58</td></tr><tr><td>RKD [29]</td><td>73.21</td><td>74.86</td><td>77.82</td><td>75.26</td><td>69.27</td><td>64.52</td><td>64.43</td></tr><tr><td>CRD [37]</td><td>75.65</td><td>75.65</td><td>78.15</td><td>75.24</td><td>70.28</td><td>69.73</td><td>69.11</td></tr><tr><td>OFD [12]</td><td>76.82</td><td>76.17</td><td>79.25</td><td>74.36</td><td>69.92</td><td>69.48</td><td>69.04</td></tr><tr><td>ReviewKD [5]</td><td>77.78</td><td>76.11</td><td>78.96</td><td>74.34</td><td>71.28</td><td>70.37</td><td>69.89</td></tr><tr><td>SimKD [4]</td><td>78.39</td><td>77.17</td><td>79.29</td><td>75.29</td><td>70.10</td><td>69.44</td><td>69.97</td></tr><tr><td>CAT-KD [10]</td><td>78.41</td><td>76.97</td><td>78.59</td><td>75.38</td><td>70.24</td><td>69.13</td><td>71.36</td></tr><tr><td rowspan="12">Logit</td><td>KD [13]</td><td>74.45</td><td>74.90</td><td>77.70</td><td>73.97</td><td>68.36</td><td>67.37</td><td>67.35</td></tr><tr><td>KD+Ours</td><td>75.56</td><td>75.26</td><td>77.92</td><td>77.11</td><td>69.23</td><td>68.61</td><td>69.02</td></tr><tr><td>Δ</td><td>1.11</td><td>0.36</td><td>0.22</td><td>3.14</td><td>0.87</td><td>1.24</td><td>1.67</td></tr><tr><td>CTKD [24]</td><td>75.37</td><td>74.57</td><td>77.66</td><td>74.61</td><td>68.34</td><td>68.50</td><td>68.67</td></tr><tr><td>CTKD+Ours</td><td>76.18</td><td>75.16</td><td>77.99</td><td>77.03</td><td>69.53</td><td>68.98</td><td>69.36</td></tr><tr><td>Δ</td><td>0.81</td><td>0.59</td><td>0.33</td><td>2.42</td><td>1.19</td><td>0.48</td><td>0.69</td></tr><tr><td>DKD [50]</td><td>77.07</td><td>75.70</td><td>78.46</td><td>75.56</td><td>69.28</td><td>69.71</td><td>70.35</td></tr><tr><td>DKD+Ours</td><td>77.37</td><td>76.19</td><td>78.95</td><td>76.75</td><td>70.01</td><td>69.98</td><td>70.45</td></tr><tr><td>Δ</td><td>0.30</td><td>0.49</td><td>0.49</td><td>1.19</td><td>0.73</td><td>0.27</td><td>0.10</td></tr><tr><td>MLKD [17]</td><td>78.44</td><td>76.52</td><td>79.26</td><td>77.33</td><td>70.78</td><td>70.57</td><td>71.04</td></tr><tr><td>MLKD+Ours</td><td>78.76</td><td>77.53</td><td>79.66</td><td>77.68</td><td>71.61</td><td>70.94</td><td>71.19</td></tr><tr><td>Δ</td><td>0.32</td><td>1.01</td><td>0.40</td><td>0.35</td><td>0.83</td><td>0.37</td><td>0.15</td></tr></table>

for image classification consisting of 50,000 training and 10,000 validation images. It contains 100 classes and its image size is $32 \times 32$ . ImageNet [32] is a large-scale dataset for image classification containing 1,000 categories and around 1.28 million training and 50,000 validation images.

Baselines. We evaluate the effect of our logit standardization as pre-process for multiple logit-based KD approaches, including KD [13], CTKD [24], DKD [50] and MLKD[17]. We also compare with various feature-based KD methods including FitNet [31], RKD [29], CRD [30], OFD [12], ReviewKD [5], SimKD [4], and CAT-KD [10].

Implementation Details. We follow the same experimental settings as previous works [5, 17, 50]. For the experiments on CIFAR-100, the optimizer is SGD [36] and the epoch number is 240, except for MLKD being 480 [17]. The learning rate is set initially 0.01 for MobileNets[14, 33] and ShuffleNets [48] and 0.05 for other architectures consisting of ResNets [11], WRNs [45] and VGGs [34]. All results are reported by taking average over 4 trials. More detailed experimental settings are elaborated in the supplements.

# 5.1. Main Results

Results on CIFAR-100. We compare the KD results of different methods under various teacher/student settings in Tab. 1 and 2. Tab. 1 shows the cases that the teacher and student models have distinct structures, while Tab. 2 demonstrates the cases that they have the same architecture.

We evaluate our pre-process on four existing logit-based KD methods. As shown, our $\mathcal{Z}$ -score standardization can

constantly improve their performances. After applying our pre-process, the vanilla KD [13] achieves comparable performance to the state-of-the-art (SOTA) feature-based methods. As SOTA logit-based methods, DKD [50] and MLKD [17] can also be further boosted by our pre-process. CTKD [24] is a KD method that can determine sample-wise temperatures. We combine it with ours by leveraging it to predict the base temperature in Algo. 2. As illustrated in tables, student models distilled by CTKD benefits from our pre-process as well.

Results on ImageNet of different methods in terms of top-1 and top-5 accuracy are compared in Tab. 3. Our pre-process can achieve consistent improvement for all the three logit-based methods on the large-scale dataset as well.

Ablation Studies We conduct extensive ablation studies in terms of different configurations of base temperature and the weight of KD loss $\lambda_{\mathrm{KD}}$ . The part of results when base temperature is 2 are shown in Tab. 4. We can see as the weight of KD loss increases, the vanilla KD where softmax takes the original logit vectors as input cannot have a considerable performance gain. In contrast, our $\mathcal{Z}$ -score pre-process achieves a significant enhancement. More ablation studies of other settings are in the supplements.

The weight of KD loss is set relatively larger than that of CE loss because our pre-process enables student to focus more on the dark knowledge from teacher instead of hard labels. Another reason of the large KD weight is to compensate the gradient involving $\mathcal{Z}$ -score.

Table 2. The Top-1 Accuracy (%) of different knowledge distillation methods on the validation set of CIFAR-100 [18]. The teacher and student have identical architectures but different configurations. The KD methods are sorted by the types. We apply our logit standardization to the existing logit-based methods and use $\Delta$ to show its performance gain. The values in blue denote slight enhancement and those in red non-trivial enhancement no less than 0.15. The best and second best results are emphasized in bold and underlined cases.   

<table><tr><td rowspan="4">Type</td><td>Teacher</td><td>ResNet32×4</td><td>VGG13</td><td>WRN-40-2</td><td>WRN-40-2</td><td>ResNet56</td><td>ResNet110</td><td>ResNet110</td></tr><tr><td rowspan="3">Student</td><td>79.42</td><td>74.64</td><td>75.61</td><td>75.61</td><td>72.34</td><td>74.31</td><td>74.31</td></tr><tr><td>ResNet8×4</td><td>VGG8</td><td>WRN-40-1</td><td>WRN-16-2</td><td>ResNet20</td><td>ResNet32</td><td>ResNet20</td></tr><tr><td>72.50</td><td>70.36</td><td>71.98</td><td>73.26</td><td>69.06</td><td>71.14</td><td>69.06</td></tr><tr><td rowspan="8">Feature</td><td>FitNet [31]</td><td>73.50</td><td>71.02</td><td>72.24</td><td>73.58</td><td>69.21</td><td>71.06</td><td>68.99</td></tr><tr><td>AT [46]</td><td>73.44</td><td>71.43</td><td>72.77</td><td>74.08</td><td>70.55</td><td>72.31</td><td>70.65</td></tr><tr><td>RKD [29]</td><td>71.90</td><td>71.48</td><td>72.22</td><td>73.35</td><td>69.61</td><td>71.82</td><td>69.25</td></tr><tr><td>CRD [37]</td><td>75.51</td><td>73.94</td><td>74.14</td><td>75.48</td><td>71.16</td><td>73.48</td><td>71.46</td></tr><tr><td>OFD [12]</td><td>74.95</td><td>73.95</td><td>74.33</td><td>75.24</td><td>70.98</td><td>73.23</td><td>71.29</td></tr><tr><td>ReviewKD [5]</td><td>75.63</td><td>74.84</td><td>75.09</td><td>76.12</td><td>71.89</td><td>73.89</td><td>71.34</td></tr><tr><td>SimKD [4]</td><td>78.08</td><td>74.89</td><td>74.53</td><td>75.53</td><td>71.05</td><td>73.92</td><td>71.06</td></tr><tr><td>CAT-KD [10]</td><td>76.91</td><td>74.65</td><td>74.82</td><td>75.60</td><td>71.62</td><td>73.62</td><td>71.37</td></tr><tr><td rowspan="12">Logit</td><td>KD [13]</td><td>73.33</td><td>72.98</td><td>73.54</td><td>74.92</td><td>70.66</td><td>73.08</td><td>70.67</td></tr><tr><td>KD+Ours</td><td>76.62</td><td>74.36</td><td>74.37</td><td>76.11</td><td>71.43</td><td>74.17</td><td>71.48</td></tr><tr><td>Δ</td><td>3.29</td><td>1.38</td><td>0.83</td><td>1.19</td><td>0.77</td><td>1.09</td><td>0.81</td></tr><tr><td>KD+CTKD [24]</td><td>73.39</td><td>73.52</td><td>73.93</td><td>75.45</td><td>71.19</td><td>73.52</td><td>70.99</td></tr><tr><td>KD+CTKD+Ours</td><td>76.67</td><td>74.47</td><td>74.58</td><td>76.08</td><td>71.34</td><td>74.01</td><td>71.39</td></tr><tr><td>Δ</td><td>3.28</td><td>0.95</td><td>0.65</td><td>0.63</td><td>0.15</td><td>0.49</td><td>0.40</td></tr><tr><td>DKD [50]</td><td>76.32</td><td>74.68</td><td>74.81</td><td>76.24</td><td>71.97</td><td>74.11</td><td>71.06</td></tr><tr><td>DKD+Ours</td><td>77.01</td><td>74.81</td><td>74.89</td><td>76.39</td><td>72.32</td><td>74.29</td><td>71.85</td></tr><tr><td>Δ</td><td>0.69</td><td>0.13</td><td>0.08</td><td>0.15</td><td>0.35</td><td>0.18</td><td>0.79</td></tr><tr><td>MLKD [50]</td><td>77.08</td><td>75.18</td><td>75.35</td><td>76.63</td><td>72.19</td><td>74.11</td><td>71.89</td></tr><tr><td>MLKD+Ours</td><td>78.28</td><td>75.22</td><td>75.56</td><td>76.95</td><td>72.33</td><td>74.32</td><td>72.27</td></tr><tr><td>Δ</td><td>1.20</td><td>0.04</td><td>0.21</td><td>0.32</td><td>0.14</td><td>0.21</td><td>0.38</td></tr></table>

Table 3. The top-1 and top-5 accuracy (\%) on the ImageNet validation set [32]. The best and second best results are emphasized in bold and underlined.   

<table><tr><td>Teacher/Student</td><td colspan="2">ResNet34/ResNet18</td><td colspan="2">ResNet50/MN-V1</td></tr><tr><td>Accuracy</td><td>top-1</td><td>top-5</td><td>top-1</td><td>top-5</td></tr><tr><td>Teacher</td><td>73.31</td><td>91.42</td><td>76.16</td><td>92.86</td></tr><tr><td>Student</td><td>69.75</td><td>89.07</td><td>68.87</td><td>88.76</td></tr><tr><td>AT [46]</td><td>70.69</td><td>90.01</td><td>69.56</td><td>89.33</td></tr><tr><td>OFD [12]</td><td>70.81</td><td>89.98</td><td>71.25</td><td>90.34</td></tr><tr><td>CRD [37]</td><td>71.17</td><td>90.13</td><td>71.37</td><td>90.41</td></tr><tr><td>ReviewKD [5]</td><td>71.61</td><td>90.51</td><td>72.56</td><td>91.00</td></tr><tr><td>SimKD [4]</td><td>71.59</td><td>90.48</td><td>72.25</td><td>90.86</td></tr><tr><td>CAT-KD [10]</td><td>71.26</td><td>90.45</td><td>72.24</td><td>91.13</td></tr><tr><td>KD [13]</td><td>71.03</td><td>90.05</td><td>70.50</td><td>89.80</td></tr><tr><td>KD+Ours</td><td>71.42+0.39</td><td>90.29+0.24</td><td>72.18+1.68</td><td>90.80+1.00</td></tr><tr><td>KD+CTKD [24]</td><td>71.38</td><td>90.27</td><td>71.16</td><td>90.11</td></tr><tr><td>KD+CTKD+Ours</td><td>71.81+0.43</td><td>90.46+0.19</td><td>72.92+1.76</td><td>91.25+1.14</td></tr><tr><td>DKD [50]</td><td>71.70</td><td>90.41</td><td>72.05</td><td>91.05</td></tr><tr><td>DKD+Ours</td><td>71.88+0.18</td><td>90.58+0.17</td><td>72.85+0.80</td><td>91.23+0.18</td></tr><tr><td>MLKD [17]</td><td>71.90</td><td>90.55</td><td>73.01</td><td>91.42</td></tr><tr><td>MLKD+Ours</td><td>72.08+0.18</td><td>90.74+0.19</td><td>73.22+0.21</td><td>91.59+0.17</td></tr></table>

# 5.2. Extensions

Logit range. We plot a bar plot in the first row of Fig. 3 to show an example of logit range. The second row of Fig. 3 illustrates the extent of average logit difference between teacher and student. Without applying our pre-process, the student fails to produce as large logit as the teacher at the target label index (7.5 v.s. 12). The mean average distance between the teacher and student logits also reaches 0.27. The restriction of logit range impedes the student to predict

![](images/c5380657e0728e0b1073f92b5a5b9a0cb8e76b35a4950b3ac6a547b60d5b4de3.jpg)

![](images/c8c5f13135044b92dec87fca7241533a612ab163d50e99a89eb79b8a175eb0da.jpg)  
(a) Vanilla KD (b) Ours w/o $\mathcal{Z}$ -score (c) Ours w/ $\mathcal{Z}$ -score Mean: 0.27, Max: 3.03. Mean: 0.94, Max: 7.36. Mean: 0.18, Max:1.18.   
Figure 3. 1st Row: An example bar plot of logit output. 2nd Row: The heatmap of the average logit difference between the teacher and student. Our pre-process indeed enables the student to generate the logits of divergent range from the teacher as shown in 3b, while its standardized logits (3c) are more closer to the teacher's than vanilla KD (3a).

correctly. In contrast, our pre-process breaks the restriction and enables student to generate the logits of appropriate range for itself. Its effective logit output after standardization on the contrary matches the teacher's nicely. The mean distance of standardized logits also shrinks to 0.18, implying its better mimicking the teacher.

Logit variance. As illustrated in the first row of Fig. 3, the vanilla KD forces the variance of the student logits approaches the teacher's (3.78 v.s. 3.10). However, our preprocess breaks the shackle and the student logit can have flexible logit variance (0.48 v.s. 3.10), while its standard

![](images/4d1b66316bae754f4e57c931274b51fc58514b953975904862aaf9fc35307272.jpg)  
(a) Teacher

![](images/825c380f3b506141d5668f2a3e32e58ba6df3b761d8e8016c6502849862f2653.jpg)

![](images/c45b748ce80d552d64edb3c1c410aab3142ee2d6ca1b5378cf1b0ebde284b865.jpg)  
(b) KD [13]

![](images/27e6286316eaa630ad9ffdac1a076e1605e1cc2f0f42240ce87a9280f9a05c6a.jpg)

![](images/41fe8efb5dbd1d966f51ead67e78a582a6780de459c5a073f543cc86bfe6feb7.jpg)

![](images/d734408b613c4380fed8e478f0b4a77defbac83358456dbea181e1ba46bf0c44.jpg)

![](images/8fa9a1a90a89d3b3e862c44e3c7189619c5e7bd5a44c961168b2496831e56b4b.jpg)

![](images/bdabb6f81fd9c8e67cfa566adb22fccd973afe8745e66f26aefed5db0491520a.jpg)

![](images/31ddb3d25a6f2b2134d5bacce4c435fa8ee83d0354cb4652a1e362ff88e73571.jpg)  
(e) MLKD [17]

(c)CTKD [24]

(d) DKD [50]

![](images/732c851efdb057a1ad5246d6a05b23101af7ba30ed12989ed6c4e7602ed614ef.jpg)  
Figure 4. The t-SNE [40] visualization of features. The teacher and student are ResNet $32 \times 4$ and ResNet $8 \times 4$ .

![](images/4395bfac863b080a3a357fa47ee4e6fcdb115f828a42d864623a614a959df4da.jpg)  
(a) Teacher models of different sizes   
(b) Teacher and student distilled by KD only and KD with our pre-process   
Figure 5. The bivariate histogram of logit mean and logit standard deviation for multiple models on CIFAR-100.

ized logits have the same variance as the teacher (both 0.99). Feature visualizations of deep representations are shown in Fig. 4. As implied, our pre-process improves the feature separability and discriminability of all the methods including KD [13], CTKD [24], DKD [50] and MLKD [17].

Improving distillation for large teacher. Existing works [7, 41, 50] observe that a larger teacher is unnecessarily a better one. The phenomenon implies that the transfer of knowledge from a large teacher is not always as smooth as a small one. They explain the observation with the existence of a capacity gap between cumbersome teachers and lightweight students. We interpret the issue as the difficulty of students in mimicking logits of comparable range and variance as teachers. As shown in the bivariate histogram of Fig. 5a, the bigger teachers like ResNet50 and VGG13 generates more condensed logits of mean closer to zero and smaller standard deviation. The tendency shows that smaller models intrinsically predicts the outputs of larger bias from zero mean and larger variance. Therefore, when students are small, the same tendency remains and they are difficult to produce as compact logits as large teachers.

We alleviate the problem by our pre-process. As shown in Tab. 5, our pre-process consistently improves the distillation performance for various teachers of different sizes and capacities. We also show the mimicking goodness of students by a bivariate histogram plot in Fig. 5b. The student

Table 4. The ablation studies under different settings in our $\mathcal{Z}$ -score. The base temperature $\tau$ is set to be 2. By default $\lambda_{\mathrm{CE}} = 0.1$ . The logit vector of teacher $\mathbf{v}_n$ and student $\mathbf{z}_n$ are abbreviated as $\mathbf{z}$ for succinctness. The teacher and student are ResNet $32 \times 4$ and ResNet $8 \times 4$ .

<table><tr><td>λKD</td><td>z (KD)</td><td>z - \(\overline{z}\)</td><td>\(\frac{z}{\sigma(z)}\)</td><td>\(\frac{(z-\overline{z})}{\sigma(z)}\) (Ours)</td></tr><tr><td>0.9</td><td>73.60</td><td>73.37</td><td>73.79</td><td>74.14</td></tr><tr><td>3.0</td><td>74.38</td><td>74.33</td><td>75.86</td><td>76.11</td></tr><tr><td>6.0</td><td>74.45</td><td>74.82</td><td>76.44</td><td>76.56</td></tr><tr><td>9.0</td><td>73.33</td><td>73.94</td><td>76.30</td><td>76.62</td></tr><tr><td>12.0</td><td>68.29</td><td>71.56</td><td>76.49</td><td>76.56</td></tr><tr><td>15.0</td><td>65.34</td><td>62.01</td><td>76.42</td><td>76.61</td></tr><tr><td>18.0</td><td>63.45</td><td>61.31</td><td>76.18</td><td>76.33</td></tr></table>

Table 5. The results of distillation of various teacher models on CIFAR-100. The student model is WRN-16-2.   

<table><tr><td>Teacher</td><td>VGG13 74.64</td><td>W-28-2 75.45</td><td>W-40-2 75.61</td><td>W-16-4 77.51</td><td>W-28-4 78.60</td><td>ResNet50 79.34</td></tr><tr><td>KD [13]</td><td>74.93</td><td>75.37</td><td>74.92</td><td>75.79</td><td>75.04</td><td>75.36</td></tr><tr><td>KD+Ours</td><td>75.03</td><td>76.32</td><td>76.11</td><td>76.72</td><td>75.77</td><td>76.24</td></tr><tr><td>DKD [50]</td><td>75.45</td><td>75.92</td><td>76.24</td><td>76.00</td><td>76.45</td><td>76.60</td></tr><tr><td>DKD+Ours</td><td>75.56</td><td>76.39</td><td>76.39</td><td>76.68</td><td>76.67</td><td>76.82</td></tr></table>

distilled by vanilla KD predicts logits apparently deviated from teachers' in terms of logit mean and standard deviation. In contrast, our pre-process enables the student to perfectly matching the teacher in terms of standardized logit mean and standard deviation (see the zoomed-in region at bottom right corner).

More experiments of distilling vision Transformers [6, 20, 21, 38, 42] are attached in the supplements.

# 6. Conclusion

In this work, we identify a lack of theoretical support for the global and shared temperature in conventional KD pipelines. Our analysis based on the principle of entropy maximization leads to the conclusion that the temperature is derived from a flexible Lagrangian multiplier, allowing for a flexible value assignment. We then highlight several drawbacks associated with the conventional practice of sharing temperatures between teachers and students. Additionally, we presented a toy case where the KD pipeline with shared temperature led to an inauthentic evaluation of student performance. To mitigate the concerns, we propose a logit $\mathcal{Z}$ -score standardization as a pre-process to enable student to focus on the innate relations of teacher logits rather than logit magnitude. The extensive experiments demonstrate the effectiveness of our pre-process in enhancing the existing logit-based KD methods.

Acknowledgements. This work has been supported in part by National Natural Science Foundation of China (No. 62322216, 62025604, 62306308), in part by Shenzhen Science and Technology Program (Grant No. JCYJ20220818102012025, KQTD20221101093559018).

# References

[1] Sungsoo Ahn, Shell Xu Hu, Andreas Damianou, Neil D Lawrence, and Zhenwen Dai. Variational information distillation for knowledge transfer. In CVPR, 2019. 2   
[2] Keshigeyan Chandrasegaran, Ngoc-Trung Tran, Yunqing Zhao, and Ngai-Man Cheung. Revisiting label smoothing and knowledge distillation compatibility: What was missing? In ICML, 2022. 2   
[3] Defang Chen, Jian-Ping Mei, Can Wang, Yan Feng, and Chun Chen. Online knowledge distillation with diverse peers. In AAAI, 2020. 2   
[4] Defang Chen, Jian-Ping Mei, Hailin Zhang, Can Wang, Yan Feng, and Chun Chen. Knowledge distillation with the reused teacher classifier. In CVPR, 2022. 2, 6, 7   
[5] Pengguang Chen, Shu Liu, Hengshuang Zhao, and Jiaya Jia. Distilling knowledge via knowledge review. In CVPR, 2021. 2, 6, 7   
[6] Xianing Chen, Qiong Cao, Yujie Zhong, Jing Zhang, Shenghua Gao, and Dacheng Tao. Dearkd: Data-efficient early knowledge distillation for vision transformers. In CVPR, 2022. 8   
[7] Jang Hyun Cho and Bharath Hariharan. On the efficacy of knowledge distillation. In ICCV, 2019. 2, 4, 8   
[8] Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q Weinberger. On calibration of modern neural networks. In ICML, 2017. 3   
[9] Jia Guo. Reducing the teacher-student gap via adaptive temperatures, 2022. 2, 5   
[10] Ziyao Guo, Haonan Yan, Hui Li, and Xiaodong Lin. Class attention transfer based knowledge distillation. In CVPR, 2023. 2, 6, 7   
[11] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. In CVPR, 2016. 6   
[12] Byeongho Heo, Jeesoo Kim, Sangdoo Yun, Hyojin Park, No-jun Kwak, and Jin Young Choi. A comprehensive overhaul of feature distillation. In ICCV, 2019. 2, 6, 7   
[13] Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. Distilling the knowledge in a neural network. arXiv preprint arXiv:1503.02531, 2015. 1, 2, 5, 6, 7, 8   
[14] Andrew G Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang, Tobias Weyand, Marco Andreetto, and Hartwig Adam. Mobilenets: Efficient convolutional neural networks for mobile vision applications. arXiv preprint arXiv:1704.04861, 2017. 6   
[15] Tao Huang, Shan You, Fei Wang, Chen Qian, and Chang Xu. Knowledge distillation from a stronger teacher. NeurIPS, 2022. 2, 4   
[16] Edwin T Jaynes. Information theory and statistical mechanics. Physical review, 106(4):620, 1957. 3

[17] Ying Jin, Jiaqi Wang, and Dahua Lin. Multi-level logit distillation. In CVPR, 2023. 2, 6, 7, 8   
[18] Alex Krizhevsky, Geoffrey Hinton, et al. Learning multiple layers of features from tiny images. 2009. 2, 5, 6, 7   
[19] Gang Li, Xiang Li, Yujie Wang, Shanshan Zhang, Yichao Wu, and Ding Liang. Knowledge distillation for object detection via rank mimicking and prediction-guided feature imitation. In AAAI, 2022. 2   
[20] Kehan Li, Runyi Yu, Zhennan Wang, Li Yuan, Guoli Song, and Jie Chen. Locality guidance for improving vision transformers on tiny datasets. In ECCV, 2022. 8   
[21] Lujun Li, Peijie Dong, Zimian Wei, and Ya Yang. Automated knowledge distillation via monte carlo tree search. In ICCV, 2023. 8   
[22] Zheng Li, Ying Huang, Defang Chen, Tianren Luo, Ning Cai, and Zhigeng Pan. Online knowledge distillation via multi-branch diversity enhancement. In ACCV, 2020. 2   
[23] Zheng Li, Jingwen Ye, Mingli Song, Ying Huang, and Zhi-geng Pan. Online knowledge distillation for efficient pose estimation. In ICCV, 2021. 2   
[24] Zheng Li, Xiang Li, Lingfeng Yang, Borui Zhao, Renjie Song, Lei Luo, Jun Li, and Jian Yang. Curriculum temperature for knowledge distillation. In AAAI, 2023. 2, 6, 7, 8   
[25] Sihao Lin, Hongwei Xie, Bing Wang, Kaicheng Yu, Xiaojun Chang, Xiaodan Liang, and Gang Wang. Knowledge distillation via the target-aware transformer. In CVPR, 2022. 2   
[26] Jihao Liu, Boxiao Liu, Hongsheng Li, and Yu Liu. Meta knowledge distillation. arXiv preprint arXiv:2202.07940, 2022.2   
[27] Yifan Liu, Ke Chen, Chris Liu, Zengchang Qin, Zhenbo Luo, and Jingdong Wang. Structured knowledge distillation for semantic segmentation. In CVPR, 2019. 2   
[28] Seyed Iman Mirzadeh, Mehrdad Farajtabar, Ang Li, Nir Levine, Akihiro Matsukawa, and Hassan Ghasemzadeh. Improved knowledge distillation via teacher assistant. In AAAI, 2020. 2, 4   
[29] Wonpyo Park, Dongju Kim, Yan Lu, and Minsu Cho. Relational knowledge distillation. In CVPR, 2019. 2, 6, 7   
[30] Baoyun Peng, Xiao Jin, Jiaheng Liu, Dongsheng Li, Yichao Wu, Yu Liu, Shunfeng Zhou, and Zhaoning Zhang. Correlation congruence for knowledge distillation. In ICCV, 2019. 2, 6   
[31] Adriana Romero, Nicolas Ballas, Samira Ebrahimi Kahou, Antoine Chassang, Carlo Gatta, and Yoshua Bengio. Fitnets: Hints for thin deep nets. *ICLR*, 2015. 2, 6, 7   
[32] Olga Russakovsky, Jia Deng, Hao Su, Jonathan Krause, Sanjeev Satheesh, Sean Ma, Zhiheng Huang, Andrej Karpathy, Aditya Khosla, Michael Bernstein, et al. Imagenet large scale visual recognition challenge. IJCV, 2015. 2, 5, 6, 7   
[33] Mark Sandler, Andrew Howard, Menglong Zhu, Andrey Zh-moginov, and Liang-Chieh Chen. Mobilenetv2: Inverted residuals and linear bottlenecks. In CVPR, 2018. 6   
[34] Karen Simonyan and Andrew Zisserman. Very deep convolutional networks for large-scale image recognition. arXiv preprint arXiv:1409.1556, 2014. 6   
[35] Wonchul Son, Jaemin Na, Junyong Choi, and Wonjun Hwang. Densely guided knowledge distillation using multiple teacher assistants. In ICCV, 2021. 2, 4

[36] Ilya Sutskever, James Martens, George Dahl, and Geoffrey Hinton. On the importance of initialization and momentum in deep learning. In ICML, 2013. 6   
[37] Yonglong Tian, Dilip Krishnan, and Phillip Isola. Contrastive representation distillation. *ICLR*, 2020. 2, 6, 7   
[38] Hugo Touvron, Matthieu Cord, Matthijs Douze, Francisco Massa, Alexandre Sablayrolles, and Herve Jegou. Training data-efficient image transformers & distillation through attention. In ICML, 2021. 8   
[39] Frederick Tung and Greg Mori. Similarity-preserving knowledge distillation. In ICCV, 2019. 2   
[40] Laurens Van der Maaten and Geoffrey Hinton. Visualizing data using t-sne. JMLR, 2008. 8   
[41] Lin Wang and Kuk-Jin Yoon. Knowledge distillation and student-teacher learning for visual intelligence: A review and new outlooks. IEEE TPAMI, 2021. 8   
[42] Kan Wu, Jinnian Zhang, Houwen Peng, Mengchen Liu, Bin Xiao, Jianlong Fu, and Lu Yuan. Tinyvit: Fast pretraining distillation for small vision transformers. In ECCV, 2022. 8   
[43] Jing Yang, Brais Martinez, Adrian Bulat, Georgios Tzimiropoulos, et al. Knowledge distillation via softmax regression representation learning. In ICLR, 2021. 2   
[44] Junho Yim, Donggyu Joo, Jihoon Bae, and Junmo Kim. A gift from knowledge distillation: Fast optimization, network minimization and transfer learning. In CVPR, 2017. 2   
[45] Sergey Zagoruyko and Nikos Komodakis. Wide residual networks. arXiv preprint arXiv:1605.07146, 2016. 6   
[46] Sergey Zagoruyko and Nikos Komodakis. Paying more attention to attention: Improving the performance of convolutional neural networks via attention transfer. *ICLR*, 2017. 6, 7   
[47] Rongzhi Zhang, Jiaming Shen, Tianqi Liu, Jialu Liu, Michael Bendersky, Marc Najork, and Chao Zhang. Do not blindly imitate the teacher: Using perturbed loss for knowledge distillation. arXiv preprint arXiv:2305.05010, 2023. 2   
[48] Xiangyu Zhang, Xinyu Zhou, Mengxiao Lin, and Jian Sun. Shufflenet: An extremely efficient convolutional neural network for mobile devices. In CVPR, 2018. 6   
[49] Ying Zhang, Tao Xiang, Timothy M Hospedales, and Huchuan Lu. Deep mutual learning. In CVPR, 2018. 2   
[50] Borui Zhao, Quan Cui, Renjie Song, Yiyu Qiu, and Jiajun Liang. Decoupled knowledge distillation. In CVPR, 2022, 2, 6, 7, 8