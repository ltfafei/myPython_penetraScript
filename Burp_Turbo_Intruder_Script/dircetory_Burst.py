#Author: unknow

def mult_host_dir_brute():
    #精细化指定具体请求
    req = '''GET /%s HTTP/1.1
Host: %s
Connection: keep-alive
'''
    engines = {}
    
for url in open('/Users/mac/temp/urls.txt'):
        url = url.rstrip()
        engine = RequestEngine(endpoint=url, 
            concurrentConnections=5,
            requestsPerConnection=100,
            pipeline=True)
        engines[url] = engine
        
for word in open('/Users/mac/safe/web/brute/all.txt'):
        word = word.rstrip()
        
for (url, engine) in engines.items():
            domain = url.split('/')[2]
            engine.queue(req, [word, domain])

def queueRequests(target, wordlists):
    mult_host_dir_brute()

def handleResponse(req, interesting):
# currently available attributes are req.status, req.wordcount, req.length and req.response
  if req.status != 404:
       table.add(req)