
## Decorators: It helps to add extra functionality into the function without changing anything in the original code

a = 100
b = a
# print(a, b)
# print(id(a), id(b))

####################################################################################

def Sam():
    print('hello')
# Sam()
# print(Sam)

# x = Sam
# print(x)

# x()

####################################################################################

def dummy(some_thing):
    print(some_thing)
# dummy(Sam)

def dummy1(some_thing):
    print(some_thing)
    res = some_thing()
    return res
# dummy1(Sam)

###############################################################################

def greet():
    print('Hello Good Morning')

def greeting(name):
    print(f'hello {name}')

def Wish(name, wish):
    print(f'Hello {wish} myself {name}')

def dummy2(some_thing):
    print(some_thing)
    return some_thing('Sonu', 'Good Morning')
# dummy2(greet)
# dummy2(greeting)
# dummy2(Wish)

##########################################################################

def dummy3(some_thing, *args):
    print(some_thing, args)
    return some_thing(*args)
# dummy3(greet)
# dummy3(greeting, 'Sonu')
# dummy3(Wish, 'Sonu', 'Good Morning')

##########################################################################

def outer(some_thing):
    print(some_thing)
    def inner(*args, **kwargs):
        print(args, kwargs)
        return some_thing(*args, **kwargs)
    return inner('Monu', wish = 'Good Morning')
# outer(greeting)
# outer(Wish)

##########################################################################

## add few seconds of delay

def add(a, b):
    return a + b

import time

def delay(some_thing):
    print(some_thing)
    def wrapper(a, b):
        time.sleep(4)
        return some_thing(a, b)
    return wrapper(12, 13)
# print(delay(add))

####################################################################################

## create the standalone function which takes integer input returns the same output
## create extra function which add the functionality to convert the negative to positive and positive be the same
## decorate the standalone function

def get_positive_no(some_thing):
    print(some_thing)
    def wrapper(number):
        res = number
        return abs(res)
    return wrapper

# @get_positive_no
def get_number(number):
    return number
# print(get_number(54))

####################################################################################

## create the standalone function which takes integer input returns the same output
## create extra function which add the functionality, get the number if it is even
# else get message 'the number is odd'
## decorate the standalone function

def check_odd_even(some_thing):
    print(some_thing)
    def wrapper(number):
        if number%2==0:
            return number
        else:
            print("The number id Odd")
    return some_thing

# @check_odd_even
def get_number(number):
    return number
# print(get_number(10))

####################################################################################

## create the standalone function which takes integer input returns the same output
## create extra function which add the functionality to convert the negative to positive and positive be the same
## decorate the standalone function

def reverse_string(some_thing):
    print(some_thing)
    def wrapper(string):
        return string[::-1]
    return wrapper

# @reverse_string
def get_string(string):
    return string
# print(get_string("Akshata"))


## create the standalone function which gets string "Hello Hii" as input and return tha same as output
## create one more function which have the functionality to replace "Hii" by "bye"
## decorate the standalone function

def replace(some_thing):
    print(some_thing)
    def wrapper(string):
        if 'Hii' in string:
            string.replace('Hii', 'bye')
            return string
    return wrapper

# @replace
def get_string(string):
    return string
# print(get_string("Hii Akshata"))
            

## create the standalone function which gets string input and return the same
## create one more function which have the functionality to execute the output 3 times
## decorate the standalone function


def three_times(some_thing):
    print(some_thing)
    def wrapper(string):
        for i in range(3):
            print(some_thing(string))
    return wrapper

@three_times
def get_string(string):
    return string
# get_string("Hii Akshata")



## create the standalone function which takes any number of args and returns the same
## create a function which have the functionality
# to get the total number of args passed and also invoke it
## decorate the standalone function


def get_args(some_thing):
    print(some_thing)
    def wrapper(*args, **kwargs):
        print(f'The length of args is {len(args)+len(kwargs)}')
        return some_thing(*args, **kwargs)
    return wrapper

@get_args
def takes_args(*args, **kwargs):
    print(args, kwargs)
takes_args(1)
takes_args(a = 1, b = 2)
takes_args(1,2,3,a = 1, b = 2)

