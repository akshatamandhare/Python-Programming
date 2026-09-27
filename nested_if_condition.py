
## We will have the if condition inside another if condition

## syntax:

# if condition1:
#     if condition2:
#         TSB2
#     else:
#         FSB2
# else:
#     FSB1

## wap to print the length of collection only if it is having length greater than 5

# Data = eval(input('enter the data: '))
# if type(Data) in [str, list, tuple, set, dict]:
#     if len(Data) > 5:
#         print(len(Data))
#     else:
#         print('The length of the given collection is not greater than 5')
# else:
#     print('The input is not collection type')

## wap to check the given character is vowel or not

# char = input('enter the character: ')
# if char.isalpha():
#     if char in 'aeiouAEIOU':
#         print('The given character is vowel')
#     else:
#         print('The given character is not vowel')
# else:
#     print('The given character is not alphabet')

## Wap to check the person eligible for indian citizenship
# (only if person is above or equal to 18 years and indian)

# Age = int(input('enter the age: '))
# Nationality = input('enter the nationality: ').upper()
# if Age >= 18:
#     if Nationality == 'INDIAN':
#         print('The person eligible for indian citizenship')
#     else:
#         print('The person is not eligible for indian citizenship')
# else:
#     print('The age is not greater or equal to 18')

## Wap to check the number is positive/negative and even/odd

# number = int(input('enter the number: '))
# if number > 0:
#     if number % 2 == 0:
#         print('The number is positive even')
#     else:
#         print('The number is positive odd')
# else:
#     if number % 2 == 0:
#         print('The number is negative even')
#     else:
#         print('The number is negative odd')

# An employee receives a bonus if their performance rating is at least 4.
# If the rating qualifies,
# check whether the employee has completed at least 2 years in the company.

# Rating = int(input('enter the rating: '))
# Year_of_Exp = int(input('enter the exp: '))
# if Rating >= 4:
#     if Year_of_Exp >= 2:
#         print('An employee receives a bonus')
#     else:
#         print('the employee has not completed at least 2 years in the company')
# else:
#     print('The rating is not good enough')

# An online store gives a discount only when the purchase amount is ₹5000 or more.
# If the amount qualifies, check whether the customer is a premium member(yes/no).
# Premium members receive 20% discount; others receive 10%.
# get the discount amount and final price after deducting the discount

# Amount = int(input('enter the amount: '))
# Premium_Membership = input('enter the value: ')
# if Amount >= 5000:
#     if Premium_Membership == 'Yes':
#         Discount = Amount * 0.2
#     else:
#         Discount = Amount * 0.1
#
#     print(f'The discount is {Discount}')
#     Total_Bill = Amount - Discount
#     print(f'The total bill is {Total_Bill}')
# else:
#     print('The person will not get the discount')

# loan application: A bank first checks whether the applicant's salary is at least Rs30,000.
# If the salary is sufficient, check the credit score.
# A credit score of 700 or above makes the applicant eligible

# salary = int(input('enter the salary: '))
# credit_score = int(input('enter the credit score: '))
# if salary >= 30000:
#     if credit_score >= 700:
#         print('The person is eligible for loan')
#     else:
#         print('The person having less credit score')
# else:
#     print('The salary of person is not sufficient')

# Write a program for login authentication. First check whether the password is correct.
# If the password is correct, check whether the Username entered by the user is correct.
# username = 'abc_123'
# password = '123_abc'

# username = input('enter the username: ')
# password = input('enter the password: ')
# if password == '123_abc':
#     if username == 'abc_123':
#         print('Logged In')
#     else:
#         print('The username is not correct')
# else:
#     print('The password in not correct')

# A travel company provides a student discount.
# First check whether the person is a student(yes/no).
# If they are a student, check their age.
# Students below 25 receive the discount.
# data = input("Enter Role: ")
# age = int(input("Enter Age: "))
# if(data == 'student'):
#     if(age<=25):
#         print("Receive discount") 
#     else:
#         print("Person is above 18")
# else:
#     print("Person is not student")

# A cinema allows online booking only if the customer is 18 or older.
# If the customer is eligible, check whether seats are available(yes/no).
age = int(input("Enter Customer Age: "))
seats = input("Enter availablity: ")
if(age > 18):
    if(seats == 'Available'):
        print("Can book online")
    else:
        print("Seats not available, can't book")
else:
    print("Customer age is greater than 18")
    

