#!/usr/bin/env python
import urllib
import os
import time

shared_file = "../Question1/shared_file/time.txt"

while True:
    cur_time = os.stat(shared_file)
    #create if not exists
    os.system("touch last_time_shared_file.txt")
    with open("last_time_shared_file.txt","r+") as f:
        f.seek(0,0)
        last_time = f.read()
        f.seek(0,0)
        if len(last_time) == 0:
            #init
            f.write(str(cur_time.st_mtime))
            f.seek(0,0)
        elif str(cur_time.st_mtime) != last_time:
            #change
            contents = urllib.urlopen("http://localhost:5000").read()
            print(contents)
            #update
            f.seek(0,0)
            f.write(str(cur_time.st_mtime))
            f.seek(0,0)
        else:
            print("not modified")
    #yield
    time.sleep(1)
        

