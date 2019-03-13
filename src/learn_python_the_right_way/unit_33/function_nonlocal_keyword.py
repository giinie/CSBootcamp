def print_hello():
    hello = 'Hello, world!'

    def print_message():
        nonlocal hello  # 현재 함수의 바깥쪽에 있는 지역 변수 사용
        hello = 'Hello, python'

    print_message()
    print(hello)


print_hello()
