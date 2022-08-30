from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.setpos(position)
        self.speed('fastest')
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        curr_y = self.ycor()
        if curr_y <= 230:
            self.goto(self.xcor(), curr_y + 30)

    def down(self):
        curr_y = self.ycor()
        if curr_y >= -230:
            self.goto(self.xcor(), curr_y - 30)







