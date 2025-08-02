import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

n=np.arange(0,11,1)
step_signal=np.zeros_like(n)
step_signal[2:]=1
print(step_signal)
xn=(0.5)**(n-2)*step_signal

impulse_signal=np.zeros_like(n)
impulse_signal[0]=1

#x(z)=(1/z^2-o.5z)
b_numerator=np.array([0,0,1])
a_deno=np.array([1,-0.5,0])
filtered_signal=signal.lfilter(b_numerator,a_deno,impulse_signal)

plt.subplot(2,1,1)
plt.stem(n,xn)
plt.xlabel('n-->')
plt.title('xn-->')
plt.ylabel('amplitude-->')

plt.subplot(2,1,2)
plt.stem(n,filtered_signal)
plt.xlabel('n-->')
plt.ylabel('amplitude-->')
plt.title('z-transform signal')
plt.subplots_adjust(hspace=0.5)
plt.show()
# Step 6:pole-zero  X(z)

b=[0,0,1]
a=[1,-0.5,0]
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