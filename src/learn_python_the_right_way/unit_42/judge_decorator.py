from functools import wraps


def html_tag(tag):  # 데코레이터가 사용할 매개변수를 지정
    def real_decorator(func):  # 장식된(호출할) 함수를 매개변수로 받음
        @wraps(func)
        def wrapper(*args, **kwargs):
            return '<{0}>{1}</{0}>'.format(tag, func(*args, **kwargs))

        return wrapper          # wrapper 함수 반환
    return real_decorator       # real_decorator 함수 반환


a, b = input().split()


@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world'


print(hello())
