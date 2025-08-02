import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,1,0.01)
yt=np.sin(2*np.pi*3*t)
plt.figure(figsize=(6,3))
plt.plot(t,yt)
plt.title("(a)sine wave-->")
plt.xlabel("time(t)-->")
plt.ylabel("amplitude(A)-->")
plt.show()

#for cos wave
yt1=np.cos(2*np.pi*5*t)
plt.figure(figsize=(6,3))
plt.plot(t,yt1)
plt.title("(b)cos wave-->")
plt.xlabel("time(t)-->")
plt.ylabel("amplitude(A)-->")
plt.show()
# unit step signal
t2=np.arange(-5,5,0.001)
yt2=np.heaviside(t2,1)
plt.figure(figsize=(6,3))
plt.plot(t2,yt2)
plt.title("(c)unit step signal-->")
plt.xlabel("time(t)-->")
plt.ylabel("amplitude(A)-->")
plt.show()

#impulse signal time is t2
def unit_impulse(t3):
    return np.where(t3==0,1,0)

t3=np.arange(-5,5,0.001)
y=unit_impulse(t3)
plt.figure(figsize=(6,3))
plt.plot(t3,y)
plt.stem([0],[1])
plt.title("(d)impulse signal-->")
plt.xlabel("time(t)-->")
plt.ylabel("amplitude(A)-->")
plt.show()
#ramp signal
def ramp(t4):
    return np.where(t4>=0,t4,0)
t4=np.arange(-2,5,1)
yy=ramp(t4)
plt.figure(figsize=(6,3))
plt.plot(t4,yy)
plt.title("(e)ramp signal-->")
plt.xlabel("time(t)-->")
plt.ylabel("amplitude(A)-->")
plt.show()

