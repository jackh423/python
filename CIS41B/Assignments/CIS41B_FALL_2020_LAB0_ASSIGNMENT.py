"""
Name: Srinivas Jakkula
CIS 41B   Fall 2020
Lab Assignment 0
Execution results are at the end of this file.

"""

from collections import namedtuple
from collections import defaultdict
from functools import reduce
import re

TEMPERATURE_DATA_FILE = "Temperature.html"
CO2_DATA_FILE = "Co2.html"

Temperature = namedtuple("Temperature", ["Year", "median", "upper", "lower"])
Co2_Emission = namedtuple("Co2_Emission", ["Year", "Year_avg_emission"])


class TemperatureReader:

    def __init__(self):
        self.temp_dict = defaultdict(lambda: "Temperature data not present for the year selected!")

    def __getitem__(self, key):
        return self.temp_dict[key]

    def temp_reader(self, temp_html_file):
        with open(temp_html_file, "r") as t_file:
            # Regex for int or float number with sign
            regex = re.compile(r'([+-]?\d+(?:\.\d+)?)')
            for line in t_file:
                # print("aaa")
                data = regex.findall(line)
                # print(data)
                if data is not None and len(data) == 4:
                    temp = Temperature._make(data)

                    self.temp_dict[int(temp.Year)] = temp

    def print_temp(self, year):
        print(self.temp_dict[year])

    def get_temp(self, year):
        t = self.temp_dict[year]
        return t.median


class CO2EmissionReader:

    def __init__(self):
        # print("co2")
        self.co2_dict = defaultdict(lambda: "Co2 Emission data not present for the year selected!")

    def __getitem__(self, key):
        return self.co2_dict[key]

    @staticmethod
    def average(lst):
        # return round(sum(lst)/len(lst), 2)
        return round(reduce(lambda a, b: a + b, lst) / len(lst), 2)

    def co2_emission_reader(self, co2_emission_file):
        with open(co2_emission_file, "r") as co2_file:
            d = defaultdict(list)
            regex = re.compile(r'([+-]?\d+(?:\.\d+)?)')
            for line in co2_file:
                data = regex.findall(line)
                if data is not None and len(data) == 7:
                    d[data[0]].append(float(data[3]))
            # for k, v in d.items():
            #     co2_em = Co2_Emission(k, self.average(v))
            #     self.co2_dict[int(co2_em.Year)] = co2_em

            self.co2_dict = {int(Co2_Emission(k, self.average(v)).Year): Co2_Emission(k, self.average(v))
                             for k, v in d.items()}

    def get_co2_emission(self, year):
        c = self.co2_dict[year]
        return c.Year_avg_emission

    def print_co2_emission(self, year):
        print(self.co2_dict[year])


class TempVsCO2Emission(TemperatureReader, CO2EmissionReader):

    def __init__(self):
        TemperatureReader.__init__(self)
        CO2EmissionReader.__init__(self)
        # self.over_lap_years = []
        self.overlap_years = []

    def reader(self):
        TemperatureReader.temp_reader(self, TEMPERATURE_DATA_FILE)
        CO2EmissionReader.co2_emission_reader(self, CO2_DATA_FILE)

    def get_overlap_years(self):
        self.overlap_years.extend(list(set(self.co2_dict.keys() & self.temp_dict.keys())))

    def display_temp_co2_emission_for_overlapping_year(self):
        for year in self.overlap_years:
            print(f"In the year: {year} Temperature is {self.get_temp(year):^10} and CO2 Emission is {self.get_co2_emission(year):^10}")


def main():
    ct = TempVsCO2Emission()
    ct.reader()
    ct.get_overlap_years()
    ct.display_temp_co2_emission_for_overlapping_year()


if __name__ == "__main__":
    main()


