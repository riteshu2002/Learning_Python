# take 3 inputs and find average 

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Avg score is: ",sum/3)

s1 = Student("Reeteshu",[98,97,93])
s1.get_avg()