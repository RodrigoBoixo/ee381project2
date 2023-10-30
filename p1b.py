import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import poisson

def nsided_die(p):

    r = np.random.rand()

    cumulative_prob = 0

    # Find the side of the die
    for i in range(len(p)):
        cumulative_prob += p[i]
        if r <= cumulative_prob:
            return i + 1


N = 10000 #number of experiments
n = 1000 #rolls/experiment

successes = []

# Probability vector for each side
die_probabilities = [0.20, 0.10, 0.30, 0.25, 0.15]

for _ in range(N):
    success_count = 0
    for _ in range(n):
        # Roll the three dice
        rolls = [nsided_die(die_probabilities) for _ in range(3)]
        # Check if all three dice show "2"
        if rolls.count(2) == 3:
            success_count += 1
    successes.append(success_count)



unique_values, counts = np.unique(successes, return_counts=True)
plt.stem(unique_values, counts / N, basefmt='b-')
plt.xlabel('Number of Successes (X)')
plt.ylabel('Probability')
plt.title('Experimental Probability Distribution of X (Stem Plot)')
plt.grid(True)

plt.show()




p_success = (0.10) ** 3  #probability of side 2 cubed


# Theoretical probability distribution using the Binomial formula
x = np.arange(0, n + 1)
pmf = binom.pmf(x, n, p_success)

experimental_data = successes  #experimental data from 1 for comparison


plt.figure(figsize=(10, 5))
plt.stem(x, pmf, linefmt='r-', markerfmt='ro', basefmt='r-', label='Theoretical Binomial PMF')
unique_values, counts = np.unique(experimental_data, return_counts=True)
plt.stem(unique_values, counts / N, linefmt='b-', markerfmt='bo', basefmt='b-', label='Experimental Data (Problem 1)')
plt.xlabel('Number of Successes (X)')
plt.ylabel('Probability')
plt.title('Bernoulli Trials: PMF - Binomial Formula')
plt.legend()
plt.grid(True)

plt.show()

# Calculate the Poisson parameter λ
lambda_poisson = n * p_success

# Possible values of X
x = np.arange(0, n + 1)

pmf_poisson = poisson.pmf(x, lambda_poisson)


experimental_data = successes

plt.figure(figsize=(10, 5))
plt.stem(x, pmf_poisson, linefmt='g-', markerfmt='go', basefmt='g-', label='Theoretical Poisson PMF')
unique_values, counts = np.unique(experimental_data, return_counts=True)
plt.stem(unique_values, counts / N, linefmt='b-', markerfmt='bo', basefmt='b-', label='Experimental Data (Problem 1)')

plt.xlabel('Number of Successes (X)')
plt.ylabel('Probability')
plt.title('Bernoulli Trials: PMF - Poisson Approximation')
plt.legend()
plt.grid(True)

plt.show()

