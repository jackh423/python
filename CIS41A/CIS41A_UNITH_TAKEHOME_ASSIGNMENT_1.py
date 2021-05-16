"""
Name: Srinivas Jakkula
CIS 41A   Spring 2020
Unit H Take-Home Assignment
"""


def overseerSystem(**kwargs):
    for key in kwargs:
        if key == "temperature":
            if kwargs[key] > 500:
                print("Warning: temperature is ", kwargs[key])
        if key == "CO2level":
            if kwargs[key] > .15:
                print("Warning: CO2level is ",kwargs[key])
        if key == "miscError":
            print("Misc error #"+str(kwargs[key]))


# TESTING WITH DICTIONARY
overseerSystem(**{"temperature": 550})
overseerSystem(**{"temperature": 475})
overseerSystem(**{"temperature": 450, "miscError": 404})
overseerSystem(**{"CO2level": .18})
overseerSystem(**{"CO2level": .2, "miscError": 418})

print()
# TESTING USING KEY = VALUE WAY
overseerSystem(temperature=550)
overseerSystem(temperature=475)
overseerSystem(temperature=450, miscError=404)
overseerSystem(CO2level=.18)
overseerSystem(CO2level=0.2, miscError=418)


"""
Execution results:

/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITH_TAKEHOME_ASSIGNMENT_1.py
Warning: temperature is  550
Misc error #404
Warning: CO2level is  0.18
Warning: CO2level is  0.2
Misc error #418

Warning: temperature is  550
Misc error #404
Warning: CO2level is  0.18
Warning: CO2level is  0.2
Misc error #418

Process finished with exit code 0

"""