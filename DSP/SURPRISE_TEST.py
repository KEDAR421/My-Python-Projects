#write a pythone code to calculate the impulse response of the system defined by
#the following transfer function
#H(Z)=(2.2403+2.4908*Z^-1+2.2403*Z^-2)/(1-0.4*Z^-1+0.75*Z^-2)
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter
import scipy.signal as signal
numerator=[2.2403,2.4908,2.2403]
denominator=[1,-0.4,0.75]
#let take for 50 samples
n_sample=50
impulse_signal=np.zeros(n_sample)
print(impulse_signal)
impulse_signal[0]=1
print(impulse_signal)
step_signal=np.zeros(n_sample)
step_signal[np.where(n_sample>=0)]=1
print(step_signal)
#impulse response of transfer function
impulse_response=lfilter(numerator,denominator,impulse_signal)

#analytically
#Hn=(A*(0.2+0.843j)**n_sample+B*(0.2-0.843j)**n_sample)*(step_signal(-n_sample-1))+impulse_signal*C
#plotting
plt.subplot(2,1,1)
plt.title('impulse signal')
plt.stem(impulse_signal)
plt.xlabel("samples")
plt.ylabel("amplitude")

plt.subplot(2,1,2)
plt.title('impulse response')
plt.stem(impulse_response)
plt.xlabel("samples")
plt.ylabel("amplitude")
plt.subplots_adjust(hspace=0.5)
plt.show()

#pole_zero plot
zeros, poles, _ = signal.tf2zpk(numerator, denominator)
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
