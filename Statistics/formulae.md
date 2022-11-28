# Statistics 1 Formulae

## Measures of Central Tendency

### Mean

#### Continuous data

$$\bar{x} = \frac{\sum_{i=1}^nx_i}{n}$$

- $n$ total number of observations
- $x_i$ each $i^{th}$ observation

#### Continuous grouped data

$$\bar{x} = \frac{\sum_{i=1}^n f_im_i}{\sum f_i}$$

- $m_i$ each group's middle value
- $f_i$ frequency of each group

#### Discrete data

$$\bar{x} = \frac{\sum_{i=1}^m f_ix_i}{\sum f_i}$$

- $x_i$ each discrete value
- $f_i$ frequency of each discrete value

#### Adding a constant

$$\bar{y} = \bar{x} + c$$

- $\bar{x}$ is old mean
- $\bar{y}$ is new mean
- $c$ is constant value added in each $x_i$ or overall mean $\bar{x}$

#### Multiplying a constant

$$\bar{y} = \bar{x}\cdot c$$

- $\bar{x}$ is old mean
- $\bar{y}$ is new mean
- $c$ is constant value multiplied with each $x_i$ or overall mean $\bar{x}$

---

### Median

```ad-important
Data must be sorted
```

#### Odd frequency $n$

$$x_i = \frac{n + 1}{2}$$

- $n$ is frequency
- $x_i$ is median value

#### Even frequency $n$

$$x_i = \frac{\frac{n}{2} + \frac{n+1}{2}}{2}$$

- $n$ is frequency
- $x_i$ is median value

#### Adding a constant

$$y_i = x_i + c$$

- $\bar{x}$ is old median
- $\bar{y}$ is new median
- $c$ is constant value added in each $x_i$ or overall median

#### Multiplying a constant

$$y_i = x_i \cdot c$$

- $\bar{x}$ is old median
- $\bar{y}$ is new mean
- $c$ is constant value multiplied in each $x_i$ or overall median $\bar{x}$

---

### Mode

- Most occured value
- If data has 2 modes, then it's _bimodal_.
- If data has more than 2 modes, then it's _multimodal_.

#### Adding a constant

$$y_i = mode + c$$

- $c$ is constant added to all terms
- $y_i$ is new mode

#### Multiplying a constant

$$y_i = mode \cdot c$$

- $c$ is constant value multiplied by all terms
- $y_i$ is new mode

---

## Measures of Dispersion

- It tells how much our data varies and spread.

### Range

- Difference b/w maximum and minimum value
  $$Range = max - min$$

---

### Variance

- It means how far data is spread in a data set.
- The units will be squared, hence we can't measure the quantity.
- It is calculated by sum of squared deviation
- Deviation = $x_i - \mu$

#### Population variance

$$\sigma^2 = \frac{\sum_{i=1}^n\left(x_i - \mu\right)^2}{n}$$

- $n$ is total no. of observations
- $\mu$ is mean of all observations

#### Sample variance

$$\sigma^2 = \frac{\sum_{i=1}^n\left(x_i - \mu\right)^2}{n - 1}$$

- $n$ is total no. of observations
- $\mu$ is mean of all observations

#### Adding a constant

- Adding a constant does **not** effect the variance.
- As constant will be added to all terms as well as mean, so it cancelled out.

#### Multiplying a constant

$$\sigma^2 = var \cdot c^2$$
$var$ is old variance

- $c$ is the constant value being multiplied by each term.
- As we are squaring the deviations, hence we need to square the constant also.

---

### Standard Deviation

- It also measures how much the data is dispersed.
- But, we can use it as it's calculated with same quantity.
- It is calculated by adding up all squared deviations and square root it.

```ad-note
- Standard deviation is the square root of variance.
$$\sigma = \sqrt{\sigma^2}$$
```

#### Population Standard Deviation

$$\sigma = \sqrt{\frac{\sum_{i=1}^n\left(x_i - \mu\right)^2}{n}}$$

- $x_i$ each observation
- $n$ is total no. of observations
- $\mu$ is mean of all observations

#### Sample Standard Deviation

$$\sigma = \sqrt{\frac{\sum_{i=1}^n\left(x_i - \mu\right)^2}{n-1}}$$

- $x_i$ each observation
- $n$ is total no. of observations
- $\mu$ is mean of all observations

#### Adding a constant

- Same as variance, adding a constant does **not** change the standard deviation.
- As constant will be added to all terms and mean, hence it cancelled out.

