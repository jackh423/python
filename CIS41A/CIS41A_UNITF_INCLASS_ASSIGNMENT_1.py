"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit F In-Class Assignment

"""

# Part One – Using a main function, Docstrings
# Write a function called hello. The function has no arguments and no return value.
# It simply prints the text "Hello World". Include a docstring that describes the function.
#
# Write a main function, as described by the Python main function reading.
#
# Call main, as described by the Python main function reading.
#
# From main, call hello and then print hello’s docstring.
#

# Part Two – Error Handling
# Write a function called printListElement. The function has two arguments and no return value.
# The first argument is a list, and the second argument is a list index.
# The function will print an element from the list as determined by the list index.
# If the list index is invalid, print an error message.
#
# We could accomplish this with a logic test, but instead, we will manage this with error handling.
#
# Write a try block that attempts to print the list element. Catch any errors with an except block,
# print an error message.
#
# From main, create a myList list with elements 0, 1, 2 by using the list and range commands.
#
# Then, call printListElement with your list and a list index value of 3.
#

# Part Three – How Python function arguments are treated
# There can be some confusion as to how Python functions treat their arguments -
# is it by reference or by value? Explore this for yourself.
#
# From main, create a myInt variable and give it the value 3. Also create a myList list with elements 0, 1, 2.
#
# Print the IDs of myInt and myList. Also print the ID of the last element of myList.
#
# Now create a function called byVal which has one argument.
# In the function, add 7 to the argument. Print the ID of the argument before and after the change.
#
# Create a second function called byRef which has one argument.
# In the function, add 7 to the last element in the list. Print the ID of the argument and
# the ID of the last element of the argument before and after the change.


def hello():
    """
    This function prints Hello world
    """
    print("Hello World")


def printListElement(mylist, index):
    """
    This function prints the element present in the index given
    If the index is invalid then it will print an error message.
    """
    try:
        print(mylist[index])
    except IndexError:
        print("Error: bad index number.")


def byVal(myVal):
    """
    This function adds value 7 to the input argument and prints the id of before adding and after adding
    """
    print(f"Original ID of parameter in byVal {id(myVal)}")
    myVal += 7
    print(f"ID of parameter in byVal after change  {id(myVal)}")


def byRef(mylist):
    """
    This funtion take a list as input and prints id of the list and last element and then added value 7
    to the last element of the list and then prints the id of list and last element.
    """
    print(f"Original ID of parameter in byRef {id(mylist)}")
    print(f"Original ID of parameter's last element in byRef {id(mylist[-1])}")
    mylist[-1] += 7
    print(f"ID of parameter in byRef after change {id(mylist)}")
    print(f"ID of parameter's last element in byRef after change {id(mylist[-1])}")


def main():
    """
    This is the main function to call other functions defined for testing this assignment
    """
    # Part 1 Solution
    hello()
    help(hello)
    # print(hello.__doc__)

    # Part 2 Solution
    myList = list()
    for ele in range(0,3):
        myList.append(ele)
    # print(myList)
    printListElement(myList, 3)
    print()

    # Part 3 Solution
    myInt = 3
    myList = [0, 1, 2]
    print(f"Original ID of myInt in main is {id(myInt)}")
    print(f"Original ID of myList in main is {id(myList)}")
    print(f"Original ID of myList's last element in main is {id(myList[-1])}")
    byVal(myInt)
    byRef(myList)
    print(f"ID of myInt in main after call to byVal is {id(myInt)}")
    print(f"ID of myList in main after call to byRef is {id(myList)}")
    print(f"ID of myList's last element in main after call to byRef is {id(myList[-1])}")
    print(f"myInt is now: {myInt}")
    print(f"myList is now: {myList}")


if __name__ == "__main__":
    main()

"""
In Python a variable is not an alias for a location in memory. Rather, it is simply a binding to a Python object.
In case of byVal function, we have passed a Integer object which is immutable and hence after adding 7 to the value, 
variable is pointing a different integer object whose value is 7.
In case of byRef function, we have passed a list object which is mutable and hence even after changing the last element 
of the list, the list object id is not changed. And last element of the list is an integer, which is immutable object. 
When we added 7 to last element of the list, list is pointing to another object 9 at last location.

Based on this:

A mutable object exhibits time-varying behavior. 
Changes to a mutable object are visible through all names bound to it. 
Python's lists are an example of mutable objects.
then these changes will be visible outside of the scope of the function

The value of immutable objects can not be modified after they are created. 
Pythons's integers are an example of immutable objects

"""

"""
Execution results:

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITF_INCLASS_ASSIGNMENT_1.py
Hello World
Help on function hello in module __main__:

hello()
    This function prints Hello world

Error: bad index number.

Original ID of myInt in main is 4327501552
Original ID of myList in main is 4333216136
Original ID of myList's last element in main is 4327501520
Original ID of parameter in byVal 4327501552
ID of parameter in byVal after change  4327501776
Original ID of parameter in byRef 4333216136
Original ID of parameter's last element in byRef 4327501520
ID of parameter in byRef after change 4333216136
ID of parameter's last element in byRef after change 4327501744
ID of myInt in main after call to byVal is 4327501552
ID of myList in main after call to byRef is 4333216136
ID of myList's last element in main after call to byRef is 4327501744
myInt is now: 3
myList is now: [0, 1, 9]

Process finished with exit code 0

"""