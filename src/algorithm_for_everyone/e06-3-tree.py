# 재귀 호출을 이용한 나무 모형 그리기
import turtle as t

def tree(br_len):
    if br_len <= 5:
        return
    new_len = br_len * 0.7
    t.forward(br_len)
    t.right(20)
    tree(new_len)
    t.left(40)
    tree(new_len)
    t.right(20)
    t.backward(br_len)

t.speed(0)
t.left(90)
tree(70)
t.hideturtle()
t.done()