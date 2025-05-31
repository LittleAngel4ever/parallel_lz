import asyncio

# global variable
counter = 0

async def safe_incr(lock: asyncio.Lock, incr: int, task_id: int):
    global counter
    for _ in range(incr):
        async with lock:
            counter += 1
        # swipe content
        await asyncio.sleep(0)
    print(f"[Coroutine {task_id}] finnished work.")

async def main():
    global counter
    lock = asyncio.Lock()         # Create asyncio Lock for synchronization
    tasks = []
    num_tasks = 10                # Number of coroutines
    incr_per_task = 100     # Each coroutine executes 100 increments

    #starts Coroutines
    for i in range(1, num_tasks + 1):
        task = asyncio.create_task(safe_incr(lock, incr_per_task, i))
        tasks.append(task)

    # finish of all tasks
    await asyncio.gather(*tasks)
    print(f"\nThe final value of the counter variable: {counter}")

if __name__ == '__main__':
    asyncio.run(main())