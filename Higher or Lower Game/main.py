from art import logo
from art import vs
from game_data import data
import os
import random

is_playing = True
score = 0


indexA = random.randint(0,54)
indexB = random.randint(0,54)

celebrityA = data[indexA]
celebrityB = data[indexB]
A = [celebrityA['name'], celebrityA['description'], celebrityA['country'], celebrityA['follower_count']]
B = [celebrityB['name'], celebrityB['description'], celebrityB['country'], celebrityB['follower_count']]

def clear_console():
  lambda: print('\n'*150)

def item_swapper():
  global B
  global A
  C = B
  A = C
  indexB2 = random.randint(0,54)
  if indexB2 != indexB and indexB2 != indexA:
    celebrityB2 = data[indexB2]
    B = [celebrityB2['name'], celebrityB2['description'], celebrityB2['country'], celebrityB2['follower_count']]
  else:
    item_swapper()
    
def game_function():
  print('Welcome to the Higher or Lower Game!')
  print('How far can you go?')
  print(logo)
  print(f'A: {A[0]}, a(n) {A[1]}, from {A[2]} ')  
  print(vs)
  print(f'B: {B[0]}, a(n) {B[1]}, from {B[2]}') 
  print("Who has more followers on Instagram? Type 'A' or 'B'. ")
  user_choice = input('Make a choice: ')
  
  if user_choice == 'A':
    if A[3] > B[3]:
      global score
      score += 1
      item_swapper()
      game_function()
    elif A[3] == B[3]:
      score += 1
      item_swapper()
      game_function()
    else:
      global is_playing
      is_playing = False
    
  elif user_choice == 'B':
    if B[3] > A[3]:
      score += 1
      item_swapper()
      game_function()
    elif B[3] == A[3]:
      score += 1
      item_swapper()
      game_function()
    else:
      is_playing = False
  else:
    is_playing = False


while is_playing == True:
  game_function()

clear_console()
print(logo)
print('Sorry, that is wrong.')
print(f'Your score: {score}')
print(f'{A[0]} has {A[3]} million followers and {B[0]} has {B[3]} million followers on Instagram.')

if score <= 4:
  print("You are straight mid.")

elif score > 4 and score <= 7:
  print('Not bad, could be better!')

elif score > 7 and score <= 10:
  print('Damn you are good at this!')

elif score > 10:
  print('WTF too cracked!')
