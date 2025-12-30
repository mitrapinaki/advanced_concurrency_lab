# 07_asyncio_basics.py

import asyncio
from common.workload import io_bound_work


async def async_worker(name: str, n: int):
    loop = asyncio.get_running_loop()
    for i in range(n):
        # offload blocking sleep to a thread to simulate IO
        delay = await loop.run_in_executor(None, io_bound_work, 0.05, 0.15)
        print(f"[{name}] iteration {i}, slept {delay:.3f}s")


async def main():
    await asyncio.gather(
        async_worker("A", 3),
        async_worker("B", 3),
    )


if __name__ == "__main__":
    asyncio.run(main())


# RESULT
# [A] iteration 0, slept 0.062s
# [B] iteration 0, slept 0.148s
# [A] iteration 1, slept 0.145s
# [B] iteration 1, slept 0.074s
# [A] iteration 2, slept 0.132s
# [B] iteration 2, slept 0.148s