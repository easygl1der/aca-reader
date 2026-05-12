$$
= \lim _ {N \rightarrow \infty} \prod_ {n = 1} ^ {N} P \{\eta_ {n} \leq m \}
$$

$$
= \lim _ {N \rightarrow \infty} (1 - e ^ {- \lambda m}) ^ {N}
$$

$$
= 0.
$$

It follows that

$$
\begin{array}{l} P \left(\lim _ {n \rightarrow \infty} \xi_ {n} <   \infty\right) \leq P \left(\bigcup_ {m = 1} ^ {\infty} \bigcap_ {n = 1} ^ {\infty} \{\eta_ {n} \leq m \}\right) \\ \leq \sum_ {m = 1} ^ {\infty} P \left(\bigcap_ {n = 1} ^ {\infty} \{\eta_ {n} \leq m \}\right) \\ = 0, \\ \end{array}
$$

completing the proof.

While it is instructive to work through the above estimates, there exists a much more elegant argument. By the strong law of large numbers

$$
\lim _ {n \rightarrow \infty} \frac {\xi_ {n}}{n} = \frac {1}{\lambda} \quad \text { a   .   s   . }
$$

Here $\frac{1}{\lambda}$ is the expectation of each of the independent identically distributed random variables $\eta_{n}$ (see Exercise 6.2). It follows that

$$
\lim _ {n \rightarrow \infty} \xi_ {n} = \infty \quad \text { a   .   s   . },
$$

as required.

# Solution 6.15

In the proof of Proposition 6.1 it was shown that

$$
P \left\{\xi_ {n} > t \right\} = e ^ {- \lambda t} \sum_ {k = 0} ^ {n - 1} \frac {(\lambda t) ^ {k}}{k !}
$$

for $t \geq 0$ , see (6.4). Therefore the distribution function

$$
F _ {n} (t) = P \left\{\xi_ {n} \leq t \right\} = 1 - P \left\{\xi_ {n} > t \right\} = e ^ {- \lambda t} \sum_ {k = n} ^ {\infty} \frac {(\lambda t) ^ {k}}{k !}
$$

of $\xi_{n}$ is differentiable, the density $f_{n}$ of $\xi_{n}$ being

$$
\begin{array}{l} f _ {n} (t) = \frac {d}{d t} F _ {n} (t) \\ = - \lambda e ^ {- \lambda t} \sum_ {k = n} ^ {\infty} \frac {(\lambda t) ^ {k}}{k !} + \lambda e ^ {- \lambda t} \sum_ {k = n} ^ {\infty} \frac {(\lambda t) ^ {k - 1}}{(k - 1) !} \\ = \lambda e ^ {- \lambda t} \frac {(\lambda t) ^ {n - 1}}{(n - 1) !} \\ \end{array}
$$

for $t > 0$ , and clearly $f_{n}(t) = 0$ for $t \leq 0$ .

# Solution 6.16

Because $N(t)$ has non-decreasing trajectories

$$
\left\{\lim _ {t \rightarrow \infty} N (t) = \infty \right\} = \bigcap_ {n = 1} ^ {\infty} \bigcup_ {k = 1} ^ {\infty} \{N (k) \geq n \}.
$$

Also, $\{N(k) \geq n\}$ , $k = 1, 2, \ldots$ is an expanding sequence of events and

$$
\begin{array}{l} P \{N (k) \geq n \} = e ^ {- \lambda k} \sum_ {i = n} ^ {\infty} \frac {(\lambda k) ^ {i}}{i !} \\ = 1 - e ^ {- \lambda k} \sum_ {i = 0} ^ {n - 1} \frac {(\lambda k) ^ {i}}{i !} \rightarrow 1 \quad \text { as } k \rightarrow \infty . \\ \end{array}
$$

It follows that

$$
P \left\{\bigcup_ {k = 1} ^ {\infty} \{N (k) \geq n \} \right\} = 1,
$$

so

$$
P \left\{\lim _ {t \rightarrow \infty} N (t) = \infty \right\} = P \left\{\bigcap_ {n = 1} ^ {\infty} \bigcup_ {k = 1} ^ {\infty} \{N (k) \geq n \} \right\} = 1.
$$

# Solution 6.17

Since

$$
\sinh (x) = \frac {e ^ {x} - e ^ {- x}}{2} = \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n + 1}}{(2 n + 1) !},
$$

$$
\cosh (x) = \frac {e ^ {x} + e ^ {- x}}{2} = \sum_ {n = 0} ^ {\infty} \frac {x ^ {2 n}}{(2 n) !},
$$

we have

$$
\begin{array}{l} P \{N (t) \text {   is   odd } \} = \sum_ {n = 0} ^ {\infty} P \{N (t) = 2 n + 1 \} \\ = \sum_ {n = 0} ^ {\infty} e ^ {- \lambda t} \frac {(\lambda t) ^ {2 n + 1}}{(2 n + 1) !} \\ = e ^ {- \lambda t} \sinh (\lambda t), \\ \end{array}
$$

$$
P \{N (t) \text { is   even } \} = \sum_ {n = 0} ^ {\infty} P \{N (t) = 2 n \}
$$

$$
= \sum_ {n = 0} ^ {\infty} e ^ {- \lambda t} \frac {(\lambda t) ^ {2 n}}{(2 n) !}
$$

$$
= e ^ {- \lambda t} \cosh (\lambda t).
$$

# Solution 6.18

We can write

$$
N (n) = N (1) + (N (2) - N (1)) + \dots + (N (n) - N (n - 1)),
$$

where $N(1), N(2) - N(1), N(3) - N(2), \ldots$ is a sequence of independent identically distributed random variables with expectation

$$
E (N (1)) = E (N (2) - N (1)) = E (N (3) - N (2)) = \dots = \lambda .
$$

By the strong law of large numbers

$$
\lim _ {n \rightarrow \infty} \frac {N (n)}{n} = \lambda \quad \text { a.s. } \tag {6.8}
$$

Now, if $n \leq t \leq n + 1$ , then $N(n) \leq N(t) \leq N(n + 1)$ and

$$
\frac {N (n)}{n + 1} \leq \frac {N (t)}{t} \leq \frac {N (n + 1)}{n}.
$$

By (6.8) both sides tend to $\lambda$ as $n\to \infty$ , implying that

$$
\lim _ {t \rightarrow \infty} \frac {N (t)}{t} = \lambda \quad \text { a   .   s   . }
$$

# Solution 6.19

Condition 3) of Definition 6.9 implies that

$$
f _ {W (t)} (x) = p (t, 0, x)
$$

is the density of $W(t)$ . Therefore, integrating by parts, we can compute the expectation

$$
\begin{array}{l} E (W (t)) = \int_ {- \infty} ^ {+ \infty} x p (t, 0, x) d x \\ = \frac {1}{\sqrt {2 \pi t}} \int_ {- \infty} ^ {+ \infty} x e ^ {- \frac {x ^ {2}}{2 t}} d x \\ = - \frac {t}{\sqrt {2 \pi t}} \int_ {- \infty} ^ {+ \infty} \frac {d}{d x} e ^ {- \frac {x ^ {2}}{2 t}} d x \\ = - \frac {t}{\sqrt {2 \pi t}} e ^ {- \frac {s ^ {2}}{2 t}} \Big | _ {- \infty} ^ {+ \infty} = 0 \\ \end{array}
$$

and variance

$$
\begin{array}{l} E \left(\left(W (t)\right) ^ {2}\right) = \int_ {- \infty} ^ {+ \infty} x ^ {2} p (t, 0, x) d x \\ = \frac {1}{\sqrt {2 \pi t}} \int_ {- \infty} ^ {+ \infty} x ^ {2} e ^ {- \frac {\xi^ {2}}{2 i}} d x \\ = - \frac {t}{\sqrt {2 \pi t}} \int_ {- \infty} ^ {+ \infty} x \frac {d}{d x} e ^ {- \frac {x ^ {2}}{2 t}} d x \\ = - \frac {t}{\sqrt {2 \pi t}} x e ^ {- \frac {\pi^ {2}}{2 t}} \left| _ {- \infty} ^ {+ \infty} + \frac {t}{\sqrt {2 \pi t}} \int_ {- \infty} ^ {+ \infty} e ^ {- \frac {\pi^ {2}}{2 t}} d x \right. \\ = 0 + \frac {t}{\sqrt {2 \pi}} \int_ {- \infty} ^ {+ \infty} e ^ {- \frac {u ^ {2}}{2}} d u = t. \\ \end{array}
$$

We have used the substitution $u = \frac{x}{\sqrt{t}}$ and the formula stated in the hint.

# Solution 6.20

Suppose that $s < t$ . Condition 3) of Definition 6.9 implies that the joint density of $W(s)$ and $W(t)$ is

$$
f _ {W (s), W (t)} (x, y) = p (s, 0, x) p (t - s, x, y).
$$

It follows that

$$
\begin{array}{l} E (W (s) W (t)) = \int_ {- \infty} ^ {+ \infty} \int_ {- \infty} ^ {+ \infty} x y p (s, 0, x) p (t - s, x, y) d x d y \\ = \int_ {- \infty} ^ {+ \infty} x p (s, 0, x) \left(\int_ {- \infty} ^ {+ \infty} y p (t - s, x, y) d y\right) d x \\ = \int_ {- \infty} ^ {+ \infty} x ^ {2} p (s, 0, x) d x = s. \\ \end{array}
$$

This is because by the results of Exercise 6.19

$$
\begin{array}{l} \int_ {- \infty} ^ {+ \infty} y p (t - s, x, y) d y = \int_ {- \infty} ^ {+ \infty} (x + u) p (t - s, x, x + u) d u \\ = \int_ {- \infty} ^ {+ \infty} (x + u) p (t - s, 0, u) d u \\ = x \int_ {- \infty} ^ {+ \infty} p (t - s, 0, u) d u + \int_ {- \infty} ^ {+ \infty} u p (t - s, 0, u) d u \\ = x + 0 = x \\ \end{array}
$$

and

$$
\int_ {- \infty} ^ {+ \infty} x ^ {2} p (s, 0, x) d x = s.
$$

It follows that for arbitrary $s, t \geq 0$

$$
E (W (s) W (t)) = \min \{s, t \}.
$$

# Solution 6.21

Suppose that $s \leq t$ . Then by Exercise 6.20

$$
\begin{array}{l} E \left(\left| W (t) - W (s) \right| ^ {2}\right) = E \left(W (t) ^ {2}\right) - 2 E \left(W (s) W (t)\right) + E \left(W (s) ^ {2}\right) \\ = t - 2 s + s = t - s. \\ \end{array}
$$

In general, for arbitrary $s, t \geq 0$

$$
E \left(\left| W (t) - W (s) \right| ^ {2}\right) = | t - s |.
$$

# Solution 6.22

Using the density $f_{W(t)}(x) = p(t,0,x)$ of $W(t)$ , we compute

$$
\begin{array}{l} E \left(\exp (i \lambda W (t))\right) = \int_ {- \infty} ^ {+ \infty} e ^ {i \lambda x} p (t, 0, x) d x \\ = \frac {1}{\sqrt {2 \pi t}} \int_ {- \infty} ^ {+ \infty} e ^ {i \lambda x} e ^ {- \frac {x ^ {2}}{2 t}} d x \\ = \frac {1}{\sqrt {2 \pi t}} e ^ {- \frac {\lambda^ {2} t}{2}} \int_ {- \infty} ^ {+ \infty} e ^ {- \frac {(z - i \lambda t) ^ {2}}{2 t}} d x \\ = e ^ {- \frac {\lambda^ {2} t}{2}}. \\ \end{array}
$$

# Solution 6.23

Using the formula for the characteristic function of $W(t)$ found in Exercise 6.22, we compute

$$
\begin{array}{l} E \left(W (t) ^ {4}\right) = \frac {d ^ {4}}{d \lambda^ {4}} \Bigg | _ {\lambda = 0} E (\exp (i \lambda W (t))) \\ = \left. \frac {d ^ {4}}{d \lambda^ {4}} \right| _ {\lambda = 0} e ^ {- \frac {1}{2} \lambda^ {2} t} \\ = 3 t ^ {2}. \\ \end{array}
$$

# Solution 6.24

Since $W^{1}(t), W^{2}(t)$ are independent, their joint density is the product of the densities of $W^{1}(t)$ and $W^{2}(t)$ . Therefore

$$
P \left\{\left| W (t) \right| <   R \right\} = \int_ {\{| x | <   R \}} p (t, 0, x) p (t, 0, y) d x d y
$$

$$
\begin{array}{l} = \frac {1}{2 \pi t} \int_ {\{| x | <   R \}} e ^ {- \frac {z ^ {2} + y ^ {2}}{2 t}} d x d y \\ = \frac {1}{2 \pi t} \int_ {0} ^ {R} \int_ {0} ^ {2 \pi} r e ^ {- \frac {r ^ {2}}{2 t}} d \varphi d r \\ = - \int_ {0} ^ {R} \frac {d}{d r} e ^ {- \frac {r ^ {2}}{2 t}} d r \\ = 1 - e ^ {- \frac {R ^ {2}}{2 t}}. \\ \end{array}
$$

We have used the polar coordinates $R, \varphi$ to compute the integral.

# Solution 6.25

For any $0 \leq s < t$

$$
\begin{array}{l} E (W (t) \mid \mathcal {F} _ {s}) = E (W (t) - W (s) \mid \mathcal {F} _ {s}) + E (W (s) \mid \mathcal {F} _ {s}) \\ = E (W (t) - W (s)) + W (s) \\ = W (s), \\ \end{array}
$$

since $W(t) - W(s)$ is independent of $\mathcal{F}_s$ by Corollary 6.2, $W(s)$ is $\mathcal{F}_s$ -measurable and $E(W(t)) = E(W(s)) = 0$ .

# Solution 6.26

For any $0 \leq s < t$

$$
\begin{array}{l} E \left(W (t) ^ {2} \mid \mathcal {F} _ {s}\right) = E \left(\left| W (t) - W (s) \right| ^ {2} \mid \mathcal {F} _ {s}\right) + E (2 W (t) W (s) \mid \mathcal {F} _ {s}) \\ - E (W (s) ^ {2} | \mathcal {F} _ {s}) \\ = E \left(| W (t) - W (s) | ^ {2}\right) + 2 W (s) E (W (t) \mid \mathcal {F} _ {s}) \\ - W (s) ^ {2} \\ = t - s + 2 W (s) ^ {2} - W (s) ^ {2} \\ = t - s + W (s) ^ {2}, \\ \end{array}
$$

since $W(t) - W(s)$ is independent of $\mathcal{F}_s$ and has the normal distribution with mean 0 and variance $t - s$ , $W(s)$ is $\mathcal{F}_s$ -measurable, and $W(t)$ is a martingale. It follows that

$$
E \left(W (t) ^ {2} - t | \mathcal {F} _ {s}\right) = W (s) ^ {2} - s,
$$

as required.

# Solution 6.27

For any $0 \leq t_{0} < t_{1} < \cdots < t_{n}$ the increments

$$
V (t _ {n}) - V (t _ {n - 1}), \dots , V (t _ {1}) - V (t _ {0})
$$

of $V(t)$ are independent, since the increments

$$
W (t _ {n} + T) - W (t _ {n - 1} + T), \dots , W (t _ {1} + T) - W (t _ {0} + T)
$$

of $W(t)$ are independent. For any $0 \leq s < t$ the increment $V(t) - V(s)$ has the normal distribution with mean zero and variance $t - s$ , since $W(t + T) - W(s + T)$ does. Moreover, the paths $t \mapsto V(t) = W(t + T) - W(T)$ are continuous and

$$
V (0) = W (T) - W (T) = 0.
$$

By Theorem 6.3 $V(t)$ is a Wiener process.

# Solution 6.28

It is clear that $V(0) = \frac{1}{c} W(0) = 0$ a.s. and the paths $t \mapsto V(t) = \frac{1}{c} W(c^{2}t)$ are a.s. continuous. We shall verify that $V(t)$ and $|V(t)|^{2} - t$ are martingales with respect to the filtration

$$
\begin{array}{l} \mathcal {G} _ {t} = \sigma \left\{V (s): 0 \leq s \leq t \right\} \\ = \sigma \left\{W (c ^ {2} s): 0 \leq s \leq t \right\} \\ = \sigma \left\{W (s): 0 \leq s \leq c ^ {2} t \right\} \\ = \mathcal {F} _ {c ^ {2} t}. \\ \end{array}
$$

Indeed, if $s < t$ , then $c^2 s < c^2 t$ , so

$$
\begin{array}{l} E (V (t) | \mathcal {G} _ {s}) = E \left(\frac {1}{c} W (c ^ {2} t) | \mathcal {F} _ {c ^ {2} s}\right) \\ = \frac {1}{c} E \left(W (c ^ {2} t) | \mathcal {F} _ {c ^ {2} s}\right) \\ = \frac {1}{c} W (c ^ {2} s) = V (s) \\ \end{array}
$$

and

$$
\begin{array}{l} E \left(\left| V (t) \right| ^ {2} - t | \mathcal {G} _ {s}\right) = E \left(\frac {1}{c ^ {2}} \left| W (c ^ {2} t) \right| ^ {2} - t | \mathcal {F} _ {c ^ {2} s}\right) \\ = \frac {1}{c ^ {2}} E \left(\left| W (c ^ {2} t) \right| ^ {2} - c ^ {2} t | \mathcal {F} _ {c ^ {2} s}\right) \\ = \frac {1}{c ^ {2}} \left(\left| W (c ^ {2} s) \right| ^ {2} - c ^ {2} s\right) \\ = | V (s) | ^ {2} - s, \\ \end{array}
$$

since $W(t)$ and $|W(t)|^2 - t$ are martingales with respect to the filtration $\mathcal{F}_t$ . It follows by Levy's martingale characterization that $V(t)$ is a Wiener process.

# Solution 6.29

Since the increments $\Delta_i^n W$ are independent and

$$
E \left(\Delta_ {i} ^ {n} W\right) = 0, \quad E \left(\left(\Delta_ {i} ^ {n} W\right) ^ {2}\right) = \frac {T}{n}, \quad E \left(\left(\Delta_ {i} ^ {n} W\right) ^ {4}\right) = \frac {3 T ^ {2}}{n ^ {2}},
$$

it follows that

$$
\begin{array}{l} E \left(\left[ \sum_ {i = 0} ^ {n - 1} \left(\Delta_ {i} ^ {n} W\right) ^ {2} - T \right] ^ {2}\right) = E \left(\left[ \sum_ {i = 0} ^ {n - 1} \left(\left(\Delta_ {i} ^ {n} W\right) ^ {2} - \frac {T}{n}\right) \right] ^ {2}\right) \\ = \sum_ {i = 0} ^ {n - 1} E \left[ \left(\left(\Delta_ {i} ^ {n} W\right) ^ {2} - \frac {T}{n}\right) ^ {2} \right] \\ = \sum_ {i = 0} ^ {n - 1} \left[ E \left(\left(\Delta_ {i} ^ {n} W\right) ^ {4}\right) - \frac {2 T}{n} E \left(\left(\Delta_ {i} ^ {n} W\right) ^ {2}\right) + \frac {T ^ {2}}{n ^ {2}} \right] \\ = \sum_ {i = 0} ^ {n - 1} \left[ \frac {3 T ^ {2}}{n ^ {2}} - \frac {2 T ^ {2}}{n ^ {2}} + \frac {T ^ {2}}{n ^ {2}} \right] = \frac {2 T ^ {2}}{n} \rightarrow 0 \\ \end{array}
$$

