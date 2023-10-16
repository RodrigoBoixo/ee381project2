import numpy as np
import matplotlib.pyplot as plt


def nsided_die(p):
  # Check if the sum of probabilities is equal to 1.0
  sum = 0.20 + 0.05 + 0.10 + 0.25 + 0.30 + 0.10
  if np.sum(p) != sum:
    raise ValueError('The sum of probabilities must be equal to 1.0.')

  # Generate a random number between 0 and 1
  r = np.random.rand()

  # Initialize the cumulative probability
  cumulative_prob = 0

  # Find the side of the die
  for i in range(len(p)):
    cumulative_prob += p[i]
    if r <= cumulative_prob:
      return i + 1


# Define the probabilities for a 6-sided die
p = [0.20, 0.05, 0.10, 0.25, 0.30, 0.10]

N = 10

results = [nsided_die(p) for _ in range(N)]

# Create a stem plot to visualize the outcomes
plt.stem(range(1, N + 1), results, basefmt=' ')
plt.xlabel('Roll Number')
plt.ylabel('Die Face')
plt.title('Simulation of a 6-sided Die')
plt.show()