import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the symbol and function
t = sp.symbols('t')
T = 2 * sp.pi  # Period of the square wave (2π)
f = sp.Piecewise((1, t < sp.pi), (-1, t >= sp.pi))  # Square wave function


# Fourier series coefficients
def fourier_series_coeff(f, T, N):
    a0 = (2 / T) * sp.integrate(f, (t, 0, T))
    a_n = [(2 / T) * sp.integrate(f * sp.cos(2 * sp.pi * n * t / T), (t, 0, T)) for n in range(1, N + 1)]
    b_n = [(2 / T) * sp.integrate(f * sp.sin(2 * sp.pi * n * t / T), (t, 0, T)) for n in range(1, N + 1)]

    return a0, a_n, b_n


# Reconstruct the Fourier series
def fourier_series(f, T, N):
    a0, a_n, b_n = fourier_series_coeff(f, T, N)

    series = a0 / 2
    for n in range(1, N + 1):
        series += a_n[n - 1] * sp.cos(2 * sp.pi * n * t / T) + b_n[n - 1] * sp.sin(2 * sp.pi * n * t / T)

    return series


# Parameters
N = 10  # Number of terms in the Fourier series

# Get the Fourier series
f_series = fourier_series(f, T, N)

# Print the Fourier series
print("Fourier series up to N terms:")
sp.pprint(f_series)

# Plot the original function and the Fourier series approximation
t_vals = np.linspace(0, 2 * np.pi, 400)
f_approx = sp.lambdify(t, f_series, 'numpy')

plt.plot(t_vals, np.sign(np.sin(t_vals)), label='Original Square Wave')
plt.plot(t_vals, f_approx(t_vals), label=f'Fourier Series Approximation (N={N})', linestyle='--')

plt.xlabel('t')
plt.ylabel('f(t)')
plt.legend()
plt.grid(True)
plt.title('Fourier Series Approximation of Square Wave')
plt.show()
