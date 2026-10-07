# 1. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

# classes_held = int(input("Number of classes held: "))
# classes_attended = int(input("Number of classes attended: "))
# percent = int(classes_attended/classes_held*100)
# if(percent >= 75):
#      print("percentage of class attended: ", percent, "%")
#      print("Student is allowed to sit")
# else:
#      print("Precentage is less than 75 so, Student is not allowed to sit")


# 2.write the o/p of the following if 
a = 9
if (a>5 and a<=10):
	print('hello')
else:
	print('bye')

# output--> hello

# 3. Write a program to list all the number which are ending with 5 with using comprehension.
numbers = ['51', '12', '123', '12345', '125', '905', '55', '15', '95655', '55555']

print([char for char in numbers if int(char[-1])==5])

# 4. Wap to get the following output using continue keyword
s = 'hello good evening how are you'
# 	##output: ['olleh', 'gnineve', 'woh' , 'era' , 'uoy']

out = []
for char in s.split():
     if(char=='good'):
          continue
     out.append(char[::-1])
print(out)

# 5. WAPT check a number is divisible by 7 or not

num = int(input("enter number: "))
if(num%7==0):
     print(" Number is divisble by 7!!")
else:
     print(" Number is not divisble by 7!!")

# 6. Write a Program to print ascii values of the characters present in a string.
# (by using all three comprehension)
sentence = "Hi How are you" 
print([ord(char) for char in sentence if char.isalpha()])
print({ord(char) for char in sentence if char.isalpha()})
print((ord(char) for char in sentence if char.isalpha()))

# 7. Write a program to find the intial index of the given character
s = 'hello everyone how are you all'
ch = 'e'

for index, char in enumerate(s):
    if char == ch:
        print(f"Found {ch} at index {index}")
        break

# 8. Write a program to get the following output 
my_string = 'hellohai'
#0/P should be 'hel-o-ai'
# for char in my_string:
i=0
while (i<len(my_string)):
    my_string.replace(my_string[i], ('-'))
    i+=3
print( "MY NEW STRING IS " , my_string)


# 9. Write a python program to get the below outputes using for loop
sentence = "Hi How are you"
# o/p should be "ouy era woH iH"
out=''
for word in sentence.split():
    out+=word[::-1]+" "
print(out)


# 10. write a program to reverse the values in the dictionary if the value is of type String 
d={'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}

for value in d:
    if(type(d[value])==str):
        d[value] = d[value][::-1]
print(d)

# 11. Wap to get the following output
list_ = [12, 'hello', 'hai', 77-8j, [1,4], 89.55, 97.333]
## output: [3, 'eo', 'ai', [89, 55], [97, 333]]

out =[]
for element in list_:
    if(type(element) == str):
        new_str = ''
        for index, char in enumerate(element):
            if char.lower() in 'aeiou':
                new_str+=char
        out.append(new_str)
    if(type(element)==float):
        new_list = []
        for char in str(element).split('.'):
            new_list.append(int(char))
        out.append(new_list)
print(out)


# 12. Write a Program to print the sum of all the numbers 
L= [[1,2,3], [4,5,6], [7,8,9]]
sum=0
for element in L:
    for value in element:
        sum+=value
print(sum)

# 13.  update the tuples
a = (1, 2, 3, 4)
b = (100, 200, 300) 
#o/p (1, 2, 3, 4, 100, 200, 300)
out =()
for a_element in a:
    out+=(a_element, )
for b_element in b:
    out+=(b_element, )
print(out)

# 14. explian the functionality of keywords break ,continue,pass with exmaple
# break:- when "break" encounter it get out of the loop and never execute loop again 
# continue:- when "continue" encounter it skip the current execution and exeute the next loop 
# pass:- pass make a empty block valid

# eg - print number from 1 to 10 if 5 occurs stop the printing
# eg - do not print the element which is divisible by 2 from 10 to 20
# eg - pass the empty block in loop 

# 15. What is Mutable and Immutable datatypes
# Mutable: datatypes we can change or modify the elements
# eg - list, dict
# immutable: datatypes we can not change or modify the elements
# eg- tuple, set

# 16. wap to extract all the string from the list using while loop

list = [12, 'hello', 'hai', 77-8j, [1,4], 89.55, 97.333]

new_list = []
for element in list:
    if(type(element)==str):
        new_list.append(element)
print(new_list)

# 17. wap to find the length of the list without using len()

count=0
for i in list:
    count+=1
print(count)

# 18. Write a program to remove the duplicate values without typecasting
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail']

new_names = []
for word in names:
    if word not in new_names:
        new_names.append(word)
print(new_names)

# 19. Write a program to count the number of white spaces in a given string
s = "This is a Programming language and Programming is fun"

count=0
for i in s:
    if(i == ' '):
        count+=1
print(count)

# 20. What is the difference between append() and extend() method in listes
# append():- Adds the entire object as a single element.
# extend():- Adds the elements one by one from the given iterable.

# 21. What is the difference between while loop and for loop. 
# while loop: - check the condition given and execute the block of code if it is false it stop execution opf code 
# for loop: - already define the condition how many time loop will execute block of code
