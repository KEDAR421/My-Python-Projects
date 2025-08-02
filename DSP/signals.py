import numpy as np
import matplotlib.pyplot as plt
A=2
f=10
phi=0
SR=100
time=np.arange(0,5,1/SR)
y=A*np.sin(2*np.pi*f*time+phi)
plt.figure(figsize=(10,4))
plt.plot(time,y)
plt.title("sine wave")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()

