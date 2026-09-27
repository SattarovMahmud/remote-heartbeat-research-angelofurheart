import serial
import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import butter, filtfilt, find_peaks

PORT = "COM5"

ser = serial.Serial(PORT, 115200)

fs = 50

buffer = []

FINGER_THRESHOLD = 30000

plt.ion()

fig, ax = plt.subplots(figsize=(12,5))

while True:

    try:

        value = int(ser.readline().decode().strip())

        if value < FINGER_THRESHOLD:

            buffer.clear()

            ax.clear()

            ax.set_title("No Finger Detected")

            plt.pause(0.01)

            continue

        buffer.append(value)

        BUFFER_SIZE = 120
        MIN_SAMPLES = 80

        if len(buffer) > BUFFER_SIZE:
            buffer.pop(0)

        if len(buffer) < MIN_SAMPLES:
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

        ax.clear()

        ax.plot(filtered)

        ax.scatter(peaks,
                   filtered[peaks],
                   color="red")

        if len(peaks) >= 2:

            intervals = np.diff(peaks) / fs

            bpm = 60 / np.mean(intervals)

            ax.set_title(f"Realtime BPM: {bpm:.1f}")

        ax.set_xlim(0, len(filtered))

        plt.pause(0.01)

    except:

        pass