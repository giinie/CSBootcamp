class MyObject(object):
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field


foo = MyObject()
print(foo.public_field == 5)
print('-' * 50)

print(foo.get_private_field() == 10)
print('-' * 50)

# foo.__private_field


class MyOtherObject(object):
    def __init__(self):
        self.__private_field = 71

    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field


bar = MyOtherObject()
print(MyOtherObject.get_private_field_of_instance(bar) == 71)
print('-' * 50)


class MyParentObject(object):
    def __init__(self):
        self.__private_field = 71


class MyChildObject(MyParentObject):
    def get_private_field(self):
        return self.__private_field


baz = MyChildObject()
# baz.get_private_field()
print(baz._MyParentObject__private_field == 71)
print(baz.__dict__)


class MyClass(object):
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return str(self.__value)


foo = MyClass(5)
print(foo.get_value() == '5')
print('-' * 50)


class MyIntegerSubclass(MyClass):
    def get_value(self):
        return int(self._MyClass__value)

foo = MyIntegerSubclass(5)
print(foo.get_value() == 5)
print('-' * 50)


class MyBaseClass(object):
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value


class MyClass(MyBaseClass):
    def get_value(self):
        return str(super().get_value())


class MyIntegerSubclass(MyClass):
    def get_value(self):
        return int(self._MyClass__value)


foo = MyIntegerSubclass(5)
# foo.get_value()
print(foo.__dict__)
print('-' * 50)


class MyClass(object):
    def __init__(self, value):
        # This stores the user-supplied value for the object.
        # It should be coercible to a string. Once assigned for
        # the object it should be treated as immutable.
        self._value = value


class ApiClass(object):
    def __init__(self):
        self._value = 5

    def get(self):
        return self._value


class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'  # conflicts


a = Child()
print(a.get(), 'and', a._value, 'should be different')
print('-' * 50)


class ApiClass(object):
    def __init__(self):
        self.__value = 5

    def get(self):
        return self.__value


class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'  # OK!


a = Child()
print(a.get(), 'and', a._value, 'are different')
print('-' * 50)

