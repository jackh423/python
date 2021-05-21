'''
To convert this Fetch code to be a member function of a class:
1.  The sqliteConnection should be a data member of the class and connected
2.  The function should take a string parameter for select statement.  See line 16.
3.  It should return 'true' if connected, otherwise 'false'
'''

import sqlite3

#con should be a data member
con = sqlite3.connect('SQLite_Python.db') # this name should be variable

def Fetch(condb,nm):
    cursorObj = con.cursor()
    con.cursor()
    sel = 'SELECT id FROM {0} WHERE name == "{1}"'.format(condb,nm)
    cursorObj.execute(sel)
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)
        
Fetch('Database','name')