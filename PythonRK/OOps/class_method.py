"""
    A class method is bound to the class & receives the class as an implicit first argument.
    Note = static method can't access or modify class state & generally for utility
        Use ---- @classmethod

"""

class person:
    name = "anonymous"

    @classmethod
    def cahnge_name(cls,name): # cls is just a object of person class
        cls.name = name # by this we are changing the name in the class

p1 = person()
p1.cahnge_name("Reeteshu")
print(p1.name)
print(person.name)
