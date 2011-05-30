#!/usr/bin/python
# -*- coding: utf-8 -*-
# model.py

import pycurl
import StringIO

status_urls = [
'localhost:8080/status',
'localhost:8998/status',
#'localhost:9204/status',
#'localhost:9240/status',
'localhost:9203/status',
'localhost:9100/status',
'dev:9202/status',
'dev:9100/status',

]

names = [
'dev as',
'dev sofea',
'as 9204',
'sofea 9240',
]

class availability:
    def __init__(self, addr):
        self.addr = addr
        self.c = c = pycurl.Curl()
        c.setopt(pycurl.URL, addr)
        c.setopt(pycurl.HTTPHEADER, ["Accept:"])
        self.b = b = StringIO.StringIO()
        c.setopt(pycurl.WRITEFUNCTION, b.write)
        c.setopt(pycurl.FOLLOWLOCATION, 1)
        c.setopt(pycurl.MAXREDIRS, 5)
    
    def getResponce(self, ):
        #c.setopt(pycurl.URL, "http://{host}:{port}/version.jsp".format(port=port))
        try:
            self.c.perform()
        except pycurl.error as e:
            return ""
        return self.b.getvalue()
    
    @classmethod
    def getAll(self, ):
        return map( availability , status_urls,)
        
	

#print availability.getAll()
