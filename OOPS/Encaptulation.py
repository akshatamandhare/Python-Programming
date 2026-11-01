## It helps to avoid the direct access of attribute/methods outside the class

## There are 3 types

##1. Public Access Specifiers
##2. Protected Access Specifiers
##3. Private Access Specifiers

##########################################################################################

##1. Public Access Specifiers

class school:
    def __init__(self, Name):
        self.Name = Name

    def school_info(self):
        print(f'Hello myself {self.Name}')

S = school('abc')
# print(S.Name)
# S.school_info()

##########################################################################################

##2. Protected Access Specifiers

class school:
    def __init__(self, Name, roll_no ):
        self.Name = Name
        self._roll_no = roll_no

    def school_info(self):
        print(f'Hello myself {self.Name} and Roll_No {self._roll_no}')

S = school('Akshata', 12)
# print(S._roll_no)
# S.school_info()

##########################################################################################

##3. Private Access Specifiers

class school:
    def __init__(self, Name, roll_no, age ):
        self.Name = Name
        self._roll_no = roll_no
        self.__age = age

    def school_info(self):
        print(f'Hello myself {self.Name}, Roll_No {self._roll_no} and age {self.__age}')

S = school('Akshata', 12, 23)
# print(S.__age)
# S.school_info()

##################################################################################

## Since the private attribute restrict the user not to access outside the class we use it in
## data hiding process

## getter and setter

class bank:
    def __init__(self, balance):
        self.__balance=balance

    def getter(self):
        print(f'Balance: {self.__balance}')

    def setter(self, balance):
        self.__balance = balance

# B = bank(10000)
# B.getter()
# B.setter(50000)
# B.getter()

######################################################################################################

## property()

class school:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade

    def getter(self):
        return self.__grade

    def setter(self, name, grade):
        self.__grade = grade

    res = property(getter, setter)

S = school('abc', 'A+')
# print(S.res)
# print(S.name)
# S.setter('xyz', 'B+')
# print(S.res)

## @property

class bank:
    def __init__(self, name, balance):
        self.name=name
        self.__balance=balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new):
        self.__balance=new

b = bank('Akshata', 50000)
print(b.balance)
b.balance = 90000
print(b.balance)
print(b.name)



