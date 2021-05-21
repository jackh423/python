from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
html = urlopen('https://climate.nasa.gov/evidence/')
soup = BeautifulSoup(html, 'html.parser') 
root = soup.body
root_childs = [e.name for e in root.descendants if e.name is not None]
print(root_childs)