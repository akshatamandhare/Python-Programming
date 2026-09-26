# Assignment- II (21-sept-2026)

string1= 'python.py'
## 'thon'
print(string1[2:5+1:1])
## 'yhnp'
print(string1[1: : 2])
## 'yp.nohtyp'
print(string1[::-1])
## 'hty'
print(string1[3:1-1:-1])
## pto.y
print(string1[::2])
## reverse entire string
print(string1[::-1])
## get alternate character in reverse
print(string1[::-2])

string = "Hi Welcome to python"
##1. Print Every Alternate Characters
print(string[::2])
##2. Print Every Alternate Characters in reverse order
print(string[::-2])
##3. Print the string in reversed order
print(string[::-1])
##4. Print extension of the filename 
path = 'youtube.txt'
print(path[-3:])
##5. Print only filename
print(path[:-5+1:1])
##6. Printing only protocol in 
url = 'https://google.com'
print(url[:4+1:])
##7. Print only domain 
print(url[8:13+1:1])

tuple_ = ('selenium', 'manual', [45, 89.9, 'webtech', ['python', 'good', 'evening']], 'sql')

## len
print(len(tuple_))
## nel
print(tuple_[0][4:2-1:-1])
## reverse the string 'python'
print(tuple_[2][3][0][::])
## get alternate character of 'evening'
print(tuple_[2][3][2][::2])
## get alternate character of 'webtech' in reverse
print(tuple_[2][2][::2])
## [89.9, 'webtech']
print(tuple_[2][1:2+1:1])
## [45, 89.9, 'webtech', ['python', 'good', 'evening']]
print(tuple_[2][::])
## ['evening', 'good', 'python']
print(tuple_[2][3][::-1])
## ['good', 'evening']
print(tuple_[2][3][1:2+1:])
## 'lqs'
print(tuple_[-1][::-1])
## 'aul'
print(tuple_[1][1::2])
## 'anu'
print(tuple_[1][1:3+1:1])
## 'nua'
print(tuple_[1][2:-2+1:1])


names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
##1. Reverse the above list. 
print(names[::-1])
##2. What is the output of names[2][3] 
print(names[2][3] ) 
ans - > '0'
##3. What is the output of
##	a. names[-2: 3]   
ans ---> 't'
##	b. names[-6:5]    
ans ---> 'e'
#	c print(names[-1:2:-1]) 
ans --->['microsoft', 'instagram', 'facebook', 'amazon']
##	d. names[13]
ans --->error


d = {'a':10, 'b':[1,2,'hello', 'python'] ,'c':{'d':[(1,2),['good morning',23,8+9j,76]]}, 'p':{1,2,3}}
##	get the following output 
##		1.‘olleh’
print(d['b'][2][::-1])
##		2.'girmdo'
print(d['c']['d'][1][0][-1::-2])
##		3.{1,2,3}
print(d['p'])
##		4.'pto'
print(d['b'][3][::2])
##		5.['good morning',23,8+9j,76]
print(d['c']['d'][1][::])
##		6.[76,8+9j,23,’good morning’]
print(d['c']['d'][1][::-1])


dict_ = {'key1': ['have a good day', 78, 90.9], 'key2': (45-9j, 'good night', 990, ['python_py']), 9:'hello_hii'}

## ['have a good day', 78, 90.9] reverse this list
print(dict_['key1'][::-1])
## (45-9j, 'good night')
print(dict_['key2'][:2])
## 'hello_hii' get alternate character in reverse
print(dict_[9])
## get alternate character from the 'have a good day' starts from 'v'
print(dict_['key1'][0][::2])
## [78, 90.9]
print(dict_['key1'][1::])
## reverse the string 'python_py'
print(dict_['key2'][3][0][::-1])

##.Explain less than or equal to operators.
Ans:- Return True if operand1 is less than or euals to the operand2 else return false
 
##.Explain membership and identity operator in brief with example.

Membership operator :-  it helps to check the values is in the collection or not
typle: - 
1. in  :-  return True if value is present in the collection else return False
eg:- 
s1 = [1, 2, 3]
print(1 in s1)
2. Not in  :-  return True if value is not present in the collection else return False
eg:- 
s1 = [1, 2, 3]
print(1 not in s1)

# identity operator:- It check two operands are pointing to the same address or not
# type:- 
# 1. is:- It return True if address of two operands are same else returbn False
# eg :-
x=1
y=1
z=2
print(x is y)
print(x is z)
# 2. is not:- It return True if address of two operands is not same else returbn false
# eg:- 
x=1
y=1
z=2
print(x is not y)
print(x is not z)

# ##.What is the output of the following tuple operation
# aTuple = (100,)
# print(aTuple * 2)
output:- (100, 100)

# ##.What is the type of the following variable
# aTuple = ("Orange")
# print(type(aTuple))
output:- string

# ##.What is the output of the following
# aTuple = (10, 20, 30, 40, 50, 60, 70, 80)
# print(aTuple[2:5], aTuple[:4], aTuple[3:])
output:- [30, 40, 50,][10, 20, 30, 40] [40, 50, 60, 70, 80]

##.Guess the correct output of the following code?
# str1 = "PYnative"
# print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1])
output:- Yna PYnat tive PYnative PYnative

##.Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))

## Find Average of Three Integer Numbers
x=1
y=2
z=3
print("Average: ", (x+y+z)/3 )

## Calculate the age of the person by taking birth year and current year as input
birth_yr = int(input("Enter Birth Year: "))
curr_yr = int(input("Enter Current Year: "))
calculate = - birth_yr + curr_yr
print("Age of the Person is: ", calculate)

## Find Perimeter of a Rectangle
length = int(input("Enter Length of Side: "))
weight = int(input("Enter Weight of Side: "))
peri = 2*length + 2*weight
print("Perimeter of a Rectangle: ", peri)

## Find Perimeter of a Square
side = int(input("Enter side of square: "))
peri = 4*side
print("Perimeter of a square: ", peri)

## Convert Days into Hours
days = int(input("Enter Days : "))
hours = days * 24
print(f"{days} Day is {hours} Hours")

## Find circumference of the circle
Radius = int(input("Enter Radius of circle: "))
circum = 2*3.142*Radius
print("circumference of the circle: ", circum)

#WAP to check the string is havinf exactly exactly 5 character
string = 
if(len(string)==5)

data = input("Enter data: ")
if(data=='integer'):
    print("Data is Integer!!")
