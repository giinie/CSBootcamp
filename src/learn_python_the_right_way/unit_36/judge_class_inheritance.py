class Animal:
    def eat(self):
        print('먹다')


class Wing:
    def flap(self):
        print('파닥거리다')


class Bird(Animal, Wing):
    def fly(self):
        print('날다')


b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))
