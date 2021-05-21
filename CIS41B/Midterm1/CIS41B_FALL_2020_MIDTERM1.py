#
# Write a Temperature class to hold the data, partially listed below, in a named tuple.
# The class should contain a constructor, a string conversion function.

# from collections import namedtuple
#
# Temperature = namedtuple("Temperature", ["Year", "Median", "Upper", "Lower"])
#
#
# class TemperatureClass:
#     def __init__(self, year, median, upper, lower):
#         self.temp = Temperature._make((year, median, upper, lower))
#         pass
#
#     def __str__(self):
#         return f"Temperature data: {self.temp}"
#
#     def __repr__(self):
#         return f"Temp: {self.temp}"
#
#     def __getitem__(self, year):
#         return self.temp
#
#
# if __name__ == "__main__":
#     t = TemperatureClass(1850, -0.373, -0.339, -0.425)
#     print(repr(t))
#     print(str(t))
#     print(t)

#
#
# Using your SQLite class, write a member function __getitem__ which returns the median data for a given year.
#

# """
# Test result of testing __getitem__ method
#
# /Users/jakkus/PycharmProjects/CIS41B/venv/bin/python /Users/jakkus/PycharmProjects/CIS41B/CIS41B_FALL_2020_MIDTERM1.py
# Median Temperature for 2000 is 0.294
# Median Temperature for 1990 is 0.296
#
# Process finished with exit code 0
#
# """
# import sqlite3
# import re
#
# TEMPERATURE_DATA_FILE = "Temperature.html"
# database_name = "Assignment1.db"
# temperature_table_name = "Temperature"
#
#
# class DatabaseHandler:
#     def __init__(self, database_name):
#         self.conn = sqlite3.connect(database_name)
#         self.cur = self.conn.cursor()
#
#     def __del__(self):
#         self.conn.close()
#
#     def close(self):
#         self.conn.close()
#
#     def create_table(self, sqlite_create_table_query):
#         try:
#             self.cur.execute(sqlite_create_table_query)
#             self.conn.commit()
#             return True
#         except sqlite3.Error as error:
#             return False
#
#     def insert(self, sqlite_insert_blob_query, data_tuple):
#         try:
#             self.cur.execute(sqlite_insert_blob_query, data_tuple)
#             self.conn.commit()
#             return True
#         except sqlite3.Error as error:
#             return False
#
#     def read_table(self, sqlite_select_query):
#         self.cur.execute(sqlite_select_query)
#         records = self.cur.fetchall()
#         return records
#
#     def search(self, sel):
#         self.cur.execute(sel)
#         rows = self.cur.fetchall()
#         return rows
#
#
# class TemperatureReader:
#
#     def __init__(self, db_name):
#         self.db_handler = DatabaseHandler(db_name)
#         self.table_name = None
#
#     def __getitem__(self, year):
#         sel = 'SELECT Median FROM {0} WHERE Year == "{1}"'.format(self.table_name, year)
#         ret_value = self.db_handler.search(sel)
#         # print(ret_value)
#         return f"Median Temperature for {year} is {ret_value[0][0]}"
#
#     def create_temp_table(self, table_name):
#         create_table_query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
#                                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                                     Year INTEGER NOT NULL UNIQUE,
#                                     Median REAL NOT NULL,
#                                     Upper REAL NOT NULL,
#                                     Lower REAL NOT NULL);"""
#
#         self.db_handler.create_table(create_table_query)
#         self.table_name = table_name
#
#     def insert_temperature_data(self, single_row_data):
#         sqlite_insert_blob_query = f""" INSERT INTO {self.table_name}
#                                         (Year, Median, Upper, Lower) VALUES (?, ?, ?, ?)"""
#         self.db_handler.insert(sqlite_insert_blob_query, tuple(single_row_data))
#
#     def read_data_from_file(self, temp_html_file):
#         with open(temp_html_file, "r") as t_file:
#             # Regex for int or float number with sign
#             regex = re.compile(r'([+-]?\d+(?:\.\d+)?)')
#             for line in t_file:
#                 # print("aaa")
#                 data = regex.findall(line)
#                 # print(data)
#                 if data is not None and len(data) == 4:
#                     self.insert_temperature_data(data)
#                     # print(data)
#
#     def read_from_db(self, field):
#         sqlite_select_query = f"""SELECT {field} from {self.table_name}"""
#         ret_value = self.db_handler.read_table(sqlite_select_query)
#         return ret_value
#
#     def get_years_list(self):
#         ret_rows = self.read_from_db("Year")
#         years = []
#         for row in ret_rows:
#             years.append(row[0])
#
#         return years
#
#     def get_med_temp_list(self):
#         ret_med_rows = self.read_from_db("Median")
#         med_temp = []
#         for row in ret_med_rows:
#             med_temp.append(row[0])
#         return med_temp
#
#
# if __name__ == "__main__":
#     td = TemperatureReader(database_name)
#     td.create_temp_table(temperature_table_name)
#     td.read_data_from_file(TEMPERATURE_DATA_FILE)
#     print(td[2000])
#     print(td[1990])
#
#

