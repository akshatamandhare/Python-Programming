
## It is the name given to memory location where set of instructions are stored to perform some tasks

## There are 2 types of functions

##1. Inbuilt Functions : These are the functions which are already pre-defined by the developers ex: print(), len(), range()
##2. User Defined Functions : These are the function which are created by the users based on the requirement

## syntax:

# def fname(args):
#     TSB
#     return value
# fname(values)

## def: It is a keyword, which helps to define the function
## fname: It helps to identify the created function
## args: These are required to perform some task
    ## There are 2 types of args
        ##1. Formal Args: These are the args which we pass in the function definition
        ##2. Actual Args: These are the args which we pass in the function call
            ## The number of formal and actual args must be equal
## return: It is a keyword which makes the control to come out of the function
## function call: It is mandatory to execute the created function

## There are 4 types based on args and return values

##1. Function without args and without return values
##2. Function with args and without return values
##3. Function without args and with return values
##4. Function with args and with return values

###########################################################################################

##1. Function without args and without return values

##1. WAP TO EXTRACT ALL THE INTEGER FROM THE GIVEN LIST

List = eval(input('enter the list: '))
out = []
for element in List:
    if type(element) == int:
        out.append(element)
# print(out)

##or

def ext_int():
    List = eval(input('enter the list: '))
    out = []
    for element in List:
        if type(element) == int:
            out.append(element)
    print(out)
# ext_int()

##2. WAP TO GET THE FOLLOWING OUTPUT
# string  = 'abcDEF'
# out = {'a':97, 'b':98, 'c':99 ....}

def get_char_ascii():
    string = input('enter the string: ')
    char_ascii = {}
    for char in string:
        char_ascii[char] = ord(char)
    print(char_ascii)
# get_char_ascii()

#####################################################################################

##2. Function with args and without return values

##1. WAPT CHECK THE STRING HAVING EXACTLY 2 LOWERCASE CHARACTERS OR NOT

# string = input('enter the string: ')
# lowercase_count = 0
# for char in string:
#     if char.islower():
#         lowercase_count += 1
# if lowercase_count == 2:
#     print('THE STRING HAVING EXACTLY 2 LOWERCASE CHARACTERS')
# else:
#     print('THE STRING NOT HAVING EXACTLY 2 LOWERCASE CHARACTERS')

##or

def Count_Lowercase(string):
    lowercase_count = 0
    for char in string:
        if char.islower():
            lowercase_count += 1
    if lowercase_count == 2:
        print('THE STRING HAVING EXACTLY 2 LOWERCASE CHARACTERS')
    else:
        print('THE STRING NOT HAVING EXACTLY 2 LOWERCASE CHARACTERS')
# Count_Lowercase('HELlo')

## WAP TO EXTRACT ALL THE COMPLEX NUMBER FROM THE SET COLLECTION ,
# ONLY IF THE REAL PART OF THE COMPLEX NUMBER IS GREATER THAN 10
# ## s = {34, 5.6, -9-9j, 45 + 6j, 3 + 79j, 'hello', 11 - 9j}
# o = {45 + 6j, 11 - 9j}

def ext_complex(Set):
    out = set()
    for element in Set:
        if type(element) == complex and element.real > 10:
            out.add(element)
    print(out)
# ext_complex({34, 5.6, -9-9j, 45 + 6j, 3 + 79j, 'hello', 11 - 9j})

####################################################################################

##3. Function without args and with return values

##1. WAP TO EXTRACT ALL THE KEY VALUE PAIR FROM THE DICTIONARY
# ONLY IF THE  VALUE IS INTEGER TYPE AND IT SHOULD BE GREATER THAN 10
DICT = {'a':1, 'b':'b', 'c':300}   ## out = {'c':300}

def create_dict():
    Dict = eval(input('enter the dict: '))
    out = {}
    for key, value in Dict.items():
        if type(value) == int and value > 10:
            out[key] = value
    return out
# print(create_dict())

##or

def CreateDict():
    Dict = eval(input('enter the dict: '))
    out = {}
    for key in Dict:
        if type(Dict[key]) == int and Dict[key] > 10:
            out[key] = Dict[key]
    return out
# print(CreateDict())

##2. WAP TO GET PRODUCT OF N NATURAL NUMBERS/ FACTORIAL OF N NATURAL NUMBERS
# 3 ===> 1 * 2 * 3 ==> 6

def Get_Factorial():
    number = int(input('enter the number: '))
    Product = 1
    for num in range(1, number + 1):
        Product *= num
    return Product
# print(Get_Factorial())

#############################################################################################

##4. Function with args and with return values

##1. WAP TO EXTRACT ALL THE KEY VALUE PAIR FROM THE DICTIONARY
# ONLY IF BOTH KEY AND VALUE ARE OF SAME TYPE
DICT = {'a':1, 'b':'b', 'c':300}   ## out = {'b':'b'}

def create_dict(Dict):
    out = {}
    for key, value in Dict.items():
        if type(key) == type(value):
            out[key] = value
    return out
# print(create_dict({'a':1, 'b':'b', 'c':300}))

## WAP TO FIND THE SUM OF ALL THE INDIVIDUAL DIGITS PRESENT
## IN THE GIVEN INTEGER NUMBER ONLY IF THE DIGIT IS EVEN

## 1234 == > 2 + 4 ==> 6

def add_even_num(number):
    Sum = 0
    for digit in str(number):       ## '1234'
        if int(digit) % 2 == 0:
            Sum += int(digit)
    return Sum
# print(add_even_num(1234))








