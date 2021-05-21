from tkinter import *

master = Tk()
master.title("Random line draw")

def line():
    import random
    x1=random.randrange(0,300)
    y1=random.randrange(0,300)
    x2=random.randrange(0,300)
    y2=random.randrange(0,300)
    canvas.create_line(x1, y1, x2, y2)

   
canvas = Canvas(master, width=300, height=300)
canvas.pack(side=TOP)

button=Button(master, text="Click to draw random line", command=line).pack(fill=BOTH)

master.mainloop()