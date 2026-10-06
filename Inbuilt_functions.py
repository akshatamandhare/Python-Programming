
## enumerate(): it is an inbuilt function, which helps to get numbering to each element of the collection

string = 'hello'
for index in range(len(string)):
    print(index, string[index])

##or

for item in enumerate(string):
    print(item)

##or

for index, char in enumerate(string):
    print(index, char)

##or 

for index, char in enumerate(string, start = 100000000000000000000000000000000):
    print(index, char)

## TAKE LIST OF STRING, GET THE STRING PRESENT AT ODD POSITION USING ENUMERATE
list_ = ['apple', 'google', 'amazon', 'youtube', 'insta', 'yahoo']
for index, string in enumerate(list_):
    if index % 2 != 0:
        print(index, string)

## TAKE LIST OF STRING, GET THE STRING PRESENT AT EVEN POSITION
# AND STRING SHOULD START WITH VOWEL
list_ = ['apple', 'google', 'Amazon', 'youtube', 'insta', 'yahoo']
for index, string in enumerate(list_):
    if index % 2 == 0 and string[0] in 'aeiouAEIOU':
        print(index, string)

## WAP TO PRINT THE SUM OF ALL THE NUMBERS PRESENT AT ODD INDEX 
# IF THE NUMBER IS EVEN
# num = '123457' ==> 2 + 4 ==> 6
num = '123457'
sum=0
for index, item in enumerate(num):
    if(int(item)%2==0 and index%2!=0):
        sum+=int(item)
print(sum)

#######################################################################################

## zip(): It is an inbuilt function, which helps to iterate over the multiple collections at the same time
## The disadvantage of zip() is it always stops at least length collection

List1 = [1,2,3]
List2 = [4,5,6]
for item in zip(List1, List2):
    print(item)
#
# ##or
#
for num1, num2 in zip(List1, List2):
    print(num1, num2)

List1 = [1,2,3]
Tuple1 = (4,5,6)
string= 'hai'
for num1, num2, char in zip(List1, Tuple1, string):
    print(num1, num2, char)

##or

List1 = [1,2,3,4,5,6,7,8,9]
Tuple1 = (4,5,6,7,8,9)
string= 'hai'
for num1, num2, char in zip(List1, Tuple1, string):
    print(num1, num2, char)

## WAP TO GET THE FOLLOWING OUTPUT
LIST1 = [1,2,3,4]
LIST2 = [5,6,7,8]
# OUT = [5,12,21,32]

out = []
for num1, num2 in zip(LIST1, LIST2):
    out.append(num1 * num2)
print(out)

#. WAP TO CREATE THE DICTIONARY BY USING GIVEN LIST
list_ = ['youtube', 'gmail','YAHOO', 'email', 'facebook', 'whatsapp', 'instagram']
_list = [1,2,3,5]

out = {}
for string, num in zip(list_, _list):
    out[string] = num
print(out)

################################################################################

## zip_longest()

from itertools import zip_longest

List1 = [1,2,3,4,5,6,7,8,9]
Tuple1 = (4,5,6,7,8,9)
string = 'hai'
for num1, num2, char in zip_longest(List1, Tuple1, string):
    print(num1, num2, char)

##or

for num1, num2, char in zip_longest(List1, Tuple1, string, fillvalue = 'no pair found'):
    print(num1, num2, char)

##or

for num1, num2, char in zip_longest(List1, Tuple1, string, fillvalue = 0):
    print(num1, num2, char)

#. WAP TO CREATE THE DICTIONARY BY USING GIVEN LIST
list_ = ['youtube', 'gmail','YAHOO', 'email', 'facebook', 'whatsapp', 'instagram']
_list = [1,2,3,5]

out = {}
for string, num in zip_longest(list_, _list):
    out[string] = num
print(out)

#####################################################################################

## defaultdict()

string = 'aaaabbaa'         ## out = {'a':6, 'b':2}

out = {}
for char in string:
    if char not in out:
        out[char] = 1
    else:
        out[char] += 1
print(out)

##or

from collections import defaultdict
string = 'aaaabbaa'
out = defaultdict(int)
for char in string:
    out[char] += 1
print(out)

##. Counting occurrences of items which starts with consonants
items = ['apple', 'banana', 'banana', 'orange', 'grape', 'apple', 'apple', 'banana', 'orange']
# out = {'banana': 3, 'grape': 1}

out = defaultdict(int)
for item in items:
    if item[0] not in 'aeiouAEIOU':
        out[item] += 1
print(out)

## Storing indices of items using enumerate()
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# out = {'apple': (0, 2, 5), 'banana': (1, 4), 'orange': (3,)}

out = defaultdict(tuple)
for index, string in enumerate(items):
    out[string] += (index, )
print(out)

## Categorizing numbers as even or odd
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# out = {'odd': {1, 3, 5, 7, 9}, 'even': {8, 2, 4, 6}}

out = defaultdict(set)
for index, num in enumerate(numbers):
    if num%2!=0:
        out["odd"].add(num)
    else:
        out["even"].add(num)
print(out)
