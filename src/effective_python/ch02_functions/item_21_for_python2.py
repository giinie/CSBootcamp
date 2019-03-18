def print_args(*args, **kwargs):
    print('Positional:', args)
    print('Keyword:', kwargs)


print_args(1, 2, foo='bar', stuff='meep')
print('-' * 50)


def safe_division_d(number, divisor, **kwargs):
    ignore_overflow = kwargs.pop('ignore_overflow', False)
    ignore_zero_division = kwargs.pop('ignore_zero_division', False)
    if kwargs:
        raise TypeError('Unexpected **kwargs: {}'.format(kwargs))
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


print(safe_division_d(1, 10))
print(safe_division_d(1, 0, ignore_zero_division=True))
print(safe_division_d(1, 10**500, ignore_overflow=True))
print(safe_division_d(1, 10**500, True, False))
print(safe_division_d(1, 0, unexpected=True))
print('-' * 50)
