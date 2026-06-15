import numpy as np
import matplotlib.pyplot as plt

# Sampling frequency
fs = 100

# Time axis
t = np.arange(0, 30, 1 / fs)

# Heartbeat (~72 BPM)
heartbeat = 0.5 * np.sin(2 * np.pi * 1.2 * t)

# Breathing (~15 breaths per minute)
breathing = 1.0 * np.sin(2 * np.pi * 0.25 * t)

# Random noise
noise = np.random.normal(0, 0.3, len(t))

# Combined signal
signal = heartbeat + breathing + noise

plt.figure(figsize=(12, 5))
plt.plot(t, signal)

plt.title("Simulated Human Vital Signs")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.show()