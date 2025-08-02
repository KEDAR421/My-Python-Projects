import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

n = np.arange(-20, 101)

# Coefficients y(n)
a = [1, -1, 0.9]

# Coefficients of x(n)
b = [1]

# Impulse response
impulse = np.zeros(len(n))
impulse[np.where(n == 0)] = 1  # Set the impulse at n=0
h_impulse = lfilter(b, a, impulse)

# Unit step response
unit_step = np.ones(len(n))
h_step = lfilter(b, a, unit_step)

# Plot the impulse response
plt.figure(figsize=(12, 6))
plt.stem(n, h_impulse)
plt.title("Impulse Response h(n)")
plt.xlabel("n")
plt.ylabel("h(n)")
plt.grid(True)
plt.show()

# Plot the unit step response
plt.figure(figsize=(12, 6))
plt.stem(n, h_step, use_line_collection=True)
plt.title("Unit Step Response h(n)")
plt.xlabel("n")
plt.ylabel("h(n)")
plt.grid(True)
plt.show()

# Check for stability: if the system is BIBO stable, the impulse response should be absolutely summable
is_stable = np.sum(np.abs(h_impulse)) < np.inf
print(f"The system is {'stable' if is_stable else 'unstable'} based on the impulse response.")