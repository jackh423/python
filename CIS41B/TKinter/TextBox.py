import tkinter as tk

root = tk.Tk()
text = tk.Text(root, font=("Helvetica", 18))
text.pack()

handle = open("Poem.txt")
text.insert(tk.END,handle.read())

root.mainloop()
