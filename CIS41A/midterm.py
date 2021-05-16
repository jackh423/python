# # Midterm Questions and Answers
#
# # Question 1    10 pts
# # 1a) Write a line of code to get an int from the user and assign it to variable x.
#
# x = int(input("Please enter an integer: "))
#
# # Question 2        10 pts
# # 1b) Print the square root of the user’s number, rounded to two decimal places.
# import math
# import copy
#
# print(f"square root of {x} is {math.sqrt(x):.2f}")
#
# # Question 3        6 pts
# # 2) Given that var1 = "python":
# #
# # 2a) Write a line of code to print the length of var1.
# var1 = "python"
# print(len(var1))
#
# # Question 4        10 pts
# # 2b) Write a line of code to assign to variable x the letters "th" from var1 by slicing.
# x = var1[2:4]
# print(x)
#
# # Question 5        8 pts
# # 2c) Write a line of code to assign to variable y the letter "h" from var1 by using it’s index.
# y = var1[3]
# print(y)
#
# # Question 6        16 pts
# # 3) Given that x contains a number:
# #
# # Write a line of code to print x, formatted as follows:
# #
# # Field width is 8
# #
# # Right-aligned
# #
# # Show 2 decimal places
# x = 10
# print(f"{x:>8.2f}")
#
#
# # Question7     3pts
# # 4) Given that list1 = [5, 7, 3]:
#
# # 4a) Should you use sort or sorted to sort list1 in place?
# #
# # sort
# #
# # sorted
#
# # Question 8:       3 pts
# # 4b) Should you use sort or sorted to create a new sorted list from list1?
# # sort
# #
# # sorted
#
#
# # Question 9        6 pts
# # 5) Given that list1 = [1, 2, 3, 4]
# #
# # 5a) Write a line of code to print the maximum value from list1.
# list1 = [1, 2, 3, 4]
# print(max(list1))
#
# # Question 10   10 pts
# # 5b) Write a line of code to assign to variable x the value 3 from list1 while simultaneously deleting the value 3 from list1.
#
# x = list1.pop(2)
#
#
# # Question 11       3 pts
# # 6) Given the following code:
# list1 = [1, 2, 3]
# list2 = list1
# # 6a) Does the code list1 == list2 produce True or False?
# # True
# #
# # False
#
# # Question 12  3 pts
# # 6b) Does the code list1 is (list2) produce True or False?
# #
# # True
# #
# # False
#
# # Question 13       3 pts
# # 7) Given the following code:
#
# # import copy
# list1 = [1, 2, 3]
#
# list2 = copy.deepcopy(list1)
# # 7a) Does the code list1 == list2 produce True or False?
# # True
# #
# # False
#
# # Question 14
# # 7b) Does the code list1 is(list2) produce True or False?
# #
# # True
# #
# # False
#
# # Question 15
# # 8) Given the following code:
# list1 = [1, 2, 3]
#
# list2 = list1
#
# list3 = [list1, list2]
# # 8a) What is the value of list3[0][1]?
#
# # Question 16
# # 8b) What is the value of list3[1][0]?

# import math
# x = int(input("Please enter an integer: "))
# print(f"square oot of {x} is {math.sqrt(x):.2f}")

# var1 = "python"
# print(len(var1))
#
# x = var1[2:4]
# print(x)
# y = var1[3]
# print(y)

# 3) Given that x contains a number:
#
# Write a line of code to print x, formatted as follows:
#
# Field width is 8
#
# Right-aligned
#
# Show 2 decimal places

# x = 120
# print(f"{x:>8.2f}")
# print(f"{x:>9.2f}")
#
#
# list1 = [1, 2, 3, 4]
#
# x = list1.pop(2)
# print(x)
# print(list1)
#
# list1 = [1, 2, 3]
# list2 = list1
# print(list1 == list2)
# print(list1 is  (list2))

# import copy
#
# list1 = [1, 2, 3]
#
# list2 = copy.deepcopy(list1)
#
# print(list1 == list2)
#
list1 = [1, 2, 3]

list2 = list1

list3 = [list1, list2]
print(list3[0][1])
print(list3[1][0])
