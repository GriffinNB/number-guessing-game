"""
Treehouse Techdegree - Data Analysis
Project 1 - Number Guessing Game
Griffin Novetsky
"""

import random
from statistics import mean, median, mode
scores = []

def stats():
  score_mean = mean(scores)
  score_median = median(scores)
  score_mode = mode(scores)
  print(f"Attempt Average: {score_mean}")
  print(f"Attempt Median: {score_median}")
  print(f"Attempt Mode: {score_mode}")
  print(f"Best Score: {min(scores)}")


def start_game():

    attempts = 0
    guess = 0

    
    print("Welcome to the Number Guessing Game!\nPlease guess a number between 1 and 100")
    if scores >= [0]:
      print(f"Score to beat: {min(scores)}")
    else:
      print("Be the first high-score!")
    random_number = random.randint(1,100)

    
    while True:
      
      try:
        guess = int(input("Type your guess:   "))
        attempts += 1
        if guess > 100 or guess < 1:
          raise ValueError("guess has to be a number between 1 and 100")
      except ValueError as err:
        print("Oop! Not a valid answer. Try again")    
      
      else:
        if guess == random_number:
          print("\nGot it!")
          break
        elif guess > random_number:
          print("It's Lower")
        elif guess < random_number:
          print("It's Higher")
    scores.append(attempts)
    print(f"You guessed it in {attempts} attempts")
    stats()

    
    new_game = input("Play again?  (Y/N)   ").upper()  
    if new_game == "Y":
      start_game()
    elif new_game == "N":
      print("Thanks for playing the Number Guessing Game!")



start_game()