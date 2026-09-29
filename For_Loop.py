
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













