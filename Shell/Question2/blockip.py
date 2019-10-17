#!/usr/bin/env python

import sys
import re
import os

if (len(sys.argv) != 3):
    raise AttributeError("Invalid number of command line args")

ipfile = sys.argv[1]
mins = sys.argv[2]

ipregex = re.compile(r'([\d]+.[\d]+.[\d]+.[\d]+)')

with open(ipfile,"r") as f:
     ips = f.read()

ip_list = ipregex.findall(ips)

for ip in ip_list:
    ip_block_cmd = "iptables -A INPUT -s {} -j DROP".format(ip)
    os.system(ip_block_cmd)
    #add unblock cmd to 'at' job to unblock them after now + 'mins'
    os.system("echo 'iptables -D INPUT -s {} -j DROP'.format | at now + {} min".format(ip,mins))