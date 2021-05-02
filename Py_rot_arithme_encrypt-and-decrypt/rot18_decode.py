#!/usr/bin/python
# Env: python3
# Author: afei_0and1
# -*- coding: utf8 -*-

import string, argparse
low_strings = string.ascii_lowercase
up_strings = string.ascii_uppercase
digits = string.digits

def rot18_decode(cipher):
    res = ''
    digits_dict = {}
    strings_dict = {}
    #rot5解密
    for i in range(len(digits)):
        digits_dict[digits[i]] = digits[i - 5]
    #rot13解密
    for i in range(len(low_strings)):
        strings_dict[low_strings[i]] = low_strings[i - 13]
    for i in range(len(up_strings)):
        strings_dict[up_strings[i]] = up_strings[i - 13]

    for i in str(cipher):
        #数字判断
        if i.isdigit():
            a_string = digits_dict[i]
        #字母判断
        if i.isalpha():
            a_string = strings_dict[i]
        else:
            a_string = i
        res += a_string
    print("************************************")
    print("\nrot18解密成功，解密结果："+res+"\n")
    print("************************************")
#rot18_decode('afei00123')

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser(description="Rot18 decode Script")
    parser.add_argument(
        '-c', '--cipher',
        metavar='', required='True',
        help='Please input need decode strings. eg: -c af123, --cipher af123'
    )
    args = parser.parse_args()
    rot18_decode(args.cipher)