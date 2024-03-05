# Conditional statements
age = int(input())
if(age>=18):
    print("Eligible to vote")
else:
    print("Not Elegible")

# with strings
light = input("color is: ")

if(light == "red"):
    print("Stop")
elif(light == "yellow"):
    print("Look")
elif(light == "green"):
    print("GO")
else:
    print("Traffic free road")

# evoluating marks of student

marks = int(input("Marks: "))

if(marks>=90 and marks<=100):
    print("1st Division")
elif(marks<90 and marks>=80):
    print("2nd Division")
elif(marks<80 and marks >=60):
    print("3rd Division")
elif(marks<60 and marks>45):
    print("Passed")
else:
    print("Fail")