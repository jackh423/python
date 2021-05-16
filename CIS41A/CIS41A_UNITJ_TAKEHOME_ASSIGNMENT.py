"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit J Take-Home Assignment
"""
import random


def roll_dice():
    return random.randint(1, 6)


def dice_gamble():
    amount_earned = 0
    while True:
        rolled = roll_dice()
        if rolled <= 3:
            return amount_earned
        else:
            amount_earned += rolled


def monte_carlo():
    sum_won = 0
    itr = 0
    max_won = 0
    while itr < 10000:
        amt_won = dice_gamble()
        sum_won += amt_won
        if amt_won > max_won:
            max_won = amt_won
        itr += 1
    return sum_won/10000, max_won


if __name__ == '__main__':
    avg_won, max_wn = monte_carlo()
    print(f"Average amount won = {avg_won:.2f}")
    print(f"Max amount won = {max_wn}")


"""
Q: Just as a thought experiment, would you pay $3 for a chance to play this game?
A: Yes, i would pay $3 for a chance to play this game.

"""
"""
Execution results:

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITJ_TAKEHOME_ASSIGNMENT.py
Average amount won = 4.92
Max amount won = 74

Process finished with exit code 0

"""