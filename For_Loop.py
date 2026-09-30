
## It helps to execute the same set of instructions number of times
## It moves all the way up to length of the collection

## syntax:

# for variable in collections:
#     TSB

## range(): It is an inbuilt function which helps to get the sequence of numbers in the given limit
## syntax: range(start_value, end_value+/-, updation)
## It always includes the start value and excludes the end value
## The default value of strat is 0 and default value of updation is 1
## It always gets the integer output

## Print the number from 0 to 10
# print(list(range(0, 11, 1)))
# print(tuple(range(11)))

## Print the alternate number from 0 to 20
# print(list(range(0, 21, 2)))

## Print the number from 10 to 0
# print(list(range(10, -1, -1)))

## Take the string and get character and index position

# string = 'hi'
# for index in range(len(string)):
#     print(index, string[index])

## WAP TO EXTRACT ALL THE DIGITS FROM THE GIVEN STRING

# string = input('enter the string: ')
# new_string = ''
# for char in string:
#     if char.isdigit():
#         new_string += char
# print(new_string)

##or

# string = input('enter the string: ')
# new_string = ''
# for index in range(len(string)):
#     if string[index].isdigit():
#         new_string += string[index]
# print(new_string)

## Note: The range() can be used in all the program, but it is enough to use only when the
## question is related to the index position

## wap to replace all the space in the given string with underscore using for loop(without using attribute)
## string = 'hello hii good morning'
## out = 'hello_hii_good_morning'

# string = input('enter the string: ')
# new_string = ''
# for char in string:
#     if char == ' ':
#         new_string += '_'
#     else:
#         new_string += char
# print(new_string)

## wap extract all the single value data item from the list
# only if the element at even index position

# List = eval(input('enter the list: '))
# new_list = []
# for index in range(len(List)):
#     if index % 2 == 0 and type(List[index]) in [int, float, complex, bool]:
#         new_list.append(List[index])
# print(new_list)

##or

# List = eval(input('enter the list: '))
# new_list = []
# for index in range(0,len(List),2):
#     if type(List[index]) in [int, float, complex, bool]:
#         new_list.append(List[index])
# print(new_list)

## wap to extract a string starting with vowel character
# list_ = ['Apple' , 'Google' , 'amazon', 'instagram', 'gmail', 'Extract']
# out = []
# for string in list_:
#     if string[0] in 'aeiouAEUIO':
#         out.append(string)
# print(out)

## wap to get the following output
# string = 'aaaabbbbbbccd'
##out: 'a4b6c2d1'

# char_count = ''
# for char in string:
#     if char not in char_count:
#         char_count += char + str(string.count(char))
# print(char_count)

# '' + 'a' + '4' ==> 'a4'
# 'a4' + 'b' + '6' ==> 'a4b6'

## wap to get the following output
# string = 'aaaabbbbbbccd'
## output: {'a':4 , 'b':6 , 'c':2 , 'd':1}

# char_count = {}
# for char in string:
#     char_count[char] = string.count(char)
# print(char_count)

##or

# char_count = {}
# for char in string:
#     if char not in char_count:
#         char_count[char] = 1
#     else:
#         char_count[char] += 1
# print(char_count)

## wap to extract all the non default  values from a list.
# List = [12, 0, 0.0, 'hii', []]   ===>  out = [12, 'hii']

# List = eval(input('enter the list: '))
# out = []
# for element in List:
#     if bool(element) == True:
#         out.append(element)
# print(out)

## wap to get the following output # 
# string = 'hello good evening' 
# ##output: {'hello':5 , 'good':4 , 'evening' : 7} 

# print('hello good evening'.split())
# word_length = {}
# for word in string.split():
#     word_length[word]=len(word)
# print(word_length)

## wap to get the following output # 
# string = 'python java web selenium SQL manual C++ jscript' 
# ##output: {'python':6 , 'java':4, 'selenium': 8, 'manual':6 }

