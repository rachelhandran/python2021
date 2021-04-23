""" Codecademy - Learn Python
Rock Paper Scissors """
from random import randint
options = ["ROCK", "PAPER", "SCISSORS"]
message = {"tie": "Yawn it's a tie!", "won": "Yay you won!", "lost": "Aww you lost!"}

def decide_winner(user_choice, computer_choice):
  print "%s" % user_choice
  print "%s" % computer_choice
  if user_choice == computer_choice:
    print message["tie"]
  elif user_choice == "ROCK" and computer_choice == "SCISSORS":
    print message["won"]
  elif user_choice == "SCISSORS" and computer_choice == "PAPER":
    print message["won"]
  elif user_choice == "PAPER" and computer_choice == "ROCK":
    print message["won"]
  else:
    print message["lost"]

def play_RPS():
  user_choice = raw_input("Enter Rock, Paper, or Scissors: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0,2)]
  decide_winner(user_choice, computer_choice)

play_RPS()

