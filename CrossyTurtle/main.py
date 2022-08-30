import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_generator = CarManager()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True

times_run = 0
n = 10  # how often a new car is created (higher value = less often)

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if times_run % n == 0:
        car_generator.generate_car()
    car_generator.move_car()

    for car in car_generator.cars:
        car_pos = car.position()
        if player.distance(car_pos) <= 25:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= 280:
        player.new_level()
        scoreboard.next_level_message()
        scoreboard.next_level()
        car_generator.increase_level()
        if n > 2:
            n -= 1

    times_run += 1
