def number_coroutine():
    try:
        while True:      # 코루틴을 계속 유지하기 위해 무한 루프 사용
            x = (yield)  # 코루틴 바깥에서 값을 받아옴, yield 를 괄호로 묶어야 함.
            print(x, end=' ')
    except GeneratorExit:  # 코루틴이 종료될 때 GeneratorExit 예외 발생
        print()            # 종료 시 원하는 코드 실행
        print('코루틴 종료')


co = number_coroutine()
next(co)    # 코루틴 안의 yield 까지 코드 실행(최초 실행)

for i in range(20):
    co.send(i)

co.close()  # 코루틴 종료
