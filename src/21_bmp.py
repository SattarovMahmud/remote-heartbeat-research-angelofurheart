import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter, find_peaks
import numpy as np

data = pd.read_csv("heartbeat_dataset.csv")

signal = data["ir"]

signal = signal.iloc[100:]

filtered = savgol_filter(signal, 31, 3)

peaks, _ = find_peaks(
    filtered,
    distance=30,
    prominence=300
)

sampling_rate = 50

peak_times = peaks / sampling_rate

intervals = np.diff(peak_times)

bpm = 60 / intervals

average_bpm = np.mean(bpm)

print("Detected peaks:", len(peaks))
print("Average BPM:", round(average_bpm, 2))

plt.figure(figsize=(12,5))

plt.plot(filtered, label="Filtered Signal")
plt.scatter(peaks, filtered[peaks], color="red")

plt.title("Heartbeat Peak Detection")
plt.xlabel("Sample")
plt.ylabel("IR")
plt.grid(True)
plt.legend()

plt.show()