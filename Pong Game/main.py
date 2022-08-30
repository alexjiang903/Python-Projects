from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
ball = Ball()
scoreboard = Scoreboard()


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG')
screen.tracer(0)

play_to = int(screen.textinput('Score Keeping', 'What score do you want to play to? Input an integer below. '))
right_player_name = screen.textinput('Right Player', 'Name of player controlling right paddle: ')
left_player_name = screen.textinput('Left Player', 'Name of player controlling left paddle:  ')


screen.listen()

screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

game_running = True
while game_running:
    time.sleep(ball.sleep_time)
    screen.update()
    ball.move()
    ball.detect_wall()

    if ball.distance(r_paddle) < 50 and ball.xcor() >= 320:
        ball.bounce_x()

    elif ball.distance(l_paddle) < 50 and ball.xcor() <= -320:
        ball.bounce_x()

    # If right paddle misses
    if ball.xcor() >= 380:
        ball.reset_game()
        scoreboard.clear()
        scoreboard.left_point()

    # If left paddle misses
    elif ball.xcor() <= -380:
        ball.reset_game()
        scoreboard.clear()
        scoreboard.right_point()

    if scoreboard.l_score == play_to or scoreboard.r_score == play_to:
        if scoreboard.l_score > scoreboard.r_score:
            print(f'{left_player_name} wins! Congratulations!')
            game_running = False

        elif scoreboard.l_score == scoreboard.r_score:
            print(f"It's a tie between {left_player_name} and {right_player_name}! GG")
            game_running = False

        else:
            print(f'{right_player_name} wins! Congratulations!')
            game_running = False

    else:
        pass


screen.exitonclick()