#https://github.com/PortSwigger/turbo-intruder/blob/master/resources/examples/default.py
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False)

    for i in range(3, 8):
        engine.queue(target.req, randstr(i), learn=1)
        engine.queue(target.req, target.baseInput, learn=2)

    for word in open(r'mypassword.dict'):
        engine.queue(target.req, word.rstrip())

def handleResponse(req, interesting):
    #currently available attributes are req.status, req.wordcount, req.length and req.response 
    if interesting:
        table.add(req)