#### Multiplying a constant

$$\sigma = \sqrt{std \cdot c^2}$$

- $std$ is old standard deviation
- $c$ is constant value being multiplied by each term.
- As we are squaring the deviations, and then taking total's root, same we are doing here.

---

### Percentiles

- Percentiles tells us how much data is distributed on a $k^{th}$ percentile.
- Data should be sorted in ascending order.

#### Even frequency

$$percentile = \frac{p}{100} \cdot \frac{n}{2} + \frac{(n+1)}{2}$$

- $n$ is the total number of observations
- $p$ is $k^{th}$ percentile.

#### Odd frequency

$$percentile = \frac{p}{100} \cdot \frac{n}{2}$$

- $\frac{n}{2}$ should be rounded to next integer.

---

### Qaurtile

1. Q1 - Lower (first) = $25\%$ tile
2. Q2 - Middle (Median) = $50\%$ tile
3. Q3 - Upper (Third) = $75\%$ tile

#### Quartile range

1. Min - Q1
2. Q1 - Q2
3. Q2 - Q3
4. Q3 - Max

![[statistics-101-04-quartiles-3.png]]

---

### InterQuartile Range (_IQR_)

$$IQR = Q3 - Q1$$

#### Detecting outliers

$$Lower = Q1 - 1.5\cdot IQR$$
$$Upper = Q3 + 1.5\cdot IQR$$

---

## Association b/w two categorical variables

### Contingency table

![[contingency_table_marginal_probabilities.webp]]

---

## Association b/w two numerical variables

### Covariance

- It quantifies the strength of the _linear association_ b/w two numerical variables.
- It shows how two variables are different.

```ad-important
- Covariance is always measures b/w $-\infty$ and $\infty$
$$-\infty \leq Cov(x, y) \leq \infty$$
```

#### Population covariance

$$Cov(x, y) = \frac{\sum_{i=1}^{N}\left(x_i - \bar{x}\right)\left(y_i - \bar{y}\right)}{N}$$

- $N$ is the total number of observations
- $x$ is first variable / column
- $y$ is second variable / column

#### Sample covariance

$$Cov(x, y) = \frac{\sum_{i=1}^{n-1}\left(x_i - \bar{x}\right)\left(y_i - \bar{y}\right)}{n-1}$$

- $n$ is the total number of observations
- $x$ is first variable / column
- $y$ is second variable / column

---

### Correlation

- It is used to interpret the _linear association_ b/w two numerical variables.
- It shows how two variables are related.
- It derives from covariance.

- Correlation is always measures b/w $-1$ and $1$
  $$-1 \leq r \leq 1$$

#### Pearson correlation

- We are using pearson correlation to find a linear relationship b/w two variables.

#### Sample correlation

$$r = \frac{cov(x, y)}{S_xS_y}$$
$$r = \frac{\sum_{i=1}^n\left(x_i - \bar{x}\right)\left(y_i - \bar{y}\right)}{\sqrt{\sum_{i=1}^n\left(x_i - \bar{x}\right)^2}\cdot \sqrt{\sum_{i=1}^n\left(y_i - \bar{y}\right)^2}}$$

- $cov(x, y)$ is covariance of $x$ and $y$
- $\bar{x}$ is $x$ variable mean.
- $\bar{y}$ is $y$ variable mean.
- $n$ is total number of observations.
- $S_x$ is standard deviation of $x$ variable/column.
- $S_y$ is standard deviation of $y$ variable/column.

#### Population correlation

$$\rho = \frac{cov(x, y)}{S_xS_y}$$
$$\rho = \frac{\sum_{i=1}^N\left(x_i - \bar{x}\right)\left(y_i - \bar{y}\right)}{\sqrt{\sum_{i=1}^N\left(x_i - \bar{x}\right)^2}\cdot \sqrt{\sum_{i=1}^N\left(y_i - \bar{y}\right)^2}}$$

- $cov(x, y)$ is covariance of $x$ and $y$
- $\bar{x}$ is $x$ variable mean.
- $\bar{y}$ is $y$ variable mean.
- $N$ is total number of observations.
- $S_x$ is standard deviation of $x$ variable/column.
- $S_y$ is standard deviation of $y$ variable/column.

## Point Bi-serial Correlation

$$\rho=\frac{\bar{Y_0}-\bar{Y_1}}{S_s}\sqrt{P_0P_1}$$

