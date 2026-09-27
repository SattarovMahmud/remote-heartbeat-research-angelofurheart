import serial
import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import butter, filtfilt, find_peaks

PORT = "COM5"

ser = serial.Serial(PORT, 115200)

fs = 50

buffer = []

plt.ion()

fig, ax = plt.subplots(figsize=(12,5))

while True:

    try:

        value = int(ser.readline().decode().strip())

        buffer.append(value)

        if len(buffer) > 300:
            buffer.pop(0)

        if len(buffer) < 150:
            continue

        signal = np.array(buffer)

        signal = signal - np.mean(signal)

        b, a = butter(3, [0.8/(fs/2), 3/(fs/2)], btype="band")

        filtered = filtfilt(b, a, signal)

        peaks, _ = find_peaks(
            filtered,
            distance=fs*0.5,
            prominence=40
        )

        quality = min(100, np.std(filtered) / 2)

        ax.clear()

        ax.plot(filtered)

        ax.scatter(peaks,
                   filtered[peaks],
                   color="red")

        if len(peaks) >= 2:

            intervals = np.diff(peaks) / fs

            bpm = 60 / np.mean(intervals)

            ax.set_title(
                f"BPM: {bpm:.1f}   |   Signal Quality: {quality:.0f}%"
            )

        ax.set_xlim(0, len(filtered))

        plt.pause(0.01)

    except:

        pass