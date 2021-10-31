# IEEE Programming SG

import socket
import sys
import threading

# Simple server and client.

class Server():

    def __init__(self, host, port):

        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))

        self.socket.listen(10)

        print("Listening to Port: %d" % port)

        self._doListen()

    def _doListen(self):

        while True:

            client, addr = self.socket.accept()

            threading.Thread(target=self._doReceive, args=(client, addr)).start()

    def _doReceive(self, client, address):

        size = 1024

        while True:

            try:
                data = client.recv(header)

                print("Received: %s" % data.decode())
                
                response = self.doHandle(client, data.decode().strip())
                client.sendall(response.encode())

            except socket.error:
                client.close()
                return False

    def doHandle(self, client, message):

        return "[NO RESPONSE]"

class Client():

    def __init__(self, host, port):

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.socket.connect((host, port))
        except socket.error:
            print("Couldn't connect to server!")

            exit()

        while True:

            data = input("> ")
            self.socket.sendall(data.encode())

            while True:

                message = self.socket.recv(4096)
                print("%s" % message.decode())
                break

def main():
        
    host = "127.0.0.1"
    port = 1234

    if sys.argv[1] == "s":

        server = Server(host, port)

    elif sys.argv[1] == "c":

        client = Client(host, port)

if __name__ == "__main__":
    main()
