import os,socket,threading

# Server Important Constants
HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
FORMAT = 'utf-8'
DISC_MSG = "!DISCONNECT"
ADDRESS = (SERVER,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDRESS)

def client_handle(con,addr):
    print(f"New connection -> {addr}")
    connected = True
    
    while connected:
        msg_len = con.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = con.recv(msg_len).decode(FORMAT)

            if(msg == DISC_MSG):
                connected = False
            print(f"[{addr}]{msg}")
            con.send("REPLY".encode(FORMAT))
            
    con.close()


def listen():
    server.listen()
    print(f"Server IP {SERVER}")
    while True:
        con, addr = server.accept()
        thread = threading.Thread(target=client_handle,args=(con,addr))
        thread.start()
        print(f"Current Thread Connections -> {threading.activeCount() - 1}")

print("Server is connecting ...")
listen()