import socket
import threading
import os

class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.accept_connections()
    
    def accept_connections(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = int(input('Enter desired port --> '))

        self.s.bind((self.ip, self.port))
        self.s.listen(100)

        print('Running on IP: '+ self.ip)
        print('Running on port: '+str(self.port))

        while 1:
            c, addr = self.s.accept()
            #print(c)
            
            threading.Thread(target=self.handle_client,args=(c,addr,)).start()
            print(f"Current Thread Connections -> {threading.activeCount() - 1}")

    def handle_client(self,c,addr):
        data = c.recv(1024).decode()
        print(data)
        if data == "!DISCONNECT":
            c.shutdown(socket.SHUT_RDWR)
            c.close()
            print("Client disconnected")
            print(f"Current Thread Connections -> {threading.activeCount() - 1}")
        
        elif not os.path.exists(data):
            c.send("file-doesn't-exist".encode())

        else:
            c.send("file-exists".encode())
            print('Sending',data, "to client: ", addr)
            if data != '':
                file = open(data,'rb')
                data = file.read(1024)
                while data:
                    c.send(data)
                    data = file.read(1024)

                c.shutdown(socket.SHUT_RDWR)
                c.close()

    def listen(self):
        self.s.listen()
        print(f"Server IP {self.ip}")
        while True:
            con, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(con,addr))
            thread.start()
            print(f"Current Thread Connections -> {threading.activeCount() - 1}")

print("Server is connecting ...")
server = Server()
# server.listen()