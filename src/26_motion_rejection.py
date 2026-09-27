import serial
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks

ser = serial.Serial("COM5", 115200)

fs = 50

plt.ion()

fig, ax = plt.subplots(figsize=(12,5))

buffer = []

while True:

    try:

        value = int(ser.readline().decode().strip())

        buffer.append(value)

        if len(buffer) > 300:
            buffer.pop(0)

        if len(buffer) < 100:
            continue

        signal = np.array(buffer)

        signal = signal - np.mean(signal)

        b, a = butter(3, [0.8/(fs/2), 3/(fs/2)], btype="band")
        filtered = filtfilt(b, a, signal)

        motion = np.std(np.diff(filtered))

        ax.clear()

        if motion > 120:

            ax.set_title("Motion Detected - Hold Finger Still")

        else:

            peaks, _ = find_peaks(filtered,
                                  distance=fs*0.5,
                                  prominence=40)

            if len(peaks) >= 2:

                intervals = np.diff(peaks) / fs
                bpm = 60 / np.mean(intervals)

                ax.set_title(f"Realtime BPM: {bpm:.1f}")

            ax.plot(filtered)

            ax.scatter(peaks,
                       filtered[peaks],
                       color="red")

        ax.set_xlim(0, len(filtered))

        plt.pause(0.01)

    except:

        pass