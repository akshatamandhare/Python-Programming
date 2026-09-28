
## It helps to execute the same set of instructions for n number of times
## It executes till the condition become False

## syntax:

# initialization
# while condition:
#     TSB
#     updation

# i = 1
# while i <= 3:
#     print('hi')
#     i += 1      ## i = i + 1

## WAP TO PRINT N NATURAL NUMBERS

# number = int(input('enter the number: '))
# i = 1
# while i <=number:
#     print(i)
#     i += 1

## Print multiplication table of a number

# number = int(input('enter the number: '))
# i = 1
# while i <= 10:
#     print(f'{number} X {i} = {number * i}')
#     i += 1

## WAP TO PRINT "N NATURAL" NUMBERS WHICH ARE DIVISIBLE BY 3

# number = int(input('enter the number: '))
# i = 1
# while i <= number:
#     if i % 3 == 0:
#         print(i)
#     i += 1

## WAP TO EXTRACT ALL THE LOWERCASE CHARACTER FROM THE GIVEN STRING
## input = 'A1b2c#' ==> output = 'bc'

# string = input('enter the string: ')
# new_string = ''
# i = 0
# while i < len(string):
#     if string[i].islower():
#         new_string += string[i]
#     i += 1
# print(new_string)

# '' + 'b' ==> 'b'
# 'b' + 'c' ==> 'bc'

## WAP TO EXTRACT ONLY THE INTEGER FROM THE LIST COLLECTION
## List = [1, 3.4, 3, 'hii', 8-9j] ===> out = [1, 3]

# List = eval(input('enter the list: '))
# new_list = []
# i = 0
# while i < len(List):
#     if type(List[i]) == int:
#         new_list += [List[i]]
#     i += 1
# print(new_list)

# [] + [1] ==> [1]
# [1] + [3] ==> [1,3]

##or

# List = eval(input('enter the list: '))
# new_list = []
# i = 0
# while i < len(List):
#     if type(List[i]) == int:
#         new_list.append(List[i])
#     i += 1
# print(new_list)

## WAP TO REMOVE THE DUPLICATE VALUES FROM THE LIST WITHOUT TYPECASTING
# NAMES = ['apple', 'google', 'apple', 'apple', 'insta']
# out = ['apple', 'google', 'insta']

# List = eval(input('enter the list: '))
# out = []
# i = 0
# while i < len(List):
#     if List[i] not in out:
#         out.append(List[i])
#     i += 1
# print(out)

## WAP TO EXTRACT ALL THE FLOAT FROM THE TUPLE COLLECTION
## Tuple = (1, 3.4, 5.3, 'hii', 8-9j) ==> out = (3.4, 5.3)

# Tuple = eval(input('enter the tuple: '))
# new_tuple = ()
# i = 0
# while i < len(Tuple):
#     if type(Tuple[i]) == float:
#         new_tuple += (Tuple[i],)
#     i += 1
# print(new_tuple)

# () + (3.4,) ==> (3.4,)
# (3.4,) + (5.3,) ==> (3.4,5.3)

## TAKE A STRING INPUT, EXTRACT ALL THE UPPERCASE, LOWERCASE, DIGITS AND SPECIAL CHARACTER IN 4 DIFFERENT VARIABLE
## String = 'A1b&2C3*D41'
## upper = 'ACD'  lower = 'b' Digit = '123'  special = '&*'

# string = input('enter the string: ')
# upper, lower, digit, special = '', '', '', ''
# i = 0
# while i < len(string):
#     if string[i].isupper():
#         upper += string[i]
#     elif string[i].islower():
#         lower += string[i]
#     elif string[i].isdigit():
#         digit += string[i]
#     else:
#         special += string[i]
#     i += 1
# print(upper, lower, digit, special)

# Write a program to convert all the lower case character to upper case
# characters present in a given string
# string = 'aBcD123' ==> out = 'ABCD123'
# string = input("Enter string: ")
# i=0
# out=[]
# while(i<len(string)):
#     if(string[i].islower()):
#         out+=string[i].upper()
#     else:
#         out+=string[i]
#     i+=1
# print(out)

