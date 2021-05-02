#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
import pywifi
from pywifi import const

# 测试PC是否连接wifi
def wifi_test():
    '''创建wifi对象'''
    wifi = pywifi.PyWiFi()
    # 获取设备上第一块网卡
    iface = wifi.interfaces()[0]
    # 判断设备是否连接wifi
    if iface.status() == const.IFACE_DISCONNECTED:
        print("wifi未连接！")
    else:
        print("wifi已连接")
wifi_test()