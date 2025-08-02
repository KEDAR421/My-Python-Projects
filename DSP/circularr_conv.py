import numpy as np


def circular_convolution(x, h):
    # Determine the length of the result
    N = max(len(x), len(h))

    # Pad x and h to length N
    x = np.pad(x, (0, N - len(x)), mode='constant')
    h = np.pad(h, (0, N - len(h)), mode='constant')

    # Compute the circular convolution
    result = np.zeros(N)
    for n in range(N):
        for k in range(N):
            result[n] += x[k] * h[(n - k) % N]

    return result


# Example usage
x = [1, 2, 3, 4]
h = [1, 0, -1, 0]
circular_conv = circular_convolution(x, h)
print("Circular Convolution:", circular_conv)
