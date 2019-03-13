from abc import *


class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass  # 추상 메서드는 호출할 일이 없으므로 빈 메서드로 만듦.

    @abstractmethod
    def go_to_school(self):
        pass  # 추상 메서드는 호출할 일이 없으므로 빈 메서드로 만듦.


class Student(StudentBase):
    def study(self):
        print('공부하기')

    def go_to_school(self):
        print('학교가기')


james = Student()
james.study()
james.go_to_school()
