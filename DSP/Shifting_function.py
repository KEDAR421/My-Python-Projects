import numpy as np
import matplotlib.pyplot as plt
x=[2,1,3,6,1,-2]
n=np.arange(-2,4,1)
# n1=min(n)
# print(n)
# n_max=max(n)
# n_new=np.zeros_like(n)
#
# shift=1
# if(shift>=0):
#        n_new=np.arange(min(n)-shift,max(n)+1-shift,1)
# else:
#     n_new=np.arange(min(n)-shift,max(n)+1-shift,1)
# print(n_new)
def shifting_function(signal,time,shift_amount):
    n_new=np.zeros_like(time+shift_amount)
    if (shift_amount >= 0):
        n_new = np.arange(min(time) - shift_amount, max(time) + 1 - shift_amount, 1)
    else:
        n_new = np.arange(min(time) - shift_amount, max(time) + 1 - shift_amount, 1)
    return signal,n_new,shift_amount

shifted_signal,shifted_time,shift=shifting_function(x,n,-2)
plt.subplot(2,1,1)
plt.stem(n,x)
plt.subplot(2,1,2)
plt.stem(shifted_time,shifted_signal)

plt.show()