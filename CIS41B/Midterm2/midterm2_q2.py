"""
Name: Srinivas Jakkula
CIS 41B   Fall 2020
Lab MIDTERM 2
Execution results are at the end of this file.
"""
from bs4 import BeautifulSoup
import json

PAGE="Presidents.html"
presidents_dict = {}
with open(PAGE, "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    for tag in soup.find_all("tr")[1:]:
        presidents_dict[tag.text.strip().split(" ", 1)[0]] = tag.text.strip().split(" ", 1)[1].strip()
    print(presidents_dict)
    print(len(presidents_dict))

json_object = json.dumps(presidents_dict, indent=4)  # Writing to a python string variable
print(json_object)  # Printing json object

with open("dict_json.json", "w") as f:
    json.dump(presidents_dict, f, indent=4)  # Writing to a file

"""
OUTPUT:
/Users/jakkus/PycharmProjects/CIS41B/venv/bin/python /Users/jakkus/PycharmProjects/CIS41B/Midterm2/midterm2_q2.py
{'1': 'George Washington', '2': 'John Adams', '3': 'Thomas Jefferson', '4': 'James Madison', '5': 'James Monroe', '6': 'John Quincy Adams', '7': 'Andrew Jackson', '8': 'Martin Van Buren', '9': 'William Henry Harrison', '10': 'John Tyler', '11': 'James K. Polk', '12': 'Zachary Taylor', '13': 'Millard Fillmore', '14': 'Franklin Pierce', '15': 'James Buchanan', '16': 'Abraham Lincoln', '17': 'Andrew Johnson', '18': 'Ulysses S. Grant', '19': 'Rutherford B. Hayes', '20': 'James Garfield', '21': 'Chester Arthur', '22': 'Grover Cleveland', '23': 'Benjamin Harrison', '24': 'Grover Cleveland', '25': 'William McKinley', '26': 'Theodore Roosevelt', '27': 'William Howard Taft', '28': 'Woodrow Wilson', '29': 'Warren G. Harding', '30': 'Calvin Coolidge', '31': 'Herbert Hoover', '32': 'Franklin D. Roosevelt', '33': 'Harry S. Truman', '34': 'Dwight Eisenhower', '35': 'John F. Kennedy', '36': 'Lyndon B. Johnson', '37': 'Richard Nixon', '38': 'Gerald Ford', '39': 'Jimmy Carter', '40': 'Ronald Reagan', '41': 'George Bush', '42': 'Bill Clinton', '43': 'George W. Bush', '44': 'Barack Obama', '45': 'Donald Trump'}
45
{
    "1": "George Washington",
    "2": "John Adams",
    "3": "Thomas Jefferson",
    "4": "James Madison",
    "5": "James Monroe",
    "6": "John Quincy Adams",
    "7": "Andrew Jackson",
    "8": "Martin Van Buren",
    "9": "William Henry Harrison",
    "10": "John Tyler",
    "11": "James K. Polk",
    "12": "Zachary Taylor",
    "13": "Millard Fillmore",
    "14": "Franklin Pierce",
    "15": "James Buchanan",
    "16": "Abraham Lincoln",
    "17": "Andrew Johnson",
    "18": "Ulysses S. Grant",
    "19": "Rutherford B. Hayes",
    "20": "James Garfield",
    "21": "Chester Arthur",
    "22": "Grover Cleveland",
    "23": "Benjamin Harrison",
    "24": "Grover Cleveland",
    "25": "William McKinley",
    "26": "Theodore Roosevelt",
    "27": "William Howard Taft",
    "28": "Woodrow Wilson",
    "29": "Warren G. Harding",
    "30": "Calvin Coolidge",
    "31": "Herbert Hoover",
    "32": "Franklin D. Roosevelt",
    "33": "Harry S. Truman",
    "34": "Dwight Eisenhower",
    "35": "John F. Kennedy",
    "36": "Lyndon B. Johnson",
    "37": "Richard Nixon",
    "38": "Gerald Ford",
    "39": "Jimmy Carter",
    "40": "Ronald Reagan",
    "41": "George Bush",
    "42": "Bill Clinton",
    "43": "George W. Bush",
    "44": "Barack Obama",
    "45": "Donald Trump"
}

Process finished with exit code 0
"""