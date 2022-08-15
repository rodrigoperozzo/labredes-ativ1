
import socket

# self ip
IP = socket.gethostbyname(socket.gethostname())

PORT = 10000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

msgFromServer       = "Hello UDP Client"

bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind(ADDR)

print("UDP server up and listening")

# Listen for incoming datagrams
while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(SIZE)

    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)