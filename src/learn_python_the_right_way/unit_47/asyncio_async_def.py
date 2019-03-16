import asyncio


async def hello():  # async def 로 네이티브 코루틴 생성.
    print('Hello, world!')


loop = asyncio.get_event_loop()     # 이벤트 루프 획득
loop.run_until_complete(hello())    # hello 가 끝날 때까지 기다림.
loop.close()                        # 이벤트 루프를 닫음.