- We need to assign a value of $1$ or $0$ to each observation, depending on whether the observation is in the first group or the second group.
- $Y_0$ is the mean of the observations in the first group.
- $Y_1$ is the mean of the observations in the second group.
- $S_s$ is the sample standard deviation of the entire sample.
- $P_0$ is the proportion of observations in the first group.
- $P_1$ is the proportion of observations in the second group.

## Scatter plot

- In scatter plot we usually measure 4 things:

1. Direction (upwards, downwards)
2. Curve (linear, quadratic, cubic)
3. Clustered or spreaded
4. Outliers

---

## Fitting a line

- A linear regression has a equation:
  $$y = mx + c$$
- $m$ is slope
- $c$ is y-intercept

### $R^2$

- It measures the goodness of fit of regression line.
- It's the error metric.
- Ranges from $0 \leq  R^2 \leq 1$

---

# Permuation and Combination

## Permutation Formula

- The number of permutations of $n$ objects when $p$ if them are of one kind and rest distinct is given by:

$$^nP_r = \frac{n!}{(n-r)!}$$

- The number of permutations of $n$ objects where $p_1$ is of one kind, $p_2$ is of another kind and $p_k$ is of $k^{th}$ kind is given by:

$$\frac{n!}{p_1!*p_2!*...p_k!}$$

## Circular Permutation: Clockwise and Anti-clockwise

- We fix one element and then we have $n-1$ elements to arrange in $n-1$ ways.

$$(n-1)!$$

- If number of elements arranged in clockwise direction and anti-clockwise direction are same then:

$$\frac{(n-1)!}{2}$$

## Combination Formula

- In general, each combination of $r$ objects from $n$ objects can give rise to $r!$ arrangements.
- The number of possible combinations of $r$ objects from collection of $n$ objects is denoted by:

$$^nC_r = \frac{n!}{r!(n-r)!}$$

- Also

$$\frac{n!}{r!(n-r)!}=\frac{n!}{(n-r)!r!} = \ ^nC_{(n-r)}$$

- In other words, selecting $r$ objects from $n$ objects is the same as rejecting $n-r$ objects from $n$ objects.

- $^nC_n = 1$ and $^nC_0 = 1$ for all values of $n$.
- $^nC_r= \ ^{n+1}C_{r-1}+ \ ^{n+1}C_{r}$ $;$ $1 \leq r \leq n$

---

# Probability

## Conditional Probability

- The probability of an event $A$ given that another event $B$ has already occurred is called conditional probability.
- It is denoted by $P(A|B)$.
  $$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

### Multiplication Rule

- The probability of two events $A$ and $B$ occurring together is given by:
  $$P(A \cap B) = P(A) \cdot P(B|A)$$

- The probability of three evennts $A,B$ and $C$ occuring together is given by:
  $$P(A \cap B \cap C) = P(A) \cdot P(B|A) \cdot P(C|A \cap B)$$
  $$P(C | A \cap B) = \frac{P(A \cap B \cap C)}{P(A \cap B)}$$

## Independent Events

- In case of independent events, the probability of two events occurring together is given by:
  $$P(A | B) = P(A)$$
- In other words, the probability of $A$ occurring given that $B$ has occurred is equal to the probability of $A$ occurring irrespective of whether $B$ has occurred or not.
  $$ P(A \cap B) = P(A) \cdot P(B)$$
- Therefore the probability of $A$ and $B$ are independent of each other.

### Independence of more than two events

- If $A,B,C$ are independent events, then:
  $$P(A \cap B \cap C) = P(A) \cdot P(B) \cdot P(C)$$

## Law of Total Probability

- Let $E$ and $F$ be two events such that $E \cap F = \emptyset$.
  $$P(E)= P(E \cap F) + P(E \cap F^c)$$
  $$or$$
  $$P(E)= P(E|F) \cdot P(F) + P(E|F^c) \cdot P(F^c)$$

## Bayes' Theorem

$$ P(B|A) = \frac{P(B \cap A)}{P(B)}$$
$$\text{or}$$
$$ P(B|A) =\frac{P(A|B) \cdot P(B)}{P(B)\cdot P(A|B) + P(B^c) \cdot P(A|B)}$$

- Suppose that events $F$

---

# Random Experiment

- A random experiment is an experiment whose outcome is not known in advance. It is an experiment whose outcome is determined by chance.
- The outcome of a random experiment is called a random variable.
- Sample Space: The set of all possible outcomes of a random experiment is called the sample space of the experiment.
  - Sample space is denoted by $S$.
  - Suppose a random experiment of throwing a die is performed. The sample space of the experiment is given by:
    $$S = \{1,2,3,4,5,6\}$$
  - The sample space of a random experiment of tossing two coins is given by:
    $$S = \{(H,H),(H,T),(T,H),(T,T)\}$$

