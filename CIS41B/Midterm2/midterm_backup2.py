# 1. Scrape, using BeautifulSoup, the local html page: Presidents.html.
# Scrape the term number and President name into a dictionary.
from bs4 import BeautifulSoup
import json

PAGE = "Presidents.html"
presidents_dict = {}
with open(PAGE, "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    for tag in soup.find_all("tr")[1:]:
        presidents_dict[tag.text.strip().split(" ", 1)[0]] = tag.text.strip().split(" ", 1)[1].strip()
    print(presidents_dict)
    print(len(presidents_dict))

# 2. Using your dictionary generated in question 1, convert the dictionary to a JSON string.
json_object = json.dumps(presidents_dict, indent=4)  # Writing to a python string variable
print(json_object)  # Printing json object

with open("dict_json.json", "w") as f:
    json.dump(presidents_dict, f, indent=4)  # Writing to a file

# 3. Using your SQLite insert function from either lab1, lab2 or lab3, insert the JSON string into your SQLite database.

import sqlite3
import json


def insert_to_database():
    with open("dict_json.json", "r") as f1:
        data1 = json.load(f1)
        print(type(data))

    conn = sqlite3.connect('midterm2.db')
    c = conn.cursor()
    create_table_query = f"""CREATE TABLE IF NOT EXISTS presidents (
                                ID INTEGER PRIMARY KEY,
                                President TEXT);"""
    c.execute(create_table_query)
    conn.commit()

    sqlite_insert_blob_query = f""" INSERT INTO presidents (ID, President) VALUES (?, ?)"""
    for k1, v1 in data1.items():
        c.execute(sqlite_insert_blob_query, (k1, v1))
        conn.commit()

    conn.close()


insert_to_database()

# 4. Show how to put the function defined in question #3 on a thread.

# 5. Convert the JSON string from question #2 to an XML file.
import json as JS
import xml.etree.ElementTree as ET

with open("dict_json.json", "r") as json_file:
    data = JS.load(json_file)

# print(data)
# print(type(data))
# import xml.etree.cElementTree as ET

root = ET.Element("root")
for k, v in data.items():
    # print(k, v)
    # print(type(v), type(k))
    ET.SubElement(root, k).text = v

tree = ET.ElementTree(root)
tree.write("Presidents.xml")
# Maths = ET.SubElement(root, "Number")
# tree = ET.ElementTree(root)
# tree.write("Presidents.xml")

# import BeautifulSoup
# f = open(PAGE)
# soup = BeautifulSoup(f)
# f.close()
# g = open('a.xml', 'w')
# print >> g, soup.prettify()
# g.close()