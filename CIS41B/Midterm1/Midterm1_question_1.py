# Write a Temperature class to hold the data, partially listed below, in a named tuple.
# The class should contain a constructor, a string conversion function.

"""
Test Result

/Users/jakkus/PycharmProjects/CIS41B/venv/bin/python /Users/jakkus/PycharmProjects/CIS41B/Midterm1_question_1.py
Temp: Temperature(Year=1850, Median=-0.373, Upper=-0.339, Lower=-0.425)
Temperature data: Temperature(Year=1850, Median=-0.373, Upper=-0.339, Lower=-0.425)
Temperature data: Temperature(Year=1850, Median=-0.373, Upper=-0.339, Lower=-0.425)

Process finished with exit code 0

"""
from collections import namedtuple

Temperature = namedtuple("Temperature", ["Year", "Median", "Upper", "Lower"])


class TemperatureClass:
    def __init__(self, year, median, upper, lower):
        self.temp = Temperature._make((year, median, upper, lower))
        pass

    def __str__(self):
        return f"Temperature data: {self.temp}"

    def __repr__(self):
        return f"Temp: {self.temp}"


if __name__ == "__main__":
    t = TemperatureClass(1850, -0.373, -0.339, -0.425)
    print(repr(t))
    print(str(t))
    print(t)