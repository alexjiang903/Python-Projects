from eugeo import art
import os

def game_intro():
  print(art)
  print("Welcome to Treasure Island.")
  print("Your mission is to find the treasure.") 

def invalid_choice():
  print("You chose something that wasn't an option. Try again. (learn to type lol)")

def want_to_play_again():
  play_again = input("Would you like to go again? Type 'y' for yes or 'n' for no.")
  if play_again == 'y':
    os.system('cls' if os.name=='nt' else 'clear')
    game()
    
def game():
  game_intro()
  crossroad_input = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right' \n").lower()
  if crossroad_input == 'left':
    swim_or_boat = input("You've come to a lake. There is an island in the middle of the lake with a canoe on the shore. Type 'boat' to canoe across. Type 'swim' to swim across. \n").lower()
    if swim_or_boat == 'swim':
        print("You get attacked by an angry salmon and drown. Lbozo Game Over.")
        want_to_play_again()
    elif swim_or_boat == 'boat':
        house_select = input('You start canoeing and eventually arrive at the island unharmed. There is a house with 3 doors. One green, one black and one red. Which colour do you choose? \n').lower()
        if house_select == 'green':
          print("You walked into a room on fire. You get burned and die. Lbozo Game Over.")
          want_to_play_again()
        elif house_select == 'black':
          print("You enter a room with demons. You get eaten and die. Lbozo Game Over.")
          want_to_play_again()
        elif house_select == 'red':
          print("You found the treasure! You Win!")
          want_to_play_again()
        else:
          invalid_choice()
          want_to_play_again()
    
  elif crossroad_input == 'right':
    print("You fell into a hole. Lbozo Game Over.")
    want_to_play_again()
        
  else:
    invalid_choice()
    want_to_play_again()
game()