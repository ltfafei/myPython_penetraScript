#!/usr/bin/python
# Env: python3
# Author: afei_0and1
# -*- coding: utf8 -*-

import string

def rot_any_encode(cipher, OffSet):
    x = []
    for i in range(len(cipher)):
        string = ord(cipher[i])
        if string >= 33 and string <= 126:
            #除94取余？127-33=94
            x.append(chr(33+(string + OffSet) % 94))
        else:
            x.append(cipher[i])
    res = ''.join(x)
    print("\nrot密码加密成功，加密结果："+res)

def rot_any_decode(strings, OffSet):
    x = []
    for i in range(len(strings)):
        string = ord(strings[i])
        if string >= 33 and string <= 126:
            #除94取余？127-33=94
            x.append(chr(string - (33 + OffSet)))
        else:
            x.append(strings[i])
    res = ''.join(x)
    print("\nrot密码解密成功，解密结果："+res)

x = input("\n功能选择：\n    加密：1\n    解密：2\n")
if x == '1':
    en = input("请输入需要加密的字符串：")
    step = int(input("请输入步长(step-33)："))
    rot_any_encode(en, step)
elif x == '2':
    de = input("请输入解密密文：")
    step = int(input("请输入步长(step-33)："))
    rot_any_decode(de, step)
else:
    print("您的输入有误！")
    exit()