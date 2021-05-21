#With the recursiveChildGenerator() method we traverse the HTML document. 
from bs4 import BeautifulSoup

with open("index.html", "r") as f:    
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')            
    for child in soup.recursiveChildGenerator():        
        if child.name:            
            print(child.name)
