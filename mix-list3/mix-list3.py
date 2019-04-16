#!/usr/bin/python3
list1 = ['cisco_nxos', 'arista_eos', 'cisco_ios']
print(list1)
list1.extend(['juniper'])
print(list1)
list1.append(['10.1.0.1', '10.20.1', '10.3.0.2'])
print(list1)
print(list1[4])
print(list1[4][0])
