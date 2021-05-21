from collections import defaultdict 


# Defining the dict and passing  
# lambda as default_factory argument 
dd = defaultdict(lambda: "No data") 
dd["x"] = 123
dd["y"] = 234

print(dd["x"]) 
print(dd["y"]) 
print(dd["z"]) 