import numpy as np
from scipy.signal import resample
A=np.array([1,2,3,4,5,6,7,8,9,10])
y=A[::2]
print("(a)Down sampled by 2=",y)
#upampling by 2
z=resample(A,len(A)*2)
print("(b)Upsampled by 2 data are=",z)
#addition of all elements
sum=0
for i in range(len(A)):
    sum=sum+A[i]
print("(c)sum of elements of A=",sum)
#averaraging is
avg=sum/len(A)
print("(d)average of the array elements=",avg)
