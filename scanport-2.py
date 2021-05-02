#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket, sys

# 定义固定扫描的端口
port = [135, 139, 145, 3306, 3389, 1433, 1521]
def open(ip, port):
    s = socket.socket
    try:
        s.connect((ip, port))
        return True
    except:
        return False

# 定义需要扫描的IP函数
def scan(ip):
    for x in port:
        if open(ip, x):
            print('%s host %s open' %(ip, x))
        else:
            print('%s host %s close' %(ip, x))

# 定义扫描端口范围函数
def rscan(ip):
    for x in range(s, e):
        if open(ip, x):
            print('%s host %s open' %(ip, x))
        else:
            print('%s host %s close' %(ip, x))

# 如果参数个数小于3个，那么打印使用说明
if len(sys.argv) < 2:
    print('''
    This program prints files to the standard output.
    Any number of files can be specified.
    Options include:
        python scanport-2.py host ports
        python scanport-2.py 127.0.0.1
        python scanport-2.py 127.0.0.1 80,90,135,145,3306,1433
        python scanport-2.py 127.0.0.1 80-90
        python scanport-2.py 127.0.0.1 all   
    ''')
    sys.exit()
# 判断给的第二个参数开头是否包含：--，如果包含就打印以下结果
if sys.argv[1].startswith('--'):
    # 将‘--’之后的内容赋值给option，进行以下判断
    option = sys.argv[1][2:]
    if option == 'version':
        print('Version 1.2')
    elif option == 'help':
        print('''
         This program prints files to the standard output.
         Any number of files can be specified.
         Options include:
            --version : Prints the version number
            --help : Display this help
        ''')
    else:
        print('Unknown option')
    sys.exit()
try:
    # 如果参数长度等于2,那么将执行scan函数，扫描host主机
    if len(sys.argv) == 2:
        scan(sys.argv[1])
    elif len(sys.argv) == 3:
        #如果‘,’在第3个参数中，执行以下代码
        if ',' in sys.argv[2]:
            p = sys.argv[2]
            p = p.split(',')
            #将端口列表str类型转换为int类型
            for x in p:
                a = []
                a.append(int(x))
                port = a
                scan(sys.argv[1])
        elif '-' in sys.argv[2]:
            # 将‘-’和前后的字符串列表分开赋值给a
            a = sys.argv[2]
            a = a.split('-')
            # 将a的值转换为int类型分别赋值给s和e
            s = int(a[0])
            e = int(a[1])+1
            # 调用rscan函数扫描IP
            rscan(sys.argv[1])
        # 扫描1-65535端口
        elif sys.argv[2] == 'all':
                s = 1
                e = 65536
                rscan(sys.argv[1])
# 捕获键盘输入异常
except KeyboardInterrupt:
    print('\n')
    print('program end!')