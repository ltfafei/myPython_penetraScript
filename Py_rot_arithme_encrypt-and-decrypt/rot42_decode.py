#!/usr/bin/python
# Env: python3
# Author: afei_0and1
# -*- coding: utf8 -*-

import argparse

def rot42_decode(cipher):
    x = []
    for i in range(len(cipher)):
        string = ord(cipher[i])
        if string >= 33 and string <= 126:
            #除94取余？127-33=94
            x.append(chr(33 + (string + 9) % 94))
        else:
            x.append(cipher[i])
    res = ''.join(x)
    print("************************************")
    print("\nrot42解密成功，解密结果：" + res +"\n")
    print("************************************")
#rot42_decode('\<B7=]2Q{;*5O%KH52e5<(dC517aPua03QgS517aPua03QiS52:QgS2S')

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser(description="Rot42 decode Script")
    parser.add_argument(
        '-c', '--cipher',
        metavar='', required='True',
        help='Please input need decode strings. eg: -c afei, --cipher afei'
    )
    args = parser.parse_args()
    rot42_decode(args.cipher)