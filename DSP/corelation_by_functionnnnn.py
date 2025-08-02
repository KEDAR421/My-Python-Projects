import numpy as np
import matplotlib.pyplot as plt

#Barker sequence
x = np.array([+1, +1, +1, +1, +1, -1, -1, +1, +1, -1, +1, -1, +1])

#v(n) signal
mean = 0
var = 0.01
v = np.random.normal(mean, np.sqrt(var), 100)  # Sequence length 100, much larger than x(n)

D = 20  # Delay
a = 0.9

# y(n) signal
y = np.zeros_like(v)
#print(y)
y[D:D+len(x)] = a * x
y=y+v  #final y signal

#correlation between x(n) and y(n)
correlation = np.correlate(y, x, mode='full')

# Plot the results
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.stem(np.arange(len(x)), x)
plt.title('x(n) signal')

plt.subplot(3, 1, 2)
plt.stem(np.arange(len(y)), y)
plt.title('y(n) signal')

plt.subplot(3, 1, 3)
plt.stem(np.arange(-len(x) + 1, len(y)), correlation)
plt.title('Correlation of x(n) and y(n)')
plt.show()