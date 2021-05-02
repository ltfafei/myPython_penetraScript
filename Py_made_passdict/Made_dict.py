#!/usr/bin/python
# -*- coding: UTF-8 -*-

import itertools as its


word = input("请输入数字字母或字符串：")
rep = int(input("请输入字典的位数："))
x = input("字典正在制作中...")
r = its.product(word, repeat=rep)
# 写入字典并保存
dic = open('pass.txt', "a")

#循环遍历字典
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))