# even_word_length = {}
# for word in string.split():
#     if(len(word)%2==0):
#         even_word_length[word]=len(word)
# print(even_word_length)


## wap to get the following output # 
# list_ = ['python.py', 'google.com', 'yahoo.in', 'file.txt' , 'file.csv'] 
##output:['py', 'com', 'in', 'txt' , 'csv']

# print(list_.split('.'))

# out = []
# for char in list_:
#     reg = char.split('.')
#     out.append(reg[1])
# print(out)


## wap to count the number of occurrence of the specified character 
# in the given string without using the attribute
# string = 'occurrence' 
# character = 'c' ## out = 3
# count = 0
# for char in string:
#     if(char==character):
#         count+=1
# print(count)


## wap to replace the old character with new character without using the attribute 
# string = 'occurrence' 
# old_char = 'c' 
# new_char = 'C' 
# ## out = 'oCCurrenCe

# new_string = ''
# for char in string:
#     if(char==old_char):
#         new_string += new_char
#     else:
#         new_string+=char
# print(new_string)

## wap to get the following output # 
# l = [1,2,3,-5,'hello','hii' ,-4] 
# #o:[1,2,3,5,4]
# out = []
# for element in l:
#     if(type(element)==int):
#         if(element<0):
#             out.append(-(element))
#         else:
#             out.append(element)
# print(out)

# or 
# out = []
# for element in l:
#     if(type(element)==int):
#         out.append(abs(element))
# print(out)

# wap to get the following output. # 
# In='hello'
#  Out={0:’h’,1:’e’,2:’l’,3:’l’,4:’e’}
# out = {}
# index=0
# for char in In:
#     out[index] = char
#     index+=1
# print(out)

# for index in range(len(In)):
#     out[index]=In[index]
# print(out)

# Wap to get the following output. 
# In='127342' # Out=’242173’ 
# out = ''
# out_last=''
# for i in In:
#     char = int(i)
#     if(char%2==0):
#         out+=i
#     else:
#         out_last+=i
# print(out+out_last)

## WAP to Print All Divisors of a Number ##6 ==> 1, 2, 3, 6

# number = int(input("Enter Number: "))
# for i in range(1, number+1):
#     if(number%i==0):
#         print(i)
    

# Wap to extract all the string values present in list only if the string is palindrome.
# List = [23, 3.4, 'hii', 'mom', '121']
# # out = ['mom', '121']

# out =[]
# for char in List:
#     if(type(char)==str ):
#         if(char == char[::-1]):
#             out.append(char)
# print(out)


## wap to get the following output
# list_ = ['python.py', 'google.com', 'yahoo.in', 'file.txt' , 'file1.csv']
# # out = {'python': 'py', 'google':'com', 'yahoo':'in', 'file':'txt', 'file1':'csv'}

# out ={}
# for char in list_:
#     reg = char.split('.')
#     out[reg[0]] = reg[1]
# print(out)

## wap to get the following output
# string = 'python java web selenium SQL manual C++ jscript'
# ##output: {'python':6 , 'java':4 , 'web':'bew', 'selenium': 8 , 'SQL':'LQS' , 'manual':6 , 'C++':'++c', 'jscript':'tpircsj'}

# out = {}
# for element in string.split(' '):
#     if(len(element)%2!=0):
#         out[element] = element[::-1]
#     else:
#         out[element] = len(element)
# print(out)

## wap to get the following output
# string = 'hello good evening'
# ##output: {'hello':'olleh' , 'good':'doog' , 'evening' : 'gnineve'}

# out = {}
# for element in string.split(' '):
#     out[element]=element[::-1]
# print(out)

## wap to get the following output
# string = 'hello good evening'
##output: {'hello':'ho' , 'good':'gd' , 'evening' : 'eg'}

# out = {}

# for element in string.split(' '):
#     new_str =''
#     new_str += element[0]
#     new_str += element[-1]
#     out[element]= new_str
# print(out)
















