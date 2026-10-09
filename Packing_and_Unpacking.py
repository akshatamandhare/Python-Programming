
## Packing: It helps to group the individual data item in the form of collection

## There are 2 types

##1. Tuple Packing
##2. Dictionary Packing

#################################################################################

##1. Tuple Packing: It helps to group the individual data item in the form of tuple
## Here we can pass 0 to n number of positional only args
## These args are collected using "*args"

## syntax:

# def fname(*args):
#     TSB
# fname(v1, v2,......)

##1.

def get_pos_args(*args):
    print(args)
# get_pos_args()
# get_pos_args(1,2,3,4.5,5-9j, 'hii')

## Create the function which takes 0-n number of positional(mandatory) args
## get only sum of integer number

def add_numbers(*args):
    print(args)
    Sum = 0
    for element in args:
        if type(element) == int:
            Sum += element
    return Sum
# print(add_numbers())
# print(add_numbers(1,2,3,4.5,5-9j, 'hii'))

## Create the function which takes 0-n number of positional(mandatory) args
## get only sum of  even integer number

def add_even_numbers(*args):
    print(args)
    Sum = 0
    for element in args:
        if type(element) == int and element % 2 == 0:
            Sum += element
    return Sum
# print(add_even_numbers())
# print(add_even_numbers(1,2,3,4.5,5-9j, 'hii'))

############################################################################################

##2. Dictionary Packing:It helps to group the individual data item in the form of dict
## Here we can pass 0 to n number of keyword only args
## These args are collected using "**kwargs"

## syntax:

# def fname(**kwargs):
#     TSB
# fname(k1 = v1, k2 = v2 ,.....)

##1.

def get_key_args(**kwargs):
    print(kwargs)
# get_key_args()
# get_key_args(a = 1, b = 2, c = 3)

## Create the function, which takes n number of keyword args get each key value pair one by one

def get_key_value(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
# get_key_value()
# get_key_value(a = 1, b = 2, c = 3)

## Create the function, which takes n number of keyword args get the key and value
## only if the value belongs to float type

def get_key_value(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        if type(value) == float:
            print(key, value)
# get_key_value(a = 1.2, v = 4, r = 4.4)

##########################################################################################

## Variable Arguments: It helps to pass both positional and keyword args in the same program

## syntax:

# def fname(*args, **kwargs):
#     TSB
# fname(v1, v2,.....)
# fname(k1 = v1, k2 = v2,...)
# fname(v1, v2,...k1 = v1, k2 = v2,...)

##1.

def get_pos_key_args(*args, **kwargs):
    print(args, kwargs)
# get_pos_key_args()
# get_pos_key_args(1,2,3,4)
# get_pos_key_args(a = 1, b = 2, v = 4)
# get_pos_key_args(1, 2, 3, 4, a = 1, b = 2, v = 4)

## create the function, which takes both positional and keyword args
## iterate over both the collections

def get_pos_key_args(*args, **kwargs):
    print(args, kwargs)
    for ele in args:
        print(ele)
    for key, value in kwargs.items():
        print(key, value)
# get_pos_key_args(1,2,3,4)
# get_pos_key_args(a = 1, b = 2, v = 4)
# get_pos_key_args(1, 2, 3, 4, a = 1, b = 2, v = 4)

#########################################################################################

## Unpacking: It helps divide the collection into individual data item

## syntax:

# def fname(var1, var2,..):
#     TSB
# fname(*collection)


## unpack the list
List = ['Testyantra', 88.8, (9, 10, 2026)]
company, share, Date = List
print(company, share, Date)

## The number of variables we use to unpack the collection must be equal to the length of the collection

## unpack the tuple

date, month, year = Date
print(date, month, year)

date, month, year = List[2]
print(date, month, year)

def unpack(var1, var2, var3):
    print(var1, var2, var3)
unpack(*'hii')
unpack(*[1,2,3])
unpack(*(11, 22, 33))
unpack(*{111, 222, 333})
unpack(*{'a':1, 'b':2, 'c':3})
unpack(*{'a':1, 'b':2, 'c':3}.values())
unpack(*{'a':1, 'b':2, 'c':3}.items())

## When we use the function to unpack the collection, the number of variables we use in function definition
## must be equal to length of collection the function call


