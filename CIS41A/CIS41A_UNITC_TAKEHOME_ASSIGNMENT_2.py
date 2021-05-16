"""
Name: Srinivas Jakkula
CIS 41A   Fall 2018
Unit C take-home assignment
"""

# Second Script – Bit Operators
# Assign the values 9 and 14 to variables a and b respectively.
# Print the binary values of a and b (use the bin built-in function).
# Calculate the value of a and b, print the result in binary.
# Calculate the value of a or b, print the result in binary.
# Examine the results. Can you see how they were arrived at?
# Example output:
#
# b) binary of a =  0b1001
# b) binary of b =  0b1110
# c) binary of a & b =  0b1000
# d) binary of a | b =  0b1111

a = 9
b = 14

print(f"binary of a = {a:#0b}")
print(f"binary of b = {b:#0b}")
print(f"binary of a  & b = {a & b:#0b}")
print(f"binary of a  | b = {a | b:#0b}")

"""
Execution results:

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITC_TAKEHOME_ASSIGNMENT_2.py
binary of a = 0b1001
binary of b = 0b1110
binary of a  & b = 0b1000
binary of a  | b = 0b1111

Process finished with exit code 0

"""