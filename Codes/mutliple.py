from scipy.stats import binom
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

n = 12   
p = 0.1   
mu = 1.2
sigma = 1.04

x1 = range(n+1)
x2 = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
y1 = binom.pmf(x1, n, p)
y2 = norm.pdf(x2, mu, sigma)

plt.bar(x1, y1,color ='blue' ,label ='pmf')
plt.plot(x2, y2,color = 'red', label='pdf')

plt.legend()
plt.xlabel('Number of successes')
plt.ylabel('Probability')
plt.title('Binomial PMF and Gaussian PDF for (n=12, p=0.1)')

plt.show()
