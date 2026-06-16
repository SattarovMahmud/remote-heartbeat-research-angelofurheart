# MAX30102 Receiver Module
# Project: Remote Heartbeat Research Angelofurheart

class MAX30102Receiver:

    def __init__(self):
        self.samples = []

    def connect(self):
        print("Waiting for MAX30102 connection...")

    def read_sample(self):
        pass

    def save_sample(self, value):
        self.samples.append(value)


if __name__ == "__main__":
    receiver = MAX30102Receiver()
    receiver.connect()