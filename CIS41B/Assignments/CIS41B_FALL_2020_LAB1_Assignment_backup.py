"""
Name: Srinivas Jakkula
CIS 41B   Fall 2020
Lab Assignment 1
Execution results are at the end of this file.

"""

from collections import namedtuple
from collections import defaultdict
from functools import reduce
import re
import sqlite3
import tkinter as tk
# import matplotlib.pyplot as plt
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib
# matplotlib.use("TkAgg")

from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['toolbar'] = 'None'


TEMPERATURE_DATA_FILE = "Temperature.html"
database_name = "Assignment1.db"
temperature_table_name = "Temperature"


class DatabaseHandler:
    def __init__(self, db_name):
        print(f"Enter __init__ method of DatabaseHandler and db_name is {db_name}")
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        print(f"conn is {self.conn} and cur is {self.cur}")
        # self.conn = None
        # self.cur = None

    def __del__(self):
        self.conn.close()

    # def connect(self, db_name):
    #     try:
    #         self.conn = sqlite3.connect(db_name)
    #         self.cur = self.conn.cursor()
    #         return True
    #     except sqlite3.Error as error:
    #         return False

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
        print(f"Entering __init__ method of TemperatureReader class with db_name as {db_name}")
        self.db_handler = DatabaseHandler(db_name)
        self.table_name = None

    def create_temp_table(self, table_name):
        print(f"Entering create_temp_table and table name is {table_name}")
        create_table_query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Year TEXT NOT NULL UNIQUE,
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













    # def connect(self, dbname):
    #     self.conn = sqlite3.connect(dbname)

        # self.sqliteConnection = sqlite3.connect(dbname)


# class DrawTemperaturePlots:
#     def __init__(self):
#         pass
#
#     def drawXYplot(self):
#         print("In drawXYplot")
#         years = [1950, 1951, 1952]
#         med_temps = [-0.3, 0.1, -0.2]
#         plt.plot(years, med_temps)
#         plt.axis([ 1950, 1960, -1, +1])
#         plt.xlabel("Year")
#         plt.ylabel("Temperature")
#         plt.show()
#
#     def drawBARplot(self):
#         print("in drawBARplot")
#
#     def drawLinearRegressionPlot(self):
#         print("in drawLinearRegressionPlot")


class TempUserInterface:

    def __init__(self):
        # pass
        self.window = Tk()
        self.frame = Frame(self.window)

        self.window.title("Temperature Anomaly Data")
        self.window.geometry("600x600")

        self.frame.pack()
        plot_button = Button(master=self.frame,
                             command=self.draw_xyplot_command,
                             # height=2,
                             # width=10,
                             text="XY PLOT")
        plot_button.pack(side=tk.LEFT)
        plot_button = Button(master=self.frame,
                             command=self.draw_bar_chart_command,
                             # height=2,
                             # width=10,
                             text="BAR PLOT")
        plot_button.pack(side=tk.LEFT)
        plot_button = Button(master=self.frame,
                             command=self.draw_xyplot_command,
                             # height=2,
                             # width=10,
                             text="LINEAR REGRESSION")
        plot_button.pack(side=tk.LEFT)
        self.canvas = None

        # self.frame = tk.Frame(self.root)
        # self.drawMPLobject = DrawTemperaturePlots()

    def draw_xyplot_command(self):
        print("Draw xy plot")

        try:
            self.canvas.get_tk_widget().pack_forget()
        except AttributeError:
            pass

        fig = Figure(figsize=(6, 5), dpi=100)
        # fig.clf()
        x = [1950, 1951, 1952]
        y = [-0.3, 0.1, -0.2]

        plot = fig.add_subplot(111, xmargin=2, ymargin=2)
        # plot.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
        plot.axis([1949, 1960, -1, +1])
        plot.set_xlabel('Year')
        plot.set_ylabel('Temperature')
        plot.plot(x, y)

        self.canvas = FigureCanvasTkAgg(fig, master=self.window)

        # canvas = FigureCanvasTkAgg(fig, master=self.frame)
        # self.canvas.draw()
        self.canvas.get_tk_widget().pack()

        # toolbar = NavigationToolbar2Tk(self.canvas, self.window)
        # # toolbar = NavigationToolbar2Tk(canvas, self.frame)
        # toolbar.update()
        # self.canvas.get_tk_widget().pack()


        # self.drawMPLobject.drawBARplot()
        # figure = Figure(figsize=(6, 4), dpi=100)
        # # plot = figure.add_subplot(1, 1, 1)
        # plot = figure.add_subplot(111)
        # canvas = FigureCanvasTkAgg(figure, self.root)
        # canvas.get_tk_widget().grid(row=30, column=30)
        # # canvas.get_tk_widget().pack(tk.LEFT, fill=tk.BOTH)
        # x = [1950, 1951, 1952]
        # y = [-0.3, 0.1, -0.2]
        # plot.plot(x, y)
        # plot.axis([1949, 1960, -1, +1])
        # plot.set_xlabel('Year')
        # plot.set_ylabel('Temperature')
        # # self.frame.pack()
        # self.root.mainloop()

    def draw_bar_chart_command(self):
        print("draw bar chart")

        try:
            self.canvas.get_tk_widget().pack_forget()
        except AttributeError:
            pass

        x = [1950, 1951, 1952]
        y = [-0.3, 0.1, -0.2]

        # plot = fig.add_subplot(111)
        # plot.axis([1949, 1960, -1, +1])
        # plot.set_xlabel('Year')
        # plot.set_ylabel('Temperature')
        # plot.plot(x, y)

        # fig = Figure(figsize=(6, 4), dpi=100)
        fig = plt.figure(figsize=(6, 4))
        # plt.clf()
        plt.xlabel("Year")
        plt.ylabel("Temperature")
        plt.title("Year and Temp")
        plt.bar(x, y, color='maroon', width=0.2)
        plt.axis([1949, 1960, -0.5, +0.5])

        self.canvas = FigureCanvasTkAgg(fig, master=self.window)
        # self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        # toolbar = NavigationToolbar2Tk(self.canvas, self.window)
        # toolbar.update()
        # self.canvas.get_tk_widget().pack()

    def draw_linear_Regression_chart_command(self):
        print("draw linear regression chart")

    def draw_front_end(self):
        # window = Tk()

        # self.frame.pack()
        self.window.mainloop()

        # self.root.geometry("600x500")
        # self.root.title("Temperature Anomaly Data")
        #
        # self.frame.pack()
        # button = tk.Button(self.frame,
        #                    text="XY PLOT",
        #                    fg="red",
        #                    command=self.draw_xyplot_command)
        # button.pack(side=tk.LEFT)
        # slogan = tk.Button(self.frame,
        #                    text="BAR CHART",
        #                    command=self.draw_bar_chart_command)
        # slogan.pack(side=tk.LEFT)
        # slogan = tk.Button(self.frame,
        #                    text="LINEAR REGRESSION",
        #                    command=self.draw_linear_Regression_chart_command)
        # slogan.pack(side=tk.LEFT)
        #
        # self.root.mainloop()