# class SQLiteClass:
#
#     def __init__(self, db_name):
#         self.conn = sqlite3.connect(db_name)
#         self.cur = self.conn.cursor()
#
#     def __del__(self):
#         self.conn.close()
#
#     # def __getitem__(self, year):
#     #     pass
#
#     def create_table(self, sqlite_create_table_query):
#         try:
#             # print(f"Entering create_table with query as {sqlite_create_table_query}")
#             self.cur.execute(sqlite_create_table_query)
#             self.conn.commit()
#             return True
#         except sqlite3.Error as error:
#             return False
#
#     def insert(self, sqlite_insert_blob_query, data_tuple):
#         try:
#             self.cur.execute(sqlite_insert_blob_query, data_tuple)
#             self.conn.commit()
#             return True
#         except sqlite3.Error as error:
#             return False
#
#     def read_table(self, sqlite_select_query):
#         self.cur.execute(sqlite_select_query)
#         records = self.cur.fetchall()
#         return records
#
#     def search(self, sel):
#         self.cur.execute(sel)
#         rows = self.cur.fetchall()
#         return rows



# Write a Named Tuple to hold the data in the Temperature.csv (partially listed below).
#
#
# Temperature.csv file excerpt:
# Year,Median,Upper,Lower
# 1850,-0.373,-0.339,-0.425
# 1851,-0.218,-0.184,-0.274
# 1852,-0.228,-0.196,-0.28
# 1853,-0.269,-0.239,-0.321
# 1854,-0.248,-0.218,-0.301
# 1855,-0.272,-0.241,-0.324
# 1856,-0.358,-0.327,-0.413
# 1857,-0.461,-0.431,-0.512
# 1858,-0.467,-0.435,-0.521
# 1859,-0.284,-0.249,-0.34
# 1860,-0.343,-0.31,-0.405
# Solution
# from collections import namedtuple
#
# Temperature = namedtuple("Temperature", ["Year", "Median", "Upper", "Lower"])
#
#
# Write a Database class that has a SQLite data base member to hold the Temperature class data.
# The class should contain a constructor, which makes a connection and initializes the table.
#
#

"""
Sample test output:

/Users/jakkus/PycharmProjects/CIS41B/venv/bin/python /Users/jakkus/PycharmProjects/CIS41B/CIS41B_FALL_2020_MIDTERM1.py
In Database
Created Database
created table
Temperature(Year=1850, Median=-0.373, Upper=-0.339, Lower=-0.425)
data_tuple is : Temperature data: Temperature(Year=1850, Median=-0.373, Upper=-0.339, Lower=-0.425)
data: 1850
In getitem
db is Median Temperature for 1850 is -0.373

Process finished with exit code 0
"""

import sqlite3
from collections import namedtuple

Temperature = namedtuple("Temperature", ["Year", "Median", "Upper", "Lower"])

db_name = "MIDTERM1.db"
table_name = "TEMP"


class SQLiteClass:
    def __init__(self, d_name):
        self.conn = sqlite3.connect(d_name)
        self.cur = self.conn.cursor()
        self.tab_name = None

    def __del__(self):
        self.conn.close()

    def close(self):
        self.conn.close()

    def create_temp_table(self, tab_name):
        self.tab_name = tab_name
        create_table_query = f"""CREATE TABLE IF NOT EXISTS {tab_name} (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Year INTEGER NOT NULL UNIQUE,
                                    Median REAL NOT NULL,
                                    Upper REAL NOT NULL,
                                    Lower REAL NOT NULL);"""
        try:
            self.cur.execute(create_table_query)
            self.conn.commit()
            return True
        except sqlite3.Error as error:
            return False

    def insert(self, data_tuple):
        print(f"data_tuple is : {data_tuple}")
        print(f"data: {data_tuple.temp.Year}")

        sqlite_insert_blob_query = f""" INSERT INTO {self.tab_name} 
                                        (Year, Median, Upper, Lower) VALUES (?, ?, ?, ?)"""
        try:
            self.cur.execute(sqlite_insert_blob_query, (data_tuple.temp.Year, data_tuple.temp.Median, data_tuple.temp.Upper, data_tuple.temp.Lower))
            self.conn.commit()
            return True
        except sqlite3.Error as error:
            return False

    def search(self, sel):
        self.cur.execute(sel)
        rows = self.cur.fetchall()
        return rows


