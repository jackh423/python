'''
To convert this updaTable code to be a member function of a class:
1.  The sqliteConnection should be a data member of the class and connected.
2.  The function should take a string parameter for the query.  See line 16.
3.  It should return 'true' if updated, otherwise 'false'
'''

import sqlite3

def updateTable(id, htext):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update Database set html = ? where id = ?"""
        data = (htext, id)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        print("Record Updated successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The sqlite connection is closed")

updateTable(2, "OS.html")