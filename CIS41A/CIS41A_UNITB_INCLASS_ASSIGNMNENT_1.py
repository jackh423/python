"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit B In-class Assignment
"""

# String methods

# Ask the user for a name (test with George Washington).
# Print the name in all uppercase letters.
# Print the length of the name.
# Print the 4th character of the name (r).
# Create a variable called name2. Assign to name2 the name with all "o" characters replaced with "x"s.
# Print name2.
# Print the original name.

name = input("Please Enter a Name:  ")
print(name.upper())
print(len(name))
print(name[3])
name2 = name.replace('o', 'x')
print(name2)
print(name)

# Counting and Finding
#
# Assign the text "Believe you can and you're halfway there." to a variable called quote (this is a quote from Theodore Roosevelt).
# Count how many "a" characters there are, print the result.
# Print the index of all the "a" characters.
# Hint: Except for the first find, set the start location for the next find as the previous location found index + 1. The second argument in the find method is the index where the find starts looking.
# A fuller explanation of the find method is given in string-methods

# quote = "Believe you can and you're halfway there."
# print(quote.count('a'))
# print([i for i, ltr in enumerate(quote) if ltr == 'a'])

quote = "Believe you can and you're halfway there."
pos = 0
index_list = []
while pos <= len(quote):
    pos = quote.find('a', pos)
    if pos < 0:
        break
    index_list.append(pos)
    pos += 1
print(index_list)
"""
Execution Results
/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITB_INCLASS_ASSIGNMNENT_1.py
Please Enter a Name:  George Washington
GEORGE WASHINGTON
17
r
Gexrge Washingtxn
George Washington
4
[13, 16, 28, 32]

Process finished with exit code 0
"""
