import numpy as np
import matplotlib.pyplot as plt
#unit step signal continous
t=np.arange(-5,5,0.001)
y=np.zeros_like(t)
y[t>=0]=1
plt.plot(t,y)
plt.title("continous unit step signal")
plt.show()

t1=np.arange(-5,5,1)
y1=np.zeros_like(t1)
y1[(t1>=0)]=1
plt.stem(t1,y1)
plt.title("discrete unit step signal:-")
plt.show()

#by using function
def unitstep(t2):
    return np.heaviside(t2,1)
t2=np.arange(-5,5,0.01)
y2=unitstep(t2)
plt.plot(t2,y2)
plt.title("unit continous step by function:-")
plt.show()
t3=np.arange(-5,5,1)
y3=unitstep(t3)
plt.stem(t3,y3)
plt.title('discrete unit step by function')
plt.show()

#methode 2
def unitstep2(t4):
    return np.where(t4>=0,1,0)
t4=np.arange(-5,5,0.01)
y4=unitstep2(t4)
plt.plot(t4,y4)
plt.title('unti step by another methode:-')
plt.show()