#!/usr/bin/python3

## standard library imports
import os
import warnings
## 3rd party import
import paramiko

## excel data or csv data
excellist = [{"un": "bender", "ip": "10.10.2.3"}, {"un": "fry", "ip": "10.10.2.4"}, {"un": "zoidberg", "ip": "10.10.2.5"}]

warnings.filterwarnings(action="ignore",module=".*paramiko.*")
## create an empty PuTTY session
sshsession = paramiko.SSHClient()

## retrieve an ssh key
mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

## skip the authorized_hosts warning 
sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for fc in excellist:
    print("connecting to...", fc['un'], "@", fc['ip'])
## press the CONNECT button in our PuTTY session
    sshsession.connect(hostname=fc['ip'], username=fc['un'], pkey=mykey)

## 3 variables are needed (or 2 if ssh_in, *results will combine out and err)
    ssh_in, ssh_out, ssh_err = sshsession.exec_command('ls /var/')

## display the results of our command
    print(ssh_out.read().decode('utf-8'))

## close ssh session
    sshsession.close()