### Discrete Random Variable

- A random variable that can take on at most a countable number of possible values is said to be a **Discrete Random Variable.**
  - Thus, any random variable that can tkae on only a finite number or countably infinite number of values is a discrete.

### Continuous Random Variable

- There also exists a random variable that can take on an uncountably infinite number of values. Such a random variable is called a **Continuous Random Variable.**

## Probability Mass Function

- The probablity mass function $p(x)$ is positive for at most a coutntable number values of $x$. That is, if $X$must assume one of the values $x_1,x_2,...,x_n$ then:
  - $p(x_i) \geq 0$ for all $i$ and $p(x_i) = 0$ for all $x \neq x_i$.
  - Since $p(x)$ is a probability, it must satisfy the following:
    $$\sum_{i=1}^\infin p(x_i) = 1$$
    $$\text{Any } x_i \text{ should not be } \geq \text{ to } 0.$$
- The graph from the probablity mass function can take many shapes. The graph can be skewed positively or negatively. It can be symmetric or asymmetric. It can be unimodal or multimodal. It can be discrete or continuous. It can also be uniform or non-uniform.

## Cumulative Distribution Function

- The cumulative distribution function $F(x)$ is defined as:
  $$F(x) = P(X \leq x)$$
- The cumulative distribution function $F(x)$ is a non-decreasing function of $x$.

## Expected Value of a Random Variable

- Let $X$ be a Discreet Random variable taking values $x_1,x_2,...,x_n$ with probabilities $p_1,p_2,...,p_n$ respectively.
- The Expectation of $X$ is denoted by $E(X)$ and is defined as:
  $$E(X) = \sum_{i=1}^n x_i \cdot p_i$$
- Suppose we want to find out the expectation of a random variable $X$ that takes on values $x_1,x_2,...,x_n$ with probabilities $p_1,p_2,...,p_n$ respectively.
  - We can find the expectation by multiplying each value of $X$ by its probability and then adding the results.
  - The expectation of a random variable is the weighted average of the possible values of the random variable.
    $$E(g(X))=\sum g(x_i)P(X=x_i)$$
- If the function $g(x)$ is multiplied by a constant $c$, then the expectation of the function is also multiplied by the same constant.
  $$E(cg(X))=cE(g(X))$$
- If we add a constant $c$ to the random variable $X$, then the expectation of the random variable is also increased by the same constant.
  $$E(X+c)=E(X)+c$$
- The expected value of the sum of random variables is equal to the sum of the individual expected values.
  $$E(X+Y)=E(X)+E(Y)$$

### Example

| $X$    | $-1$  | $0$   | $1$   |
| ------ | ----- | ----- | ----- |
| $P(X)$ | $0.2$ | $0.5$ | $0.3$ |

- Let $Y = g(X) = X^2.$ What is $E(Y)$
- $E(Y) = \sum_{i=1}^n y_i \cdot p_i$
- $E(Y) = [1 \cdot 0.2] + [0 \cdot 0.5] + [1 \cdot 0.3]$
- $E(Y) = 0.2 + 0.3 = 0.5$

| $X$    | $-2$   | $2$      | $5$       |
| ------ | ------ | -------- | --------- |
| $P(X)$ | $0.25$ | $0.3334$ | $0.41667$ |

- Calculate the expected value of $(2X+1)^2$.
- $E(Y) = \sum_{i=1}^n y_i \cdot p_i$
- $E(Y) = [(2 \cdot -2 + 1) \cdot 0.25] + [(2 \cdot 2 + 1) \cdot 0.3334] + [(2 \cdot 5 + 1) \cdot 0.41667]$
- $E(Y) = 0.75 + 1.6667 + 4.5833

## Variance of a Random Variable

- Let's denote expected value of a random variable $X$ by the greek letter $\mu$.
- Let $X$ be a random variable with the expected value $\mu$. Then the variance of $X$ denoted by $Var(X)$ is defined as:
  $$Var(X) = E(X-\mu)^2$$
  $$\text{or}$$
  $$Var(X) = E(X^2) - \mu^2$$
  $$E(X) = \sqrt{Var(X)+\mu^2}$$
- In other words, the variance of random variable $X$ measures the square of the difference of the random variable from its mean, $\mu$, on the average.

