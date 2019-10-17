#!/usr/bin/env python3

import os

pwd = os.getcwd()

with open("check_shared_file.service", "rt") as fin:
    with open("check_shared_file_pwd.service", "wt") as fout:
        for line in fin:
            fout.write(line.replace('/home/pavan/Softwares/DevOps/Question2', pwd))

os.system("cp check_shared_file_pwd.service /etc/systemd/system/check_shared_file.service && rm check_shared_file_pwd.service")
#start it
os.system("systemctl start check_shared_file")
#enable it for bootup start
os.system("systemctl enable check_shared_file")