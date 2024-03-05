"""
    Que 1 -- Definr a circle class to create with radius r using the constructoe
    Define an area() method of the class which calculates the area of the circle.
    define a perimeter() method of the clss which allows you to calculate the perimeter of the circle.

"""

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

