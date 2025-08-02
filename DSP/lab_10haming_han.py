import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, windows

def ideal_impulse_response(N, wc):
    h = np.zeros(N)
    M = (N - 1) / 2
    for n in range(N):
        if n == M:
            h[n] = wc / np.pi
        else:
            h[n] = np.sin(wc * (n - M)) / (np.pi * (n - M))
    return h


def apply_window(h, window_type):
    if window_type == 'hamming':
        window = windows.hamming(len(h))
    elif window_type == 'hann':
        window = windows.hann(len(h))
    else:
        raise ValueError("Unsupported window type")
    return h * window


def plot_response(h, fs=2 * np.pi, title=""):
    w, H = freqz(h, worN=8000)
    plt.figure(figsize=(12, 6))

    # Magnitude Response
    plt.subplot(2, 1, 1)
    plt.plot(w, 20 * np.log10(abs(H)), 'b')
    plt.title("Magnitude Response - " + title)
    plt.xlabel("Frequency (rad/sample)")
    plt.ylabel("Magnitude (dB)")
    plt.grid()

    # Phase Response
    plt.subplot(2, 1, 2)
    plt.plot(w, np.angle(H), 'r')
    plt.title("Phase Response - " + title)
    plt.xlabel("Frequency (rad/sample)")
    plt.ylabel("Phase (radians)")
    plt.grid()

    plt.tight_layout()
    plt.show()


# Filter specifications
wc = np.pi / 6  # Cutoff frequency
filter_lengths = [7, 25, 125]  # Number of taps

# Only Hamming and Hann windows
window_types = ['hamming', 'hann']

for N in filter_lengths:
    for window_type in window_types:
        # Step 1: Ideal impulse response
        h_ideal = ideal_impulse_response(N, wc)

        # Step 2: Apply window
        h_windowed = apply_window(h_ideal, window_type)

        # Step 3: Plot the magnitude and phase response
        title = f"{N}-tap FIR Filter with {window_type.capitalize()} Window"
        plot_response(h_windowed, title=title)
