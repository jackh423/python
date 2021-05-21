from bs4 import BeautifulSoup
import csv

file = "../greenhouse_gas_inventory_data_data.csv"
c = 0
with open(file, "r") as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        # print(row[3])
        if row[1] == str(2014) and row[3] == "carbon_dioxide_co2_emissions_without_land_use_land_use_change_and_forestry_lulucf_in_kilotonne_co2_equivalent":
            print(row[0], row[2])
            c += 1
    # print("haaa")
    # print(reader)
    f.seek(0)
    red = csv.reader(f, delimiter=',')
    x = 0
    for re in red:
        # print("HOOO")
        print(re[3])
        x += 1

print(c)
print(x)

