"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit G In-Class Assignment

"""

# Part One – Working with Files
# Create a new file called ZenOfPython.txt and write the first two lines of the Zen of Python (see The Zen of Python) to the file. Close the file.
#
# Reopen the file and append the 7th and the 17th lines. Then close the file.
#
# Open the file again and read and print the entire contents of the file (there shouldn't be any blank lines between the text).
# Then close the file.
#
# Sample Execution Results:
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Readability counts.
# If the implementation is hard to explain, it's a bad idea.
# Part Two – CSV Files
# For this exercise, you will need to download the file Cities.csv from Canvas and save it into the same directory as your Python script. To do this, login to Canvas, select CIS 41A, select Files, select Cities.csv, select Download, and save into the same directory with your unit G in-class Python script.
#
# The file contains a list of cities, their state, and their population. The file starts with a header row of field names, which are City, State, Population.
#
# You will need to save this data (but not the header data) into a dictionary. The dictionary key will be a tuple consisting of the name of the city and the name of the state. The dictionary value will be the population.
# The reason for this structure is that there are a number of duplicate city names within the file, but no duplicate city/state pairs.
#
# Hint: When you create your reader object, you should use the DictReader from the csv module. Because the file contains a header row of field names, we don’t have to explicitly define them when creating the reader object. However, you should use these field names instead of numerical indexes when working with the row data.
#
# After reading the csv file, iterate through the dictionary and print the data.
#
# Then, ask the user for a city and state, then print that city’s population, if it exists.
# Test with Dublin, California.
#
# Sample Execution Results:
#
# Athens Georgia 115452
# Athens Ohio 23832
# Berlin Connecticut 19866
# Berlin Wisconsin 5524
# Dublin California 46036
# Dublin Ohio 41751
# and so on...
#
# Please enter a city: Dublin
# Please enter a state: California
# Dublin California has a population of 46036

# import this
import csv

def section1():
    # with open("ZenOfPython.txt", 'w') as file1:
    #     file1.write("Beautiful is better than ugly.")
    #     file1.write("Explicit is better than implicit.")

    file1 = open("ZenOfPython.txt", 'w')
    file1.write("Beautiful is better than ugly.\n")
    file1.write("Explicit is better than implicit.\n")
    file1.close()

    file1 = open("ZenOfPython.txt", 'a')
    file1.write("Readability counts.\n")
    file1.write("If the implementation is hard to explain, it's a bad idea.")
    file1.close()

    file1 = open("ZenOfPython.txt", "r")
    print(file1.read())
    file1.close()


def section2():
    with open("Cities.csv", "rt") as file:
        cities_pop = csv.DictReader(file)
        cities_dict = {}

        for row in cities_pop:
            # print(row['City'])
            cities_dict[(row['City'], row['State'])] = row['Population']

        for k, v in cities_dict.items():
            print(k[0], k[1], v)

        city = input("Please enter a city: ")
        state = input("Please enter a state: ")

        for k, v in cities_dict.items():
            # print(k[0], k[1], city, state)
            if k[0] == city and k[1] == state:
                print(f"{city} {state} has a population of {v}")


def main():
    section1()
    print()
    section2()


if __name__ == "__main__":
    main()

"""
Execution results:

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITG_INCLASS_ASSIGNMENT.py
Beautiful is better than ugly.
Explicit is better than implicit.
Readability counts.
If the implementation is hard to explain, it's a bad idea.

Athens Georgia 115452
Athens Ohio 23832
Berlin Connecticut 19866
Berlin Wisconsin 5524
Dublin California 46036
Dublin Ohio 41751
Glasgow Connecticut 11951
Glasgow Kentucky 14028
London Kentucky 7993
London Ohio 9904
Milan Illinois 5099
Milan Michigan 5836
Milan Tennessee 7851
Paris Kentucky 8553
Paris Tennessee 10156
Paris Texas 25171
Warsaw Indiana 13559
Warsaw New York 5064
Please enter a city: Dublin
Please enter a state: California
Dublin California has a population of 46036

Process finished with exit code 0

"""