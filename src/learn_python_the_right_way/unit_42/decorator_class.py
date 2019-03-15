class Trace:
    def __init__(self, func):   # 장식될(호출할) 함수를 인스턴스의 초깃값으로 받음.
        self.func = func        # 장식될 함수를 속성 func 에 저장

    def __call__(self, *args, **kwargs):
        print(self.func.__name__, '함수 시작')  # __name__으로 함수 이름 출력
        self.func()                             # 속성 func 에 저장된 함수를 호출
        print(self.func.__name__, '함수 끝')


@Trace  # @decorator
def hello():
    print('hello')


hello()  # 함수를 그대로 호출

# trace_hello = Trace(hello)  # 데코레이너에 호출할 함수를 넣어서 인스턴스 생성
# trace_hello()               # 인스턴스를 호출. __call__ 메서드가 호출됨.
