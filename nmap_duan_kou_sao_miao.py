# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 10:07:09 2018

@author: canlang
"""

import nmap
# 安装好windows下的nmap
# pip3 install nmap
# 设置nmap的环境变量
tgtHost = '123.125.115.110'
tgtPorts = range(20,25)

# 过滤端口
nmScan = nmap.PortScanner()
for tgtPort in tgtPorts:
    nmScan.scan(tgtHost,str(tgtPort))
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print('[%s]state:%s'% (tgtPort,state))

