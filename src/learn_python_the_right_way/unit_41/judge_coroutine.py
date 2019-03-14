def calc():
    result = 0
    while True:
        x = (yield result)
        a, o, b = x.split(' ')
        if o == '+':
            result = int(a) + int(b)
        elif o == '-':
            result = int(a) - int(b)
        elif o == '*':
            result = int(a) * int(b)
        else:
            result = int(a) / int(b)


expressions = input().split(', ')

c = calc()
next(c)

for e in expressions:
    print(c.send(e))

c.close()
