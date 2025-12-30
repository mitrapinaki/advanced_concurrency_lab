# 08_asyncio_producer_consumer

import asyncio
from common.workload import io_bound_work


async def producer(q: "asyncio.Queue[float]", n: int):
    loop = asyncio.get_running_loop()
    for _ in range(n):
        delay = await loop.run_in_executor(None, io_bound_work, 0.01, 0.05)
        await q.put(delay)
    await q.put(None)  # sentinel


async def consumer(q: "asyncio.Queue[float]"):
    while True:
        item = await q.get()
        if item is None:
            q.task_done()
            break
        print(f"[async consumer] got delay={item:.3f}")
        q.task_done()


async def main():
    q: "asyncio.Queue[float]" = asyncio.Queue()
    prod = asyncio.create_task(producer(q, 10))
    cons = asyncio.create_task(consumer(q))
    await asyncio.gather(prod, cons)
    await q.join()


if __name__ == "__main__":
    asyncio.run(main())
