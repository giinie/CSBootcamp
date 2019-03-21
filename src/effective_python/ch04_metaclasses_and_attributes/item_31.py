from weakref import WeakKeyDictionary


class Homework(object):
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._grade = value


galileo = Homework()
galileo.grade = 95

print(galileo.grade)
print('-' * 50)


class Exam(object):
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")

    @property
    def writing_grade(self):
        return self._writing_grade

    @writing_grade.setter
    def writing_grade(self, value):
        self._check_grade(value)
        self._writing_grade = value

    @property
    def math_grade(self):
        return self._math_grade

    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self._math_grade = value


galileo = Exam()
galileo.writing_grade = 85
galileo.math_grade = 99
print('Writing: %5r' % galileo.writing_grade)
print('Math:    %5r' % galileo.math_grade)
print('-' * 50)


# class Grade(object):
#     def __get__(*args, **kwargs):
#         pass
#
#     def __set__(*args, **kwargs):
#         pass
#
#
# class Exam(object):
#     # Class attributes
#     math_grade = Grade()
#     writing_grade = Grade()
#     science_grade = Grade()
#
#
# exam = Exam()
# exam.writing_grade = 40
#
# Exam.__dict__['writing_grade'].__set__(exam, 40)
#
# print(exam.writing_grade)
#
# print(Exam.__dict__['writing_grade'].__get__(exam, Exam))
# print('-' * 50)


class Grade(object):
    def __init__(self):
        self._value = 0

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._value = value


class Exam(object):
    # Class attributes
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


first_exam = Exam()
first_exam.writing_grade = 82
first_exam.science_grade = 99
print('Writing', first_exam.writing_grade)
print('Science', first_exam.science_grade)
print('-' * 50)

second_exam = Exam()
second_exam.writing_grade = 75
print('Second', second_exam.writing_grade, 'is right')
print('First', first_exam.writing_grade, 'is wrong')
print('-' * 50)


# class Grade(object):
#     def __init__(self):
#         self._values = {}
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return self._values.get(instance, 0)
#
#     def __set__(self, instance, value):
#         if not (0 <= value <= 100):
#             raise ValueError('Grade must be between 0 and 100')
#         self._values[instance] = value


class Grade(object):
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value


class Exam(object):
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


first_exam = Exam()
first_exam.writing_grade = 82
second_exam = Exam()
second_exam.writing_grade = 75
print('First', first_exam.writing_grade, 'is right')
print('Second', second_exam.writing_grade, 'is right')
print('-' * 50)

