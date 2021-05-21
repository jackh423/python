
import socket

class Client:
    def __init__(self,nport):
        self.host = socket.gethostname()  # as both code is running on same pc
        self.port = nport  # socket server port number
        self.client_socket = socket.socket()  # instantiate
        self.client_socket.connect((self.host, self.port))  # connect to the server
    def Connect(self):
        message = input(" -> ")  # take input
        while message.lower().strip() != 'bye':
            self.client_socket.send(message.encode())  # send message
            data = self.client_socket.recv(1024).decode()  # receive response
            print('Received from server: ' + data)  # show in terminal
            message = input(" -> ")  # again take input
        self.client_socket.close()  # close the connection

if __name__ == '__main__':
    client = Client(5000)
    client.Connect()
