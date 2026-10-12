
List = [1, 3.4, 'hii', 5-9j]            ## Iterable
# print(List)
# print(type(List))

# print(List[0], List[1], List[2], List[3])

# for ele in List:
#     print(ele)

## Iterator: It is an object/address, which helps to iterate over the collections without storing the values in the memory
## iter(): It helps to convert the iterables to iterator
## syntax: iter_var = iter(col_var)         ##or            iter_var = col_var.__iter__()

iter_list = iter(List)          ## Iterators
# print(iter_list)
# print(type(iter_list))

# for ele in iter_list:
#     print(ele)

## next(): It is an inbuilt function which helps to get the value of iterator one by one
## syntax: next(iter_var)           ##or            iter_var.__next__()

# print(next(iter_list))
# print(next(iter_list))
# print(iter_list.__next__())
# print(iter_list.__next__())
# print(iter_list.__next__())     ## Here we get the StopIteration error

## When we get the StopIteration error we must understand that the iterator is already been exhausted
## so there is no element left to fetch

# print(next(iter_list))
# print(iter_list.__next__())
# print('*******************************')
# for ele in iter_list:
#     print(ele)

## Here the for loop gets only the remaining two elements because in case of iterators we can
## iterate only once. Since we have accessed the first two elements using next() the for
## will start from the beginning it will start from the place where it stopped


## Difference between iterables and iterators

## Iterables

##1. It stores the values in the memory
##2. It consist of only __iter__() attribute in it
print(dir(List))
##3. We can iterate multiple times
##4. We can use indexing on iterables because we have the method __getitem__() in it
# print(List[0], List[1], List[2], List[3])   ## or print(List.__getitem__(0))
##5. We can use the len() on the iterables because we have the method __len__() in it
# print(len(List))                ##or       print(List.__len__())


## Iterators

##1. It will store the values inside the memory it stores the address
##2. It consist of both __iter__() and __next__() attribute in it
print(dir(iter_list))
##3. we can iterate only once, if we try to iterate multiple times we get the StopIteration error
##4. We can't use indexing on iterators because we don't have the method __getitem__() in it
# print(iter_list[0], iter_list[1])
##5. We can't use the len() on the iterators because we don't have the method __len__() in it
# print(len(iter_list))

###################################################################################

def Sam():
    return 1
    return 2
    return 3
# print(Sam())

def Demo():
    print('hii')
    return 'hello'
    print('Good Morning')
    return "How are you??"
# print(Demo())

## Generator: It is an inbuilt iterator which helps to create sequence of collection
## Here we use "yield" keyword instead of "return" keyword

def Demo():
    yield 1
    yield 'hiii'
    yield 7-9j
# print(Demo())

# res = Demo()
# print(next(res))
# print(next(res))
# print(res.__next__())
# # print(res.__next__())           ## Here we get StopIteration error because we have no element to fetch

##or

# print(tuple(Demo()))

## WAP TO GET ALL THE EVEN NUMBERS FROM THE LIST USING GENERATOR
# list_ = [1,2,3,4,5,6,7]  out = [2,4,6]

def Get_Even_Num(List):
    for num in List:
        if num % 2 == 0:
            yield num
# print(list(Get_Even_Num([1,2,3,4,5,56])))

##generator expression

List = [1,2,3,4,5,56]
# print(list(num for num in List if num % 2 == 0))

## WAP TO YIELD ALL THE STRING WHICH STARTS WITH VOWEL
list_ = ['apple', 'google', 'ajio', 'youtube', 'insta', 'amazon', 'gmail']

def Get_String(list_):
    for string in list_:
        if string[0] in 'aeiouAEUIO':
            yield string
# print(list(Get_String(['apple', 'google', 'ajio', 'youtube', 'insta', 'amazon', 'gmail'])))

##or

# print(list(string for string in list_ if string[0] in 'aeiouAEUIO'))

## WAP TO GET THE FOLLOWING OUTPUT
list_ = [4.5, 77, 'python', 5-8j, 'java']
# out: {'python':'pn', 'java':'ja'}

def create_dict(list_):
    for element in list_:
        if type(element) == str:
            yield (element, element[0] + element[-1])
# print(dict(create_dict([4.5, 77, 'python', 5-8j, 'java'])))

##or

# print(dict((element, element[0] + element[-1]) for element in list_ if type(element) == str))

# Generator to yield only vowels from a string

def Get_Vowel(string):
    for char in string:
        if char in 'aeiouAUIOU':
            yield char
# print(set(Get_Vowel('hello hii good morning')))

##or
string = 'hello hii good morning'
# print(set(char for char in string if char in 'aeiouAUIOU'))

# Generator to convert words to uppercase
string = 'hello hii good morning'
print(list( char.upper() for char in string ))




# Generator to yield word and length of word in tuple form
string = 'hello hii good evening'









