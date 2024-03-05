"""
        Methods that don't use the self parameter (work at class level)
 # here we use  @staticmethod as decorator
    Decorators allow us to wrap another function in order to 
    extend the behaviour of the wrapped function without permanently modifying it


    # ABSTRACTION
        Hiding the implementation details of a class and only showing the essential features to the user

    # ENCAPSULATION
        Wrapping data and functions into a single unit (Object)

    
"""
class car:
    def __init__(self) -> None: # definig inner process of car 
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("car Started...")

car1 = car()
car1.start()   # this code is example of abstracton


