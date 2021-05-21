import tkinter as tk
win = tk.Tk()

# globals
can = tk.Canvas(win, width=300, height=300)
strvar = tk.StringVar()
lab = tk.Label(win, textvar=strvar)
strvar.set("Press a key")

def Click(event=None):
    canvas_id = can.create_text(event.x, event.y, anchor="nw")
    can.itemconfig(canvas_id, text=str(event.x)+',')
    can.insert(canvas_id, 10, str(event.y))

def Key_down(event=None):
    strvar.set(event.keysym)

def UC_at(event=None):
    top = tk.Toplevel(win)
    top.geometry("200x200")
    sv = tk.StringVar()
    sv.set("Hover the mouse over me")
    label = tk.Label(top, textvar=sv)
    label.bind("<Enter>", lambda e, sv=sv: sv.set("Hello mouse!"))
    label.bind("<Leave>", lambda e, sv=sv: sv.set("Goodbye mouse!"))
    label.pack(expand=1, fill=tk.BOTH)

def Binder():
    can.bind('<Button-1>', Click)
    win.bind('<@>', UC_at)
    win.bind('<KeyPress>', Key_down)
    win.bind('<e>', lambda e, s=lab: lab.configure(font=(None, 18)))
    can.pack()
    lab.pack(side=tk.BOTTOM)

def main():
    Binder()
    win.mainloop()

main()
