import numpy as np
import matplotlib.pyplot as plt

# Barker sequence
xn = np.array([1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1])
xn_time=np.arange(0,13,1)
barker_length = len(xn)

sequence_length = 100
time_for_y=np.arange(0,100,1)
D = 20
a = 0.9
variance = 0.01

v = np.random.normal(0, np.sqrt(variance), sequence_length)
# Generate the y(n)
y = np.zeros(len(time_for_y))#sequence_length)
start_index = D
end_index = start_index +len(xn_time)

# Ensure the Barker sequence fits within the signal length
if end_index <= sequence_length:
    y[start_index:end_index] = a * xn
y =y+v  # Add noise
correlation = np.correlate(y, xn, mode='full')


def convolve_signals(signal1, signal2):
    signal2_new = np.flip(signal2)
    len1 = len(signal1)
    len2 = len(signal2)

    # The length of the convolution result
    conv_len = len1 + len2 - 1

    # Initialize the convolution result with zeros
    result = [0] * conv_len
    print(result)

    # Compute the convolution
    for i in range(len1):
        for j in range(len2):
            result[i + j] += signal1[i] * signal2[j]

    return result
result=convolve_signals(xn,y)

# Plot the results
plt.figure(figsize=(14, 7))

plt.subplot(4, 1, 1)
plt.title('Barker Sequence')
plt.stem(xn_time,xn )
plt.grid(True)

plt.subplot(4, 1, 2)
plt.title('Received Signal y(n)')
plt.stem(time_for_y,y, label='Received Signal')
plt.grid(True)
plt.legend()

plt.subplot(4, 1, 3)
plt.title('Cross-Correlation')
plt.stem(correlation)
plt.grid(True)
plt.subplot(4,1,4)
plt.title('function corelation')
plt.stem(result)
plt.grid()
plt.show()

