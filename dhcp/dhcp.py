#!/usr/local/env python3
#Created By: J.Medlock
#Created On: 2017.09.12

import re

data = "/home/johnny/Programming/python/dhcp/sample-dhcp.conf"

class ComputerSearch:

    def name_lookup(question, data):
        bar = {}
        with open(data, "r") as f:
            for line in f:
                pattern = re.search(r"\s*host\s\s*([^ ]*)\s.*$", line, re.M)
                name = pattern.group(1)
                bar = {name: "test"}
                #if bar is question:
                if pattern:
                    print(bar[0])
    def mac_lookup(self, question):
       pass 

question = str(input("enter a computer name to search for: "))

#info_lookup = ComputerSearch()
#info_lookup.name_lookup(question, data)
ComputerSearch.name_lookup(question, data)
