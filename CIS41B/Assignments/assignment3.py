# Threading class using inheritance
import sqlite3
import threading
import time
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
import queue
SITE_NAME = "https://www.esrl.noaa.gov/gmd/aggi/aggi.html"

threadList1 = ["CO2", "CH4", "N2O", "CFC12", "CFC11", "15-minor"]
count = len(threadList1)
exitFlag = False

database_name = "Assignment3_1.db"
grf_table_name = "GRF_Data"
SITE_NAME = "https://www.esrl.noaa.gov/gmd/aggi/aggi.html"
threadLock = threading.Lock()


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


class AGGIReader:
    def __init__(self, db_name):
        self.db_handler = DatabaseHandler(db_name)
        self.table_name = None

    def create_aggi_table(self, table_name):
        create_table_query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Year INTEGER,
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

    # def scrape_data(self, site):
    #     html = urlopen(site)
    #     soup = BeautifulSoup(html, 'html.parser')
    #     tb1 = soup.find_all('tbody')[1].find_all('tr')
    #     for row in tb1[2:]:
    #         t = list()
    #         for ele in row.find_all('td')[0:7]:
    #             t.append(ele.text.strip())
    #         result = [int(x) if x.lstrip(" -+").isdigit() else float(x) for x in t]
    #         self.insert_co2_data(tuple(result))


def scrape_data(threadName, site, pos):
    time.sleep(random.randint(1, 5))
    print("%s: %s" % (threadName, time.ctime(time.time())))
    time.sleep(1)
    html = urlopen(site)
    soup = BeautifulSoup(html, 'html.parser')
    tb1 = soup.find_all('tbody')[1].find_all('tr')
    for row in tb1[2:]:
        print(threadName, row.find_all('td')[0].text.strip(), row.find_all('td')[pos + 1].text.strip())


class TimeThread (threading.Thread):
    def __init__(self, threadID,  name, site, pos):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.site = site
        self.name = name
        self.pos = pos

    def run(self):
        print("Starting " + self.name)
        # global threadLo
        threadLock.acquire()
        scrape_data(self.name, self.site, self.pos)
        threadLock.release()
        print("Exiting " + self.name)


def main():
    grf = AGGIReader(database_name)
    grf.create_aggi_table(grf_table_name)

    # Create new threads

    threadlist = []
    for i in range(count):
        sthread = "Thread-"+str(i+1)
        threadlist.insert(i, TimeThread(i+1, sthread, SITE_NAME, i))

    # Start new Threads
    for i in range(count):
        threadlist[i].start()

    # Join Threads
    for i in range(count):
        threadlist[i].join()

    print("Exiting Main Thread")


if __name__ == "__main__":
    main()
