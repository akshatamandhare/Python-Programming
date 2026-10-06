
## break: It is a keyword, ASA the control encounter the "break" keyword it will come out
## of the loop and never go back to the same loop

## Guessing the number game

# Number = int(input('enter the number: '))
#
# while True:
#     Guess_Number = int(input('Guess the number: '))
#     if Number == Guess_Number:
#         print('Congrats you won the game')
#         break
#     elif Number > Guess_Number:
#         print('sorry, you guessed smaller number try again!!')
#     else:
#         print('sorry, you guessed larger number try again!!')

## WAP TO CHECK THE GIVEN TUPLE IS HOMOGENOUS OR NOT

# Tuple = eval(input('enter the tuple: '))
# for element in Tuple:
#     if type(Tuple[0]) != type(element):
#         print('The given tuple is not homogenous')
#         break
# else:
#     print('The tuple is homogeneous')

##WAP TO PRINT THE INITIAL INDEX OF THE GIVEN CHARACTER
STRING = 'INITIAL'
CHAR = 'I'
# out: index - 0

# for index in range(len(STRING)):
#     if STRING[index] == CHAR:
#         print(index, STRING[index])
#         break

#######################################################################################

## continue: it is a keyword, ASA the control encounter "continue" keyword it skips the current execution
## and go back to the same loop

#1. WAP TO GET THE FOLLOWING OUTPUT
string = 'hello hiii how are youu'
# # out = ['olleh', 'woh', 'era']

# out = []
# for word in string.split():
#     if len(word) % 2 == 0:
#         continue
#     else:
#         out.append(word[::-1])
# print(out)

## WAP TO EXTRACT ALL THE COMPLEX NUMBERS FROM THE GIVEN SET COLLECTION
Set = {12, 4-8j, 67-8j, 5.4, 'py'}
# out = {4-8j, 67-8j}

# out = set()
# for element in Set:
#     if type(element) != complex:
#         continue
#     else:
#         out.add(element)
# print(out)

## Wap to extract all the character from the string except the uppercase vowel
# string = 'Apple' ==> out = 'pple'

# string = input('enter the string: ')
# new_string = ''
# for char in string:
#     if char in 'AEIOU':
#         continue
#     else:
#         new_string += char
# print(new_string)

#################################################################################

## pass: It is a keyword, it helps to make the empty statement block valid

# for num in range(1, 10):
#     pass
#
# for num in range(1, 10):
#     if num % 2 == 0:
#         pass
#




