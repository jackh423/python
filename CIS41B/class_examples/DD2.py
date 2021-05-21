from collections import defaultdict 


# Defining the dict 
dd = defaultdict(lambda: "No data") 
dd["x"] = 123
dd["y"] = 234
print(dd)

# Provides the default value  for the key 
dd.__missing__('x')
dd.__missing__('y')
print(dd)