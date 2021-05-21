"""
Name: Srinivas Jakkula
CIS 41B   Fall 2020
Lab Assignment 2
Execution results are at the end of this file.
"""
import sqlite3
from bs4 import BeautifulSoup
from urllib.request import urlopen
from matplotlib import pyplot as plt
import numpy as np


database_name = "Assignment2.db"
co2_emission_table_name = "CO2Emission"
SITE_NAME = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions"


def absolute_value(val):
    # print(val)
    sizes = np.array(val)
    # print(sizes)
    a = np.round(val / 100. * sizes.sum(), 2)
    # a = np.round(val, 2)
    print(a)
    return a


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


class CO2EmissionReader:

    def __init__(self, db_name):
        self.db_handler = DatabaseHandler(db_name)
        self.table_name = None

    def create_co2_table(self, table_name):
        create_table_query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Country TEXT NOT NULL UNIQUE,
                                    CO2_Per REAL NOT NULL);"""

        self.db_handler.create_table(create_table_query)
        self.table_name = table_name

    def insert_co2_data(self, single_row_data):
        sqlite_insert_blob_query = f""" INSERT INTO {self.table_name} 
                                        (Country, CO2_Per) VALUES (?, ?)"""
        self.db_handler.insert(sqlite_insert_blob_query, single_row_data)

    def get_top_10_county_emissions(self):
        sql_select_query = f"""SELECT * from {self.table_name} ORDER BY CO2_Per DESC LIMIT 10"""
        ret_value = self.db_handler.read_table(sql_select_query)
        country_wise_co2_emission = []
        for row in ret_value:
            country_wise_co2_emission.append((row[1], row[2]))
        return country_wise_co2_emission

    def scrape_data_and_insert(self, site):
        html = urlopen(site)
        soup = BeautifulSoup(html, 'html.parser')
        tb1 = soup.find_all('tbody')[1].find_all('tr')
        # emission_percentage = []
        for row in tb1[5:]:
            self.insert_co2_data((row.find_all('td')[0].text.strip(), float(row.find_all("td")[4].text[:-1])))
            # emission_percentage.append((row.find_all('td')[0].text.strip(), float(row.find_all("td")[4].text[:-1])))

    def read_from_db(self, field):
        sqlite_select_query = f"""SELECT {field} from {self.table_name}"""
        ret_value = self.db_handler.read_table(sqlite_select_query)
        return ret_value

    def readall_from_db(self):
        sqlite_select_query = f"""SELECT * from {self.table_name}"""
        ret_value = self.db_handler.read_table(sqlite_select_query)
        return ret_value


class CO2EmissionUserInterface:
    def __init__(self):
        pass

    @classmethod
    def draw_pie_chart(cls, country_data):
        data = [i[1] for i in country_data]
        print(data)
        labels = [i[0] for i in country_data]
        print(labels)
        fig = plt.figure(figsize=(10, 7))
        fig.suptitle('Top 10 Co2 Emission Countries', fontsize=20)
        # plt.pie(data, labels=labels, autopct=absolute_value)
        plt.pie(data, labels=labels)
        plt.show()


def main():
    td = CO2EmissionReader(database_name)
    td.create_co2_table(co2_emission_table_name)
    td.scrape_data_and_insert(SITE_NAME)
    top10_data = td.get_top_10_county_emissions()
    print(top10_data)
    CO2EmissionUserInterface.draw_pie_chart(top10_data)


if __name__ == "__main__":
    main()