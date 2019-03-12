x, y = map(int, input().split())


def calc(a, b):
    return a + b, a - b, a * b, a / b


a, s, m, d = calc(x, y)
print('덧셈: {}, 뺄셈: {}, 곱셈: {}, 나눗셈: {}'.format(a, s, m, d))
