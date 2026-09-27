import numpy as np
from scipy.signal import butter, filtfilt, find_peaks

FS = 50

b, a = butter(
    3,
    [0.8 / (FS / 2), 3.0 / (FS / 2)],
    btype="band"
)


def process_signal(signal):

    signal = signal - np.mean(signal)

    filtered = filtfilt(b, a, signal)

    signal_range = np.max(filtered) - np.min(filtered)

    finger_detected = signal_range > 150

    quality_score = min(signal_range / 800, 1.0)

    peaks, _ = find_peaks(
        filtered,
        distance=FS * 0.5,
        prominence=40
    )

    bpm = None
    rr = None
    sdnn = None
    rmssd = None

    if finger_detected and len(peaks) >= 2:

        rr = np.diff(peaks) / FS

        bpm = 60 / np.mean(rr)

        sdnn = np.std(rr) * 1000

        if len(rr) >= 2:
            rmssd = np.sqrt(np.mean(np.diff(rr) ** 2)) * 1000

    return (
        filtered,
        peaks,
        bpm,
        finger_detected,
        quality_score,
        rr,
        sdnn,
        rmssd
    )