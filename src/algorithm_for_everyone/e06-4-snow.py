# 재귀 호출을 이용한 눈꽃 그리기
import turtle as t

def snow_line(snow_len):
    if snow_len <= 10:
        t.forward(snow_len)
        return
    new_len = snow_len / 3
    snow_line(new_len)
    t.left(60)
    snow_line(new_len)
    t.right(120)
    snow_line(new_len)
    t.left(60)
    snow_line(new_len)

t.speed(0)
snow_line(150)
t.right(120)
snow_line(150)
t.right(120)
snow_line(150)
t.hideturtle()
t.done()