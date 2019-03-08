a, b = map(int, input().split())

i = a

while True:
    if i > b:
        break

    if i % 10 == 3:
        i += 1
        continue

    print(i, end=' ')
    i += 1

print()

a = int(input())

for i in range(a):
    for j in range(a * 2 - 1):
        if (a - 1 - i) <= j <= (a - 1 + i):
            print('*', end='')
        else:
            print(' ', end='')
    print()
print()

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, 'FizzBuzz')
    elif i % 3 == 0:
        print(i, 'Fizz')
    elif i % 5 == 0:
        print(i, 'Buzz')
    else:
        print(i)
