def trace(func):        # 장식된(호출할) 함수를 매개변수로 받음
    def wrapper(a, b):  # 장식된 함수 add(a, b)의 매개변수와 똑같이 지정
        r = func(a, b)  # func 에 매개변수 a, b 를 넣어서 호출하고 반환값을 변수에 저장
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))
        return r        # 매개변수와 반환값 출력, func 의 반환값을 반환
    return wrapper      # wrapper 함수 반환


@trace              # @decorator
def add(a, b):      # 매개변수는 두 개
    return a + b    # 매개변수 두 개를 더해서 반환


print(add(10, 20))
