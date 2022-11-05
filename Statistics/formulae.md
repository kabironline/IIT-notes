# Week 1 - 4 formulae

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

```ad-important
- Correlation is always measures b/w $-1$ and $1$
$$-1 \leq r \leq 1$$
```

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

### Contributions by [https://github.com/Param302](https://github.com/Param302)
