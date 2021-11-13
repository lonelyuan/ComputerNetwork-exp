#/usr/bin/python3
# 实现简陋的静态HTTP服务器
# Author: lonelyuan


import socket
from scapy.layers.http import *
from scapy.all import *
import os


host = '0.0.0.0'
port = 8000
rootPath = './'


s = socket.socket() 
s.bind((host, port))
s.listen(5)
print('[+] listening:', port)


def route(path):
    path = 'index.html' if path == '/' else path[1:]
    if path in os.listdir(rootPath):
        with open(path,'rb') as f:
            laod = f.read() 
            return laod
    return 404
    
    
def http_handler(req_str):
    req = HTTPRequest()
    req.do_dissect(req_str) # 解析请求
    print('[+] req: ', req.summary())
    body = route(req.Path.decode()) # 路由函数
    res = HTTPResponse()
    if body == 404:
        res = HTTPResponse(Status_Code='404', Reason_Phrase='Not Found')
        body = "<h1>Not Found.</h1>"
    res = HTTP()/res/body
    print('[+] res: ', res.summary())
    return raw(res)
    

while True:
    c, addr = s.accept()
    print('[+] accepted:', addr)
    req = c.recv(1024)
    res = http_handler(req)
    c.send(res)
    c.close()
