
from bs4 import BeautifulSoup
import sqlite3
import json
import json as JS
import xml.etree.ElementTree as ET
import threading

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


def insert_to_database():
    with open("dict_json.json", "r") as f1:
        data1 = json.load(f1)
        print(type(data1))

    conn = sqlite3.connect('midterm2.db')
    c = conn.cursor()
    create_table_query = f"""CREATE TABLE IF NOT EXISTS presidents (
                                ID INTEGER PRIMARY KEY,
                                President TEXT);"""
    c.execute(create_table_query)
    conn.commit()

    sqlite_insert_blob_query = f""" INSERT or REPLACE INTO presidents (ID, President) VALUES (?, ?)"""
    for k1, v1 in data1.items():
        c.execute(sqlite_insert_blob_query, (k1, v1))
        conn.commit()

    conn.close()


# insert_to_database()
thd1 = threading.Thread(target=insert_to_database)
thd1.start()
thd1.join()


with open("dict_json.json", "r") as json_file:
    data = JS.load(json_file)

root = ET.Element("root")

for k, v in data.items():
    ET.SubElement(root, k).text = v

tree = ET.ElementTree(root)
tree.write("Presidents.xml")
