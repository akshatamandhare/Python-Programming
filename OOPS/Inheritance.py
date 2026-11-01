## It is the process of deriving the properties from one class to another class
## The properties from which we inherit is called as parent/super/base class
## The properties to which we inherit is called as child/sub/derived class
## When we inherit the properties from parent to child it will inherit each and every thing
## if we don't want certain properties to be same parent we can re-define in child class

## There are 5 types

##1. Single Level Inheritance
##2. Multi Level Inheritance
##3. Multiple Inheritance
##4. Hierarchical Inheritance
##5. Hybrid Inheritance

####################################################################################

## Constructor Chaining: It helps to invoke the constructor of parent into the child class

## syntax:

##1. super().__init__(args)
##2. ParentName.__init__(self, args)

class School: 
    def __init__(self, name, age, phone_no):
        self.name=name
        self.age=age
        self.phone_no=phone_no

    def info(self):
        print("I am in school class")

# s1 = School('abc', 12, 65144144461)
# print(s1.name, s1.age, s1.phone_no)
# s1.info()


class New_School(School):
    def __init__(self, name, age, phone_no, Class, section):
        School.__init__(self,name, age, phone_no)
        self.Class=Class
        self.section=section

    def info(self):
        print("I am in new_school class")

# s2 = New_School('xyz', 15, 1116854111, '12th', 'A')
# print(s2.name, s2.age, s2.phone_no, s2.Class, s2.section)
# s2.info()

################################################################################################

##1. Single Level Inheritance: It is the process of deriving the properties from single parent to single child class

## syntax:

# class Parent_Class:
#     TSB
#
# class Child_Class(Parent_Class):
#     TSB

class shoppingCart:
    product = {'iphone':8, 'imac':7, 'ipad':5, 'iwatch':6}
    price = {'iphone': 8000, 'imac':7000, 'ipad':5000, 'iwatch':6000}

    def __init__(self):
        self.cart =[]

    def add_items(self, name, quantity = 1):
        if name not in self.product.keys():
            raise Exception("The product not available!!")
        elif self.product[name]>quantity:
            self.cart.append({'Name':name, 'Price': self.price[name], 'Quantity':quantity} )
        else:
            raise Exception("Product Out of Stock") 

    def remove_items(self, name):
        for item in self.cart:
            if name == item['Name']:
                if item['Quantity']==1:
                    self.cart.remove(item)
                else:
                    item['Quantity']-=1

S = shoppingCart()
# print(S.cart)
# S.add_items('oneplus')
# S.add_items('iphone', 40)
# S.add_items('iphone', 4)
# S.add_items('imac', 5)
# S.add_items('ipad', 3)
# S.add_items('iwatch')
# print(S.cart)
# S.remove_items('iwatch')
# print(S.cart)
# S.remove_items('iphone')
# print(S.cart)

## Create one more class and inherit it with ShoppingCart implement the method to calculate total bill

class billing(shoppingCart):

    def calculate_bill(self):
        return sum([])

C = billing()
# print(C.cart)
# C.add_items('iphone', 4)
# C.add_items('ipad', 3)
# C.add_items('iwatch', 4)
# C.add_items('imac', 5)
# print(C.cart)
# print(C.Total_Bill())

##########################################################################################

##2. Multi Level Inheritance: It is the process of deriving the properties from one class
##   to another class by considering more than one level

# syntax:

# class Class1:
#     TSB
#
# class Class2(Class1):
#     TSB
#
# class Class3(Class2):
#     TSB

class BankAccount:
    INTREST_RATE = 0.02

    def __init__(self, name, balance):
        self.name=name
        self.balance = balance
        self.transactions = []
        self.transactions.append(f"The initial amount deposited iss {balance}")

    def Deposite(self, amount):
        if amount <= 0:
            raise Exception(f"You can't deposite rs {0}")
        self.balance = self.balance + amount
        self.transactions.append(f"The amount deposited is {amount}")

    def Withdraw(self, amount):
        if self.balance>amount:
            self.balance = self.balance - amount
            self.transactions.append(f"The amount remining after withdrawal {amount} is {self.balance}")
        else:
            raise Exception("You don't have enough amount")

    def ROI(self):
        ROI_amount = self.balance*self.INTREST_RATE
        self.balance+=ROI_amount
        self.transactions.append(f" The amount credeted Intrest is {ROI_amount}")


    def Statement(self):
        for transaction in self.transactions:
            print(transaction)


B = BankAccount('abc', 10000)
# print(B.name, B.balance, B.transactions)
# B.Deposite(0)
# B.Deposite(20000)
# print(B.balance, B.transactions)
# B.Withdraw(50000)
# print(B.balance, B.transactions)
# B.ROI()
# print(B.balance, B.transactions)
# B.Statement()


class SavingsBankAccount(BankAccount):
    INTREST_RATE = 0.03

    def Withdraw(self, amount):
        if amount>10000:
            raise Exception("The maximum withdraw limit is 10k")
        super().Withdraw(amount)

