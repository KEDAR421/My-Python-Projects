import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# X(z) = 1 / ((1 - 0.9*z^(-1))^2 * (1 + 0.9*z^(-1)))
#step 2:Residue and Poles
b = [1,0,0,0]
a = [1,-0.9,-0.81,0.729]

print(f'Numerator coefficients (b): {b}')
print(f'Denominator coefficients (a): {a}')
residues, poles, direct_term = signal.residuez(b, a)

print("Residues:", residues)
print("Poles:", poles)
print("Direct Term:", direct_term)

# Step 3: x(n) by filter
n = np.arange(0,8,1)##function in NumPy is used to generate arrays with evenly spaced values within a specified interval.
impulse=np.zeros_like(n)
impulse[0]=1
x_n = signal.lfilter(b, a, impulse)
print(f'Sequence x(n) from dimpulse: {x_n}')
# Step 4: x(n) analytically from X(z)
step_signal=np.zeros_like(n)
print("step ",step_signal)
step_signal[0:]=1
print("fff",step_signal)
x_n_analytical=((0.25*(-0.9)**n)+(0.5*(n+1)*(0.9)**n)+(0.25*(0.9)**n))*step_signal
print("analytical",x_n_analytical)
plt.subplot(2,1,1)
plt.stem(n,x_n)
plt.xlabel('n-->')
plt.ylabel('amplitude-->')
plt.title('x_n signal by filter:- ')

plt.subplot(2,1,2)
plt.stem(n,x_n_analytical)
plt.xlabel('n-->')
plt.ylabel('amplitude-->')
plt.title('x_n signal by filter analytically:- ')
plt.subplots_adjust(hspace=0.5)
plt.show()
# Step 6:pole-zero plot from X(z)
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
