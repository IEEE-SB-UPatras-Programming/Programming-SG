import socket

def HTTP_Request(server, path):

    # Creating a socket to connect and read from
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Finding server address (assuming port 80)
    adr=(socket.gethostbyname(server), 80)

    # Connecting to server
    s.connect(adr)

    # Sending request
    s.send("GET {} \n\n".format(path).encode())

    # Printing response
    resp=s.recv(1024)
    while resp.decode() != "":
        print((resp.decode()))
        print()
        resp=s.recv(1024)


HTTP_Request("google.com", "/")


# from urllib.request import urlopen
# html = urlopen("https://vagoslabrou.xyz/")
# print(html.read())