as $n\to \infty$

# Solution 6.30

We claim that, with probability 1, for any positive integer $n$ there is a $t \in [0, \frac{1}{n^4}]$ such that $\frac{|W(t)|}{t} > n$ . This condition implies that $W(t)$ is not differentiable at $t = 0$ .

Let us put

$$
A _ {n} = \left\{\frac {| W (t) |}{t} > n \text {   for   some   } t \in [ 0, \frac {1}{n ^ {4}} ] \right\}
$$

By Exercise 6.28

$$
V _ {n} (t) = \frac {1}{n ^ {2}} W (n ^ {4} t)
$$

is a Brownian motion for any $n$ . Therefore

$$
\begin{array}{l} P \left(A _ {n}\right) \geq P \left\{\frac {\left| W \left(1 / n ^ {4}\right) \right|}{1 / n ^ {4}} > n \right\} \\ = P \left\{\frac {\left| V \left(1 / n ^ {4}\right) \right|}{1 / n ^ {4}} > n \right\} \\ = P \left\{\left| W (1) \right| > \frac {1}{n} \right\}\rightarrow 1 \quad \text { as } n \rightarrow \infty . \\ \end{array}
$$

Since $A_{1}, A_{2}, \ldots$ is a contracting sequence of events,

$$
P \left(\bigcap_ {n = 1} ^ {\infty} A _ {n}\right) = \lim _ {n \rightarrow \infty} P (A _ {n}) = 1,
$$

which proves the claim.

# Solution 6.31

By Exercise 6.27 $V_{t}(s) = W(s + t) - W(t)$ is a Wiener process for any $t \geq 0$ . Therefore, by Exercise 6.30 $V_{t}(s)$ is a.s. non-differentiable at $s = 0$ . But this implies that $W(t)$ is a.s. non-differentiable at $t$ .

# Solution 6.32

Differentiating

$$
p (t, x, y) = \frac {1}{\sqrt {2 \pi t}} e ^ {- \frac {(y - x) ^ {2}}{2 t}},
$$

we obtain

$$
\frac {\partial}{\partial t} p (t, x, y) = \frac {y ^ {2} - 2 y x + x ^ {2} - t}{2 t ^ {2}} p (t, x, y),
$$

$$
\frac {\partial}{\partial y} p (t, x, y) = \frac {x - y}{t} p (t, x, y),
$$

$$
\frac {\partial^ {2}}{\partial y ^ {2}} p (t, x, y) = \frac {y ^ {2} - 2 y x + x ^ {2} - t}{t ^ {2}} p (t, x, y),
$$

so

$$
\frac {\partial p}{\partial t} = \frac {1}{2} \frac {\partial^ {2} p}{\partial y ^ {2}},
$$

as required.

# Solution 6.33

Clearly, $Z(t) = -W(t)$ has a.s. continuous trajectories and $Z(0) = -W(0) = 0$ a.s. If $W(t)$ has stationary independent increments, then so does $Z(t) = -W(t)$ . Finally,

$$
Z (t) - Z (s) = - \left(W (t) - W (s)\right)
$$

has the same distribution as $W(t)-W(s)$ , i.e. normal with mean 0 and variance t-s. By Theorem 6.3 $Z(t)$ is a Wiener process.

# Solution 6.34

Let $0 \leq s < t$ . Then

$$
\begin{array}{l} \int_ {\{W (s) \in B \}} 1 _ {A} (W (t)) d P = P \{W (s) \in B, W (t) \in A \} \\ = \int_ {B} \int_ {A} p (s, 0, x) p (t - s, x, y) d x d y \\ = \int_ {B} \left(\int_ {A} p (t - s, x, y) d y\right) p (s, 0, x) d x \\ = \int_ {\{W (s) \in B \}} \left(\int_ {A} p (t - s, W (s), y) d y\right) d P \\ \end{array}
$$

for any Borel set $B \subset \mathbb{R}$ . It follows that

$$
P \left\{W (t) \in A | W (s) \right\} = E \left(1 _ {A} (W (t)) | W (s)\right) = \int_ {A} p (t - s, W (s), y) d y.
$$

# Solution 6.35

We shall prove that $e^{W(t)}e^{-\frac{1}{2}}$ is a martingale with respect to the filtration $F_{t}$ . Clearly, it is adapted to the filtration $F_{t}$ , since $W(t)$ is. Let $0 \leq s < t$ . Because $W(t) - W(s)$ is independent of $F_{s}$ and $W(s)$ is $F_{s}$ -measurable,

$$
\begin{array}{l} E \left(e ^ {W (t)} | \mathcal {F} _ {s}\right) = E \left(e ^ {W (t) - W (s)} e ^ {W (s)} | \mathcal {F} _ {s}\right) \\ = e ^ {W (s)} E \left(e ^ {W (t) - W (s)} | \mathcal {F} _ {s}\right) \\ = e ^ {W (s)} E \left(e ^ {W (t) - W (s)}\right). \\ \end{array}
$$

The increment $W(t) - W(s)$ has the normal distribution with mean 0 and variance $t - s$ , so the expectation of $e^{W(t) - W(s)}$ is equal to

$$
\begin{array}{l} E \left(e ^ {W (t) - W (s)}\right) = \int_ {- \infty} ^ {+ \infty} e ^ {x} p (t - s, 0, x) d x \\ = e ^ {\frac {t - s}{2}} \int_ {- \infty} ^ {+ \infty} p (t - s, 0, x - t) d x \\ = e ^ {\frac {t - s}{2}}. \\ \end{array}
$$

It follows that

$$
E \left(e ^ {W (t)} e ^ {- \frac {t}{2}} | \mathcal {F} _ {s}\right) = e ^ {W (s)} e ^ {- \frac {s}{2}}.
$$

It also follows that $e^{W(t)}e^{-\frac{t}{2}}$ is integrable. Therefore $e^{W(t)}e^{-\frac{t}{2}}$ is a martingale.

# Solution 6.36

Let $0 \leq s < t$ . We are looking for a Borel function $F$ such that $E(W(s)|W(t)) = F(W(t))$ , i.e.

$$
\int_ {\{W (t) \in A \}} W (s) d P = \int_ {\{W (t) \in A \}} F (W (t)) d P
$$

for any Borel set A in R. The integral on the right-hand side can be written as

$$
\int_ {\{W (t) \in A \}} F (W (t)) d P = \int_ {A} F (y) p (t, 0, y) d y
$$

and the integral on the left-hand side as

$$
\int_ {\{W (t) \in A \}} W (s) d P = \int_ {A} \left(\int_ {- \infty} ^ {+ \infty} x p (s, 0, x) p (t - s, x, y) d x\right) d y
$$

using the expression for the joint density of $W(s)$ and $W(t)$ in Solution 6.20. Let us compute the inner integral:

$$
\begin{array}{l} \int_ {- \infty} ^ {+ \infty} x p (s, 0, x) p (t - s, x, y) d x = p (t, 0, y) \int_ {- \infty} ^ {\infty} x p \left(\frac {s (t - s)}{t}, \frac {s}{t} y, x\right) d x \\ = \frac {s}{t} y p (t, 0, y). \\ \end{array}
$$

(To see that the first equality holds, just use formula (6.5) for $p(t, x, y)$ .) Therefore

$$
\int_ {\{W (t) \in A \}} W (s) d P = \int_ {A} \frac {s}{t} y p (t, 0, y) d y.
$$

It follows that $F(y) = \frac{s}{t} y$ , i.e.

$$
E (W (s) | W (t)) = \frac {s}{t} W (t).
$$

# Itô Stochastic Calculus

One of the first applications of the Wiener process was proposed by Bachelier, who around 1900 wrote a ground-breaking paper on the modelling of asset prices at the Paris Stock Exchange. Of course Bachelier could not have called it the Wiener process, but he used what in modern terminology amounts to $W(t)$ as a description of the market fluctuations affecting the price $X(t)$ of an asset. Namely, he assumed that infinitesimal price increments $dX(t)$ are proportional to the increments $dW(t)$ of the Wiener process,

$$
d X (t) = \sigma d W (t),
$$

where $\sigma$ is a positive constant. As a result, an asset with initial price $X(0) = x$ would be worth

$$
X (t) = x + \sigma W (t)
$$

at time $t$ . This approach was ahead of Bachelier's time, but it suffered from one serious flaw: for any $t > 0$ the price $X(t)$ can be negative with non-zero probability. Nevertheless, for short times it works well enough, since the probability is negligible. But as $t$ increases, so does the probability that $X(t) < 0$ , and the model departs from reality.

To remedy the flaw it was observed that investors work in terms of their potential gain or loss $dX(t)$ in proportion to the invested sum $X(t)$ . Therefore, it is in fact the relative price $dX(t)/X(t)$ of an asset that reacts to the market fluctuations, i.e. should be proportional to $dW(t)$ ,

$$
d X (t) = \sigma X (t) d W (t). \tag {7.1}
$$

What is the precise mathematical meaning of this equality? Formally, it resembles a differential equation, but this immediately leads to a difficulty because the paths of $W(t)$ are nowhere differentiable. A way around the obstacle was found by Itô in the 1940s. In his hugely successful theory of stochastic integrals and stochastic differential equations Itô gave a rigorous meaning to equations such as (7.1) by writing them as integral equations involving a new kind of integral. In particular, (7.1) can be written as

$$
X (t) = x + \sigma \int_ {0} ^ {t} X (t) d W (t),
$$

where the integral with respect to $W(t)$ on the right-hand side is called the Itô stochastic integral and will be defined in the next section. While at first sight one would expect the solution to this equation to be $xe^{W(t)}$ , in fact it turns out to be

$$
X (t) = x e ^ {W (t)} e ^ {- \frac {t}{2}},
$$

which is the exponential martingale introduced in Exercise 6.35. The intriguing additional factor $e^{-\frac{t}{2}}$ is due to the non-differentiability of the paths of the Wiener process. Clearly, if $x > 0$ , then $X(t) > 0$ for all $t \geq 0$ , as required in the model of asset prices. In the following sections we shall learn how to transform and compute stochastic integrals and how to solve stochastic differential equations.

Throughout this chapter $W(t)$ will denote a Wiener process adapted to a filtration $F_{t}$ and $L^{2}$ will be the space of square integrable random variables.

# 7.1 Itô Stochastic Integral: Definition

We shall follow a construction resembling that of the Riemann integral. First, the integral will be defined for a class of piecewise constant processes called random step processes. Then it will be extended to a larger class by approximation.

There are, however, at least two major differences between the Riemann and Itô integrals. One is the type of convergence. The approximations of the Riemann integral converge in $\mathbb{R}$ , while the Itô integral will be approximated by sequences of random variables converging in $L^2$ . The other difference is this. The Riemann sums approximating the integral of a function $f:[0,T]\to\mathbb{R}$ are of the form

$$
\sum_ {j = 0} ^ {n - 1} f (s _ {j}) \left(t _ {j + 1} - t _ {j}\right),
$$

where $0 = t_{0} < t_{1} < \cdots < t_{n} = T$ and $s_{j}$ is an arbitrary point in $[t_{j}, t_{j+1}]$ for each j. The value of the Riemann integral does not depend on the choice of the points $s_{j} \in [t_{j}, t_{j+1})$ . In the stochastic case the approximating sums will have the form

$$
\sum_ {j = 0} ^ {n - 1} f (s _ {j}) \left(W (t _ {j + 1}) - W (t _ {j})\right).
$$

It turns out that the limit of such approximations does depend on the choice of the intermediate points $s_{j}$ in $[t_{j}, t_{j+1}]$ . In the next exercise we take $f(t) = W(t)$ and consider two different choices of intermediate points.

# Exercise 7.1

Let $0 = t_0^n < t_1^n < \cdots < t_n^n = T$ , where $t_j^n = \frac{jT}{n}$ , be a partition of the interval $[0, T]$ into $n$ equal parts. Find the following limits in $L^2$ :

$$
\lim _ {n \rightarrow \infty} \sum_ {j = 0} ^ {n - 1} W (t _ {j} ^ {n}) \left(W (t _ {j + 1} ^ {n}) - W (t _ {j} ^ {n})\right)
$$

and

$$
\lim _ {n \rightarrow \infty} \sum_ {j = 0} ^ {n - 1} W \left(t _ {j + 1} ^ {n}\right)\left(W \left(t _ {j + 1} ^ {n}\right) - W \left(t _ {j} ^ {n}\right)\right).
$$

Hint Apply Exercise 6.29. You will need to transform the sums to make this possible. The identities

$$
a (b - a) = \frac {1}{2} \left(b ^ {2} - a ^ {2}\right) - \frac {1}{2} (a - b) ^ {2},
$$

$$
b (b - a) = \frac {1}{2} \left(b ^ {2} - a ^ {2}\right) + \frac {1}{2} (a - b) ^ {2}
$$

may be of help.

The ambiguity resulting from different choices of the intermediate points $s_{j}$ in each subinterval $[t_{j}, t_{j+1}]$ can be removed by insisting that the approximations of the integrand should consist only of processes adapted to the underlying filtration $F_{t}$ . This amounts to taking $s_{j} = t_{j}$ for each j. The choice is motivated by the interpretation of $F_{t}$ : the value of the approximation at t may depend only on what has happened up to time t, but not on any future events.

# Definition 7.1

We shall call $f(t), t \geq 0$ a random step process if there is a finite sequence of numbers $0 = t_0 < t_1 < \ldots < t_n$ and square integrable random variables

$\eta_0, \eta_1, \ldots, \eta_{n-1}$ such that

$$
f (t) = \sum_ {j = 0} ^ {n - 1} \eta_ {j} 1 _ {[ t _ {j}, t _ {j + 1})} (t), \tag {7.2}
$$

where $\eta_j$ is $\mathcal{F}_{t_j}$ -measurable for $j = 0,1,\ldots,n-1$ . The set of random step processes will be denoted by $M_{\mathrm{step}}^2$ :

Observe that the assumption that the $\eta_{j}$ are to be $F_{t_{j}}$ -measurable ensures that $f(t)$ is adapted to the filtration $F_{t}$ . The assumption that the $\eta_{j}$ are square integrable ensures that $f(t)$ is square integrable for each t. Also, $M_{step}^{2}$ is a vector space, that is, $af + bg \in M_{step}^{2}$ for any $f, g \in M_{step}^{2}$ and $a, b \in R$ .

# Definition 7.2

The stochastic integral of a random step process $f \in M_{\mathrm{step}}^2$ of the form (7.2) is defined by

$$
I (f) = \sum_ {j = 0} ^ {n - 1} \eta_ {j} \left(W (t _ {j + 1}) - W (t _ {j})\right). \tag {7.3}
$$

# Proposition 7.1

For any random step process $f \in M_{\text{step}}^2$ the stochastic integral $I(f)$ is a square integrable random variable, i.e. $I(f) \in L^2$ , such that

$$
E \left(\left| I (f) \right| ^ {2}\right) = E \left(\int_ {0} ^ {\infty} | f (t) | ^ {2} d t\right).
$$

# Proof

Let us denote the increment $W(t_{j+1}) - W(t_j)$ by $\Delta_j W$ and $t_{j+1} - t_j$ by $\Delta_j t$ for brevity. Then

$$
E \left(\Delta_ {j} W\right) = 0 \quad \text { and } \quad E \left(\Delta_ {j} ^ {2} W\right) = \Delta_ {j} t.
$$

First, we shall compute the expectation of

$$
\left| I (f) \right| ^ {2} = \sum_ {j = 0} ^ {n - 1} \sum_ {k = 0} ^ {n - 1} \eta_ {j} \eta_ {k} \Delta_ {j} W \Delta_ {k} W = \sum_ {j = 0} ^ {n - 1} \eta_ {j} ^ {2} \Delta_ {j} ^ {2} W + 2 \sum_ {k <   j} \eta_ {j} \eta_ {k} \Delta_ {j} W \Delta_ {k} W.
$$

Since $\eta_j$ and $\Delta_j W$ are independent,

$$
E \left(\eta_ {j} ^ {2} \Delta_ {j} ^ {2} W\right) = E \left(\eta_ {j} ^ {2}\right) E \left(\Delta_ {j} ^ {2} W\right) = E \left(\eta_ {j} ^ {2}\right) \Delta_ {j} t.
$$

If $k < j$ , then $\eta_j \eta_k \Delta_k W$ and $\Delta_j W$ are independent, so

$$
E \left(\eta_ {j} \eta_ {k} \Delta_ {j} W \Delta_ {k} W\right) = E \left(\eta_ {j} \eta_ {k} \Delta_ {k} W\right) E \left(\Delta_ {j} W\right) = 0.
$$

Therefore

$$
E \left(\left| I (f) \right| ^ {2}\right) = \sum_ {j = 0} ^ {n - 1} E \left(\eta_ {j} ^ {2}\right) \Delta_ {j} t.
$$

It follows that $I(f) \in L^2$ , since $\eta_0, \eta_1, \ldots, \eta_{n-1} \in L^2$ .

On the other hand,

$$
| f (t) | ^ {2} = \sum_ {j = 0} ^ {n - 1} \sum_ {k = 0} ^ {n - 1} \eta_ {j} \eta_ {k} 1 _ {[ t _ {j}, t _ {j + 1})} (t) 1 _ {[ t _ {k}, t _ {k + 1})} (t) = \sum_ {j = 0} ^ {n - 1} \eta_ {j} ^ {2} 1 _ {[ t _ {j}, t _ {j + 1})} (t),
$$

implying that

$$
E \left(\int_ {0} ^ {\infty} | f (t) | ^ {2} d t\right) = \sum_ {j = 0} ^ {n - 1} E \left(\eta_ {j} ^ {2}\right) \Delta_ {j} t.
$$

This means that

$$
E \left(| I (f) | ^ {2}\right) = E \left(\int_ {0} ^ {\infty} | f (t) | ^ {2} d t\right),
$$

as required. □

# Exercise 7.2

Verify that for any random step processes $f, g \in M_{\mathrm{step}}^2$

$$
E (I (f) I (g)) = E \left(\int_ {0} ^ {\infty} f (t) g (t) d t\right).
$$

Hint Try to adapt the proof of Proposition 7.1. Use a common partition $0 = t_0 < t_1 < \cdots < t_n$ in which to represent both $f$ and $g$ in the form (7.2).

# Exercise 7.3

Show that $I: M_{\mathrm{step}}^2 \to L^2$ is a linear map, i.e. for any $f, g \in M_{\mathrm{step}}^2$ and any $\alpha, \beta \in \mathbb{R}$

$$
I (\alpha f + \beta g) = \alpha I (f) + \beta I (g).
$$

Hint As in Exercise 7.2, use a common partition $0 = t_0 < t_1 < \cdots < t_n$ in which to represent both $f$ and $g$ in the form (7.2).

