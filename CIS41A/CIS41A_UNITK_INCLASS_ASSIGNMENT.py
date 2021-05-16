"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit K In-Class Assignment

"""

# Unit K
# This assignment consists of one part.
# Part 1 of 1 – Generating Unique Random Numbers
# Generate ten random but unique numbers that range from 1 to 15 inclusive.
# Print the sorted numbers.
#
# Hint: Use one of the methods from Python’s random module.
#
# Optional Challenge: Do this with one line of code.
#
# Sample Execution Results:
#
# [2, 4, 6, 7, 8, 9, 11, 12, 13, 15]


import random
random_list = []
while len(random_list) < 10:
    r = random.randrange(1, 16)
    if r not in random_list: random_list.append(r)
random_list.sort()
print(random_list)

# Second method single line solution
r_list = sorted(random.sample(range(1, 16), 10))
print(r_list)

"""
Execution results:

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITK_INCLASS_ASSIGNMENT.py
[1, 2, 4, 6, 9, 10, 11, 12, 13, 14]
[2, 3, 4, 7, 8, 9, 10, 11, 12, 14]

Process finished with exit code 0


"""