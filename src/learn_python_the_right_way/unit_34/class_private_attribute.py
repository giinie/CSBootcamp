class Person:
    def __init__(self, name, age, address, wallet):
        self.__hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # 변수 앞에 __를 붙여서 비공개 속성으로 만듦.

    def __greeting(self):  # 비공개 메서드
        print('{} 저는 {}입니다.'.format(self.__hello, self.name))

    def hello(self):
        self.__greeting()  # 클래스 안에서는 비공개 메서드를 호출할 수 있음.

    def pay(self, amount):
        if amount > self.__wallet:
            print('돈이 모자라네....')
            return
        self.__wallet -= amount  # 비공개 속성은 클래스 안의 메서드에서만 접근 가능.
        print('이제 {}원 남았네요.'.format(self.__wallet))


maria = Person('maria', 20, 'seocho Seoul, Korea', 10000)

print('name:', maria.name)
print('age:', maria.age)
print('addr:', maria.address)
# print('wall:', maria.wallet)  # 클래스 바깥에서 비공개 속성에 접근하면 에러 발생.
maria.pay(3000)
maria.pay(10000)
maria.hello()
maria.__greeting()  # error: 클래스 바깥에서는 비공개 메서드를 호출할 수 없음.
