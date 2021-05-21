# importing "collections" for namedtuple() 
from collections import namedtuple
  
# Declaring namedtuple() 
Student = namedtuple('Student',['name','age','DOB']) 
  
# Adding values 
S = Student('Nancy','19','2541997') 
  
# using _fields to display all the keynames of namedtuple() 
print ("All the fields of students are : ") 
print (S._fields) 
  
# using _replace() to change the attribute values of namedtuple 
print ("The modified namedtuple is : ") 
print(S._replace(name = 'Nick')) 