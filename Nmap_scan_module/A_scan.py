#!/usr/bin/python
# -*- coding: GBK -*-

import nmap, sys

def A_scan(scan1):
    nm = nmap.PortScanner()
    # 配置nmap参数
    scan_result = nm.scan(hosts=scan1, arguments='-v -n -A')
    # 分析扫描结果，优化打印
    for host, result in scan_result['scan'].items():
        if result['status']['state'] == "up":
            print('#' * 17 + 'Host：' + host + '#' * 17)
            # 猜测操作系统，for循环遍历打印
            print('-' * 17 + '操作系统猜测' + '-' * 17)
            for os in result['osmatch']:
                print('操作系统为：' + os['name'] + " " * 3 + '准确度为：'+ os['accuracy'])
            idno = 1
            try:
                for port in result['tcp']:
                    try:
                        print('-' * 17 + "TCP服务详细信息" + '[' + str(idno) + ']' + '-' * 17)
                        idno += 1
                        print("TCP端口号：" + str(port))
                        try:
                            print("服务：" + result['tcp'][port]['name'])
                        except:
                            pass
                        try:
                            print("状态：" + result['tcp'][port]['state'])
                        except:
                            pass
                        try:
                            print("版本：" + result['tcp'][port]['version'])
                        except:
                            pass
                        try:
                            print("发送的包：" + result['tcp'][port]['reason'])
                        except:
                            pass
                        try:
                            print("产品：" + result['tcp'][port]['product'])
                        except:
                            pass
                        try:
                            print("CPE：" + result['tcp'][port]['cpe'])
                        except:
                            pass

                        try:
                            print("额外信息：" + result['tcp'][port]['extrainfo'])
                        except:
                            pass
                        try:
                            print("脚本：" + result['tcp'][port]['script'])
                        except:
                            pass
                    except:
                        pass
            except:
                pass

            idno = 1
            try:
                for port in result['udp']:
                    try:
                        print('-' * 17 + "UDP服务详细信息" + '[' + str(idno) + ']' + '-' * 17)
                        idno += 1
                        print("UDP端口号：" + str(port))
                        try:
                            print("服务：" + result['udp'][port]['name'])
                        except:
                            pass
                        try:
                            print("状态：" + result['udp'][port]['state'])
                        except:
                            pass
                        try:
                            print("版本：" + result['udp'][port]['version'])
                        except:
                            pass
                        try:
                            print("发送的包：" + result['udp'][port]['reason'])
                        except:
                            pass
                        try:
                            print("产品：" + result['udp'][port]['product'])
                        except:
                            pass
                        try:
                            print("CPE：" + result['udp'][port]['cpe'])
                        except:
                            pass

                        try:
                            print("额外信息：" + result['udp'][port]['extrainfo'])
                        except:
                            pass
                        try:
                            print("脚本：" + result['udp'][port]['script'])
                        except:
                            pass
                    except:
                        pass
            except:
                pass

if __name__ == '__main__':
    A_scan('192.168.0.120')