
## The control statement helps to control the flow of execution in 2 ways

##1. based on some conditions/decisions
##2. when we want to execute the same set of instructions n number of times

## There are 2 types of control statement

##1. Conditional/Decisional statement
##2. Looping statement

############################################################################################

##1. Conditional/Decisional statement: It helps to control the flow of execution based on some conditions or decisions

## There are 4 types

##1. if condition
##2. else condition
##3. elif condition
##4. nested if condition

############################################################################################

##1. if condition: "if" is a keyword. The control returns true statement block only when the
## condition get satisfied if not it just ignores

## syntax:

# if condition:
#     TSB

## wap to check the given integer number is greater than 15

# number = int(input('enter the number: '))
# if number > 15:
#     print('The given integer number is greater than 15')

## WAP TO CHECK THE GIVEN INTEGER NUMBER IS EVEN

# number = int(input('enter the number: '))
# if number % 2 == 0:
#     print('THE GIVEN INTEGER NUMBER IS EVEN')

## wap to check the string is having exactly 5 characters

# string = input('enter the string: ')
# if len(string) == 5:
#     print('The string is having exactly 5 characters')

## wap to check the given data is integer

# Data = eval(input('enter the data: '))
# if type(Data) == int:
#     print('The given data is integer')

## wap to check the given character is uppercase

# char = input('enter the character: ')
# if char.isupper():
#     print('The given character is uppercase')

## wap to check the given string is having even number of characters

# string = input('enter the string: ')
# if len(string) % 2 == 0:
#     print('The given string is having even number of characters')

## wap to check the given string starts with vowel character

# string = input('enter the string: ')
# if string[0] in 'aeiouAEIOU':
#     print('The given string starts with vowel character')

##or

# string = input('enter the string: ')
# if string.startswith(('a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')):
#     print('The given string starts with vowel character')

## wap to check the given number is divisible by 3 and multiple of 5

# number = int(input('enter the number: '))
# if number % 3 == 0 and number % 5 == 0:
#     print('The given number is divisible by 3 and multiple of 5')

## wap to check the given data is single value datatype

# Data = eval(input('enter the data: '))
# if type(Data) == int or type(Data) == float or type(Data) == complex or type(Data) == bool:
#     print('The given data is single value datatype')

##or

# Data = eval(input('enter the data: '))
# if type(Data) in [int, float, complex, bool]:
#     print('The given data is single value datatype')

## wap to check the given character is a lowercase

# char = input('enter the character: ')
# if char.islower():
#     print('The given character is a lowercase')

## wap to check the given character is a digit

# char = input('enter the character: ')
# if char.isdigit():
#     print('The given character is a digit')

## wap to check the given string having odd number of character

# string = input('enter the string: ')
# if len(string) % 2 != 0:
#     print('The given string having odd number of character')

## wap to check the given integer number is positive

# number = int(input('enter the number: '))
# if number > 0:
#     print('The given integer number is positive')

## wap to check the given data is string

# Data = eval(input('enter the data: '))
# if type(Data) == str:
#     print('The given data is string')

## wap to check the given data is dictionary

# Data = eval(input('enter the data: '))
# if type(Data) == dict:
#     print('The given data is string')




