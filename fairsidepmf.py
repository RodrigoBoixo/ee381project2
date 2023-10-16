import numpy as np
import matplotlib.pyplot as plt

N = 100000
d1 = np.ceil(6 * np.random.rand(N))
d2 = np.ceil(6 * np.random.rand(N))
s = d1 + d2
bins = np.arange(1, 14)
yvalues, xvalues = np.histogram(s, bins=bins, density=True)

# Bar graph
plt.figure(1)
plt.bar(xvalues[:-1], yvalues, width=1.0)
plt.title('Bar graph: PMF of the sum of the rolls of two fair dice')
plt.xlabel('Sum of two dice')
plt.ylabel('Probability')

# Stem plot
plt.figure(2)
plt.stem(xvalues[:-1], yvalues)
plt.title('Stem plot: PMF of the sum of the rolls of two fair dice')
plt.xlabel('Sum of two dice')
plt.ylabel('Probability')

plt.show()