# 09_asyncio_vs_threads_fx_demo.py

import asyncio
from concurrent.futures import ThreadPoolExecutor

from common.workload import io_bound_work
from common.timing import timed


def fetch_fx_quote(pair: str) -> str:
    io_bound_work(0.05, 0.15)
    return f"QUOTE {pair}"


PAIRS = ["EURUSD", "USDJPY", "GBPUSD", "AUDUSD", "USDCHF"] * 4


def thread_demo():
    with timed("Threads FX fetch"):
        with ThreadPoolExecutor(max_workers=5) as executor:
            results = list(executor.map(fetch_fx_quote, PAIRS))
    print(f"Received {len(results)} quotes (threads).")


async def async_fetch_fx_quote(pair: str) -> str:
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, fetch_fx_quote, pair)
    return result


async def async_demo():
    with timed("Async FX fetch"):
        results = await asyncio.gather(
            *(async_fetch_fx_quote(p) for p in PAIRS)
        )
    print(f"Received {len(results)} quotes (async).")


if __name__ == "__main__":
    thread_demo()
    asyncio.run(async_demo())
