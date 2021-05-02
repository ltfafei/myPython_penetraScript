# -*- coding: utf-8 -*-

from socket import *
tgtHost = input('请输入你要访问的主机：')

c_sock = socket(AF_INET,SOCK_STREAM)  
tgtPorts = range(1,65536)
setdefaulttimeout(1)
# 遍历端口，逐一尝试发送数据
for tgtPort in tgtPorts:
    try:
        c_sock.connect((tgtHost,tgtPort))
        c_sock.send('hello'.encode())
        res = c_sock.recv(100)
        print('[+]Port :',tgtPort)
        print('[+]Proto :',res.decode())
    except:
        print('[-]Port :',tgtPort)
        continue