import numpy as np
import matplotlib.pyplot as plt
n1=np.arange(-2,2,1)
x=np.array([3,1,6,5])
n2=np.arange(1,5,1)
x2=np.array([3,8,5,1])
#addition
n3min=min(n1[0],n2[0])
n3max=max(n1[-1],n2[-1])
n3=np.arange(n3min,n3max+1,1)
xnew=np.zeros_like(n3)
xnew[(n3>=n1[0])&(n3<=n1[-1])]=x
x2new=np.zeros_like(n3)
x2new[(n3>=n2[0])&(n3<=n2[-1])]=x2
x3=xnew+x2new
print(x2new)
print(n1)
print(x3)
plt.subplot(3,1,1)
plt.stem(n1,x)
plt.subplot(3,1,2)
plt.stem(n2,x2)
plt.subplot(3,1,3)
plt.stem(n3,x3)
plt.show()