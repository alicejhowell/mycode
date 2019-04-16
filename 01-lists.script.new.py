#!/usr/bin/python3

input("press enter to continue")

#Read data from a file
mydata = open('01-lists.txt', 'r')
input("grrrr")
#same as mydata = open('01-lists.txt', 'r') 
#r=read, default mode

#create a list of lines
mylist = mydata.readlines()

#close the file
mydata.close()

input("input")

mylist.append('netscout')
mylist.append('aws\n')
mylist.append('microsoft')


#write data, w=write
outdata = open('01-newlists.txt','w')

for vendor in mylist:
    #push mylist to outdata (01-newlists.txt)
    outdata.write(vendor.rstrip('\n') + '\n')

#close our new file
outdata.close()



input("Press enter to exit")

