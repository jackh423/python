"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit H In-Class Assignment

"""


class StateData(object):
    def __init__(self, name, abbreviation, region, population):
        self.name = name
        self.abbreviation = abbreviation
        self.region = region
        self. population = population

    def __str__(self):
        return self.name

    def displayState(self):
        print(f"{self.name} ({self.abbreviation}) is in the {self.region} region and has population of {self.population}")


class StateData2(object):
    def __init__(self, name):
        self.name = name
        self.region = ""
        self.pop = ""

    def setRegion(self, region):
        self.region = region

    def getRegion(self):
        return self.region


class StateData3(object):
    def __init__(self, ):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"


def main():
    s1 = StateData("California", "CA", "West", 39250000)

    print(s1)
    s1.displayState()
    print()
    s2 = StateData2("California")
    s2.setRegion("West")
    s2.pop = 39250000
    print(s2.name)
    print(s2.getRegion())
    print(s2.region)
    print(s2.pop)
    print()

    test = StateData3()
    print(test.public)
    print(test._protected)
    print(test.__private)
    # If we need to access private variables (with double underscore, use below way
    # name mangling is the reason for the traceback error
    # print(test._StateData3__private)


if __name__ == "__main__":
    main()


"""
Execution results:
/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITH_INCLASS_ASSIGNMENT_1.py
California
California (CA) is in the West region and has population of 39250000

California
West
West
39250000

Public
Protected
Traceback (most recent call last):
  File "/Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITH_INCLASS_ASSIGNMENT_1.py", line 66, in <module>
    main()
  File "/Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITH_INCLASS_ASSIGNMENT_1.py", line 60, in main
    print(test.__private)
AttributeError: 'StateData3' object has no attribute '__private'

Process finished with exit code 1

"""