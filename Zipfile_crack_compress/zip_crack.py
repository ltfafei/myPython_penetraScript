#!/usr/bin/python
# -*- coding: UTF-8 -*-
import zipfile

# 需要破解的压缩包
zf = zipfile.ZipFile("test.zip")
# 密码字典
passfile = open("pass.txt", "r")
# 破解后文件的保存路径
save = input("请输入文件保存的路径(默认保存到当前文件夹)：")

# 遍历字典
for line in passfile.readlines():
    try:
        password = line.strip("\n")
        # 解压文件，默认保存到当前文件夹
        zf.extractall(path=save, members=zf.namelist(),
                      pwd=password.encode("utf-8"))
        print('\n')
        print("破解成功，密码是：%s" %password)
        break
    except:
        print("密码不正确！")