import numpy as np
import matplotlib.pyplot as plt

# Constants
wo = np.pi / 4
r_values = [0.85, 0.95]
w = np.linspace(-2 * np.pi, 2 * np.pi, 1024)

# Transfer function
def notch_filter(r, omega0, omega):
    numerator = 1 - 2 * np.cos(omega0) * np.exp(-1j * omega) + np.exp(-2j * omega)
    denominator = 1 - 2 * r * np.cos(omega0) * np.exp(-1j * omega) + (r**2) * np.exp(-2j * omega)
    H_z = numerator / denominator
    return H_z

# Calculate transfer function for both r values
H_r85 = notch_filter(r_values[0], wo, w)
H_r95 = notch_filter(r_values[1], wo, w)

# Magnitude and Phase for both filters
magnitude_r85 = np.abs(H_r85)
phase_r85 = np.angle(H_r85)
magnitude_r95 = np.abs(H_r95)
phase_r95 = np.angle(H_r95)

# Difference in magnitude and phase
magnitude_diff = magnitude_r85 - magnitude_r95
phase_diff = phase_r85 - phase_r95

# Plotting
plt.figure(figsize=(12, 8))

# Magnitude Spectrum
plt.subplot(2, 1, 1)
plt.plot(w, magnitude_r85, label='r = 0.85')
plt.plot(w, magnitude_r95, label='r = 0.95')
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency (ω)')
plt.ylabel('Magnitude')
plt.legend()
plt.grid()

# Phase Spectrum
plt.subplot(2, 1, 2)
plt.plot(w, phase_r85, label='r = 0.85')
plt.plot(w, phase_r95, label='r = 0.95')
plt.title('Phase Spectrum')
plt.xlabel('Frequency (ω)')
plt.ylabel('Phase (radians)')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
