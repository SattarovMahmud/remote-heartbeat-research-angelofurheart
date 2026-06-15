import numpy as np
from scipy.signal import butter, filtfilt

# Sampling frequency
fs = 100

# Time axis
t = np.arange(0, 30, 1 / fs)

# Simulated signals
heartbeat = 0.5 * np.sin(2 * np.pi * 1.2 * t)
breathing = 1.0 * np.sin(2 * np.pi * 0.25 * t)
noise = np.random.normal(0, 0.3, len(t))

signal = heartbeat + breathing + noise

# Heartbeat filter
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

# Find strongest frequency
peak_index = np.argmax(fft)

peak_frequency = freqs[peak_index]

bpm = peak_frequency * 60

print(f"Detected Frequency: {peak_frequency:.2f} Hz")
print(f"Detected BPM: {bpm:.1f}")