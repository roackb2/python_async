import asyncio
from window import Window
from server import Server

async def main():
    window = Window()
    server = Server()

    server_task = server.get_task()
    await (window.get_task())
    await server_task

asyncio.run(main())
