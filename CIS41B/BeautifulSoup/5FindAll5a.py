from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re

html = urlopen('https://climate.nasa.gov/evidence/')
soup = BeautifulSoup(html, 'html.parser') 
dict = {}
for tag in soup.find_all("li"):
        print("{0}: {1}".format(tag.name, tag.text))
        r = re.compile(r'\s')
        s = r.split(tag.text)
        for i in range (0,len(s)-1):
                dict[s[i]] = s[i+1]
        for k,v in dict.items():
                print('key= ',k,'\tvalue= ',v)