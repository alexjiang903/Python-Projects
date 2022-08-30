from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager():
    def __init__(self):
        self.cars = []
        self.generate_car()

    def random_pos(self):
        random_y = random.randint(-230, 250)
        return 300, random_y

    def generate_car(self):
        car = Turtle()
        car.shape('square')
        car.speed('fastest')
        car.color(random.choice(COLORS))
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(self.random_pos())
        self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.back(STARTING_MOVE_DISTANCE)


    def increase_level(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

