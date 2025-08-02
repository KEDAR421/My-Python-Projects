import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from scipy.signal import lfilter,tf2zpk,residue
t=np.arange(0,10,1)
step_signal = np.zeros(10)
step_signal[2:] = 1

tn = 0.5**(t-2)
xn = tn*step_signal
plt.stem(t,xn)
plt.show()

z = sp.symbols('z')
#Xz =sum([xn[k]z*-k for k in range(0,10)])
#print(Xz)


a= [0,0,1]
b = [1,-0.5,0]
wn = lfilter(a,b,xn)
print(wn)
plt.stem(t,wn)
plt.show()
zeros, poles, gain = tf2zpk(a,b)

theta = np.linspace(0,2*np.pi,100)
x = np.cos(theta)
y = np.sin(theta)

plt.figure()

plt.plot(x,y ,'-',  label='Unit circle')
plt.plot(np.real(zeros), np.imag(zeros), 'o', markersize=5, label='Zeros')
plt.plot(np.real(poles), np.imag(poles), 'x', markersize=5, label='Poles')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Pole-Zero Plot')
plt.grid(True)
plt.legend(loc = 'upper right')
plt.show()