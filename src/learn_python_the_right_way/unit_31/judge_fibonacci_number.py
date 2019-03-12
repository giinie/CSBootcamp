def fib(x):
    if x <= 1:
        return x
    return fib(x-2) + fib(x-1)


n = int(input())
if n < 0:
    print('Please enter a positive integer.')
else:
    print(fib(n))
