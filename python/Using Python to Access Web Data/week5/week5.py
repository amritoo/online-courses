import urllib.request
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
data = urllib.request.urlopen(url, context=ctx).read()

print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
ar = [int(count.text) for count in counts]

print('Count:', len(ar))
print('Sum:', sum(ar))
