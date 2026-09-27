import serial
import numpy as np
import matplotlib.pyplot as plt

from processing.signal_processing import process_signal

ser = serial.Serial("COM5", 115200)

buffer = []

plt.ion()

fig = plt.figure(figsize=(13, 7))

ax = fig.add_subplot(111)

line, = ax.plot([], [], lw=2)
points, = ax.plot([], [], "ro")

info = ax.text(
    0.02,
    0.98,
    "",
    transform=ax.transAxes,
    fontsize=12,
    verticalalignment="top",
    bbox=dict(facecolor="white", alpha=0.8)
)

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

        ax.set_ylim(
            filtered.min() - 200,
            filtered.max() + 200
        )

        if not finger:

            status = "NO FINGER"

        elif quality < 0.5:

            status = "LOW QUALITY"

        else:

            status = "GOOD"

        text = ""

        text += f"Status : {status}\n"

        text += f"Quality : {quality*100:.1f}%\n\n"

        if bpm is not None:
            text += f"BPM : {bpm:.1f}\n"
        else:
            text += "BPM : --\n"

        if sdnn is not None:
            text += f"SDNN : {sdnn:.1f} ms\n"
        else:
            text += "SDNN : --\n"

        if rmssd is not None:
            text += f"RMSSD : {rmssd:.1f} ms\n"
        else:
            text += "RMSSD : --\n"

        text += f"\nPeaks : {len(peaks)}"

        info.set_text(text)

        plt.pause(0.01)

    except Exception:
        pass