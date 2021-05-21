from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
html = urlopen('https://climate.nasa.gov/evidence/')
soup = BeautifulSoup(html, 'html.parser')          
for child in soup.recursiveChildGenerator():        
            if child.name:            
                        print(child.name)
