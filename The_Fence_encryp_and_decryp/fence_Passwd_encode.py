#!/usr/bin/python
# Env: python3
# Author: afei_0and1
# -*- coding: utf8 -*-

def fence_Passwd_encode():
    string = input('请输入需要加密的明文：')
    num = int(input('请输入栅栏数(密钥)：'))
    res = ''
    for i in range(int(num)):
        #遍历循环输出结果
        for j in range(int(string.__len__()/num + 0.5)):
            #print(j)
            try:
                res += string[j*num+i]
            except:
                pass
    print(res)
            
if(__name__ == '__main__'):
    fence_Passwd_encode()