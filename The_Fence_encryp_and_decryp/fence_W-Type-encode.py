#!/usr/bin/python
# Env: python3
# Author: afei_0and1
# -*- coding: utf8 -*-

import sys

def generaget_W():
    if (len(sys.argv) < 3):
        print("-----------------------------------------------")
        print(" ")
        print("Useg: python %s <string> <col_num>" % sys.argv[0])
        print("eg: python fence_W-Type_encode.py helloworld 3")
        print(" ")
        print("-----------------------------------------------")
        return
    string = sys.argv[1]
    num = sys.argv[2]
    
    arr = [['*']*len(string) for i in range(int(num))]
    #行数，初始定义为0
    row = 0
    upflag = False
    #在矩阵上按“W”画出string
    for column in range(len(string)):
        arr[row][column] = string[column]
        if row == int(num)-1:
            upflag = True
        if row == 0:
            upflag = False
        if upflag:
            #上边界
            row -= 1
        else:
            #下边界
            row += 1
    #打印W图案
    for i in arr:
        print(i)
    
    #存放加密结果
    res = []
    for row in range(int(num)):
        for column in range(len(string)):
            if arr[row][column] != '*':
                res.append(arr[row][column])
    print(''.join(res))
    
if(__name__ == '__main__'):
    generaget_W()