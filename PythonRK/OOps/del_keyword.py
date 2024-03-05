"""
    # del keyword
        used to deleter object properties or object itself

        del s1.name # it will delete the object property
        del s1 # it will delete the whole object
"""

class Student:
    def __init__(self,name) -> None:
        self.name = name

s1 = Student("Reeteshu")
print(s1.name)
del s1.name   # deleted the object property
print(s1.name) # output : Student object has no attribute
