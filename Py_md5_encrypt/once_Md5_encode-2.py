#!/usr/bin/python
# Env: python3
# Author: afei_0and1
# -*- coding: utf8 -*-

import hashlib, argparse

def once_Md5_encode(text):
    #MD5加密
    data = hashlib.md5()
    data.update(str(text).encode('utf-8'))
    print(text+'加密结果：'+data.hexdigest())

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser(description="Once encode md5 Script")
    parser.add_argument(
    '-t', '--text',
    #metavar可进行指向替换--text
    #required='True'表示如果没有接参数，将打印信息提示
    type = str, metavar='', required='True',
    help = 'Input decode md5 data. eg: -t afei, --text afei'
    )
    args = parser.parse_args()
    once_Md5_encode(args.text)