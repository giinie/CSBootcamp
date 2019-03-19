class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class Explicit(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value * 2)


class Implicit(MyBaseClass):
    def __init__(self, value):
        super().__init__(value * 2)


print(Explicit(10).value == Implicit(10).value)


class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 5


class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value += 2


class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super().__init__(value)


foo = GoodWay(5)
print('Should be 5 * (5 + 2) = 35 and is', foo.value)
print('-' * 50)

from pprint import pprint
pprint(GoodWay.mro())
