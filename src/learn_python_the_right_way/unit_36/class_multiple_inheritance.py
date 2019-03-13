class Person:
    def greeting(self):
        print('안녕하세요.')


class University:
    def manage_credit(self):
        print('학점관리')


class Undergraduate(Person, University):
    def study(self):
        print('공부하기')


james = Undergraduate()
james.greeting()        # 기반 클래스 Person 의 메서도 호출
james.manage_credit()   # 기반 클래스 University 의 메서드 호출
james.study()           # 파생 클래스 Undergraduate 에 추가한 메서드 호출
