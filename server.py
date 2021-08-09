import client_file
import socket
import threading
import os

class Server(threading.Thread):
    def __init__(self, ip, port, m, finger):
        threading.Thread.__init__(self)
        self.dead = False
        self.ip = str(ip)
        self.port = int(port)
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.m = int(m)
        self.total_nodes = 2 ** self.m
        self.finger_arr = finger
        self.finger_table = {}
        self.position = hash(self.ip + str(self.port)) % (self.total_nodes)
        self.predecessor = None
        self.accept_connections()
        
    
    def accept_connections(self):
        # self.ip = socket.gethostbyname(socket.gethostname())
        # self.port = int(input('Enter desired port --> '))

        self.s.bind((self.ip, self.port))
        self.s.listen(100)

        print('Running on IP: '+ self.ip)
        print('Running on port: ' + str(self.port))
        print('Node at position: ', self.position)

        while 1:
            c, addr = self.s.accept()
            #print(c)
            
            threading.Thread(target=self.handle_client,args=(c,addr,)).start()
            print(f"Current Thread Connections -> {threading.activeCount() - 1}")

    def print_finger_table(self):
        for key in self.finger_table:
            print(key, self.finger_table[key][1], ":", self.print_finger_table[key][2])

    def create_ring(self):
        self.predecessor = [self.position, self.ip, self.port]
        for i in range(self.m):
            self.finger_table[i] = [self.position, self.ip, self.port]

    # def handle_client(self,c,addr):
    #     data = c.recv(1024).decode()
    #     print(data)
    #     if data == "!DISCONNECT":
    #         c.shutdown(socket.SHUT_RDWR)
    #         c.close()
    #         print("Client disconnected")
    #         print(f"Current Thread Connections -> {threading.activeCount() - 1}")
        
    #     elif not os.path.exists(data):
    #         c.send("file-doesn't-exist".encode())

    #     else:
    #         c.send("file-exists".encode())
    #         print('Sending',data, "to client: ", addr)
    #         if data != '':
    #             file = open(data,'rb')
    #             data = file.read(1024)
    #             while data:
    #                 c.send(data)
    #                 data = file.read(1024)

    #             c.shutdown(socket.SHUT_RDWR)
    #             c.close()
        

    # def listen(self):
    #     self.s.listen()
    #     print(f"Server IP {self.ip}")
    #     while True:
    #         con, addr = server.accept()
    #         thread = threading.Thread(target=handle_client, args=(con,addr))
    #         thread.start()
    #         print(f"Current Thread Connections -> {threading.activeCount() - 1}")


print("Server is connecting ...")
server = Server()
