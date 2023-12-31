from turtle import *
import turtle as t

# def draw_polygon(length,n):
#     t.home()
#     t.shape('turtle')
#     t.color('skyblue','lavender')
#     t.begin_fill()
#     for i in range(n):
#         t.forward(length)
#         t.right(360/n)
#     t.end_fill()

# t.speed(1)
# draw_polygon(50,6)
# draw_polygon(100,4)

# t.setheading(135)
# t.forward(150)
# t.dot(10,'pink')

# 원의 반지름
r=100
# r만큼 이동해서 그리기 준비
up(); forward(r); down(); left(90)
# 반지름이 r인 원 그리기
circle(r)
# 한 변의 길이가 r의 두 배인 정사각형 그리기
# 한 번에 2r씩 직진해도 되지만 아래처럼 해도 될듯?

for i in range(4):
    forward(r); left(90); forward(r) # 정사각형 한변씩

# 자취 안남기기
penup()

import math
from random import randrange

def draw_random_dot():
    x,y = randrange(-r,r),randrange(-r,r)
    goto(x,y)
    if in_circle(x,y,r):
        color('red')
    else:
        color('blue')   
    dot()
    xcor()

def in_circle(x,y,r):
    return math.sqrt(x**2+y**2) <=r

#점 30개 찍기
for i in range(30):
    draw_random_dot()

hideturtle()

t.done() # turtle 그림유지

