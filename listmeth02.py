#!/usr/bin/python3

proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append('dns')
protoa.append('dns')
print('\n', "append: ")
print(proto)

proto2 = [22, 80, 443, 53]
proto.extend(proto2)
print('\n', "extend:")
print(proto)
protoa.append(proto2)
print('\n', "append: ")
print(protoa)

input("press enter")
