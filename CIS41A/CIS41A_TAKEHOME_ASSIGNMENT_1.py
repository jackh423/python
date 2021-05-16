"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit E Take-Home Assignment

"""
#
# This assignment has one script with three parts.
# All print output should include descriptions as shown in the example output below.
# Part One – Keyword Arguments and Default Values
# Write an invoice function.
# The function will generate a simple invoice and will have two required arguments and two keyword arguments.
# The two required arguments are unitPrice and quantity.
# The first keyword argument is shipping, and it has a default value of 10.
# The second keyword argument is handling, and it has a default value of 5.
# Test it twice from main:
# First test: unitPrice 20, quantity 4, and shipping 8 (handling is not specified).
# Second test: unitPrice 15, quantity 3, and handling 15 (shipping is not specified).
# Don't worry about making the formatting pretty.
# Part Two – args (Variable-Length Arguments)
# Write a printGroupMembers function.
# The function prints a list of students who are working together on a group project, as well as the group name.
# The function has one required argument, the group name, and one variable-length argument that contains the student names.
# Test it twice from main:
# First test: Call as follows:
# printGroupMembers("Group A", "Li", "Audry", "Jia")
# Second test: Create a list as follows:
# groupB = ["Group B", "Sasha", "Migel", "Tanya", "Hiroto"]
# and then call the function using this list.
# Part Three – Non-Rectangular (Ragged) 2D lists
# Write two functions that will build and display a Bell triangle - see: What is a Bell triangle
# A Bell triangle can be constructed as follows:
#
# The first row has a single element which has the value 1.
# For the second row and all subsequent rows:
# The number of elements in a row is equal to the number of elements in the previous row + 1.
# The first element in the row is equal to the last element of the previous row.
# The second through nth elements of a row are calculated by adding the value of the previous element (n-1) in the current row to the (n-1) element of the previous row.
# As an example of this calculation, start by looking at the triangle shown below. To calculate the 3rd (n=3) element of the 4th row, we add the 2nd (3-1=2) element of the 4th row (7) to the 2nd (3-1=2) element of the 3rd row (3), with the total being 10 (7+3=10).
#
# The first function should be called buildBell. It has one argument, the number of rows, and returns a ragged table (a list of lists).
#
# The second function should be called printBell. It has one argument, a ragged table (a list of lists). Generate formatted output where each number is right justified within a fixed field size, so that the numbers in each column are aligned.
#
# Hint: The easiest way to format the numbers is probably by using the rjust string function.
#
# Test by calling buildBell from main to build a Bell triangle with 8 rows.
#
# Then call printBell from main to print the triangle.



"""
Execution results:

"""
