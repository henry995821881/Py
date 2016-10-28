import requests

#r = requests.get('http://10.10.10.31:90/cgi-bin/hello.py')
r = requests.get('http://10.10.10.31:90/cgi-bin/jjson.py')
print r.content

