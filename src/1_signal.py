import numpy as np
import matplotlib.pyplot as plt

# Sampling frequency (samples per second)
fs = 100

# Generate 10 seconds of time values
t = np.arange(0, 10, 1 / fs)

# Simulated heartbeat signal
# 1.2 Hz ≈ 72 beats per minute
heartbeat = np.sin(2 * np.pi * 1.2 * t)

# Create a figure for plotting
plt.figure(figsize=(10, 4))

# Plot the heartbeat signal
plt.plot(t, heartbeat)

# Add title and axis labels
plt.title("Artificial Heartbeat Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

# Display grid for better readability
plt.grid(True)

# Show the plot
plt.show()