import numpy as np
import matplotlib.pyplot as plt

# Given sequence
x_n = np.array([1, 2, 3, 4])

#DFT of x[n] by equation
N =np.arange(0,8,1)
dft_x_n = np.array([sum(x_n[n] * np.exp(-2j * np.pi * n * k / N) for k in range(N-1)) for n in range(len(x_n))])

#DFT by fft function
fft_x_n = np.fft.fft(x_n)

# Plot
plt.figure(figsize=(12, 6))

# Manual DFT
plt.subplot(1, 2, 1)
plt.stem(np.abs(dft_x_n),N)
plt.title("Magnitude of DFT (Manual Calculation)")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")

# Inbuilt FFT
plt.subplot(1, 2, 2)
plt.stem(np.abs(fft_x_n),N)
plt.title("Magnitude of DFT (Inbuilt FFT)")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")

plt.tight_layout()
plt.show()

# Showing both results for comparison
#dft_x_n, fft_x_n
