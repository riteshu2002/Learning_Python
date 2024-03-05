"""
    Funtions in python --
        Block of statements that perform a specific task

      def keyword is use to define a function

        
        
"""
def calc(a,b): # passing parameters
    sum=a+b
    print(sum)

calc(3,6)  # calling the function

def hello_W(): # without parameters
    print("Hello World")

hello_W()

def avg(a,b,c):
    sum=a+b+c
    average = sum/3
    return average
sum=avg(2,5,7)
print(sum)

def sum(a=2,b=5): # we can values as argument too 
    print(a+b)
sum()

cities = ["delhi ","mumbai", "prayagraj","lucknow"]

def city(printcity):
    print(printcity, end=" ")
city(cities)



