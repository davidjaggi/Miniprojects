# http://bigdata-madesimple.com/how-to-implement-these-5-powerful-probability-distributions-in-python/

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
# Binomial Distribution
n = 10
p = 0.3
k = np.arange(0,21)
binomial = stats.binom.pmf(k, n, p)
binomial

plt.plot(k, binomial, 'o-')
plt.title('Binomial: n = %i , p = %.2f' % (n,p), fontsize=15)
plt.xlabel('Number of successes')
plt.ylabel('Probability of successes', fontsize = 15)
plt.show()

binom_sim = data = stats.binom.rvs(n = 10, p = 0.3, size = 10000)
print(f'Mean: {np.mean(binom_sim):.4f}')
print(f'SD: {np.std(binom_sim, ddof = 1):.4f}')
plt.hist(binom_sim, bins = 10, normed = True)
plt.xlabel('x')
plt.ylabel('density')
plt.show()

# Poisson distribution
rate = 2
n = np.arange(0,10)
y = stats.poisson.pmf(n, rate)
y

plt.plot(n ,y , 'o-')
plt.title(f'Poisson: $\lambda$ = {rate}')
plt.xlabel('Number of accidents')
plt.ylabel('Probability of number of accidents')
plt.show()

data = stats.poisson.rvs(mu = 2, loc = 0, size = 1000)
print(f'Mean: {np.mean(data):.4f}')
print(f'SD: {np.std(data, ddof=1):.4f}')

plt.figure()
plt.hist(data, bins = 9, normed = True)
plt.xlim(0, 10)
plt.xlabel('Number of accidents')
plt.title('Simulating Poisson Random Variables')
plt.show()

# Normal distribution
mu = 0
sigma = 1
x = np.arange(-5,5,0.1)

y = stats.norm.pdf(x, 0, 1)
plt.plot(x, y)
plt.title(f'Normal: $\mu$ ={mu:.1f}, $\sigma^2$={sigma:.1f}')
plt.xlabel('x')
plt.ylabel('Probability density')
plt.show()

# Beta distribution
a = 0.5
b = 0.5
x = np.arange(0.01, 1, 0.01)
y = stats.beta.pdf(x, a, b)
plt.plot(x, y)
plt.title(f'Beta: a = {a:.1f}, b = {b:.1f}')
plt.xlabel('x')
plt.ylabel('Probability density')
plt.show()

# Exponential distribution
lambd =  0.5
x = np.arange(0, 15, 0.1)
y = lambd*np.exp(-lambd*x)
plt.plot(x, y)
plt.title(f'Exponential: $\lambda$ = {lambd:.2f}')
plt.xlabel('x')
plt.ylabel('Probability density')
plt.show()

data = stats.expon.rvs(scale = 2, size = 1000)
print(f'Mean: {np.mean(data):.4f}')
print(f'SD: {np.std(data, ddof=1):.4f}')
plt.figure()
plt.hist(data, bins = 20, normed = True)
plt.xlim(0,15)
plt.ylabel('Probability density')   
plt.title('Simulatind Exponential Random Variables')
plt.show()
