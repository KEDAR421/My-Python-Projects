import numpy as np
import matplotlib.pyplot as plt
x1=[1,2,1,3,2] #x(n) signal
n1=np.arange(-2,3,1)
hn=[1,2,1] #h(n) signal
n2=np.arange(-1,2,1)
print(n1)
print(max(n1))
time_started_for_conv=min(n1)+min(n2)#-2
time_end_for_conv=max(n1)+max(n2)#3

total_right_shift=max(n1)+max(n2)#right shift time for the signal h(n-k) for starting the convolution
print(total_right_shift)
#folding: h(n)=h(-n)
def folding(signal,time):
    signal_fold=list(reversed(signal))
    time_fold=np.flip(time*-1)
    return signal_fold,time_fold
folded_hn,folded_n2=folding(hn,n2)

#shifting:for h(-k)=h(k-n)
def shifting_function(signal,time,shift_amount):
    n_new=np.zeros_like(time)
    if (shift_amount >= 0):
        n_new = np.arange(min(time) - shift_amount, max(time) + 1 - shift_amount, 1)
    else:
        n_new = np.arange(min(time) - shift_amount, max(time) + 1 - shift_amount, 1)
    return signal,n_new

#right shift the signal[h(n-k)]
first_shift_signal,first_time_shift=shifting_function(folded_hn,folded_n2,-total_right_shift)

 #multiplication
def multiplication(signal1, time1, signal2, time2):
    min_time1 = min(time1[0], time2[0])
    max_time1 = max(time1[-1], time2[-1])
    n_time = np.arange(min_time1, max_time1 + 1, 1)
    x1_new1 = np.zeros_like(n_time)
    x2_new1 = np.zeros_like(n_time)
    x1_new1[(n_time >= time1[0]) & (n_time <= time1[-1])] = signal1
    x2_new1[(n_time >= time2[0]) & (n_time <= time2[-1])] = signal2
    product = x1_new1 * x2_new1  # just change the sign as per requirement
    return n_time, x1_new1, x2_new1, product

length_of_convolution=len(n1)+len(n2)-1
time_for_convold_signal=np.arange(time_started_for_conv,time_end_for_conv+1,1) #time for convolution
#initialize the convolution signal
convoluted_signal=[]
for i in range(length_of_convolution):
    shifted_signal,shifted_time=shifting_function(first_shift_signal,first_time_shift,i)#shifting left side continuously..
    total_time,first_signal,second_signal,product=multiplication(x1,n1,shifted_signal,shifted_time)
    #print(product)
    sum=0
    for i in range(len(product)):
         sum=sum+product[i]
    #print(sum)
    convoluted_signal.append(sum)#the convoluted signal is in reverse order so reversed it.
print(convoluted_signal)
convoluted_signal.reverse()
print(convoluted_signal)

#to plot the signals
plt.figure(figsize=(12,10))
plt.subplot(3,1,1)
plt.stem(n1,x1)
plt.title("x(n) signal-->")
plt.xlabel('n1-->')
plt.ylabel('amplitude-->')
plt.grid()
plt.subplot(3,1,2)
plt.stem(n2,hn)
plt.title("h(n) signal-->")
plt.xlabel('n2-->')
plt.ylabel('amplitude-->')
plt.grid()
plt.subplot(3,1,3)
plt.stem(time_for_convold_signal,convoluted_signal)
plt.title("convoluted signal-->")
plt.xlabel('n-->')
plt.ylabel('amplitude-->')
plt.subplots_adjust(hspace=0.5)#to keep the space between two subplote
plt.grid()
plt.show()

