'''
To convert this readTable code to be a member function of a class:
1.  The sqliteConnection should be a data member of the class, and connected
2.  The function should take a string parameter for the select statement.  See line 16.
3.  It should return 'true' if data read, otherwise 'false'
'''

import sqlite3

def readTable():
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from Database"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("id: ", row[0])
            print("name: ", row[1]) 
            print("photo: ", row[2])
            print("html: ", row[3])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

readTable()