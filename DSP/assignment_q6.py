import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import resample
A=np.array([1,2,3,4,5,6,7,8,9,10])
plt.figure(figsize=(6,3))
plt.stem(A)
#plt.plot(A)
plt.show()
y=A[::2]
print("(a)Down sampled by 2=",y)
plt.stem(y)
plt.show()
#upampling by 2
z=resample(A,len(A)*2)
print("(b)Upsampled by 2 data are=",z)
plt.stem(z)
plt.show()