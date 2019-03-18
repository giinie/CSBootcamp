def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('{}: {}'.format(message, values_str))


log('My numbers are', [1, 2])
log('Hi there', [])

print('-' * 50)


def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('{}: {}'.format(message, values_str))


log('My numbers are', 1, 2)
log('Hi there')

print('-' * 50)

favorites = [7, 33, 99]
log('Favorite colors', *favorites)

print('-' * 50)


def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)


it = my_generator()
my_func(*it)

print('-' * 50)


def log(sequence, message, *values):
    if not values:
        print('{}: {}'.format(sequence, message))
    else:
        values_str = ', '.join(str(x) for x in values)
        print('{}: {}: {}'.format(sequence, message, values_str))


log(1, 'Favorites', 7, 33)      # New usage is OK
log('Favorite numbers', 7, 33)  # Old usage breaks

print('-' * 50)

