import socket

def client_connection(ip, port, data):
    ip = str(ip)
    port = int(port)
    request = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        request.connect((ip, port))
        request.send(data)
        data = request.recv(1024)
        request.close()
    except:
        data = "Connection Failed"
    return data