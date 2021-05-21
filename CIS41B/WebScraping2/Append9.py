#The append() method appends a new tag to the HTML document. 
from bs4 import BeautifulSoup

with open("index.html", "r") as f:   
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    newtag = soup.new_tag('li')
    newtag.string='OpenBSD'
    ultag = soup.ul    
    ultag.append(newtag)   
    print(ultag.prettify()) 