from nmap import PortScanner
import ipaddress
import socket
import subprocess

class IPDiscover:
    def __init__(self):
        self.my_ip = socket.gethostbyname(socket.gethostname())
        print(self.my_ip)

    def nmap_test(self):
        network_address = self.my_ip
        print('Scanner in progress')

        map = PortScanner()
        map.scan(hosts=network_address, arguments='-sn')

        ip_list = []
        for i in map.all_hosts():
            ip_list.append(i, map[i]['status']['state'])

        for host, status in ip_list:
            print('Host\t{}'.format(host))

    def ipaddress_test(self):
        network = ipaddress.ip_network(self.my_ip + '/16', False)
        #host_list = list(network.hosts())
        #for i in range(len(host_list)):
        #    print(host_list[i])
        for x in network.hosts():
            res = subprocess.call(['ping', '-c', '3', str(x)])
            if res == 0:
                print(x)


network = IPDiscover()
network.ipaddress_test()