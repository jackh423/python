from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

def EmptyTag(tag):   
    return tag.is_empty_element

html = urlopen('https://climate.nasa.gov/evidence/')
soup = BeautifulSoup(html, 'html.parser') 
tags = soup.find_all(EmptyTag)
print(tags) 
