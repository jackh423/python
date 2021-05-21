import re
from collections import defaultdict
from collections import namedtuple
from functools import reduce

# with open("Temperature.html", "r") as t_file:
#     # t_file_content = t_file.read()
#     # print(t_file_content)
#     # regex = re.compile(r'-?\d+\.\d+')
#     regex = re.compile(r'(\d+(?:\.\d+)?)')
#     for line in t_file:
#         # print(line)
#         data = regex.findall(line)
#         if data is not None and len(data) == 4:
#             print(data)

        # phone = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
        # number = phone.search(target)
        # number = phone.search(target)
        # if number != None:
        #     return number.group()
        # print(line)


def co2_def_value():
    return "Co2 data not present for the year selected"


co2_dict = defaultdict(co2_def_value)

Temperature = namedtuple("Temperature", ["Year", "median", "upper", "lower"])

# Co2_Emission = namedtuple("Co2_Emission", ["Year", "year_avg_decimal", "year_avg", "year_avg_interpoated", "avg_trend"])

Co2_Emission = namedtuple("Co2_Emission", ["Year", "Year_avg_emission"])


co2_dict = defaultdict(lambda: "Co2 Emission data not present for the year selected!")


def average(lst):
    # round(answer, 2)
    return round(reduce(lambda a, b: a + b, lst) / len(lst), 2)


with open("Co2.html", "r") as co2_file:
    d = defaultdict(list)
    regex = re.compile(r'([+-]?\d+(?:\.\d+)?)')
    for line in co2_file:
        data = regex.findall(line)
        # print(data)
        if data is not None and len(data) == 7:
            # print(data)
            # co2_em = Co2_Emission(data[0], )
            d[data[0]].append(float(data[3]))
    for k, v in d.items():
        # print(v)
        # print(average(v))
        co2_em = Co2_Emission(k, average(v))
        co2_dict[co2_em.Year] = co2_em.Year_avg_emission

    for ke, va in co2_dict.items():
        print(ke, va)



