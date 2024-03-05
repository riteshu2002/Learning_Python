"""
    # INheritance ==
        When one class (child/derived) derives the properties & methods of another class (Parent/base).
    # Types of inhertance - 
        1- Single inhertance
        2- Multi-level inheritance // where a class is derived from another derived class which was derived from base class
        3- multiple inheritance // here a derived class can inherit the properties of multiple base classes


"""
 # This is an example if single inhertance
# class car:
#     @staticmethod
#     def start():
#         print("Start")
#     @staticmethod
#     def stop():
#         print("Stop")

# class maruti_car(car): # now this class is inherting the properties of car class
#     def __init__(self, name) -> None:
#         self.name = name

# car1 = maruti_car("Fortuner")
# car1 = maruti_car("Prius")


# print(car1.name)
# print(car1.start()) # here we are calling base class using child class


# multi - level inheritance -- 
class car:
    @staticmethod
    def start():
        print("Start")
    @staticmethod
    def stop():
        print("Stop")

class maruti_car(car): # now this class is inherting the properties of car class
    def __init__(self, brand) -> None:
        self.brand = brand


class fortuner(maruti_car):
    def __init__(self, type) -> None:
        self.type =  type

car1 =fortuner("petrol")

print(car1.type)
print(car1.start()) # here we are calling base class using child class
      
# Multiple inheritance
class A:
    varA = "Welcome To class A"

class B: 
    varB = "Welcome to class B"

class c(A,B): # it is inherting both base classes A and B
    varC = "Welcome to class C"

c1 = c()
print(c1.varC)
print(c1.varB)
print(c1.varA)