s = SavingsBankAccount('xyz', 40000)
# print(s.balance, s.transactions)
# s.Deposite(0)
# s.Deposite(50000)
# print(s.balance, s.transactions)
# s.Withdraw(12000)
# s.Withdraw(1000)
# print(s.balance, s.transactions)
# s.ROI()
# print(s.balance, s.transactions)
# s.Statement()


## create class by name SalaryAccount inherit it with SavingsBankAccount redefine interest rate
## override the method deposit if amount less than 20 k raise the error else add amount
## to balance and add the transaction

class SalaryAccount(SavingsBankAccount):
    INTREST_RATE = 0.04

    def Deposite(self, amount):
        if amount < 20000:
            raise Exception("The salary must be more than 20k")
        super().Deposite(amount)

s = SalaryAccount('pqr', 30000)
# print(s.balance, s.transactions)
# s.Deposite(10000)
# s.Deposite(50000)
# print(s.balance, s.transactions)
# s.Withdraw(5000)
# print(s.balance, s.transactions)
# s.ROI()
# print(s.balance, s.transactions)
# s.Statement()

#######################################################################################

##3. Multiple Inheritance: It is the process of deriving the properties from multiple parent to single child class

## syntax:

# class Parent_Class1:
#     TSB
#
# class Parent_Class2:
#     TSB
#
# class Child_Class(Parent_Class1, Parent_Class2):
#     TSB

class Player:
    def __init__(self, name):
        self.name = name

    def Player_Info(self):
        print(f'Hello myself {self.name}')

class Vehicle:
    def __init__(self, Vehicle_name):
        self.Vehicle_name = Vehicle_name

    def Vehicle_Info(self):
        print(f'I am using {self.Vehicle_name}')

class Weapon:
    def __init__(self, Weapon_name):
        self.Weapon_name = Weapon_name

    def Weapon_Info(self):
        print(f'I am using {self.Weapon_name}')

class Game(Player, Vehicle, Weapon):
    def __init__(self, name, Vehicle_name, Weapon_name):
        Player.__init__(self,name)
        Vehicle.__init__(self, Vehicle_name)
        Weapon.__init__(self, Weapon_name)

    def Game_Info(self):
        print(f'Hello myself {self.name} playing the game with {self.Vehicle_name} and {self.Weapon_name}')

G = Game('Steve', 'Motorcycle', 'Gun')
# G.Player_Info()
# G.Vehicle_Info()
# G.Weapon_Info()
# G.Game_Info()

##4. Hierarchical Inheritance:It is the process of deriving the properties from single parent to multiple child class

## syntax:

# class Parent_Class:
#     TSB
#
# class Child_Class1(Parent_Class):
#     TSB
#
# class Child_Class2(Parent_Class):
#     TSB

class Unlock:
    def __init__(self, PIN, FACE):
        self.PIN = PIN
        self.FACE = FACE

    def Unlock_PIN(self, pin):
        if self.PIN == pin:
            print('Unlocked')
        else:
            print('PIN not matching')

    def Unlock_Face(self, face):
        if self.FACE == face:
            print('Unlocked')
        else:
            print('Face not matching') 

U = Unlock('123', 'abc')
# U.Unlock_PIN('123')
# U.Unlock_Face('xyz')

## Create 2 claas
##1. IOS just inherit with Unlock
##2. ANDROID inherit it with Unlock along with PIN, FACE add one more object member
## Fingerprint add implement the method for it


class IOS(Unlock):
    pass

I = IOS('789', 'abc')
# I.Unlock_PIN('123')
# I.Unlock_FACE('abc')

class Android(Unlock):
    def __init__(self, PIN, FACE, FP):
        super().__init__(PIN, FACE)
        self.Fingerprint = FP

    def  Unlock_FP(self, FP):
        if self.Fingerprint == FP:
            print('Unlocked')
        else:
            print("Fingerprint not matching")

A = Android('123', 'abc', 'a1b2')
# A.Unlock_FP('a1b2')
# A.Unlock_PIN('123')
# A.Unlock_Face('xyz')

############################################################################################

##5. Hybrid Inheritance: It is the process of combining  the properties from more than one type of inheritance

class Product:
    def __init__(self, Name, Price):
        self.Name = Name
        self.Price = Price

    def Product_Info(self):
        print(f'Name: {self.Name} Price: {self.Price}')

class SmartPhone(Product):
    def __init__(self, Brand, Model):
        self.Brand = Brand
        self.Model = Model
    
    def SmartPhone_Info(self):
        print(f'Brand: {self.Brand} Model: {self.Model}')

class Premium_Product:
    def __init__(self, Waranty_year):
        self.Waranty_year = Waranty_year

    def Waranty_Info(self):
        print(f'Waranty_year: {self.Waranty_year}')

class Premium_SmartPhone(SmartPhone, Premium_Product):
    def __init__(self, Name, Price, Brand, Model, Waranty_year ):
        Product.__init__(self, Name, Price)
        SmartPhone.__init__(self, Brand, Model)
        Premium_Product.__init__(self, Waranty_year)

    def Info(self):
        print('you are using hybrid inheritance')

P = Premium_SmartPhone('Iphone', 90000, 'Apple', 'iphone 17 pro', 2)
P.Product_Info()
P.SmartPhone_Info()
P.Waranty_Info()
P.Info()
