import numpy as np
import matplotlib.pyplot as plt

def fold_signal(signal, n):
    return signal[::-1], -n[::-1]

def shift_signal(signal, n, shift_amount):
    n_shifted = n + shift_amount
    return n_shifted, signal

def multiply_signals(signal1, n1, signal2, n2):
    n_common = np.arange(min(n1[0], n2[0]), max(n1[-1], n2[-1]) + 1)
    x_common = np.zeros(len(n_common))
    h_common = np.zeros(len(n_common))
    x_common[np.isin(n_common, n1)] = signal1
    h_common[np.isin(n_common, n2)] = signal2
    return n_common, x_common * h_common

def correlation(x, n1, h, n2):
    h_folded, n2_folded = fold_signal(h, n2)
    n_corr = np.arange(n1[0] + n2_folded[0], n1[-1] + n2_folded[-1] + 1)
    y = np.zeros(len(n_corr))
    for i, n0 in enumerate(n_corr):
        h_shifted_n, h_shifted_signal = shift_signal(h_folded, n2_folded, n0)
        _, product = multiply_signals(x, n1, h_shifted_signal, h_shifted_n)
        y[i] = np.sum(product)
    return n_corr, y

x = np.array([1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1])
n = np.arange(0, len(x))

N = 100
D = 20
a = 0.9
variance = 0.01

v = np.random.normal(0, np.sqrt(variance), N)

y = np.zeros(N)
for i in range(N):
    if i >= D and i - D < len(x):
        y[i] = a * x[i - D] + v[i]
    else:
        y[i] = v[i]

n_y = np.arange(0, N)

n_corr_custom, corr_custom = correlation(y, n_y, x, n)

corr_inbuilt = np.correlate(y, x, mode='full')
lags = np.arange(-(len(x) - 1), len(y))


plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.title('Barker Sequence x(n)')
plt.stem(n, x)
plt.grid(True)

plt.subplot(2, 2, 2)
plt.title('Received Signal y(n)')
plt.stem(n_y, y)
plt.grid(True)

plt.subplot(2, 2, 3)
plt.title('Custom Correlation')
plt.stem(lags, corr_inbuilt)
plt.grid(True)

plt.subplot(2, 2, 4)
plt.title('Inbuilt Correlation')
plt.stem(lags, corr_inbuilt)
plt.grid(True)

plt.tight_layout()
plt.show()