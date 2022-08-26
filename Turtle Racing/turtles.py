from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.bgpic('finish_line.gif')
colors = ['red', 'orange', 'gold', 'green', 'blue', 'purple']
turtles_racing = []

user_bet = screen.textinput('Make your bet!', 'Which turtle will win the race? '
'Enter a color below (red, orange, gold, green, blue, or purple):')

if user_bet in colors:
    n = -80
    for color in colors:
        bob = Turtle(shape='turtle')
        bob.penup()
        bob.color(color)
        bob.goto(x=-220, y=n)
        turtles_racing.append(bob)
        n += 40

    is_racing = True
    while is_racing:
        for turtle in turtles_racing:
            if turtle.xcor() > 210:
                winning_color = turtle.pencolor()
                is_racing = False
            random_dist = random.randint(0, 10)
            turtle.forward(random_dist)

    if user_bet == turtle.pencolor():
        print(f'You won! The {winning_color} turtle was the winner.')

    else:
        print(f'You lost! The {winning_color} turtle was the winner.')
else:
    print('Sorry, that is not a valid color. Please try again.')

screen.exitonclick()
