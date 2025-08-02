import numpy as np
import matplotlib.pyplot as plt
def multiplication(signal_1, time1, signal_2, time_2):
    min_time1=min(time1[0], time_2[0])
    max_time1=max(time1[-1], time_2[-1])
    total_time=np.arange(min_time1,max_time1+1,1)
    x1_new1=np.zeros_like(total_time)
    x2_new1=np.zeros_like(total_time)
    x1_new1[(total_time >= time1[0]) & (total_time <= time1[-1])] = signal_1
    x2_new1[(total_time >= time_2[0]) & (total_time <= time_2[-1])] = signal_2
    product=x1_new1*x2_new1 # just change the sign as per requirement
    return total_time,product
x1=[3,2,1,0,1]
n1=np.arange(-2,3,1)
x2=[3,1,2,4]
n2=np.arange(-1,3,1)
time,multiple=multiplication(x1,n1,x2,n2)

plt.figure(figsize=(12,10))
plt.subplot(3,1,1)
plt.title('first signal')
plt.stem(n1,x1)
plt.xlabel('n1-->')
plt.ylabel('amplitude-->')

plt.subplot(3,1,2)
plt.title('second signal')
plt.stem(n2,x2)
plt.xlabel('n2-->')
plt.ylabel('amplitude-->')

plt.subplot(3,1,3)
plt.title('product signal')
plt.stem(time,multiple)
plt.xlabel('n(multiple)-->')
plt.ylabel('amplitude-->')
plt.subplots_adjust(hspace=0.5)
plt.show()