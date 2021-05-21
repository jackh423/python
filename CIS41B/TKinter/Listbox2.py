from tkinter import *

master = Tk()
master.geometry("500x300")

def OnDouble(event):
    widget = event.widget
    selection = widget.curselection()
    value = widget.get(selection[0])
    print("selection:", selection, ": '%s'" % value)
        
lbox=Listbox(master, background="white", fg="black",selectbackground="blue",highlightcolor="black")
lbox.grid(row=1, column=1)
lbox.insert("end", "one")
lbox.insert("end", "two")
lbox.insert("end", "three")
lbox.bind("<Double-Button-1>", OnDouble)
lbox.pack(side="top", fill="both", expand=True)

master.mainloop()
