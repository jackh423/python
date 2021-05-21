from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
html = urlopen('https://climate.nasa.gov/evidence/')
soup = BeautifulSoup(html, 'html.parser') 
newtag = soup.new_tag('li')
newtag.string='OpenBSD'
ultag = soup.ul  
ultag.append(newtag)  
print(ultag.prettify()) 