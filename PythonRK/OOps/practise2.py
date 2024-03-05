"""
    Que 2--- Define a Employee class with attribute role, department & salary/ This
    class also have showMethd()
        Create an Enginner class that inherits role, department from employee & have additional
        attributes : name and age

"""
class Employee:
    def __init__(self,role,dept,salary) -> None:
        self.role = role
        self.dept = dept 
        self.salary = salary
    
    def showDetails(self):
        print("Role = ",self.role)
        print("dept = ",self.dept)
        print("Salary = ",self.salary)

class Engineer(Employee):
    def __init__(self, name,age) -> None:
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","99000")
      

eng1 = Engineer("Reetshu",22)
eng1.showDetails()
