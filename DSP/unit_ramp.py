import numpy as np
import matplotlib.pyplot as plt
def ramp(t):
    return np.where(t>=0,t,0)
t=np.arange(-5,5,1)
y=ramp(t)
plt.plot(t,y)
plt.title('continous ramp')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()

t1=np.arange(-6,6,1)
y1=ramp(t1)
plt.stem(t1,y1)
plt.title('discrete ramp')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()
