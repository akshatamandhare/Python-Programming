## Exception: It is an unauthorized error that occurs while executing the program
## Exception handling helps to handle the error which stops the program execution
## The syntax error can't be handled using the exception handling
## There are 4 blocks
##1. try            ##2. except             ##3. else           ##4. finally
## Among these 4 blocks try and except blocks are the mandatory blocks
## Whereas else and finally are the optional
## In try block we will have the problem statement in except block we will have the solution for the problem

#########################################################################

##1. Specific Exception Handling:

# names = ['apple', 'orange', 'apple', 'apple', 'orange']
# name_count = {}
# for name in names:
#     name_count[name] += 1
# print(name_count)

## Handle the KeyError

names = ['apple', 'orange', 'apple', 'apple', 'orange']
name_count = {}
for name in names:
    try:
        name_count[name] += 1
    except KeyError:
        name_count[name] = 1
# print(name_count)

##2.

def div(a, b):
    return a/b
# print(div(40, 0))

## Handle ZeroDivisionError

def Division(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('The value of b should not be 0')
# Division(60, '5')

## Handle ZeroDivisionError and TypeError

def Division(a, b):
    try:
        res = a/b
    except ZeroDivisionError:
        print('The value of b should not be 0')
    except TypeError:
        print('Invalid values')
    ## It gets executed only when there in no error in the try block
    else:
        print(res)
    ## It executes in each and every execution
    finally:
        print('Completed my work')
# Division(40, '5')

##3. create the function, inside which have the try block inside the try block take user list input
## and user index input. If index position present get the element at that position if not handle the error

def Index_Error():
    try:
        List = eval(input('enter the list: '))
        Index_Position = int(input('enter the index position: '))
        print(f'The element present at {Index_Position} is {List[Index_Position]}')
    except IndexError:
        print('Invalid index position')
# Index_Error()

def Handle_Error():
    try:
        List = eval(input('enter the list: '))
        Index_Position = int(input('enter the index position: '))
        print(f'The element present at {Index_Position} is {List[Index_Position]}')
    except IndexError:
        print('Invalid index position')
    except ValueError:
        print('The index position should always be integer type')
# Handle_Error()

########################################################################################

##2. Generic Exception Handling:

names = ['apple', 'orange', 'apple', 'apple', 'orange']
name_count = {}
for name in names:
    try:
        name_count[name] += 1
    except:
        name_count[name] = 1
# print(name_count)

##2.

def Division(a, b):
    try:
        print(a/b)
    except:
        print('Error Handled')
# Division(60, 0)

##3.

# def Handle_Error():
#     try:
#         List = eval(input('enter the list: '))
#         Index_Position = int(input('enter the index position: '))
#         print(f'The element present at {Index_Position} is {List[Index_Position]}')
#     except Exception:
#         print('Learn Indexing')
# Handle_Error()

###################################################################################

## custom exception handling: It helps to throw the error whenever we want
## syntax: raise Errorname('msg')       ## msg is optional

# Data = eval(input('enter the data: '))
# for ele in Data:
#     if type(ele) == int:
#         print(ele)
#     else:
#         raise TypeError('Encountered non-int type')

## Take any 2 collections and check the length, print the message "both have the same length" if
## the length is equal else raise the error

# Data1 = eval(input('enter the data1: '))
# Data2 = eval(input('enter the data2: '))
# if len(Data1) == len(Data2):
#     print('both have the same length')
# else:
#     raise Exception

## Create the function take mail_id as arg, check if the mail_id has "@" in it and endswith ".com"
## if both condition satisfied print mail_id else raise the error

def get_email(mail_id):
    if '@' in mail_id and mail_id.endswith(".com"):
        print(mail_id)
    else:
        raise Exception

# get_email("Akshata@.com")
#########################################################################################

## User Defined Exception Handling: It helps to create our own error based on the requirement

## syntax:

# class Errorname(Exception):
#     pass

class WithdrawLimit(Exception):
    pass

def withdraw(amount):
    if amount < 5000:
        print('Withdrawn Successfully')
    else:
        raise WithdrawLimit('The maximum withdraw limit is 5k')
# withdraw(30000)

## Create the function which takes username and password as args
## if username == 'abc_123'  and password == '123_abc' print "logged in" else raise your own error

class LoginError(Exception):
    pass

def Login(username, password):
    if username == 'abc_123' and password == '123_abc':
        print('Logged In')
    else:
        raise LoginError
# Login('abc_123', '123_abc')

## Create the function which takes number of questions as arg
## if number of questions are less than or equal to 25 print "i will do it" else raise your own error

class MoreQuestions(Exception):
    pass

def get_ans(no_of_ques):
    if no_of_ques<=25:
        print("i will do it")
    else:
        raise MoreQuestions

# get_ans(10)