# Write a program to convert all the lower case character to upper case
# character and upper case character to lower case character by keeping number
# and special character as it is

# string = 'aBcD123' ==> out =  'AbCd123'
# string = input("Enter string: ")
# i=0
# out=[]
# while(i<len(string)):
#     if(string[i].islower()):
#         out+=string[i].upper()
#     elif(string[i].isupper()):
#         out+=string[i].lower()
#     else:
#         out+=string[i]
#     i+=1
# print(out)

# or

# string = input("Enter string: ")
# i=0
# out=[]
# while(i<len(string)):
#     out+=string[i].swapcase()
#     i+=1
# print(out)

## Write a program to return the positions of vowels present in the given string
# string = 'aBcDEf123' #==> 0, 4
# i=0
# while(i<len(string)):
#     if(string[i].lower() in 'aueiouAEIOU'):
#         print(i, string[i])
#     i+=1

#WAP to extraact all the int numbers from the tuple only if the numbers present at odd index position
# tuple = (10, 20, 30, 40, 50, "akshata", 'good')
# i=0
# new_tuple=[]
# while(i<len(tuple)):
#     if(i%2!=0 and type(tuple[i])==int):
#         new_tuple += (tuple[i],)
#     i+=2
# print(new_tuple)

#string is palinedrom or not without sclicing
# string = input("enter string: ")
# i=0
# reverse_string = ''
# while(i<len(string)):
#     reverse_string = reverse_string + string[i] 
#     i+=1

# if(string == reverse_string):
#     print("String Palindrom")
# else:
#     print("String not palindrom")



## WAP to separate the positive and negative integer number present in list 
# l = [1,2,3,-5,-6,-7] 

# positive_list = []
# negative_list = []

# i = 0

# while i < len(l):
#     if l[i] > 0:
#         positive_list.append(l[i])
#     elif l[i] < 0:
#         negative_list.append(l[i])
#     i += 1
# print("positive_list: ",positive_list, "negative_list: ", negative_list)

# print("Positive numbers:", positive_list)
# print("Negative numbers:", negative_list)

#int sum cube
# string =(input("Enter Sring: "))
# i=0
# sum =0
# while(i<len(string)):
#     if(string[i].isdigit()):
#         sum+=int(string[i])**3
#     i+=1
# print("SUM: ", sum)

# string = input("Enter String: ")
# i=0
# count, vowels, consonents = 0, 0, 0

#count digit, vowels, and cons count
#  while(i<len(string)):
#     if(string[i].isdigit()):
#         count+=1
#     if(string[i].lower() in 'aeiou' ):
#         vowels+=1
#     if(string[i].lower() not in 'aeiou' ):
#         consonents+=1
#     i+=1
# print(count, vowels, consonents)

# Write a program to get the following output # input='abcd' 
# # output={‘a’:97,’b’:98,’c’:99,’d’:100} 

# string = input("Enter String: ")
# i=0
# dict ={}
# while(i<len(string)):
#     dict[string[i]] = ord(string[i])
#     i+=1
# print(dict)

#print all the divisor of number
# number = int(input("enter number: "))
# i=1
# while(i<=number):
#     if(number%i==0):
#         print(i)
#     i+=1

# Find the sum of elements in a list
# l = [10, 20, 30, 40, 50]
# i=0
# sum=0
# while(i<len(l)):
#     sum+=l[i]
#     i+=1
# print(sum)


# Count positive, negative and zero values
# l = [10, -5, 0, 20, -8, 0, 15]
# positive, negative, zero = 0, 0, 0
# i=0
# while(i<len(l)):
#     if(l[i]<0):
#         negative+=1
#     elif(l[i]>0):
#         positive+=1
#     elif(l[i]==0):
#         zero+=1
#     i+=1
# print("positive: ", positive,"\nNegative: ", negative, "\nZeros: ",zero);










