"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit A In-class Assignment
"""

height = 2.9
width = 7.1
area = height * width
print("{:8s} {:<}".format("height:", height))
print("{:8s} {:<}".format("width:", width))
print("{:8s} {:<}".format("area:", area))

height = height // 2
width = width // 2
area = height * width
print()
print("{:8s} {:<}".format("height:", height))
print("{:8s} {:<}".format("width:", width))
print("{:8s} {:<}".format("area:", area))

"""
Execution Results
/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITA_INCLASS_1.py
height:  2.9
width:   7.1
area:    20.59

height:  1.0
width:   3.0
area:    3.0

Process finished with exit code 0
"""