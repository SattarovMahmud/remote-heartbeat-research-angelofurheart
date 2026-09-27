import serial
import numpy as np
import matplotlib.pyplot as plt
from processing.signal_processing import process_signal

ser = serial.Serial("COM5", 115200)

fs = 50


buffer = []

plt.ion()

fig, ax = plt.subplots(figsize=(12,5))

line, = ax.plot([], [])
points, = ax.plot([], [], "ro")

ax.set_title("Realtime Heartbeat")
ax.set_xlabel("Samples")
ax.set_ylabel("Amplitude")

while True:

    try:

        value = int(ser.readline().decode().strip())

        buffer.append(value)

        if len(buffer) > 300:
            buffer.pop(0)

        if len(buffer) < 150:
            continue

        signal = np.array(buffer)

        filtered, peaks, bpm, finger, quality, rr, sdnn, rmssd = process_signal(signal)

        line.set_data(range(len(filtered)), filtered)

        points.set_data(peaks, filtered[peaks])

        ax.set_xlim(0, len(filtered))

        ax.set_ylim(filtered.min()-200, filtered.max()+200)

        if not finger:
            ax.set_title("Finger not detected")

        elif quality < 0.4:
            ax.set_title("Poor signal quality")

        if not finger:

            ax.set_title(

                "Finger not detected"

            )


        elif bpm is None:

            ax.set_title(

                f"Finger detected | Quality: {quality * 100:.0f}%"

            )


        else:

            ax.set_title(

                f"BPM: {bpm:.1f} | "

                f"Quality: {quality * 100:.0f}% | "

                f"SDNN: {sdnn:.1f} ms | "

                f"RMSSD: {rmssd:.1f} ms"

            )

        plt.draw()

        plt.pause(0.01)


    except Exception as e:

        print(e)