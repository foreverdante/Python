#!/usr/local/env python3
#Created By: J.Medlock
#Created On: 2017.09.22

import nmap
nm = nmap.PortScanner()
ip = str(input("Enter an IP address to scan: "))

nm.scan(ip, '22-443')

for host in nm.all_hosts():
    if nm[host].state() == 'up':
        print('----------------------------')
        host1, domain = nm[host].hostname().split('.', 1)        
        print("Host: %s" % host1)
        print("State: %s" % nm[host].state())
    else:
        print("Something is wrong")
