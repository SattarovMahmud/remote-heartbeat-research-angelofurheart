# MAX30102 signal parser

class HeartbeatProcessor:
    def __init__(self):
        self.samples = []

    def add_sample(self, value):
        self.samples.append(value)

    def calculate_bpm(self):
        pass