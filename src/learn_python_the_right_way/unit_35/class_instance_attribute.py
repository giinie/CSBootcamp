class Person:
    def __init__(self):
        self.bag = []  # 인스턴스 속성(instance attribute): 인스턴스 별로 독립적 사용.

    def put_bag(self, stuff):
        self.bag.append(stuff)  # self.으로 인스턴스 속성에 접근


james = Person()
james.put_bag('book')

maria = Person()
maria.put_bag('key')

print(james.bag)
print(maria.bag)

print(james.__dict__)
print(Person.__dict__)
