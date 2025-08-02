import numpy as np
import matplotlib.pyplot as plt
x1=[2,3,4,1]
t1=np.arange(0,4,1)
x2=[3,1,4,5,2]
t2=np.arange(0,5,1)
y=np.convolve(x1,x2)
t=np.arange(0,8,1)

plt.show()
plt.subplot(3,1,1)
plt.stem(t1,x1)
plt.subplot(3,1,2)
plt.stem(t2,x2)
plt.subplot(3,1,3)
plt.stem(t,y)
plt.show()

print(y)