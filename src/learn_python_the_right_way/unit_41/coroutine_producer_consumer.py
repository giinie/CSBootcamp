def sum_coroutine():
    total = 0
    while True:            # 코루틴을 계속 유지하기 위해 무한 루프 사용
        x = (yield total)  # 코루틴 바깥에서 값을 받아오면서 바깥으로 값(total)을 전달
        total += x


co = sum_coroutine()
print(next(co))    # 코루틴 안의 yield 까지 코드 실행(최초 실행)하고 코루틴에서 나온 값 출력

print(co.send(1))  # 코루틴에 숫자 1을 보내고 코루틴에서 나온 값 출력
print(co.send(2))  # 코루틴에 숫자 2을 보내고 코루틴에서 나온 값 출력
print(co.send(3))  # 코루틴에 숫자 3을 보내고 코루틴에서 나온 값 출력