### Example

- Random Experiment: Roll a die once.
  - Sample Space: $S = \{1,2,3,4,5,6\}$
  - Random Variable: $X = \text{number of spots on the die}$
    |$X$ | 1 | 2 | 3 | 4 | 5 | 6 |
    | --- | --- | --- | --- | --- | --- | --- |
    |$X^2$ | 1 | 4 | 9 | 16 | 25 | 36 |
    |$P(X)$ | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 |
    |$E(X)$ | 1/6 | 2/6 | 3/6 | 4/6 | 5/6 | 6/6 |
    |$E(X^2)$ | 1/6 | 4/6 | 9/6 | 16/6 | 25/6 | 36/6 |
  - $E(X) = \frac{1}{6} + \frac{2}{6} + \frac{3}{6} + \frac{4}{6} + \frac{5}{6} + \frac{6}{6} = \frac{21}{6} = 3.5$
  - $E(X^2) = \frac{1}{6} + \frac{4}{6} + \frac{9}{6} + \frac{16}{6} + \frac{25}{6} + \frac{36}{6} = \frac{91}{6} = 15.17$
  - $Var(X) = E(X^2) - \mu^2 = 15.17 - 3.5^2 = 15.17 - 12.25 = 2.92$

## Bernoulli Random Variable

- A random variable that takes on either the value 1 or 0 is called a **Bernoulli Random Variable**.
- Let $X$ be a Bernoulli random variable with $p$ being the probability of success. Then the probability mass function of $X$ is:
  $$p(x) = \begin{cases} p & \text{if } x = 1 \\ 1-p & \text{if } x = 0 \end{cases}$$
  $$Var(X) = p(1-p)$$

## Discrete Uniform random variable

- Let $X$ be a random variable that is equally likely to occur on any of the $n$ possible values $x_1,x_2,...,x_n$. Then $X$ is said to be a **Discrete Uniform Random Variable**.
  $$Var(X) = \frac{(n^2-1)}{12}$$

### Variance of a Random Variable when mulplied by a constant

$$Var(cX) = c^2Var(X)$$

### Variance of a Random Variable when added to a constant

$$Var(X+c) = Var(X)$$

### Collorary

$$Var(aX+b) = a^2Var(X)$$

### Variance of the sum of two random variables

- This is applicable only when the two random variables are independent.
  $$E(X+Y) = E(X)+E(Y)$$

### Variance of sum of many independent random variables

$$V(X_1+X_2 \ ... \ X_k) = V(X_1)+V(X_2)+...+V(X_k)$$
$$\text{or}$$
$$V(\sum_{i=1}^k X_i) = \sum_{i=1}^k V(X_i)$$

## Standard Deviation of a Random Variable

$$SD(X) = \sqrt{Var(X)}$$

- Hence, the standard deviation is a positive square root of variance.
- Standard deviation is in the same units as the random variable.

## Standard Deviation adding or being multiplied by a constant

### Multplied by a constant

$$SD(cX) = \sqrt{c^2Var(X)} = c\sqrt{Var(X)}$$
$$\text{or}$$
$$SD(cX) = cSD(X)$$

### Added to a constant

- The standard deviation of a random variable is not affected by adding a constant to the random variable.
  $$SD(X+c) = SD(X)$$

### Collorary

$$SD(aX+b) = aSD(X)$$
$$SD(aX+b) = \sqrt{a^2Var(X)} = a\sqrt{Var(X)}$$

## Bernoulli Distribution

- $X$ is a binomial random variable with praameters $n$ and $p$ that represents the number of successes in $n$ independent Bernoulli Trails, when each trial is a succees witha probablity $p$. $X$ takes the values $0,1,2,...,n$ with the probablity.
  $$P(X=i) =\ ^nC_i \cdot p^i \cdot (1-p)^{n-i}$$
- We can predict the skewness of the distribution graph of $X$ by the value of $p$.

  - If $p < 0.5$ , then the distribution is skewed to the right.
  - If $p = 0.5$ , then the distribution is symmetric.
  - If $p > 0.5$ , then the distribution is skewed to the left.

- The Probablity Distribution of Bernoulli Random Variable is
  | $X$ | $0$ | $1$ |
  | --- | --- | --- |
  | $P(X)$ | $1-p$ | $p$ |

  $$E(X) = 0 \cdot (1-p) + 1 \cdot p = p$$

### Example : Tossing a coin

