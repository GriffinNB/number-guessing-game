"""
Project 1 - Number Guessing Game
Griffin Novetsky
"""

import random



def start_game():

    number_of_guesses = 0

    
    # 1. Display an intro/welcome message to the player.
    print("Welcome to the Number Guessing Game!")
 
    # 2. Store a random number as the answer/solution.
    random_number = random.randint(1,100)

    # 3. Continuously prompt the player for a guess.
    guess = int(input("Guess a number between 1 and 100:   "))
    while guess != random_number:
      number_of_guesses += 1
      # a. If the guess greater than the solution, display to the player "It's lower".
      if guess > random_number:
        guess = int(input("It's Lower   "))
      # b. If the guess is less than the solution, display to the player "It's higher".
      elif guess < random_number:
        guess = int(input("It's Higher   "))
      
    # 4. Once the guess is correct, stop looping, inform the user they "Got it"
    number_of_guesses += 1
    print("Got it!")
         #and show how many attempts it took them to get the correct number.
    print(f"Number of Guesses: {number_of_guesses}")     
    # 5. Save their attempt number to a list.

    # 6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.
    # 7. Ask the player if they want to play again.

    
    # (add more features/enhancements if needed. )





start_game()