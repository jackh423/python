# 1. Scrape, using BeautifulSoup, the local html page: Presidents.html.
# Scrape the term number and President name into a dictionary.
from bs4 import BeautifulSoup
PAGE="Presidents.html"
presidents_dict = {}
with open(PAGE, "r") as f:
    contents = f.read()
    # soup = BeautifulSoup(contents, 'html.parser')
    soup = BeautifulSoup(contents, 'lxml')
    # print(soup.prettify())
    for tag in soup.find_all("tr")[1:]:
        # print(tag)
        # print(len(tag.find_all("b")))
        # for el in tag.find_all("b"):
        #     print(el.txt)
        for el in tag.find_all("td"):
            # print(el)
            # print(el.text.split())
            presidents_dict[el.text.split()[0]] = el.text.split()[1:]
        #
        #     break
        # break
    print(presidents_dict)
# tb1 = soup.find_all('tbody').find_all('tr')
# tb1 = soup.find_all('tr')
# print(tb1)
# 2. Using your dictionary generated in question 1, convert the dictionary to a JSON string.

# 3. Using your SQLite insert function from either lab1, lab2 or lab3, insert the JSON string into your SQLite database.

# 4. Show how to put the function defined in question #3 on a thread.

# 5. Convert the JSON string from question #2 to an XML file.