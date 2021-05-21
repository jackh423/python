#With the prettify() method, we can make the HTML code look better. 
from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    newtag = soup.new_tag('li')
    newtag.string='OpenBSD'
    ultag = soup.ul  
    ultag.append(newtag)  
    print(ultag.prettify()) 