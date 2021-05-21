from bs4 import BeautifulSoup

with open("index.html", "r") as f:   
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    spanElem = soup.select('span')
    print(spanElem)
    for i in range(0,len(spanElem)):
        print(str((spanElem)[i]))    