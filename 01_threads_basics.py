# 01_threads_basics.py

import threading
import time

from common.workload import io_bound_work


def worker(name: str):
    for i in range(3):
        delay = io_bound_work(0.05, 0.15)
        print(f"[{name}] iteration {i}, slept {delay:.3f}s")


if __name__ == "__main__":
    t1 = threading.Thread(target=worker, args=("T1",))
    t2 = threading.Thread(target=worker, args=("T2",))

    print("Starting threads...")
    t1.start()
    t2.start()

    print("Waiting for threads to finish...")
    t1.join()
    t2.join()
    print("Done.")
