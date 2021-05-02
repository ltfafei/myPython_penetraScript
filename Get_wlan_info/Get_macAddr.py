#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import uuid

# 获取网卡的UUID值
node = uuid.uuid1()
print("node的类型为：", type(node))
print("node：", node)
# 转换为十六进制
hex = node.hex
print("hex的类型为：：", type(hex))
print("hex：", hex)
# 获取十六进制的MAC地址，倒数12位为MAC地址
mac_addr = hex[-12:]
print("mac_addr = ", mac_addr)