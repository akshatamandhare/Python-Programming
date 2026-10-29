## It is the process of using the same method/operator to work on different operation

## There are 3 types

##1. Operator Overloading
##2. Method Overloading
##3. Method Overriding

#####################################################################################

##1. Operator Overloading: WKT all the operator works on inbuilt classes but not on user defined class
## to make operator work on user defined class we use operator overloading

class sam:
    def __init__(self, a):
        self.a=a

    def __add__(self, other):
        return self.a + other.a

    def __sub__(self, other):
        return abs(self.a - other.a)

    def __mul__(self, other):
        return (self.a * other.a)

# s1 = sam(12)
# s2 = sam(22)

# print(dir(s1))
# print(s1.__add__(s2))
# print(s1.__sub__(s2))
# print(s1.__mul__(s2))
# print(s1.a, s2.a)

########################################################################################

##2. Method Overloading: Python doesn't support method overloading by default
## Here in this case we will have same method name but different number of args in a same class

class demo1:

    def add(self, a, b, c=0):
        return a+b+c

d1=demo1()
print(d1.add(2, 4))
print(d1.add(2, 4, 7))


class demo2:

    def add(self, *args):
        print(args)
        total=0
        for num in args:
            total+=num
        return total

d1=demo2()
# print(d1.add())
# print(d1.add(2, 4))
print(d1.add(2, 4, 7, 6))


#######################################################################

##3. Method Overriding: We must have at least 2 class. Here we will have the same method name
## same number of args but the functionality differs based on the location

class company1:
    company_name = 'Infosys'
    company_loc = 'Mysore'

    def __init__(self, id, dept):
        self.id = id
        self.dept = dept

    def info(self):
        print(f'i am using {c.dept}')

c1 = company1(101, 'IT')
c=company1(102, 'Finance')
# print(company1.company_name, company1.company_loc)
# print(c1.company_name, c1.company_loc)
# c1.info()
# c.info()


class company2(company1):
    def info(self):
        print("I am in company 2")

c2=company2(104, 'HR')
print(c2.dept, c2.company_loc)
c2.info()