# Write a Named Tuple to hold the data in the Temperature.csv (partially listed below).
#
#
# Temperature.csv file excerpt:
# Year,Median,Upper,Lower
# 1850,-0.373,-0.339,-0.425
# 1851,-0.218,-0.184,-0.274
# 1852,-0.228,-0.196,-0.28
# 1853,-0.269,-0.239,-0.321
# 1854,-0.248,-0.218,-0.301
# 1855,-0.272,-0.241,-0.324
# 1856,-0.358,-0.327,-0.413
# 1857,-0.461,-0.431,-0.512
# 1858,-0.467,-0.435,-0.521
# 1859,-0.284,-0.249,-0.34
# 1860,-0.343,-0.31,-0.405

from collections import namedtuple

Temperature = namedtuple("Temperature", ["Year", "Median", "Upper", "Lower"])