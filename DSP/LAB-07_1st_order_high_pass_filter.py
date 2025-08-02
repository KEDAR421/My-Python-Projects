import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

# Parameters
alpha = 0.9
w = np.linspace(-np.pi, np.pi, 1024)

# Transfer function H(z)
numerator = (1 - alpha) / 2 * (1 - np.exp(-1j * w))
denominator = 1 + alpha * np.exp(-1j * w)
H_z = numerator / denominator

# Magnitude and Phase
magnitude = np.abs(H_z)
phase = np.angle(H_z)

# Plot
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(w, magnitude, label="Magnitude")
plt.title("Magnitude Spectrum of H(z)")
plt.xlabel("Frequency (rad/sample)")
plt.ylabel("|H(z)|")
plt.grid(True)

# Plot
plt.subplot(2, 1, 2)
plt.plot(w, phase, label="Phase", color='orange')
plt.title("Phase Spectrum of H(z)")
plt.xlabel("Frequency (rad/sample)")
plt.ylabel("Phase (radians)")
plt.grid(True)

plt.tight_layout()
plt.show()


b=[1,-1]
a=[20,18]
#pole_zero plot
zeros, poles, _ = signal.tf2zpk(b, a)
#plt.figure()
theta = np.linspace(0,2*np.pi,100)
x = np.cos(theta)
y = np.sin(theta)

plt.plot(x,y ,'-',  label='Unit circle')
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', label='Zeros')
plt.scatter(np.real(poles), np.imag(poles), marker='x', label='Poles')
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title('Pole-Zero Plot')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.grid()
plt.legend()
plt.show()