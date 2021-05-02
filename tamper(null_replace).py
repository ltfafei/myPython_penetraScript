#!/usr/bin/python
# -*- coding: UTF-8 -*-

def tamper(payload, **kwargs):
    ret = payload

    if payload:
        ret = ""
        quote = False
        # 遍历字符窜
        for x in payload:
            # 如果语句中包含单引号或者双引号就不替换
            if x == "'" or x == '"':
                quote = not quote
            # 将引号之外的空格替换掉
            elif x.isspace() and not quote:
                ret += "/*|%20--%20|*/"
            else:
                ret += x
    return ret
print(tamper(" and 1=2 and name like 'afei 123'"))