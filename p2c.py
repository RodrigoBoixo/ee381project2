import numpy as np
import matplotlib.pyplot as plt

N = 10000

U = np.random.rand(N)

# Use the formula
T = -(1/2) * np.log(1 - U)

# Plot
plt.figure(figsize=(8, 6))

# PlotT
plt.hist(T, bins=50, density=True, alpha=0.7, label='Generated Exponential RV T')


t = np.linspace(0, 5, 100)
pdf = 2 * np.exp(-2 * t)
plt.plot(t, pdf, 'r', label='Theoretical PDF: 2 * exp(-2t)')

plt.xlabel('t')
plt.ylabel('Probability Density')
plt.title('Exponentially Distributed RV T')
plt.legend()
plt.grid(True)
plt.show()
