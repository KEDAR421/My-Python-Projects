import numpy as np
import matplotlib.pyplot as plt
t=np.arange(-2,3,1)
y=np.array([1,2,0,3,4])
plt.figure(figsize=(12,10))
plt.subplot(1,5,1)
plt.stem(t,y)
plt.title('discrete signal X1-->')
plt.xlabel('[n]-->')
plt.ylabel('amplitude-->')

plt.subplot(1,5,2)
t2=np.arange(-1,5,1)
y2=np.array([2,0,3,4,5,6])
plt.stem(t2,y2)
plt.title('discrete signal X2-->')
plt.xlabel('[n]-->')
plt.ylabel('amplitude-->')

min_time=min(t[0],t2[0])

max_time=max(t[-1],t2[-1])

new_time=np.arange(min_time,max_time+1,1)#max_time added for range upto 4
y_new=np.zeros_like(new_time,dtype=float)
y2_new=np.zeros_like(new_time,dtype=float)

y_new[(t-min_time)]=y
y2_new[(t2-min_time)]=y2
print(y_new)
print(y2_new)

addition_result=y_new+y2_new
plt.subplot(1,5,3)
plt.stem(new_time,addition_result)
plt.title('addition (X1+X2)-->')
plt.xlabel('[n]-->')
plt.ylabel('amplitude-->')

difference=y_new-y2_new
plt.subplot(1,5,4)
plt.stem(new_time,difference)
plt.title('subtraction (X1-X2)-->')
plt.xlabel('[n]-->')
plt.ylabel('amplitude-->')
plt.subplot(1,5,5)
multiplication=y_new*y2_new
# print(multiplication)
plt.stem(new_time,multiplication)
plt.title('multiplication (X1*X2)-->')
plt.xlabel('[n]-->')
plt.ylabel('amplitude-->')
plt.show()


 #signal_operation(x1=np.array([2,7,4,5]),x2=np.array([4,6,8]),t1=np.arange(-1,4,1),t2=np.arange(-1,2,1))