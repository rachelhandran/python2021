""" Codecademy - Learn Python
Number Guess
This program rolls a pair of dice, adds the values of the roll, prompts the user to guess a number, and compare the two numbers to determine the winner. """
from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Enter a number guess: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum value is %d." % max_val
  guess = get_user_guess()
  if guess > max_val:
    print "Guess exceeds maximum value."
  else:
    print "Rolling..."
    sleep(2)
    print "%d" % first_roll
    sleep(1)
    print "%d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print total_roll
    print "Result..."
    sleep(1)
    if guess == total_roll:
      print "You win!"
    else:
      print "You lost."

roll_dice(6)
