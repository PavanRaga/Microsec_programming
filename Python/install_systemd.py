#!/usr/bin/env python3

import os

pwd = os.getcwd()

with open("myserver.service", "rt") as fin:
    with open("myserver_pwd.service", "wt") as fout:
        for line in fin:
            fout.write(line.replace('/home/pavan/Softwares/microsec/Python', pwd))

os.system("cp myserver_pwd.service /etc/systemd/system/myserver.service && rm myserver_pwd.service")
#start it
os.system("systemctl start myserver")
#enable it for bootup start
os.system("systemctl enable myserver")