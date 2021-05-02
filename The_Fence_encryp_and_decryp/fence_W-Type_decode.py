#!/usr/bin/python
# Env: python3
# Author: afei_0and1
# -*- coding: utf8 -*-

def generaget_W(string, num):   
    arr = [['*']*len(string) for i in range(int(num))]
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
    return arr

#解密，知道栅栏数解密方法
def fence_W_Type_decode():
    string = input("请输入需要解密的栅栏密码：")
    num = int(input("请输入栅栏数："))
    arr = generaget_W(string, num)
    index = 0
    #将W型字符串按row行的顺序依次替换为string
    for row in range(num):
        for column in range(len(string)):
            if arr[row][column] != '*':
                arr[row][column] = string[index]
                index += 1
    #存放解密后的字符串
    res = []
    #以column列的顺序依次连接取出来的字符
    for column in range(len(string)):
        for row in range(num):
            if arr[row][column] != '*':
                res.append(arr[row][column])
    print("解密结果："+''.join(res))

if(__name__ == '__main__'):
    fence_W_Type_decode()