# 1. WAP to check the given number is a neon number or not.
def neon(n):
    digits = list(map(lambda x: int(x), str(n ** 2)))
    if sum(digits) == n:
        print("Neon Number")
    else:
        print("Not a Neon Number")

neon(9)
neon(4584)

# 2. sort this list based on age, grade and name
students = [
     {"name": "john", "grade": "A", "age": 26},
     {"name": "jane", "grade": "B", "age": 28},
     {"name": "dave", "grade": "B", "age": 22}
        ]

print(list(sorted(students, key = lambda data : data['age'])))
print(list(sorted(students, key = lambda data : data['grade'])))
print(list(sorted(students, key = lambda data : data['name'])))

# 3. sort the list based on name, shares and price
portfolio = [
            {'name': 'IBM', 'shares': 100, 'price': 91.1},
            {'name': 'AAPL', 'shares': 50, 'price': 543.22},
            {'name': 'FB', 'shares': 200, 'price': 21.09},
            {'name': 'HPQ', 'shares': 35, 'price': 31.75},
            {'name': 'YHOO', 'shares': 45, 'price': 16.35},
            {'name': 'ACME', 'shares': 75, 'price': 115.65}
            ]

print(list(sorted(portfolio, key= lambda x: x['name'])))
print(list(sorted(portfolio, key= lambda x: x['shares'])))
print(list(sorted(portfolio, key= lambda x: x['price'])))

# 4. Write a program to get the below output sentence
string = "hello world welcome to python programming hi there"
#d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python","programming"]}

words = string.split()
keys = set(map(lambda word: word[0], words))
result = dict(map(lambda key: (key, list(filter(lambda word: word[0] == key, words))),keys))
print(result)

# 5. Read the data from the file,
	# 1. get ip address
def get_ip():
    with open("access-log.txt", 'r') as a:
        ip_address = []
        for line in a:
            data = line.split()
            if data :
                ip_address.append(data[0])
        return ip_address
print(get_ip())

# 2. unique ip address
def get_unique_ip():
    ip_address = get_ip()
    unique_ip = []
    for ip in ip_address:
        if ip not in unique_ip:
            unique_ip.append(ip)
    return unique_ip
print(get_unique_ip())

# 3.create the dict, in which the ip_address acts as key and number of times it repeated as value
def get_ip_count():
    ip_address = get_ip()
    ip_dict = {}
    for ip in ip_address:
        if ip not in ip_dict.keys():
            ip_dict[ip] =1
        else : 
            ip_dict[ip] +=1
    return ip_dict
print(get_ip_count())

# 6. write a decorator to validate name,if name having minimum 5 character in it print "you have good name " else print "add few more characters"
def get_name_length(some_thing):
    print(some_thing)
    def wrapper(string):
        res = some_thing(string)
        if len(res)>=5:
            print("You have good name")
        else:
            print("add few more characters")
    return wrapper

@get_name_length
def get_name(string):
    return string

get_name("Akshata")
get_name("Dev")

# 7. WAP to get the following output
string = 'work hard to get success'
# out = 'krow drah ot teg sseccus'
print(list(map(lambda word: word[::-1], string.split())))

# 8. WAP to iterate over list of list, which consists of students details in it (like name, mail, ph_no),
#     take input from user
#     #. if he enters 1 it should display names of all students
#     #. if he enters 2 it should display mail of all students
#     #. if he enters 3 it should display ph_no of all students

list_ =[ ['Akshata', 'akshat@.com', 41651619874], ['abc', 'abc@.com', 651619654191], ['xyz', 'xyz@.com', 5498498198498]]
number = int(input("Enter Number: "))
print(list(map(lambda data: data[0] if number == 1 else data[1] if number == 2 else data[2],list_)))


# 9. WAP to get following output
string = 'one eight three' ##out: 12 
dict_ = {
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
    'ten':10
}
print(sum(list(map(lambda word: dict_[word] , string.split()))))

# 10. WAP to get the following output
number = 183 # out = 'one eight three' 

num_list = list(map(lambda x: int(x), str(number)))
dict_ = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten'
}
# print(num_list)
result = ' '.join(map(lambda x: dict_[x], num_list))
print(result)

# 11. Input
tuples = [("Alice", 25), ("Bob", 30), ("Carol", 20), ("David", 25)]
# # Output
# # [("Carol", 20), ("Alice", 25), ("David", 25), ("Bob", 30)]
print(list(sorted(tuples, key = lambda x: x[-1])))

# 12. 
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
# by using lambda.
# # Output
# # [10, 40, 90, 160]
print(list(map(lambda x : x[0]*x[1], zip(list1, list2))))

# 13. remove empty strings by using filter
# # Input
strings = ["hello", "", "world", "", "python"]
# # Output
# # ["hello", "world", "python"]
print(list(filter(lambda string: string!="", strings)))

# 14. capitalize_words
# # Input
words = ["apple", "banana", "cherry", "date"]
# # Output
# # ["Apple", "Banana", "Cherry", "Date"]
print(list(map(lambda string: string.capitalize(), words)))

# 15.count_vowels  using a lambda function and map.
# # Input
words = ["hello", "world", "python", "programming"]
# # Output
# # [2, 1, 1, 3]
print(list(map(lambda word: sum(map(lambda ch: ch in 'aeiou', word.lower())), words)))

#16. WAPT return dict of index and element pair
list_ = ['hai', 'take', 'care']
print(dict(map(lambda index: index ,enumerate(list_))))

#17. WAPT to return a string by reversing if it is having even length else
#return as it is
string = 'Akshata mandhare'
print(list(map(lambda string: string[::-1] if len(string)%2==0 else string, string.split())))