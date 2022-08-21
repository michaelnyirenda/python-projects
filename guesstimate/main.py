from logo import art
import random

easy = 10
hard = 5
print(art)

# function to select the difficulty of the game
def diff():
  diff = input("choose a difficulty. type 'easy' or 'hard': ")
  if diff == "easy":
    return easy
  else:
    return hard

# compares the guesses with the hidden number 
def compare(guess, num, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > num:
    print("too high")
    return turns - 1
  elif guess < num:
    print("too low")
    return turns - 1
  else:
    print(f"yessirkski! the answer was {num}")


def game():
  print("welcome to guesstimate \n the number guessing game")
  print("im thinking of a number between 1 and 100")
  num = random.randint(1, 100)
  
  
  turns = diff()
  
  guess = 0
  while guess != num:
    print(f"you have {turns} attempts remaining")
    guess = int(input("make a guess: "))
  
    turns = compare(guess, num, turns)
    if turns == 0:
      print("you are out of guesses, you lose")
      return
game()