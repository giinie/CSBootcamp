def fn_expressive(upper=1000000):
    total = 0
    for n in range(upper):
        total += n
    return total


def fn_terse(upper=1000000):
    return sum(range(upper))


print('Functions return the same result:', fn_expressive() == fn_terse())

