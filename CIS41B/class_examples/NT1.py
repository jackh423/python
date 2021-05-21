import collections 

# Declaring namedtuple() 
Student = collections.namedtuple('Student',['name','age','DOB']) 

# Adding values 
S = Student('Nancy','19','2541997') 

# initializing iterable  
li = ['Mark', '19', '411997' ] 

# initializing dict 
di = { 'name' : "Bob", 'age' : 19 , 'DOB' : '1391997' } 

# using _make() to return namedtuple() 
print ("The namedtuple instance using iterable is  : ") 
print (Student._make(li)) 

# using _asdict() to return an OrderedDict() 
print ("The OrderedDict instance using namedtuple is  : ") 
print (S._asdict()) 

# using ** operator to return namedtuple from dictionary 
print ("The namedtuple instance from dict is  : ") 
print (Student(**di)) 