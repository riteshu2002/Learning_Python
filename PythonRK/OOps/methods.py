"""
    Methods are function that belong to objects.

"""
class Student:
    collg_namae = "ABD College"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def welcome(self): # method
        print("Welcome student :",self.name)
    

s1 = Student("Reeteshu",98)
s1.welcome()
