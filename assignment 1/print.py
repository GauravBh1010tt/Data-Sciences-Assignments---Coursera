import urllib
import json
res = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
#print type(res)
p = json.load(res)
r = p["results"]
#for i in range(0,10):
print r[0]["text"]
