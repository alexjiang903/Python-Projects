from replit import clear
import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"
list_of_guesses = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    clear()
    
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter        
    list_of_guesses += guess
    if len(list_of_guesses) != len(set(list_of_guesses)):
      print('You guessed that letter already. Please guess a different letter.')
    
    if guess not in chosen_word:
        lives -= 1
        print(f'You chose {guess}, but that is not in the word. You lose a life!')
        if lives == 0:
            end_of_game = True
            print(f"You lose. The correct word was {chosen_word}")


    print(f"{' '.join(display)}")

  
    if "_" not in display:
        end_of_game = True
        print("You win.")

  
    print(hangman_art.stages[lives])