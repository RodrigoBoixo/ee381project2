import math

def binomial_pmf(n, k, p):
    binomial_coefficient = math.comb(n, k)
    probability = binomial_coefficient * (p**k) * ((1-p)**(n-k))
    return probability

n_experiments = 100000
n_tosses = 1000
p_success = 0.5
k_success = 500  # The number of "heads" for success

probability_of_success = binomial_pmf(n_tosses, k_success, p_success)

total_successes = n_experiments * probability_of_success

print(f"Theoretical Probability of success: {probability_of_success:.5f}")
print(f"Total Successes in {n_experiments} experiments: {total_successes:.0f}")