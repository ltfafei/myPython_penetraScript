#!/usr/bin/python
# Env: python3
# -*- coding:utf-8 -*-
# Author：afei_0and1

'''
绝大部分采用base64编码，base32和base16同理。

    base64编码方法：base64.b64encode()
    base32编码方法：base64.b32encode()
    base64编码方法：base64.b16encode()
    
    base64解码方法：base64.b64decode()
    base32解码方法：base64.b32decode()
    base64解码方法：base64.b16decode()
'''

import base64, sys

def img_Transbase64():
    if (len(sys.argv) < 3):
        print("-----------------------------------------------")
        print(" ")
        print("Useg: python %s <path/source.png> <path/base64.txt>" % sys.argv[0])
        print("eg: python image_hideinfo.py c:/1.png c:/base64.txt")
        print(" ")
        print("-----------------------------------------------")
        return

    img_path = sys.argv[1]
    result_path = sys.argv[2]

    with open(img_path, 'rb') as f:
        #使用base64编码
        base64_data = base64.b64encode(f.read())
        #print(str(base64_data))
        outfile = open(result_path, 'wt')
        outfile.write(str(base64_data))
        outfile.close()
    print("图片转换base64编码成功!")

if (__name__ == '__main__'):
    img_Transbase64()