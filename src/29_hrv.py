import pandas as pd
import numpy as np

from scipy.signal import butter
from scipy.signal import filtfilt
from scipy.signal import find_peaks

data = pd.read_csv("heartbeat_dataset.csv")

time = data["time"].values
signal = data["ir"].values

signal = signal[100:]
time = time[100:]

fs = 50

b, a = butter(
    3,
    [0.8/(fs/2), 3/(fs/2)],
    btype="band"
)

filtered = filtfilt(b, a, signal)

peaks, _ = find_peaks(
    filtered,
    distance=25,
    prominence=300
)

peak_times = time[peaks]

rr = np.diff(peak_times)

bpm = 60 / np.mean(rr)

sdnn = np.std(rr) * 1000

rmssd = np.sqrt(
    np.mean(
        np.diff(rr) ** 2
    )
) * 1000

print()

print("========== RESULTS ==========")

print(f"BPM   : {bpm:.2f}")

print(f"SDNN  : {sdnn:.2f} ms")

print(f"RMSSD : {rmssd:.2f} ms")