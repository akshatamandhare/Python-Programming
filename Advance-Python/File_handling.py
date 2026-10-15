
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

with open('file1.txt', 'w') as a:
    a.write('Hello')

with open('file1.txt', 'w') as a:
    a.write('Hello Hii')

## If the file is not present it creates the file and stores the new data in it
## If the file is already present it overwrites the previous data and stores the latest one

# writelines(): it helps to write multiple lines of data in the list format
# syntax: var.writelines(['data1', 'data2',........])

with open('file2.txt', 'w') as b:
    b.writelines(['Hello\n', 'Hi\n', 'Good Morning\n', 'How are you??'])

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
print(Get_Time())

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
















