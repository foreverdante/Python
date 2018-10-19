#!/usr/local/env python3
#Created By: J.Medlock
#Created On: 2017.09.22

from socket import *
network = str(input("Please enter the network you would like to scan: "))

def is_up(addr):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(0.01)
    if not s.connect_ex((addr, 135)):
        s.close()
        return 1
    else:
        s.close()

def run():
    print("")
    for ip in range(1, 256):
        addr = network + str(ip)
        if is_up(addr):
            print("%s \t- %s" % (addr, getfqdn(addr)))
    print

if __name__ == "__main__":
    print("Scanning entire network for devices that are up")
    run()
    input("Done")
        
