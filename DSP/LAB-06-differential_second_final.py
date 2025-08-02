import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter
import scipy.signal as signal
#time for signals
n=np.arange(0,51,1)

x_n=(0.8)**n  #x(n) signal
h_n=(-0.9)**n  #h(n) signal
# convolution by analytically y(n)=[9*(-0.9^n)(1-(-8/9)^n+1)]/17
yn=((9*((-0.9)**n)*(1-(-8/9)**(n+1)))/17)
nn=np.convolve(x_n,h_n) # convolution by inbuiltTIK
conv_by_inbuilt= nn[:51]
# function convolution
def manual_convolution(x, h):
    len_x = len(x)
    len_h = len(h)
    len_y = len_x + len_h - 1  # Length of the convolution result
    y = np.zeros(len_y)

    # Convolution sum
    for n in range(len_y):
        sum_val = 0
        for k in range(len_x):
            if 0 <= n - k < len_h:  # checking for h(n - k) is valid
                sum_val += x[k] * h[n - k]
        y[n] = sum_val

    return y
y_n = manual_convolution(x_n, h_n)
y_n1=yn[:51]

y_n_filter = lfilter(h_n, [1], x_n)
# Plot the results
plt.subplot(2, 1, 1)
plt.stem(n, x_n)
plt.title("x(n) signal")
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(n, h_n)
plt.title("h(n) signal")
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid()
plt.subplots_adjust(hspace=0.5)
plt.show()

# y(n) = x(n) * h(n) Convolution results

plt.subplot(2, 1, 1)
plt.stem(n, yn)
plt.title("Convolution result analytically")
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(n, conv_by_inbuilt)
plt.title("Convolution by inbuilt")
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid()
plt.subplots_adjust(hspace=0.5)
plt.show()

plt.subplot(2, 1, 1)
plt.stem(n, y_n1)
plt.title("Convolution by function)")
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(2,1,2)
plt.stem(n,y_n_filter)
plt.title("Convolution by filter")
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid()
# Adjust subplot spacing and show the plot
plt.subplots_adjust(hspace=0.5)
plt.show()