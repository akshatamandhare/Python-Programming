#1. Input
tuples = [("Alice", 25), ("Bob", 30), ("Carol", 20), ("David", 25)]
# Output
# [("Carol", 20), ("Alice", 25), ("David", 25), ("Bob", 30)]

print(sorted(tuples, key = lambda x:x[1]))

# 2. 
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
# by using lambda.
# Output
# [10, 40, 90, 160]

print(list(map(lambda item:item[0]*item[1], zip(list1, list2))))

# 3. remove empty strings by using filter
# Input
strings = ["hello", "", "world", "", "python"]
# Output
# ["hello", "world", "python"]

print(list(filter(lambda word: word!='', strings)))

# 4. capitalize_words
# Input
words = ["apple", "banana", "cherry", "date"]
# Output
# ["Apple", "Banana", "Cherry", "Date"]

print(list(map(lambda item:item.capitalize(), words)))

# 5.count_vowels  using a lambda function and map.
# Input
words = ["hello", "world", "python", "programming"]
# Output
# [2, 1, 1, 3]

print(list(map(lambda item: sum(1 for char in item if char in 'aeiouAEIOU'), words )))

#6. WAPT return dict of index and element pair
list_ = ['hai', 'take', 'care']
print(dict(map(lambda item: (item[0], item[1]), enumerate(list_))))


#7. WAPT to return a string by reversing if it is having even length else
#return as it is

print(list(map(lambda item: item[::-1] if len(item)%2==0 else item, list_ )))

#8. WAPT RETURN DICT OF INDEX AND ELEMENT PAIR
l = [3,2,5,7,8]
print(dict(map(lambda item: (item[0], item[1]), enumerate(l))))

#9. WRITE A LAMBDA FUNCTION TO FIND WHETHER A NUMBER LIES BETWEEN 10 AND 100.
number = [30, 40, 20, 10, 9]
print(list(map(lambda item: item in range(10, 100), number)))

#10. REPLACE NUMBERS GREATER THAN 50 WITH "HIGH" ELSE "LOW"
nums = [10, 55, 40, 80, 30]
print(list(map(lambda item: "HIGH" if item>50 else "LOW", nums)))

#11. WAPT CALCULATE THE SUM OF ONLY POSITIVE NUMBER OF A GIVEN LIST
nums = [1,-8,-3,4,-7,-12]
print(sum(filter(lambda x:x>0, nums)))

#12. WAPT FIND IF A GIVEN LIST OF STRING STARTING WITH 'A'
names =['Alex','steve','Anna','henry','john']
print(list(filter(lambda item:item[0] == 'A', names)))

#13. Find the longest non-repeated word in the string
string = 'this is programming language and programming is fun'
words = string.split()
unique_words = list(dict.fromkeys(words))

print(max(unique_words, key=lambda word: len(word)))


#14. Find the most repeated word in given string
string = 'hii helllo hii hii hello good evening good morning hii hii'
words = string.split()
unique_words = [word for word in words if words.count(word) == 1]

print(max(unique_words, key=lambda word: len(word)))