The stochastic integral $I(f)$ has been defined for any random step process $f \in M_{step}^{2}$ . The next stage is to extend I to a larger class of processes by approximation. This larger class can be defined as follows.

# Definition 7.3

We denote by $M^2$ the class of stochastic processes $f(t), t \geq 0$ such that

$$
E \left(\int_ {0} ^ {\infty} | f (t) | ^ {2} d t\right) <   \infty
$$

and there is a sequence $f_{1}, f_{2}, \ldots \in M_{\mathrm{step}}^{2}$ of random step processes such that

$$
\lim _ {n \rightarrow \infty} E \left(\int_ {0} ^ {\infty} | f (t) - f _ {n} (t) | ^ {2} d t\right) = 0. \tag {7.4}
$$

In this case we shall say that the sequence of random step processes $f_{1}, f_{2}, \ldots$ approximates f in $M^{2}$ .

# Definition 7.4

We call $I(f) \in L^2$ the Itô stochastic integral (from 0 to $\infty$ ) of $f \in M^2$ if

$$
\lim _ {n \rightarrow \infty} E \left(\left| I (f) - I \left(f _ {n}\right)\right| ^ {2}\right) = 0 \tag {7.5}
$$

for any sequence $f_1, f_2, \ldots \in M_{\mathrm{step}}^2$ of random step processes that approximates $f$ in $M^2$ , i.e. such that (7.4) is satisfied. We shall also write

$$
\int_ {0} ^ {\infty} f (t) d W (t)
$$

in place of $I(f)$ .

# Proposition 7.2

For any $f \in M^2$ the stochastic integral $I(f) \in L^2$ exists, is unique (as an element of $L^2$ , i.e. to within equality a.s.) and satisfies

$$
E \left(| I (f) | ^ {2}\right) = E \left(\int_ {0} ^ {\infty} | f (t) | ^ {2} d t\right). \tag {7.6}
$$

# Proof

It will be convenient to write

$$
\| f \| _ {M ^ {2}} = \sqrt {E \left(\int_ {0} ^ {\infty} | f (t) | ^ {2} d t\right)} \quad \text { and } \quad \| \eta \| _ {L ^ {2}} = \sqrt {E (\eta^ {2})}
$$

for any $f \in M^2$ and $\eta \in L^2$ . These are norms $^1$ in $M^2$ and $L^2$ , respectively.

Let $f_{1}, f_{2}, \ldots \in M_{\text{step}}^{2}$ be a sequence of random step processes approximating $f \in M^{2}$ , i.e. satisfying (7.4), which can be written as

$$
\lim _ {n \rightarrow \infty} \| f - f _ {n} \| _ {M ^ {2}} = 0.
$$

We claim that $I(f_1), I(f_2), \ldots$ is a Cauchy sequence in $L^2$ . Indeed, for any $\varepsilon > 0$ there is an $N$ such that $\| f - f_n \|_{M^2} < \frac{\varepsilon}{2}$ for all $n > N$ . By Proposition 7.1

$$
\begin{array}{l} \left\| I \left(f _ {m}\right) - I \left(f _ {n}\right) \right\| _ {L ^ {2}} = \left\| I \left(f _ {m} - f _ {n}\right) \right\| _ {L ^ {2}} \\ = \left\| f _ {m} - f _ {n} \right\| _ {M ^ {2}} \\ \leq \left\| f - f _ {m} \right\| _ {M ^ {2}} + \left\| f - f _ {n} \right\| _ {M ^ {2}} \\ <   \frac {\varepsilon}{2} + \frac {\varepsilon}{2} = \varepsilon \\ \end{array}
$$

for any $m, n > N$ , which proves the claim.

Because $L^2$ with the norm $\| \cdot \|_{L^2}$ is a complete space (in fact a Hilbert space), every Cauchy sequence in $L^2$ has a limit. It follows that $I(f_1), I(f_2), \ldots$ has a limit in $L^2$ for any sequence $f_1, f_2, \ldots$ of random step processes approximating $f$ . It remains to show that the limit is the same for all such sequences. Suppose that $f_1, f_2, \ldots$ and $g_1, g_2, \ldots$ are two sequences of random step processes approximating $f$ . Then the interlaced sequence $f_1, g_1, f_2, g_2, \ldots$ approximates $f$ too, so the sequence $I(f_1), I(g_1), I(f_2), I(g_2), \ldots$ has a limit in $L^2$ . But then all subsequences of the latter sequence, in particular, $I(f_1), I(f_2), \ldots$ and $I(g_1), I(g_2), \ldots$ have the same limit, which we denote by $I(f)$ . We have shown that

$$
\lim _ {n \rightarrow \infty} | | I (f) - I (f _ {n}) | | _ {L ^ {2}} = 0,
$$

i.e. (7.5) holds for any sequence $f_1, f_2, \ldots$ of random step processes approximating $f$ .

Finally, by Proposition 7.1

$$
\left| \left| I (f _ {n}) \right| \right| _ {L ^ {2}} = \left| \left| f _ {n} \right| \right| _ {M ^ {2}}
$$

for each $n$ , since the $f_{n}$ are random step processes. By taking the limit as $n \to \infty$ we obtain

$$
\left\| I (f) \right\| _ {L ^ {2}} = \left\| f \right\| _ {M ^ {2}}.
$$

But this is equality (7.6). $\square$

# Exercise 7.4

Show that for any $f, g \in M^2$

$$
E (I (f) I (g)) = E \left(\int_ {0} ^ {\infty} f (t) g (t) d t\right).
$$

Hint Write the left-hand side in terms of $E\left(|I(f) + I(g)|^2\right)$ and $E\left(|I(f) - I(g)|^2\right)$ , the right-hand side in terms of $E\left(\int_0^\infty |f(t) + g(t)|^2 dt\right)$ and $E\left(\int_0^\infty |f(t) - g(t)|^2 dt\right)$ and then use (7.6).

Having defined the Itô stochastic integral from 0 to $\infty$ , we are now in a position to consider stochastic integrals over any finite time interval $[0, T]$ .

# Definition 7.5

For any $T > 0$ we shall denote by $M_T^2$ the space of all stochastic processes $f(t), t \geq 0$ such that

$$
\mathbf {1} _ {[ 0, T)} f \in M ^ {2}
$$

The Itô stochastic integral (from 0 to $T$ ) of $f \in M_T^2$ is defined by

$$
I _ {T} (f) = I \left(1 _ {[ 0, T)} f\right). \tag {7.7}
$$

We shall also write

$$
\int_ {0} ^ {T} f (t) d W (t)
$$

in place of $I_T(f)$ .

# Exercise 7.5

Show that each random step process $f \in M_{\text{step}}^2$ belongs to $M_t^2$ for any $t > 0$ and

$$
I _ {t} (f) = \int_ {0} ^ {t} f (s) d W (s)
$$

is a martingale.

Hint The stochastic integral of a random step process $f$ is given by the sum (7.3). What is the conditional expectation of the $j$ th term of this sum given $\mathcal{F}_s$ if $s < t_j$ ? What is it when $s \geq t_j$ ?

The processes for which the stochastic integral exists have been defined as those that can be approximated by random step processes. However, it is not always easy to check whether or not such an approximation exists. For practical purposes it is important to have a straightforward sufficient condition for a process to have a stochastic integral. In calculus there is a well-known result of this kind: the Riemann integral exists for any continuous function. Here is a theorem of this kind for the Itô integral.

![](images/f870019a3ce257588aca6033e440be8636663b7e2b20c9cf54f96f00c2aeea3f.jpg)

# Theorem 7.1

Let $f(t), t \geq 0$ be a stochastic process with a.s. continuous paths adapted to the filtration $\mathcal{F}_t$ . Then

1) $f \in M^2$ , i.e. the Itô integral $I(f)$ exists, whenever

$$
E \left(\int_ {0} ^ {\infty} | f (t) | ^ {2} d t\right) <   \infty ; \tag {7.8}
$$

2) $f \in M_T^2$ , i.e. the Itô integral $I_T(f)$ exists, whenever

$$
E \left(\int_ {0} ^ {T} | f (t) | ^ {2} d t\right) <   \infty . \tag {7.9}
$$

# Proof

1) Suppose that $f(t), t \geq 0$ is an adapted process with a.s. continuous paths. If (7.8) holds, then

$$
f _ {n} (t) = \left\{ \begin{array}{l l} n \int_ {\frac {k - 1}{n}} ^ {\frac {k}{n}} f (s) d s & \frac {k}{n} \leq t <   \frac {k + 1}{n} \text {   for   } k = 1, 2, \dots , n ^ {2} - 1, \\ 0 & \text { otherwise }, \end{array} \right. \tag {7.10}
$$

is a sequence of random step processes in $M_{\mathrm{step}}^2$ . Observe that for any $k = 1, 2, \ldots$

$$
\int_ {\frac {k}{n}} ^ {\frac {k + 1}{n}} \left| f _ {n} (t) \right| ^ {2} d t = n \left| \int_ {\frac {k - 1}{n}} ^ {\frac {k}{n}} f (t) d t \right| ^ {2} \leq \int_ {\frac {k - 1}{n}} ^ {\frac {k}{n}} | f (t) | ^ {2} d t \quad \text { a.s. } \tag {7.11}
$$

by Jensen's inequality. We claim that

$$
\lim _ {n \rightarrow \infty} \int_ {0} ^ {\infty} | f (t) - f _ {n} (t) | ^ {2} d t = 0 \quad \text { a   .   s   . }
$$

This will imply that

$$
\lim _ {n \rightarrow \infty} E \left(\int_ {0} ^ {\infty} | f (t) - f _ {n} (t) | ^ {2} d t\right) = 0
$$

by the dominated convergence theorem and condition (7.8) because

$$
\begin{array}{l} \int_ {0} ^ {\infty} | f (t) - f _ {n} (t) | ^ {2} d t \leq 2 \int_ {0} ^ {\infty} \left(| f (t) | ^ {2} + | f _ {n} (t) | ^ {2}\right) d t \\ \leq 4 \int_ {0} ^ {\infty} | f (t) | ^ {2} d t. \\ \end{array}
$$

The last inequality follows, since

$$
\int_ {0} ^ {\infty} | f _ {n} (t) | ^ {2} d t \leq \int_ {0} ^ {\infty} | f (t) | ^ {2} d t \quad \text { a.s. }
$$

for any $n$ , by taking the sum from $k = 0$ to $\infty$ in (7.11).

To verify the claim observe that

$$
\begin{array}{l} \int_ {0} ^ {\infty} | f (t) - f _ {n} (t) | ^ {2} d t = \int_ {0} ^ {N} | f (t) - f _ {n} (t) | ^ {2} d t + \int_ {N} ^ {\infty} | f (t) - f _ {n} (t) | ^ {2} d t \\ \leq \int_ {0} ^ {N} | f (t) - f _ {n} (t) | ^ {2} d t + 2 \int_ {N} ^ {\infty} \left(| f (t) | ^ {2} + | f _ {n} (t) | ^ {2}\right) d t \\ \leq \int_ {0} ^ {N} | f (t) - f _ {n} (t) | ^ {2} d t + 4 \int_ {N - 1} ^ {\infty} | f (t) | ^ {2} d t \quad \text { a   .   s   . } \\ \end{array}
$$

The last inequality holds because

$$
\int_ {N} ^ {\infty} | f _ {n} (t) | ^ {2} d t \leq \int_ {N - \frac {1}{n}} ^ {\infty} | f (t) | ^ {2} d t \leq \int_ {N - 1} ^ {\infty} | f (t) | ^ {2} d t \quad \text { a.s. }
$$

for any $n$ and $N$ , by taking the sum from $k = nN$ to $\infty$ in (7.11). The claim follows because

$$
\lim _ {N \rightarrow \infty} \int_ {N - 1} ^ {\infty} | f (t) | ^ {2} d t = 0 \quad \text { a   .   s   . }
$$

by (7.8) and

$$
\lim _ {n \rightarrow \infty} \int_ {0} ^ {N} | f (t) - f _ {n} (t) | ^ {2} d t = 0 \quad \text { a   .   s   . }
$$

for any fixed $N$ by the continuity of paths of $f$ .

The above means that the sequence $f_1, f_2, \ldots \in M_{\text{step}}^2$ approximates $f$ in the sense of Definition 7.3, so $f \in M^2$ .

2) If $f$ satisfies (7.9) for some $T > 0$ , then $1_{[0,T)}f$ satisfies (7.8). Since $f$ is adapted and has a.s. continuous paths, $1_{[0,T)}f$ is also adapted and its paths are a.s. continuous, except perhaps at $T$ . But the lack of continuity at the single point $T$ does not affect the argument in 1), so $1_{[0,T)}f \in M^2$ . This in turn implies that $f \in M_T^2$ , completing the proof.

# Exercise 7.6

Show that the Wiener process $W(t)$ belongs to $M_T^2$ for each $T > 0$ .

Hint Apply part 2) of Theorem 7.1.

# Exercise 7.7

Show that $W(t)^2$ belongs to $M_T^2$ for each $T > 0$ .

Hint Once again, apply part 2) of Theorem 7.1.

The next theorem, which we shall state without proof, provides a characterization of $M^{2}$ and $M_{T}^{2}$ , i.e. a necessary and sufficient condition for a stochastic process f to belong to $M^{2}$ or $M_{T}^{2}$ . It involves the notion of a progressively measurable process.

# Definition 7.6

A stochastic process $f(t), t \geq 0$ is called progressively measurable if for any $t \geq 0$

$$
(s, \omega) \mapsto f (s, \omega)
$$

is a measurable function from $[0, t] \times \Omega$ with the $\sigma$ -field $\mathcal{B}[0, t] \bar{\times} \mathcal{F}$ to $\mathbb{R}$ . Here $\mathcal{B}[0, t] \bar{\times} \mathcal{F}$ is the product $\sigma$ -field on $[0, t] \times \Omega$ , that is, the smallest $\sigma$ -field containing all sets of the form $A \times B$ , where $A \subset [0, t]$ is a Borel set and $B \in \mathcal{F}$ .

# Theorem 7.2

1) The space $M^2$ consists of all progressively measurable stochastic processes $f(t), t \geq 0$ such that

$$
E \left(\int_ {0} ^ {\infty} | f (t) | ^ {2} d t\right) <   \infty .
$$

2) The space $M_T^2$ consists of all progressively measurable stochastic processes $f(t), t \geq 0$ such that

$$
E \left(\int_ {0} ^ {T} | f (t) | ^ {2} d t\right) <   \infty .
$$

# 7.2 Examples

According to Exercise 7.6, the Wiener process $W(t)$ belongs to $M_{T}^{2}$ for any T > 0. Therefore the stochastic integral in the next exercise exists.

# Exercise 7.8

Verify the equality

$$
\int_ {0} ^ {T} W (t) d W (t) = \frac {1}{2} W (T) ^ {2} - \frac {1}{2} T
$$

by computing the stochastic integral from the definition, that is, by approximating the integrand by random step functions.

Hint It is convenient to use a partition of the interval $[0, T]$ into $n$ equal parts. The limit of the sums approximating the integral has been found in Exercise 7.1.

# Exercise 7.9

Verify the equality

$$
\int_ {0} ^ {T} t d W (t) = T W (T) - \int_ {0} ^ {T} W (t) d t,
$$

by computing the stochastic integral from the definition. (The integral on the right-hand side is understood as a Riemann integral defined pathwise, i.e. separately for each $\omega \in \Omega$ .)

Hint You may want to use the same partition of $[0, T]$ into $n$ equal parts as in Solution 7.8. The sums approximating the stochastic integral can be transformed with the aid of the identity

$$
c (b - a) = (d b - c a) - b (d - c).
$$

# Exercise 7.10

Show that $W(t)^2$ belongs to $M_T^2$ for each $T > 0$ and verify the equality

$$
\int_ {0} ^ {T} W (t) ^ {2} d W (t) = \frac {1}{3} W (T) ^ {3} - \int_ {0} ^ {T} W (t) d t,
$$

where the integral on the right-hand side is a Riemann integral.

Hint As in the exercises above, it is convenient to use the partition of $[0, T]$ into $n$ equal parts. The identity

$$
a ^ {2} (b - a) = \frac {1}{3} (b ^ {3} - a ^ {3}) - a (b - a) ^ {2} - \frac {1}{3} (b - a) ^ {3}
$$

can be applied to transform the sums approximating the stochastic integral. You may also need the following identity:

$$
\left(a ^ {2} - b ^ {2}\right) ^ {2} = (a - b) ^ {4} + 4 (a - b) ^ {3} b + 4 (a - b) ^ {2} b ^ {2}.
$$

# 7.3 Properties of the Stochastic Integral

The basic properties of the Itô integral are summarized in the theorem below.

# Theorem 7.3

The following properties hold for any $f, g \in M_t^2$ , any $\alpha, \beta \in \mathbb{R}$ , and any $0 \leq s < t$ :

1) linearity

$$
\int_ {0} ^ {t} (\alpha f (r) + \beta g (r)) d W (r) = \alpha \int_ {0} ^ {t} f (r) d W (r) + \beta \int_ {0} ^ {t} g (r) d W (r);
$$

2) isometry

$$
E \left(\left| \int_ {0} ^ {t} f (r) d W (r) \right| ^ {2}\right) = E \left(\int_ {0} ^ {t} | f (r) | ^ {2} d r\right);
$$

3) martingale property

$$
E \left(\int_ {0} ^ {t} f (r) d W (r) \mid \mathcal {F} _ {s}\right) = \int_ {0} ^ {s} f (r) d W (r).
$$

# Proof

1) If $f$ and $g$ belong to $M_t^2$ , then $1_{[0,t)}f$ and $1_{[0,t)}g$ belong to $M^2$ , so there are sequences $f_1, f_2, \ldots$ and $g_1, g_2, \ldots$ in $M_{\text{step}}^2$ approximating $1_{[0,t)}f$ and $1_{[0,t)}g$ . It follows that $1_{[0,t)}(\alpha f + \beta g)$ can be approximated by $\alpha f_1 + \beta g_1, \alpha f_2 + \beta g_2, \ldots$ . By Exercise 7.3

$$
I \left(\alpha f _ {n} + \beta g _ {n}\right) = \alpha I (f _ {n}) + \beta I (g _ {n})
$$

for each $n$ . Taking the $L^2$ limit on both sides of this equality as $n \to \infty$ , we obtain

$$
I \left(\mathbf {1} _ {[ 0, t)} (\alpha f + \beta g)\right) = \alpha I (\mathbf {1} _ {[ 0, t)} f) + \beta I (\mathbf {1} _ {[ 0, t)} g),
$$

which proves 1).

2) This follows by approximating $1_{[0,t)}f$ by random step processes in $M_{\text{step}}^2$ and using Proposition 7.1.

3) If $f$ belongs to $M_t^2$ , then $1_{[0,t)}f$ belongs to $M^2$ . Let $f_1, f_2, \ldots$ be a sequence of processes in $M_{\text{step}}^2$ approximating $1_{[0,t)}f$ . By Exercise 7.5

