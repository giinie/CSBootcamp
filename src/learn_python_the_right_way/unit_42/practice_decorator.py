from functools import wraps


def type_check(type_a, type_b):  # 데코레이터가 사용할 매개변수를 지정
    def real_decorator(func):    # 장식된(호출할) 함수를 매개변수로 받음
        @wraps(func)
        def wrapper(*args, **kwargs):
            if isinstance(args[0], type_a) and isinstance(args[1], type_b):
                return func(*args, **kwargs)
            else:
                raise RuntimeError('자료형이 올바르지 않습니다.')
        return wrapper          # wrapper 함수 반환
    return real_decorator       # real_decorator 함수 반환


@type_check(int, int)
def add(a, b):
    return a + b


print(add(10, 20))
print(add('hello', 'world'))
