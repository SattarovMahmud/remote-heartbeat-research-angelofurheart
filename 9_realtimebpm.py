import numpy as np
from scipy.signal import butter, filtfilt
import time

# Sampling frequency
fs = 100
history = []

while True:
    # Simulate 10 seconds of data
    t = np.arange(0, 30, 1 / fs)
    heart_rate = np.random.uniform(1.1, 1.3)
    heartbeat = 0.5 * np.sin(
        2 * np.pi * heart_rate * t
    )
    breathing = 1.0 * np.sin(2 * np.pi * 0.25 * t)
    noise = np.random.normal(0, 2.0, len(t))
    movement = 2.0 * np.sin(2 * np.pi * 0.05 * t)

    signal = heartbeat + breathing + noise + movement

    # Heartbeat band-pass filter
    b, a = butter(
        4,
        [0.8 / (fs / 2), 2.5 / (fs / 2)],
        btype="band"
    )

    filtered = filtfilt(b, a, signal)

    # FFT
    fft = np.fft.fft(filtered)
    freqs = np.fft.fftfreq(len(filtered), 1 / fs)

    positive = freqs > 0

    freqs = freqs[positive]
    fft = np.abs(fft[positive])

    peak_index = np.argmax(fft)
    peak_frequency = freqs[peak_index]

    bpm = peak_frequency * 60

    history.append(bpm)

    if len(history) > 5:
        history.pop(0)

    average_bpm = np.mean(history)

    print(
        f"Current BPM: {bpm:.1f} | "
        f"Stable BPM: {average_bpm:.1f}"
    )

    time.sleep(1)