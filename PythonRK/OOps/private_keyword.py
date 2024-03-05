"""
    Private (like) attribute & methods
        Private attribute & method are meant to be used only within the class and are not
        accessible from outside the class

        To make any value pprivate put __ before name of the variable
          __name , __account_no 
"""
class Accoubt:
    __name = " Anonymous" # private variable

    def __hello(self): # private method
        print("Hello this is private method , you cannot access me outside of the class")
    
    def welcome(self): # this will the private method , which is inside the class

        self.__hello()

p1 = Accoubt()
print(p1.welcome()) 


