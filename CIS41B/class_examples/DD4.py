from collections import defaultdict 


# Defining the dict 
dd = defaultdict(int) 

L = ['a','b','c','d','e','f','g'] 

# Iterate through the list 
for c in L: 

    # The default value is 0 
    dd[c] += ord(c)

print(dd) 