#!/usr/bin/python3

counter = 0

## open the file and read all lines into the list mylines
with open("keystone.common.wsgi", "r") as keyfile:
    mylines = keyfile.readlines()
    for line in mylines:
        if "- - - - -] Authorization failed" in line:
            counter += 1
keyfile.close()

print("the number of failed logins is: ", counter)

counter = 0

## open the file and read line by line
with open("keystone.common.wsgi") as keyfile:
    for line in keyfile:
        if "- - - - -] Authorization failed" in line:
            counter += 1
keyfile.close()

print("the number of failed logins is: ", counter)

