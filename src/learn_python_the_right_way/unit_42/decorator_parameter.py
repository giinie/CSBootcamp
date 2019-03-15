def is_multiple(x):             # 데코레이터가 사용할 매개변수를 지정
    def real_decorator(func):   # 장식된(호출할) 함수를 매개변수로 받음
        def wrapper(*args, **kwargs):
            r = func(*args, **kwargs)
            if r % x == 0:
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r            # func 의 반환값을 반환
        return wrapper          # wrapper 함수 반환
    return real_decorator       # real_decorator 함수 반환


@is_multiple(3)  # @decorator(param)
# @is_multiple(7)  # @decorator(param)
def add(a, b):
    return a + b


print(add(10, 20))
print(add(2, 5))
