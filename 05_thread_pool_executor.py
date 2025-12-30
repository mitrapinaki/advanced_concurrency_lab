# 05_thread_pool_executor.py

from concurrent.futures import ThreadPoolExecutor, as_completed

from common.timing import timed
from common.workload import io_bound_work


def task(i: int) -> float:
    delay = io_bound_work(0.05, 0.15)
    return delay


if __name__ == "__main__":
    N_TASKS = 20
    MAX_WORKERS = 5

    with timed("ThreadPoolExecutor IO-bound"):
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = [executor.submit(task, i) for i in range(N_TASKS)]
            for fut in as_completed(futures):
                delay = fut.result()
                print(f"Completed task with delay={delay:.3f}")
