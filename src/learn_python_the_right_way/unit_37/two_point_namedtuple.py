import math
import collections

Point2D = collections.namedtuple('Point2D', ['x', 'y'])  # namedtuple 로 점 표현


p1 = Point2D(x=30, y=20)  # 점1
p2 = Point2D(x=60, y=50)  # 점2

a = p2.x - p1.x  # 선 a의 길이
b = p2.y - p1.y  # 선 b의 길이

c = math.sqrt((a * a) + (b * b))  # (a * a) + (b * b)의 제곱근을 구함.
print(c)
