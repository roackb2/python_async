import asyncio

async def echo(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 5760)

    print(f'send message: {message!r}')
    writer.write(message.encode())
    print(f'close the connection')
    writer.close()

asyncio.run(echo('hey'))
