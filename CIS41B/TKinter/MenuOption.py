from tkinter import*

def selected(value):
    print(value)

root = Tk()
root.geometry("500x300")
options = ["Option1","Option2","Option3"]
var = StringVar()
menu = OptionMenu(root,var,*options,command=selected)
menu.place(x=1,y=1)

root.mainloop()
