# class Meta(type):
#     def __new__(meta, name, bases, class_dict):
#         print((meta, name, bases, class_dict))
#         return type.__new__(meta, name, bases, class_dict)
#
#
# class MyClass(object, metaclass=Meta):
#     stuff = 123
#
#     def foo(self):
#         pass


class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        # Don't validate the abstract Polygon class
        if bases != (object,):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides')
        return type.__new__(meta, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
    sides = None  # Specified by subclass

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    sides = 3


print(Triangle.interior_angles())
print('-' * 50)

print('Before class')
class Line(Polygon):
    print('Before sides')
    sides = 1
    print('After sides')
print('After class')
