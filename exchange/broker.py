import asyncio


async def handle_producer(reader, writer, queue):
    while True:
        data = await reader.readline()
        message = data.decode().strip()
        if message == 'END':
            break
        await queue.put(message)
    writer.close()
    await writer.wait_closed()


async def handle_consumer(reader, writer, queue):
    while True:
        message = await queue.get()
        if message == 'END':
            break
        writer.write((message + '\n').encode())
        await writer.drain()
    writer.close()
    await writer.wait_closed()


async def broker():
    queue = asyncio.Queue()

    async def handle_client(reader, writer):
        client_type = await reader.readline()
        if client_type.decode().strip() == 'PRODUCER':
            await handle_producer(reader, writer, queue)
        else:
            await handle_consumer(reader, writer, queue)

    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)

    async with server:
        await server.serve_forever()


asyncio.run(broker())
