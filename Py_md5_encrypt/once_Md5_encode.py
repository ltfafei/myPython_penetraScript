#!/usr/bin/python
# Env: python3
# Author: afei_0and1
# -*- coding: utf8 -*-

import sys, hashlib

def once_Md5_encode():
    if (len(sys.argv) < 2):
        print("-----------------------------------------------")
        print(" ")
        print("Useg: python %s <string>" % sys.argv[0])
        print("eg: python once_Md5_encode.py 'hloolelwrd'")
        print(" ")
        print("-----------------------------------------------")
        return
    flag = sys.argv[1]
    #MD5加密
    data = hashlib.md5()
    data.update(flag.encode('utf-8'))
    print(flag+'加密结果：'+data.hexdigest())

if(__name__ == '__main__'):
    once_Md5_encode()