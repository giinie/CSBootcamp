class Person:
    bag = []  # 클래스 속성(class attribute): 모든 인스턴스에서 공유.

    def put_bag(self, stuff):
        # self.bag.append(stuff)  # self.으로 클래스 속성에 접근 가능하지만
        Person.bag.append(stuff)  # 클래스 이름으로 클래스 속성에 접근하면 코드가 명확해진다.


james = Person()
james.put_bag('book')

maria = Person()
maria.put_bag('key')

print(james.bag)
print(maria.bag)
print(Person.bag)  # 클래스 바깥에서도 클래스 이름으로 클래스 속성에 접근 가능.

print(james.__dict__)
print(Person.__dict__)
