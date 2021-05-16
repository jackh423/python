"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit E Take-Home Assignment

"""

# First Script – Decision Making
# Write a script that can determine where different plants can be planted.
#
# Each plant has a name, a type (Flower, Vegetable, Tree, etc.), and a maximum height.
# There are three gardens as follows:
#
# The Vegetable Garden can have only Vegetables, and there is no maximum height.
# The Low Garden can have only Flowers, and there is a maximum height of 3.
# The High Garden can have only Flowers, and there is a maximum height of 6.
# Print ONE line that identifies the one or more gardens that a given plant can be planted in. If a plant does not match the criteria for any of the gardens, then say so.
#
# Test the script six times with the following test data:
#
# Name: Lily, Type: Flower, Height 3
# Name: Bonsai, Type: Tree, Height 2
# Name: Carrots, Type: Vegetable, Height 1
# Name: Corn, Type: Vegetable, Height 8
# Name: Rose, Type: Flower, Height 5
# Name: Sunflower, Type: Flower, Height 8
# Example output:
#
# Please enter the plant name: Lily
# Please enter the plant type: Flower
# Please enter the plant height: 3
# A Lily can be planted in the Low Garden or the High Garden.

plant_name = input("Please enter the plant name: ")
plant_type = input("Please enter the plant type: ")
plant_height = int(input("Please enter the plant height: "))

if plant_type.lower() == "vegetable":
    print(f"{plant_name} can be planted in the Vegetable Garden")
elif plant_type.lower() == "flower" and plant_height <= 3:
    print(f"A {plant_name} can be planed in the Low Garden or High Garden")
elif plant_type.lower() == "flower" and plant_height > 3 and plant_height <= 6:
    print(f"A {plant_name} can be planted in High Garden")
else:
    print(f"A {plant_name} does not match the criteria for any of the gardens")





"""
Execution results:

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITE_TAKEHOME_ASSIGNMENT_1.py
Please enter the plant name: Lily
Please enter the plant type: Flower
Please enter the plant height: 3
A Lily can be planed in the Low Garden or High Garden

Process finished with exit code 0

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITE_TAKEHOME_ASSIGNMENT_1.py
Please enter the plant name: Bonsai
Please enter the plant type: Tree
Please enter the plant height: 2
A Bonsai does not match the criteria for any of the gardens

Process finished with exit code 0

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITE_TAKEHOME_ASSIGNMENT_1.py
Please enter the plant name: Carrots
Please enter the plant type: Vegetable
Please enter the plant height: 8
Carrots can be planted in the Vegetable Garden

Process finished with exit code 0

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITE_TAKEHOME_ASSIGNMENT_1.py
Please enter the plant name: corn
Please enter the plant type: Vegetable
Please enter the plant height: 8
corn can be planted in the Vegetable Garden

Process finished with exit code 0

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITE_TAKEHOME_ASSIGNMENT_1.py
Please enter the plant name: Rose
Please enter the plant type: Flower
Please enter the plant height: 5
A Rose can be planted in High Garden

Process finished with exit code 0

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITE_TAKEHOME_ASSIGNMENT_1.py
Please enter the plant name: Sunflower
Please enter the plant type: Flower
Please enter the plant height: 8
A Sunflower does not match the criteria for any of the gardens

Process finished with exit code 0 
"""