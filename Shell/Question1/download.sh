#!/bin/sh
file = $1
search = $2

#Get all the html files from the website recursevily
wget -r --accept=html $1 -o new
#Search for pattern
grep -nr $1 -e $2