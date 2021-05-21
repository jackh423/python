from bs4 import BeautifulSoup
from urllib.request import urlopen

# site = "https://www.kaggle.com/unitednations/international-greenhouse-gas-emissions/version/1?select=greenhouse_gas_inventory_data_data.csv"
site = "https://www.kaggle.com/unitednations/international-greenhouse-gas-emissions"
html = urlopen(site)
soup = BeautifulSoup(html, 'html.parser')

# tb = soup.find_all(class_="sc-fzqAbL sc-fzqMAW dmEdIJ")
tb = soup.find_all('div')
print(tb)
