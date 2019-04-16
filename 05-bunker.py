#!/usr/bin/python3

bunkerdict = {}
bedata = open('bunkereast.txt', 'r')
belist = bedata.readlines
bedata.close()
for line in belist:
    hostip = line.split(' ')
    bunkerdict[hostip[0]] = hostip[1].rstrip('\n')

eastwest = {}
eastwest.update(east: bunkerdict)
print(eastwest)

bunkerdict.clear()
#!/usr/bin/python3

bunkerdict = {}
bedata = open('bunkereast.txt', 'r')
belist = bedata.readlines
bedata.close()
for line in belist:
    hostip = line.split(' ')
    bunkerdict[hostip[0]] = hostip[1].rstrip('\n')

eastwest = {}
eastwest.update(east: bunkerdict)
print(eastwest)

bunkerdict.clear()
bwdata = open('bunkerwest.txt', 'r')
bwlist = bwdata.readlines()
bwdata.close()
for line in bwlist:
    hostip = line.split(' ')
    bunkerdict[hostip[0]] = hostip[1].rstrip('\n')

eastwest.update({"west": bunkerdict})
print(eastwest)

input("press enter to exit")
bwdata = open('bunkerwest.txt', 'r')
bwlist = bwdata.readlines()
bwdata.close()
for line in bwlist:
    hostip = line.split(' ')
    bunkerdict[hostip[0]] = hostip[1].rstrip('\n')

eastwest.update({"west": bunkerdict})
print(eastwest)

input("press enter to exit")

