"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit A Take-Home Assignment
"""
import math

# Calculate and print the final value of each variable.
#
# a equals 3 to the power of 2.5
# b equals 2 b equals b + 3 (use +=)
# c equals 12 c = c divided by 4 (use /=)
# d equals the remainder of 5 divided by 3

# Basic math and string operations
a = 3 ** 2.5
b = 2
b += 3
c = 12
c /= 4
d = 5 % 3

print(f"{'a equals:':10s}{a}")
print(f"{'b equals:':10s}{b}")
print(f"{'c equals:':10s}{c}")
print(f"{'d equals:':10s}{d}")
print()

# Built-in functions abs, round, and min
# Use abs, round, and min to calculate some values. These are all Python built in functions (see: BIF ).
#
# Print the difference between 5 and 7.
# Print 3.14159 rounded to 4 decimal places.
# Print 186282 rounded to the nearest hundred.
# Print the minimum of 6, -9, -3, 0

print(f"{abs(5 - 7)}")
print(f"{round(3.14159, 4)}")
# print(f"{int(math.ceil(186282/100.0))*100}")
print(f"{round(186282, -2)}")
print(f"{min(6, -9, -3, 0)}")
print()

# Functions from the math module
# Use some functions from Pythons math module to perform some calculations.
#
# Ask the user for a number (test with the value 7.6).
# Print the square root of the number, rounded to two decimal places (include an appropriate description).
# Print the base-10 log of the number, rounded to two decimal places (include an appropriate description)
# (see https://docs.python.org/3/library/math.html).

num = float(input("Please enter a number:   "))
print(f"Square root of {num} is {round(math.sqrt(num), 2)}")
print(f"base-10 log of {num} is {round(math.log10(num),2)}")
print()

# Complex numbers

# Do a calculation with complex numbers. Note that, while you might be familiar with the notation convention commonly used within mathematics for complex numbers (z = a + bi), Python uses the notation convention used in electromagnetism and electrical engineering (z = a + bj).
#
# Assign z1 the value of 4 + 3j
# Assign z2 the value of 2 + 2j
# Assign z3 the value of z1 times z2
# Print the value of z3

z1 = 4 + 3j
z2 = 2 + 2j
z3 = z1 + z2

print(f"z3 vale is: {z3}")



"""
Execution results:

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITA_TAKEHOME_1.py
a equals: 15.588457268119896
b equals: 5
c equals: 3.0
d equals: 2

2
3.1416
186300
-9

Please enter a number:   7.6
Square root of 7.6 is 2.76
base-10 log of 7.6 is 0.88

z3 vale is: (6+5j)

Process finished with exit code 0

"""
