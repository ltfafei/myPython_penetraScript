#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: afei

import smtplib, config, threading, time, random
from email.mime.text import MIMEText

#定义连接邮箱服务器方法
def connect():
    try:
        server = smtplib.SMTP(config.smtpServer, config.smtpPort)
        server.ehlo()
        server.login(config.smtpUser, config.smtpPass)
        return server
    except Exception:
        print('无法连接到邮箱服务器！请检查配置。')

#定义邮件发送方法
def sendInfo(server, to, subject, content):
    msg = MIMEText(contents)
    msg['Mine-Version']='1.0'
    msg['From']=config.smtpUser
    msg['To']=to
    msg['Project']=subject
    msg.set_payload(contents)
    try:
        mailinfo = server.sendmail(config.smtpUser, to, str(msg))
    except Exception as ex:
        print("Error! 邮件发送失败，请检查配置！ %s" %ex)
    else:
        print("Goodluck! 邮件发送成功！")

#定义邮件发送内容
def sendinfo():
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('I am MailBomb. Now is %s\n' %now)
    global contents
    print(contents)
    text = "Hello boy and girls. If you don't get luncky, try hard!"
    if contents != text:
        contents = text
        server = connect()
        sendInfo(server, to, subject, contents)
    thred = threading.Timer(10, sendinfo)
    thred.start()

if __name__ == '__main__':
    while True:
        to = config.sendTo
        subject="Hello Boy"
        server = connect()
        contents = "Hello boy and girls. If you don't get luncky, try hard!"
        sendInfo(server, to, subject, contents)
        timer = threading.Timer(10, sendinfo)
        timer.start()
        t = random.randint(1,60)
        time.sleep(t)