#!/usr/bin/env python3

import os

pwd = os.getcwd()

with open("docker-compose.service", "rt") as fin:
    with open("docker-compose_pwd.service", "wt") as fout:
        for line in fin:
            fout.write(line.replace('/home/pavan/Softwares/DevOps/Question2', pwd))

os.system("cp docker-compose_pwd.service /etc/systemd/system/read_write_service.service && rm docker-compose_pwd.service")
#start it
os.system("systemctl start read_write_service")
#enable it for bootup start
os.system("systemctl enable read_write_service")