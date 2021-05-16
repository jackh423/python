"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit E Take-Home Assignment

"""

# Second Script – Guessing Game
# Write a script that plays a simple guessing game.
# The script will generate a secret number from 1 to 100, inclusive, and the user will have to guess the number.
# After each guess, the script will tell the user if they are high, low, or correct.
# If they are correct, the script will congratulate the user, tell them how many guesses they took, and then end the script.
# Hint: most of the game code will be in a loop that repeats until the correct number is guessed.
# To generate the secret number, you will need to use the randint function from Python's Random module, as follows:
# import random
#
# #this generates a random int from 1-100, inclusive
# secretNum = random.randint(1,100)
# Example output:
#
# Welcome to the guessing game.
# You need to guess a number from 1 to 100.
# What is your guess? 50
# Guess is too low.
# What is your guess? 75
# Guess is too low.
# What is your guess? 87
# Guess is too high.
# What is your guess? 81
# Guess is too low.
# What is your guess? 84
# Guess is too low.
# What is your guess? 85
# Congratulations!
# You guessed the secret number in 6 guesses!

import random

secretNum = random.randint(1,101)
print("Welcome to the guessing game")
print("You need to guess a number from 1 to 100.")
count = 0
while True:
    num = int(input("What is your guess? "))
    count += 1
    if num > secretNum:
        print("Guess is too high")
    elif num < secretNum:
        print("Guess is too low")
    elif num == secretNum:
        print("Congratulations!")
        break
print(f"You guessed the secret number in {count} guesses!")
print("You guessed the secret number in {} guesses!".format(count))



"""
Execution results:

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITE_TAKEHOME_ASSIGNMENT_2.py
Welcome to the guessing game
You need to guess a number from 1 to 100.
What is your guess? 50
Guess is too high
What is your guess? 30
Guess is too low
What is your guess? 40
Guess is too low
What is your guess? 45
Guess is too high
What is your guess? 44
Guess is too high
What is your guess? 41
Guess is too low
What is your guess? 42
Congratulations!
You guessed the secret number in 7 guesses!

Process finished with exit code 0
"""