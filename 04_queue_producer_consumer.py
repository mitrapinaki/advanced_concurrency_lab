# 04_queue_producer_consumer.py

import threading
import queue
import time

from common.workload import io_bound_work

SENTINEL = object()


def producer(q: "queue.Queue[float]", n: int):
    for _ in range(n):
        delay = io_bound_work(0.01, 0.05)
        q.put(delay)
    q.put(SENTINEL)  # signal consumer to stop


def consumer(q: "queue.Queue[float]"):
    while True:
        item = q.get()
        if item is SENTINEL:
            q.task_done()
            break
        print(f"[consumer] got delay={item:.3f}")
        q.task_done()


if __name__ == "__main__":
    q: "queue.Queue[float]" = queue.Queue()

    prod = threading.Thread(target=producer, args=(q, 10))
    cons = threading.Thread(target=consumer, args=(q,))

    prod.start()
    cons.start()

    q.join()
    prod.join()
    cons.join()
    print("All tasks processed.")
