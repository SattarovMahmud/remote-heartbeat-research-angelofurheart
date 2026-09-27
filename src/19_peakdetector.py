import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

data = pd.read_csv("heartbeat_dataset.csv")

print(data.columns)

signal = data.iloc[:, 1]
peaks, _ = find_peaks(
    signal,
    distance=35,
    prominence=500
)

plt.figure(figsize=(12,5))

plt.plot(signal)

plt.plot(
    peaks,
    signal.iloc[peaks],
    "ro",
    markersize=5
)

plt.title("Peak Detection")
plt.xlabel("Sample")
plt.ylabel("IR")

plt.grid(True)

plt.show()