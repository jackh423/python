from bs4 import BeautifulSoup
import re

with open("index.html", "r") as f:   
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    print(soup.prettify())
    dict = {}
    for tag in soup.find_all("li"):
        print("{0}: {1}".format(tag.name, tag.text))
        r = re.compile(r'\s')
        s = r.split(tag.text)
        dict[s[0]] = s[1]
    for k,v in dict.items():
        print('key= ',k,'\tvalue= ',v)