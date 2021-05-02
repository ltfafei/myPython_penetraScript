#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib

a = raw_input("请输入时间：")
b = raw_input("请输入UID：")
f = open(r'dict.txt', 'w')

for i in range(30):
    num = b + str(int(a) + i)
    print num
    mn = hashlib.md5(num)
    f.write(mn.hexdigest() + "\n")
f.close()