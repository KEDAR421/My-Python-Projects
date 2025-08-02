# # import numpy as np
# # A=np.array([2,3,4,2,9])
# # print(A)
# #comment command / for select and command all  '''multi line comment out'''
# print('i am kedar\ni am \"good\" a student')
# print('kedar',18,sep="-")


import numpy as np
import matplotlib.pyplot as plt

# Define the length and signals x(n) and h(n)
n = np.arange(0, 51, 1)
x_n = (0.8)**n  # x(n) = (0.8)^n for n >= 0
h_n = (-0.9)**n  # h(n) = (-0.9)^n for n >= 0

# Perform manual convolution
def manual_convolution(x, h):
    len_x = len(x)
    len_h = len(h)
    len_y = len_x + len_h - 1  # Length of the convolution result
    y = np.zeros(len_y)

    # Convolution sum
    for n in range(len_y):
        sum_val = 0
        for k in range(len_x):
            if 0 <= n - k < len_h:  # Ensure index for h(n - k) is valid
                sum_val += x[k] * h[n - k]
        y[n] = sum_val

    return y

# Get the convolution result
y_n = manual_convolution(x_n, h_n)

# Define the time axis for the convolution result
n_conv = np.arange(0, len(y_n), 1)

# Plot the results
plt.figure(figsize=(12, 10))

# Plot x(n)
plt.subplot(3, 1, 1)
plt.stem(n, x_n)
plt.title("x(n) signal")
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid()

# Plot h(n)
plt.subplot(3, 1, 2)
plt.stem(n, h_n)
plt.title("h(n) signal")
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid()

# Plot y(n) = x(n) * h(n) (Convolution result)
plt.subplot(3, 1, 3)
plt.stem(n_conv, y_n)
plt.title("Convolution result y(n) = x(n) * h(n) (Manual Calculation)")
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid()

# Adjust subplot spacing and show the plot
plt.subplots_adjust(hspace=0.5)
plt.show()
