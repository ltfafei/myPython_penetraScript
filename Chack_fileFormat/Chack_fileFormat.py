#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
   chardet模块主要用于判断字符编码
'''
import chardet

file = open("input.csv", 'rb')
str = file.read()
chardet_ = chardet.detect(str)
print("该文件编码信息为：", chardet_)
print("该文件编码格式为：", chardet_['encoding'])