"""
Name: Srinivas Jakkula
CIS 41B   Fall 2020
Lab Assignment 3
Execution results are at the end of this file.

"""
import sqlite3
from bs4 import BeautifulSoup
from urllib.request import urlopen
import threading
import time
import random
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import matplotlib.pyplot as plt
import csv
import pandas as pd
from sklearn.linear_model import LinearRegression


database_name = "Assignment3_2.db"
grf_table_name = "GRF_Data"
SITE_NAME = "https://www.esrl.noaa.gov/gmd/aggi/aggi.html"
RDF_List = ["CO2", "CH4", "N2O", "CFC12", "CFC11", "Minor15"]
threadLock = threading.Lock()
threadList1 = ["CO2", "CH4", "N2O", "CFC12", "CFC11", "Minor15"]
count = len(threadList1)
all_data = {}


class DatabaseHandler:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
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


class AGGIReader:
    def __init__(self, db_name):
        self.db_handler = DatabaseHandler(db_name)
        self.table_name = None

    def create_aggi_table(self, table_name):
        create_table_query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Year INTEGER UNIQUE,
                                    CO2 REAL NOT NULL,
                                    CH4 REAL NOT NULL,
                                    N2O REAL NOT NULL,
                                    CFC12 REAL NOT NULL,
                                    CFC11 REAL NOT NULL,
                                    Minor15 REAL NOT NULL);"""

        self.db_handler.create_table(create_table_query)
        self.table_name = table_name

    def insert_co2_data(self, single_row_data):
        sqlite_insert_blob_query = f""" INSERT INTO {self.table_name} 
                                        (Year, CO2, CH4, N2O, CFC12, CFC11, Minor15) VALUES (?, ?, ?, ?, ?, ?, ?)"""
        self.db_handler.insert(sqlite_insert_blob_query, single_row_data)

    def scrape_data(self, site):
        html = urlopen(site)
        soup = BeautifulSoup(html, 'html.parser')
        tb1 = soup.find_all('tbody')[1].find_all('tr')
        for row in tb1[2:]:
            t = list()
            for ele in row.find_all('td')[0:7]:
                t.append(ele.text.strip())
            result = [int(x) if x.lstrip(" -+").isdigit() else float(x) for x in t]
            self.insert_co2_data(tuple(result))

    def get_grf_emissions(self, type1):
        sql_select_query = f"""SELECT Year, {type1} from {self.table_name}"""
        ret_value = self.db_handler.read_table(sql_select_query)
        grf_emission = []
        for row in ret_value:
            grf_emission.append(row)
        return grf_emission


def process_data(key, value):
    with open(f"{key}.csv", "w") as f:
        writer = csv.writer(f)
        for v in value:
            writer.writerow(v)


def draw_linear_plots():
    for k, v in all_data.items():
        process_data(k, v)

    window = tk.Tk()
    # frame = tk.Frame(window)

    window.title(" Global Radiative Forcing Data")
    window.geometry("800x800")

    fig = plt.figure(figsize=(8, 6))

    data = pd.read_csv('CO2.csv')
    X = data.iloc[:, 0].values.reshape(-1, 1)
    Y = data.iloc[:, 1].values.reshape(-1, 1)

    ax1 = fig.add_subplot(2, 3, 1)

    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(X, Y)  # perform linear regression
    Y_pred = linear_regressor.predict(X)  # make predictions
    ax1.scatter(X, Y)
    ax1.plot(X, Y_pred, color='red')
    ax1.set_xlabel("Year")
    ax1.set_ylabel("CO2")
    plt.title("Global Radiative Forcing")
    bar1 = FigureCanvasTkAgg(fig, window)
    ax1.set_title('Year Vs. CO2')

    data1 = pd.read_csv('CH4.csv')
    X1 = data1.iloc[:, 0].values.reshape(-1, 1)
    Y1 = data1.iloc[:, 1].values.reshape(-1, 1)

    ax2 = fig.add_subplot(2, 3, 2)
    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(X1, Y1)  # perform linear regression
    Y1_pred = linear_regressor.predict(X1)  # make predictions
    ax2.scatter(X1, Y1)
    ax2.plot(X1, Y1_pred, color='red')
    ax2.set_xlabel("Year")
    ax2.set_ylabel("CH4")
    bar2 = FigureCanvasTkAgg(fig, window)
    ax2.set_title('Year Vs. CH4')

    data2 = pd.read_csv('N2O.csv')
    X2 = data2.iloc[:, 0].values.reshape(-1, 1)
    Y2 = data2.iloc[:, 1].values.reshape(-1, 1)

    ax3 = fig.add_subplot(2, 3, 3)
    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(X2, Y2)  # perform linear regression
    Y2_pred = linear_regressor.predict(X2)  # make predictions
    ax3.scatter(X2, Y2)
    ax3.plot(X2, Y2_pred, color='red')
    ax3.set_xlabel("Year")
    ax3.set_ylabel("N2O")
    bar3 = FigureCanvasTkAgg(fig, window)
    ax3.set_title('Year Vs. N2O')

    data3 = pd.read_csv('CFC12.csv')
    X3 = data3.iloc[:, 0].values.reshape(-1, 1)
    Y3 = data3.iloc[:, 1].values.reshape(-1, 1)

    ax4 = fig.add_subplot(2, 3, 4)
    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(X3, Y3)  # perform linear regression
    Y3_pred = linear_regressor.predict(X3)  # make predictions
    ax4.scatter(X3, Y3)
    ax4.plot(X3, Y3_pred, color='red')
    ax4.set_xlabel("Year")
    ax4.set_ylabel("CFC12")
    bar4 = FigureCanvasTkAgg(fig, window)
    ax4.set_title('Year Vs. CFC12')

    data4 = pd.read_csv('CFC11.csv')
    X4 = data4.iloc[:, 0].values.reshape(-1, 1)
    Y4 = data4.iloc[:, 1].values.reshape(-1, 1)

    ax5 = fig.add_subplot(2, 3, 5)
    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(X4, Y4)  # perform linear regression
    Y4_pred = linear_regressor.predict(X4)  # make predictions
    ax5.scatter(X4, Y4)
    ax5.plot(X4, Y4_pred, color='red')
    ax5.set_xlabel("Year")
    ax5.set_ylabel("CFC11")
    bar5 = FigureCanvasTkAgg(fig, window)
    ax5.set_title('Year Vs. CFC11')

    data5 = pd.read_csv('Minor15.csv')
    X5 = data5.iloc[:, 0].values.reshape(-1, 1)
    Y5 = data5.iloc[:, 1].values.reshape(-1, 1)

    ax6 = fig.add_subplot(2, 3, 6)
    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(X5, Y5)  # perform linear regression
    Y5_pred = linear_regressor.predict(X5)  # make predictions
    ax6.scatter(X5, Y5)
    ax6.plot(X4, Y5_pred, color='red')
    ax6.set_xlabel("Year")
    ax6.set_ylabel("Minor15")
    bar6 = FigureCanvasTkAgg(fig, window)
    bar6.get_tk_widget().pack()
    ax6.set_title('Year Vs. Minor15')

    window.mainloop()


def readData(scrape_col, db_conn):
    time.sleep(random.randint(1, 5))
    print("%s: %s" % (scrape_col, time.ctime(time.time())))
    grf_emi = db_conn.get_grf_emissions(scrape_col)
    all_data[scrape_col] = grf_emi
    time.sleep(1)


class TimeThread (threading.Thread):

    def __init__(self, threadID, name, db_con):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.db_con = db_con

    def run(self):
        print("Starting " + self.name)
        print("")
        threadLock.acquire()
        readData(self.name, self.db_con)
        threadLock.release()
        print("Exiting " + self.name)


grf = AGGIReader(database_name)
grf.create_aggi_table(grf_table_name)
grf.scrape_data(SITE_NAME)

threadlist = []
for i in range(count):
    sthread = "Thread-"+str(i+1)
    threadlist.insert(i, TimeThread(i + 1, threadList1[i], grf))
# Start new Threads
for i in range(count):
    threadlist[i].start()

# Join Threads
for i in range(count):
    threadlist[i].join()

print("Exiting Main Thread")

draw_linear_plots()

"""
Output:
/Users/jakkus/PycharmProjects/CIS41B/venv/bin/python /Users/jakkus/PycharmProjects/CIS41B/Assignments/CIS41B_FALL_2020_LAB3_ASSIGNMENT.py
Starting CO2

Starting CH4

Starting N2O

Starting CFC12

Starting CFC11

Starting Minor15

CO2: Mon Nov 16 23:13:59 2020
Exiting CO2
CH4: Mon Nov 16 23:14:03 2020
Exiting CH4
N2O: Mon Nov 16 23:14:06 2020
Exiting N2O
CFC12: Mon Nov 16 23:14:12 2020
Exiting CFC12
CFC11: Mon Nov 16 23:14:14 2020
Exiting CFC11
Minor15: Mon Nov 16 23:14:18 2020
Exiting Minor15
Exiting Main Thread

"""