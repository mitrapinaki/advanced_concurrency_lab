# 02_race_conditions.py

import threading

from common.timing import timed

COUNTER = 0
N_INCREMENTS = 100_000
N_THREADS = 4


def unsafe_increment():
    global COUNTER
    for _ in range(N_INCREMENTS):
        # Not atomic: read-modify-write
        COUNTER += 1


if __name__ == "__main__":
    with timed("Race condition demo"):
        threads = [threading.Thread(target=unsafe_increment) for _ in range(N_THREADS)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

    expected = N_INCREMENTS * N_THREADS
    print(f"Expected: {expected}, actual: {COUNTER}")
    print("Run multiple times to see non-deterministic results.")
