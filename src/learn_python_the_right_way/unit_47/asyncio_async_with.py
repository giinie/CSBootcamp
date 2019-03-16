import asyncio


class AsyncAdd:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    async def __aenter__(self):
        await asyncio.sleep(1.0)
        return self.a + self.b

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass


async def main():
    async with AsyncAdd(1, 2) as result:
        print(result)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
