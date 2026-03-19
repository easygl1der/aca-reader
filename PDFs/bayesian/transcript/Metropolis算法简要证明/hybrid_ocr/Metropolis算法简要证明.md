# Metropolis算法简要证明

# Metropolis算法

目的：从 $f(x)$ 中抽取样本

方法：用迭代算法生成随机变量序列（马尔可夫链）

要求：建议分布需要对称

# 步骤

1. 给定 $x^{t - 1}$ , 从建议分布 $J(x^{t} \mid x^{t - 1})$ 中抽取样本, 并记为 $x^{*}$   
2. 计算 $r = \frac{f(x^{*})}{f(x^{t - 1})}$ , 并从 $U[0,1]$ 中抽取 $u$   
3. 若 $u \leq \min \{r, 1\}$ , 则令 $x^{t} = x^{*}$ ; 否则令 $x^{t} = x^{t - 1}$

# 问题

1. 按以上方法得到的随机变量序列收敛，即存在平稳分布。（此问题由随机过程可证。）  
2. 平稳分布为 $f$ , 即随机变量序列的平稳分布为目标分布。

# 记号

- 马尔科夫链（Markov chain）： $X_{1}, X_{2}, \ldots, X_{t}, X_{t+1}, \ldots$   
- 转移函数（transition kernel）：

$$
T (b | a) \doteq P (X _ {t + 1} = b | X _ {t} = a) \doteq f _ {X _ {t + 1} | X _ {t}} (b | a)
$$

从 $X_{t} = a$ 转移到 $X_{t + 1} = b$ 的概率, 或  
$\bullet$ 给定 $X_{t} = a$ 时 $X_{t + 1} = b$ 的条件密度

# 定义

若 $T$ 对某一（密度）函数 $f$ 满足：对任意 $a$ 和 $b$ ，有

$$
T (b | a) \times f (a) = T (a | b) \times f (b),
$$

则称 $T$ 满足平衡条件（detailed balanced condition）。

# 引理

对于马尔科夫链 $X_{1}, X_{2}, \ldots, X_{t}, X_{t+1}, \ldots$ , $T$ 为该马尔科夫链的转移函数。若 $T$ 满足平衡条件（detailed balanced condition），则对应的密度函数 $f$ 为该马氏链的平稳分布。

# 证明

设 $X_{t}$ 的密度函数为 $f_{X_{t}}$ 。对任意 $a$ 和 $b$ , 有

$$
\begin{array}{l} f _ {X _ {t + 1}, X _ {t}} (b, a) = f _ {X _ {t + 1} | X _ {t}} (b | a) \times f _ {X _ {t}} (a) \doteq T (b | a) \times f _ {X _ {t}} (a) \\ = T (a | b) \times f _ {X _ {t}} (b) \doteq f _ {X _ {t + 1} | X _ {t}} (a | b) \times f _ {X _ {t}} (b) = f _ {X _ {t + 1}, X _ {t}} (a, b) 。 \\ \end{array}
$$

# 证明

$$
\begin{array}{l} f _ {X _ {t + 1}} (b) = \int f _ {X _ {t + 1}, X _ {t}} (b, a) d a = \int f _ {X _ {t + 1}, X _ {t}} (a, b) d a \\ = \int f _ {X _ {t + 1} | X _ {t}} (a | b) \times f _ {X _ {t}} (b) d a = f _ {X _ {t}} (b) \times \int f _ {X _ {t + 1} | X _ {t}} (a | b) d a = f _ {X _ {t}} (b) \circ \\ \end{array}
$$

可见 $f_{X_{t + 1}}(b) = f_{X_t}(b)$ 对任意 $b$ 成立，即 $X_{t + 1}$ 的密度函数仍为 $f_{X_t}$ ，故 $f_{X_t}$ 为平稳分布。

# 定理

Metropolis算法所提出的 $T$ 满足密度函数为目标分布 $f$ 的平衡条件。

# 证明

对任意 $a$ 和 $b$ , 有

$$
\begin{array}{l} T (b | a) \times f (a) = J (b | a) \times \min \{r, 1 \} \times f (a) \\ = J (b | a) \times \min \left\{\frac {f (b)}{f (a)}, 1 \right\} \times f (a) = J (b | a) \times \min \{f (b), f (a) \}. \\ \end{array}
$$

# 证明

$$
\begin{array}{l} T (a | b) \times f (b) = J (a | b) \times \min  \{r, 1 \} \times f (b) \\ = J (a | b) \times \min \left\{\frac {f (a)}{f (b)}, 1 \right\} \times f (b) = J (a | b) \times \min \{f (a), f (b) \}. \\ \end{array}
$$

# 证明

- $T(b \mid a) \times f(a) = J(b \mid a) \times \min \{f(b), f(a)\}$ ;   
$T(a|b) \times f(b) = J(a|b) \times \min \{f(a), f(b)\}$ ;   
$\cdot J(b \mid a) = J(a \mid b)$ ;   
- $T(b \mid a) \times f(a) = T(a \mid b) \times f(b)$ （满足平衡条件）

# 注

$\bullet$ Metropolis算法中要求 $J(b \mid a) = J(a \mid b)$ , 即建议分布为对称。   
- Metropolis-Hastings算法对Metropolis算法进行推广，不再要求

建议分布对称，接收概率为 $r = \frac{f(x^{*})}{f(x^{t - 1})} \times \frac{J(x^{t - 1} | x^{*})}{J(x^{*} | x^{t - 1})}$ 。

# 思考

1. 写出Metropolis-Hastings算法的转移函数 $T$ 。  
2. 根据以上证明思路证明: Metropolis-Hastings算法的转移函数 $T$ 满足平衡条件。