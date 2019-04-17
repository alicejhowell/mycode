#!/usr/bin/python3
"""paramiko with SFTP and SSH"""

import paramiko

## define servers we want to connect to
usercreds = [{"un": "bender" ,"ip": "10.10.2.3"}, {"un": "fry" ,"ip": "10.10.2.4"}, {"un": "zoidberg", "ip": "10.10.2.5"}]

## loop through servers that we want to connect to
for fc in usercreds:
    mytransport = paramiko.Transport(fc["ip"], 22)
    mytransport.connect(username=fc['un'], password="alta3")
    sftp = paramiko.SFTPClient.from_transport(mytransport)

    ## move ahbash.sh to each server
    sftp.put("/home/student/mycode/ahbash.sh", "/tmp/ahbash.sh")
    ## done with SFTP object so close the session
    sftp.close()
    mytransport.close()

    sshsession = paramiko.SSHClient()
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshsession.connect(hostname=fc['ip'], username=fc['un'], pkey=mykey)

    ## execute ahbash.sh
    sshsession.exec_command('cd /tmp; chmod u+x ahbash.sh; ./ahbash.sh')

## cat both files (zfile.txt) and (itworks.txt)

## close connections
sshsession.close()
