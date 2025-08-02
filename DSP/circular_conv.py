import numpy as np
import matplotlib.pyplot as plt
# Given sequences
x1_n = np.array([1, 2, 3, 4])
x2_n = np.array([1, 2, 2])

# a) Perform circular convolution using folding, shifting, and multiplication
# Zero-pad x2 to make it the same length as x1
N = max(len(x1_n), len(x2_n))
x1_n = np.pad(x1_n, (0, N - len(x1_n)), mode='constant')
x2_n = np.pad(x2_n, (0, N - len(x2_n)), mode='constant')

# Circular convolution using folding, shifting, and multiplication
circular_conv = np.zeros(N, dtype=complex)
for n in range(N):
    for k in range(N):
        circular_conv[n] += x1_n[k] * x2_n[(n - k) % N]

# b) Verify the results using the DFT function
# Calculate DFT of both sequences
X1 = np.fft.fft(x1_n)
X2 = np.fft.fft(x2_n)

# Perform element-wise multiplication in the frequency domain and take the inverse DFT
circular_conv_dft = np.fft.ifft(X1 * X2)

# Plotting both results
plt.figure(figsize=(12, 6))

# Circular convolution using manual method
plt.subplot(1, 2, 1)
plt.stem(np.real(circular_conv))
plt.title("Circular Convolution (Manual Calculation)")
plt.xlabel("n")
plt.ylabel("Amplitude")

# Circular convolution using DFT method
plt.subplot(1, 2, 2)
plt.stem(np.real(circular_conv_dft))
plt.title("Circular Convolution (DFT Method)")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

# Showing both results for comparison
circular_conv, circular_conv_dft
