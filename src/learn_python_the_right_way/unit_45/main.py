# from unit_45 import square2
#
# print(square2.base)         # 모듈.변수 형식으로 모듈의 변수 사용
# print(square2.square(10))   # 모듈.함수() 형식으로 모듈의 함수 사용

# import person
#
# maria = person.Person('Maria', 20, 'banpodong seochogu seoul')
# maria.greeting()

# import hello
#
# print('main.py __name__:', __name__)

# import calcpkg.operation
# import calcpkg.geometry
#
# print(calcpkg.operation.add(10, 20))
# print(calcpkg.operation.mul(10, 20))
#
# print(calcpkg.geometry.triangle_area(30, 40))
# print(calcpkg.geometry.rectangle_area(30, 40))

# import calcpkg
#
# print(calcpkg.add(10, 20))
# print(calcpkg.mul(10, 20))
#
# print(calcpkg.triangle_area(30, 40))
# print(calcpkg.rectangle_area(30, 40))

from calcpkg import *

print(add(10, 20))
# print(mul(10, 20))

print(triangle_area(30, 40))
# print(rectangle_area(30, 40))
