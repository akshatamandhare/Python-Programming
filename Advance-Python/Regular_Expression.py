
## It helps to fetch the particular data item from the collection/file

## syntax:

# import re
# var = re.findall('pattern', 'string')         # findall() it helps to get all the matching records in the list form
# print(var)

##########################################################################################

import re
res = re.findall('the','the theory of relativity')
print(res)
print(re.findall('cat','the dragging belly indicates your cat is too fat'))
print(re.findall('python','python and java are object oriented'))
print(re.findall('Python','python and java are object oriented'))
print(re.findall('Python','python/Python and java are object oriented'))
print(re.findall('Smith','smith and blackSmith'))

##########################################################################################

## character set: It helps to match one in many character

print(re.findall('[Ss]mith','smith and blackSmith'))

print(re.findall('[pP]ython','python/Python and java are object oriented'))

## match grey and gray
print(re.findall('gr[ea]y','match grey and gray'))

## match any one in vowel (either a, e, i, o, u)
print(re.findall('[aeiou]','the book costs 122346 Rs and pen costs 778998'))

## match the numbers
print(re.findall('[0123456789]','the book costs 122346 Rs and pen costs 778998'))

#############################################################################################

## character "-": It helps to match the character in the given range

## match the numbers
print(re.findall('[0-9]','the book costs 122346 Rs and pen costs 778998'))

## match the lowercase characters
print(re.findall('[a-z]','the book costs 122346 Rs and pen costs 778998'))

## match the uppercase characters
print(re.findall('[A-Z]','the book costs 122346 Rs and pen costs 778998'))

## match the lowercase and uppercase characters
print(re.findall('[a-zA-Z]','the book costs 122346 Rs and pen costs 778998'))

##############################################################################################

## Character "+": It helps to 1 to n number of character as long as there is a match

## match the numbers as long there is a match
print(re.findall('[0-9]+','the book costs 122346 Rs and pen costs 778998'))

## match the lowercase characters as long there is a match
print(re.findall('[a-z]+','the book costs 122346 Rs and pen costs 778998'))

print(re.findall('An+a','Hello Anna'))
print(re.findall('An+a','Hello Annnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnna'))
print(re.findall('An+a','Hello Ana'))
print(re.findall('An+a','Hello Aa'))

######################################################################################

## character "*": It helps to match 0 to n number of character as long as there is match

print(re.findall('An*a','Hello Anna'))
print(re.findall('An*a','Hello Annnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnna'))
print(re.findall('An*a','Hello Ana'))
print(re.findall('An*a','Hello Aa'))

######################################################################################

## character "?": It helps to match exactly 0 or 1 character

print(re.findall('colou?r','What a beautiful colour'))
print(re.findall('colou?r','What a beautiful color'))
print(re.findall('colou?r','What a beautiful colouuuur'))

######################################################################################

## Negation "^"

## match the characters other than digit
print(re.findall('[^0-9]','the book costs 122346 Rs and pen costs 778998'))

## match the characters other than lowercase
print(re.findall('[^a-z]','the book costs 122346 Rs and pen costs 778998'))

## match the characters as long as there is match other than digit
print(re.findall('[^0-9]+','the book costs 122346 Rs and pen costs 778998'))

######################################################################################

## word boundary(\b):It helps to match the character in the given boundary
## word boundary means there must be transition between word character and non-word character

print(re.findall('day',"what a beautiful day today is"))
print(re.findall(r'\bday',"what a beautiful day today is"))
print(re.findall(r'day\b',"what a beautiful day today is"))
print(re.findall(r'\bday\b',"what a beautiful day today is"))

# Regular expression which matches words that starts with "h"
print(re.findall(r'\bh[a-zA-Z]+','hello world hi hello universe how are you happy birthday'))

# Regular expression which matches words that starts with "P or J"
print(re.findall(r'\b[PJ][a-zA-Z]+','Python is a programming language. Python is easier than Java'))

# Regular expression which matches words that ends with "y"
print(re.findall(r'\b[a-zA-Z]+y\b','hello world hi hello universe how are you happy birthday feeling very sleepy flying'))

# print only those words starting with vowel character
print(re.findall(r'\b[aeiou][a-zA-Z]+',"hello hi american english and indian ocean united states"))

# Matching only pdf files
print(re.findall(r'\b[a-zA-z]+.pdf\b',"downloading apple.pdf orange.csv grape.pdf ice.txt to downloads folder"))











