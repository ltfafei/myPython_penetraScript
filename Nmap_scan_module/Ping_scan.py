#!/usr/bin/python
# -*- coding: UTF-8 -*-
import nmap
import sys
def nmap_ping_scan(scan1):
    # 创建一个扫描实例
    nm = nmap.PortScanner()
    # 配置nmap参数
    ping_scan_raw_result = nm.scan(hosts=scan1, arguments='-v -n -sn')
    # 分析扫描结果，并放入列表
    host_list = []
    for result in ping_scan_raw_result['scan'].values():
        if result['status']['state'] == 'up':
            host_list.append(result['addresses']['ipv4'])
        return host_list


if __name__ == '__main__':
    # for host in nmap_ping_scan(sys.argv[1]):
    #     print('%-20s %5s' % (host, 'is UP'))
    for host in nmap_ping_scan("47.105.177.204 "):
        print('%-20s %5s' % (host, 'is UP'))