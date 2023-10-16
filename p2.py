import numpy as np
import matplotlib.pyplot as plt
N = 100000
success = 0
d1 = np.ceil(6 * np.random.rand(N))
d2 = np.ceil(6 * np.random.rand(N))
s = d1 + d2
for i in s:
    if i == 3 or i == 8:
        success += 1
fails = 100000 - success

S = [success/100000, fails/100000]
# Create a list of the possible outcomes
outcomes = ["success", "fail"]

# Calculate the probability of each outcome
probabilities = [S[0], S[1]]

# Plot the probabilities of each outcome as a bar graph
plt.figure(1)
plt.bar(outcomes, probabilities, width=1.0)
plt.title('PMF of the outcome of rolling two fair dice')
plt.xlabel('Outcome')
plt.ylabel('Probability')

# Plot the probabilities of each outcome as a stem plot
plt.figure(2)
plt.stem(outcomes, probabilities)
plt.title('PMF of the outcome of rolling two fair dice')
plt.xlabel('Outcome')
plt.ylabel('Probability')

plt.show()


plt.show()