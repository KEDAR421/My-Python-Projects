import numpy as np
import matplotlib.pyplot as plt

t=np.arange(-3,2,1)
signal = np.array([3, 1, -2, 3, 1])

shift = 1
shifted_signal = np.zeros_like(signal)
if shift > 0:
    shifted_signal[shift:] = signal[:-shift]
else:
    shifted_signal[:shift] = signal[-shift:]

plt.subplot(1,2,1)
plt.title("original signal")
new_time=t-shift
plt.stem(t,signal)
plt.subplot(1,2,2)
plt.title("shifted signal:-")
plt.stem(new_time,shifted_signal)
plt.show()

#shifting by function
def shifting(x,time,shift1):
    new_time=time-shift
    return x,new_time

shift1=-1
shift_x,shift_t=shifting(signal,t,shift1)
plt.subplot(1,2,1)
plt.title('original by function')
plt.stem(t,signal)
plt.subplot(1,2,2)
plt.title('shifted signal by function')
plt.stem(shift_t,shift_x)
plt.show()