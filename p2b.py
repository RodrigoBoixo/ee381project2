import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Probability of getting a 2 in a single roll
p_success = (0.10) ** 3  # Cube because we need three twos

# Number of rolls in each experiment (n)
n = 1000

# Theoretical probability distribution using the Binomial formula
x = np.arange(0, n + 1)  # Possible values of X
pmf = binom.pmf(x, n, p_success)  # Probability mass function

# Experimental data (from Problem 1)
experimental_data = successes  # Make sure 'successes' is the list from Problem 1

# Create plots
plt.figure(figsize=(10, 5))

# Theoretical Binomial PMF
plt.stem(x, pmf, linefmt='r-', markerfmt='ro', basefmt='r-', label='Theoretical Binomial PMF')

# Experimental data (from Problem 1)
unique_values, counts = np.unique(experimental_data, return_counts=True)
plt.stem(unique_values, counts / N, linefmt='b-', markerfmt='bo', basefmt='b-', label='Experimental Data (Problem 1)')

plt.xlabel('Number of Successes (X)')
plt.ylabel('Probability')
plt.title('Comparison of Theoretical Binomial PMF and Experimental Data')
plt.legend()
plt.grid(True)

plt.show()

