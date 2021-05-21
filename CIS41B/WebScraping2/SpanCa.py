from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
html = urlopen('https://climate.nasa.gov/evidence/')
soup = BeautifulSoup(html, 'html.parser')
pElems = soup.select('span')
print(spanElem)
for i in range(0,len(spanElem)):
    print(str((spanElem)[i]))
