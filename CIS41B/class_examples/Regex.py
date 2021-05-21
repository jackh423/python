import re

address = "<De Anza College>,<12250 Stevens Creek Blvd>,<Cupertino>,<95014>,<864-5300>"

morse = ".--. -.-- - .... ---','-.'"
letters = ['P','Y','T','H','O','N']
    
def RemoveAlphabetic(target):
    print("\D - RemoveAlphabetic")
    print("Before: ",target)
    numbers = re.sub(r'\D',"",target)
    print("After:   ",numbers)
    return numbers

def RemoveNumbers(target):
    print("\d - RemoveNumbers")
    print("Before: ",target)
    alphabetic = re.sub(r'\d',"",target)
    return alphabetic

def RemoveAlphaNumeric(target):
    print("\w - RemoveAlphaNumeric")
    print("Before: ",target)
    alphabetic = re.sub(r'\w',"",target)
    return alphabetic
    
def RemovePunctuation(target):
    print("\W - RemovePunctuation")
    print("Before: ",target)
    alphabetic = re.sub(r'\W',"",target)
    return alphabetic
'''
def RemoveSpaces(target):
    print("\s - RemoveSpaces")
    print("Before: ",target)
    alphabetic = re.sub(r'\s',"",target)
    return alphabetic

def RemoveNonSpaces(target):
    print("\S - RemoveNonSpaces")
    print("Before: ",target)
    alphabetic = re.sub(r'\S',"",target)
    return alphabetic

def RemoveNonVowels(target):
    print("[aeiouAEIOU] - RemoveNonVowels")
    print("Before: ",target)
    nvowelsregex = re.compile(r'[aeiouAEIOU]*')
    vlist = nvowelsregex.findall(target)
    return vlist

def RemoveVowels(target):
    print("[^aeiouAEIOU] - RemoveVowels")
    print("Before: ",target)
    vowelsregex = re.compile(r'[^aeiouAEIOU]')
    nvlist = vowelsregex.findall(target)
    return nvlist

def RemoveCommas(target):
    print("[^,]* - RemoveCommas")
    print("Before: ",target)
    commaregex = re.compile(r'[^,]*')
    clist = commaregex.findall(target)
    return clist
'''
def SubstituteLetter(target,letter,substitute):
    print("Substitute")
    print("Before: ",target)
    regex = re.compile(r''+letter)
    elist = regex.sub(substitute,target)
    print(elist)

def SearchWord(target,word):
    print("SearchWord")
    print("Before: ",target)
    regex = re.compile(r''+word)
    find = regex.search(target)
    return find

def MatchPattern(target,pattern):
    print("MatchPattern")
    print("Before: ",target)
    regex = re.compile(r''+pattern)
    found = regex.search(target)
    return found

def MatchPhone(target):
    print("Match")
    print("Before: ",target)
    m = re.compile(r'''(
                    (\d{3}) # first 3 digits
                    (\s|-|\.) # separator
                    (\d{4}) # last 4 digits
                    )''', re.VERBOSE)
    found = m.findall(target)
    return found

def Splitter(target):
    # \s is whitespace
    # {4} is up to 4
    print("Splitter")
    print("Before: ",target)
    regex = re.compile(r'[\s{4}]*')
    mlist = regex.split(target)
    print(mlist)
    
def isRegexPhone(target):
    # /d is number
    print("Before: ",target)
    print('non-regex phone number')
    phone = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    number = phone.search(target) 
    if number != None:
        return number.group()
    else:
        return "not found"
    
def isPhoneNumber(text):
    print('non-regex phone number')
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print(isPhoneNumber('408-864-5300'))
print(isRegexPhone('My number is 408-864-5300.'))
print(MatchPhone(address))
print(MatchPattern(address,'\d{3}-\d{4}'))
print(RemoveAlphabetic(address))
print(RemoveNumbers(address))
print(RemovePunctuation(address))
print(Splitter(morse))
print(SubstituteLetter(address,'e','E'))
print(SearchWord(address,'Anza'))
