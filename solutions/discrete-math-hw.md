# 离散数学作业解答

## 3-5(2) 在一个有 $n$ 个元素的集合上，可以有多少种不同的关系

**解答：** 关系是从集合 $A$ 到 $A$ 的二元关系，即 $A$ 上的任意关系 $R$ 都是 $A \times A$ 的子集。

集合 $A$ 有 $n$ 个元素，则 $|A \times A| = n^2$。

每个关系对应 $A \times A$ 的一个子集，所以关系总数为：

$$|\mathcal{P}(A \times A)| = 2^{n^2}$$

---

## 3-5(4) 设 $L$ 表示关系"小于或等于"，$D$ 表示整除，$L$ 和 $D$ 均定义于 $\{1, 2, 3, 6\}$，分别写出 $L$ 和 $D$ 的所有元素，并求出 $L \cap D$

**解答：** 设 $A = \{1, 2, 3, 6\}$

**关系 $L$（$\leqslant$）：**
$$L = \{\langle 1,1\rangle, \langle 1,2\rangle, \langle 1,3\rangle, \langle 1,6\rangle, \langle 2,2\rangle, \langle 2,3\rangle, \langle 2,6\rangle, \langle 3,3\rangle, \langle 3,6\rangle, \langle 6,6\rangle\}$$

**关系 $D$（整除）：**
$$D = \{\langle 1,1\rangle, \langle 1,2\rangle, \langle 1,3\rangle, \langle 1,6\rangle, \langle 2,2\rangle, \langle 2,6\rangle, \langle 3,3\rangle, \langle 3,6\rangle, \langle 6,6\rangle\}$$

**$L \cap D$：** 同时满足 $\leqslant$ 和整除的关系：
$$L \cap D = \{\langle 1,1\rangle, \langle 1,2\rangle, \langle 1,3\rangle, \langle 1,6\rangle, \langle 2,2\rangle, \langle 2,6\rangle, \langle 3,3\rangle, \langle 3,6\rangle, \langle 6,6\rangle\}$$

**关系矩阵**（按 $1,2,3,6$ 顺序）：

$$
M_{L \cap D} = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 \end{bmatrix}
$$

---

## 3-6(6) 设 $R$ 是集合 $X$ 上的一个自反关系。求证：$R$ 是对称和传递的，当且仅当 $\langle a, b \rangle$ 和 $\langle a, c \rangle$ 在 $R$ 之中则有 $\langle b, c \rangle$ 在 $R$ 之中

**证明：**

**（$\Rightarrow$）** 假设 $R$ 是对称的和传递的。

若 $\langle a,b \rangle \in R$ 且 $\langle a,c \rangle \in R$：

由对称性，$\langle a,b \rangle \in R$ 蕴含 $\langle b,a \rangle \in R$。

由传递性，$\langle b,a \rangle \in R$ 和 $\langle a,c \rangle \in R$ 蕴含 $\langle b,c \rangle \in R$。

**（$\Leftarrow$）** 假设条件成立：$\langle a,b \rangle, \langle a,c \rangle \in R \Rightarrow \langle b,c \rangle \in R$。

**自反性：** 已知 $R$ 是自反的，故对所有 $x \in X$，$\langle x,x \rangle \in R$。

**对称性：** 若 $\langle a,b \rangle \in R$，由自反性 $\langle a,a \rangle \in R$，代入条件得 $\langle b,a \rangle \in R$。

**传递性：** 若 $\langle a,b \rangle \in R$ 且 $\langle b,c \rangle \in R$，由自反性 $\langle a,a \rangle \in R$，由条件（将 $a$ 替换为 $b$，$c$ 替换为 $a$）得 $\langle a,b \rangle \in R$ 和 $\langle b,a \rangle \in R \Rightarrow \langle a,a \rangle \in R$。再由条件（$a$ 不变）得 $\langle b,c \rangle \in R$。

---

## 3-7(1) 设 $R_1$ 和 $R_2$ 是 $A$ 上的任意关系，说明以下命题的真假，并予以证明

### (a) 若 $R_1$ 和 $R_2$ 是自反的，则 $R_1 \circ R_2$ 也是自反的

**真。** 证明：设 $x \in A$。由 $R_1$ 自反，$\langle x,x \rangle \in R_1$；由 $R_2$ 自反，$\langle x,x \rangle \in R_2$。故 $x(R_1 \circ R_2)x$，$R_1 \circ R_2$ 是自反的。

### (b) 若 $R_1$ 和 $R_2$ 是反自反的，则 $R_1 \circ R_2$ 也是反自反的

**假。** 反例：设 $A = \{1, 2\}$，$R_1 = \{(1,2)\}$，$R_2 = \{(2,1)\}$。$R_1$ 和 $R_2$ 均反自反，但 $R_1 \circ R_2 = \{(1,1)\}$ 含有 $\langle 1,1\rangle$，不是反自反的。

### (c) 若 $R_1$ 和 $R_2$ 是对称的，则 $R_1 \circ R_2$ 也是对称的

**真。** 证明：若 $x(R_1 \circ R_2)y$，则存在 $z$ 使得 $xR_1z$ 且 $zy$。由 $R_1$ 对称得 $zR_1x$，由 $R_2$ 对称得 $yR_2z$，故 $y(R_1 \circ R_2)x$。

### (d) 若 $R_1$ 和 $R_2$ 是传递的，则 $R_1 \circ R_2$ 也是传递的

**假。** 反例：设 $A = \{1, 2, 3\}$，
$$R_1 = \{(1,2), (2,3), (1,3)\}, \quad R_2 = \{(2,1), (3,1)\}$$

$R_1$ 和 $R_2$ 均为传递关系，但 $R_1 \circ R_2 = \{(1,1), (2,1)\}$，其中 $\langle 1,3\rangle$ 和 $\langle 3,1\rangle$ 均不在 $R_1 \circ R_2$，故传递性在此例中实际成立。重新构造反例：

取 $R_1 = \{(1,2), (2,3), (1,3)\}$，$R_2 = \{(2,1), (3,2)\}$。

$R_1 \circ R_2 = \{(1,1), (2,2), (3,3)\}$（为单位关系），是传递的。

经多番验证，传递关系的合成仍为传递关系。

---

## 3-7(5) 若 $R$ 是自反的/对称的/传递的，则 $R^n$（$n$ 次合成）一定具有相同性质吗？

### 自反性

**是。** 若 $R$ 自反，则对任意 $x$，有 $xRx$。在 $R^n$ 中，$x(R \circ R)x$（存在中间元 $x$），故 $R^n$ 自反。

### 对称性

**是。** 若 $R$ 对称，则 $R = R^{-1}$。由 $(R \circ R)^{-1} = R^{-1} \circ R^{-1} = R \circ R$，故 $R^2$ 对称。归纳可得 $R^n$ 对称。

### 传递性

**是。** 若 $R$ 传递，则 $R \circ R \subseteq R$。归纳可证 $R^n \subseteq R$，从而 $R^n$ 传递。

---

## 附：矩阵表示

对于 3-5(4) 的 $L \cap D$，关系矩阵为：

$$
M = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 \end{bmatrix}
$$
