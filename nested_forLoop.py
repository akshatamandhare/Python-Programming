## WAP TO GET THE FOLLOWING OUTPUT
list_ = ['hello', 'hai', 'good', 'morning']
# out = ['eo', 'ai', 'oo', 'oi']

out = []
for word in list_:
    s=''
    for char in word:
        if char.lower() in "aeiou":
            s+=char
    out.append(s)
print(out)

## WAP TO GET THE FOLLOWING OUTPUT
LIST_ = [123, 32, 31, 21]
# OUT = [6, 5, 4, 3]

out = []
for number in LIST_:
    sum=0
    for digit in str(number):
        sum+=int(digit)
    out.append(sum)
print(out)

##. WAP TO GET THE FOLLOWING OUTPUT
list_ = ['HEllo@', 67, 7-9j, 'goOD#']
# out = ['heLLO', 67, (7-9j), 'GOod']

out = []
for element in list_:
    if(type(element) == str):
        new_string = ''
        for char in element:
            if(char.islower()):
                new_string+=char.upper()
            elif char.isupper():
                new_string += char.lower()
        out.append(new_string)
    else:
        out.append(element)
print(out)

##or

out = []
for element in list_:
    if type(element) == str:
        new_string = ''
        for char in element:
            if char.isalpha():
                new_string += char.swapcase()
        out.append(new_string)
    else:
        out.append(element)
print(out)

## WAP TO GET THE FOLLOWING OUTPUT
list_ = [12, 5.6,'hello', 3, 'abc']
# out = {12:144, 'hello':'h104e101l1o8l1o8o111', 3:9, 'abc':'a97b98c99'}

out = {}
for element in list_:
    if type(element) == str:
        new_string = ''
        for char in element:
            new_string += char + str(ord(char))
        out[element] = new_string
    elif type(element)==int:
        out[element]=element**2
print(out)

## WAP TO GET THE FOLLOWING OUTPUT
LIST_ = ['hAi', 'HEllO', 'GOod']
# out: ['A', 'HEO', 'GO']

out =[]
for word in LIST_:
    new_string =''
    for char in word:
        if(char.isupper()):
            new_string+=char
    out.append(new_string)
print(out)


# Wap to get the following output. without length function.
S='power star'
# Out={‘power’:5,’star’:4}

out = {}
for element in S.split():
    count=0
    for char in element:
        count+=1
    out[element]=count
print(out)


# Wap to get the following output.
S ='python programming is fun'
# out = {'pn': ('pythn', 5, 'nhtyp'), 'pg': ('prgrmmng', 8, 'gnmmrgrp'), 'is': ('s', 1, 's'), 'fn': ('fn', 2, 'nf')}
# {'first_char + last_char': ('consonants', len_consonant, 'reverse_consonants')}


out = {}
for word in S.split():              ## ['python', 'programming', 'is', 'fun']
    consonants = ''
    for char in word:
        if char not in 'aeiouAEIOU':
            consonants += char
    out[word[0] + word[-1]] = (consonants, len(consonants), consonants[::-1])
print(out)