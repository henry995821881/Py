import requests

r =requests.get("http://10.10.10.31:8080/jrtours")
print r.content
