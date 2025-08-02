import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

# Parameters
a =0.8
b=0.5
k=(1+a)/2
w = np.linspace(-2*np.pi, 2*np.pi, 1024)  # Frequency range from -π to π

# Transfer function H(z) calculation
numerator =k * (1-2*b*(np.exp(-1j*w))+(np.exp(-2j * w)))
denominator = (1-b*(1 + a) * (np.exp(-1j * w))+a*(np.exp(-2j*w)))
H_z = numerator / denominator

# Magnitude and Phase calculation
magnitude = np.abs(H_z)
phase = np.angle(H_z)

peak_magnitude = np.max(magnitude)
hp = peak_magnitude / np.sqrt(2)
wc=[]
for i in range(1, len(magnitude)):
    if magnitude[i-1] < hp <= magnitude[i]:
        wc.append(w[i])
    elif magnitude[i-1] > hp >= magnitude[i]:
        wc.append(w[i])

cutoff_frequencies = np.array(wc)

# Plotting the magnitude spectrum
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(w, magnitude, label="Magnitude")

plt.axhline(y=hp, color='r', linestyle='--')
for cf in cutoff_frequencies:
    plt.axvline(x=cf, color='r', linestyle='--')

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


b_num=[9,-9,9]
a_deno=[10,-9,8]
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