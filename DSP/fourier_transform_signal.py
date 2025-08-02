import numpy as np
import matplotlib.pyplot as plt

# Define the sampling rate and time array
sampling_rate = 1000  # Samples per second
T = 1.0 / sampling_rate  # Sampling interval
t = np.arange(0, 1, T)  # Time vector (1 second)

# Create a signal (sum of sine waves)
f1 = 50  # Frequency of the first sine wave (50 Hz)
f2 = 120  # Frequency of the second sine wave (120 Hz)
signal = 3*np.sin(2*np.pi*f1*t) + 2*np.sin(2*np.pi*f2*t)

# Compute the Fourier Transform using numpy's FFT
fft_signal = np.fft.fft(signal)
N = len(fft_signal)  # Number of samples
frequencies = np.fft.fftfreq(N, T)  # Frequency bins

# Plot the signal in time domain
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Time Domain Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Plot the magnitude of the Fourier Transform (frequency domain)
plt.subplot(2, 1, 2)
plt.plot(frequencies[:N // 2], 2.0 / N * np.abs(fft_signal[:N // 2]))  # Positive frequencies only
plt.title('Frequency Domain (Fourier Transform)')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
