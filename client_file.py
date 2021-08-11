import socket
import os

HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
FORMAT = 'utf-8'
DISC_MSG = "!DISCONNECT"
SERVER = "192.168.1.165"
ADDRESS = (SERVER,PORT)
class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connect_to_server()

    def connect_to_server(self):
        self.target_ip = input('Enter ip --> ')
        self.target_port = input('Enter port --> ')

        self.s.connect((self.target_ip,int(self.target_port)))

        self.main()

    def reconnect(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((self.target_ip,int(self.target_port)))

    def send_message(self, msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_len = str(msg_length).encode(FORMAT)
        send_len += b' ' *(HEADER - len(send_len))
        self.s.send(send_len)
        self.s.send(message)
        print(client.recv(2048))

    def main(self):
        while 1:
            file_name = input('Enter file name on server --> ')
            self.s.send(file_name.encode())

            confirmation = self.s.recv(1024)
            if confirmation.decode() == "file-doesn't-exist":
                print("File doesn't exist on server.")

                self.s.shutdown(socket.SHUT_RDWR)
                self.s.close()
                self.reconnect()

            else:        
                write_name = 'from_server '+ file_name
                if os.path.exists(write_name): os.remove(write_name)

                with open(write_name,'wb') as file:
                    while 1:
                        data = self.s.recv(1024)

                        if not data:
                            break

                        file.write(data)

                print(file_name,'successfully downloaded.')

                self.s.shutdown(socket.SHUT_RDWR)
                self.s.close()
                self.reconnect()
        
                
client = Client()