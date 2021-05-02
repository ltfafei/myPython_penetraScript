#!/usr/bin/python3
# -*- coding: UTF-8 -*-

'''
    代理IP网址：https://www.89ip.cn/
    89ip代理使用的都是http协议
'''

import requests
import time
from lxml import etree
import sys

#获取第一页上的代理IP和端口并写入result.txt
'''
url = 'https://www.89ip.cn/index_1.html'
page = requests.get(url).text
html = etree.HTML(page)
ip = html.xpath('//td[1]/text()')
port = html.xpath('//td[2]/text()')
for a, b in zip(ip, port):
    # strip()去除字符串首尾空格
    IP = a.strip()
    PORT = b.strip()
    result = ("http://"+ IP +':'+ PORT)
    with open('./result.txt', 'a')as file:
        file.write(result +'\n')
'''

#获取89ip前十页url并写入urls.txt
list = [1,2,3,4,5,6,7,8,9,10]
for i in list:
    url = "https://www.89ip.cn/index_%s.html" % i
    with open ('./urls.txt', 'a')as f:
        f.write(url +'\n')
        f.close()

# 获取前10页IP和端口
urlfile = open('urls.txt', 'r')
urllist = urlfile.readlines()
Len = len(urllist)
for j in range(1, Len+1):
    URL = "https://www.89ip.cn/index_%s.html" %j
    page = requests.get(URL).text
    html = etree.HTML(page)
    #匹配IP
    ip = html.xpath('//td[1]/text()')
    #匹配端口
    port = html.xpath('//td[2]/text()')

    for a,b in zip(ip, port):
        IP = a.strip()
        PORT = b.strip()
        result = (IP +':'+ PORT)
        with open('./result.txt', 'a')as file:
            file.write(result +'\n')
print("代理IP爬取成功")

#测试获取的代理IP是否可用
print("正在测试代理IP...")
print(" ")
def check(result):
    urls = 'http://%s' % result.strip()
    try:
        relu = requests.get(urls, timeout=3)
        print(result +"代理可用")
        with open('useful_ip.txt', 'a') as useful:
            useful.write(result)
    except:
        print(result +"代理不可用！")

with open('result.txt', 'r')as churl:
    churls = churl.readlines()
    for result in churls:
        check(result)
print(" ")

#打印爬取IP可用率
useful_file = open('useful_ip.txt', 'r')
read_uesful = useful_file.readlines()
usefulLen = len(read_uesful)
resuLen = len(result)
print("所爬取页面代理IP可用率为：{:.2%}".format(usefulLen/resuLen))