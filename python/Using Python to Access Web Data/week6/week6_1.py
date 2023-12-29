import urllib.request
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
data = urllib.request.urlopen(url, context=ctx).read()

print('Retrieved', len(data), 'characters')
info = json.loads(data)

ar = [int(x['count']) for x in info['comments']]

print('Count:', len(ar))
print('Sum:', sum(ar))
