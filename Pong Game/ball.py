from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = 12
        self.y_move = 12
        self.sleep_time = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def detect_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.sleep_time *= 0.9

    def reset_game(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.sleep_time = 0.1













