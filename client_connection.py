import socket

HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
FORMAT = 'utf-8'
DISC_MSG = "!DISCONNECT"
SERVER = "192.168.56.1"
ADDRESS = (SERVER,PORT)
client  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(ADDRESS)

def send_message(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_len = str(msg_length).encode(FORMAT)
    send_len += b' ' *(HEADER - len(send_len))
    client.send(send_len)
    client.send(message)
    print(client.recv(2048))

send_message("TEST!")
input()
send_message("CLEARING TEST")
input()
send_message(DISC_MSG)