import numpy as np
import matplotlib.pyplot as plt

#x[n]
x_n = np.array([1, 2, 3, 4])
N=8 #change the value as per requirment

#  DFT
def DFT_manual(x, N):
    X_k = []
    for k in range(N):
        sum_value = 0
        for n in range(len(x)):
            sum_value += x[n] * np.exp(-2j * np.pi * k * n / N)
        X_k.append(sum_value)
    return np.array(X_k)

# Calculate DFT using FFT by inbuilt
X_k_fft = np.fft.fft(x_n, N)

# Calculate DFT manually for N=16 and N=8
X_k_manual = DFT_manual(x_n, N)

# Plot
plt.figure(figsize=(12, 6))

# Manual DFT
plt.subplot(1, 2, 1)
plt.stem(np.abs(X_k_fft))
plt.title("Magnitude of DFT (Manually) for n=12")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")

# Inbuilt FFT
plt.subplot(1, 2, 2)
plt.stem(np.abs(X_k_manual))
plt.title("Magnitude of DFT (Inbuilt FFT) for N=12")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")

plt.tight_layout()
plt.show()