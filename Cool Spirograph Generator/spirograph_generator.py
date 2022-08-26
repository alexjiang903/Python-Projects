import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
import random

bob = Turtle()
bob.shape('turtle')
bob.fillcolor('aquamarine')
bob.speed('fastest')


def random_colour():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


n = 360  # change the number of circles you want in your spirograph
angle = 360 / n
for x in range(n):
    bob.pencolor(random_colour())
    bob.circle(100)
    current_direction = bob.heading()
    bob.seth(current_direction + angle)

screen = Screen()
screen.exitonclick()
screen.screensize(1000, 1000)
