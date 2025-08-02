import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

# Parameters
a =0.5
b=0.5
k=0.25
w = np.linspace(-np.pi, np.pi, 1024)  # Frequency range from -π to π

# Transfer function H(z)
numerator =k * ((1 + np.exp(-1j * w))**2)
denominator = (1 - a * np.exp(-1j * w)*(1-b*np.exp(-1j*w)))
H_z = numerator / denominator

# Magnitude and Phase calculation
magnitude = np.abs(H_z)
phase = np.angle(H_z)

# Plotting the magnitude spectrum
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(w, magnitude, label="Magnitude")
plt.title("Magnitude Spectrum of H(z)")
plt.xlabel("Frequency (rad/sample)")
plt.ylabel("|H(z)|")
plt.grid(True)

# Plotting the phase spectrum
plt.subplot(2, 1, 2)
plt.plot(w, phase, label="Phase", color='orange')
plt.title("Phase Spectrum of H(z)")
plt.xlabel("Frequency (rad/sample)")
plt.ylabel("Phase (radians)")
plt.grid(True)

# Display plots
plt.tight_layout()
plt.show()


b_num=[0.25,0.5,0.25]
a_deno=[1,-1,0.25]
#pole_zero plot
zeros, poles, _ = signal.tf2zpk(b_num, a_deno)
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