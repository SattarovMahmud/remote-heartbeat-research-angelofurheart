import numpy as np
import matplotlib.pyplot as plt

# Sampling frequency
fs = 100

# Time axis
t = np.arange(0, 10, 1 / fs)

# Simulated heartbeat
heartbeat = np.sin(2 * np.pi * 1.2 * t)

# Noise
noise = np.random.normal(0, 0.5, len(t))

# Combined signal
signal = heartbeat + noise

# Fast Fourier Transform
fft = np.fft.fft(signal)

# Frequency axis
freqs = np.fft.fftfreq(len(signal), 1 / fs)

# Magnitude
magnitude = np.abs(fft)

# Keep only positive frequencies
positive = freqs > 0

plt.figure(figsize=(10, 4))
plt.plot(freqs[positive], magnitude[positive])

plt.title("Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)

plt.show()