- $S=\{ HHH, HHT, HTH, HTT, THH, THT, TTH, TTT \}$
- Sucess: $H$ and Failure: $T$
- $X$ is a random variable which counts the number of heads in toe tosses of a coin. $n = 3 ,p = 0.5$
  | $X$ | $0$ | $1$ | $2$ | $3$ |
  | --- | --- | --- | --- | --- |
  | $P(X)$ | $0.125$ | $0.375$ | $0.375$ | $0.125$ |

$P(X=3) = \ ^3C_3 \cdot 0.5^3 \cdot (0.5)^{3-3} = 0.125$

### Variance of a Bernoulli Random Variable

$$V(X) = p(1-p) = p - p^2$$

- The largest variance occurs when $p = 0.5$. In happens when the success and failure are equally likely. In other words the most uncertain outcome is when the probability of success and failure are equal.

### Independent and Identically Distributed Random Variables

- Two random variables are said to be **Independent and Identically Distributed** if they are independent and have the same probability distribution.
- A collection of random variables is said to be **Independent and Identically Distributed** if each random variable in the collection is independent and has the same probability distribution.

### Expectation of Binomial Random Variable

$$E(X) = np$$

### Variance of Binomial Random Variable

$$V(X) = np(1-p)$$

### Standard Deviation of Binomial Random Variable

$$SD(X) = \sqrt{np(1-p)}$$

## Hypergeometric Distribution

- Let $X$ be the number of items of type $1$, then the probablity mass function of the discrete random variable, $X$, is called the hypergeometric distribution and is of the form:
  $$P(X=i) = \frac{\ ^mC_i \cdot \ ^{N-m}C_{n-i}}{\ ^NC_n}$$

### Example: Choosing balls without replacement

- A bag consists of $7$ balls of which $4$ are white and $3$ are black. A student randomly samples two balls without replacement. Let X be the number of black balls selected.
  - Here, $N = 7, m = 3, n = 2$
  - $X$ has the values $0,1,2$
  - the probability mass function of $X$ is:
    $$P(X=0) = \frac{\ ^3C_0 \cdot \ ^{7-3}C_{2-0}}{\ ^7C_2} = \frac{12}{42}$$
    $$P(X=1) = \frac{\ ^3C_1 \cdot \ ^{7-3}C_{2-1}}{\ ^7C_2} = \frac{24}{42}$$
    $$P(X=2) = \frac{\ ^3C_2 \cdot \ ^{7-3}C_{2-2}}{\ ^7C_2} = \frac{6}{42}$$

### Expectation of Hypergeometric Random Variable

$$E(X) = \frac{n \cdot m}{N}$$

### Variance of Hypergeometric Random Variable

$$V(X) = n \cdot \frac{m}{N} \cdot \frac{N-m}{N}$$

- The variance of the hypergeometric distribution is symmetric when both $m$ and $n$ are equal to $\frac{N}{2} \text{ or } \frac{m}{N}=\frac{1}{2}$.

## Poisson Distribution

- The Poisson probablity distribution gives the probablity of a number of ecents occurring in a fixed interval of time or space.
- We assume that these events happen with a known average rate, $\lambda$, and independently of the time since the last event.
- Let $X$ be the number of events in a given interval. Then the probability mass function of the discrete random variable, $X$, is called the Poisson distribution and is of the form:
  $$P(X=i) = \frac{e^{-\lambda} \cdot\lambda^x}{x!}$$

#### Things to note about the graphs of Poisson Distribution

- If the value of $\lambda$ is very small, the the graph is skewed to the right.
- As the value of $\lambda$ increases, the graph becomes more symmetric.

### Poisson as Binomial Approximation

- Define "success" as exactly one event happening in a short interval of length $\delta t$.
- The $n$ events happening in interval of length $t$ can be viewed as $n$ successes happening in $n$ intervals of length $\delta t$, with each one of them being an Independent and Identical trails.
- Hence the problem can be viewed as
  $$Bin(n,p=\frac{\lambda}{n})=\ ^nC_1 \cdot (\frac{\lambda}{n})^x \cdot (\frac{n-\lambda}{n})^{n-x}$$

### Expectation of Poisson Random Variable
- The expectation of a Poisson random variable is equal to the value of $\lambda$ itself.
$$E(X) = \lambda$$

### Variance of Poisson Random Variable
- The variance of a Poisson random variable is equal to the value of $\lambda$.
- $$V(X) = \lambda$$
###### Contributions by [https://github.com/Param302](https://github.com/Param302)
