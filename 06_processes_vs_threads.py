# 06_processes_vs_threads.py

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from common.workload import cpu_bound_work
from common.timing import timed


def cpu_task(n: int) -> int:
    return cpu_bound_work(n)


if __name__ == "__main__":
    N_TASKS = 8
    WORK = 200_000_0

    with timed("Threads CPU-bound"):
        with ThreadPoolExecutor(max_workers=4) as executor:
            list(executor.map(cpu_task, [WORK] * N_TASKS))

    with timed("Processes CPU-bound"):
        with ProcessPoolExecutor(max_workers=4) as executor:
            list(executor.map(cpu_task, [WORK] * N_TASKS))


# Sample Results
# Threads CPU-bound: 0.3734s
# Processes CPU-bound: 0.1889s