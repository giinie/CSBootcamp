def accumulate():
    total = 0
    while True:
        x = (yield)         # 코루틴 바깥에서 값을 받아옴
        if x is None:       # 받아온 값이 None 이면
            return total    # 합계를 반환
        total += x


def sum_coroutine():
    while True:
        total = yield from accumulate()  # accumulate 의 반환값을 가져옴
        print(total)


co = sum_coroutine()
next(co)

for i in range(1, 11):
    co.send(i)          # 코루틴 accumulate 에 숫자를 보냄
co.send(None)           # 코루틴 accumulate 에 None 을 보내서 숫자 누적을 끝냄

for i in range(1, 101):
    co.send(i)          # 코루틴 accumulate 에 숫자를 보냄
co.send(None)           # 코루틴 accumulate 에 None 을 보내서 숫자 누적을 끝냄
