#!/usr/bin/env python

import datetime

time = datetime.datetime.now()
time = time.strftime("%Y-%m-%dT%H:%M:%S.%f")
print(time)

with open("/app/time.txt", "a") as f:
    f.write(time+"\n")