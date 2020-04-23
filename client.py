import asyncio

async def echo(message):
    reader, writer = await asyncio.open_connection('localhost', 5760)

    print(f'send message: {message!r}')
    writer.write(message.encode())
    print(f'close the connection')
    writer.close()

asyncio.run(echo('hey'))
