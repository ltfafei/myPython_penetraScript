#!/usr/bin/python
# Env: python3
# -*- coding:utf-8 -*-
# Author：afei_0and1

import base64, sys

def base64_Trans_img():
    if (len(sys.argv) < 3):
        print("-----------------------------------------------")
        print(" ")
        print("Useg: python %s <path/base64.txt> <path/img.png>" % sys.argv[0])
        print("eg: python image_hideinfo.py c:/base64.txt c:/img.png")
        print(" ")
        print("-----------------------------------------------")
        return

    base64_path = sys.argv[1]
    img_path = sys.argv[2]

    with open(base64_path, 'r') as f:
        #使用base64编码
        #data = f.read().split("'")[1]
        data = f.read().split(",")[1]
        #print(data)
        base64_data = base64.b64decode(data)
        outfile = open(img_path, 'wb')
        outfile.write(base64_data)
        outfile.close()
    print("base64编码转换图片成功!")

if (__name__ == '__main__'):
    base64_Trans_img()