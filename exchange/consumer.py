import asyncio


async def consumer():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    writer.write(b'CONSUMER\n')
    await writer.drain()

    while True:
        data = await reader.readline()
        message = data.decode().strip()
        if message == 'END':
            break
        print(f'Consumed {message}')

    writer.close()
    await writer.wait_closed()


asyncio.run(consumer())
