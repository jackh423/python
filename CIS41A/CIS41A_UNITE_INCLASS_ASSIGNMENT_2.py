"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit E In-Class Assignment
"""
# Second Script - two parts
# 1) Using range with a for loop.
# Use a for loop to print the even integers in descending order from 10 to 0 inclusive.
# 2) Looping through dictionary items.
# Create a dictionary named movies and populate it with these key value pairs:
# The Wizard of Oz:1939
# The Godfather:1972
# Lawrence of Arabia:1962
# Raging Bull:1980
# Loop through the dictionary items and print the year in which each movie was made. Output should be alpha sorted by movie title.
# Sample Execution Results:
#
# 10
# 8
# 6
# 4
# 2
# 0
# Lawrence of Arabia was made in 1962
# Raging Bull was made in 1980
# The Godfather was made in 1972
# The Wizard of Oz was made in 1939
for num in range(10, -1, -1):
    # print(num)
    if num % 2 == 0:
        print(num)

movies = {"The Wizard of Oz": 1939,
          "The Godfather": 1972,
          "Lawrence of Arabia": 1962,
          "Raging Bull": 1980}

for k, v in sorted(movies.items()):
    print(f"{k} was made in {v}")
"""
Execution results:

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITE_INCLASS_ASSIGNMENT_2.py
10
8
6
4
2
0
Lawrence of Arabia was made in 1962
Raging Bull was made in 1980
The Godfather was made in 1972
The Wizard of Oz was made in 1939

Process finished with exit code 0
"""