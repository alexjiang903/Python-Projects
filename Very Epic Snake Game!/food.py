from turtle import Turtle
import random


def random_location():
    random_x = random.randint(-280, 280)
    random_y = random.randint(-280, 245)
    return random_x, random_y


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('red')
        self.shapesize(stretch_len=0.4, stretch_wid=0.4)
        self.setpos(random_location())

    def refresh(self):
        self.setpos(random_location())
