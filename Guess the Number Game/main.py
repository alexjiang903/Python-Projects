from art import logo
import random

print(logo)

RANDOM_NUMBER = random.randint(1, 100)


def game_intro():
    print('')
    print('Welcome to Guess the Number!')
    print('I am thinking of a number between 1 and 100.')
    print('')
    print('''Game Modes:
    Easy: 10 guesses
    Medium: 7 guesses
    Hard: 5 guesses''')

game_intro()


def value_checker():
    global LIVES
    global USER_GUESS
    if USER_GUESS != RANDOM_NUMBER:
        if USER_GUESS < RANDOM_NUMBER:
            print('Too low!')
            print('Guess again.')
            LIVES -= 1
            print(f'You have {LIVES} lives left to guess the number')
            USER_GUESS = int(input('Make a guess:'))
        elif USER_GUESS > RANDOM_NUMBER:
            print('Too high!')
            print('Guess again.')
            LIVES -= 1
            print(f'You have {LIVES} lives left')
            USER_GUESS = int(input('Make a guess:'))


print('')
difficulty = input("Choose a difficulty: Type 'easy', 'medium', and 'hard' to select your difficulty. ")
difficulty = difficulty.lower()

if difficulty == 'easy':
    LIVES = 10
    lives_left = print(f'You have {LIVES} lives left')
    USER_GUESS = int(input('Make a guess: '))

    while USER_GUESS != RANDOM_NUMBER and LIVES > 1:
        value_checker()

    if USER_GUESS == RANDOM_NUMBER:
        print(f'Correct! The number was {RANDOM_NUMBER}. ')
        print(f'You had {LIVES} lives remaining.')
    elif LIVES == 1 and USER_GUESS != RANDOM_NUMBER:
        print(f'The number was {RANDOM_NUMBER}')
        print('You ran out of guesses. You lose!')

elif difficulty == 'medium':
    LIVES = 7
    lives_left = print(f'You have {LIVES} lives left')
    USER_GUESS = int(input('Make a guess: '))

    while USER_GUESS != RANDOM_NUMBER and LIVES > 1:
        value_checker()

    if USER_GUESS == RANDOM_NUMBER:
        print(f'Correct! The number was {RANDOM_NUMBER}. ')
        print(f'You had {LIVES} lives remaining.')
    elif LIVES == 1 and USER_GUESS != RANDOM_NUMBER:
        print(f'The number was {RANDOM_NUMBER}')
        print('You ran out of guesses. You lose!')

elif difficulty == 'hard':
    LIVES = 5
    lives_left = print(f'You have {LIVES} lives left')
    USER_GUESS = int(input('Make a guess: '))

    while USER_GUESS != RANDOM_NUMBER and LIVES > 1:
        value_checker()

    if USER_GUESS == RANDOM_NUMBER:
        print(f'Correct! The number was {RANDOM_NUMBER}. ')
        print(f'You had {LIVES} lives remaining.')
    elif LIVES == 1 and USER_GUESS != RANDOM_NUMBER:
        print(f'The number was {RANDOM_NUMBER}')
        print('You ran out of guesses. You lose!')

else:
    print('Invalid choice! Try again!')