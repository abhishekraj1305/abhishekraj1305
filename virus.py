#creating a virus shape using python
from turtle import *
speed(10)
color('red')
bgcolor('black')
b = 200
while b > 0:
    left(b)
    forward(b * 4)
    b = b - 1