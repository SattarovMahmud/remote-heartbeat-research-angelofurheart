import serial
import matplotlib.pyplot as plt
from collections import deque

ser = serial.Serial("COM5",115200)

values = deque([0]*30, maxlen=30)

plt.ion()

fig,ax=plt.subplots()

line,=ax.plot(values)



while True:

    try:
        text = ser.readline().decode().strip()
        print(text)
        value = int(text)
        values.append(value)
        minimum = min(values)
        maximum = max(values)

        ax.set_ylim(minimum - 500, maximum + 500)

        line.set_ydata(values)
        line.set_xdata(range(len(values)))

        plt.draw()
        plt.pause(0.001)

    except:
        pass