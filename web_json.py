#!C:\\Python27\python.exe
# -*- coding: UTF-8 -*-
import json

class Myclass:
 

 def __init__(self,name,age):
      self.name = name
      self.age =age

obj = Myclass('sdf',12)
objDict = obj.__dict__
s = json.dumps(objDict)

print "Content-type:text/html"
print                               
print '<html>'
print '<head>'
print '<meta charset="utf-8">'
print '<title>Hello Word -</title>'
print '</head>'
print '<body>'
print '<h2>Hello Word! </h2>'
print '<span>%s</span>' % (s)
print '</body>'
print '</html>'
