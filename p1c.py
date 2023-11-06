import numpy as np
import matplotlib.pyplot as plt

N = 10000
a = 1
b = 3
mu_w = (a + b) / 2
sig_w = np.sqrt((b - a) ** 2 / 12)
X = np.zeros(N)

# CREATE EXPERIMENTS
n = 15
mu = n * mu_w
sig = np.sqrt(n) * sig_w

for k in range(N):
    x = np.random.uniform(a, b, n)
    w = np.sum(x)
    X[k] = w

mean_thickness = np.mean(X)
std_dev = np.std(X)

# PLOTTING
nbins = 15
del_ = (max(X) - min(X)) / (nbins - 1)
bins = np.arange(min(X), max(X) + del_, del_)

hist, xout = np.histogram(X, bins)
pdf = hist / N / del_  # Divide by del to make Total_Area=1

plt.figure(1)
plt.bar(xout[:-1], pdf, width=del_, align='edge', alpha=0.6)
plt.grid(True)


def gaussian_pdf(x, mu, sig):
    return (1 / (sig * np.sqrt(2 * np.pi))) * np.exp(-((x - mu) ** 2) / (2 * sig ** 2))

z = np.arange(min(X), max(X), 0.1)
plt.plot(z, gaussian_pdf(z, mu, sig), 'r', linewidth=3)


print("Mean Thickness:", mean_thickness)
print("Standard Deviation:", std_dev)

plt.xlabel('Thickness (cm)')
plt.ylabel('Frequency')
plt.title('Comparison of Histogram and Gaussian Distribution for n = '+str(n))
plt.show()
