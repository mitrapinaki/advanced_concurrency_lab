# common/workload.py

import time
import random


def cpu_bound_work(n: int) -> int:
    """Fake CPU-bound work: compute something intensive-ish."""
    total = 0
    for i in range(n):
        total += i * i
    return total


def io_bound_work(min_delay: float = 0.05, max_delay: float = 0.15) -> float:
    """Fake IO-bound work: sleep for a random small duration."""
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)
    return delay
