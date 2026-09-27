
## "else" is a keyword. The control get TSB only when the condition get satisfied it not
## it executes the FSB

## syntax:

# if condition:
#     TSB
# else:
#     FSB

## wap to check the given number is odd or even

# number = int(input('enter the number: '))
# if number % 2 != 0:
#     print('The given number is odd')
# else:
#     print('The given number is even')

## wap to check the two variables having positive integer value are pointing to same address or not

# num1 = int(input('enter the num1: '))
# num2 = int(input('enter the num2: '))
# if id(num1) == id(num2):
#     print('The two variables having positive integer value are pointing to same address')
# else:
#     print('The two variables having positive integer value are not pointing to same address')

##or

# num1 = int(input('enter the num1: '))
# num2 = int(input('enter the num2: '))
# if num1 is num2:
#     print('The two variables having positive integer value are pointing to same address')
# else:
#     print('The two variables having positive integer value are not pointing to same address')

## wap to check the first element of list is string or not

# List = eval(input('enter the list: '))
# if type(List[0]) == str:
#     print('The first element of list is string')
# else:
#     print('The first element of list is not string')

## wap to check the given string having a middle character or not

# string = input('enter the string: ')
# if len(string) % 2 != 0:
#     print('The given string having a middle character')
# else:
#     print('The given string not having a middle character')

## wap to check the first character in the string is uppercase or not,
# if uppercase get the reversed string else get the string as is

# string = input('enter the string: ')
# if string[0].isupper():
#     print(string[::-1])
# else:
#     print(string)

## wap to check the square of the integer number is even or odd,
# if even print 'hii' else print 'hello'

# number = int(input('enter the number: '))
# if (number ** 2) % 2 == 0:
#     print('Hii')
# else:
#     print("Hello")

##  wap to check the last digit of the integer number is divisible by 3 or not

# number = int(input('enter the number: '))
# if (number % 10) % 3 == 0:
#     print('The last digit of the integer number is divisible by 3')
# else:
#     print('The last digit of the integer number is not divisible by 3')

##or

# number = int(input('enter the number: '))
# if int(str(number)[-1]) % 3 == 0:
#     print('The last digit of the integer number is divisible by 3')
# else:
#     print('The last digit of the integer number is not divisible by 3')

## wap to check two variables having  positive integer value are pointing to different address or not
# x, y = int(input("Enter x: ")), int(input("Enter y: "))
# if(id(x) == id(y)):
#     print("Same id")
# else:
#     print("Different id")

# or

# x, y = int(input("Enter x: ")), int(input("Enter y: "))
# if(x is y):
#     print("Same id")
# else:
#     print("Different id")


## wap to check the given data is collection type or not
# data = eval(input("Enter data: "))

# print(type(data))

# if isinstance(data, (list, tuple, set, dict, str)):
#     print("Data is of collection type!!")
# else:
#     print("Data is not collection type!!")


