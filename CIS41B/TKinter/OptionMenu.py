data = [
 "Belgium",
 "Hungary",
 "Chile",
 "France",
 "Mexico",
 "Hong Kong",
 "Turkey",
 "Ireland",
 "Ghana",
 "Argentina",
 "Slovakia"
]

from tkinter import *

def Country(s):
    print(s)
    
master = Tk()
variable = StringVar()
variable.set(data[0]) # default value
w = OptionMenu(master, variable, *data, command=Country).pack()

mainloop() 
