import xml.etree.ElementTree as ET
import pprint
from tkinter import *
import socket
import json
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

PARSEFILE = "UNData.xml"
country_set = set()


def parse_xml_file(filename):
    root = ET.parse(filename).getroot()
    for element in root.findall("data/record"):
        country = element.find("Country").text
        country_set.add(country)


class Client:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 5000
        self.client_socket = socket.socket()
        self.client_socket.connect((self.host, self.port))

    def send_data(self, country):
        # print(f"country is: {country}")
        self.client_socket.send(country.encode())


class UNDataUserInterface:
    def __init__(self):
        options = sorted(list(country_set))
        self.master = Tk()
        self.frame = Frame(self.master)  # added

        self.master.geometry("800x800")
        self.master.title("UN Data")

        self.frame.pack()

        self.variable = StringVar(self.master)
        self.variable.set(options[0])  # default value
        self.client = Client()

        w = OptionMenu(self.frame, self.variable, *options)
        w.pack()

        button = Button(self.master, text="DRAW XY PLOT", command=self.ok)
        button.pack()
        self.canvas = None

    def draw_front_end(self):
        self.master.mainloop()

    def ok(self):
        country = self.variable.get()
        print(f"Sending country is {country}")
        self.client.send_data(country)
        data = self.client.client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)
        obj = json.loads(data)
        years = []
        values = []
        for k, v in obj.items():
            years.append(int(k))
            values.append(v)
        print(years)
        print(values)
        self.draw_xy_plot_command(country, years, values)

    def draw_xy_plot_command(self, cou, x, y):
        print(x)
        print(y)
        print(min(y), max(y))
        try:
            self.canvas.get_tk_widget().pack_forget()
        except AttributeError:
            pass

        fig = Figure(figsize=(7, 6), dpi=100)
        plot = fig.add_subplot(111, xmargin=20, ymargin=20, xscale="linear")
        plot.axis([min(x) - 1, max(x) + 1, min(y), max(y)])
        plot.set_xlabel('Year')
        plot.set_ylabel('UN DATA Value')
        plot.plot(x, y)
        plot.title.set_text(f"{cou} UNData")

        self.canvas = FigureCanvasTkAgg(fig, master=self.master)
        self.canvas.get_tk_widget().pack()

    def __del__(self):
        self.client.client_socket.close()


if __name__ == "__main__":
    parse_xml_file(PARSEFILE)  # To get Country list to display in drop down menu
    userInterface = UNDataUserInterface()  # Initiates the object
    userInterface.draw_front_end()  # Draw the frontend for the user interface


