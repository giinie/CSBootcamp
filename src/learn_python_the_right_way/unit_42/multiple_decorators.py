def decorator1(func):
    def wrapper():
        print('decorator1')
        func()
    return wrapper


def decorator2(func):
    def wrapper():
        print('decorator2')
        func()
    return wrapper


# 데코레이터를 여러 개 지정
@decorator1
@decorator2
def hello():
    print('hello')


hello()

# @을 사용하지 않을 경우
# decorated_hello = decorator1(decorator2(hello))
# decorated_hello()
