
## File: It is the container which helps to store the data/information
## Based on the extension we get to know the type of data stored in the file
## File handling: It helps to write the data into the file and read the data from the file
## syntax we use to open file is: with open('file_name/file_path', mode) as var:
## There are 3 types of mode
##1. write mode             ##2. read mode                  ##3. append mode

#################################################################################

##1. write mode: It helps to write the data into the file

# write(): It helps to write the single line of data in the form of string
# syntax: var.write('data')

# with open('file1.txt', 'w') as a:
#     a.write('Hello')

# with open('file1.txt', 'w') as a:
#     a.write('Hello Hii')

## If the file is not present it creates the file and stores the new data in it
## If the file is already present it overwrites the previous data and stores the latest one

# writelines(): it helps to write multiple lines of data in the list format
# syntax: var.writelines(['data1', 'data2',........])

# with open('file2.txt', 'w') as b:
#     b.writelines(['Hello\n', 'Hi\n', 'Good Morning\n', 'How are you??'])

################################################################################

##2. read mode: It helps to read the data from the file

# read(): It helps to read the complete data from the file in the form of string
# syntax: var.read()

# with open('file2.txt', 'r') as a:
#     print(a.read())

# readline(): It helps to read one line of data at once

# with open('file2.txt', 'r') as a:
#     print(a.readline())
#     print(a.readline())

# readlines(): It helps to read complete data from the file in the form of list

# with open('file2.txt', 'r') as a:
#     print(a.readlines())

################################################################################

## append mode: It helps to write the data into the file
## The difference between the write and append mode is, in case of write mode it overwrites the
## previous data and store new data file is already present but in case of append it adds the add

# with open('file1.txt', 'a') as c:
#     c.write('Good Morning')

################################################################################

## Reading the data from the file using for loop

# with open(r"C:\Users\QSP\Documents\File_Handling\logfilesample.txt") as a:
#     for line in a:
#         print(line)
#
# with open(r"C:\Users\QSP\Documents\File_Handling\logfilesample.txt") as a:
#     for line in a:
#         print(line.strip())

## Get the line number to each line

# with open(r"C:\Users\QSP\Documents\File_Handling\logfilesample.txt") as a:
#     for line_no, line in enumerate(a):
#         print(line_no, line.strip())

# with open(r"C:\Users\QSP\Documents\File_Handling\logfilesample.txt") as a:
#     for line_no, line in enumerate(a, start = 1):
#         print(line_no, line.strip())

## Create the dict in such a way the line number acts as key and line as value

# with open(r"C:\Users\QSP\Documents\File_Handling\logfilesample.txt") as a:
#     Dict = {}
#     for line_no, line in enumerate(a, start = 1):
#         Dict[line_no] = line
#     print(Dict)

#####################################################################################

## Reading the data from the file using function

def read_log():
    with open(r"C:\Users\QSP\Documents\File_Handling\logfilesample.txt") as a:
        records = []
        for line in a:
            clean_line = line.strip()
            words = clean_line.split()
            records.append(words)
        return records
# print(read_log())

## Get only the time component

def Get_Time():
    data = read_log()
    get_time = []
    for item in data:
        get_time.append(item[1])
    return get_time
# print(Get_Time())

## Remove all the duplicate time(with and without typecasting)

## With Typecasting

def Get_Unique_Time():
    data = read_log()
    get_Unique_time = []
    for item in data:
        get_Unique_time.append(item[1])
    return list(set(get_Unique_time))
# print(Get_Unique_Time())

## Without Typecasting

def Unique_Time():
    data = Get_Time()
    unique_time = []
    for time in data:
        if time not in unique_time:
            unique_time.append(time)
    return unique_time
# print(Unique_Time())


#########################################################################

## CSV File Handling(comma separated values)

## syntax to write the data into the csv file

# import csv
# with open('file_path/file_name', 'w') as var:
#     var1 = csv.writer(var)
#     var1.writerow([data1, data2,.....])         ## It helps to write single row of data
#     var1.writerows([[data1, data2,.....], [data1, data2,.....], [data1, data2,.....]])  ## It helps to write multiple row of data

# import csv
# with open('file1.csv', 'w', newline= '') as a:
#     b = csv.writer(a)
#     b.writerow(['name', 'age', 'ph_no'])
#     b.writerows([['abc', 13, 765432345654], ['xyz', 15, 87654345678], ['pqr', 14, 8765432345]])

## syntax to read the data from the file

# import csv
# with open('file_name/file_path', 'r') as var:
#     var1 = csv.reader(var)
#     print(list(var1))

import csv
# with open('file1.csv') as a:
#     b = csv.reader(a)
    # print(list(b))

##or

# with open('file1.csv') as a:
#     b = csv.reader(a)
#     for row in b:
#         print(row)

with open(r"C:\Users\QSP\Documents\File_Handling\employees.csv") as a:
    b = csv.reader(a)
    for row in b:
        print(row)
    print('**************')

## Get the count of male and female

# with open(r"C:\Users\QSP\Documents\File_Handling\employees.csv") as a:
#     b = csv.reader(a)
#     male_count, female_count = 0, 0
#     for row in b:
#         if row[1] == 'male':
#             male_count += 1
#         elif row[1] == 'female':
#             female_count += 1
#     print(f'Male_Count:{male_count} Female_Count:{female_count}')

##or

# with open(r"C:\Users\QSP\Documents\File_Handling\employees.csv") as a:
#     b = csv.reader(a)
#     b.__next__()
#     male_count, female_count = 0, 0
#     for row in b:
#         if row[1] == 'male':
#             male_count += 1
#         else:
#             female_count += 1
#     print(f'Male_Count:{male_count} Female_Count:{female_count}')

## Get unique Department

# with open(r"C:\Users\QSP\Documents\File_Handling\employees.csv") as a:
#     b = csv.reader(a)
#     b.__next__()
#     Department = []
#     for row in b:
#         if row[2] not in Department:
#             Department.append(row[2])
#     print(Department)

## Total_Pay

# with open(r"C:\Users\QSP\Documents\File_Handling\employees.csv") as a:
#     b = csv.reader(a)
#     b.__next__()
#     Total_Pay = 0
#     for row in b:
#         Total_Pay += int(row[3])
#     print(Total_Pay)

## Get the details of emp whose name starts with vowel

# with open(r"C:\Users\QSP\Documents\File_Handling\employees.csv") as a:
    # b = csv.reader(a)
    # b.__next__()
    # for row in b:
    #     if row[0][0] in 'aeiouAEIOU':
    #         print(row)


## Get the details of emp whose salary is more than 75k

# with open(r"C:\Users\QSP\Documents\File_Handling\employees.csv") as a:
#     b = csv.reader(a)
#     b.__next__()
#     for row in b:
#         if int(row[3]) > 75000:
#             print(row)

## Get the details of male emp whose salary is less than 75k

# with open(r"C:\Users\QSP\Documents\File_Handling\employees.csv") as a:
#     b = csv.reader(a)
#     b.__next__()
#     for row in b:
#         if int(row[3]) < 75000 and row[1] == 'male':
#             print(row)

## get the details of emp whose name starts with consonants and works in development team

# with open(r"C:\Users\QSP\Documents\File_Handling\employees.csv") as a:
#     b = csv.reader(a)
#     b.__next__()
#     for row in b:
#         if row[0][0] not in 'aeiouAEIOU' and row[2] == 'development':
#             print(row)
