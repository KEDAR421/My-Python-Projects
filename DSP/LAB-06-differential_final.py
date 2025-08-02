import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter
import scipy.signal as signal
n=np.arange(-20,101,1)
xn=np.zeros_like(n)
#xn[n==0]=1
a=[1,-1,0.9]
b=[1]
xn[np.where(n == 0)] = 1
h_impulse_response= lfilter(b, a, xn)
xn1=np.zeros_like(n)
xn1[np.where(n>=0)]=1
h_step_response=lfilter(b,a,xn1)
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

plt.subplot(2,1,1)
plt.title("impulse signal")
plt.xlabel('n')
plt.ylabel('amplitude')
plt.stem(n,xn)

plt.subplot(2,1,2)
plt.title("unit step signal")
plt.xlabel('n')
plt.ylabel('amplitude')
plt.stem(n,xn1)
plt.subplots_adjust(hspace=1)
plt.show()

plt.subplot(2,1,1)
plt.title("impulse response")
plt.xlabel('n')
plt.ylabel('amplitude')
plt.stem(n,h_impulse_response)

plt.subplot(2,1,2)
plt.title('step response')
plt.stem(n,h_step_response)
plt.xlabel('n')
plt.ylabel('amplitude')
plt.subplots_adjust(hspace=1)


