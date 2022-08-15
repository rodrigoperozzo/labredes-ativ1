import socket

# this is the target ip
IP = socket.gethostbyname(socket.gethostname())

PORT = 10001
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

""" Staring a TCP socket. """
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

""" Connecting to the server. """
client.connect(ADDR)

""" Opening and reading the file data. """
file = open("../data/test.txt", "r")
data = file.read()


""" Breaking files into max size chunks. """
""" Sending the file data to the server. """
while (len(data) > 1024):
    dataToSend = data[0 : 1023]
    data = data[1024:]
    client.send(dataToSend.encode(FORMAT))

client.send(data.encode(FORMAT))
msg = client.recv(SIZE).decode(FORMAT)
print(f"[SERVER]: {msg}")

""" Closing the file. """
file.close()

""" Closing the connection from the server. """
client.close()