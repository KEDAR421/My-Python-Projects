import numpy as np
import matplotlib.pyplot as plt
x1=np.array([3,1,2,3,4])
t1=np.arange(-1,4,1)#upto 3
x2=np.array([3,8,4,1,5])
t2=np.arange(-3,2,1)
min_time=min(t1[0],t2[0])
max_time=max(t1[-1],t2[-1])

time_new=np.arange(min_time,max_time+1,1)
print(time_new)
x1_new=np.zeros_like(time_new)#make all elemtnts zero
x2_new=np.zeros_like(time_new)
x1_new[(time_new >= t1[0]) & (time_new<=t1[-1])]=x1
print(x1_new)
x2_new[(time_new>=t2[0])&(time_new<=t2[-1])]=x2
print(x2_new)
sum=x1_new+x2_new
print(sum)
plt.subplot(3,1,1)
plt.title('x1')
plt.stem(t1,x1)
plt.subplot(3,1,2)
plt.title('x2')
plt.stem(t2,x2)
plt.subplot(3,1,3)
plt.title('sum')
plt.stem(time_new,sum)
plt.show()

def addition(x1,n1,x2,n2):
    min_time1=min(n1[0],n2[0])
    max_time1=max(n1[-1],n2[-1])
    n_time=np.arange(min_time1,max_time1+1,1)
    x1_new1=np.zeros_like(n_time)
    x2_new1=np.zeros_like(n_time)
    x1_new1[(n_time>= n1[0]) & (n_time <= n1[-1])] = x1
    x2_new1[(n_time >= n2[0]) & (n_time <= n2[-1])] = x2
    added=x1_new1+x2_new1 # just change the sign as per requirement
    return n_time,added
signal=[1,4,3,2,2,1]
t1=np.arange(-2,4,1)
signal2=[3,1,5,6,2]
t2=np.arange(-1,4,1)
n_time,added=addition(signal,t1,signal2,t2)
print(added)
plt.figure(figsize=(12,10))
plt.subplot(3,1,1)
plt.stem(t1,signal)
plt.title('first signal')
plt.xlabel('n1-->')
plt.ylabel('amp-->')

plt.subplot(3,1,2)
plt.stem(t2,signal2)
plt.title('2nd signal')
plt.xlabel('n2-->')
plt.ylabel('amp-->')

plt.subplot(3,1,3)
plt.stem(n_time,added)
plt.title('added signal')
plt.xlabel('time-->')
plt.ylabel('amp-->')
plt.show()