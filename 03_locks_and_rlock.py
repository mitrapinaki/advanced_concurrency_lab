# 03_locks_and_rlock.py

import threading

from common.timing import timed

COUNTER = 0
LOCK = threading.Lock()
N_INCREMENTS = 100_000
N_THREADS = 4


def safe_increment():
    global COUNTER
    for _ in range(N_INCREMENTS):
        with LOCK:
            COUNTER += 1


if __name__ == "__main__":
    with timed("Locked increment"):
        threads = [threading.Thread(target=safe_increment) for _ in range(N_THREADS)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

    expected = N_INCREMENTS * N_THREADS
    print(f"Expected: {expected}, actual: {COUNTER}")
