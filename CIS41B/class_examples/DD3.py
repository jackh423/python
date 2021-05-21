from collections import defaultdict 
  

# Defining a dict 
astring = "abcdefg"
dd = defaultdict(list) 
  
for i in range(len(astring)): 
    dd[i].append(astring[i]) 
      
print("Dictionary with values as list:") 
print(dd) 