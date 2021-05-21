'''
Python supports a type of container like dictionaries called 
namedtuples() present in module collection. Like dictionaries 
they contain keys that are hashed to a particular value. But on 
contrary, it supports both access from key value and iteration, 
the functionality that dictionaries lack.
'''

import collections 

# Declaring namedtuple() 
Student = collections.namedtuple('Student',['name','age','DOB'])

# Adding values 
S = Student('Nancy','29','2541997') 

# Access using index 
print ("The Student age using index is : ",end ="") 
print (S[1]) 

# Access using name  
print ("The Student name using keyname is : ",end ="") 
print (S.name) 

# Access using getattr() 
print ("The Student DOB using getattr() is : ",end ="") 
print (getattr(S,'DOB')) 