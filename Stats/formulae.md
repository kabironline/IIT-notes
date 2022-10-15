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

---

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

This article was created by [https://github.com/Param302](https://github.com/Param302)
