import random

def guess_number():

  answer = random.randint(1,100)
  print(f"Pssh. the answer i {answer}")
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  attempts = 0

  while True:
    guess = guess = int(input("Make your guess: "))
    attempts += 1

    if guess < answer:
      print("Too low! Try again")
    elif guess > answer:
      print("Too high! Try again")
    else:
      print(f"Congratulations! You've guessed the number {answer} correctly!")
      print(f"It took you {attempts} attempts to guess the number.")
      break

guess_number()