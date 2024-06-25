import asyncio
import random


async def producer():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    writer.write(b'PRODUCER\n')
    await writer.drain()

    for i in range(10):
        item = random.randint(0, 100)
        message = f'{item}\n'
        writer.write(message.encode())
        await writer.drain()
        await asyncio.sleep(1)

    writer.write(b'END\n')
    await writer.drain()
    writer.close()
    await writer.wait_closed()


asyncio.run(producer())
