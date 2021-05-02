#!/usr/bin/python
# Env: python3
# Author: afei00123
# -*- coding: utf8 -*-

import os, re, argparse
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

class host_alive_Check():
    def alive_Check(self, file):
        for ip in file:
            try:
                ip = ip.replace("\n", "")
                data = os.popen("ping -n 1 {0}".format(ip)).read()
                try:
                    ttl_str = re.search(r"ttl=", str(data), re.I).group()
                    if ttl_str == "ttl=" or ttl_str == "TTL=":
                        print(f"{ip} 存活")
                        with open("res_alive.txt", 'a+') as f:
                            f.writelines(ip + "\n")
                except Exception:
                    print(f"\033[31m[n] {ip}不存活！")
            except AttributeError as e:
                print(f"\033[31m[n] {ip}不存活！", e)

if(__name__ == "__main__"):
    title()
    parser = argparse.ArgumentParser(description="host_alive_Check Script")
    parser.add_argument(
        '-f', '--file', type=argparse.FileType('r'),
        help='Please input urls file path. eg: c:\\urls.txt'
    )
    args = parser.parse_args()
    run_Check = host_alive_Check()
    if args.file:
        run_Check.alive_Check(args.file)
        print("\n[done] 存活主机探测完成，请查看：res_alive.txt")