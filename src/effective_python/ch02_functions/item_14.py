def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


x, y = 1, 0
result = divide(x, y)
if result is None:
    print('Invalid inputs')
else:
    print('Result is {:.1f}'.format(result))

print('-' * 50)

x, y = 0, 5
result = divide(x, y)
if not result:  # This is wrong!
    print('Invalid inputs')
else:
    print('Result is {:.1f}'.format(result))

print('-' * 50)


def divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


x, y = 0, 5
success, result = divide(x, y)
if not success:
    print('Invalid inputs')
else:
    print('Result is {:.1f}'.format(result))

print('-' * 50)

x, y = 0, 5
_, result = divide(x, y)
if not result:
    print('Invalid inputs')
else:
    print('Result is {:.1f}'.format(result))

print('-' * 50)


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e


x, y = 5, 3
try:
    result = divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is {:.1f}'.format(result))
