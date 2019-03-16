import asyncio


async def add(a, b):
    print('add: {} + {}'.format(a, b))
    await asyncio.sleep(1.0)    # 1초 대기. asyncio.sleep 도 네이티브 코루틴
    return a + b


async def print_add(a, b):
    result = await add(a, b)  # await 로 다른 네이티브 코루틴 실행하고 반환값을 변수에 저장
    print('print_add: {} + {} = {}'.format(a, b, result))


loop = asyncio.get_event_loop()
loop.run_until_complete(print_add(1, 2))
loop.close()
