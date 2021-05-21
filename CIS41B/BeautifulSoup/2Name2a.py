from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
html = urlopen('https://climate.nasa.gov/evidence/')
soup = BeautifulSoup(html, 'html.parser')
print("HTML: {0}, name: {1}, text: {2}".format(soup.h2, soup.h2.name, soup.h2.text))