$$
E \left(I \left(1 _ {[ 0, t)} f _ {n}\right) \mid \mathcal {F} _ {s}\right) = I \left(1 _ {[ 0, s)} f _ {n}\right) \tag {7.12}
$$

for each $n$ . By taking the $L^2$ limit of both sides of this equality as $n \to \infty$ , we shall show that

$$
E \left(I \left(1 _ {[ 0, t)} f\right) \mid \mathcal {F} _ {s}\right) = I \left(1 _ {[ 0, s)} f\right),
$$

which is what needs to be proved. Indeed, observe that $\mathbf{1}_{[0,s)}f_1, \mathbf{1}_{[0,s)}f_2, \ldots$ is a sequence in $M_{\text{step}}^2$ approximating $\mathbf{1}_{[0,s)}f$ , so

$$
I \left(1 _ {[ 0, s)} f _ {n}\right)\rightarrow I \left(1 _ {[ 0, s)} f\right) \quad \text { in } L ^ {2} \text { as } n \rightarrow \infty .
$$

Similarly, $1_{[0,t)}f_1, 1_{[0,t)}f_2, \ldots$ is also a sequence in $M_{\mathrm{step}}^2$ approximating $1_{[0,t)}f$ , which implies that

$$
I \left(1 _ {[ 0, t)} f _ {n}\right)\rightarrow I \left(1 _ {[ 0, t)} f\right) \quad \text { in } L ^ {2} \text { as } n \rightarrow \infty .
$$

The lemma below implies that

$$
E \left(I \left(1 _ {[ 0, t)} f _ {n}\right) | \mathcal {F} _ {s}\right)\rightarrow E \left(I \left(1 _ {[ 0, t)} f\right) | \mathcal {F} _ {s}\right) \quad \text { in } L ^ {2} \text { as } n \rightarrow \infty ,
$$

completing the proof. $\square$

# Lemma 7.1

If $\xi$ and $\xi_1, \xi_2, \ldots$ are square integrable random variables such that $\xi_n \to \xi$ in $L^2$ as $n \to \infty$ , then

$$
E \left(\xi_ {n} | \mathcal {G}\right)\rightarrow E (\xi | \mathcal {G}) \quad \text { in } L ^ {2} \text { as } n \rightarrow \infty
$$

for any $\sigma$ -field $\mathcal{G}$ on $\Omega$ contained in $\mathcal{F}$ .

# Proof

By Jensen's inequality, see Theorem 2.2,

$$
\left| E \left(\xi_ {n} | \mathcal {G}\right) - E (\xi | \mathcal {G}) \right| ^ {2} = \left| E \left(\xi_ {n} - \xi | \mathcal {G}\right) \right| ^ {2} \leq E \left(\left| \xi_ {n} - \xi \right| ^ {2} \mid \mathcal {G}\right),
$$

which implies that

$$
\begin{array}{l} E \left(\left| E (\xi_ {n} | \mathcal {G}) - E (\xi | \mathcal {G}) \right| ^ {2}\right) \leq E \left(E \left(\left| \xi_ {n} - \xi \right| ^ {2} \mid \mathcal {G}\right)\right) \\ = E \left(\left| \xi_ {n} - \xi \right| ^ {2}\right)\rightarrow 0 \\ \end{array}
$$

as $n\to \infty$ .□

In the next theorem we consider the stochastic integral $\int_{0}^{t}f(s)dW(s)$ as a function of the upper integration limit t. Similarly as for the Riemann integral, it is natural to ask if this is a continuous function of t. The answer to this question involves the notion of a modification of a stochastic process.

# Definition 7.7

Let $\xi(t)$ and $\zeta(t)$ be stochastic processes defined for $t \in T$ , where $T \subset \mathbb{R}$ . We say that the processes are modifications (or versions) of one another if

$$
P \left\{\xi (t) = \zeta (t) \right\} = 1 \quad \text { for   all } t \in T. \tag {7.13}
$$

# Remark 7.1

If $T \subset \mathbb{R}$ is a countable set, then (7.13) is equivalent to the condition

$$
P \left\{\xi (t) = \zeta (t) \text {   for   all   } t \in T \right\} = 1.
$$

However, this is not necessarily so if $T$ is uncountable.

The following result is stated without proof.

# Theorem 7.4

Let $f(s)$ be a process belonging to $M_t^2$ and let

$$
\xi (t) = \int_ {0} ^ {t} f (s) d W (s)
$$

for every $t \geq 0$ . Then there exists an adapted modification $\zeta(t)$ of $\xi(t)$ with a.s. continuous paths. This modification is unique up to equality a.s.

From now on we shall always identify $\int_{0}^{t}f(s)dW(s)$ with the adapted modification having a.s. continuous paths. This convention works beautifully together with Theorem 7.1 whenever there is a need to show that a stochastic integral can be used as the integrand of another stochastic integral, i.e. belongs to $M_{T}^{2}$ for $T\geq0$ . This is illustrated by the next exercise.

# Exercise 7.11

Show that

$$
\xi (t) = \int_ {0} ^ {t} W (s) d W (s)
$$

belongs to $M_T^2$ for any $T \geq 0$ .

Hint By Theorem 7.4 $\xi(t)$ can be identified with an adapted modification having a.s. continuous trajectories. Because of this, it suffices to verify that $\xi(t)$ satisfies condition (7.9) of Theorem 7.1.

# 7.4 Stochastic Differential and Itô Formula

Any continuously differentiable function $x(t)$ such that $x(0) = 0$ satisfies the formulae

$$
x (T) ^ {2} = 2 \int_ {0} ^ {T} x (t) d x (t),
$$

$$
x (T) ^ {3} = 3 \int_ {0} ^ {T} x (t) ^ {2} d x (t),
$$

where $dx(t)$ can simply be understood as a shorthand notation for $x'(t)dt$ , the integrals on the right-hand side being Riemann integrals. Similar formulae have been obtained in Exercises 7.8 and 7.10 for the Wiener process:

$$
\begin{array}{l} W (T) ^ {2} = \int_ {0} ^ {T} d t + 2 \int_ {0} ^ {T} W (t) d W (t), \\ W (T) ^ {3} = 3 \int_ {0} ^ {T} W (t) d t + 3 \int_ {0} ^ {T} W (t) ^ {2} d W (t). \\ \end{array}
$$

Here the stochastic integrals resemble the corresponding expressions for a smooth function $x(t)$ , but there are also the intriguing terms $\int_{0}^{T} dt$ and $3\int_{0}^{T} W(t)dt$ . The formulae for $W(T)^{2}$ and $W(T)^{3}$ are examples of the much more general Itô formula, a crucial tool for transforming and computing stochastic integrals. Terms such as $\int_{0}^{T} dt$ and $3\int_{0}^{T} W(t)dt$ , which have no analogues in the classical calculus of smooth functions, are a feature inherent in the Itô formula and referred to as the Itô correction. The class of processes appearing in the Itô formula is defined as follows.

# Definition 7.8

A stochastic process $\xi(t), t \geq 0$ is called an Itô process if it has a.s. continuous paths and can be represented as

$$
\xi (T) = \xi (0) + \int_ {0} ^ {T} a (t) d t + \int_ {0} ^ {T} b (t) d W (t) \quad \text {a.s.}, \tag {7.14}
$$

where $b(t)$ is a process belonging to $M_{T}^{2}$ for all T > 0 and $a(t)$ is a process adapted to the filtration $F_{t}$ such that

$$
\int_ {0} ^ {T} | a (t) | d t <   \infty \quad \text { a.s. } \tag {7.15}
$$

for all $T \geq 0$ . The class of all adapted processes $a(t)$ satisfying (7.15) for some $T > 0$ will be denoted by $\mathcal{L}_T^1$ .

For an Itô process $\xi$ it is customary to write (7.14) as

$$
d \xi (t) = a (t) d t + b (t) d W (t) \tag {7.16}
$$

and to call $d\xi(t)$ the stochastic differential of $\xi(t)$ . This is known as the Itô differential notation. It should be emphasized that the stochastic differential has no well-defined mathematical meaning on its own and should always be understood in the context of the rigorous equation (7.14). The Itô differential notation is an efficient way of writing this equation, rather than an attempt to give a precise mathematical meaning to the stochastic differential.

# Example 7.1

The Wiener process $W(t)$ satisfies

$$
W (T) = \int_ {0} ^ {T} d W (t).
$$

(The right-hand side is the stochastic integral $I(f)$ of the random step process $f = 1_{[0,T)}$ .) This is an equation of the form (7.14) with $a(t) = 0$ and $b(t) = 1$ , which belong, respectively, to $\mathcal{L}_T^1$ and $M_T^2$ for any $T \geq 0$ . It follows that the Wiener process is an Itô process.

# Example 7.2

Every process of the form

$$
\xi (T) = \xi (0) + \int_ {0} ^ {T} a (t) d t,
$$

where $a(t)$ is a process belonging to $L_{T}^{1}$ for any $T \geq 0$ , is an Itô process. In particular, every deterministic process of this form, where $a(t)$ is a deterministic integrable function, is an Itô process.

# Example 7.3

Since $a(t) = 1$ and $b(t) = 2W(t)$ belong, respectively, to the classes $\mathcal{L}_T^1$ and $M_T^2$ for each $T \geq 0$ ,

$$
W (T) ^ {2} = \int_ {0} ^ {T} d t + 2 \int_ {0} ^ {T} W (t) d W (t)
$$

is an Itô process; see Exercise 7.8. The last equation can also be written as

$$
d \left(W (t) ^ {2}\right) = d t + 2 W (t) d W (t),
$$

providing a formula for the stochastic differential $d(W(t)^2)$ of $W(t)^2$ .

# Exercise 7.12

Show that $W(t)^3$ is an Itô process and find a formula for the stochastic differential $d(W(t)^3)$ .

Hint Refer to Exercise 7.10.

# Exercise 7.13

Show that $tW(t)$ is an Itô process and find a formula for the stochastic differential $d(tW(t))$ .

Hint Use Exercise 7.9.

The above examples and exercises are particular cases of an extremely important general formula for transforming stochastic differentials established by Itô. To begin with, we shall state and prove a simplified version of the formula, followed by the general theorem. The proof of the simplified version captures the essential ingredients of the somewhat tedious general argument, which will be omitted. In fact, many of the essential ingredients of the proof are already present in the examples and exercises considered above.

# Theorem 7.5 (Itô formula, simplified version)

Suppose that $F(t, x)$ is a real-valued function with continuous partial derivatives $F_t'(t, x)$ , $F_x'(t, x)$ and $F_{xx}''(t, x)$ for all $t \geq 0$ and $x \in \mathbb{R}$ . We also assume that the process $F_x'(t, W(t))$ belongs to $M_T^2$ for all $T \geq 0$ . Then $F(t, W(t))$ is an Itô process such that

$$
\begin{array}{l} F (T, W (T)) - F (0, W (0)) = \int_ {0} ^ {T} \left(F _ {t} ^ {\prime} (t, W (t)) + \frac {1}{2} F _ {x x} ^ {\prime \prime} (t, W (t))\right) d t \\ + \int_ {0} ^ {T} F _ {x} ^ {\prime} (t, W (t)) d W (t) \quad \text { a.s. } \tag {7.17} \\ \end{array}
$$

In differential notation this formula can be written as

$$
d F (t, W (t)) = \left(F _ {t} ^ {\prime} (t, W (t)) + \frac {1}{2} F _ {x x} ^ {\prime \prime} (t, W (t))\right) d t + F _ {x} ^ {\prime} (t, W (t)) d W (t). \tag {7.18}
$$

# Remark 7.2

Compare the latter with the chain rule

$$
d F (t, x (t)) = F _ {t} ^ {\prime} (t, x (t)) d t + F _ {x} ^ {\prime} (t, x (t)) d x (t).
$$

for a smooth function $x(t)$ , where $dx(t)$ is understood as a shorthand notation for $x'(t)dt$ . The additional term $\frac{1}{2} F_{xx}''(t, W(t))dt$ in (7.18) is called the Itô correction.

# Proof

First we shall prove the Itô formula under the assumption that $F$ and the partial derivatives $F_x'$ and $F_{xx}''$ are bounded by some $C > 0$ .

Consider a partition $0 = t_{0}^{n} < t_{1}^{n} < \cdots < t_{n}^{n} = T$ , where $t_{i}^{n} = \frac{iT}{n}$ , of $[0, T]$ into n equal parts. We shall denote the increments $W(t_{i+1}^{n}) - W(t_{i}^{n})$ by $\Delta_{i}^{n}W$ and $t_{i+1}^{n} - t_{i}^{n}$ by $\Delta_{i}^{n}t$ . We shall also write $W_{i}^{n}$ instead of $W(t_{i}^{n})$ for brevity. According to the Taylor formula, there is a point $\tilde{W}_{i}^{n}$ in each interval $[W(t_{i}^{n}), W(t_{i+1}^{n})]$ and a point $\tilde{t}_{i}^{n}$ in each interval $[t_{i}^{n}, t_{i+1}^{n}]$ such that

$$
\begin{array}{l} F (T, W (T)) - F (0, W (0)) = \sum_ {i = 0} ^ {n - 1} \left(F \left(t _ {i + 1} ^ {n}, W _ {i + 1} ^ {n}\right) - F \left(t _ {i} ^ {n}, W _ {i} ^ {n}\right)\right) \\ = \sum_ {i = 0} ^ {n - 1} \left(F \left(t _ {i + 1} ^ {n}, W _ {i + 1} ^ {n}\right) - F \left(t _ {i} ^ {n}, W _ {i + 1} ^ {n}\right)\right) + \sum_ {i = 0} ^ {n - 1} \left(F \left(t _ {i} ^ {n}, W _ {i + 1} ^ {n}\right) - F \left(t _ {i} ^ {n}, W _ {i} ^ {n}\right)\right) \\ = \sum_ {i = 0} ^ {n - 1} F _ {t} ^ {\prime} \left(\tilde {t} _ {i} ^ {n}, W _ {i + 1} ^ {n}\right) \Delta_ {i} ^ {n} t + \sum_ {i = 0} ^ {n - 1} F _ {x} ^ {\prime} \left(t _ {i} ^ {n}, W _ {i} ^ {n}\right) \Delta_ {i} ^ {n} W + \frac {1}{2} \sum_ {i = 0} ^ {n - 1} F _ {x x} ^ {\prime \prime} \left(t _ {i} ^ {n}, \tilde {W} _ {i} ^ {n}\right) \left(\Delta_ {i} ^ {n} W\right) ^ {2} \\ = \sum_ {i = 0} ^ {n - 1} F _ {t} ^ {\prime} \left(\tilde {t} _ {i} ^ {n}, W _ {i + 1} ^ {n}\right) \Delta_ {i} ^ {n} t + \frac {1}{2} \sum_ {i = 0} ^ {n - 1} F _ {x x} ^ {\prime \prime} \left(t _ {i} ^ {n}, W _ {i} ^ {n}\right) \Delta_ {i} ^ {n} t + \sum_ {i = 0} ^ {n - 1} F _ {x} ^ {\prime} \left(t _ {i} ^ {n}, W _ {i} ^ {n}\right) \Delta_ {i} ^ {n} W \\ + \frac {1}{2} \sum_ {i = 0} ^ {n - 1} F _ {x x} ^ {\prime \prime} \left(t _ {i} ^ {n}, W _ {i} ^ {n}\right) \left(\left(\Delta_ {i} ^ {n} W\right) ^ {2} - \Delta_ {i} ^ {n} t\right) \\ + \frac {1}{2} \sum_ {i = 0} ^ {n - 1} \left[ F _ {x x} ^ {\prime \prime} (t _ {i} ^ {n}, \tilde {W} _ {i} ^ {n}) - F _ {x x} ^ {\prime \prime} (t _ {i} ^ {n}, W _ {i} ^ {n}) \right] (\varDelta_ {i} ^ {n} W) ^ {2}. \\ \end{array}
$$

We shall deal separately with each sum in the last expression, splitting the proof into several steps.

Step 1. We claim that

$$
\lim _ {n \rightarrow \infty} \sum_ {i = 0} ^ {n - 1} F _ {t} ^ {\prime} \left(\tilde {t} _ {i} ^ {n}, W _ {i + 1} ^ {n}\right) \Delta_ {i} ^ {n} t = \int_ {0} ^ {T} F _ {t} ^ {\prime} (t, W (t)) d t \quad \text {a.s.}
$$

This is because the paths of $W(t)$ are a.s. continuous, and $F_{t}^{\prime}(t,x)$ is continuous as a function of two variables by assumption. Indeed, every continuous path of the Wiener process is bounded on $[0,T]$ , i.e. there is an M > 0, which may depend on the path, such that

$$
| W (t) | \leq M \quad \text { for   all } t \in [ 0, T ].
$$

As a continuous function, $F_{t}^{\prime}(t,x)$ is uniformly continuous on the compact set $[0,T]\times [-M,M]$ and $W$ is uniformly continuous on $[0,T]$ . It follows that

$$
\lim _ {n \to \infty} \sup _ {i, t} \left| F _ {t} ^ {\prime} (\tilde {t} _ {i} ^ {n}, W _ {i + 1} ^ {n}) - F _ {t} ^ {\prime} (t, W (t)) \right| = 0 \quad \text { a.s. },
$$

where the supremum is taken over all $i = 0, \ldots, n - 1$ and $t \in [t_i^n, t_{i+1}^n]$ . By the definition of the Riemann integral this proves the claim.

Step 2. This is very similar to Step 1. By continuity

$$
\lim _ {n \rightarrow \infty} \sup _ {i, t} | F _ {x x} ^ {\prime \prime} (t _ {i} ^ {n}, W _ {i} ^ {n}) - F _ {x x} ^ {\prime \prime} (t, W (t)) | = 0 \quad \text { a.s. },
$$

where the supremum is taken over all $i = 0, \ldots, n - 1$ and $t \in [t_i^n, t_{i+1}^n]$ . By the definition of the Riemann integral

$$
\lim _ {n \rightarrow \infty} \sum_ {i = 0} ^ {n - 1} F _ {x x} ^ {\prime \prime} (t _ {i} ^ {n}, W _ {i} ^ {n}) \Delta_ {i} ^ {n} t = \int_ {0} ^ {T} F _ {x x} ^ {\prime \prime} (t, W (t)) d t \quad \text { a.s. }
$$

Step 3. We shall verify that

$$
\lim _ {n \rightarrow \infty} \sum_ {i = 0} ^ {n - 1} F _ {x} ^ {\prime} (t _ {i} ^ {n}, W _ {i} ^ {n}) \Delta_ {i} ^ {n} W = \int_ {0} ^ {T} F _ {x} ^ {\prime} (t, W (t)) d W (t) \quad \text { in } L ^ {2}.
$$

If $F_{x}^{\prime}(t,x)$ is bounded by $C > 0$ , then $f(t) = F_{x}^{\prime}(t,W(t))$ belongs to $M_T^2$ by Theorem 7.1, and the sequence of random step processes

$$
f _ {n} = \sum_ {i = 0} ^ {n - 1} F _ {x} ^ {\prime} (t _ {i} ^ {n}, W _ {i} ^ {n}) 1 _ {[ t _ {i} ^ {n}, t _ {i + 1} ^ {n})} \in M _ {\mathrm{step}} ^ {2}
$$

