# ESP32 Serial Receiver Prototype

class ESP32Receiver:

    def connect(self):
        print("Connecting to ESP32...")

    def read_line(self):
        return "72"

if __name__ == "__main__":
    esp = ESP32Receiver()
    esp.connect()

    bpm = esp.read_line()
    print("Received:", bpm)