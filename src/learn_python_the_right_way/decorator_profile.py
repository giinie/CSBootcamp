from time import time
from functools import reduce, wraps


def profile(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        begin = time()
        r = func(*args, **kwargs)
        end = time()
        print('실행 시간: {:.3f}초'.format(end - begin))
        return r
    return wrapper


@profile
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(10000))
