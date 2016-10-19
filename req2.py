#post request
import urllib
import urllib2
test_data = {'code':'sdfj','nm':'123'}
test_data_urlencode= urllib.urlencode(test_data)
requrl = "http://192.168.0.200/json"
req = urllib2.Request(url=requrl,data=test_data_urlenconde)
#print req
req_data = urllib2.urlopen()
res = response.read()
print res
