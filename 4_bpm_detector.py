import numpy as np

# Sampling frequency
fs = 100

# Time axis
t = np.arange(0, 10, 1 / fs)

# Heartbeat signal
heartbeat = np.sin(2 * np.pi * 1.2 * t)

# Random noise
noise = np.random.normal(0, 0.5, len(t))

# Combined signal
signal = heartbeat + noise

# FFT
fft = np.fft.fft(signal)

# Frequencies
freqs = np.fft.fftfreq(len(signal), 1 / fs)

# Magnitude
magnitude = np.abs(fft)

# Positive frequencies only
positive = freqs > 0

freqs = freqs[positive]
magnitude = magnitude[positive]

# Find strongest frequency
peak_index = np.argmax(magnitude)

peak_frequency = freqs[peak_index]

# Convert Hz to BPM
bpm = peak_frequency * 60

print(f"Detected frequency: {peak_frequency:.2f} Hz")
print(f"Detected BPM: {bpm:.1f}")