import xml.etree.ElementTree as ET
import sqlite3
import pprint
import json
import socket


PARSEFILE = "UNData.xml"
DATABASE_NAME = "Assignment4.db"
TABLE_NAME = "UNData"


class DatabaseHandler:
    def __init__(self, db_name):
        # self.conn = sqlite3.connect(db_name, check_same_thread=False)
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


class UNDataReader:
    def __init__(self, db_name):
        self.db_handler = DatabaseHandler(db_name)
        self.table_name = None

    def create_undata_table(self, table_name):
        create_table_query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Country TEXT,
                                    Year INTEGER,
                                    Value REAL NOT NULL,
                                    UNIQUE (Country, Year));"""

        self.db_handler.create_table(create_table_query)
        self.table_name = table_name

    def insert_un_data(self, single_row_data):
        sqlite_insert_blob_query = f""" INSERT INTO {self.table_name} 
                                        (Country, Year, Value) VALUES (?, ?, ?)"""
        self.db_handler.insert(sqlite_insert_blob_query, single_row_data)

    def parse_xml_file(self, filename):
        root = ET.parse(filename).getroot()
        # print(root.tag)
        count = 0
        for element in root.findall("data/record"):
            # print(element.tag)
            country = element.find("Country").text
            year = element.find("Year").text
            value = element.find("Value").text

            single_data = (country, year, value)
            # print(single_data)
            count += 1
            self.insert_un_data(single_data)
            # print(count)

    def get_country_wise_data(self, country):
        sql_select_query = f"""SELECT Year, Value from {self.table_name} WHERE Country == \"{country}\""""
        ret_value = self.db_handler.read_table(sql_select_query)
        # print(ret_value)
        # grf_emission = []
        # for row in ret_value:
        #     grf_emission.append(row)
        # return grf_emission
        return ret_value

    def country_dat_to_json(self, lst):
        json_string = json.dumps(dict(lst))
        # print(json_string)
        return json_string


class Server:
    def __init__(self):
        self.grf = UNDataReader(DATABASE_NAME)
        self.grf.create_undata_table(TABLE_NAME)
        self.grf.parse_xml_file(PARSEFILE)

        self.host = socket.gethostname()
        self.port = 5000  # initiate port no above 1024

        self.server_socket = socket.socket()  # get instance
        # look closely. The bind() function takes tuple as argument
        self.server_socket.bind((self.host, self.port))  # bind host address and port together

    def connect(self):
        self.server_socket.listen(2)
        conn, address = self.server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            if not data:
                # if data is not received break
                break
            print("from connected user: " + str(data))

            country_data = self.grf.get_country_wise_data(data)
            json_country_data = self.grf.country_dat_to_json(country_data)
            print(f"json_country_data is:{json_country_data}")
            conn.send(json_country_data.encode())
            print("sent data")

            # a = grf.get_country_wise_data("Australia")
            # pprint.pprint(a)
            # print(grf.country_dat_to_JSON(a))
            # Get the data
            # Convert the data to JSON string
            # Send the data
            # data = input(' -> ')
            # conn.send(data.encode())  # send data to the client
            # conn.send(json_country_data.encode())

        conn.close()  # close the connection


# def server_program():
#     # get the hostname
#     host = socket.gethostname()
#     port = 5000  # initiate port no above 1024
#
#     server_socket = socket.socket()  # get instance
#     # look closely. The bind() function takes tuple as argument
#     server_socket.bind((host, port))  # bind host address and port together
#
#     # configure how many client the server can listen simultaneously
#     server_socket.listen(2)
#     conn, address = server_socket.accept()  # accept new connection
#     print("Connection from: " + str(address))
#     while True:
#         # receive data stream. it won't accept data packet greater than 1024 bytes
#         data = conn.recv(1024).decode()
#         if not data:
#             # if data is not received break
#             break
#         print("from connected user: " + str(data))
#
#         data = input(' -> ')
#         conn.send(data.encode())  # send data to the client
#
#     conn.close()  # close the connection


if __name__ == "__main__":
    # grf = UNDataReader(DATABASE_NAME)
    # grf.create_undata_table(TABLE_NAME)
    # grf.parse_xml_file(PARSEFILE)
    # a = grf.get_country_wise_data("Australia")
    # pprint.pprint(a)
    # print(grf.country_dat_to_JSON(a))
    # server_program()

    server = Server()
    server.connect()




