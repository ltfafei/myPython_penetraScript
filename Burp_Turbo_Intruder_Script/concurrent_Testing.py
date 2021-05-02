#Resocure: https://github.com/PortSwigger/turbo-intruder/blob/master/resources/examples/race.py

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=100,
                           requestsPerConnection=200,
                           pipeline=False)

    # the 'gate' argument blocks the final byte of each request until openGate is invoked
    for i in range(100):
        engine.queue(target.req, target.baseInput, gate='race1')

    # wait until every 'race1' tagged request is ready
    # then send the final byte of each request
    # (this method is non-blocking, just like queue)
    engine.openGate('race1')
    engine.complete(timeout=60)

def handleResponse(req, interesting):
    table.add(req)