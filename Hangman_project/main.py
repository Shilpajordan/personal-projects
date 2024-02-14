
import random
from hangman_words import word_list
from hangman_art import logo,stages


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
#Testing code
print(logo)
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -=1
        if lives == 0:
          end_of_game = True
          print("You lose!")
    #Join all the elements in the list and turn it into a String.
    print(f"{' '. join(display)}")

    #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    
# print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.index similar to the livfe left
print(stages[lives])