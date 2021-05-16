"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit I In-Class Assignment

"""
import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius * self.radius


class Cylinder(Circle):

    def __init__(self, radius, height):
        self.height = height
        super().__init__(radius)

    def getVolume(self):
        return self.getArea() * self.height


if __name__ == '__main__':
    c1 = Circle(4)
    print(f"Circle area is: {c1.getArea():.2f}")
    # print(f"Circle area is: {c1.getArea()}")
    cy2 = Cylinder(2, 5)
    print(f"Cylinder volume is: {cy2.getVolume():.2f}")
    # print(f"Cylinder volume is: {cy2.getVolume()}")

"""
Execution results:

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITI_INCLASS_ASSIGNMENT_1.py
Circle area is: 50.27
Cylinder volume is: 62.83

Process finished with exit code 0
"""

