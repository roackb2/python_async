import asyncio

async def hello():
    await asyncio.sleep(1)
    print('hello')

async def world():
    await asyncio.sleep(2)
    print('world')

async def main():
    task1 = asyncio.create_task(world())
    task2 = asyncio.create_task(hello())
    await task1
    await task2

asyncio.run(main())
