"""
    super() method 
        IT is related to inheritance
        super() method is used to access methods of the parent class


"""

class car:
    def __init__(self,type) -> None:
        self.type = type
    @staticmethod
    def start():
        print("Car started")
    

    @staticmethod
    def stop():
        print("Stop")

class ToyotaCar(car):
    def __init__(self, name,type) -> None:
         self.name = name
         super().__init__(type) # calling base class objects directly
         super().start()
       

c1 = ToyotaCar("Fortuner","Petrol")
print(c1.type)


