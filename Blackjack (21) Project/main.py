from art import logo
from replit import clear
import random

print(logo)

game_complete = False

want_to_play = input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no. ")

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def display_user_cards(cards, sum):
  print(f"Your cards: {cards}, current score: {sum}")

def display_computer_cards(cards, sum):
  print(f"Computer cards: {cards}, Computer score: {sum}")

def turn(player, cards, ssum, display):
  global want_to_play
  global game_complete
  cards.append(deal_cards())
  ssum = sum(cards)
  
  if ssum > 21:
    if 11 in cards:
      ssum -= 10
      cards[cards.index(11)] = 1
      display(cards, ssum)
      return ssum
    else:
      display(cards, ssum)
      if player:
        print("You lose lul")
      else:
        print("You win")
      want_to_play = input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no. ")
      game_complete = True
      return ssum
  elif ssum == 21:
    display(cards, ssum)
    if not player:
        print("You lose lul")
    else:
        print("You win")
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no. ")
    game_complete = True
    return ssum
  display(cards, ssum)
  return ssum

while want_to_play == 'y':
  clear()
  game_complete = False
  
  user_cards = []
  computer_cards = []
  
  for i in range(0,2):
      user_cards.append(deal_cards())
      computer_cards.append(deal_cards())
  print(user_cards)
  user_sum = sum(user_cards)
  computer_sum = sum(computer_cards)
  
  print(f"Your cards: {user_cards}, current score: {user_sum}")
  print(f"Computer's first card: {computer_cards[0]}")
  go_again = input("Would you like to draw another card? Type 'y' for yes or 'n' for no.")
  
  while user_sum < 21 and go_again == 'y' and not game_complete:
    user_sum = turn(True, user_cards, user_sum, display_user_cards)
    go_again = input("Would you like to draw another card? Type 'y' for yes or 'n' for no.")
  
  while computer_sum < 17 and not game_complete:
    computer_sum = turn(False, computer_cards, computer_sum, display_computer_cards)
  
  if not game_complete:
    if computer_sum > 21 or user_sum > computer_sum:
      print("You win lul")
    else:
      if len(computer_cards) == 2: 
        print(f"Computer cards: {computer_cards}, computer score: {computer_sum}")
      if computer_sum == user_sum:
        print("You tie")
      else:
        print("You lose")
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no. ")