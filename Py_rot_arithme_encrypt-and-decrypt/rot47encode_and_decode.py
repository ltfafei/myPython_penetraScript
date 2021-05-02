#!/usr/bin/python
# Env: python3
# Author: afei_0and1
# -*- coding: utf8 -*-

import string

def rot47_encode(cipher):
    x = []
    for i in range(len(cipher)):
        string = ord(cipher[i])
        if string >= 33 and string <= 126:
            #除94取余？127-33=94
            x.append(chr(33+(string + 14) % 94))
        else:
            x.append(cipher[i])
    res = ''.join(x)
    print("\nrot47加密成功，加密结果："+res)
#rot47_encode('234')

def rot47_decode(strings):
    x = []
    for i in range(len(strings)):
        string = ord(strings[i])
        if string >= 33 and string <= 126:
            #除94取余？127-33=94
            x.append(chr(string - 47))
        else:
            x.append(strings[i])
    res = ''.join(x)
    print("\nrot47解密成功，解密结果："+res)
#rot47_decode('abc')

x = input("\n功能选择：\n    加密：1\n    解密：2\n")
if x == '1':
    en = input("请输入需要加密的字符串：")
    rot47_encode(en)
elif x == '2':
    de = input("请输入解密密文：")
    rot47_decode(de)
else:
    print("您的输入有误！")
    exit()