"""

Execution results:


/Users/jakkus/PycharmProjects/CIS41B/venv/bin/python /Users/jakkus/PycharmProjects/CIS41B/CIS41B_FALL_2020_LAB0_ASSIGNMENT.py
In the year: 1959 Temperature is   0.017    and CO2 Emission is   315.97  
In the year: 1960 Temperature is   -0.049   and CO2 Emission is   316.91  
In the year: 1961 Temperature is   0.038    and CO2 Emission is   317.64  
In the year: 1962 Temperature is   0.014    and CO2 Emission is   318.45  
In the year: 1963 Temperature is   0.048    and CO2 Emission is   318.99  
In the year: 1964 Temperature is   -0.223   and CO2 Emission is   214.41  
In the year: 1965 Temperature is   -0.14    and CO2 Emission is   320.04  
In the year: 1966 Temperature is   -0.068   and CO2 Emission is   321.38  
In the year: 1967 Temperature is   -0.074   and CO2 Emission is   322.16  
In the year: 1968 Temperature is   -0.113   and CO2 Emission is   323.04  
In the year: 1969 Temperature is   0.032    and CO2 Emission is   324.62  
In the year: 1970 Temperature is   -0.027   and CO2 Emission is   325.68  
In the year: 1971 Temperature is   -0.186   and CO2 Emission is   326.32  
In the year: 1972 Temperature is   -0.065   and CO2 Emission is   327.45  
In the year: 1973 Temperature is   0.062    and CO2 Emission is   329.68  
In the year: 1974 Temperature is   -0.214   and CO2 Emission is   330.18  
In the year: 1975 Temperature is   -0.149   and CO2 Emission is   295.23  
In the year: 1976 Temperature is   -0.241   and CO2 Emission is   332.04  
In the year: 1977 Temperature is   0.047    and CO2 Emission is   333.83  
In the year: 1978 Temperature is   -0.062   and CO2 Emission is   335.4   
In the year: 1979 Temperature is   0.057    and CO2 Emission is   336.84  
In the year: 1980 Temperature is   0.092    and CO2 Emission is   338.75  
In the year: 1981 Temperature is    0.14    and CO2 Emission is   340.1   
In the year: 1982 Temperature is   0.011    and CO2 Emission is   341.45  
In the year: 1983 Temperature is   0.194    and CO2 Emission is   343.05  
In the year: 1984 Temperature is   -0.014   and CO2 Emission is   307.42  
In the year: 1985 Temperature is   -0.03    and CO2 Emission is   346.12  
In the year: 1986 Temperature is   0.045    and CO2 Emission is   347.42  
In the year: 1987 Temperature is   0.192    and CO2 Emission is   349.19  
In the year: 1988 Temperature is   0.198    and CO2 Emission is   351.57  
In the year: 1989 Temperature is   0.118    and CO2 Emission is   353.12  
In the year: 1990 Temperature is   0.296    and CO2 Emission is   354.39  
In the year: 1991 Temperature is   0.254    and CO2 Emission is   355.61  
In the year: 1992 Temperature is   0.105    and CO2 Emission is   356.45  
In the year: 1993 Temperature is   0.148    and CO2 Emission is   357.1   
In the year: 1994 Temperature is   0.208    and CO2 Emission is   358.83  
In the year: 1995 Temperature is   0.325    and CO2 Emission is   360.82  
In the year: 1996 Temperature is   0.183    and CO2 Emission is   362.61  
In the year: 1997 Temperature is    0.39    and CO2 Emission is   363.73  
In the year: 1998 Temperature is   0.539    and CO2 Emission is   366.7   
In the year: 1999 Temperature is   0.306    and CO2 Emission is   368.38  
In the year: 2000 Temperature is   0.294    and CO2 Emission is   369.55  
In the year: 2001 Temperature is   0.441    and CO2 Emission is   371.14  
In the year: 2002 Temperature is   0.496    and CO2 Emission is   373.28  
In the year: 2003 Temperature is   0.505    and CO2 Emission is   375.8   
In the year: 2004 Temperature is   0.447    and CO2 Emission is   377.52  
In the year: 2005 Temperature is   0.545    and CO2 Emission is   379.8   
In the year: 2006 Temperature is   0.506    and CO2 Emission is   381.9   
In the year: 2007 Temperature is   0.491    and CO2 Emission is   383.79  
In the year: 2008 Temperature is   0.395    and CO2 Emission is   385.6   
In the year: 2009 Temperature is   0.506    and CO2 Emission is   387.43  
In the year: 2010 Temperature is    0.56    and CO2 Emission is   389.9   
In the year: 2011 Temperature is   0.425    and CO2 Emission is   391.65  
In the year: 2012 Temperature is    0.47    and CO2 Emission is   393.85  
In the year: 2013 Temperature is   0.514    and CO2 Emission is   396.52  
In the year: 2014 Temperature is   0.579    and CO2 Emission is   398.65  
In the year: 2015 Temperature is   0.763    and CO2 Emission is   400.83  
In the year: 2016 Temperature is   0.797    and CO2 Emission is   404.24  
In the year: 2017 Temperature is   0.677    and CO2 Emission is   406.55  
In the year: 2018 Temperature is   0.595    and CO2 Emission is   408.52  

Process finished with exit code 0

"""