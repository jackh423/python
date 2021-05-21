import xml.etree.ElementTree as ET
import pprint
from tkinter import *
import socket
import json
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import matplotlib.pyplot as plt


PARSEFILE = "UNData.xml"

country_set = set()


class Client:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 5000
        self.client_socket = socket.socket()
        self.client_socket.connect((self.host, self.port))

    def Connect(self):
        while True:
            # send_data()
            # message = get_data()
            # self.client_socket.send(message.encode())
            print("I am waiting in client receive loop")
            data = self.client_socket.recv(4096).decode("ascii")  # receive response
            print('Received from server: ' + data)  # show in terminal
            # message = input(" -> ")  # again take input
        self.client_socket.close()

    def send_data(self, country):
        print(f"country is: {country}")
        self.client_socket.send(country.encode())


# def client_program():
    # host = socket.gethostname()
    # port = 5000
    # client_socket = socket.socket()
    # client_socket.connect((host, port))
    # message = input(" -> ")
    # while message.lower().strip() != 'bye':
    #     client_socket.send(message.encode())  # send message
    #     data = client_socket.recv(1024).decode()  # receive response
    #
    #     print('Received from server: ' + data)  # show in terminal
    #
    #     message = input(" -> ")  # again take input
    #
    # client_socket.close()


# def send_data(country):
#     pass

def parse_xml_file(filename):
    root = ET.parse(filename).getroot()
    # print(root.tag)
    count = 0
    for element in root.findall("data/record"):
        # print(element.tag)
        country = element.find("Country").text
        year = element.find("Year").text
        value = element.find("Value").text
        # print(country, year, value)
        country_set.add(country)
        count += 1
        # if country != "Australia":
        #     break
    # print(count)
    # pprint.pprint(country_set)


class UNDataUserInterface:
    def __init__(self):
        options = sorted(list(country_set))
        self.master = Tk()
        self.frame = Frame(self.master)  # added

        self.master.geometry("600x600")
        self.master.title("UN Data")

        self.frame.pack()

        self.variable = StringVar(self.master)
        self.variable.set(options[0])  # default value
        self.client = Client()

        # w = OptionMenu(self.master, self.variable, *options)  # commented
        w = OptionMenu(self.frame, self.variable, *options)
        w.pack()

        button = Button(self.master, text="DRAW XY PLOT", command=self.ok)
        button.pack()
        self.canvas = None

    def draw_front_end(self):
        self.master.mainloop()

    def ok(self):
        print("value is:" + self.variable.get())
        country = self.variable.get()
        print(f"country is: {country}")
        # self.client_socket.send(country.encode())
        print("I am sending data")
        self.client.send_data(self.variable.get())
        print("I am waiting in client receive loop")
        data = self.client.client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)
        print(type(data))
        obj = json.loads(data)
        years = []
        values = []
        for k, v in obj.items():
            years.append(int(k))
            values.append(v)
        print(years)
        print(values)
        self.draw_xy_plot_command(years, values)

        # self.client_socket.send(country.encode())

        # self.call_client()

    def call_client(self):
        self.client.connect()
        # self.client

    def draw_xy_plot_command(self, x, y):
        try:
            self.canvas.get_tk_widget().pack_forget()
        except AttributeError:
            pass

        fig = Figure(figsize=(6, 5), dpi=100)

        plot = fig.add_subplot(111, xmargin=2, ymargin=2, xscale="linear")

        plot.axis([min(x) - 1, max(x) + 1, min(y), max(y)])

        plot.set_xlabel('Year')
        plot.set_ylabel('UN DATA Value')
        plot.plot(x, y)

        self.canvas = FigureCanvasTkAgg(fig, master=self.master)

        self.canvas.get_tk_widget().pack()

    def __delete__(self, instance):
        self.client.client_socket.close()



# def draw_drop_down_menu():
#     OPTIONS = sorted(list(country_set))
#     # client = Client()
#     # client.connect()
#     master = Tk()
#     master.geometry("600x600")
#     master.title("UN Data")
#     variable = StringVar(master)
#     variable.set(OPTIONS[0])  # default value
#
#     w = OptionMenu(master, variable, *OPTIONS)
#     w.pack()
#
#     def ok(self):
#         print("value is:" + variable.get())
#         self.client.send_data(variable.get())
#
#     button = Button(master, text="DRAW XYPLOT", command=ok)
#     button.pack()
#
#     mainloop()


if __name__ == "__main__":
    parse_xml_file(PARSEFILE)
    # draw_drop_down_menu()
    # client_program()
    userInterface = UNDataUserInterface()
    # userInterface.call_client()
    userInterface.draw_front_end()


