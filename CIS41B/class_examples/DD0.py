'''
Dictionary in Python is an unordered collection of data values 
that are used to store data values like a map. Unlike other Data 
Types that hold only single value as an element, the Dictionary 
holds key:value pair. In Dictionary, the key must be unique and 
immutable. This means that a Python Tuple can be a key whereas 
a Python List can not. A Dictionary can be created by placing a 
sequence of elements within curly {} braces, separated by comma.

Defaultdict is a container like dictionaries present in the module 
collections. Defaultdict is a sub-class of the dict class that returns 
a dictionary-like object. The functionality of both dictionaries and 
defualtdict are almost same except for the fact that defualtdict never 
raises a KeyError. It provides a default value for the key that does 
not exist.
'''

from collections import defaultdict 
  
try:
    Dict = {10: 'Face', 20: 'To', 30: 'Face'}  
    print("Dictionary:")  
    print(Dict) 
    print(Dict[20]) 
    print(Dict[40]) 
except KeyError:
    print("Exception:  Value not in dictionary")
  
# Function to return a default 
# values for keys that is not present 
def def_value(): 
    return 0
      
# Defining the dict 
dd = defaultdict(def_value) 
dd["abc"] = 1
dd["xyz"] = 2
  
print(dd["abc"]) 
print(dd["xyz"]) 
print(dd["aaa"]) 