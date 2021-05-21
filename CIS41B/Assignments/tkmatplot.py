
from tkinter import *
# from tkinter.ttk import *

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use("TkAgg")


root = Tk()
figure = Figure(figsize=(6, 4), dpi=100)
plot = figure.add_subplot(1, 1, 1)
canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().grid(row=0, column=0)
# plot.plot(0.5, 0.3, color="#C41E3A", marker="o", linestyle="")
# x = [ 0.1, 0.2, 0.3 ]
# y = [ -0.1, -0.2, -0.3 ]
x = [1950, 1951, 1952]
y = [-0.3, 0.1, -0.2]
# plot.plot(x, y, color="blue", marker="x", linestyle="")
plot.plot(x, y)
plot.axis([1949, 1960, -1, +1])
# plot.xlabel("Year")
# plot.ylabel("Temperature")
plot.set_xlabel('Year')
plot.set_ylabel('Temperature')
root.mainloop()


#
# import matplotlib.pyplot as plt
#
# years = [1950, 1951, 1952]
# med_temps = [-0.3, 0.1, -0.2]
# plt.plot(years, med_temps)
# plt.axis([ 1950, 1960, -1, +1])
# plt.xlabel("Year")
# plt.ylabel("Temperature")
# plt.show()










# import numpy as np
# from matplotlib.figure import Figure
# from tkinter import *
#
# class mclass:
#     def __init__(self,  window):
#         self.window = window
#         self.box = Entry(window)
#         self.button = Button (window, text="check", command=self.plot)
#         self.box.pack ()
#         self.button.pack()
#
#     def plot (self):
#         x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#         v= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,22.81226])
#         p= np.array ([16.23697,     17.31653,     17.22094,     17.68631,     17.73641 ,    18.6368,
#             19.32125,     19.31756 ,    21.20247  ,   22.41444   ,  22.11718  ,   22.12453])
#
#         fig = Figure(figsize=(6,6))
#         a = fig.add_subplot(111)
#         a.scatter(v,x,color='red')
#         a.plot(p, range(2 +max(x)),color='blue')
#         a.invert_yaxis()
#
#         a.set_title ("Estimation Grid", fontsize=16)
#         a.set_ylabel("Y", fontsize=14)
#         a.set_xlabel("X", fontsize=14)
#
#         canvas = FigureCanvasTkAgg(fig, master=self.window)
#         canvas.get_tk_widget().pack()
#         canvas.draw()
#
# window= Tk()
# start= mclass (window)
# window.mainloop()