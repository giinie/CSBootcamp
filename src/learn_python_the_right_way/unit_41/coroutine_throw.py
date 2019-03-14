def sum_coroutine():
    try:
        total = 0
        while True:            # 코루틴을 계속 유지하기 위해 무한 루프 사용
            x = (yield total)  # 코루틴 바깥에서 값을 받아오면서 바깥으로 값(total)을 전달
            total += x
    except RuntimeError as e:
        print(e)
        yield total            # 코루틴 바깥으로 값 전달


co = sum_coroutine()
next(co)

for i in range(20):
    co.send(i)

print(co.throw(RuntimeError, '예외로 코루틴 끝내기'))  # 코루틴의 except 에서 yield 로 전달받은 값
