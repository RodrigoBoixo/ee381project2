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

# Number of rolls
N = 1000

# Simulate the rolls of the die and store the results
results = [nsided_die(p) for _ in range(N)]

# Count the occurrences of each die face
die_face_counts = [results.count(i) for i in range(1, len(p) + 1)]

# Create a bar plot to visualize the counts
plt.bar(range(1, len(p) + 1), die_face_counts)
plt.xlabel('Die Face')
plt.ylabel('Count')
plt.title('Roll Count of Each Die Face')
plt.xticks(range(1, len(p) + 1))
plt.show()