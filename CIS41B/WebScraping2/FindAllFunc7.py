#The find_all() method can also take a function which determines 
#what elements should be returned. 
from bs4 import BeautifulSoup

def myfun(tag):   
    return tag.is_empty_element

with open("index.html", "r") as f: 
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    tags = soup.find_all(myfun)
    print(tags) 
