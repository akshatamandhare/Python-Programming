
## Whenever we want to check multiple conditions we use elif condition

## syntax:

# if condition1:
#     TSB1
# elif condition2:
#     TSB2
# elif condition3:
#     TSB3
#
# else:
#     FSB         ## else is optional

## wap to check the relationship between two integer number

# num1 = int(input('enter the num1: '))
# num2 = int(input('enter the num2: '))
# if num1 == num2:
#     print('Both numbers are equal')
# elif num1 > num2:
#     print('num1 is greater')
# elif num1 < num2:
#     print('num2 is greater')

##or

# num1 = int(input('enter the num1: '))
# num2 = int(input('enter the num2: '))
# if num1 == num2:
#     print('Both numbers are equal')
# elif num1 > num2:
#     print('num1 is greater')
# else:
#     print('num2 is greater')

## wap to check the given character is uppercase or lowercase or number or special character

# char = input('enter the character: ')
# if char.isupper():
#     print('The given character is uppercase')
# elif char.islower():
#     print('The given character is lowercase')
# elif char.isdigit():
#     print('The given character is digit')
# else:
#     print('The given character is special')

## wap to check the positive integer number is having exactly single or
# double or triple digit or more than 3 digit

# number = int(input('enter the number: '))
# if len(str(number)) == 1:
#     print('The positive integer number is having exactly single digit')
# elif len(str(number)) == 2:
#     print('The positive integer number is having exactly double digit')
# elif len(str(number)) == 3:
#     print('The positive integer number is having exactly triple digit')
# else:
#     print('The positive integer number is having more than three digit')

##or

# number = int(input('enter the number: '))
# if 0 <= number <= 9:
#     print('The positive integer number is having exactly single digit')
# elif 10 <= number <= 99:
#     print('The positive integer number is having exactly double digit')
# elif 100 <= number <= 999:
#     print('The positive integer number is having exactly triple digit')
# else:
#     print('The positive integer number is having more than three digit')

## take a string input,
##1. if the string having exactly 5 character print the given input
##2. if the string having less than 5 character print reverse string
##3. if the string having more than 5 character print alternate characters

# string = input('enter the string: ')
# if len(string) == 5:
#     print(string)
# elif len(string) < 5:
#     print(string[::-1])
# else:
#     print(string[::2])

## take an integer input,
##1. if given number is divisible by 3 print 'hii'
##2. if given number is divisible by 5 print 'bye'
##3. if given number is divisible by 3 and also 5 print 'hiibye'

# number = int(input('enter the number: '))
# if number % 3 == 0 and number % 5 == 0:
#     print('HiBye')
# elif number % 3 == 0:
#     print('Hii')
# elif number % 5 == 0:
#     print('Bye')

## wap to check the greater among 3 integer number
## wap to check the given character is alphabet or number or special












