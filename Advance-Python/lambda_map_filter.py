
# lambda: It is a keyword, it is the shortest form of writing the function

## syntax:

# var = lambda args: expression
# print(var(values))

## Add 10 to the given number

Add_10 = lambda number: number + 10
# print(Add_10(10))

## WAP TO GET THE SQUARE AND CUBE OF THE GIVEN NUMBER
Sqr_Cube = lambda number:(number ** 2, number ** 3)
# print(Sqr_Cube(2))

## WAP TO GET THE LAST CHARACTER OF THE STRING
get_last_char = lambda string: string[-1]
# print(get_last_char('hello'))

## WAP TO CHECK THE STRING IS PALINDROME OR NOT
check_for_palindrome = lambda string: string == string[::-1]
# print(check_for_palindrome('Python'))           ## 'Python' == 'nohtyP'
# print(check_for_palindrome('mom'))              ## 'mom' == 'mom'

## WAP TO CHECK THE CHARACTER PRESENT IN STRING OR NOT
check_for_char = lambda string, char: char in string
# print(check_for_char('Python', 'p'))        ## "p" in "Python"
# print(check_for_char('Python', 'P'))        ## "P" in "Python"

## WAP TO RETURN LAST n ELEMENT FROM THE COLLECTION

## 'python', 2 ==> 'on'
## [1,2,3,4,5,6,7,9], 4 ==> [5,6,7,9]

## syntax of lambda exp when we have condition to check
# var = lambda args:TSB if condition else FSB
# print(var(values))

## WAP TO PRINT THE ASCII VALUE OF THE CHARACTER IF IS LOWERCASE
# ELSE GET THE REVERSE OF THE ASCII VALUE

get_ascii_value = lambda char:ord(char) if char.islower() else int(str(ord(char))[::-1])
# print(get_ascii_value('a'))
# print(get_ascii_value('A'))

## ord("A") ==> 65 ==> str(65) ==> '65' ==> '65'[::-1] ==> '56' ==> int('56') ==> 56

## WAP TO CHECK THE GIVEN STRING IS KEYWORD OR NOT

import keyword
check_for_keyword = lambda string:"Keyword" if string in keyword.kwlist else "Not Keyword"
# print(check_for_keyword('range'))
# print(check_for_keyword('if'))

## WAP TO GET THE SQUARE OF LENGTH IF THE COLLECTION IS HAVING EVEN LENGTH ELSE GET THE CUBE

check_for_len = lambda collection:len(collection) ** 2 if len(collection) % 2 == 0 else len(collection) ** 3
# print(check_for_len('hii'))
# print(check_for_len([1,2,3,4]))

## WAP TO CHECK THE GIVEN NUMBER IS EVEN OR NOT

####################################################################################

## map(): It is an inbuilt function, which helps to execute the same set of instructions to each and every element of the collection

## syntax:

# var = map(fname, collections)
# print(list(var))

# map stores value as address so that use container to access the value  

## WAP TO SQUARE AND CUBE EACH AND EVERY ELEMENT IN THE GIVEN LIST
# list_ = [1,2,3,4] ===> out = [[1, 1], [4, 8], [9, 27], [16, 64]]

def get_square_cube(list_):
    out = []
    for num in list_:
        out.append([num ** 2, num ** 3])
    return out
# print(get_square_cube([1,2,3,4]))

##or

sqr_cube = lambda num: [num ** 2, num ** 3]
res = map(sqr_cube, [1,2,3,4])
# print(list(res))

##or

# print(list(map(lambda num: [num ** 2, num ** 3], [1,2,3,4])))

# WAP TO GET THE FOLLOWING OUTPUT
list_ = [56, 8.7, [1,2,4], 'helloo', 9-9j, [1,2,3,4]]
# out = [1, 1, 3, 6, 1, 4]
# print(list(map(lambda data:1 if type(data) in [int, float, complex, bool] else len(data), list_)))

##WAP TO GET THE FOLLOWING OUTPUT
string = 'hii hello how are you'
# out = [3, 5, 3, 3, 3]
# print(list(map(lambda word:len(word), string.split())))

# Add two lists element-wise using zip()
a = [1, 2, 3]
b = [4, 5, 6]
# print(list(map(lambda item: item[0] + item[1], zip(a, b))))

## Prefix each item with its index using enumerate
items = ['apple', 'banana', 'cherry']            
## out = {0: 'apple', 1: 'banana', 2: 'cherry'}
# print(dict(map(lambda item: (item[0], item[1]), enumerate(items))))

## Strip whitespace from strings
raw_strings = ['  apple  ', ' banana ', 'cherry  ']    
## out =  ['apple', 'banana', 'cherry']
# print(list(map(lambda string: string.strip(), raw_strings)))

#Convert list of strings to integers
list_ = ['1', '2', '34', '4567', '56789']
# print(lsit(map(lambda data : int(data), list_)))

####################################################################################

## filter(): It is an inbuilt function, which helps to filter the particular data item from the collection

## syntax:

# var = filter(fname, collection)
# print(list(var))

## WAP TO EXTRACT ALL THE STRINGS FROM THE TUPLE
print(list(filter(lambda data: type(data)==str, (10, 20, 'hii'))))

## WAP TO EXTRACT ALL THE INTEGER NUMBER FROM THE COLLECTION ONLY IF THE NUMBER HAVING 3 DIGITS
print(list(filter(lambda data: type(data)==int and len(str(data))==3 , (10, 123, 'hii'))))

## WAP TO GET ALL THE PALINDROME NUMBERS IN THE RANGE 10 TO 100
print(list(filter(lambda data: str(data)==str(data)[::-1], range(10, 100))))

## TAKE A LIST OF STRING INPUT, CREATE A NEW LIST WHICH CONSISTS OF ONLY THE EVEN LENGTH STRING
print(list(filter(lambda data: len(data)%2==0, ['apple', 'banana', 'cherry' ])))

## Filter strings that are all lowercase.
list_ = ['hello', 'WORLD', 'PYTHON']
print(list(filter(lambda data: data.isupper(), list_)))

## Filter strings that start with a vowel. 
list_ =['apple', 'banana', 'orange']
print(list(filter(lambda data: data[0].lower() in 'aeiou', list_)))

# people older than 18
people = [{'name': 'Tom', 'age':17}, {'name':'Anna', 'age':21}]
print(list(filter(lambda data: data['age']>18, people)))

## Filter Valid phone numbers (10 digits)
numbers = ['1234567890', '98765', '123456789a']
print(list(filter(lambda data: len(str(data))==10 , numbers)))

## Filter Movies rated > 8
movies = [{'title': 'Inception', 'rating': 8.8}, {'title': 'Cats', 'rating': 4.2}]
print(list(filter(lambda data: data['rating']>8, movies)))