def main():

    td = TemperatureReader(database_name)
    td.create_temp_table(temperature_table_name)
    td.read_data_from_file(TEMPERATURE_DATA_FILE)

    # td.create_temp_table(temperature_table_name)

    # db_handler = DatabaseHandler(database_name)
    # create_table_query = f"""CREATE TABLE IF NOT EXISTS {temperature_table_name} (
    #                             id INTEGER PRIMARY KEY,
    #                             Year TEXT NOT NULL UNIQUE,
    #                             Median REAL NOT NULL,
    #                             Upper REAL NOT NULL,
    #                             Lower REAL NOT NULL);"""
    # db_handler.create_table(create_table_query)


    # td.create_table("temperature_table")

    #td.read_data_from_file(TEMPERATURE_DATA_FILE)

    my_user_interface = TempUserInterface()
    my_user_interface.draw_front_end()

    # mp = DrawTemperaturePlots()
    # mp.drawXYplot()


if __name__ == "__main__":
    main()



# try:
#     sqliteConnection = sqlite3.connect('SQLite_Python.db')
#     sqlite_create_table_query = '''CREATE TABLE Database (
#                                 id INTEGER PRIMARY KEY,
#                                 name TEXT NOT NULL,
#                                 photo text NOT NULL UNIQUE,
#                                 html text NOT NULL UNIQUE);'''
#
#     cursor = sqliteConnection.cursor()
#     print("Successfully Connected to SQLite")
#     cursor.execute(sqlite_create_table_query)
#     sqliteConnection.commit()
#     print("SQLite table created")
#
#     cursor.close()
#
# except sqlite3.Error as error:
#     print("Error while creating a sqlite table", error)
# finally:
#     if (sqliteConnection):
#         sqliteConnection.close()
#         print("sqlite connection is closed")



#
# try:
#     sqliteConnection = sqlite3.connect('SQLite_Python.db')
#     cursor = sqliteConnection.cursor()
#     print("Database created and Successfully Connected to SQLite")
#     sqlite_select_Query = "select sqlite_version();"
#     cursor.execute(sqlite_select_Query)
#     record = cursor.fetchall()
#     print("SQLite Database Version is: ", record)
#     cursor.close()
#
# except sqlite3.Error as error:
#     print("Error while connecting to sqlite", error)
# finally:
#     if (sqliteConnection):
#         sqliteConnection.close()
#         print("The SQLite connection is closed")