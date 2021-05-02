# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 22:09:19 2018

@author: afei
"""

# pip3 install pexpect
# 连接ssh的模块
# expect

import pexpect
import optparse
prompt = ['[p|P]assword:','#', '>>>', '>', '\$']     # 捕获到列表中任意一个元素表示连接成功
# '\$':结束
# ‘#’：命令执行成功，或者是ssh连接成功
def send_command(child, cmd):
    # sendline
    child.sendline(cmd)
    index = child.expect(prompt)
    # index 匹配到的索引值
    if prompt[index] == prompt[-1]:
        print('[-]Connect Closed')
        
    print(child.before.decode())
    # child.before在匹配完成之后 可以拿出来匹配之前的东西
    
def connect(user, host, password):
   # ssh连接的各种状态：
   # Are you sure you want to continue connecting (yes/no)?
   # root@192.168.2.222's password:
   # Permission denied, please try again.
   # Permission denied (publickey,gssapi-keyex,gssapi-with-mic,password).
   # Connection closeed by 192.168.2.222
   # ssh: connect to host 192.168.2.22 port 22: No route to host
   # ssh: Could not resolve hostname 192.168.2.222222: Name or service not known
   
   f_con = 'Are you sure you want to continue connecting'
   connstr = 'ssh' + user + '@' + host
   # ssh root@192.168.2.222
   child = pexpect.spawn(connstr,timeout=3)
   #spawn spawn spawn spawn spawn
   ret = child.expect([pexpect.TIMEOUT,f_con,'[p|P]assword]:'])
   if ret == 0:
       print('[-]Time out',host)
       return
   if ret == 1:
       child.sendline('yes')
       ret = child.expect([pexpect.TIMEOUT,'[p|P]assword]:'])
   if ret == 0:
       print('[-]Time out',host)
       return
   child.sendline(password)     # 发送密码
   index = child.expect(prompt)     # 进行捕获
   if index == 0:
       child.sendline(password)
       index += 1
       res = child.expect(prompt)
       if prompt[res] == prompt[-1] or prompt[res] == '[p|P]assword]:':
           print('*******************')
           print('[+]Connection Failed!!!)
           return
   print('[+]Connection Success!!!')
   return child

parser = optparse.OptionParser()
parser.add_option('-H',dest='host',type='string')
parser.add_option('-u',dest='user',type='string')
parser.add_option('-p',dest='passwd',type='string')
options,agrs = parser.parse_args()
host = options.host
user = options.user
passwd = options.passwd
connect(user, host, passwd)
cmd = input('Shell you wanna type:')
send_command(child,cmd)
      
###  windows中无法运行pexpect模块，但在linux可以。       
   
        