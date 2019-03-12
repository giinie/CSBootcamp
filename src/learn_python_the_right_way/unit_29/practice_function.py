x = 10
y = 3


def get_quotient_remainder(a, b):
    return a // b, a % b


quotient, remainder = get_quotient_remainder(x, y)
print('몫: {}, 나머지: {}'.format(quotient, remainder))
