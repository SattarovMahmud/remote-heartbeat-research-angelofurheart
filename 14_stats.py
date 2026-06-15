import pandas as pd
import numpy as np

# Load recorded signal
data = pd.read_csv("recorded_signal.csv")

signal = data["signal"]

print()
print("Signal Statistics")
print("------------------")

print(f"Samples: {len(signal)}")
print(f"Mean: {np.mean(signal):.3f}")
print(f"Max: {np.max(signal):.3f}")
print(f"Min: {np.min(signal):.3f}")
print(f"Std: {np.std(signal):.3f}")