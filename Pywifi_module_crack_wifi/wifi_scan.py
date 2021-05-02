#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
import pywifi

def wifiscan():
    '''创建wifi对象'''
    wifi = pywifi.PyWiFi()
    # 获取网卡
    iface = wifi.interfaces()[0]
    # 扫描附近wifi
    iface.scan()
    # 接收扫描的结果
    wifi_list = iface.scan_results()
    # 打印wifi名称
    for wifi in wifi_list:
        '''ssid：wifi名称'''
        print(wifi.ssid)
# 实例化
wifiscan()