import asyncio
import ipaddress

async def handle_client(reader, writer):
    res = await reader.read()
    message = res.decode()
    addr = writer.get_extra_info('peername')
    print(f"Received {message!r} from {addr[0]!r}")

async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 5760)
    addr = server.sockets[0].getsockname()
    print(f'Server listening on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
