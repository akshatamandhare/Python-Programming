# ## Break

# # 1. Write a for loop that prints numbers from 1 to 10. Use a break statement to exit the loop when the number 5 is encountered.
for i in range(1, 10):
    if i==5:
        break
    else:
        print(i)



# 2. Create a loop that continuously prompts the user to enter a number. 
# Use a break statement to exit the loop if the user enters a negative number.
while True:
    num = int(input("Enter num: "))
    if(num<0):
        print("Number is negative!!")
        break


# 3. Given a list of numbers, write a for loop to search for the number 7. If found, print "Found" and exit the loop using break.
list = [10, 20, 30, 7]
for i in list:
    if(i==7):
        print("Found")
        break
    else :
        print(i)


# 4. Iterate through numbers from 1 to 20. Use a break statement to exit the loop when a number divisible by 3 is encountered.
for i in range(1, 20):
    if(i%3==0):
        break
    else:
        print(i)

# 5.  Iterate over each character in the 
string = "PythonProgramming"
# Use a break statement to exit the loop when the character 'g' is encountered.
for char in string:
    if char=='g':
        print("found 'g'")
        break    
    print(char)

# 6. Write a loop that adds numbers from a list until the sum exceeds 50. Use a break statement to exit the loop once this condition is met.
list = [10, 20, 3, 4, 5, 16,19,28]
sum =0
for i in list:
    sum+=i
    if sum>50:
        print(sum)
        break

# ## continue

# 1. Write a for loop that prints numbers from 1 to 10, but skips the number 5 using the continue statement.
for i in range(1, 10):
    if i==5 :
        continue
    print(i)

# 2.  Iterate through numbers from 1 to 20. Use continue to skip even numbers and print only the odd ones.
for i in range(1, 10):
    if i%2==0 :
        continue
    print(i)

# 3. Given the 
string = "Python Programming"
# write a loop that prints each character except vowels. Use continue to skip vowels.
for char in string:
    if char.lower() in 'aeiou':
        continue
    print(char)

# 4. Write a loop that prints numbers from 1 to 30, but skips numbers that are multiples of 3 using the continue statement.
for i in range(1, 30):
    if i%3==0 :
        continue
    print(i)

# 5. Given a list of fruits
list = ["apple", "banana", "cherry", "date", "fig"]
# write a loop that prints each fruit except "banana" and "date". Use continue to skip these.
for word in list:
    if word  in ("banana" and "date"):
        continue
    print(word)


# 6. Given a list of numbers 
list = [10, -5, 20, -3, 0, 15]
# write a loop that prints only the non-negative numbers using continue to skip negatives.
for i in list:
    if i<0:
        continue
    print(i)

# ## Comprehension

# 1. WAP TO CREATE A NEW LIST, WHICH CONSIST OF NAMES STRATS WITH CONSONANTS
NAMES = ['APPLE', 'YOUTUBE', 'EMAIL', 'GMAIL', 'YAHOO']
print([word for word in NAMES if word[0].lower() not in 'aeiou'])

# 2. COUNTING THE NUMBER OF EACH WORD IN A STRING, GET LIST OUTPUT
sentence = 'hello world welcome to python hello hi world welcome to python'
print([len(word) for word in sentence.split()])

# 3. WAP TO CREATE THE LIST OF ONLY THOSE KEYS OF DICT WHOSE VALUE IS EVEN
dict_ = {'a':1, 'b':2, 'c':3, 'd':4}      #out = ['b', 'd']
print([ key for key in dict_ if dict_[key]%2==0 ])

# 4. WAPT CREATE A SET OF NUMBERS WHICH ARE DIVIDING WITH 6 OR 9 TILL 50 THAT SHOULD BE UNIQUE
print({i for i in range(1, 50) if i%6==0 or i%9==0})

# 5. WAP TO EXTRACT ALL THE NUMBER WHOSE LAST 2 DIGITS ARE DIVISIBLE BY 4
list_ = [444, 1234,448, 1096, 1908, 575]
print([element for element in list_ if(element%100)%4==0])
        
# 6. WAP TO CREATE THE LIST OF KEYS AND VALUES IF THE VALUE ARE ODD
dict_ = {'A':1, 'B':2, 'C':3, 'D':4}   ##out = [('A', 1), ('C', 3)] 
print([(key, dict_[key]) for key in dict_ if dict_[key]%2!=0])