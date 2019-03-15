def trace(func):
    def wrapper(self, *args, **kwargs):  # 장식된(호출할) 함수가 인스턴스 메서드이므로
                                         # 첫 번째 매개변수는 self 로 지정
        r = func(self, *args, **kwargs)  # self 와 매개변수fmf rmeofh sjgdjwna
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(func.__name__, args, kwargs, r))
        return r        # 매개변수와 반환값 출력, func 의 반환값을 반환
    return wrapper      # wrapper 함수 반환


class Calc:
    @trace
    def get_max(self, *args):
        return max(args)

    @trace
    def get_min(self, **kwargs):
        return min(kwargs.values())

    @trace
    def add(self, a, b):
        return a + b


c = Calc()
print(c.get_max(10, 20))
print(c.get_min(x=10, y=20, z=30))
print(c.add(10, 30))
