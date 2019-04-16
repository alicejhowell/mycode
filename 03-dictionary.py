#!/usr/bin/python3

#this is a dictionary, they work off key: value pairs
#{} are used to work with dictionaries
#keys --------> values
servers = {"fluffy": "10.0.0.2", "whiskers": "192.168.5.10", "socks": "172.7.7.7"}
print("here is the original dictionary ")
print(servers)

#display the value for fluffy
#dictionary is server
print('\n' + "here comes fluffy " + servers['fluffy'])

print("and here comes socks " + servers["socks"])

#add an entry
servers["mittens"] = "8.8.8.8"

print("our new dictionary looks like...")
print(servers)

#use a different method to add an entry
servers.update({"timmy": "192.168.3.2", "rodney": "84.32.5.6"})

print('\n' + "our really new dictionary looks like...")
print(servers)
input("press enter to exit")


#if run multiple times, it should overwrite the old key value or maybe error out?

