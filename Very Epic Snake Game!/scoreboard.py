from turtle import Turtle
import time

FONT = 'Helvetica'
SIZE = 18
TYPE = 'normal'
ALIGNMENT = 'center'
COLOR = 'white'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pencolor(COLOR)
        self.penup()
        self.setpos(0, 270)
        self.write(f'Scoreboard: {self.score} ', align=ALIGNMENT, font=(FONT, 18, TYPE))

    def scorekeep(self):
        self.clear()
        self.score += 1
        self.write(f'Scoreboard: {self.score} ', align=ALIGNMENT, font=(FONT, 18, TYPE))

    def game_over(self):
        self.setpos(0, 0)
        self.write('Game Over.', align=ALIGNMENT, font=(FONT, 18, TYPE))
        time.sleep(3)
