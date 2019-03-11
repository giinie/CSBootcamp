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

for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)

a, b = map(int, input().split())

for i in range(a, b + 1):
    if i % 5 == 0 and i % 7 == 0:
        print(i, 'FizzBuzz')
    elif i % 5 == 0:
        print(i, 'Fizz')
    elif i % 7 == 0:
        print(i, 'Buzz')
    else:
        print(i)

import turtle as t

# n = int(input())
n = 6
t.shape('turtle')
t.color('#FF69B4')
t.begin_fill()
for i in range(n):
    t.fd(100)
    t.rt(360 / n)
t.end_fill()
t.mainloop()
print()

import turtle as t

# n = int(input())
n = 60
t.shape('turtle')
t.speed('fastest')
for i in range(n):
    t.circle(120)
    t.rt(360 / n)
t.mainloop()
print()

import turtle as t

t.shape('turtle')
t.speed('fastest')
for i in range(300):
    t.fd(i)
    t.rt(91)
t.mainloop()
print()

import turtle as t

a, b = map(int, input().split())

t.shape('turtle')
for i in range(a):
    t.fd(b)
    t.rt((360 / a) * 2)
    t.fd(b)
    t.lt(360 / a)
t.mainloop()
print()
