import numpy as np
import matplotlib.pyplot as plt

fs = 100

t = np.arange(0, 10, 1 / fs)

heartbeat = np.sin(2 * np.pi * 1.2 * t)

# Random noise
noise = np.random.normal(0, 0.3, len(t))

signal = heartbeat + noise

plt.figure(figsize=(10, 4))
plt.plot(t, signal)

plt.title("Heartbeat With Noise")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.show()