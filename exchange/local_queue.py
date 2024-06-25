import asyncio
import random


async def producer(queue):
    for i in range(10):
        item = random.randint(0, 100)
        await queue.put(item)
        print(f'Produced {item}')
        await asyncio.sleep(1)


async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f'Consumed {item}')
        await asyncio.sleep(1)


async def main():
    queue = asyncio.Queue()
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    await producer_task
    await queue.put(None)
    await consumer_task


asyncio.run(main())
