from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")
SUB_FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.ht()
        self.penup()
        self.goto(-270, 250)
        self.speed('fastest')
        self.write(f'Level: {self.level}', align='Left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER. :(', align='Center', font=FONT)
        time.sleep(2)

    def next_level(self):
        self.clear()
        self.level += 1
        self.goto(-270, 250)
        self.write(f'Level: {self.level}', align='Left', font=FONT)

    def next_level_message(self):
        self.goto(0, 0)
        self.write(f'Congrats on beating level {self.level}! How far can you go?', align='Center', font=SUB_FONT)
        time.sleep(3)







