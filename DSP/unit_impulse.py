import numpy as np
import matplotlib.pyplot as plt
def impulse(t):
    return np.where(t==0,1,0)
t=np.arange(-5,6,0.5)
y=impulse(t)
print(t,y)
plt.plot(t,y)
plt.title('continous unit impulse signal')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()

t1=np.arange(-6,6,1)
y1=impulse(t1)
plt.stem(t1,y1)
plt.title('discrete impulse signal')
plt.show()