#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import psutil

# 获取网卡设备详细信息
info = psutil.net_if_addrs()
print("info = ", info)
print("info的类型为：", type(info))
print('\n')

# 取出其中的WLAN网卡信息
net1 = info['WLAN']
print("net1 = ", net1)
print("net1的类型为：", type(net1))
print("\n")

# 取出返回的列表(WLAN网卡)中第一个属性的值
packet1 = net1[0]
print("packet1 = ", packet1)
print("packet1的类型为：",type(packet1))
# 取出packet1中属性为address的值(MAC地址)
print("ac_Addr = ", packet1.address)
print("\n")

# 取出返回的列表(WLAN网卡)中第二个属性的值
packet2 = net1[1]
print("packet2 = ", packet2)
print("packet2的类型为：",type(packet2))
# 取出packet2中属性为address的值(IP地址)
print("ip_Addr = ", packet2.address)