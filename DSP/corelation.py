import numpy as np
import matplotlib.pyplot as plt

# Define two discrete-time signals
x = np.array([ 3, 4, 5])
y = np.array([5, 4, 3, 2, 1])

# Ensure that y is the same length as x by padding with zeros if necessary
N = len(x)
M = len(y)
if M < N:
    y = np.pad(y, (0, N - M))

# Manual cross-correlation computation
def cross_correlation(x, y):
    N = len(x)
    correlation = []
    for lag in range(-N + 1, N):
        sum_product = 0
        for n in range(N):
            if 0 <= n + lag < N:
                sum_product += x[n] * y[n + lag]
        correlation.append(sum_product)
    return np.array(correlation)

# Compute the cross-correlation
correlation = cross_correlation(x, y)

# Compute lags
lags = np.arange(-len(x) + 1, len(x))

# Plot the signals and their correlation
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.stem(x)
plt.title('Signal x')

plt.subplot(3, 1, 2)
plt.stem(y)
plt.title('Signal y')

plt.subplot(3, 1, 3)
plt.stem(lags, correlation)
plt.title('Cross-Correlation')
plt.xlabel('Lag')
plt.ylabel('Correlation')

plt.tight_layout()
plt.show()
