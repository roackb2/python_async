import asyncio

async def handle_client(reader, writer):
    res = await reader.read()
    res = res.decode()
    print(res)

async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 5760)
    addr = server.sockets[0].getsockname()
    print(f'Server listening on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
