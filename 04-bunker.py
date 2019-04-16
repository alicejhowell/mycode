#!/usr/bin/python3

#open file1 - "bunker east"
bedata = open('bunkereast.txt', 'r')

#open file2 - "bunker west"
bwdata = open('bunkerwest.txt', 'r')

input("grrrr")

#read file1 - "bunker east"
belines = bedata.readlines()

#read file2 - "bunker west"
bwlines = bwdata.readlines()

#close file1 - "bunker east"
bedata.close()

#close file2 - "bunker west"
bwdata.close()

input("press enter")

#create a single file of all our lines
bafile = open('bunkerall.txt', 'w')
#loop bunker east lines
for switch in belines:
    bafile.write('e-' + switch.rstrip('\n') + '\n')
#loop bunker west lines
for switch in bwlines:
    bafile.write('w-' + switch.rstrip('\n') + '\n')
bafile.close()


#read in all lines from single file
bafile = open('bunkerall.txt', 'r')
balines = bafile.readlines()
#create a new file for ips only
bafileip = open('bunkerips.txt', 'w')
for line in balines:
    bafileip.write(line.split(' ')[1])

bafileip.close()
bafile.close()


input("press enter again")

