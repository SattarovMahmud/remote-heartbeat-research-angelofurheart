import numpy as np
import pandas as pd
import time

signal_data = []

print("Recording signal...")

for i in range(100):

    heartbeat = np.sin(2 * np.pi * 1.2 * i / 10)

    noise = np.random.normal(0, 0.3)

    sample = heartbeat + noise

    signal_data.append(sample)

    print(f"Sample {i}: {sample:.3f}")

    time.sleep(0.05)

df = pd.DataFrame({
    "signal": signal_data
})

df.to_csv(
    "recorded_signal.csv",
    index=False
)

print("Signal saved to recorded_signal.csv")