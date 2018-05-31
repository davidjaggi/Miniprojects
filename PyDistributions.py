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