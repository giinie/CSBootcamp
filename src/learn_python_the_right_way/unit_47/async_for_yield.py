import asyncio


async def async_counter(stop):
    n = 0
    while n < stop:
        yield n
        n += 1
        await asyncio.sleep(1.0)


async def main():
    async for i in async_counter(3):
        print(i, end=' ')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
