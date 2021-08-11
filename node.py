import socket
import os
import sys
import server

ip = input("Enter IP of node: ")
ip = str(ip)
port = input("Enter port to be used: ")
port = int(port)
m = 10
finger = [-1 for i in range(m)]

active_server = server.Server(ip, port, m, finger)
active_server.start()
