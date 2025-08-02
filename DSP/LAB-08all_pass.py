import numpy as np
import matplotlib.pyplot as plt
# Constants
wo = np.pi / 4
r = 0.9
w = np.linspace(-2 * np.pi, 2 * np.pi, 1024)

# Transfer function
def all_pass_filter(r, omega0, omega):
    numerator = r**2 - 2 * r * np.cos(omega0) * np.exp(-1j * omega) + np.exp(-2j * omega)
    denominator = 1 - 2 * r * np.cos(omega0) * np.exp(-1j * omega) + (r**2) * np.exp(-2j * omega)
    H_z = numerator / denominator
    return H_z

# Calculate transfer function for the all-pass filter
H_z = all_pass_filter(r, wo, w)

# Magnitude and Phase
magnitude = np.abs(H_z)
phase = np.angle(H_z)

# Plotting
plt.figure(figsize=(10, 6))

# Magnitude Spectrum
plt.subplot(2, 1, 1)
plt.plot(w, magnitude)
plt.title('Magnitude Spectrum of All-Pass Filter')
plt.xlabel('Frequency (ω)')
plt.ylabel('Magnitude')
plt.grid()

# Phase Spectrum
plt.subplot(2, 1, 2)
plt.plot(w, phase)
plt.title('Phase Spectrum of All-Pass Filter')
plt.xlabel('Frequency (ω)')
plt.ylabel('Phase (radians)')
plt.grid()

plt.tight_layout()
plt.show()
