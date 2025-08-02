import numpy as np
import matplotlib.pyplot as plt

# Given sequences
x1 = np.array([1, 2, 3, 4])
x2 = np.array([1, 2, 2])
N = max(len(x1), len(x2))
x1_padded = np.pad(x1, (0,N-len(x1)))
x2_padded = np.pad(x2, (0, N - len(x2)))
print(x1_padded)
print(x2_padded)
def circular_convolution(x1, x2):
    N = len(x1)
    y = np.zeros(N)
    for n in range(N):
        # Shifted and folded x2
        x2_shifted = np.roll(x2, n)[::-1]
        # Multiply and sum for each shift
        y[n] = np.sum(x1 * x2_shifted)
    return y

#circular convolution manually
y_circular_manual = circular_convolution(x1_padded, x2_padded)
# Circular Convolution using DFT
def DFT_manual(x, N):
    X_k = []
    for k in range(N):
        sum_value = 0
        for n in range(len(x)):
            sum_value += x[n] * np.exp(-2j * np.pi * k * n / N)
        X_k.append(sum_value)
    return np.array(X_k)
X1 = DFT_manual(x1,4)
X2 = DFT_manual(x2,4)
Y_dft = np.fft.ifft(X1 * X2).real  # Inverse DFT of the element-wise product

# Plot results
k = np.arange(N)

plt.figure(figsize=(12, 6))

# Plotting
plt.subplot(1, 2, 1)
plt.stem(-k, y_circular_manual, basefmt="-")
plt.title("Circular Convolution using Manual Method")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid()

# Plotting
plt.subplot(1, 2, 2)
plt.stem(k, Y_dft, basefmt="-")
plt.title("Circular Convolution using DFT")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid()

plt.tight_layout()
plt.show()