approximates $f$ . Indeed, by continuity

$$
\lim _ {n \rightarrow \infty} | f _ {n} (t) - f (t) | ^ {2} = 0 \quad \text { for   any } t \in [ 0, T ], \quad \text { a.s. }
$$

Because $|f_n(t) - f(t)|^2 \leq 4C^2$ , it follows that

$$
\lim _ {n \rightarrow \infty} \int_ {0} ^ {T} | f _ {n} (t) - f (t) | ^ {2} d t = 0 \quad \text { a   .   s   . }
$$

by Lebesgue's dominated convergence theorem. But $\int_0^T |f_n(t) - f(t)|^2 dt \leq 4TC^2$ , so

$$
\lim _ {n \rightarrow \infty} E \left(\int_ {0} ^ {T} | f _ {n} (t) - f (t) | ^ {2} d t\right) = 0
$$

again by Lebesgue's dominated convergence theorem. This shows that $f_{n}$ approximates $f$ , which in turn implies that $I(f_{n})$ tends to $I(f)$ in $L^2$ , concluding Step 3.

Step 4. If $F_{xx}''$ is bounded by $C > 0$ , then

$$
\lim _ {n \rightarrow \infty} \sum_ {i = 0} ^ {n - 1} F _ {x x} ^ {\prime \prime} (t _ {i} ^ {n}, W _ {i} ^ {n}) \left((\Delta_ {i} ^ {n} W) ^ {2} - \Delta_ {i} ^ {n} t\right) = 0 \quad \text { in } L ^ {2},
$$

since

$$
\begin{array}{l} E \left| \sum_ {i = 0} ^ {n - 1} F _ {x x} ^ {\prime \prime} \left(t _ {i} ^ {n}, W _ {i} ^ {n}\right) \left(\left(\Delta_ {i} ^ {n} W\right) ^ {2} - \Delta_ {i} ^ {n} t\right) \right| ^ {2} \\ = \sum_ {i = 0} ^ {n - 1} E \left| F _ {x x} ^ {\prime \prime} \left(t _ {i} ^ {n}, W _ {i} ^ {n}\right) \left(\left(\Delta_ {i} ^ {n} W\right) ^ {2} - \Delta_ {i} ^ {n} t\right) \right| ^ {2} \\ = \sum_ {i = 0} ^ {n - 1} E \left| F _ {x x} ^ {\prime \prime} \left(t _ {i} ^ {n}, W _ {i} ^ {n}\right) \right| ^ {2} E \left| \left(\Delta_ {i} ^ {n} W\right) ^ {2} - \Delta_ {i} ^ {n} t \right| ^ {2} \\ \leq C ^ {2} \sum_ {i = 0} ^ {n - 1} E \left| \left(\Delta_ {i} ^ {n} W\right) ^ {2} - \Delta_ {i} ^ {n} t \right| ^ {2} = 2 C ^ {2} \sum_ {i = 0} ^ {n - 1} \left(\Delta_ {i} ^ {n} t\right) ^ {2} \\ = 2 C ^ {2} \sum_ {i = 0} ^ {n - 1} \frac {T ^ {2}}{n ^ {2}} = 2 C ^ {2} \frac {T ^ {2}}{n} \rightarrow 0 \quad \text { as } n \rightarrow \infty . \\ \end{array}
$$

The first equality above holds because for any $i < j$

$$
\begin{array}{l} E \left[ F _ {x x} ^ {\prime \prime} \left(t _ {i} ^ {n}, W _ {i} ^ {n}\right) \left(\left(\Delta_ {i} ^ {n} W\right) ^ {2} - \Delta_ {i} ^ {n} t\right) F _ {x x} ^ {\prime \prime} \left(t _ {j} ^ {n}, W _ {j} ^ {n}\right) \left(\left(\Delta_ {j} ^ {n} W\right) ^ {2} - \Delta_ {j} ^ {n} t\right) \right] \\ = E \left[ F _ {x x} ^ {\prime \prime} \left(t _ {i} ^ {n}, W _ {i} ^ {n}\right) \left(\left(\Delta_ {i} ^ {n} W\right) ^ {2} - \Delta_ {i} ^ {n} t\right) F _ {x x} ^ {\prime \prime} \left(t _ {j} ^ {n}, W _ {j} ^ {n}\right) \right] E \left[ \left(\Delta_ {j} ^ {n} W\right) ^ {2} - \Delta_ {j} ^ {n} t \right] \\ = 0. \\ \end{array}
$$

This is because the expressions in the last two square brackets are independent and the last expectation is equal to zero.

Step 5. By a similar continuity argument as in Steps 1 and 2

$$
\lim _ {n \to \infty} \sup _ {i} \left| F _ {x x} ^ {\prime \prime} (t _ {i} ^ {n}, \tilde {W} _ {i} ^ {n}) - F _ {x x} ^ {\prime \prime} (t _ {i} ^ {n}, W _ {i} ^ {n}) \right| = 0 \quad \mathrm{a.s.},
$$

where the supremum is taken over all $i = 0,1,\ldots ,n - 1$ . Since $\sum_{i = 0}^{n - 1}\left(\Delta_i^n W\right)^2\to T$ in $L^2$ as $n\to \infty$ , there is a subsequence $n_1 < n_2 < \ldots$ such that

$$
\cdot \quad \sum_ {i = 0} ^ {n _ {k} - 1} \left(\Delta_ {i} ^ {n _ {k}} W\right) ^ {2} \rightarrow T \quad \text { a.s. }
$$

as $k\to \infty$ .It follows that

$$
\begin{array}{l} \left| \sum_ {i = 0} ^ {n _ {k} - 1} \left(F _ {x x} ^ {\prime \prime} (t _ {i} ^ {n _ {k}}, \tilde {W} _ {i} ^ {n _ {k}}) - F _ {x x} ^ {\prime \prime} (t _ {i} ^ {n _ {k}}, W _ {i} ^ {n _ {k}})\right) (\Delta_ {i} ^ {n _ {k}} W) ^ {2} \right| \\ \leq \sup _ {i} \left| F _ {x x} ^ {\prime \prime} (t _ {i} ^ {n _ {k}}, \tilde {W} _ {i + 1} ^ {n _ {k}}) - F _ {x x} ^ {\prime \prime} (t _ {i} ^ {n _ {k}}, W _ {i + 1} ^ {n _ {k}}) \right| \sum_ {i = 0} ^ {n _ {k} - 1} (\Delta_ {i} ^ {n _ {k}} W) ^ {2} \to 0 \quad \text { a.s. } \\ \end{array}
$$

as $k \to \infty$ .

In those steps above where $L^2$ convergence was obtained, we also have convergence a.s. by taking a subsequence. This proves the Itô formula (7.17) under the assumption that the partial derivatives $F_x'(t,x)$ and $F_{xx}''(t,x)$ are bounded. To complete the proof we need to remove this assumption. Let $F(t,x)$ be an arbitrary function satisfying the conditions of Theorem 7.5. For each positive integer $n$ take a smooth function $\varphi_n$ from $\mathbb{R}$ to [0,1] such that $\varphi_n(x) = 1$ for any $x \in [-n,n]$ and $\varphi_n(x) = 0$ for any $x \notin [-n - 1,n + 1]$ . Then

$$
F _ {n} (t, x) = \varphi_ {n} (x) F (t, x)
$$

also satisfies the conditions of Theorem 7.5 and has bounded partial derivatives $(F_n)_x'(t,x)$ and $(F_n)_{xx}''(t,x)$ for each $n$ . Therefore, by the first part of the proof

$$
\begin{array}{l} F _ {n} (T, W (T)) - F _ {n} (0, W (0)) \\ = \int_ {0} ^ {T} \left((F _ {n}) _ {t} ^ {\prime} (t, W (t)) + \frac {1}{2} (F _ {n}) _ {x x} ^ {\prime \prime} (t, W (t))\right) d t + \int_ {0} ^ {T} (F _ {n}) _ {x} ^ {\prime} (t, W (t)) d W (t). \\ \end{array}
$$

Consider the expanding sequence of events

$$
A _ {n} = \left\{\sup _ {t \in [ 0, T ]} | W (t) | <   n \right\}.
$$

Since $F(t, x) = F_n(t, x)$ for every $t \in [0, T]$ and $x \in [-n, n]$ , it follows that (7.17) holds on $A_n$ . It remains to show that

$$
\lim _ {n \rightarrow \infty} P (A _ {n}) = 1
$$

to prove that (7.17) holds a.s. But the latter is true because of Doob's maximal $L^2$ inequality, Theorem 6.7, which implies that

$$
\begin{array}{l} n ^ {2} \left(1 - P (A _ {n})\right) = n ^ {2} P \left\{\sup _ {t \in [ 0, T ]} | W (t) | \geq n \right\} \\ \leq E \left(\sup _ {t \in [ 0, T ]} | W (t) |\right) ^ {2} \\ \leq 4 E | W (T) | ^ {2} = 4 T, \\ \end{array}
$$

completing the proof. □

# Example 7.4

For $F(t, x) = x^2$ we have $F_t'(t, x) = 0$ , $F_x'(t, x) = 2x$ and $F_{xx}''(t, x) = 2$ . The Itô formula gives

$$
d \left(W (t) ^ {2}\right) = d t + 2 W (t) d W (t),
$$

which is the same equality as in Exercise 7.8.

# Example 7.5

For $F(t, x) = x^3$ we have $F_t'(t, x) = 0$ , $F_x'(t, x) = 3x^2$ and $F_{xx}''(t, x) = 6x$ . By the Itô formula we obtain the same equality

$$
d \left(W (t) ^ {3}\right) = 3 W (t) d t + 3 W (t) ^ {2} d W (t)
$$

as in Exercise 7.10.

# Exercise 7.14 (exponential martingale)

Show that the exponential martingale $X(t) = e^{W(t)}e^{-\frac{t}{2}}$ is an Itô process and verify that it satisfies the equation

$$
d X (t) = X (t) d W (t).
$$

Hint Use the Itô formula with $F(t, x) = e^x e^{-\frac{t}{2}}$ .

As compared with the simplified version just proved, in the general Itô formula below $W(t)$ will be replaced by an arbitrary Itô process $\xi(t)$ such that

$$
d \xi (t) = a (t) d t + b (t) d W (t), \tag {7.19}
$$

where a belongs to $L_{t}^{1}$ and b to $M_{t}^{2}$ for all $t \geq 0$ . In the general case the proof will be omitted.

# Theorem 7.6 (Itô formula, general case)

Let $\xi(t)$ be an Itô process as above. Suppose that $F(t,x)$ is a real-valued function with continuous partial derivatives $F_t'(t,x)$ , $F_x'(t,x)$ and $F_{xx}''(t,x)$ for all $t \geq 0$ and $x \in \mathbb{R}$ . We also assume that the process $b(t)F_x'(t,\xi(t))$ belongs to $M_T^2$ for all $T \geq 0$ . Then $F(t,\xi(t))$ is an Itô process such that

$$
\begin{array}{l} d F (t, \xi (t)) = \left(F _ {t} ^ {\prime} (t, \xi (t)) + F _ {x} ^ {\prime} (t, \xi (t)) a (t) + \frac {1}{2} F _ {x x} ^ {\prime \prime} (t, \xi (t)) b (t) ^ {2}\right) d t \\ + F _ {x} ^ {\prime} (t, \xi (t)) b (t) d W (t). \tag {7.20} \\ \end{array}
$$

A convenient way to remember the Itô formula is to write down the Taylor expansion for $F(t,x)$ up to the terms with partial derivatives of order two, substituting $\xi(t)$ for x and the expression on the right-hand side of (7.19) for $d\xi(t)$ , and using the so-called Itô multiplication table

$$
\begin{array}{l} d t d t = 0, \quad d t d W (t) = 0, \\ d W (t) d t = 0, \quad d W (t) d W (t) = d t. \\ \end{array}
$$

This informal procedure gives

$$
\begin{array}{l} d F = F _ {t} ^ {\prime} d t + F _ {x} ^ {\prime} d \xi + \frac {1}{2} F _ {t t} ^ {\prime \prime} d t d t + F _ {t x} ^ {\prime \prime} d t d \xi + \frac {1}{2} F _ {x x} ^ {\prime \prime} d \xi d \xi \\ = F _ {t} ^ {\prime} d t + F _ {x} ^ {\prime} (a d t + b d W) \\ + \frac {1}{2} F _ {t t} ^ {\prime \prime} d t d t + F _ {t x} ^ {\prime \prime} d t (a d t + b d W) + \frac {1}{2} F _ {x x} ^ {\prime \prime} (a d t + b d W) (a d t + b d W) \\ = F _ {t} ^ {\prime} d t + F _ {x} ^ {\prime} (a d t + b d W) + \frac {1}{2} F _ {x x} ^ {\prime \prime} b ^ {2} d t \\ = \left(F _ {t} ^ {\prime} + F _ {x} ^ {\prime} a + \frac {1}{2} F _ {x x} ^ {\prime \prime} b ^ {2}\right) d t + F _ {x} ^ {\prime} b d W, \\ \end{array}
$$

which is the expression in (7.20). Here we have omitted the arguments $(t, \xi(t))$ and, respectively, $(t)$ in all functions for brevity.

# Exercise 7.15

Applying the Itô formula to $F(t, x) = x^n$ , show that

$$
d W (t) ^ {n} = \frac {n (n - 1)}{2} W (t) ^ {n - 2} d t + n W (t) ^ {n - 1} d W (t) \tag {7.21}
$$

Hint This is a direct application of the Itô formula, but be careful with the assumptions, in particular make sure that $nW(t)^{n-1}$ belongs to $M_T^2$ for all $T > 0$ .

# Exercise 7.16 (Ornstein-Uhlenbeck process)

Suppose that $\alpha > 0$ and $\sigma \in \mathbb{R}$ are fixed. Define $Y(t), t \geq 0$ to be an adapted modification of the Itô integral

$$
Y (t) = \sigma e ^ {- \alpha t} \int_ {0} ^ {t} e ^ {\alpha s} d W (s)
$$

with a.s. continuous paths. Show that $Y(t)$ satisfies

$$
d Y (t) = - \alpha Y (t) d t + \sigma d W (t)
$$

Hint $Y(t) = F(t,\xi (t))$ with $\xi (t) = \sigma \int_0^t e^{\alpha s}dW(s)$ and $F(t,x) = e^{-\alpha t}x.$

# 7.5 Stochastic Differential Equations

This section will be devoted to stochastic differential equations of the form

$$
d \xi (t) = f (\xi (t)) d t + g (\xi (t)) d W (t).
$$

Solutions will be sought in the class of Itô processes $\xi(t)$ with a.s. continuous paths. As in the theory of ordinary differential equations, we need to specify an initial condition

$$
\xi (0) = \xi_ {0}.
$$

Here $\xi_0$ can be a fixed real number or, in general, a random variable. Being an Itô process, $\xi(t)$ must be adapted to the filtration $\mathcal{F}_t$ of $W(t)$ , so $\xi_0$ must be $\mathcal{F}_0$ -measurable.

# Example 7.6

The stochastic differential equation

$$
d X (t) = X (t) d W (t) \tag {7.22}
$$

was used as a motivation for developing Itô stochastic calculus at the beginning of the present chapter. In Exercise 7.14 it was verified that the exponential martingale

$$
X (t) = e ^ {W (t)} e ^ {- \frac {t}{2}}
$$

satisfies (7.22). It also satisfies the initial condition $X(0) = 1$ . This is an example of a linear stochastic differential equation. For the solution of a general equation of this type with an arbitrary initial condition, see Exercise 7.20.

# Example 7.7

In Exercise 7.16 it was shown that the Ornstein-Uhlenbeck process

$$
Y (t) = \sigma e ^ {- \alpha t} \int_ {0} ^ {t} e ^ {\alpha s} d W (s)
$$

satisfies the stochastic differential equation

$$
d Y (t) = - \alpha Y (t) d t + \sigma d W (t)
$$

with initial condition $Y(0)=0$ . This is an example of an inhomogeneous linear stochastic differential equation. See Exercise 7.17 for a solution with an arbitrary initial condition.

# Definition 7.9

An Itô process $\xi(t)$ , $t \geq 0$ is called a solution of the initial value problem

$$
\begin{array}{l} d \xi (t) = f (\xi (t)) d t + g (\xi (t)) d W (t), \\ \xi (0) = \xi_ {0} \\ \end{array}
$$

if $\xi_0$ is an $\mathcal{F}_0$ -measurable random variable, the processes $f(\xi(t))$ and $g(\xi(t))$ belong, respectively, to $\mathcal{L}_T^1$ and $M_T^2$ , and

$$
\xi (T) = \xi_ {0} + \int_ {0} ^ {T} f (\xi (t)) d t + \int_ {0} ^ {T} g (\xi (t)) d W (t) \quad \text { a.s. } \tag {7.23}
$$

for all $T \geq 0$ .

# Remark 7.3

In view of this definition, the notion of a stochastic differential equation is a fiction. In fact, only stochastic integral equations of the form (7.23) have a rigorous mathematical meaning. However, it proves convenient to use stochastic differentials informally and talk of stochastic differential equations to draw on the analogy with ordinary differential equations. This analogy will be employed to solve some stochastic differential equations later on in this section.

The existence and uniqueness theorem below resembles that in the theory of ordinary differential equations, where it is also crucial for the right-hand side of the equation to be Lipschitz continuous as a function of the solution.

# Theorem 7.7

Suppose that $f$ and $g$ are Lipschitz continuous functions from $\mathbb{R}$ to $\mathbb{R}$ , i.e. there is a constant $C > 0$ such that for any $x, y \in \mathbb{R}$

$$
\begin{array}{l} \left| f (x) - f (y) \right| \leq C | x - y |, \\ \left| g (x) - g (y) \right| \leq C | x - y |. \\ \end{array}
$$

Moreover, let $\xi_{0}$ be an $F_{0}$ -measurable square integrable random variable. Then the initial value problem

$$
d \xi (t) = f (\xi (t)) d t + g (\xi (t)) d W (t), \tag {7.24}
$$

$$
\xi (0) = \xi_ {0} \tag {7.25}
$$

has a solution $\xi(t), t \geq 0$ in the class of Itô processes. The solution is unique in the sense that if $\eta(t), t \geq 0$ is another Itô process satisfying (7.24) and (7.25), then the two processes are identical a.s., that is,

$$
P \left\{\xi (t) = \eta (t) \text {   for   all   } t \geq 0 \right\} = 1.
$$

# Proof (outline)

Let us fix $T > 0$ . We are looking for a process $\xi \in M_T^2$ such that

$$
\xi (s) = \xi_ {0} + \int_ {0} ^ {s} f (\xi (t)) d t + \int_ {0} ^ {s} g (\xi (t)) d W (t) \quad \text {a.s.} \tag {7.26}
$$

for all $s \in [0, T]$ . Once we have shown that such a $\xi \in M_T^2$ exists, to obtain a solution to the stochastic differential equation (7.24) with initial condition (7.25) it suffices to take a modification of $\xi$ with a.s. continuous paths, which exists by Theorem 7.4.

