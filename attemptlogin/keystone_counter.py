#!/usr/bin/python3
loginfail = 0
logingood = 0

keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")
keystone_file_lines=keystone_file.readlines()
for line in keystone_file_lines:
    if "- -] Authorization failed" in line:
# this is the same as loginfail = loginfail + 1
        loginfail += 1
    else:
        logingood += 1

print("the number of failed log in attempts " + str(loginfail))
print("\n" + "the number of good log in attempts " + str(logingood))
