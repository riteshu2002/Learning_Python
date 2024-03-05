"""
        __init__ Function
        All classes have a function called __init__(), which is always executed when the class is being initiated

"""

class Student:
   
    def __init__(self, fullname) : # constructor // We have to always pass an argument in constructor i.e self 
        self.name = fullname
        print("Adding new database")

s1= Student("Reeteshu")
print(s1.name) # Reeteshu
