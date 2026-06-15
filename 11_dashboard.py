import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

history = []

fig, ax = plt.subplots()

def update(frame):

    bpm = np.random.randint(68, 76)

    history.append(bpm)

    if len(history) > 50:
        history.pop(0)

    ax.clear()

    ax.plot(history)

    ax.set_title(f"Live BPM Monitor | Current BPM: {bpm}")

    ax.set_ylabel("BPM")

    ax.set_xlabel("Samples")

    ax.grid(True)

ani = FuncAnimation(
    fig,
    update,
    interval=500,
    cache_frame_data=False
)

plt.show()