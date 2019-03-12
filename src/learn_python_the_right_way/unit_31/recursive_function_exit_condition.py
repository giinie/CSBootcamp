def hello(count):
    if count == 0:  # 종료 조건을 만듦. count가 0이면 다시 hello 함수를 호출하지 않고 끝냄.
        return

    print('Hello, world!', count)
    count -= 1  # count 1 감소
    hello(count)  # 다시 hello에 넣음.


hello(5)
