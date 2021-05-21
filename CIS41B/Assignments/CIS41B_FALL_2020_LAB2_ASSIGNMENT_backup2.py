from bs4 import BeautifulSoup
from urllib.request import urlopen
from matplotlib import pyplot as plt
import numpy as np


def absolute_value(val):
    a = np.round(val/100.*sizes.sum(), 2)
    return a


site = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions"
html = urlopen(site)
soup = BeautifulSoup(html, 'html.parser')
tb1 = soup.find_all('tbody')[1].find_all('tr')
emission_percentage = []
for row in tb1[5:]:
    emission_percentage.append((row.find_all('td')[0].text.strip(), float(row.find_all("td")[4].text[:-1])))


emission_percentage.sort(key=lambda x: x[1], reverse=True)
data = [i[1] for i in emission_percentage[0:10]]
lab = [i[0] for i in emission_percentage[0:10]]

sizes = np.array(data)
fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels=lab, autopct=absolute_value)
plt.show()



