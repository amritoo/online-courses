import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
position = int(input('Enter position: ')) - 1
count = int(input('Enter count: '))

# go and print the 'position'-th url 'count' times
print(url)
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    url = [tag.get('href', None) for tag in soup('a')][position]
    print(url)
# end for

print('Answer =', re.findall('_([A-Za-z]+).html$', url)[0])
