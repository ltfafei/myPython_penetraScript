# -*- coding: utf-8 -*-

# 编写一个TCP的客户端
# 主动去找服务器连接
from socket import *

tgtHost = input('请输入你要访问的主机：')
tgtPort = input('请输入你要访问的主机端口：')
# tgtHost -> str
c_sock = socket(AF_INET,SOCK_STREAM)  
# TCP:SOCK_STREAK
# UDP:SOCK_DGRAM
try:
    c_sock.connect((tgtHost,tgtPort))
    c_sock.send('ok'.encode())
    #encode 编码
    #decode 解码
    res = c_sock.recv(100)
    print('Server:',res)
except:
    print('连接失败')
    