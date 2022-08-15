import socket

# self ip
IP = socket.gethostbyname(socket.gethostname())

PORT = 10000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

msgFromClient       = "Hello UDP Server"
message         = str.encode(msgFromClient)

# Create a UDP socket at client side
UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(message, ADDR) 

msgFromServer = UDPClientSocket.recvfrom(SIZE)

msg = "Message from Server {}".format(msgFromServer[0])

print(msg)