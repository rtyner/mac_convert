# types of macs to convert from/to
# eui48 - 71-54-ED-69-9B-E9
# unix - 71:54:ed:69:9b:e9
# cisco - 7154.ed69.9be9
# bare - 7154ED699BE9

import sys
import netaddr
from netaddr import EUI

# take file as input
in_file = sys.argv[1]

def convert_mac(octet):
    return EUI(netaddr.strategy.eui48.packed_to_int(octet))

# take input here to act on later
mac_type = input("What format do you want to convert to? Bare, Cisco, EUI48, or Unix: ")

with open(in_file,'r') as i: # open and read file
    lines = i.readlines()
    for line in lines:
        mac = EUI(line)
        if mac_type == str('Cisco'):
            mac.dialect = netaddr.mac_cisco
            print(mac) 
        elif mac_type == str('Bare'):
            mac.dialect = netaddr.mac_bare
            print(mac)
        elif mac_type == str('Unix'):
            mac.dialect = netaddr.mac_unix_expanded
            print(mac)
        elif mac_type == str('EUI48'):
            mac.dialect = netaddr.mac_eui48
            print(mac)
