import numpy as np
import matplotlib.pyplot as plt

x1=np.array([1,2,0,3,4])
t1=np.arange(-2,3,1)

plt.figure(figsize=(14,10))
plt.subplot(1,4,1)
plt.stem(t1,x1)
plt.title('original signal of (x1)-->')
plt.xlabel('n-->')
plt.ylabel('amplitude-->')

t1_flipped=np.flip(t1*-1)
x1_flipped=list(reversed(x1))

plt.subplot(1,4,2)
plt.stem(t1_flipped,x1_flipped)
plt.title('folded signal of (x1)-->')
plt.xlabel('n-->')
plt.ylabel('amplitude-->')

t2=np.arange(-1,5,1)
y2=np.array([2,0,3,4,5,6])

plt.subplot(1,4,3)
plt.stem(t2,y2)
plt.title('original signal of (x2)-->')
plt.xlabel('n-->')
plt.ylabel('amplitude-->')

plt.subplot(1,4,4)
t2_flipped=np.flip(t2*-1)
x2_flipped=list(reversed(y2))

plt.stem(t2_flipped,x2_flipped)
plt.title('folded signal of (x2)-->')
plt.xlabel('n-->')
plt.ylabel('amplitude-->')
plt.show()

#folding by function
def folding(signal,time):
    time_flip=-np.flip(time)
    flip_signal=np.flip(np.flip(signal*-1))

    return flip_signal,time_flip
x3=np.array([1,2,0,3,4])
t3=np.arange(-2,3,1)

flipped_signal,flipped_time=folding(x3,t3)
plt.subplot(1,2,1)
plt.title('original by function')
plt.stem(x3,t3)

plt.subplot(1,2,2)
plt.title('folded by function')
plt.stem(flipped_signal,flipped_time)
plt.show()







