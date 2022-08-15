
import socket

# self ip
IP = socket.gethostbyname(socket.gethostname())

PORT = 10001
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

print("[STARTING] Server is starting.")
""" Staring a TCP socket. """
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

""" Bind the IP and PORT to the server. """
server.bind(ADDR)

""" Server is listening, i.e., server is now waiting for the client to connected. """
server.listen()
print("[LISTENING] Server is listening.")

while True:
    """ Server has accepted the connection from the client. """
    conn, addr = server.accept()
    print(f"[NEW CONNECTION] {addr} connected.")

    """ Receiving the file data from the client. """
    while True:
        data = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the file data.")
        file = open("recv.txt", "a")
        file.write(data)
        print(f"data: {data}")
        
    conn.send("File data received".encode(FORMAT))
    
    """ Closing the file. """
    file.close()

    """ Closing the connection from the client. """
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")
