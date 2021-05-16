# 1)  Given that you have function f that accepts a kwargs argument and does not have a return. You also have a variable d that has been assigned a dictionary, write a line of code that passes variable d to function f (you don't need to write function f).
# f(**d)

# 2a)  Complete the following code to build the states dictionary.  The USPresidents.txt file has a number of lines of data, with each line containing two pieces of data: a two letter state abbreviation and the name of a president born in that state.  The dictionary keys should be the state abbreviation and the dictionary values should be a count of how many presidents were born in that state (this is just like one of your lab exercises).  Only build the one dictionary – don't build any lists, etc.

# states = {}
#
# file = open("USPresidents.txt", "r")
#
# for line in file:
#     (state_name, president_name) = line.split()
#     states[state_name] = states.get(state_name, 0) + 1
#
# file.close()
#
# for k, v in states.items():
#     print(f"State Abbr: {k}  No of Presidents: {v}")

# 3a)  Write a complete Square class.  It should have an __init__ method and a getArea method.
# The __init__ method should accept side (the length of the side of the square) as a parameter.

# class Square(object):
#     def __init__(self, side):
#         self.side = side
#
#     def getArea(self):
#         return self.side * self.side
#
#
# class Cube(Square):
#     def __init(self, side):
#         Square.__init__(side)
#
#     def getVoluem(self):
#         return self.getArea() * self.side
#
# s1 = Square(5)
# print(s1.getArea())
#
# c1 = Cube(5)
# print(c1.getVoluem())
#
#
# myLists = []
#
# for row in range(1,6,2):
#
#     newRow = []
#
#     for col in range(1,6,2):
#
#         newRow.append(row*col**2)
#
#     myLists.append(newRow)
#
# print(myLists[0][1])
#

# 6)  Write a function called calcTotal.  It should have a required parameter called price and
#     an optional parameter called taxRate with a default value of 0.08.
#     The function should return the total price including the calculated tax.
#
# def calcTotal(price, taxRate=0.08):
#     tax = price * taxRate
#     total_price = price + tax
#     return total_price, tax
#
#
# print(calcTotal(100))

# Question 15 pts
# 1)  Given that you have function f that accepts a kwargs argument and does not have a return.
# You also have a variable d that has been assigned a dictionary, write a line of code that passes
# variable d to function f (you don't need to write function f).

# f(**d)


# Question 218 pts
#
# 2a)  Complete the following code to build the states dictionary.
# The USPresidents.txt file has a number of lines of data, with each line containing
# two pieces of data: a two letter state abbreviation and the name of a president born in that state.
# The dictionary keys should be the state abbreviation and the dictionary values should be a count of
# how many presidents were born in that state (this is just like one of your lab exercises).
# Only build the one dictionary – don't build any lists, etc.
#
# states = {}
#
# file = open("USPresidents.txt", "r")
#
# for line in file:
#
# 2b)  Iterate through the states dictionary to print the key and value for each item in the dictionary.


# states = {}
# file = open("USPresidents.txt", "r")
#
# for line in file:
#     state_name, president_name = line.split()
#     states[state_name] = states.get(state_name, 0) + 1
#
# file.close()
#
# for k, v in states.items():
#     print(f"State Abbr: {k}  No of Presidents: {v}")

# 3a)  Write a complete Square class.  It should have an __init__ method and a getArea method.
# The __init__ method should accept side (the length of the side of the square) as a parameter.

# 3b)  Write a complete Cube class.  It should inherit from the Square class and should have an __init__ method
# and a getVolume method.  The __init__ method should accept side as a parameter.

# 3c)  Initialize variable s with a square object with a side of 3.

# 3d)  Print the area of square s.

# 3e)  Initialize variable c with a cube object with a side of 4.

# 3f)  Print the volume of cube c.
#
#
# class Square(object):
#     def __init__(self, side):
#         self.side = side
#
#     def getArea(self):
#         return self.side * self.side
#
#
# class Cube(Square):
#     def __init(self, side):
#         Square.__init__(side)
#
#     def getVoluem(self):
#         return self.getArea() * self.side
#
#
# s = Square(3)
# print(s.getArea())
#
# c = Cube(4)
# print(c.getVoluem())


# 4a)  Given that you have a Liquid class that can be initialized with any amount of gallons,
# liters, ounces, etc, write the first line of the method that will allow you to add together
# two Liquid objects using operator overloading.  Again, write ONLY the first line (method definition) –
# you do NOT have to write the entire method.

# def __add__(self, other):

# 4b)  Given that you have L1 and L2 which are instances of the Liquid class, write a line of code that uses operator
# overloading  to add them together and assign the result to L3.
# L1 = ""
# L2 = "A"
# L3 = L1 + L2

# 5)  Given the following code, what prints?
#
# myLists = []
# for row in range(1, 6, 2):
#     newRow = []
#     for col in range(1, 6, 2):
#         newRow.append(row * col ** 2)
#     myLists.append(newRow)
#
# for e in myLists:
#     print(e)
#
# print(myLists[0][1])

# 6)  Write a function called calcTotal.  It should have a required parameter called price and an optional parameter
# called taxRate with a default value of 0.08.  The function should return the total price including the calculated tax.


# def calcTotal(price, taxRate=0.08):
#     tax = price * taxRate
#     total_price = price + tax
#     return total_price

# # If you want to return both total price and tax then following code needs to be used
def calcTotal(price, taxRate=0.08):
    tax = price * taxRate
    total_price = price + tax
    return total_price, tax


print(calcTotal(100, 0.08))
print(calcTotal(100))
