import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Parameters
pi = np.pi
cutoff_freq = pi / 6
filter_lengths = [7, 25, 125]


def ideal_impulse_response(num_taps, cutoff):
    n = np.arange(num_taps) - (num_taps - 1) / 2
    h_d = np.sinc(2 * cutoff * n / pi)
    return h_d


def rectangular_window(num_taps):
    return np.ones(num_taps)
windows = {
    "Rectangular": rectangular_window,

}

for num_taps in filter_lengths:
    h_d = ideal_impulse_response(num_taps, cutoff_freq)

    plt.figure(figsize=(10, 6))
    for window_name, window_func in windows.items():
        window = window_func(num_taps)
        h = h_d * window
        #plt.plot(h, label=f'{window_name} Window')

    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid()
    plt.show()

    plt.figure(figsize=(10, 6))
    for window_name, window_func in windows.items():
        window = window_func(num_taps)
        h = h_d * window
        w, h_response = freqz(h, worN=8000)
        magnitude = 20 * np.log10(abs(h_response))
        phase = np.angle(h_response)

        plt.subplot(2, 1, 1)
        plt.plot(w / pi, magnitude, label=f'{window_name} Window')
        plt.title(f"Frequency Response (Magnitude) for {num_taps}-Tap Filter")
        plt.ylabel("Magnitude (dB)")
        plt.legend()
        plt.grid()

        plt.subplot(2, 1, 2)
        plt.plot(w / pi, phase, label=f'{window_name} Window')
        plt.title(f"Frequency Response (Phase) for {num_taps}-Tap Filter")
        plt.ylabel("Phase (radians)")
        plt.legend()
        plt.grid()

    plt.tight_layout()
    plt.show()