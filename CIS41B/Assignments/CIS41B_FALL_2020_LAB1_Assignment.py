"""
Name: Srinivas Jakkula
CIS 41B   Fall 2020
Lab Assignment 1
Execution results are at the end of this file.

"""

import re
import csv
import sqlite3
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import matplotlib.pyplot as plt

import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn import preprocessing

TEMPERATURE_DATA_FILE = "Temperature.html"
database_name = "Assignment1.db"
temperature_table_name = "Temperature"


class DatabaseHandler:
    def __init__(self, db_name):
        # print(f"Enter __init__ method of DatabaseHandler and db_name is {db_name}")
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        # print(f"conn is {self.conn} and cur is {self.cur}")
        # self.conn = None
        # self.cur = None

    def __del__(self):
        self.conn.close()

    def close(self):
        self.conn.close()

    def create_table(self, sqlite_create_table_query):
        try:
            # print(f"Entering create_table with query as {sqlite_create_table_query}")
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
        # print(f"Entering __init__ method of TemperatureReader class with db_name as {db_name}")
        self.db_handler = DatabaseHandler(db_name)
        self.table_name = None

    def create_temp_table(self, table_name):
        # print(f"Entering create_temp_table and table name is {table_name}")
        create_table_query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Year INTEGER NOT NULL UNIQUE,
                                    Median REAL NOT NULL,
                                    Upper REAL NOT NULL,
                                    Lower REAL NOT NULL);"""
        # print(create_table_query)

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
        # print(ret_value)
        # for row in ret_value:
        #     print(row[0])
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


class TempUserInterface:

    def __init__(self, x, y):
        # pass
        self.window = tk.Tk()
        self.frame = tk.Frame(self.window)

        self.window.title("Temperature Anomaly Data")
        self.window.geometry("600x600")

        self.frame.pack()
        plot_button = tk.Button(master=self.frame,
                             command=self.draw_xyplot_command,
                             # height=2,
                             # width=10,
                             text="XY PLOT")
        plot_button.pack(side=tk.LEFT)
        plot_button = tk.Button(master=self.frame,
                             command=self.draw_bar_chart_command,
                             # height=2,
                             # width=10,
                             text="BAR PLOT")
        plot_button.pack(side=tk.LEFT)
        plot_button = tk.Button(master=self.frame,
                             command=self.draw_linear_regression_chart_command,
                             # height=2,
                             # width=10,
                             text="LINEAR REGRESSION")
        plot_button.pack(side=tk.LEFT)
        self.canvas = None
        self.x = x
        self.y = y

    def draw_xyplot_command(self):
        print("Draw xy plot")

        try:
            self.canvas.get_tk_widget().pack_forget()
        except AttributeError:
            pass

        fig = Figure(figsize=(6, 5), dpi=100)

        # x = [1950, 1951, 1952]
        # y = [-0.3, 0.1, -0.2]

        plot = fig.add_subplot(111, xmargin=2, ymargin=2, xscale="linear")

        plot.axis([min(self.x)-1, max(self.x) + 1, min(self.y), max(self.y)])

        plot.set_xlabel('Year')
        plot.set_ylabel('Temperature')
        plot.plot(self.x, self.y)

        self.canvas = FigureCanvasTkAgg(fig, master=self.window)

        self.canvas.get_tk_widget().pack()

    def draw_bar_chart_command(self):
        print("draw bar chart")

        try:
            self.canvas.get_tk_widget().pack_forget()
        except AttributeError:
            pass

        # x = [1950, 1951, 1952]
        # y = [-0.3, 0.1, -0.2]

        fig = plt.figure(figsize=(6, 4))
        plt.xlabel("Year")
        plt.ylabel("Temperature")
        plt.title("Year and Temp")
        plt.bar(self.x, self.y, color='maroon', width=0.2)

        plt.axis([min(self.x), max(self.x), min(self.y), max(self.y)])

        self.canvas = FigureCanvasTkAgg(fig, master=self.window)
        self.canvas.get_tk_widget().pack()

    def draw_linear_regression_chart_command(self):

        try:
            self.canvas.get_tk_widget().pack_forget()
        except AttributeError:
            pass

        print("draw linear regression chart")

        fig = plt.figure(figsize=(6, 4))

        data = pd.read_csv('temp_data.csv')
        X = data.iloc[:, 0].values.reshape(-1, 1)
        Y = data.iloc[:, 1].values.reshape(-1, 1)

        linear_regressor = LinearRegression()  # create object for the class
        linear_regressor.fit(X, Y)  # perform linear regression
        Y_pred = linear_regressor.predict(X)  # make predictions
        plt.scatter(X, Y)
        plt.plot(X, Y_pred, color='red')
        plt.xlabel("Year")
        plt.ylabel("Temperature")
        plt.title("Temperature Anomaly")

        self.canvas = FigureCanvasTkAgg(fig, master=self.window)
        self.canvas.get_tk_widget().pack()

    def draw_front_end(self):
        self.window.mainloop()


def write_data_csv_file(y, m):
    with open("temp_data.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(zip(y, m))


def main():

    td = TemperatureReader(database_name)
    td.create_temp_table(temperature_table_name)
    td.read_data_from_file(TEMPERATURE_DATA_FILE)
    years = td.get_years_list()
    med_temp = td.get_med_temp_list()
    # print(years)
    # print(med_temp)

    write_data_csv_file(years, med_temp)

    my_user_interface = TempUserInterface(years, med_temp)
    my_user_interface.draw_front_end()


if __name__ == "__main__":
    main()
