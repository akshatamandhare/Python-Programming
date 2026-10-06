# enumerate

## TAKE LIST OF STRING, GET THE STRING PRESENT AT ODD POSITION USING 
# list_ = ['apple', 'google', 'amazon', 'youtube', 'insta', 'yahoo'] 

# for index, char in enumerate(list_, start = 0):
#     if(index%2==1):
#         print(index, char)

## TAKE LIST OF STRING, GET THE STRING PRESENT AT EVEN POSITION # 
# AND STRING SHOULD START WITH VOWEL # 
# list_ = ['apple', 'google', 'Amazon', 'youtube', 'insta', 'yahoo']

# for index, char in enumerate(list_):
#     if(index%2==0 and char[0].lower() in "aeiou"):
#         print(index, char)

#################################################################

## WAP TO GET THE FOLLOWING OUTPUT 
# LIST1 = [1,2,3,4] 
# LIST2 = [5,6,7,8] 
# # OUT = [5,12,21,32]
# out =[]

# for num1, num2 in zip(LIST1, LIST2):
#     out.append(num1*num2)
# print(out)

#. WAP TO CREATE THE DICTIONARY BY USING GIVEN LIST 
list_ = ['youtube', 'gmail','YAHOO', 'email', 'facebook', 'whatsapp', 'instagram'] 
_list = [1,2,3,5] 
out={}

# for key, value in zip(list_, _list):
#     out[key]=value
# print(out)

from itertools import zip_longest
for key, value in zip_longest(list_, _list, fillvalue = 'no pairs found'):
    out[key]=value
print(out)


