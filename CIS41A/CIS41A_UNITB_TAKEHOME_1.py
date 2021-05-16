'''
Srinivas Jakkula
CIS 41A   Spring 2020
Unit B take-home assignment 1
'''

# Below section of code is for String Type Tests
user_input = input("Enter a string:   ")
print("User input string is upper: ", user_input.isupper())
print("User input string is digit: ", user_input.isdigit())
print("User input string is isalpha: ", user_input.isalpha())
print("")
# Below section of the code is for Escape Characters within a string
haiku_str = "Type, type, type away.\n Compile. Run. Hip hip hooray!\n No error today!"
print(haiku_str)
print("")
# Below section of code is for Slicing a string
quote ="And now for something completely different"
print(quote[:6])
print(quote[-4:])
print(quote[14:16])
print(quote[::2])
print(quote[::-1])
print("")
#Below section of code is for Using string operators + and *
pattern1 = ".~*'"
pattern2 = pattern1 + pattern1[::-1]
print(pattern2*5)

'''
Execution results:

########################################################################
Program Output:
########################################################################
/usr/bin/python3 /Users/jakkus/PycharmProjects/CIS41A/CIS41A_UNITB_TAKEHOME_1.py
Enter a string:   ABC123
User input string is upper:  True
User input string is digit:  False
User input string is isalpha:  False

Type, type, type away.
 Compile. Run. Hip hip hooray!
 No error today!

And no
rent
me
Adnwfrsmtigcmltl ifrn
tnereffid yletelpmoc gnihtemos rof won dnA

.~*''*~..~*''*~..~*''*~..~*''*~..~*''*~.

Process finished with exit code 0
'''