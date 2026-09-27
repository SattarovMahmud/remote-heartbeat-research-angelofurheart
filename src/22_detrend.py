import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

data = pd.read_csv("heartbeat_dataset.csv")

signal = data["ir"].iloc[100:]

trend = savgol_filter(signal, 401, 3)

heartbeat = signal - trend

plt.figure(figsize=(12,5))

plt.plot(heartbeat)

plt.title("Heartbeat Signal")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.grid(True)

plt.show()