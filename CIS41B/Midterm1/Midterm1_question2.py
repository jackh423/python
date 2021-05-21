"""
# Using your SQLite class, write a member function __getitem__ which returns the median data for a given year.
#
Test result of testing __getitem__ method

/Users/jakkus/PycharmProjects/CIS41B/venv/bin/python /Users/jakkus/PycharmProjects/CIS41B/CIS41B_FALL_2020_MIDTERM1.py
Median Temperature for 2000 is 0.294
Median Temperature for 1990 is 0.296

Process finished with exit code 0

"""
import sqlite3
import re

TEMPERATURE_DATA_FILE = "Temperature.html"
database_name = "Assignment1.db"
temperature_table_name = "Temperature"


class DatabaseHandler:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def close(self):
        self.conn.close()

    def create_table(self, sqlite_create_table_query):
        try:
            self.cur.execute(sqlite_create_table_query)
            self.conn.commit()
            return True
        except sqlite3.Error as error:
            return False

    def insert(self, sqlite_insert_blob_query, data_tuple):
        try:
            self.cur.execute(sqlite_insert_blob_query, data_tuple)
            self.conn.commit()
            return True
        except sqlite3.Error as error:
            return False

    def read_table(self, sqlite_select_query):
        self.cur.execute(sqlite_select_query)
        records = self.cur.fetchall()
        return records

    def search(self, sel):
        self.cur.execute(sel)
        rows = self.cur.fetchall()
        return rows


class TemperatureReader:

    def __init__(self, db_name):
        self.db_handler = DatabaseHandler(db_name)
        self.table_name = None

    def __getitem__(self, year):
        sel = 'SELECT Median FROM {0} WHERE Year == "{1}"'.format(self.table_name, year)
        ret_value = self.db_handler.search(sel)
        # print(ret_value)
        return f"Median Temperature for {year} is {ret_value[0][0]}"

    def create_temp_table(self, table_name):
        create_table_query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Year INTEGER NOT NULL UNIQUE,
                                    Median REAL NOT NULL,
                                    Upper REAL NOT NULL,
                                    Lower REAL NOT NULL);"""

        self.db_handler.create_table(create_table_query)
        self.table_name = table_name

    def insert_temperature_data(self, single_row_data):
        sqlite_insert_blob_query = f""" INSERT INTO {self.table_name} 
                                        (Year, Median, Upper, Lower) VALUES (?, ?, ?, ?)"""
        self.db_handler.insert(sqlite_insert_blob_query, tuple(single_row_data))

    def read_data_from_file(self, temp_html_file):
        with open(temp_html_file, "r") as t_file:
            # Regex for int or float number with sign
            regex = re.compile(r'([+-]?\d+(?:\.\d+)?)')
            for line in t_file:
                # print("aaa")
                data = regex.findall(line)
                # print(data)
                if data is not None and len(data) == 4:
                    self.insert_temperature_data(data)
                    # print(data)

    def read_from_db(self, field):
        sqlite_select_query = f"""SELECT {field} from {self.table_name}"""
        ret_value = self.db_handler.read_table(sqlite_select_query)
        return ret_value

    def get_years_list(self):
        ret_rows = self.read_from_db("Year")
        years = []
        for row in ret_rows:
            years.append(row[0])

        return years

    def get_med_temp_list(self):
        ret_med_rows = self.read_from_db("Median")
        med_temp = []
        for row in ret_med_rows:
            med_temp.append(row[0])
        return med_temp


if __name__ == "__main__":
    td = TemperatureReader(database_name)
    td.create_temp_table(temperature_table_name)
    td.read_data_from_file(TEMPERATURE_DATA_FILE)
    print(td[2000])
    print(td[1990])
