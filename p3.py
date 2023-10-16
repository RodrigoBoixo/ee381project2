import numpy as np
import matplotlib.pyplot as plt


N = 100000
n = 1000
success = 0
def flip_coin(n):
    heads = sum(np.round(np.random.rand(n, 1)))
    tails = N - heads
    p_heads = heads / N
    #print(p_heads)
    p_tails = tails / N
    yes = 0

    if p_heads == 0.500000:
        yes = 1
    return yes

print('start')
for i in range(N):
    yes = flip_coin(n)
    success = success + yes


fails = N - success
print(success)
S = [success/N, fails/N]
print(S[0])
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