To show that a solution to the stochastic integral equation (7.26) exists we shall employ the Banach fixed point theorem in $M_{T}^{2}$ with the norm

$$
\left| \left| \xi \right| \right| _ {\lambda} ^ {2} = E \int_ {0} ^ {T} e ^ {- \lambda t} | \xi (t) | ^ {2} d t, \tag {7.27}
$$

which turns $M_{T}^{2}$ into a complete normed vector space. The number $\lambda > 0$ should be chosen large enough, see below. To apply the fixed point theorem define $\Phi : M_{T}^{2} \to M_{T}^{2}$ by

$$
\Phi (\xi) (s) = \xi_ {0} + \int_ {0} ^ {s} f (\xi (t)) d t + \int_ {0} ^ {s} g (\xi (t)) d W (t) \tag {7.28}
$$

for any $\xi \in M_T^2$ and $s\in [0,T]$ . We claim that $\varPhi$ is a strict contraction, i.e.

$$
\left\| \Phi (\xi) - \Phi (\zeta) \right\| _ {\lambda} \leq \alpha \| \xi - \zeta \| _ {\lambda} \tag {7.29}
$$

for some $\alpha < 1$ and all $\xi, \zeta \in M_T^2$ . Then, by the Banach theorem, $\Phi$ has a unique fixed point $\xi = \Phi(\xi)$ . This is the desired solution to (7.26).

It remains to verify that $\Phi$ is indeed a strict contraction. It suffices to show that the two maps $\Phi_{1}$ and $\Phi_{2}$ , where

$$
\Phi_ {1} (\xi) (s) = \int_ {0} ^ {s} f (\xi (t)) d t, \quad \Phi_ {2} (\xi) (s) = \int_ {0} ^ {s} g (\xi (t)) d W (t),
$$

are strict contractions with contracting constants $\alpha_{1}$ and $\alpha_{2}$ such that $\alpha_{1} + \alpha_{2} < 1$ . For $\Phi_{1}$ this follows from the Lipschitz continuity of $f$ . For $\Phi_{2}$ we need to use the Lipschitz continuity of $g$ and the isometry property of the Itô integral. Let us mention just one essential step in the latter case. For any $\xi, \zeta \in M_{T}^{2}$

$$
\begin{array}{l} \left\| \Phi_ {2} (\xi) - \Phi_ {2} (\zeta) \right\| _ {\lambda} ^ {2} = E \int_ {0} ^ {T} e ^ {- \lambda s} \left| \int_ {0} ^ {s} [ g (\xi (t)) - g (\zeta (t)) ] d W (t) \right| ^ {2} d s \\ = E \int_ {0} ^ {T} e ^ {- \lambda s} \int_ {0} ^ {s} | g (\xi (t)) - g (\zeta (t)) | ^ {2} d t d s \\ \leq C ^ {2} E \int_ {0} ^ {T} e ^ {- \lambda s} \int_ {0} ^ {s} | \xi (t) - \zeta (t) | ^ {2} d t d s \\ \end{array}
$$

$$
\begin{array}{l} = C ^ {2} E \int_ {0} ^ {T} \left(\int_ {t} ^ {T} e ^ {- \lambda s} e ^ {\lambda t} d s\right) e ^ {- \lambda t} | \xi (t) - \zeta (t) | ^ {2} d t \\ \leq \frac {C ^ {2}}{\lambda} E \int_ {0} ^ {T} e ^ {- \lambda t} | \xi (t) - \zeta (t) | ^ {2} d t = \frac {C ^ {2}}{\lambda} \| \xi - \zeta \| _ {\lambda} ^ {2}, \\ \end{array}
$$

since $\int_t^T e^{-\lambda s}e^{\lambda t}ds = \frac{1}{\lambda} (1 - e^{-\lambda (T - t)})\leq \frac{1}{\lambda}$ . Here $C$ is the Lipschitz constant of $g$ . If $\lambda >C^2 /\varepsilon$ , then $\varPhi_2$ is a strict contraction with contracting constant $\leq \varepsilon$ .

There remain some technical points to be settled, but the main idea of the proof is shown above. □

# Exercise 7.17

Find a solution of the stochastic differential equation

$$
d X (t) = - \alpha X (t) d t + \sigma d W (t)
$$

with initial condition $X(0) = x_{0}$ , where $x_{0}$ is an arbitrary real number. Show that the solution is unique.

Hint Use the substitution $Y(t) = e^{at}X(t)$ .

A linear stochastic differential equation has the general form

$$
d X (t) = a X (t) d t + b X (t) d W (t), \tag {7.30}
$$

where a and b are real numbers. In particular, for a = 0 and b = 1 we obtain the stochastic differential equation $dX(t) = X(t) \, dW(t)$ in Example 7.6. The solution to the initial value problem for any linear stochastic differential equation can be found by exploiting the analogy with ordinary differential equations, as presented in the exercises below.

# Exercise 7.18

Suppose that $w(t)$ , $t \geq 0$ is a deterministic real-valued function of class $C^{1}$ such that $w(0) = 0$ . Solve the ordinary differential equation

$$
d x (t) = a x (t) d t + b x (t) d w (t), \tag {7.31}
$$

with initial condition $x(0) = x_0$ to find that

$$
x (t) = x _ {0} e ^ {a t + b w (t)}. \tag {7.32}
$$

