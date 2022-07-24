print('You will be playing Rock Paper Scissors against Kevin Kang today!')

import random

winner= ''

random_choice = random.randint(0,2)

if random_choice == 0:
    computer_choice = 'Rock'


elif random_choice == 1:
    computer_choice = 'Paper'

else:
    computer_choice = 'Scissors'

user_choice = ''
while (user_choice != 'Rock' and 
    user_choice != 'Paper' and
     user_choice != 'Scissors'):
    user_choice = input('Rock, Paper, or Scissors? ')

print('You chose', user_choice, 'and Kevin Kang chose', computer_choice)

if computer_choice == user_choice:
    winner = 'tie'

elif computer_choice == 'Paper' and user_choice == 'Rock':
    winner = 'Kevin Kang'


elif computer_choice == 'Scissors' and user_choice == 'Rock':
    winner = 'You'


elif computer_choice == 'Rock' and user_choice == 'Scissors':
    winner = 'Kevin Kang'

else:
    winner = 'You'

if winner == 'tie':
    print('You tied. gg.')

if winner == 'Kevin Kang':
    print('Oh no! You lost to Kevin! ggwp.')

if winner == 'You':
    print('YOU WON! GG EZZZZZ!!!')

