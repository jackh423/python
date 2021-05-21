from bs4 import BeautifulSoup
from urllib.request import urlopen
from pprint import pprint
from matplotlib import pyplot as plt
import numpy as np

site = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions"

html = urlopen(site)
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# tb = soup.find_all("tbody")
# print(tb)
# pprint(tb[1])

# tb1 = soup.find_all('table')[1].find_all('tr')
tb1 = soup.find_all('tbody')[1].find_all('tr')
# c = 0
emission_percentage = []
e_p = []
for row in tb1[5:]:
    # print(row)
    # print("!!!!!!!!!!")
    print(row.find_all('td')[0].text, row.find_all("td")[4].text)
    # print(row.find_all("td")[4].text)
    # print("#################")
    emission_percentage.append((row.find_all('td')[0].text.strip(), float(row.find_all("td")[4].text[:-1])))
    e_p.append(float(row.find_all("td")[4].text[:-1]))

print(len(emission_percentage))
emission_percentage.sort(key=lambda x: x[1], reverse=True)
print(emission_percentage[0:10])
print(e_p)

data = [i[1] for i in emission_percentage[0:10]]
lab = [i[0] for i in emission_percentage[0:10]]
print(data)
print(lab)
sizes = np.array(data)


def absolute_value(val):
    a = np.round(val/100.*sizes.sum(), 2)
    return a


fig = plt.figure(figsize =(10, 7))
# plt.pie(data, labels=lab, autopct='%1.2f%%')
# plt.pie(data, labels=lab, autopct=absolute_value, shadow=True)
plt.pie(data, labels=lab, autopct=absolute_value)
# plt.pie(data)
plt.show()

# print(sorted(emission_percentage, reverse=True)[0:10])

    # c += 1
    # if c > 5:
    #     break
# print(tb1)

# for tb in soup.find_all("tbody"):
#     print(tb)

