class Trace:
    def __init__(self, func):   # 장식될(호출할) 함수를 인스턴스의 초깃값으로 받음.
        self.func = func        # 장식될 함수를 속성 func 에 저장

    def __call__(self, *args, **kwargs):    # 장식될 함수의 매개변수 처리
        r = self.func(*args, **kwargs)      # self.func 에 매개변수를 넣어서 호출하고
                                            # 반환값을 변수에 저장
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(self.func.__name__, args, kwargs, r))
        return r  # 매개변수와 반환값 출력 후, self.func 의 반환값을 반환


@Trace  # @decorator
def add(a, b):
    return a + b


print(add(10, 20))
print(add(a=10, b=30))
