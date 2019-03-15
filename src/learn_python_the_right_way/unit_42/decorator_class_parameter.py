from functools import wraps


class IsMultiple:
    def __init__(self, x):  # 데코레이터가 사용할 매개변수를 초깃값으로 받음.
        self.x = x          # 매개변수를 속성 x 에 저장

    def __call__(self, func):               # 장식될(호출할) 함수를 매개변수로 받음
        @wraps(func)
        def wrapper(*args, **kwargs):       # 장식될 함수의 매개변수와 똑같이 지정
            r = func(*args, **kwargs)       # func 을 호출하고 반환값을 변수에 저장
            if r % self.x == 0:
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, self.x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, self.x))
            return r    # func 의 반환값을 반환
        return wrapper  # wrapper 함수 반환


@IsMultiple(3)  # @decorator(param)
@IsMultiple(7)  # @decorator(param)
def add(a, b):
    return a + b


print(add(10, 20))
print(add(a=2, b=5))
