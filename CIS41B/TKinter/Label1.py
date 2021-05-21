from tkinter import * 

window = Tk() 
window.title("Edit Box") 
window.geometry('500x300') 
lbl = Label(window, text="Button Clicked") 
lbl.grid(column=0, row=0) 

def clicked(): 
    lbl.configure(text="Button was clicked") 

btn = Button(window, text="Click Me", fg='green', command=clicked) 
btn.grid(column=1, row=0) 
window.mainloop() 

