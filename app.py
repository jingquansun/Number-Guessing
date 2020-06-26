"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

def high_score(current, new):
  if new <= current:
    return new
  else:
    return current

def start_game():
  current_highscore = 10
  while True:
    answer = random.randint(1, 10)
    
    guess = get_user_answer("Hello! Welcome to the guessing game. The current high score is {}. Please guess a number between 1 and 10:   ".format(current_highscore))
    
    tries = 1
    while guess != answer:
      if guess > 10 or guess < 1:
        guess = get_user_answer("This is not a valid number. The number is between 1 and 10, please guess again:   ")
        tries += 1
      if guess > answer:
        guess = get_user_answer("It's lower! Please guess again:   ")
        tries += 1
      elif guess < answer:
        guess = get_user_answer("It's higher! Please guess again:   ")
        tries += 1
        
    current_highscore = high_score(current_highscore, tries)
    print("You got it! It took you {} tries!".format(tries))
    restart = input("The current high score is {}! The game is over, would you like to play again?\nYes/No:  ".format(current_highscore))
    if restart.lower() == "yes":
      continue
    else:
      print("Thanks for playing!")
      break
        
        
def get_user_answer(input_phrase):
    guess = input(input_phrase)
    while True:
      try:
        guess = int(guess) 
      except ValueError:
        guess = input("This is an invalid input. Please guess between 1 and 10 using integers:   ")
      else:
        return guess
        break
    
start_game()
