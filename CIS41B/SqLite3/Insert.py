'''
To convert this insert code to be a member function of a class:
1.  The sqliteConnection should be a data member of the class, and connected.
2.  The function should take a string query for inserting the data.  See line 21 & 22.
3.  It should return 'true' if data inserted, otherwise 'false'
'''

import sqlite3

def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insert(Id, name, photo, hfile):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO Database
                                  (Id, name, photo, html) VALUES (?, ?, ?, ?)"""

        foto = convertToBinaryData(photo)
        html = convertToBinaryData(hfile)
        # Convert data into tuple format
        data_tuple = (Id, name, foto, html)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")

insert(1, "Temperature", "Temperature.png", "Temperature.html")
insert(2, "CO2", "CO2.png", "CO2.html")