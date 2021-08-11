from ip_scanner import IPScanner
import os
import sys

class Ping(IPScanner):

    def __init__(self):
        scan = IPScanner(ip='192.168.1.1')
        self.ip_list = scan.get_available_devices()
        self.ip_status = []

    def ping(self):
        # find os build on machine
        my_os = sys.platform
        param = None
        # different os's use different parms for their ping execution command
        if my_os == 'win32':    # windows
            param = '-n'
        else:
            param = '-c'

        # iterate through ip address list
        for ip in self.ip_list:
            # ping with cmd command. append exit status in list
            self.ip_status.append(os.system('ping {} 1 {}'.format(param, ip)))

        self.print_ip_info()

    def print_ip_info(self):
        print('\n\nIP Address\t\tStatus')
        for ip, status in zip(self.ip_list, self.ip_status):
            if status == 0:
                print('{}\t\tOK'.format(ip))
            else:
                print('{}\t\tDISCONNECTED'.format(ip))
    
ping = Ping()
ping.ping()