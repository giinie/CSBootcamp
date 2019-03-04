def apply(func: object, value: object) -> object:
    return func(value)


def outer_1():
    def inner():
        print('This is inner.')

    print('This is outer, invoking inner.')
    inner()


def outer():
    def inner():
        print('This is inner.')

    print('This is outer, invoking inner.')
    return inner


def myfunc(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()


def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()


def myfunc3(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=' ')
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()
