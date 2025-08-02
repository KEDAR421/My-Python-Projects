import numpy as np
import matplotlib.pyplot as plt
x=[4,1,3,5,0,3]
n=np.arange(-1,5,1)
x_fold=list(reversed(x))
n_fold=np.flip(n*-1)
print(x)
print(x_fold)
print(n)
print(n_fold)
def folding(signal,time):
    signal_fold=list(reversed(signal))
    time_fold=np.flip(time*-1)
    return signal_fold,time_fold
signall,timee=folding(x,n)
plt.subplot(2,1,1)
plt.stem(n,x)
plt.subplot(2,1,2)
plt.stem(timee,signall)
plt.show()
