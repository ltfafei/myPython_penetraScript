#!/usr/bin/python
# Env: python3
# Author: afei_0and1
# -*- coding: utf8 -*-

import string, argparse
digits = string.digits

def rot5_decode(cipher):
    res = ''
    #存放循环获得的所有结果
    digits_dict = {}
    for i in range(len(digits)):
        digits_dict[digits[i]] = digits[i-5]
    for i in str(cipher):
        if i in digits:
            a_digit = digits_dict[i]
        else:
            print("您输入的不是rot5密文，解密结果有误，请检查！")
        res += a_digit
    print("\nRot5解密成功，解密结果："+res)

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser(description="Rot5 encode Script")
    parser.add_argument(
    '-c', '--cipher',
    metavar='', required='True',
    help = 'Input need encode rot5 data. eg: -c 123, --cipher 123'
    )
    args = parser.parse_args()
    rot5_decode(args.cipher)