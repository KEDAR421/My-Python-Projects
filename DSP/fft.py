import numpy as np
import matplotlib.pyplot as plt

# Define the sampling rate and time vector
sampling_rate = 1000  # 1000 samples per second
T = 1.0 / sampling_rate  # Sampling interval
t = np.arange(0, 1, T)  # Time vector (1 second)

# Create a signal (sum of sine waves)
f1 = 50  # Frequency of the first sine wave (50 Hz)
f2 = 120  # Frequency of the second sine wave (120 Hz)
signal = 3 * np.sin(2 * np.pi * f1 * t) + 2 * np.sin(2 * np.pi * f2 * t)

# Compute the FFT of the signal
fft_signal = np.fft.fft(signal)
N = len(fft_signal)  # Number of samples

# Compute the frequency bins (positive frequencies only)
frequencies = np.fft.fftfreq(N, T)[:N // 2]

# Plot the time-domain signal
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Time Domain Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Plot the magnitude of the FFT (frequency domain)
plt.subplot(2, 1, 2)
plt.plot(frequencies, 2.0 / N * np.abs(fft_signal[:N // 2]))  # Normalize the magnitude
plt.title('Frequency Domain (FFT)')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
