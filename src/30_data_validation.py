import pandas as pd
import numpy as np

from processing.signal_processing import process_signal

data = pd.read_csv("heartbeat_dataset.csv")

signal = data["ir"].values

(
    filtered,
    peaks,
    bpm,
    finger,
    quality,
    rr,
    sdnn,
    rmssd
) = process_signal(signal)

print("\n========== VALIDATION ==========\n")

errors = []

if not finger:
    errors.append("Finger not detected")

if quality < 0.4:
    errors.append("Poor signal quality")

if bpm is None:
    errors.append("Unable to calculate BPM")

elif bpm < 40 or bpm > 180:
    errors.append(f"Unrealistic BPM: {bpm:.1f}")

if sdnn is not None:

    if sdnn < 10 or sdnn > 250:
        errors.append(f"Unrealistic SDNN: {sdnn:.1f} ms")

if rmssd is not None:

    if rmssd < 5 or rmssd > 300:
        errors.append(f"Unrealistic RMSSD: {rmssd:.1f} ms")

if len(errors) == 0:

    print("Measurement Accepted\n")

    print(f"BPM      : {bpm:.2f}")
    print(f"Quality  : {quality*100:.1f}%")
    print(f"SDNN     : {sdnn:.2f} ms")
    print(f"RMSSD    : {rmssd:.2f} ms")

else:

    print("Measurement Rejected\n")

    for error in errors:
        print("-", error)