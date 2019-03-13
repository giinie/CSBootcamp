class Person:
    count = 0  # class attribute

    def __init__(self):
        Person.count += 1  # 인스턴스가 만들어질 때 클래스 속성 count 에 1을 더함.

    @classmethod
    def print_count(cls):
        print('{}명 생성되었습니다.'.format(cls.count))  # cls 로 클래스 속성에 접근

    @classmethod
    def create(cls):
        p = cls()
        return p


james = Person()
maria = Person()

Person.print_count()
