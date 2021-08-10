import os
import re

class ARPTable():
    def __init__(self):
        self.arp_table = []

    def form_table(self):
        with os.popen('arp -a') as f:
            read = f.read()

        for data in re.findall('([-.0-9]+)\s+([-0-9a-f]{17})\s+(\w+)', read):
            self.arp_table.append({'ip': data[0], 'physical': data[1], 'type': data[2]})

        self.print_table()

    def print_table(self):
        print('ARP Table')
        print('IP Address\t\tPhysical Address\tType')
        for ip_info in self.arp_table:
            print('{}\t\t{}\t{}'.format(ip_info['ip'], ip_info['physical'], ip_info['type']))

arp = ARPTable()
arp.form_table()