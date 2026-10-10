# Activity_on_Functions

# 1. WAP to check the given number is perfect number
# sum of divisor of number is equal to given number call perfect number
def per_num(number):
    i=1
    sum=0
    while(i<number):
        if(number%i==0):
            sum+=i
        i+=1
    if(sum==number):
        return True
    else:
        return False
print(per_num(10))

# 2. WAP to check the given number is amstrong number
def amstrong(number):
    original_num = number
    sum=0
    length = len(str(number))

    while(number>0):
        digit = number%10
        temp=digit**length
        sum+=temp
        number//=10
    if(sum==original_num):
        return True
    else:
        return False
print(amstrong(10))
print(amstrong(153))
print(amstrong(370))

# 3. WAP to check the given number is strong number
def strong_num(number):
    original_number = number
    sum=0

    while(number > 0):
        digit = number%10

        fact=1
        i=1

        while(i<=digit):
            fact *= i
            i+=1
        sum+=fact
        number//=10
    
    if(sum==original_number):
        return True
    else:
        return False
print(strong_num(145))
print(strong_num(123))

# 4. Wap to check the given number is harsad number
def harshad_num(number):
    original_num=number
    sum=0
    while(number>0):
        digit = number%10
        sum+=digit
        number//=10
    if(sum!=0 and original_num%sum==0):
        return True
    else:
        return False
print(harshad_num(18))
print(harshad_num(21)) 

# 5. Given a list of integers, return True if the sequence of numbers 1, 2, 3 appears in the list somewhere.
# For example:
	# listCheck([1, 1, 2, 3, 1]) → True
	# listCheck([1, 1, 2, 4, 1]) → False
	# listCheck([1, 1, 2, 1, 2, 3]) → True

def list_check(number):
    for i in range(len(number)-2):
        if(number[i]==1 and number[i+1]==2 and number[i+2]==3):
            return True
    return False
print(list_check([1, 1, 2, 3, 1]))


# 6. Given a string, return a string where for every char in the original, there are two chars.
	# doubleChar('The') → 'TThhee'
	# doubleChar('AAbb') → 'AAAAbbbb'
	# doubleChar('Hi-There') → 'HHii--TThheerree'

def double_char(string):
    new_str = ''
    for i in range(len(string)):
        new_str+=string[i]+string[i]
    return new_str
print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))

# 7. Wap to get the following output
dict_ = {'A':10, 'B':20, 'c':10, 'D':30, 'E':20}
	# output = {10:['A', 'C'], 20:['B', 'E'], 30:['D']} 

def get_output(dict):
    out = {}
    for key in (dict):
        value=dict[key]
        if(value in out):
            out[value].append(key)
        else:
            out[value] = [key]
    return out
print(get_output(dict_))



# 8. WAP TO FIND THE SUM OF ASCII VALUE OF ALL THE SPECIAL CHARACTER PRESENT IN THE STRING

def ascii_value(string):
    sum=0
    for char in string:
        if not char.isalnum() and not char.isspace():
            print(f'ASCII value of {char} : {ord(char)}')
            sum+= ord(char)
    return sum
print("Sum of ASCII values:", ascii_value('Akshata@#sisj'))

# 9. WAP TO FIND THE SUM OF ALL THE INDIVIDUAL DIGITS PRESENT IN THE GIVEN INTEGER NUMBER ONLY IF THE DIGIT IS EVEN

def get_sum(number):
    sum=0
    while(number>0):
        digit = number%10
        if(digit%2==0):
            sum+=digit
        number//=10
    return sum
# print(get_sum(154))
print(get_sum(4286))

# 10.WAP get the sum of all the even digits we have the input string

def get_sum_evendigit(string):
    sum=0
    for char in string:
        if char.isdigit():
            integer = int(char)
            if(integer%2==0):
                sum+=integer
    return sum
print(get_sum_evendigit('Ak12334mandhare'))

# 11.WAP to extract all the string from the tuple only if the length of string > 4

def get_string(tuple_):
    out = ()
    for element in tuple_:
        if isinstance(element, str) and len(element) > 4:
            print(element)
            out += (element,)
    return out
print(get_string((10, 20, 30, 'Akshata', 'Good Morning', 'hii')))


# 12.WAP to extract all the int number from the list, if number having exactly 3 digits

def get_integer(list_):
    out = []
    for char in list_:
        if(type(char)==int and len(str(char))==3):
            print(char)
            out.append(char)
    return out
print(get_integer([10, 20, 50,859 ,35,1000, 100, "Akshata", 'good']))

# 13. Give examples for each
	# 1. local variable : 
    def get():
        a=10
	# 2. Global variable
    a=10
    def get():
        b=10
	# 3. What is global keyword, give an example
    # we can global keyword into the  functon or outside the function 

	# 4. What is non-local keyword, give an example
    # 

	# 5. Tuple Packing
    #
	# 6. Dictionary Packing
	# 7. Variable argument
	# 8. Unpacking  