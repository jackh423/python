'''
To convert this delete code to be a member function of a class:
1.  The sqliteConnection should be a data member of the class and already connected
2.  The function should take a string parameter for the delete query
3.  It should return 'true' if deleted, otherwise 'false'
'''

import sqlite3

def deleteRecord():
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # Deleting single record now
        sql_delete_query = """DELETE from Database where id = 2"""
        cursor.execute(sql_delete_query)
        sqliteConnection.commit()
        print("Record deleted successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete record from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")

deleteRecord()