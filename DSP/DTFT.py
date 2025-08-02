# import numpy as np
# import matplotlib.pyplot as plt
#
# # Define the discrete signal
# n = np.arange(0, 20)  # Sample indices
# signal = np.sin(0.2 * np.pi * n)  # Example: A discrete sine wave
#
# # Define the frequency range for the DTFT (normalized frequency)
# omega = np.linspace(-np.pi, np.pi, 1000)
#
# # DTFT computation
# def compute_dtft(signal, n, omega):
#     dtft = np.array([np.sum(signal * np.exp(-1j * w * n)) for w in omega])
#     return dtft
#
# # Compute DTFT
# dtft_signal = compute_dtft(signal, n, omega)
#
# # Plot the original discrete signal
# plt.figure(figsize=(12, 6))
#
# plt.subplot(2, 1, 1)
# plt.stem(n, signal)
# plt.title('Discrete Signal')
# plt.xlabel('Sample Index n')
# plt.ylabel('Amplitude')
#
# # Plot the magnitude of the DTFT
# plt.subplot(2, 1, 2)
# plt.plot(omega, np.abs(dtft_signal))
# plt.title('Magnitude of the DTFT')
# plt.xlabel('Frequency (rad/sample)')
# plt.ylabel('Magnitude')
# plt.grid(True)
#
# plt.tight_layout()
# plt.show()



import numpy as np
import matplotlib.pyplot as plt

# Define the discrete-time signal (e.g., a finite-length sequence)
n = np.arange(0, 10)  # Time index
x = np.sin(0.2 * np.pi * n)  # Example signal (sinusoidal)

# Define frequency range for DTFT (from -pi to pi)
omega = np.linspace(-np.pi, np.pi, 1000)  # Frequency values

# Compute DTFT manually
def dtft(x, n, omega):
    X = np.zeros(len(omega), dtype=complex)
    for k in range(len(omega)):
        X[k] = np.sum(x * np.exp(-1j * omega[k] * n))
    return X

# Compute DTFT of the signal
X_omega = dtft(x, n, omega)

# Plot the magnitude and phase of the DTFT
plt.figure(figsize=(12, 6))

# Magnitude plot
plt.subplot(2, 1, 1)
plt.plot(omega, np.abs(X_omega))
plt.title('Magnitude of DTFT')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Magnitude')
plt.grid(True)

# Phase plot
plt.subplot(2, 1, 2)
plt.plot(omega, np.angle(X_omega))
plt.title('Phase of DTFT')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Phase (radians)')
plt.grid(True)

plt.tight_layout()
plt.show()
