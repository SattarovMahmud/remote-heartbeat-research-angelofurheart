import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Sampling frequency
fs = 50

# Create figure
fig, ax = plt.subplots(figsize=(10, 4))

x_data = []
y_data = []

line, = ax.plot([], [])

ax.set_xlim(0, 100)
ax.set_ylim(-2, 2)

ax.set_title("Live Heartbeat Sensor Simulation")
ax.set_xlabel("Samples")
ax.set_ylabel("Amplitude")

sample_counter = 0


def update(frame):
    global sample_counter

    heartbeat = 0.5 * np.sin(
        2 * np.pi * 1.2 * sample_counter / fs
    )
    ax.set_xlim(
        max(0, sample_counter - 500),
        sample_counter + 1
    )

    breathing = 1.0 * np.sin(
        2 * np.pi * 0.25 * sample_counter / fs
    )

    noise = np.random.normal(0, 0.2)

    signal = heartbeat + breathing + noise

    x_data.append(sample_counter)
    y_data.append(signal)

    if len(x_data) > 500:
        x_data.pop(0)
        y_data.pop(0)

    line.set_data(x_data, y_data)
    if len(x_data) > 0:
        ax.set_xlim(x_data[0], x_data[-1] + 1)

    sample_counter += 1

    return line,


ani = FuncAnimation(
    fig,
    update,
    interval=20,
    blit=True
)

plt.show()