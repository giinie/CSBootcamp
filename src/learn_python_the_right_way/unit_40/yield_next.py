def number_generator():
    yield 0
    yield 1
    yield 2


g = number_generator()

a = next(g)  # yield 를 사용하여 함수 바깥으로 전달한 값은 next 의 반환값으로 나옴.
print(a)

b = next(g)
print(b)

c = next(g)
print(c)
