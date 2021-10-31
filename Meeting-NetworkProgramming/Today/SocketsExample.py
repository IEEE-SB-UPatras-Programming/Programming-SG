import socket
import pickle

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.bind(("127.0.0.1", 1234))


