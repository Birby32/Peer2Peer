from scapy.all import ARP, Ether, srp

class IPScanner:
    def __init__(self, ip=None):
        print(ip)
        if ip is None:
            self.target_ip_address = input('Enter the target IP Address --> ')
        else:
            self.target_ip_address = ip
        self._available_devices = []
        self._available_physical_address = []
        self.scapy_scan()

    def get_available_devices(self):
        return self._available_devices

    def get_available_physical_address(self):
        return self._available_physical_address

    def scapy_scan(self):
        # Adding /24 to the end of the target ip in order to search through
        # the range of xxx.xxx.x.0 and xxx.xxx.x.255
        self.target_ip_address = self.target_ip_address + '/24'

        arp_call = ARP(pdst=self.target_ip_address)
        broadcast_ether = Ether(dst='ff:ff:ff:ff:ff:ff')
        packet = broadcast_ether/arp_call

        result = srp(packet, timeout=3)[0]

        for sent, received in result:
            # calls in the received packets from the result
            self._available_devices.append(received.psrc)           # ip address
            self._available_physical_address.append(received.hwsrc) # physical address
        
        print('Available devices in the network:')
        print('\nIP Address')
        for ip in self._available_devices:
            print(ip)

#network = IPScanner()
