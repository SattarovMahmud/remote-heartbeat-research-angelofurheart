import serial
import time

PORT = "COM5"
BAUD = 2000000

print(f"Connecting to {PORT}...")

try:
    ser = serial.Serial(PORT, BAUD, timeout=1)
    print("Connected!\n")

    while True:
        data = ser.read(1)

        if data:
            print(len(data), data.hex())

except KeyboardInterrupt:
    print("\nStopped.")

except Exception as e:
    print("Error:", e)

finally:
    try:
        ser.close()
    except:
        pass