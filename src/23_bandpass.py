import pandas as pd
import matplotlib.pyplot as plt

from scipy.signal import butter
from scipy.signal import filtfilt

data = pd.read_csv("heartbeat_dataset.csv")

signal = data["ir"]

fs = 50

low = 0.7
high = 3.5

b, a = butter(
    3,
    [low / (fs / 2), high / (fs / 2)],
    btype="band"
)

filtered = filtfilt(b, a, signal)

plt.figure(figsize=(12,5))

plt.plot(signal, alpha=0.4, label="Raw")

plt.plot(filtered, linewidth=2, label="Bandpass")

plt.title("Bandpass Filter")

plt.xlabel("Sample")

plt.ylabel("Amplitude")

plt.grid(True)

plt.legend()

plt.show()