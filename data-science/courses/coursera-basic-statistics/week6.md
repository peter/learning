# Basic Statistics Week 6 - Confidence Intervals

We can distinguish two types of statistical inference methods. We can estimate population parameters and we can test hypotheses about these parameters. In the present module we'll talk about the first type of inferential statistics.

In the first video of this section we argue that we can estimate the value of a population parameter in two ways: by means of a so-called point estimate (a single number that is our best guess for the population parameter) or by means of an interval estimate (a range of values within which we expect the parameter to fall). An interval estimate is a range of numbers, which, most likely, contains the actual population value. The probability that the interval contains the population value is what we call the confidence level.

In the next two videos we'll explain how you can construct a confidence interval yourself, and we'll discuss how such a confidence interval should be interpreted. In the first of these two videos we'll show you how to compute a confidence interval if the population standard deviation is known. In this case we need the z-distribution. However, because this is a rather unlikely scenario, the next video looks at the more realistic situation that the standard deviation in the population is unknown. In this case we need the t-distribution.

## 6.1 Statistical inference

Random sample of 60 parents asking how many hours less they sleep as parents.
Sample mean is 2.6 (x bar) is a point estimate for the population mean.
The precision is given by an interval estimate, i.e. 2.3-2.9, with a confidence
level which is usually 95%.

## 6.2 CI for mean with known population sd

Sample mean is 2.6 and sd 0.9. Population sigma is 1.1 (usually not known).
The sampling distribution standard deviation is sigma divided by the square
root of n (the sample size). We also know that 95% of values of a normal
distribution lie between 1.96 standard deviations. This means that there is
a 95% chance that the sample mean falls within 1.96 sd of the population mean.
The distance of 1.96 sd is called the margin of error.

## 6.3 CI for mean with unknown population sd

You usually don't know the population sd. We therefore need to estimate it using
the t distribution. The estimated sd is the sample sd divided by the square root of n
(the standard error). Instead of using the z-score for the normal distribution
we use the t distribution with the degrees of freedom given by the sample size n.
The t distribution has thicker tails than the normal distribution, i.e. has greater
sd. With an infinite n the t distribution is identical to the normal distribution.


We'll show that a higher confidence level leads to a wider confidence interval. This means that the more confident we are that we draw a correct inference, the larger our margin of error is. This implies that we have to compromise between confidence and precision; as one gets better the other gets worse.The video concludes with a step-by-step plan for constructing a confidence interval.

## 6.4 CI for proportion

We have 0.17 babies who poo while diper is being changed. The sampling distribution
sd for proportions is sqrt(p(1-p)/n). The maximum value of p(1-p) is 0.25 at p = 0.5.

We don't make use of the t distribution for proportions. Criteria for using the normal
distribution for proportions: np >= 15 and n(1-p) >= 15

## 6.6 Choosing the sample size

Smaller margin of error requires larger sample and the same goes for the confidence level. A high sd of the population also requires a larger sample size. The formula
is n = s^2z^2/m^2 where z is the z-score for the confidence level and m is
the margin of error and s is the population sd.

Estimate population sd by saying 95% of parents fall between 0 and 5 hours and this
means z-score 1.96 is 2.5, i.e. sd is roughly 1.25.

The formula for proportions is n = p(1-p)z^2/m^2
