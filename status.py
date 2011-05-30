#!/usr/bin/python
# -*- coding: utf-8 -*-

from model import *
import re
from flask import Flask
app = Flask(__name__)

html = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"> 
<html> 
<head> 
  <title>Service status</title> 
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"> 
  <meta http-equiv="refresh" content="1" />
</head> 
<body> 
    %s  
</body> 
</html> '''

green_sq = '<table bgcolor="{color}"><tbody><tr><td>{name}</td></tr><tr><td>{address}</td></tr> <tr><td>{message}</td></tr></tbody></table>'
red_sq = '<table bgcolor="Red"><tbody ><tr><td >%1</td></tr></tbody></table>'

@app.route("/")
def hello():
    ''' consider user had asked for list of most common statuses '''
    
    statuses = availability.getAll()
    
    sqs = [green_sq.format(**name_color_address_message(status)) for status in statuses]
    
    #green_sq.format(**name_color_address_message(dev_as_status )
    
    return html % '<br>'.join(sqs)

def name_color_address_message(avail):
    
    name = ''
    
    message = avail.getResponce()
    
    color = color_of_message(message)[0]
    
    return dict(name= name , color = color, address = avail.addr, message = message)
    
def color_of_message(message):
    yellow = re.compile('50[0-9]')
    lime = re.compile('.')
    if yellow.search(message):
        return ('yellow', message)
    if lime.match(message):
        return ('lime', message)
    return ('red', 'is down')

@app.route("/source/")
def grep_source(pattern='MailCommandImpl'):
    return 'MailCommandImpl.java'

if __name__ == "__main__":
    app.run(debug=True)
