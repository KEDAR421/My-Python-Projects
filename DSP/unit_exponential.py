import numpy as np
import matplotlib.pyplot as plt
def unit_expon(t):
    return np.exp(t)
t=np.arange(-5,5,0.01)
y=unit_expon(t)
plt.plot(t,y)
plt.title('unit exponential signal(continous)')
plt.show()

t1=np.arange(-7,7,1)
y1=unit_expon(t1)
plt.stem(t1,y1)
plt.title('unit exponential signal(discrete):-')
plt.show()