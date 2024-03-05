class Student:
    collg_name = "ABC College"
    name = "anonymous"  # class attribute
    def __init__(self,name, marks):
        self.name = name # obejct attribute has higher precedence so value will be same as passes in parameter
        self.marks = marks
        print("adding new student in Database-")

s1 = Student("Reeteshu","98")
print(s1.name)
# here if name is not passsed as parameter then class attribute will work