(We write $dw(t)$ in place of $w'(t)dt$ to emphasize the analogy with stochastic differential equations.)

![](images/595411dd39de56411c2b761afc90b330c079df9baa04197538dd85e47ef354b2.jpg)

Hint The variables can be separated:

$$
\frac {d x (t)}{x (t)} = \left(a + b w ^ {\prime} (t)\right) d t.
$$

By analogy with the deterministic solution (7.32), let us consider a process defined by

$$
X (t) = X _ {0} e ^ {a t + b W (t)} \tag {7.33}
$$

for any $t \geq 0$ , where $W(t)$ is a Wiener process.

# Exercise 7.19

Show that $X(t)$ defined by (7.33) is a solution of the linear stochastic differential equation

$$
d X (t) = \left(a + \frac {b ^ {2}}{2}\right) X (t) d t + b X (t) d W (t), \tag {7.34}
$$

with initial condition $X(0) = X_0$ .

Hint Use the Itô formula with $F(t, x) = e^{at + bx}$ .

# Exercise 7.20

Show that the linear stochastic differential equation

$$
d X (t) = a X (t) d t + b X (t) d W (t)
$$

with initial condition $X(0) = X_0$ has a unique solution given by

$$
X (t) = X _ {0} e ^ {(a - \frac {b ^ {2}}{2}) t + b W (t)}.
$$

Hint Apply the result of Exercise 7.19 with suitably redefined constants.

Having solved the general linear stochastic differential equation (7.30), let us consider an example of a non-linear stochastic differential equation. Once again, we begin with a deterministic problem.

# Exercise 7.21

Suppose that $w(t), t \geq 0$ is a deterministic real-valued function of class $C^1$ such that $w(0) = 0$ . Solve the ordinary differential equation

$$
d x (t) = \sqrt {1 + x (t) ^ {2}} d t + \sqrt {1 + x (t) ^ {2}} d w (t)
$$

with initial condition $x(0) = x_0$ .

Hint The variables in this differential equation can be separated.

# Exercise 7.22

Show that the process defined by

$$
X (t) = \sinh (C + t + W (t)),
$$

where $W(t)$ is a Wiener process and $C = \sinh^{-1} X_{0}$ , is a solution of the stochastic differential equation

$$
d X (t) = \left(\sqrt {1 + X (t) ^ {2}} + \frac {1}{2} X (t)\right) d t + \left(\sqrt {1 + X (t) ^ {2}}\right) d W (t)
$$

with initial condition $X(0) = X_0$ .

Hint Use the Itô formula with $F(t, x) = \sinh (t + x)$ .

We shall conclude this chapter with an example of a stochastic differential equation which does not satisfy the assumptions of Theorem 7.7. It turns out that the solution may fail to exist for all times $t \geq 0$ . This is a familiar phenomenon in ordinary differential equations. However, stochastic differential equations add a new effect, which does not even make sense in the deterministic case: the maximum time of existence of the solution, called the explosion time may be a (non-constant) random variable, in fact a stopping time.

# Example 7.8

Consider the stochastic differential equation

$$
d X (t) = X (t) ^ {3} d t + X (t) ^ {2} d W (t).
$$

Then

$$
X (t) = \frac {1}{1 - W (t)}
$$

is a solution, which can be verified, at least formally, by using the Itô formula with $F(t,x) = \frac{1}{1 - x}$ . The solution $X(t)$ exists only up to the first hitting time

$$
\tau = \inf \left\{t \geq 0: W (t) = 1 \right\}
$$

This is the explosion time of $X(t)$ . Observe that

$$
\lim _ {t \nearrow r} X (t) = \infty .
$$

Strictly speaking, the Itô formula stated in Theorem 7.6 does not cover this case, since $F(t, x) = \frac{1}{1 - x}$ has a singularity at $x = 1$ . Definition 7.9 does not apply either, as it requires the solution $X(t)$ to be defined for all $t \geq 0$ . Suitable extensions of the Itô formula and the definition of a solution are required to study stochastic differential equations involving explosions. However, to prevent an explosion of this book, we have to refer the interested reader to a further course in stochastic analysis.

# 7.6 Solutions

# Solution 7.1

Using the first identity in the hint we obtain

$$
\begin{array}{l} \sum_ {j = 0} ^ {n - 1} W \left(t _ {j} ^ {n}\right) \left(W \left(t _ {j + 1} ^ {n}\right) - W \left(t _ {j} ^ {n}\right)\right) = \frac {1}{2} \sum_ {j = 0} ^ {n - 1} \left(W \left(t _ {j + 1} ^ {n}\right) ^ {2} - W \left(t _ {j} ^ {n}\right) ^ {2}\right) \\ - \frac {1}{2} \sum_ {j = 0} ^ {n - 1} \left(W \left(t _ {j + 1} ^ {n}\right) - W \left(t _ {j} ^ {n}\right)\right) ^ {2} \\ = \frac {1}{2} W (T) ^ {2} - \frac {1}{2} \sum_ {j = 0} ^ {n - 1} \left(W \left(t _ {j + 1} ^ {n}\right) - W \left(t _ {j} ^ {n}\right)\right) ^ {2}. \\ \end{array}
$$

By Exercise 6.29 the limit is

$$
\lim _ {n \rightarrow \infty} \sum_ {j = 0} ^ {n - 1} W (t _ {j} ^ {n}) \left(W (t _ {j + 1} ^ {n}) - W (t _ {j} ^ {n})\right) = \frac {1}{2} W (T) ^ {2} - \frac {1}{2} T.
$$

Similarly, the second identity in the hint enables us to write

$$
\begin{array}{l} \sum_ {j = 0} ^ {n - 1} W \left(t _ {j + 1} ^ {n}\right) \left(W \left(t _ {j + 1} ^ {n}\right) - W \left(t _ {j} ^ {n}\right)\right) = \frac {1}{2} \sum_ {j = 0} ^ {n - 1} \left(W \left(t _ {j + 1} ^ {n}\right) ^ {2} - W \left(t _ {j} ^ {n}\right) ^ {2}\right) \\ + \frac {1}{2} \sum_ {j = 0} ^ {n - 1} \left(W \left(t _ {j + 1} ^ {n}\right) - W \left(t _ {j} ^ {n}\right)\right) ^ {2} \\ = \frac {1}{2} W (T) ^ {2} + \frac {1}{2} \sum_ {j = 0} ^ {n - 1} \left(W \left(t _ {j + 1} ^ {n}\right) - W \left(t _ {j} ^ {n}\right)\right) ^ {2}. \\ \end{array}
$$

It follows that

$$
\lim _ {n \rightarrow \infty} \sum_ {j = 0} ^ {n - 1} W (t _ {j + 1} ^ {n}) \left(W (t _ {j + 1} ^ {n}) - W (t _ {j} ^ {n})\right) = \frac {1}{2} W (T) ^ {2} + \frac {1}{2} T.
$$

# Solution 7.2

For any random step processes $f, g \in M_{\text{step}}^2$ there is a partition $0 = t_0 < t_1 < \cdots < t_n$ such that for any $t \geq 0$

$$
f (t) = \sum_ {j = 0} ^ {n - 1} \eta_ {j} 1 _ {[ t _ {j}, t _ {j + 1})} (t) \quad \text { and } \quad g (t) = \sum_ {j = 0} ^ {n - 1} \zeta_ {j} 1 _ {[ t _ {j}, t _ {j + 1})} (t),
$$

where $\eta_j$ and $\zeta_j$ are square integrable $\mathcal{F}_{t_j}$ -measurable random variables for each $j = 0, 1, \ldots, n - 1$ . (If the two partitions in the formulae for $f$ and $g$ happen to be different, then it is always possible to find a common refinement of the two partitions.)

As in the proof of Proposition 7.1, we denote the increment $W(t_{j+1}) - W(t_j)$ by $\Delta_j W$ and $t_{j+1} - t_j$ by $\Delta_j t$ . Then

$$
\begin{array}{l} I (f) I (g) = \sum_ {j = 0} ^ {n - 1} \sum_ {k = 0} ^ {n - 1} \eta_ {j} \zeta_ {k} \Delta_ {j} W \Delta_ {k} W \\ = \sum_ {j = 0} ^ {n - 1} \eta_ {j} \zeta_ {j} | \Delta_ {j} W | ^ {2} + \sum_ {j <   k} \eta_ {j} \zeta_ {k} \Delta_ {j} W \Delta_ {k} W + \sum_ {j <   k} \zeta_ {j} \eta_ {k} \Delta_ {j} W \Delta_ {k} W, \\ \end{array}
$$

where, by independence,

$$
E \left(\eta_ {j} \zeta_ {j} | \varDelta_ {j} W | ^ {2}\right) = E \left(\eta_ {j} \zeta_ {j}\right) E \left(| \varDelta_ {j} W | ^ {2}\right) = E \left(\eta_ {j} \zeta_ {j}\right) \varDelta_ {j} t
$$

and

$$
E \left(\eta_ {j} \zeta_ {k} \Delta_ {j} W \Delta_ {k} W\right) = E \left(\eta_ {j} \zeta_ {k} \Delta_ {j} W\right) E \left(\Delta_ {k} W\right) = 0
$$

$$
E \left(\zeta_ {j} \eta_ {k} \Delta_ {j} W \Delta_ {k} W\right) = E \left(\zeta_ {j} \eta_ {k} \Delta_ {j} W\right) E \left(\Delta_ {k} W\right) = 0
$$

for any $j < k$ . It follows that

$$
E (I (f) I (g)) = \sum_ {j = 0} ^ {n - 1} E (\eta_ {j} \zeta_ {j}) \Delta_ {j} t.
$$

Therefore, it suffices to show that

$$
E \left(\int_ {0} ^ {\infty} f (t) g (t) d t\right) = \sum_ {j = 0} ^ {n - 1} E \left(\eta_ {j} \zeta_ {j}\right) \Delta_ {j} t,
$$

but this is true because

$$
\begin{array}{l} f (t) g (t) = \sum_ {j = 0} ^ {n - 1} \sum_ {k = 0} ^ {n - 1} \eta_ {j} \zeta_ {k} 1 _ {[ t _ {j}, t _ {j + 1})} (t) 1 _ {[ t _ {k}, t _ {k + 1})} (t) \\ = \sum_ {j = 0} ^ {n - 1} \eta_ {j} \zeta_ {j} 1 _ {\{t _ {j}, t _ {j + 1})} (t). \\ \end{array}
$$

# Solution 7.3

We shall use a partition $0 = t_{0} < t_{1} < \cdots < t_{n}$ such that

$$
f = \sum_ {j = 0} ^ {n - 1} \eta_ {j} 1 _ {[ t _ {j}, t _ {j + 1})} \quad \text { and } \quad g = \sum_ {j = 0} ^ {n - 1} \zeta_ {j} 1 _ {[ t _ {j}, t _ {j + 1})},
$$

where $\eta_j$ and $\zeta_j$ are square integrable $\mathcal{F}_{t_j}$ -measurable random variables for each $j = 0,1,\ldots,n-1$ . (If the two partitions in the formulae for $f$ and $g$ happen to be different, then it is always possible to find a common refinement of the two partitions.) The increments $W(t_{j+1}) - W(t_j)$ will be denoted by $\Delta_j W$ for brevity. Then

$$
\alpha f + \beta g = \sum_ {j = 0} ^ {n - 1} \left(\alpha \eta_ {j} + \beta \zeta_ {j}\right) \mathbf {1} _ {\left[ t _ {j}, t _ {j + 1}\right)}
$$

and

$$
\begin{array}{l} I (\alpha f + \beta g) = \sum_ {j = 0} ^ {n - 1} \left(\alpha \eta_ {j} + \beta \zeta_ {j}\right) \Delta_ {j} W \\ = \alpha \sum_ {j = 0} ^ {n - 1} \eta_ {j} \Delta_ {j} W + \beta \sum_ {j = 0} ^ {n - 1} \zeta_ {j} \Delta_ {j} W \\ = \alpha I (f) + \beta I (g). \\ \end{array}
$$

# Solution 7.4

Consider the following scalar products in $M^{2}$ and $L^{2}$ :

$$
\langle f, g \rangle_ {M ^ {2}} = E \left(\int_ {0} ^ {\infty} f (t) g (t) d t\right) \quad \text { and } \quad \langle \eta , \zeta \rangle_ {L ^ {2}} = E (\eta \zeta)
$$

for any $f, g \in M^{2}$ and $\eta, \zeta \in L^{2}$ . They can be expressed in terms of the corresponding norms defined in the proof of Proposition 7.2,

$$
\langle f, g \rangle_ {M ^ {2}} = \frac {1}{4} \| f + g \| _ {M ^ {2}} ^ {2} - \frac {1}{4} \| f - g \| _ {M ^ {2}} ^ {2},
$$

$$
\langle \eta , \zeta \rangle_ {L ^ {2}} = \frac {1}{4} \| \eta + \zeta \| _ {L ^ {2}} ^ {2} - \frac {1}{4} \| \eta - \zeta \| _ {L ^ {2}} ^ {2}.
$$

Therefore Proposition 7.2 implies that

$$
\langle I (f), I (g) \rangle_ {L ^ {2}} = \langle f, g \rangle_ {M ^ {2}},
$$

which is the same as the equality to be proved.

# Solution 7.5

If $f \in M_{\text{step}}^2$ is a random step process, then so is $1_{[0,t]}f \in M_{\text{step}}^2 \subset M^2$ for any $t > 0$ . This in turn implies that $f \in M_t^2$ for any $t > 0$ .

We shall verify that $I_{t}(f)$ is a martingale with respect to the filtration $F_{t}$ . Let $0 \leq s < t$ and suppose that $f \in M_{step}^{2}$ can be written in the form (7.2), where

$$
0 = t _ {0} <   t _ {1} <   \dots <   t _ {k} = s <   t _ {k + 1} <   \dots <   t _ {m} = t <   t _ {m + 1} <   \dots <   t _ {n}.
$$

Such a partition $t_0, \ldots, t_n$ can always be obtained by adding the points $s$ and $t$ if necessary. We shall denote the increment $W(t_{j+1}) - W(t_j)$ by $\Delta_j W$ as in the proof of Proposition 7.1. Then

$$
1 _ {[ 0, t ]} f = \sum_ {j = 0} ^ {m - 1} \eta_ {j} 1 _ {[ t _ {j}, t _ {j + 1} ]}
$$

and

$$
I _ {t} (f) = I \left(1 _ {[ 0, t ]} f\right) = \sum_ {j = 0} ^ {m - 1} \eta_ {j} \Delta_ {j} W,
$$

which is adapted to $\mathcal{F}_t$ and square integrable, and so integrable. It remains to compute

$$
E \left(I _ {t} (f) | \mathcal {F} _ {s}\right) = E \left(I (1 _ {[ 0, t ]} f) | \mathcal {F} _ {s}\right) = \sum_ {j = 0} ^ {m - 1} E \left(\eta_ {j} \Delta_ {j} W | \mathcal {F} _ {s}\right).
$$

If $j < k$ , then $\eta_j$ and $\Delta_j W$ are $\mathcal{F}_s$ -measurable and

$$
E \left(\eta_ {j} \Delta_ {j} W | \mathcal {F} _ {s}\right) = \eta_ {j} \Delta_ {j} W.
$$

If $j \geq k$ , then $\mathcal{F}_s \subset \mathcal{F}_{t_j}$ and

$$
\begin{array}{l} E \left(\eta_ {j} \Delta_ {j} W | \mathcal {F} _ {s}\right) = E \left(E \left(\eta_ {j} \Delta_ {j} W | \mathcal {F} _ {t _ {j}}\right) | \mathcal {F} _ {s}\right) \\ = E \left(\eta_ {j} E \left(\Delta_ {j} W \mid \mathcal {F} _ {t _ {j}}\right) \mid \mathcal {F} _ {s}\right) \\ = E \left(\eta_ {j} \mid \mathcal {F} _ {s}\right) E \left(\Delta_ {j} W\right) = 0, \\ \end{array}
$$

since $\eta_j$ is $\mathcal{F}_{t_j}$ -measurable and $\Delta_j W$ is independent of $\mathcal{F}_{t_j}$ . It follows that

$$
E \left(I _ {t} (f) | \mathcal {F} _ {s}\right) = \sum_ {j = 0} ^ {k - 1} \eta_ {j} \Delta_ {j} W = I (1 _ {[ 0, s ]} f) = I _ {s} (f).
$$

# Solution 7.6

By definition, $W(t)$ is adapted to the filtration $\mathcal{F}_t$ and has a.s. continuous paths. Moreover,

$$
\begin{array}{l} E \left(\int_ {0} ^ {T} | W (t) | ^ {2} d t\right) = \int_ {0} ^ {T} E \left(| W (t) | ^ {2}\right) d t \\ = \int_ {0} ^ {T} t d t <   \infty . \\ \end{array}
$$

By Theorem 7.1 it follows that the Wiener process $W$ belongs to $M_T^2$ .

# Solution 7.7

Since $W(t)$ is adapted to the filtration $\mathcal{F}_t$ , so is $W(t)^2$ . Moreover,

$$
\begin{array}{l} E \left(\int_ {0} ^ {T} | W (t) | ^ {4} d t\right) = \int_ {0} ^ {T} E \left(| W (t) | ^ {4}\right) d t \\ = \int_ {0} ^ {T} 3 t ^ {2} d t <   \infty . \\ \end{array}
$$

Theorem 7.1 implies that $W(t)^2$ belongs to $M_T^2$ .

# Solution 7.8

We fix $T > 0$ and put

$$
f (t) = 1 _ {[ 0, T)} (t) W (t).
$$

Then $f\in M^2$ and

$$
\int_ {0} ^ {T} W (t) d W (t) = \int_ {0} ^ {\infty} f (t) d W (t).
$$

Take $0 = t_{0}^{n} < t_{1}^{n} < \cdots < t_{n}^{n} = T$ , where $t_{i}^{n} = \frac{iT}{n}$ , to be a partition of $[0, T]$ into n equal parts, and put

$$
f _ {n} = \sum_ {i = 0} ^ {n - 1} W (t _ {i} ^ {n}) 1 _ {\left\{t _ {i} ^ {n}, t _ {i + 1} ^ {n}\right)}.
$$

Then the sequence $f_{1}, f_{2}, \ldots \in M_{\mathrm{step}}^{2}$ approximates $f$ , since

$$
\begin{array}{l} E \left(\int_ {0} ^ {\infty} | f (t) - f _ {n} (t) | ^ {2} d t\right) = \sum_ {i = 0} ^ {n - 1} \int_ {t _ {i} ^ {n}} ^ {t _ {i + 1} ^ {n}} E \left(| W (t) - W \left(t _ {i} ^ {n}\right) | ^ {2}\right) d t \\ = \sum_ {i = 0} ^ {n - 1} \int_ {t _ {i} ^ {n}} ^ {t _ {i + 1} ^ {n}} \left(t - t _ {i} ^ {n}\right) d t \\ = \frac {1}{2} \sum_ {i = 0} ^ {n - 1} \left(t _ {i + 1} ^ {n} - t _ {i} ^ {n}\right) ^ {2} \\ = \frac {1}{2} \frac {T ^ {2}}{n} \rightarrow 0 \quad \text { as } n \rightarrow \infty . \\ \end{array}
$$

By Exercise 7.1

$$
I (f _ {n}) = \sum_ {i = 0} ^ {n - 1} W (t _ {i} ^ {n}) \left(W (t _ {i + 1} ^ {n}) - W (t _ {i} ^ {n})\right)\rightarrow \frac {1}{2} W (T) ^ {2} - \frac {1}{2} T
$$

in $L^2$ as $n\to \infty$ . We have found, therefore, that

$$
\int_ {0} ^ {T} W (t) d W (t) = \frac {1}{2} W (T) ^ {2} - \frac {1}{2} T.
$$

# Solution 7.9

Let $f(t) = t$ . Then $1_{[0,T]}f$ belongs to $M_T^2$ . We shall use the same partition of $[0,T]$ into $n$ equal parts as in Solution 7.8. The sequence

$$
f _ {n} = \sum_ {i = 0} ^ {n - 1} t _ {i} ^ {n} 1 _ {\left[ t _ {i} ^ {n}, t _ {i + 1} ^ {n}\right)} \in M _ {\text { step }} ^ {2}
$$

approximates $1_{[0,T]}f$ , since

$$
\begin{array}{l} E \left(\int_ {0} ^ {\infty} | 1 _ {[ 0, T ]} f (t) - f _ {n} (t) | ^ {2} d t\right) = E \left(\int_ {0} ^ {T} | f (t) - f _ {n} (t) | ^ {2} d t\right) \\ = \sum_ {i = 1} ^ {n - 1} \int_ {t _ {i} ^ {n}} ^ {t _ {i + 1} ^ {n}} \left| t - t _ {i} ^ {n} \right| ^ {2} d t \\ = \frac {1}{3} \sum_ {i = 1} ^ {n - 1} \frac {T ^ {3}}{n ^ {3}} \\ = \frac {T ^ {3}}{3 n ^ {2}} \rightarrow 0 \quad \text { as } n \rightarrow \infty . \\ \end{array}
$$

With the aid of the identity in the hint, we can write the stochastic integral of $f_{n}$ as

$$
\begin{array}{l} I \left(f _ {n}\right) = \sum_ {i = 0} ^ {n - 1} t _ {i} ^ {n} \left(W \left(t _ {i + 1} ^ {n}\right) - W \left(t _ {i} ^ {n}\right)\right) \\ = \sum_ {i = 0} ^ {n - 1} \left(t _ {i + 1} ^ {n} W \left(t _ {i + 1} ^ {n}\right) - t _ {i} ^ {n} W \left(t _ {i} ^ {n}\right)\right) - \sum_ {i = 0} ^ {n - 1} W \left(t _ {i + 1} ^ {n}\right) \left(t _ {i + 1} ^ {n} - t _ {i} ^ {n}\right) \\ = T W (T) - \sum_ {i = 0} ^ {n - 1} W \left(t _ {i + 1} ^ {n}\right) \left(t _ {i + 1} ^ {n} - t _ {i} ^ {n}\right). \\ \end{array}
$$

It follows that

$$
I (f _ {n}) \rightarrow T W (T) - \int_ {0} ^ {T} W (t) d t
$$

in $L^2$ as $n \to \infty$ . Indeed, by the classical inequality $\left|\sum_{i=0}^{n-1} a_i\right|^2 \leq n \sum_{i=0}^{n-1} |a_i|^2$ and by the Cauchy-Schwartz inequality

$$
E \left(\left| \sum_ {i = 0} ^ {n - 1} W (t _ {i + 1} ^ {n}) \left(t _ {i + 1} ^ {n} - t _ {i} ^ {n}\right) - \int_ {0} ^ {T} W (t) d t \right| ^ {2}\right)
$$

$$
= E \left(\left| \sum_ {i = 0} ^ {n - 1} \left(\int_ {t _ {i} ^ {n}} ^ {t _ {i + 1} ^ {n}} \left(W \left(t _ {i + 1} ^ {n}\right) - W (t)\right) d t\right) \right| ^ {2}\right)
$$

$$
\leq n \sum_ {i = 0} ^ {n - 1} E \left(\left| \int_ {t _ {i} ^ {n}} ^ {t _ {i + 1} ^ {n}} \left(W \left(t _ {i + 1} ^ {n}\right) - W (t)\right) d t \right| ^ {2}\right)
$$

$$
\leq n \sum_ {i = 0} ^ {n - 1} \left(t _ {i + 1} ^ {n} - t _ {i} ^ {n}\right) E \left(\int_ {t _ {i} ^ {n}} ^ {t _ {i + 1} ^ {n}} \left| W \left(t _ {i + 1} ^ {n}\right) - W (t) \right| ^ {2} d t\right)
$$

$$
= n \sum_ {i = 0} ^ {n - 1} \frac {\left(t _ {i + 1} ^ {n} - t _ {i} ^ {n}\right) ^ {3}}{2} = n \sum_ {i = 0} ^ {n - 1} \frac {T ^ {3}}{2 n ^ {3}} = \frac {T ^ {3}}{2 n} \rightarrow 0 \quad \text { as } n \rightarrow \infty .
$$

This proves the equality in the exercise.

# Solution 7.10

Using the same partition of $[0, T]$ into $n$ equal parts as in Solution 7.8 and putting

$$
f _ {n} = \sum_ {i = 0} ^ {n - 1} W (t _ {i} ^ {n}) ^ {2} 1 _ {[ t _ {i} ^ {n}, t _ {i + 1} ^ {n})},
$$

we obtain a sequence $f_1, f_2, \ldots \in M_{\text{step}}^2$ of random step processes which approximates $f = 1_{[0,T]}W^2$ . Indeed,

$$
E \left(\int_ {0} ^ {\infty} | f (t) - f _ {n} (t) | ^ {2} d t\right) = \sum_ {i = 0} ^ {n - 1} \int_ {t _ {i} ^ {n}} ^ {t _ {i + 1} ^ {n}} E \left(\left| W (t) ^ {2} - W \left(t _ {i} ^ {n}\right) ^ {2} \right| ^ {2}\right) d t
$$

$$
= \sum_ {i = 0} ^ {n - 1} \int_ {t _ {i} ^ {n}} ^ {t _ {i + 1} ^ {n}} \left(3 (t - t _ {i} ^ {n}) ^ {2} + 4 (t - t _ {i} ^ {n}) t _ {i} ^ {n}\right) d t
$$

$$
= \sum_ {i = 0} ^ {n - 1} \left[ \left(\frac {T}{n}\right) ^ {3} + 2 \left(\frac {T}{n}\right) ^ {2} \frac {i T}{n} \right]
$$

$$
= \frac {T ^ {3}}{n} \rightarrow 0 \quad \text { as } n \rightarrow \infty .
$$

The expectation above is computed with the aid of the following formula valid for any $0 \leq s \leq t$ :

$$
E \left(\left(W _ {t} ^ {2} - W _ {s} ^ {2}\right) ^ {2}\right) = E \left(\left(W _ {t} - W _ {s}\right) ^ {4}\right) + 4 E \left(\left(W _ {t} - W _ {s}\right) ^ {3} W _ {s}\right)
$$

$$
+ 4 E \left(\left(W _ {t} - W _ {s}\right) ^ {2} W _ {s} ^ {2}\right)
$$

$$
= 3 (t - s) ^ {2} + 4 (t - s) s
$$

Using the identity in the hint, we can write

$$
\begin{array}{l} I (f _ {n}) = \sum_ {i = 0} ^ {n - 1} W (t _ {i} ^ {n}) ^ {2} \left(W (t _ {i + 1} ^ {n}) - W (t _ {i} ^ {n})\right) \\ = \frac {1}{3} \sum_ {i = 0} ^ {n - 1} \left(W (t _ {i + 1} ^ {n}) ^ {3} - W (t _ {i} ^ {n}) ^ {3}\right) \\ - \sum_ {i = 0} ^ {n - 1} W \left(t _ {i} ^ {n}\right) \left(W \left(t _ {i + 1} ^ {n}\right) - W \left(t _ {i} ^ {n}\right)\right) ^ {2} - \frac {1}{3} \sum_ {i = 0} ^ {n - 1} \left(W \left(t _ {i + 1} ^ {n}\right) - W \left(t _ {i} ^ {n}\right)\right) ^ {3} \\ = \frac {1}{3} W (T) ^ {3} - \sum_ {i = 0} ^ {n - 1} W \left(t _ {i} ^ {n}\right) \left(t _ {i + 1} ^ {n} - t _ {i} ^ {n}\right) \\ - \sum_ {i = 0} ^ {n - 1} W \left(t _ {i} ^ {n}\right) \left[ \left(W \left(t _ {i + 1} ^ {n}\right) - W \left(t _ {i} ^ {n}\right)\right) ^ {2} - \left(t _ {i + 1} ^ {n} - t _ {i} ^ {n}\right) \right] \\ - \frac {1}{3} \sum_ {i = 0} ^ {n - 1} \left(W (t _ {i + 1} ^ {n}) - W (t _ {i} ^ {n})\right) ^ {3}. \\ \end{array}
$$

The $L^2$ limits of the last three sums are

$$
\lim _ {n \rightarrow \infty} \sum_ {i = 0} ^ {n - 1} W \left(t _ {i} ^ {n}\right)\left(t _ {i + 1} ^ {n} - t _ {i} ^ {n}\right) = \int_ {0} ^ {T} W (t) d t
$$

$$
\lim _ {n \rightarrow \infty} \sum_ {i = 0} ^ {n - 1} W \left(t _ {i} ^ {n}\right)\left[\left(W \left(t _ {i + 1} ^ {n}\right) - W \left(t _ {i} ^ {n}\right)\right) ^ {2} - \left(t _ {i + 1} ^ {n} - t _ {i} ^ {n}\right)\right] = 0
$$

$$
\lim _ {n \rightarrow \infty} \sum_ {i = 0} ^ {n - 1} \left(W \left(t _ {i + 1} ^ {n}\right) - W \left(t _ {i} ^ {n}\right)\right) ^ {3} = 0
$$

Indeed, the first limit is correct because

$$
\begin{array}{l} E \left(\left| \sum_ {i = 0} ^ {n - 1} W \left(t _ {i} ^ {n}\right) \left(t _ {i + 1} ^ {n} - t _ {i} ^ {n}\right) - \int_ {0} ^ {T} W (t) d t \right| ^ {2}\right) \\ = E \left(\left| \sum_ {i = 0} ^ {n - 1} \int_ {t _ {i} ^ {n}} ^ {t _ {i + 1} ^ {n}} \left(W \left(t _ {i} ^ {n}\right) - W (t)\right) d t \right| ^ {2}\right) \\ = \sum_ {i = 0} ^ {n - 1} \int_ {t _ {i} ^ {n}} ^ {t _ {i + 1} ^ {n}} E \left(\left| W \left(t _ {i} ^ {n}\right) - W (t) \right| ^ {2}\right) d t \\ = \sum_ {i = 0} ^ {n - 1} \int_ {t _ {i} ^ {n}} ^ {t _ {i + 1} ^ {n}} \left(t - t _ {i} ^ {n}\right) d t \\ = \frac {T ^ {2}}{2 n} \rightarrow 0 \quad \text { as } n \rightarrow \infty . \\ \end{array}
$$

To the second limit can be verified as follows:

$$
\begin{array}{l} E \left(\left| \sum_ {i = 0} ^ {n - 1} W (t _ {i} ^ {n}) \left[ \left(W (t _ {i + 1} ^ {n}) - W (t _ {i} ^ {n})\right) ^ {2} - \left(t _ {i + 1} ^ {n} - t _ {i} ^ {n}\right) \right] \right| ^ {2}\right) \\ = \sum_ {i = 0} ^ {n - 1} E \left(W \left(t _ {i} ^ {n}\right) ^ {2} \left| \left(W \left(t _ {i + 1} ^ {n}\right) - W \left(t _ {i} ^ {n}\right)\right) ^ {2} - \left(t _ {i + 1} ^ {n} - t _ {i} ^ {n}\right) \right| ^ {2}\right) \\ = \sum_ {i = 0} ^ {n - 1} E \left(W \left(t _ {i} ^ {n}\right) ^ {2}\right) E \left(\left| \left(W \left(t _ {i + 1} ^ {n}\right) - W \left(t _ {i} ^ {n}\right)\right) ^ {2} - \left(t _ {i + 1} ^ {n} - t _ {i} ^ {n}\right) \right| ^ {2}\right) \\ = 2 \sum_ {i = 0} ^ {n - 1} t _ {i} ^ {n} \left(t _ {i + 1} ^ {n} - t _ {i} ^ {n}\right) ^ {2} \\ = \frac {(n - 1)}{n ^ {2}} T ^ {2} \rightarrow 0 \quad \text { as } n \rightarrow \infty . \\ \end{array}
$$

Finally, for the third limit we have

$$
\begin{array}{l} E \left(\left| \sum_ {i = 0} ^ {n - 1} \left(W (t _ {i + 1} ^ {n}) - W (t _ {i} ^ {n})\right) ^ {3} \right| ^ {2}\right) \\ = \sum_ {i = 0} ^ {n - 1} E \left(\left(W \left(t _ {i + 1} ^ {n}\right) - W \left(t _ {i} ^ {n}\right)\right) ^ {6}\right) \\ = 6 \sum_ {i = 0} ^ {n - 1} \left(t _ {i + 1} ^ {n} - t _ {i} ^ {n}\right) ^ {3} \\ = 6 \sum_ {i = 0} ^ {n - 1} \frac {T ^ {3}}{n ^ {3}} = \frac {6 T ^ {3}}{n ^ {2}} \rightarrow 0 \quad \text { as } n \rightarrow \infty . \\ \end{array}
$$

It follows that

$$
I (f _ {n}) \rightarrow \frac {1}{3} W (T) ^ {3} - \int_ {0} ^ {T} W (t) d t,
$$

which proves the formula in the exercise.

# Solution 7.11

We shall use part 2) of Theorem 7.1 to verify that

