import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import butter
from scipy.signal import filtfilt
from scipy.signal import find_peaks

data = pd.read_csv("heartbeat_dataset.csv")

time = data["time"].values
signal = data["ir"].values

signal = signal[100:]
time = time[100:]

fs = 50

low = 0.7
high = 3.5

b, a = butter(
    3,
    [low / (fs / 2), high / (fs / 2)],
    btype="band"
)

filtered = filtfilt(b, a, signal)

peaks, _ = find_peaks(
    filtered,
    distance=25,
    prominence=300
)

peak_times = time[peaks]

intervals = np.diff(peak_times)

bpm = 60 / intervals

average_bpm = np.mean(bpm)

print("Detected peaks:", len(peaks))
print("Average BPM:", round(average_bpm, 2))

plt.figure(figsize=(12,5))

plt.plot(filtered)

plt.scatter(
    peaks,
    filtered[peaks],
    color="red",
    s=35
)

plt.title("Realtime BPM Detection")

plt.xlabel("Sample")

plt.ylabel("Amplitude")

plt.grid(True)

plt.show()