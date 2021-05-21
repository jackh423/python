#The name attribute of a tag gives its name and the text attribute its text content. 
from bs4 import BeautifulSoup

with open("index.html", "r") as f: 
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    print("HTML: {0}, name: {1}, text: {2}".format(soup.h2, soup.h2.name, soup.h2.text))
