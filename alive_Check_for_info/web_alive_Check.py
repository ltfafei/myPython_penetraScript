#!/usr/bin/python
# Env: python3
# Author: afei00123
# -*- coding: utf8 -*-

import requests, urllib3, time, argparse
from colorama import init
init(autoreset=True)

def title():
    print("")
    print('*'.center(60, '*'))
    print("github：https://github.com/ltfafei".center(50))
    print("gitee：https://gitee.com/afei00123".center(50))
    print("CSDN: afei00123.blog.csdn.net".center(50))
    print("公众号：网络运维渗透".center(50))
    print("")
    print('*'.center(60, '*'))
    print("")

class web_alive_Check():
    def url_alive_Check(self, url):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            status = requests.get(url, timeout=3).status_code
            print(f"[+]{url}请求正常，响应状态码：{status}")
            with open("res_alive.txt", 'a') as f:
                f.writelines(f"{url}，响应状态码：{status}" + "\n")
        except:
            print(f"\033[31m[n]{url}请求失败！")

    def url_alive_Batch_Check(self, url, file):
        if url:
            return True
        if file:
            for url in file:
                url = url.replace("\n", "")
                time.sleep(1)
                self.url_alive_Check(url)

if(__name__ == "__main__"):
    title()
    parser = argparse.ArgumentParser(description="web-urls_alive_Check Script")
    parser.add_argument(
        '-u', '--url', type=str,
        help='Please input target url. eg: https://ip:port'
    )
    parser.add_argument(
        '-f', '--file', type=argparse.FileType('r'),
        help='Please input urls file path. eg: c:\\urls.txt'
    )
    args = parser.parse_args()
    run = web_alive_Check()
    if args.url:
        run.url_alive_Check(args.url)
    if args.file:
        run.url_alive_Batch_Check(args.url, args.file)
        print("\n[done] 存活url探测完成，请查看：res_alive.txt")