# may take a few seconds to load because the colors need to be extracted from the image
import turtle
from colors import rgb_colors
from turtle import Turtle, Screen
import random
turtle.colormode(255)

bob = Turtle()
bob.shape('turtle')
bob.color('green')
bob.resizemode('auto')
bob.speed('fastest')
bob.penup()

bob.setpos(-250, -250)


def paint_row():
    for x in range(10):
        random_color = random.choice(rgb_colors)
        bob.dot(20, random_color)
        bob.forward(50)


n = -200
for k in range(10):
    paint_row()
    bob.setpos(-250, n)
    n += 50

screen = Screen()
screen.screensize(1000, 1000)
screen.exitonclick()
