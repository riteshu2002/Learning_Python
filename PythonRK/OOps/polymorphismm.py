"""
        # Polymorphism
            When the same operator is allowed to have diffrent meaning according to the context
          example of polymorphism is like operator overloading\
                print(1+3) # adding
                print("RK" + "is good") // concatenating
                print([1,2,4] + [5,6,7]) // merging  ... so we can see that one single operator is acting diffrently according to the scenerio

                

"""

class Complex:
    def __init__(self,real,img) -> None:
        self.real = real
        self.img = img
    
    def showNUmber(self):
        print(self.real, "i + ",self.img,"j")
    
    def __add__(self,num2): # __add__ is used to overlaod the +, 
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(1,3)
num1.showNUmber()

num2 = Complex(4,6)
num2.showNUmber()

num3 = num1 - num2 # here we subtracted two methods by using operator overloading
num3.showNUmber()



