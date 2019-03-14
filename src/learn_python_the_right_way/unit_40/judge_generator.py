def prime_number_generator(start, stop):
    for i in range(start, stop):
        if is_prime_number(i):
            yield i


def is_prime_number(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        return False


start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')
