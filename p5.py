import random

# Function to simulate one experiment
def experiment(m, passcode):
    hacker_list = [random.randint(0, 9999) for _ in range(m)]
    return passcode in hacker_list

# Function to estimate the probability for a given value of m and N experiments
def estimate_probability(m, passcode, N):
    success_count = 0
    for _ in range(N):
        if experiment(m, passcode):
            success_count += 1
    return success_count / N

# Your 4-digit passcode
your_passcode = 1234
N = 1000

# Part 1: m = 10^4
m1 = 10**4
#probability1 = estimate_probability(m1, your_passcode, N)

# Part 2: m = 10^6
m2 = 10**6
#probability2 = estimate_probability(m2, your_passcode, N)

# Part 3: Find m for probability of 0.5
desired_probability = 0.5
m_trial = 10
while True:
    probability_trial = estimate_probability(m_trial, your_passcode, N)
    if probability_trial >= desired_probability:
        break
    m_trial *= 2

#print(f"Part 1: Probability with m = {m1} is {probability1:.6f}")
#print(f"Part 2: Probability with m = {m2} is {probability2:.6f}")
print(f"Part 3: The approximate value of m for probability {desired_probability} is {m_trial}")