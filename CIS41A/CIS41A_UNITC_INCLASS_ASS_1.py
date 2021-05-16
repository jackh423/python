'''
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit C In-class Assignment
'''

import copy

list1 = [2, 4.1, 'hello']

list2 = list1
# list3 = list(list1)
# list3 = list1.copy()
# list3 = list1[:]
list3 = copy.deepcopy(list1)

print("list1 == list2: ", list1 == list2)
print("list1 == list3: ", list1 == list3)
print("list2 == list3: ", list2 == list3)

print("list1 is list2: ", list1 is list2)
print("list1 is list3: ", list1 is list3)
print("list2 is list3: ", list2 is list3)

print("list1 ID", id(list1))
print("list2 ID", id(list2))
print("list3 ID", id(list3))

list1.append(8)
list2.insert(1, "goodbye")
list3.pop(0)

print("list1 printed: ", list1)
print("list2 printed: ", list2)
print("list3 printed: ", list3)

"""
The results do not match.
The reason for that is, list contains the reference of the elements. When we do deep copy,
it will create new object for every element and refers in newly created list.
"""

'''
Execution results:

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITC_INCLASS_ASS_1.py
list1 == list2:  True
list1 == list3:  True
list2 == list3:  True
list1 is list2:  True
list1 is list3:  False
list2 is list3:  False
list1 ID 4565334536
list2 ID 4565334536
list3 ID 4565334472
list1 printed:  [2, 'goodbye', 4.1, 'hello', 8]
list2 printed:  [2, 'goodbye', 4.1, 'hello', 8]
list3 printed:  [4.1, 'hello']

Process finished with exit code 0

'''