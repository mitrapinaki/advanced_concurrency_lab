# advanced_concurrency_lab

A practical lab for understanding **Python concurrency** in the context of real workloads.

This lab builds on `object_model_lab` and focuses on:

- Threads and the GIL
- Race conditions and shared state
- Locks and thread-safe patterns
- Producer–consumer pipelines
- Thread pools
- Processes vs threads
- `asyncio` basics and async pipelines
- Comparing async vs threads on FX-like workloads

Each file is a standalone experiment; together they form a coherent mental model.

---

## Files overview

### 01_threads_basics.py
- Create threads using `threading.Thread`
- Show interleaved output
- Demonstrate join and main-thread blocking

### 02_race_conditions.py
- Shared counter incremented by multiple threads
- Demonstrates race conditions and non-deterministic results

### 03_locks_and_rlock.py
- Protect shared state using `Lock` and `RLock`
- Show correct increments and discuss cost

### 04_queue_producer_consumer.py
- Use `queue.Queue` with producer/consumer threads
- Graceful shutdown using sentinel values

### 05_thread_pool_executor.py
- Use `concurrent.futures.ThreadPoolExecutor`
- Map tasks across threads
- Discuss when to use pools vs manual threads

### 06_processes_vs_threads.py
- Use `ProcessPoolExecutor` vs `ThreadPoolExecutor`
- Compare for CPU-bound vs IO-bound workloads

### 07_asyncio_basics.py
- Introduce coroutines, `async`/`await`
- Run multiple coroutines concurrently
- Show difference between sequential vs concurrent async

### 08_asyncio_producer_consumer.py
- Async producer–consumer using `asyncio.Queue`
- Demonstrate backpressure and cooperative multitasking

### 09_asyncio_vs_threads_fx_demo.py
- Simulated FX quote/order workload
- Compare threads vs asyncio for IO-bound tasks
- Show where async shines and where it doesn’t

### common/workload.py
- Simulated CPU-bound and IO-bound tasks
- Reused across the lab for consistent comparison

### common/timing.py
- Timing helpers for measuring execution time

### Learning goals
By the end of this lab, you should be able to:

- Explain Python’s GIL and its impact

- Choose between threads, processes, and asyncio

- Build thread-safe and async-safe producer–consumer pipelines

- Reason about state mutation under concurrency

- Apply these patterns to FX-style microservices
---

## How to run

From the project root:

```bash
python 01_threads_basics.py
python 02_race_conditions.py
...
python 09_asyncio_vs_threads_fx_demo.py


