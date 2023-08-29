import turtle
import pandas as pd
import time


#Initializing turtles/display settings
screen = turtle.Screen()
writing_turtle = turtle.Turtle()
score_turtle = turtle.Turtle()
error_turtle = turtle.Turtle()

screen.title('U.S. States Guessing Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


#Turtle settings/functionality
writing_turtle.penup()
writing_turtle.hideturtle()

score_turtle.penup()
score_turtle.hideturtle()

error_turtle.penup()
error_turtle.hideturtle()


#Pandas data extraction
data = pd.read_csv("50_states.csv")
states_names = data['state'].to_list()
states_x_coord = data['x'].to_list()
states_y_coord = data['y'].to_list()


#Game functions/setup for the game
correct_guesses = []
score = 0
exit_int = 0

def setup():
    global user_guess

    score_turtle.goto(-150,250)
    score_turtle.write(f"Current score: {score}/50", font=('Arial', 30, 'bold'))

    if score == 0:
        user_guess = screen.textinput("U.S. States Game", "Name a U.S. State below:")
        user_guess = user_guess.title()

    elif score > 0:
          user_guess = screen.textinput("U.S. States Game", "Can you name another one?")
          user_guess = user_guess.title()

    else:
        pass


def game_function():
    global score
    global exit_int
    global missing_states
    global new_data
    setup()
    if user_guess in states_names and user_guess not in correct_guesses:
        score += 1
        state_chosen = data[data['state'] == user_guess]
        x_coord = int(state_chosen['x'])
        y_coord = int(state_chosen['y']) 
        correct_guesses.append(user_guess)

        writing_turtle.goto(x_coord, y_coord)
        writing_turtle.write(user_guess,align='Center',font=('Arial', 12, 'bold'))

        score_turtle.clear()
    
    elif user_guess == 'Exit':
        missing_states = [item for item in states_names if item not in correct_guesses]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        exit_int = 1

    else:
        error_turtle.goto(-20, 340)
        error_turtle.write("Invalid choice! Try again", align='Center',font=('Arial', 18, 'bold'))
        time.sleep(1)
        error_turtle.clear()


#Game loop
while len(correct_guesses)<50 and exit_int == 0:
    game_function()