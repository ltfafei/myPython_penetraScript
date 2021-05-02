#!/usr/bin/python
# Env: python3
# Author: afei_0and1
# -*- coding: utf8 -*-

import sys

def fence_Passwd_burst():
    if (len(sys.argv) < 2):
        print("-----------------------------------------------")
        print(" ")
        print("Useg: python %s <fence_encryp_string>" % sys.argv[0])
        print("eg: python fence_Passwd_burst.py 'hloolelwrd'")
        print(" ")
        print("-----------------------------------------------")
        return
    secret = sys.argv[1]
    
    #栅栏密码解密，循环遍历有多少栏
    res = [step for step in range(2, len(secret)) if len(secret)%step == 0]
    for step in res:
        flag = ''
        #获取解密结果，以step栏进行遍历获取解密后的flag
        for i in range(step):
            flag += secret[i::step]
        print('第%s栏： 解密结果：%s' %(str(step), flag))

if(__name__ == '__main__'):
    fence_Passwd_burst()