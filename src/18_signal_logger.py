import serial
import csv
import time

ser = serial.Serial("COM5", 115200)

filename = "heartbeat_dataset.csv"

with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time", "ir"])

    start = time.time()

    print("Recording...")

    while True:
        try:
            value = int(ser.readline().decode().strip())

            t = time.time() - start

            writer.writerow([t, value])

            print(round(t,2), value)

        except KeyboardInterrupt:
            break

        except:
            pass

print("Saved:", filename)