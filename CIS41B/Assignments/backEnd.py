from collections import namedtuple
from collections import defaultdict
from functools import reduce
import re


TEMPERATURE_DATA_FILE = "Temperature.html"
CO2_DATA_FILE = "Co2.html"

Temperature = namedtuple("Temperature", ["Year", "median", "upper", "lower"])
temp_dict = defaultdict(lambda: "Temperature data not present for the year selected!")

Co2_Emission = namedtuple("Co2_Emission", ["Year", "Year_avg_emission"])
co2_dict = defaultdict(lambda: "Co2 Emission data not present for the year selected!")


def average(lst):
    # return round(sum(lst)/len(lst), 2)
    return round(reduce(lambda a, b: a + b, lst) / len(lst), 2)


def read_temp_data(inp_file):
    try:
        with open(inp_file, "r") as t_file:
            # Regex for int or float number with sign
            regex = re.compile(r'([+-]?\d+(?:\.\d+)?)')
            for line in t_file:
                data = regex.findall(line)
                # print(data)
                if data is not None and len(data) == 4:
                    temp = Temperature._make(data)
                    # print(temp)
                    temp_dict[temp.Year] = temp

        # return temp_dict

    except IOError:
        print("Error: File does not appear to exists")
        # return
    except Exception as e:
        print("Error: There seems to be an error in processing Temperature.html file", e)
        # print(e, inp_file)
        # return


def read_co2_emission(input_file):
    try:
        with open(input_file, "r") as co2_file:
            d = defaultdict(list)
            regex = re.compile(r'([+-]?\d+(?:\.\d+)?)')
            for line in co2_file:
                data = regex.findall(line)
                # print(data)
                if data is not None and len(data) == 7:
                    # print(data)
                    d[data[0]].append(float(data[3]))
            for k, v in d.items():
                co2_em = Co2_Emission(k, average(v))
                # co2_dict[co2_em.Year] = co2_em.Year_avg_emission
                co2_dict[co2_em.Year] = co2_em
        # return co2_dict
    except IOError:
        print("Error: File does not appear to exists")
        # return
    except Exception as e:
        print("Error: There seems to be an error in processing Temperature.html file", e)
        # return


def check_if_year_overlaps(year):
    if year in temp_dict and year in co2_dict:
        return True
    return False


def get_temp(year):
    t = temp_dict[year]
    # print(dir(t))
    # print(t.median)
    return t.median
    # return temp_dict[year].median


def get_co2_emission(year):
    c2 = co2_dict[year]
    # return c2[1]
    return c2.Year_avg_emission
    # return co2_dict[year].Year_avg.emission


def run_program():
    read_temp_data(TEMPERATURE_DATA_FILE)
    read_co2_emission(CO2_DATA_FILE)
    while True:
        year = input("Enter the year to display temperature and co2 emissions: ")
        if check_if_year_overlaps(year):
            # print(temp_dict[year])
            # print(co2_dict[year])
            print(f"In the year: {year} Temperature is {get_temp(year)} and CO2 Emission is {get_co2_emission(year)}")
        else:
            print(f"There is no overlapping data of temp and/or co2 emission for the year: {year}")


class Backend:

    def __init__(self):
        print("I am here")


if __name__ == "__main__":
    run_program()




#
# Use sets, because they have a built-in intersection method which ought to be quick:
#
# myRDP = { 'Actinobacter': 'GATCGA...TCA', 'subtilus sp.': 'ATCGATT...ACT' }
# myNames = { 'Actinobacter': '8924342' }
#
# rdpSet = set(myRDP)
# namesSet = set(myNames)
#
# for name in rdpSet.intersection(namesSet):
#     print name, myNames[name]

# Prints: Actinobacter 8924342






    # print(['2018'])
    # print(temp_dict['2018'])

    # b = Backend()
    #print("I am after")
    # year = input("Enter the year to display temperature and co2 emissions: ")
    # print(b.print_temp_co2_em(year))


    # read_temp_data(TEMPERATURE_DATA_FILE)
    #
    # print(temp_dict['1850'])
    #
    # read_co2_emission(CO2_DATA_FILE)
    #
    # print(co2_dict['2018'])






### Waste code

# def co2_def_value():
#     return "Co2 data not present for the year selected"
#
#
# co2_dict = defaultdict(co2_def_value)


# def temp_def_value():
#     return "Temp data not present for the year selected"
#
#
# temp_dict1 = defaultdict(temp_def_value)

# Temperature = namedtuple("Temperature", ["year", "median", "upper", "lower"])


    # print(Temperature(temp_dict['1018']))

    # print(co2_dict[1930])

#
# with open("Co2.html", "r") as co2_file:
#     d = defaultdict(list)
#     regex = re.compile(r'([+-]?\d+(?:\.\d+)?)')
#     for line in co2_file:
#         data = regex.findall(line)
#         # print(data)
#         if data is not None and len(data) == 7:
#             # print(data)
#             # co2_em = Co2_Emission(data[0], )
#             d[data[0]].append(float(data[3]))
#     for k, v in d.items():
#         # print(v)
#         # print(average(v))
#         co2_em = Co2_Emission(k, average(v))
#         co2_dict[co2_em.Year] = co2_em.Year_avg_emission
#
#     for ke, va in co2_dict.items():
#         print(ke, va)


# except:
#     e = sys.exc_info()[0]
#     print("Error: There seems to be error in processing Temperature.html file", e)


# @staticmethod
# def read_co2_emission(input_file):
#     try:
#         with open(input_file, "r") as co2_file:
#             d = defaultdict(list)
#             regex = re.compile(r'([+-]?\d+(?:\.\d+)?)')
#             for line in co2_file:
#                 data = regex.findall(line)
#                 # print(data)
#                 if data is not None and len(data) == 7:
#                     # print(data)
#                     d[data[0]].append(float(data[3]))
#             for k, v in d.items():
#                 co2_em = Co2_Emission(k, average(v))
#                 # co2_dict[co2_em.Year] = co2_em.Year_avg_emission
#                 co2_dict[co2_em.Year] = co2_em
#         return temp_dict
#     except IOError:
#         print("Error: File does not appear to exists")
#         return
#     except Exception as e:
#         print("Error: There seems to be an error in processing Temperature.html file", e)
#         return



        # print("I am in init")
        # # self.year_wise_temp_data = Backend.read_temp_data(TEMPERATURE_DATA_FILE)
        # print("I am ")
        # self.year_wise_co2_emission_data = Backend.read_co2_emission(CO2_DATA_FILE)

    # def print_temp_co2_em(self, year):
    #     # self.year_wise_temp_data[year]
    #     pass

