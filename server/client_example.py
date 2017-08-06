import httplib
from datetime import datetime
import json


TESTDATA = {'text': 'my example text'}

#conn = httplib.HTTPSConnection("sheltered-river-24109.herokuapp.com", 443)
conn = httplib.HTTPConnection("localhost", 8880)
conn.request("POST", "/", json.dumps(TESTDATA))

res = conn.getresponse()

print(res.status, res.reason)

print(res.read())

