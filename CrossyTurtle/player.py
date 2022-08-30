from turtle import Turtle
import time

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.speed('fastest')
        self.penup()
        self.goto(STARTING_POSITION)
        self.seth(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def new_level(self):
        time.sleep(1)
        self.goto(STARTING_POSITION)
        self.seth(90)




