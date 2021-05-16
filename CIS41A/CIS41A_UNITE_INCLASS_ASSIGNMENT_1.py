"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit E In-Class Assignment
"""

# Unit E
# This assignment has two scripts, the second with two parts.
#
# All print output should include descriptions as shown in the example output below.

# First Script
# 1) Determining the genre of a movie.
# Create a list called scifi that contains the elements Alien, Solaris, Inception, Moon.
# Create a list called comedy that contains the elements Borat, Idiocracy, Superbad, Bridesmaids.
# Ask the user for the name of a movie.
# Using if/elif/else, determine and print the genre of the movie.
# Test three times: first with Moon, then Superbad, then Dunkirk.
# Example output from the three tests:
#
# Please enter a movie title: Moon
# Moon is a scifi movie.
# Please enter a movie title: Superbad
# Superbad is a comedy movie.
# Please enter a movie title: Dunkirk
# Sorry, I don't know what kind of movie Dunkirk is.

scifi = ["Alien", "Solaris", "Inception", "Moon"]
comedy = ["Borat", "Idiocracy", "Superbad", "Bridesmaids"]
user_input = input("Please enter a movie title: ")
if user_input in scifi:
    print(f"{user_input} is a scifi movie.")
elif user_input in comedy:
    print(f"{user_input} is a comedy movie.")
else:
    print(f"sorry, I don't know what kind of movie {user_input} is.")


"""
Execution results:

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITE_INCLASS_ASSIGNMENT_1.py
Please enter a movie title: Moon
Moon is a scifi movie.

Process finished with exit code 0

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITE_INCLASS_ASSIGNMENT_1.py
Please enter a movie title: Superbad
Superbad is a comedy movie.

Process finished with exit code 0

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITE_INCLASS_ASSIGNMENT_1.py
Please enter a movie title: Dunkirk
sorry, I don't know what kind of movie Dunkirk is.

Process finished with exit code 0
"""