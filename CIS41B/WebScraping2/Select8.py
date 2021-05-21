#With the select() and select_one() methods, we can use some 
#CSS selectors to find elements.
from bs4 import BeautifulSoup

with open("index.html", "r") as f:   
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    print(soup.select("li:nth-of-type(3)"))