class Database:
    def __init__(self, d_hand, temperature_data):
        self.db_handler = d_hand
        d_hand.insert(temperature_data)

    def __getitem__(self, year):
        print("In getitem")
        sel = 'SELECT Median FROM {0} WHERE Year == "{1}"'.format(table_name, year)
        ret_value = self.db_handler.search(sel)
        # print(ret_value)
        return f"Median Temperature for {year} is {ret_value[0][0]}"


class TemperatureClass:
    def __init__(self, year, median, upper, lower):
        self.temp = Temperature._make((year, median, upper, lower))
        pass

    def __str__(self):
        return f"Temperature data: {self.temp}"

    def __repr__(self):
        return f"Temp: {self.temp}"

    def __getitem__(self, year):
        return self.temp


if __name__ == "__main__":
    temp_data = TemperatureClass(1850, -0.373, -0.339, -0.425)

    db_handle = SQLiteClass(db_name)
    db_handle.create_temp_table(table_name)

    d = Database(db_handle, temp_data)
    print(f"db is {d[1850]}")






# class DatabaseHandler:
#     def __init__(self, db_name):
#         # print(f"Enter __init__ method of DatabaseHandler and db_name is {db_name}")
#         self.conn = sqlite3.connect(db_name)
#         self.cur = self.conn.cursor()
#         # print(f"conn is {self.conn} and cur is {self.cur}")
#         # self.conn = None
#         # self.cur = None
#
#     def __del__(self):
#         self.conn.close()
#
#     def close(self):
#         self.conn.close()
#
#     def create_table(self, sqlite_create_table_query):
#         try:
#             # print(f"Entering create_table with query as {sqlite_create_table_query}")
#             self.cur.execute(sqlite_create_table_query)
#             self.conn.commit()
#             return True
#         except sqlite3.Error as error:
#             return False
#
#     def insert(self, sqlite_insert_blob_query, data_tuple):
#         try:
#             self.cur.execute(sqlite_insert_blob_query, data_tuple)
#             self.conn.commit()
#             return True
#         except sqlite3.Error as error:
#             return False
#
#     def read_table(self, sqlite_select_query):
#         self.cur.execute(sqlite_select_query)
#         records = self.cur.fetchall()
#         return records
#
#     def search(self, sel):
#         self.cur.execute(sel)
#         rows = self.cur.fetchall()
#         return rows




# Write a function to convert a defaultdict, like the following:
#
# { 'Cat':2, 'Dog':3, 'Bird':4, 'Fish':6, 'Elephant':5 }
#
# Into a Pandas DataFrame.  The function should receive the dictionary as a paramater, and return the DataFrame.

# import pandas as pd
#
#
# def dict_to_data_frame_with_key_index(de_dict):
#     df = pd.DataFrame(data=de_dict, index=[0])
#     return df
#
#
# def dict_to_data_frame_with_value_index(de_dict):
#     df = pd.DataFrame(data=de_dict, index=[1])
#     return df
#
#
# if __name__ == "__main__":
#
#     d = {'Cat': 2, 'Dog': 3, 'Bird': 4, 'Fish': 6, 'Elephant': 5 }
#     data_frame_with_key_index = dict_to_data_frame_with_key_index(d)
#     print(data_frame_with_key_index)
#     data_frame_with_value_index = dict_to_data_frame_with_value_index(d)
#     print(data_frame_with_value_index)
#
#
# """
# /Users/jakkus/PycharmProjects/CIS41B/venv/bin/python /Users/jakkus/PycharmProjects/CIS41B/CIS41B_FALL_2020_MIDTERM1.py
#    Cat  Dog  Bird  Fish  Elephant
# 0    2    3     4     6         5
#    Cat  Dog  Bird  Fish  Elephant
# 1    2    3     4     6         5
#
# Process finished with exit code 0
# """


#
# class TemperatureReader1:
#
#     def __init__(self, db_name):
#         self.db_handler = DatabaseHandler(db_name)
#         self.table_name = None
#
#     def __getitem__(self, year):
#         sel = 'SELECT Median FROM {0} WHERE Year == "{1}"'.format(self.table_name, year)
#         ret_value = self.db_handler.search(sel)
#         # print(ret_value)
#         return f"Median Temperature for {year} is {ret_value[0][0]}"
