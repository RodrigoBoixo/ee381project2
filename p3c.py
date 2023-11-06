import numpy as np
import matplotlib.pyplot as plt

N = 10000


U = np.random.rand(N)  #random variables
T = -np.log(U) / 2  # Transform to exponentially distributed RVs

#hist bins, counts
nbins = 15
hist, xout = np.histogram(T, bins=nbins)
pdf = hist / N / (xout[1] - xout[0])  # Normalize the histogram

#PDF
def theoretical_pdf(t):
    y = np.zeros_like(t)  #new empty array like T
    for i in range(len(t)):
        if t[i] < 0:
            y[i] = 0
        else:
            y[i] = 2 * np.exp(-2 * t[i])
    return y

t = np.linspace(min(T), max(T), 100)  #PDF line
y = theoretical_pdf(t)

# Plot
plt.figure(figsize=(10, 6))
plt.stairs(xout[:-1], pdf, fill=True, label='Simulated PDF')
plt.plot(t, y, color='red', label='Theoretical PDF')
plt.xlabel('T (seconds)')
plt.ylabel('Probability Density')
plt.title('Exponentially Distributed RV Histogram')
plt.legend()
plt.grid(True)
plt.show()
