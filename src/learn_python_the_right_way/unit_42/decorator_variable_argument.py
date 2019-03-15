def trace(func):                   # 장식된(호출할) 함수를 매개변수로 받음
    def wrapper(*args, **kwargs):  # 가변 인수 함수로 만듦
        r = func(*args, **kwargs)  # func 에 args, kwargs 를 언패킹하여 넣어줌.
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(func.__name__, args, kwargs, r))
        return r        # 매개변수와 반환값 출력, func 의 반환값을 반환
    return wrapper      # wrapper 함수 반환


@trace                  # @decorator
def get_max(*args):     # 위치 인수를 사용하는 가변 인수 함수
    return max(args)


@trace                  # @decorator
def get_min(**kwargs):  # 키워드 인수를 사용하는 가변 인수 함수
    return min(kwargs.values())


@trace
def add(a, b):
    return a + b


print(get_max(10, 20))
print(get_min(x=10, y=20, z=30))
print(add(10, 30))
