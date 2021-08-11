import socket
import threading
from threading import Thread
import os
import connection
import random

class Server(Thread):
    def __init__(self, ip, port, m, finger):
        Thread.__init__(self)
        self.dead = False
        self.ip = str(ip)
        self.port = int(port)
        self.heartbeat_listening_ip = ip
        self.heartbeat_listening_port = int(random.randint(10000, 21000))
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.m = int(m)
        self.total_nodes = 2 ** self.m
        self.finger_arr = finger
        self.finger_table = {}
        self.node_table = {}
        self.position = hash(self.ip + str(self.port)) % (self.total_nodes)
        self.predecessor = None
        self.successor = None
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
            c_position = hash(addr[0] + str(addr[1])) % (self.total_nodes)
            self.node_table[c_position] = (addr[0], addr[1])
            for node in self.node_table:
                print(node)
            #print(c)
            
            threading.Thread(target=self.handle_client,args=(c,addr,)).start()
            print(f"Current Thread Connections -> {threading.activeCount() - 1}")

    def send_heartbeat(self):
        if self.dead:
            return
        if self.successor.dead == False:
            connection.client_connection(self.successor.ip, self.successor.port, self.dead)
        return

    def listen_heartbeat(self):
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind((self.heartbeat_listening_ip, self.heartbeat_listening_port))
        listen_socket.listen(5)
        listen_socket.settimeout(10.0)
        while True:
            if self.dead:
                break
            # try:
            #     client, addr = listen_socket.accept()
            #     data_received = client.recv(1024)
            #     send_data = "received"
            #     client.send(send_data)
            #     client.close()
            # except:
            #     print("predecessor dead")
            #     if self.predecessor[0] == self.finger_table[0][0]:
            #         self.predecessor = [self.position, self.ip, self.port]
            #         for i in range(self.m):
            #             self.finger_table[i] = [self.position, self.ip, self.port]



    def print_finger_table(self):
        for key in self.finger_table:
            print(key, self.finger_table[key][1], ":", self.print_finger_table[key][2])

    def create_ring(self):
        self.predecessor = [self.position, self.ip, self.port]
        for i in range(self.m):
            self.finger_table[i] = [self.position, self.ip, self.port]

    def peers(self):
        for peers in self.finger_table:
            print(peers[1], peers[2])
            print()

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
# server = Server()
