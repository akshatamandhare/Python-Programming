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


s=shoppingCart()
# print(s.cart)
# s.add_items('oneplus')
# s.add_items('oneplus', 40)
s.add_items('iphone', 4)
s.add_items('ipad', 4)
s.add_items('imac', 10)
s.add_items('iwatch')
print(s.cart)