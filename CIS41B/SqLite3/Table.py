'''
To convert this table code to be a member function of a class:
1.  The sqliteConnection should be a data member of the class and connected.
2.  The function should take a string parameter for the query.  See lines 12-16.
3.  It should return 'true' if table created, otherwise 'false'
'''

import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    sqlite_create_table_query = '''CREATE TABLE Database (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                photo text NOT NULL UNIQUE,
                                html text NOT NULL UNIQUE);'''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")