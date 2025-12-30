# 04_01_queue_producer_multiple_consumer.py

import threading
import queue
import time

from common.workload import io_bound_work

SENTINEL = object()
N_CONSUMERS = 3


def producer(q: "queue.Queue[float]", n: int, n_consumers: int = 1):
    for _ in range(n):
        delay = io_bound_work(0.01, 0.05)
        q.put(delay)
    # put one sentinel per consumer so each can stop
    for _ in range(n_consumers):
        q.put(SENTINEL)  # signal consumers to stop


def consumer(q: "queue.Queue[float]", cid: int):
    while True:
        item = q.get()
        if item is SENTINEL:
            q.task_done()
            break
        print(f"[consumer-{cid}] got delay={item:.3f}")
        q.task_done()


if __name__ == "__main__":
    q: "queue.Queue[float]" = queue.Queue()

    prod = threading.Thread(target=producer, args=(q, 30, N_CONSUMERS))
    consumers = [
        threading.Thread(target=consumer, args=(q, i)) for i in range(N_CONSUMERS)
    ]

    prod.start()
    for c in consumers:
        c.start()

    q.join()
    prod.join()
    for c in consumers:
        c.join()
    print("All tasks processed.")