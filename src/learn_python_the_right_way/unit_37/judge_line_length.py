import math


class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())

for i in range(len(p) - 1):
    a = p[i].x - p[i+1].x  # 선 a의 길이
    b = p[i].y - p[i+1].y  # 선 b의 길이
    length += math.sqrt((a * a) + (b * b))

print(length)
