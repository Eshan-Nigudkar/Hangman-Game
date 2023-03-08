from replit import clear
import random


#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)



#Create blanks
display = []
for _ in range(word_length):
  display += "_"
print(f"{' '.join(display)}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    
    if guess in display:
      print(f"You have already guessed {guess}. Please try another letter.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
      print(f"You have guessed {guess}.That's a wrong guess.You just lost a live. Please try again.")
        
      lives -= 1
      if lives == 0:
          end_of_game = True
          print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    from hangman_art import stages
    print(stages[lives])