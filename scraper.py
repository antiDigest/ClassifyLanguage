import requests
from BeautifulSoup import BeautifulSoup
import re
import os

url = 'htmlfile.html'
soup = BeautifulSoup(open(url))

for p in soup.findAll('a',href=re.compile('http[.]*')):
	os.system('wget -c '+p['href'])
# print soup.prettify()