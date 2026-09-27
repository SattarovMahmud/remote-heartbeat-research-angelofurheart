import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

data = pd.read_csv("heartbeat_dataset.csv")

signal = data["ir"]

filtered = savgol_filter(signal, 31, 3)

plt.figure(figsize=(12, 5))

plt.plot(signal, alpha=0.4, label="Raw")
plt.plot(filtered, linewidth=2, label="Filtered")

plt.title("Signal Filtering")
plt.xlabel("Sample")
plt.ylabel("IR")
plt.legend()
plt.grid(True)

plt.show()