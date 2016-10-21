import requests

r = requests.get('http://www.baidu.com')
print r.status_code
print '\n'
print r.encoding
print '\n'
print r.headers
#print r.content

