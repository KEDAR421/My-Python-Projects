
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

alpha = 0.8
beta = 0.34
omega = np.linspace(-2 * np.pi, 2 * np.pi, 1024)

H = ((1 - alpha) / 2) * (1 - np.exp(-2j * omega)) / (1 - (beta * (1 + alpha) * np.exp(-1j * omega)) + alpha * np.exp(-2j * omega))

magnitude = np.abs(H)
phase = np.angle(H)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(omega, magnitude, color='b', label="Magnitude")
plt.title('Magnitude Spectrum of the Band-Pass Filter')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Magnitude')
plt.grid()

peak_magnitude = np.max(magnitude)
hp = peak_magnitude / np.sqrt(2)
wc=[]
for i in range(1,len(magnitude)):
    if(magnitude[i-1]<hp<=magnitude[i]):
        wc
    else:
        wc=0
print(wc)
half_power_indices = np.where(magnitude >= hp)[0]
bandwidth = omega[half_power_indices[-1]] - omega[half_power_indices[0]]

plt.axhline(y=hp, color='g', linestyle='--', label='-3 dB Level')
plt.axvline(x=omega[half_power_indices[0]], color='r', linestyle='--', label='Bandwidth Edges')
plt.axvline(x=omega[half_power_indices[-1]], color='r', linestyle='--')

plt.fill_between(omega[half_power_indices[0]:half_power_indices[-1]], 0, magnitude[half_power_indices[0]:half_power_indices[-1]], color='yellow', alpha=0.3, label='Bandwidth')

plt.legend()

plt.subplot(2, 1, 2)
plt.plot(omega, phase, color='r')
plt.title('Phase Spectrum of the Band-Pass Filter')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Phase (radians)')
plt.grid()

plt.tight_layout()
plt.show()

print(f"Estimated Bandwidth: {bandwidth:.4f} radians/sample")

b = np.array([1, 0, -1])
a = np.array([10, -6.12, 8])
z, p, k = signal.tf2zpk(b, a)

plt.figure()
plt.scatter(np.real(z), np.imag(z), color='r', marker='o', label='Zeros')
plt.scatter(np.real(p), np.imag(p), color='b', marker='x', label='Poles')
unit_circle = plt.Circle((0, 0), 1, color='black', fill=False, linestyle='--')
plt.gca().add_artist(unit_circle)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Pole-Zero Plot')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid()
plt.axis('equal')
plt.legend()
plt.show()