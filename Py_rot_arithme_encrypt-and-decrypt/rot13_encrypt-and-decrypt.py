#!/usr/bin/python
# Env: python3
# Author: afei_0and1
# -*- coding: utf8 -*-

import string

def rot13_encode(strings, OffSet=13):
    def encode_chr(i):
        s = lambda x: chr((ord(i) - x + OffSet % 26 + x))
        #从ASCII码指定。chr(97)=a, chr(65)=A
        return s(97) if i.islower() else (s(65) if i.isupper() else i)
    #return  ''.join(encode_chr(c) for c in strings)
    res = ''.join(encode_chr(c) for c in strings)
    print("\nRot13加密成功，加密结果："+res)

low_strings = string.ascii_lowercase
up_strings = string.ascii_uppercase
def rot13_decode(cipher):
    res = ''
    #存放解密后字符串
    strings_dict = {}
    #小写字母解密
    for i in range(len(low_strings)):
        strings_dict[low_strings[i]] = low_strings[i - 13]
    #大写字母解密
    for i in range(len(up_strings)):
        strings_dict[up_strings[i]] = up_strings[i - 13]
    for i in str(cipher):
        a_string = strings_dict[i]
        res += a_string
    print("\nRot13解密成功，解密结果："+res)

if(__name__ == '__main__'):
    print('---------------------------------------')
    x = input("请选择功能：\n加密：1\n解密：2\n")
    if x == '1':
        en = input('请输入需要加密的字符串：')
        rot13_encode(en)
    elif x == '2':
        de = input('请输入需要解密的密文：')
        rot13_decode(de)
    else:
        print('您的输入有误！')
        exit()