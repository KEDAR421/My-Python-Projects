import numpy as np
import matplotlib.pyplot as plt


def circular_convolution(x, h):
    # Determine the length of the result
    N = max(len(x), len(h))

    # Pad x and h to length N
    x = np.pad(x, (0, N - len(x)), mode='constant')
    h = np.pad(h, (0, N - len(h)), mode='constant')

    # Compute the circular convolution
    result = np.zeros(N)
    for n in range(N):
        for k in range(N):
            result[n] += x[k] * h[(n - k) % N]

    return result


# Example signals
x = [1, 2, 3, 4]  # Signal 1
h = [1, 0, -1, 0]  # Signal 2

# Compute circular convolution
circular_conv = circular_convolution(x, h)

# Plotting
plt.figure(figsize=(10, 5))

# Plot Signal 1
plt.subplot(3, 1, 1)
plt.stem(x, basefmt="-")
plt.title("Signal x[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")

# Plot Signal 2
plt.subplot(3, 1, 2)
plt.stem(h, basefmt="-")
plt.title("Signal h[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")

# Plot Circular Convolution
plt.subplot(3, 1, 3)
plt.stem(circular_conv, basefmt="-")
plt.title("Circular Convolution of x[n] and h[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
