import pandas as pd
import matplotlib.pyplot as plt

# Load recorded signal
data = pd.read_csv("recorded_signal.csv")

# Plot signal
plt.figure(figsize=(10, 4))

plt.plot(data["signal"])

plt.title("Recorded Heartbeat Signal")

plt.xlabel("Sample")

plt.ylabel("Amplitude")

plt.grid(True)

plt.show()