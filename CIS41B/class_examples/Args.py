def Pack(*args, **kwargs):
    print(type(args))
    print(type(kwargs))

def Add(*num):
    sum = 0
    for n in num:
        sum = sum + n
    return sum
    
def Multiply(*args):
    product = 1
    for x in args:
        product = product * x
    return product

def Average(*args):
    total = 0
    print('Packed Argument Tuple ->', args)
    for i in args:
        total += i
    return total / len(args)
    
def Identify(**data):
    print("\nData type of argument:",type(data))
    for key, value in data.items():
        print("{} is {}".format(key,value))
        
def Concatenate(**words):
    result = ""
    for arg in words.values():
        result += arg
    return result

def Sum(**numbers):
    sum = 0
    for n in numbers.values():
        sum += n
    return sum

Pack()

print(Add(3,5))
print(Add(4,5,6,7))
print(Add(1,2,3,5,6))
t = (10, 30, 60)
print(Add(*t))

print(Average(1, 2, 3))
print(Average(1, 2, 3, 4, 5))
print(Average(1, 2, 3, 4, 5, 6, 7, 8, 9))

print(Multiply(1, 2, 3))
print(Multiply(1, 2, 3, 4, 5))
print(Multiply(1, 2, 3, 4, 5, 6, 7, 8, 9))

Identify(Firstname="Alice", Lastname="Zhu")
Identify(Firstname="Bob", Lastname="Smith", Age=25, Phone=1234567890)
Identify(Firstname="John", Lastname="Jones", Email="johnjones@kwargs.com", Country="US", Age=35, Phone=9876543210)

print(Concatenate(a='United',b='States'))
print(Concatenate(a='De',b='Anza',c='College'))
print(Concatenate(v='Python',w='Programming',x='Language',y='Guido',z='vanRossum'))

d = {'a':10,'b':20,'c':30}
print(Sum(**d))