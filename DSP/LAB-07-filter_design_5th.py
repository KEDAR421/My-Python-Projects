import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft, fftfreq

# Parameters
Fs = 2000  # Sampling frequency
N = 1024  # Number of samples
n = np.arange(N)  # Time
# Frequencies in Hz
frequencies = [0, 200, 400, 600, 800, 1000]
# Angular frequencies
omega = [2 * np.pi * f / Fs for f in frequencies]
# Input signal x(n) as a sum of cosines with the given
frequencies
x = sum([np.cos(w * n) for w in omega])
# FFT of input signal
X = fft(x)
# Frequency range for H(w)
w = np.linspace(-np.pi, np.pi, N)
# constants for transfer functions
alpha = 0.9
K = 0.25
a = 0.5
b = 0.5
# Define transfer functions H1, H2, H3, H4
H1 = ((1 - alpha) / 2) * (1 + np.exp(-1j * w)) / (1 - alpha *
                                                  np.exp(-1j * w))
H2 = ((1 - alpha) / 2) * (1 - np.exp(-1j * w)) / (1 - alpha *
                                                  np.exp(-1j * w))
H3 = (K * ((1 + np.exp(-1j * w)) ** 2)) / ((1 - a * np.exp(-1j
                                                           * w)) * (1 - b * np.exp(-1j * w)))
H4 = (K * ((1 - np.exp(-1j * w)) ** 2)) / ((1 - a * np.exp(-1j
                                                           * w)) * (1 - b * np.exp(-1j * w)))
# Shift H1, H2, H3, H4 to match frequency range of X
new_H1 = np.fft.ifftshift(H1)
new_H2 = np.fft.ifftshift(H2)
new_H3 = np.fft.ifftshift(H3)
new_H4 = np.fft.ifftshift(H4)

# Multiply X with each transfer function to find Y(w) for
Y1 = X * new_H1
Y2 = X * new_H2
Y3 = X * new_H3
Y4 = X * new_H4
# Find the output in the time domain by taking the inverse FFT
y1 = ifft(Y1).real
y2 = ifft(Y2).real
y3 = ifft(Y3).real
y4 = ifft(Y4).real
# Plot the output signals for each system
plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)
plt.plot(n, x)
plt.title("Input Signal x(n)")
plt.xlabel("Samples (n)")
plt.ylabel("Amplitude")
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(w, X, )
plt.title("X(w)")

plt.xlabel("w")
plt.ylabel("Amplitude")
plt.grid()
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 8))
plt.subplot(4, 1, 1)
plt.plot(n, y1, label='Output y1(n) for H1')
plt.title('Output time domain y1(n)')
plt.grid()
plt.subplot(4, 1, 2)
plt.plot(n, y2, label='Output y2(n) for H2')
plt.title('Output time domain y2(n)')
plt.grid()
plt.subplot(4, 1, 3)
plt.plot(n, y3, label='Output y3(n) for H3')
plt.title('Output time domain y3(n)')
plt.grid()
plt.subplot(4, 1, 4)
plt.plot(n, y4, label='Output y4(n) for H4')
plt.title('Output time domain y4(n)')

plt.grid()
plt.tight_layout()
plt.show()
# Plot the frequency spectrum of the output signals
Y1_spectrum = np.abs(fft(y1))
Y2_spectrum = np.abs(fft(y2))
Y3_spectrum = np.abs(fft(y3))
Y4_spectrum = np.abs(fft(y4))
freqs = fftfreq(N, 1 / Fs)
plt.figure(figsize=(10, 8))
plt.subplot(4, 1, 1)
plt.plot(freqs[:N // 2], Y1_spectrum[:N // 2], label='Spectrum of y1(n)')
plt.title('Frequency Spectrum of y1(n)')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid()
plt.subplot(4, 1, 2)
plt.plot(freqs[:N // 2], Y2_spectrum[:N // 2], label='Spectrum of y2(n)')
plt.title('Frequency Spectrum of y2(n)')

plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid()
plt.subplot(4, 1, 3)
plt.plot(freqs[:N // 2], Y3_spectrum[:N // 2], label='Spectrum of y3(n)')
plt.title('Frequency Spectrum of y3(n)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid()
plt.subplot(4, 1, 4)
plt.plot(freqs[:N // 2], Y4_spectrum[:N // 2], label='Spectrum of y4(n)')
plt.title('Frequency Spectrum of y4(n)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid()
plt.tight_layout()
plt.show()
# Optionally: plot the magnitude of the frequency responses (H1, H2, H3, H4)
plt.figure(figsize=(10, 8))
plt.subplot(4, 1, 1)

plt.plot(w, np.abs(H1))
plt.title('Magnitude Response |H1(w)|')
plt.grid()
plt.subplot(4, 1, 2)
plt.plot(w, np.abs(H2))
plt.title('Magnitude Response |H2(w)|')
plt.grid()
plt.subplot(4, 1, 3)
plt.plot(w, np.abs(H3))
plt.title('Magnitude Response |H3(w)|')
plt.grid()
plt.subplot(4, 1, 4)
plt.plot(w, np.abs(H4))
plt.title('Magnitude Response |H4(w)|')
plt.grid()
plt.tight_layout()
plt.show()