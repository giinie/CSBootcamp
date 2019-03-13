class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{} 저는 {}입니다.'.format(self.hello, self.name))


maria = Person('maria', 20, 'seocho Seoul, Korea')
maria.greeting()

print('name:', maria.name)
print('age:', maria.age)
print('addr:', maria.address)
