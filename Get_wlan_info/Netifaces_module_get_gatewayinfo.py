#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
   netifaces模块能够获取网路设备的网卡接口信息
'''
import netifaces
# 获取设备网关信息
gate1= netifaces.gateways()
print("gate1 = ", gate1)
print("gate1的类型为：", type(gate1))
print("\n")
# 分析结果获取网关地址
gate = gate1["default"][2][0]
print("gateway_addr：", gate)