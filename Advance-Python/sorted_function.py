list_ = [12548725122, 524484, 10]
list_.sort()
print(list_)
list_.sort(reverse = True)
print(list_)

# tuple_ = (12548725122, 524484, 10)
# tuple_.sort()
# print(tuple_)
# tuple_.sort(reverse = True)
# print(tuple_)

# to overcome this use sorted function

## sorted(): It is an inbuilt function, which helps to arrange the elements in particular order
## It will not modify anything in the original collection
## It always gets the list output

## Sorting the list
List = [23456543234567, 876543234567, 876, 1, 100, 4, 989]
print(sorted(List))
print(sorted(List, reverse = True))
print(List)

## sorting the tuple
Tuple = (23456543234567, 876543234567, 876, 1, 100, 4, 989)
print(sorted(Tuple))
print(sorted(Tuple, reverse = True))
print(Tuple)

## sorting the set
set_ = {12548725122, 524484, 10}
print(sorted(set_))
print(sorted(set_, reverse = True))

## sorting the string
string = 'Akshata'
print(sorted(string))
print(sorted(string, reverse = True))

## sorting the dict
dict_ = {'y':3, 'a':100, 'o':4, 'd':60000}
print(sorted(dict_))
print(sorted(dict_, reverse = True))
print(sorted(dict_.values()))
print(sorted(dict_.items()))

#################################################################################

## sorting the list of string based on the length
List = ['amazon', 'youtubeeeeeeeeeeeeeeeee', 'emaillllllllllllllllllllllllllllllllllllll', 'gmail']
print(sorted(List))
print(sorted(List, key = len))
print(sorted(List, key = len, reverse = True))

##2. sorting the list based on last character of the string
list_ = ['bv', 'aw', 'dt', 'cu']
print(sorted(list_))
print(sorted(list_, key = lambda item:item[1]))

##3. sorting the list based on the temperature 
temperatures = [('bangalore', 39), ('delhi',40), ('chennai', 38), ('mumbai', 41)]
print(sorted(temperatures, key = lambda item:item[-1]))
# print(sorted(temperatures))

## sorting the dict based on values 
dict_ = {'a':4, 'b':3, 'c':1, 'd':9}
print(dict_.items())
print(sorted(dict_.items()))
print(sorted(dict_.items(), key= lambda item:item[1]))

print(sorted(dict_.items(), key = lambda item:item[1]))

# sorting the list based on the first element of inner list
list_ = [[2,6], [7,3], [3,8], [8,7], [9,7], [4,9]]
print(sorted(list_, key = lambda item:item[0]))
print(sorted(list_))

# sorting the list based on the last element of inner list
list_ = [[2,6], [7,3], [3,8], [8,7], [9,7], [4,9]]
print(sorted(list_, key = lambda item:item[-1]))

## find the longest substring
string = 'this is programming language and programming is fun'

word_length = {word:len(word) for word in string.split()}
print(word_length)
print(sorted(word_length.items(), key = lambda item:item[1]))
print(sorted(word_length.items(), key = lambda item:item[1])[-1])
print(sorted(word_length.items(), key = lambda item:item[1])[-1][0])