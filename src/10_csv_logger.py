import csv
import time
import random

with open("heartbeat_log.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "timestamp",
        "bpm"
    ])

    for _ in range(20):

        bpm = random.randint(68, 75)

        timestamp = time.time()

        writer.writerow([
            timestamp,
            bpm
        ])

        print(
            f"Saved BPM: {bpm}"
        )

        time.sleep(0.5)

print("Logging completed.")