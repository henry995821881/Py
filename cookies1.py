import requests , json

r = requests.get('http://www.baidu.com')
print r.cookies
