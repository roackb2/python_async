import asyncio

class Server:
    async def handle_client(self, reader, writer):
        res = await reader.read()
        message = res.decode()
        addr = writer.get_extra_info('peername')
        print(f"Received {message!r} from {addr[0]!r}")

    async def run(self):
        self.server = await asyncio.start_server(self.handle_client, 'localhost', 5760)
        addr = server.sockets[0].getsockname()
        print(f'Server listening on {addr}')
        await self.server.serve_forever()

    def get_task(self):
        return asyncio.create_task(self.run())
