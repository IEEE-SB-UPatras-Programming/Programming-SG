import selectors
import socket

socketSelector = selectors.DefaultSelector()

def doAccept(socket, mask):

    connection, address = socket.accept()

    print("Accepted connection!")
    
    connection.setblocking(False)    

    socketSelector.register( connection, selectors.EVENT_READ, doRead )

def doRead(connection, mask):

    data = connection.recv(1000)

    if data:
        print( "Echoing: ", repr(data), "to", connection )
        connection.send(data)
    else: 
        print( "Closing: ", connection )
        socketSelector.unregister(connection)
        connection.close()

def main():

    ip, port = "127.0.0.1", 1235

    serverSocket = socket.socket()

    serverSocket.bind((ip, port))

    serverSocket.listen(10)

    serverSocket.setblocking(False)

    socketSelector.register(serverSocket, selectors.EVENT_READ, doAccept)

    print("Server running on port ", port)

    while True:

        events = socketSelector.select()

        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)

if __name__ == "__main__":
    main()
