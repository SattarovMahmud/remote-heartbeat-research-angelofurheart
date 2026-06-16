import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Sampling frequency
fs = 100

# Time axis
t = np.arange(0, 30, 1 / fs)

# Signals
heartbeat = 0.5 * np.sin(2 * np.pi * 1.2 * t)
breathing = 1.0 * np.sin(2 * np.pi * 0.25 * t)
noise = np.random.normal(0, 0.3, len(t))

signal = heartbeat + breathing + noise

# Band-pass filter
low = 0.8
high = 2.5

b, a = butter(
    N=4,
    Wn=[low / (fs / 2), high / (fs / 2)],
    btype="band"
)

filtered = filtfilt(b, a, signal)

plt.figure(figsize=(12, 5))

plt.plot(t, signal, alpha=0.4, label="Raw Signal")
plt.plot(t, filtered, linewidth=2, label="Heartbeat Extracted")

plt.legend()
plt.grid(True)

plt.title("Heartbeat Extraction")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.show()