$$
\xi (t) = \int_ {0} ^ {t} W (s) d W (s)
$$

belongs to $M_{T}^{2}$ for any $T \geq 0$ . By Theorem 7.4 $\xi(t)$ can be identified with an adapted modification having a.s. continuous trajectories. It suffices to verify that $\xi(t)$ satisfies condition (7.9). Since the stochastic integral is an isometry,

$$
E \left| \int_ {0} ^ {t} W (s) d W (s) \right| ^ {2} = E \int_ {0} ^ {t} | W (s) | ^ {2} d s = \int_ {0} ^ {t} s d s = \frac {t ^ {2}}{2}.
$$

It follows that

$$
E \int_ {0} ^ {T} | \xi (t) | ^ {2} d t = E \int_ {0} ^ {T} \left| \int_ {0} ^ {t} W (s) d W (s) \right| ^ {2} d t = \int_ {0} ^ {T} \frac {t ^ {2}}{2} d t = \frac {T ^ {3}}{6} <   \infty ,
$$

i.e. $\xi(t)$ satisfies (7.9). As a result, $\xi(t)$ belongs to $M_T^2$ .

# Solution 7.12

We shall use the equality proved in Exercise 7.10:

$$
W (T) ^ {3} = 3 \int_ {0} ^ {T} W (t) d t + 3 \int_ {0} ^ {T} W (t) ^ {2} d W (t).
$$

The process $3W(t)$ belongs to $\mathcal{L}_T^1$ for any $T \geq 0$ because it is adapted and has a.s. continuous paths, so the integral $\int_0^T |3W(t)| dt$ exists and is finite. By Exercise 7.7 the process $3W(t)^2$ belongs to $M_T^2$ for any $T \geq 0$ . It follows that $W(t)^3$ is an Itô process. Moreover, the above equation can be written in differential form as

$$
d W (t) ^ {3} = 3 W (t) d t + 3 W (t) ^ {2} d W (t),
$$

which gives a formula for the stochastic differential $dW(t)^3$ .

# Solution 7.13

It has been shown in Exercise 7.9 that

$$
T W (T) = \int_ {0} ^ {T} W (t) d t + \int_ {0} ^ {T} t d W (t).
$$

Since the Wiener process $W(t)$ is adapted and has continuous paths, it belongs to $\mathcal{L}_T^1$ , while the deterministic process $f(t) = t$ belongs to $M_T^2$ for any $T > 0$ . It follows that $tW(t)$ is an Itô process with stochastic differential

$$
d (t W (t)) = W (t) d t + t d W (t).
$$

# Solution 7.14

For $F(t, x) = e^x e^{-\frac{t}{2}}$ the partial derivatives are $F_t'(t, x) = -\frac{1}{2} e^x e^{-\frac{t}{2}}$ , $F_x'(t, x) =$ $e^x e^{-\frac{t}{2}}$ and $F_{xx}''(t,x) = e^x e^{-\frac{t}{2}}$ . Since $X(t) = e^{W(t)}e^{-\frac{t}{2}}$ , the Itô formula implies that

$$
\begin{array}{l} d X (t) = d F (t, W (t)) \\ = \left(F _ {t} ^ {\prime} (t, W (t)) + \frac {1}{2} F _ {x x} ^ {\prime \prime} (t, W (t))\right) d t + F _ {x} ^ {\prime} (t, W (t)) d W (t) \\ = \left(- \frac {1}{2} X (t) + \frac {1}{2} X (t)\right) d t + X (t) d W (t) \\ = X (t) d W (t). \\ \end{array}
$$

Because of this, to show that $X(t)$ is an Itô process we need to verify that $X(t) = e^{W(t)}e^{-\frac{t}{2}}$ belongs to $M_T^2$ for any $T > 0$ . Clearly, it is an adapted process. It was computed in Solution 6.35 that $Ee^{W(t)} = e^{\frac{t}{2}}$ , so

$$
E \int_ {0} ^ {T} | X (t) | d t = \int_ {0} ^ {T} E e ^ {W (t)} e ^ {- \frac {t}{2}} d t = \int_ {0} ^ {T} d t = T <   \infty ,
$$

which proves that $X(t)$ belongs to $M_{T}^{2}$ .

# Solution 7.15

Take $F(t, x) = x^n$ . Then $F_t'(t, x) = 0$ , $F_x'(t, x) = nx^{n-1}$ and $F_{xx}''(t, x) = n(n-1)x^{n-2}$ . The derivatives of $F(t, x)$ are obviously continuous, so we only need to verify that $F_x'(t, W(t)) = nW(t)^{n-1}$ belongs to $M_T^2$ for $T \geq 0$ . Clearly, it is adapted and has a.s. continuous paths. Moreover,

$$
E \int_ {0} ^ {T} | n W (t) ^ {n - 1} | ^ {2} d t = n ^ {2} \int_ {0} ^ {T} E | W (t) | ^ {2 n - 2} d t = \int_ {0} ^ {T} a _ {2 n - 2} t ^ {n - 1} d t <   \infty ,
$$

where $a_{k} = 2^{k/2}\pi^{-1/2}\Gamma\left(\frac{k+1}{2}\right)$ and $\Gamma(x) = \int_{0}^{\infty} t^{x-1} e^{-t} dt$ is the Euler gamma function. It follows by part 2) of Theorem 7.1 that $F_{x}'(t, W(t)) = nW(t)^{n-1}$ belongs to $M_{T}^{2}$ . Therefore we can apply the Itô formula to get

$$
d (W (t) ^ {n}) = \frac {n (n - 1)}{2} W (t) ^ {n - 2} d t + n W (t) ^ {n - 1} d W (t),
$$

as required.

# Solution 7.16

Some elementary calculus shows that $F(t, x) = e^{-\alpha t}x$ has continuous partial derivatives such that $F_t'(t, x) = -\alpha e^{-\alpha t}x$ , $F_x'(t, x) = e^{-\alpha t}$ and $F_{xx}''(t, x) = 0$ . Clearly, $\xi(t) = \sigma \int_0^t e^{\alpha s} dW(s)$ is an Itô process with

$$
d \xi (t) = \sigma e ^ {\alpha t} d W (t).
$$

Since the function $\sigma e^{\alpha t}F_x'(t,x)$ is bounded on each set of the form $[0,T]\times\mathbb{R}$ , it follows immediately that $\sigma e^{\alpha t}F_x'(t,\xi(t))$ belongs to $M_T^2$ for any $T\geq 0$ . As a consequence, we can use the Itô formula (the general case in Theorem 7.6) to get

$$
\begin{array}{l} d Y (t) = d \left(e ^ {- \alpha t} \xi (t)\right) \\ = - \alpha e ^ {- \alpha t} \xi (t) d t + e ^ {- \alpha t} \sigma e ^ {\alpha t} d W (t) \\ = - \alpha Y (t) d t + \sigma d W (t), \\ \end{array}
$$

which proves that $Y(t)$ satisfies the equality

$$
d Y (t) = - \alpha Y (t) d t + \sigma d W (t).
$$

# Solution 7.17

Take $F(t,x) = e^{\alpha t}x$ and consider the process

$$
Y (t) = F (t, X (t)).
$$

Then $Y(0) = x_0$ and

$$
\begin{array}{l} d Y (t) = d F (t, X (t)) \\ = \left(F _ {t} ^ {\prime} (t, X (t)) - \alpha X (t) F _ {x} ^ {\prime} (t, X (t)) + \frac {1}{2} \sigma^ {2} F _ {x x} ^ {\prime \prime} (t, X (t))\right) d t \\ + \sigma F _ {x} ^ {\prime} (t, X (t)) d W (t) \\ = \left(\alpha e ^ {\alpha t} X (t) - \alpha e ^ {\alpha t} X (t)\right) d t + \sigma e ^ {\alpha t} d W (t) \\ = \sigma e ^ {\alpha t} d W (t). \\ \end{array}
$$

by the Itô formula. It follows that

$$
Y (t) = x _ {0} + \sigma \int_ {0} ^ {t} e ^ {\alpha s} d W (s)
$$

and

$$
\begin{array}{l} X (t) = e ^ {- \alpha t} Y (t) \\ = e ^ {- \alpha t} x _ {0} + \sigma e ^ {- \alpha t} \int_ {0} ^ {t} e ^ {\alpha s} d W (s). \\ \end{array}
$$

Uniqueness follows directly from the above argument, but Theorem 7.7 can also be used. Namely, the stochastic differential equation

$$
d X (t) = - \alpha X (t) d t + \sigma d W (t)
$$

is of the form (7.24) with $f(x) = -\alpha x$ and $g(x) = \sigma$ , which are Lipschitz continuous functions. Therefore, the solution to the initial value problem must be unique in the class of Itô processes with a.s. continuous paths.

# Solution 7.18

According to the theory of ordinary differential equations, (7.31) with initial condition $x(0) = x_0$ has a unique solution. If $x_0 = 0$ , then $x(t) = 0$ is the solution. If $x_0 \neq 0$ , then

$$
\ln \frac {x (t)}{x _ {0}} = a t + w (t)
$$

by integrating the equation in the hint, which implies that

$$
\boldsymbol {x} (t) = \boldsymbol {x} _ {0} e ^ {\boldsymbol {a t} + \boldsymbol {b w} (t)}.
$$

# Solution 7.19

By the Itô formula (verify the assumptions!)

$$
\begin{array}{l} d X (t) = d \left(X _ {0} e ^ {a t + b W (t)}\right) \\ = \left(a X _ {0} e ^ {a t + b W (t)} + \frac {b ^ {2}}{2} X _ {0} e ^ {a t + b W (t)}\right) d t + b X _ {0} e ^ {a t + b W (t)} d W (t) \\ = \left(a + \frac {b ^ {2}}{2}\right) X (t) d t + b X (t) d W (t). \\ \end{array}
$$

This proves that $X(t)$ satisfies the stochastic differential equation (7.34). As regards the initial condition, we have

$$
X (0) = \left. X _ {0} e ^ {a t + b W (t)} \right| _ {t = 0} = X _ {0}.
$$

# Solution 7.20

The stochastic differential equation

$$
d X (t) = a X (t) d t + b X (t) d W (t)
$$

can be written as

$$
d X (t) = \left(c + \frac {b ^ {2}}{2}\right) X (t) d t + b X (t) d W (t),
$$

where $c = a - \frac{b^2}{2}$ . By Exercise 7.19 the solution this stochastic differential equation with initial condition $X(0) = X_0$ is

$$
\begin{array}{l} X (t) = X _ {0} e ^ {c t + b W (t)} \\ = X _ {0} e ^ {\left(a - \frac {b ^ {2}}{2}\right) t + b W (t)}. \\ \end{array}
$$

The uniqueness of this solution follows immediately from Theorem 7.7.

# Solution 7.21

We can write the ordinary differential equation to be solved in the form

$$
\frac {d x (t)}{\sqrt {1 + x (t) ^ {2}}} = \left(1 + w ^ {\prime} (t)\right) d t,
$$

which implies that

$$
\sinh^ {- 1} x (t) - \sinh^ {- 1} x _ {0} = t + w (t).
$$

Composing the last formula with sinh, we obtain

$$
\boldsymbol {x} (t) = \sinh (c + t + w (t)), \tag {7.35}
$$

where $c = \sinh^{-1}x_0$ .

# Solution 7.22

Since $F(t, x) = \sinh (t + x)$ satisfies the assumptions of the Itô formula,

$$
\begin{array}{l} d X (t) = d F (t, C + W (t)) \\ = \left(F _ {t} ^ {\prime} (t, C + W (t)) + \frac {1}{2} F _ {x x} ^ {\prime \prime} (t, C + W (t))\right) d t \\ + F _ {x} ^ {\prime} (t, C + W (t)) d W (t) \\ = \left(\cosh (C + t + W (t)) + \frac {1}{2} \sinh (C + t + W (t))\right) d t \\ + \cosh (C + t + W (t)) d W (t) \\ = \left(\sqrt {1 + \sinh^ {2} (C + t + W (t))} + \frac {1}{2} \sinh (C + t + W (t))\right) d t \\ + \sqrt {1 + \sinh^ {2} (C + t + W (t))} d W (t) \\ = \left(\sqrt {1 + X (t) ^ {2}} + \frac {1}{2} X (t)\right) d t + \left(\sqrt {1 + X (t) ^ {2}}\right) d W (t). \\ \end{array}
$$

The initial condition $X(0) = \sinh C = X_0$ is also satisfied.

a.s. see almost surely

absolutely continuous distribution 5

adapted process 140

adapted sequence of random variables 48

almost surely 2

aperiodic state 105

Bachelier 179

Borel function 4

Borel sets 2

Borel-Cantelli lemma 3

Brownian motion see Wiener process

Chapman-Kolmogorov equation 92

closed set of states 107

conditional density 33

conditional expectation 17

\- and independence 29

\- given a discrete random variable 19

\- given a sigma-field 27

\- given an arbitrary random variable 22

\- given an event 17

-linearity of 29

\- positivity 29

\- tower property 29

conditional probability 8, 18, 22, 27

convex function 31

De Morgan's law 11

density 5

\- joint 6

diffusion equation 150

discrete distribution 5

discrete time 45

distribution

\- absolutely continuous 5

\- discrete 5

\- exponential 140

\- gamma 149

\- joint 6

\- normal 152

\- of a random variable 4

\- Poisson 143

distribution function 4

Doob's maximal inequality 68

Doob's theorem 71

Doob-Dynkin lemma 4

ergodic Markov chain 113

ergodic state 105

events 2

\- contracting sequence of 3

\- expanding sequence of 2

-independent 8

\- pairwise disjoint 2

expectation 6

\- conditional 17,19

explosion time 208

exponential distribution 140

exponential martingale 160

Fatou lemma 109

filtration 47,139

first entry time 55

first hitting time 54

function

\- Borel 4

-convex 31

- distribution 4   
-indicator 6,18   
- step 6

gambling strategy 52

gamma distribution 149

increments

\- independent 148

\- stationary 148

independence 8

independent

\- events 8

\- increments 148

\- random variables 9

\- sigma-fields 9

indicator function 6,18

inequality

\- Jensen's 31

\- Schwarz 8,13

\- upcrossings 70

integrable random variable 6

invariant measure 110

inverse image 4

irreducible set of states 107

Itô 180

\- correction 196

\- differential notation 194

\- formula 196,201

\- multiplication table 201

\- process 194

\- stochastic integral 180, 184, 186

Jensen's inequality 31

joint density 6

joint distribution 6

Kolmogorov's zero-one law 78

lack of memory 141

Lebesgue measure 2

lemma

\- Borel-Cantelli 3

\- Doob-Dynkin 4

Lévy's martingale characterization 156

Markov chain 88

\- homogeneous 90

\- $n$ -step transition matrix 91

\- state space of 88

\- transition matrix 90

\- transition probability 90

Markov property 88

martingale 49,140

\- exponential 160

mass 5

measurable function 3

measure

\- Lebesgue 2

\- probability 2

modification of a process 192

normal distribution 152

null-recurrent state 104

optional stopping theorem 58

Ornstein-Uhlenbeck process 202

pairwise disjoint sets 2

path 139

periodic state 105

Poisson distribution 143

Poisson process 142

positive-recurrent state 104

previsible sequence of random variables 52

probability

\- conditional 8,18

\- measure 2

\- space 2

process

\- Itô 194

\- Ornstein-Uhlenbeck 202

\- Poisson 142

\- stochastic 139

\- Wiener 151

Radon-Nikodym theorem 28

random step process 181

random variable 3

\- distribution of 4

\- expectation of 6

\- integrable 6

\- sigma-field generated by 4

\- square integrable 7

\- variance of 7

random variables

\- independent 9

\- uncorrelated 9

random walk 50,93

recurrent state 101

sample path 45,139

Schwarz inequality 8,13

sequence of random variables

\- adapted 48

-previsible 52

-stopped 55

\- uniformly integrable 74

set, Borel 2

sigma-field 1

\- generated by a random variable 4

-independent 9

\- tail 78

square integrable random variable 7

state space 88

stationary increments 148

step function 6

stochastic differential 194

stochastic differential equation 180, 202

\- linear 206

stochastic integral 180

\- of a random step process 182

stochastic matrix 90

\- double 90

stochastic process 139

\- adapted 140

\- in continuous time 139

\- in discrete time 139

\- modification of 192

\- sample path of 139

\- version of 192

\- with independent increments 148

\- with stationary increments 148

stopped sequence of random variables 55

stopping time 54

submartingale 51,140

supermartingale 51,140

symmetric random walk 50

tail sigma-field 78

taking out what is known 29

theorem

\- Doob's 71

\- optional stopping 58

\- Radon-Nikodym 28

time

\- continuous 139

\- discrete 45,139

\- first entry 55

\- first hitting 54

-stopping 54

total probability formula 8

tower property 29

transient state 101

transition density 151

transition matrix 90

\- $n$ -step 91

transition probability 90

uncorrelated random variables 9

uniform integrability 74

upcrossings 69

upcrossings inequality 70

upcrossings strategy 69

variance 7

variation 157

version of a process 192

Wiener process 151

\- Lévy's martingale characterization 156

\- $n$ -dimensional 153

zero-one law 78

Document generated by Anna's Archive around 2023-2024 as part of the DuXiu collection (https://annas-blog.org/duxiu-exclusive.html).

Images have been losslessly embedded. Information about the original file can be found in PDF attachments. Some stats (more in the PDF attachments):

```json
{
    "before_pdg2pic_conversion": {
    "filename": "MTI1NjcyMTAuemlw",
    "filename_decoded": "12567210.zip",
    "filesize": 6228021,
    "md5": "d08494f0efd88c8e7a32e1dceb18099e",
    "header_md5": "61eae87c203f9dbc5100a79053a3bab6",
    "sha1": "f40a932c9375aa1b07666d26a29d031517fee407",
    "sha256": "4f56b20444ecf7ecb1695da1184a45b4efd7207c89f86cb813011feaf1bcd0c4",
    "crc32": 3824654725,
    "zip_password": "52gv",
    "uncompressed_size": 6472863,
    "pdg_dir_name": "_12567210",
    "pdg_main_pages_found": 225,
    "pdg_main_pages_max": 225,
    "total_pages": 239,
    "total_pixels": 22308096
},
"after_pdg2pic_conversion": {
    "filename": "MTI1NjcyMTAuemlw",
    "filename_decoded": "12567210.zip",
    "filesize": 11417265,
    "md5": "fcf742ce3bb882ffc2d72b9e8e75740f",
    "header_md5": "b3c0c50e42536b712e213a6022d3abd6",
    "sha1": "e23111a345cbbe61efa83545b373cfc992813439",
    "sha256": "abed769bde75f13deaf09882d1416b9dfac6e19fbc5e64bd715ea810eebea804",
    "crc32": 342888659,
    "zip_password": "",
    "uncompressed_size": 12100061,
    "pdg_dir_name": "",
    "pdg_main_pages_found": 225,
    "pdg_main_pages_max": 225,
    "total_pages": 239,
    "total_pixels": 1332908736
},
"pdf_generation_missing_pages": false
} 
```