a=int(input("A: "))
g=input("M/F: ")

if((a==1 or a==2) and g=="m"):
    print("fee is 100")
elif((a==3 or a==4) and g=="f"):
    print("fee is 200")
else:
    print("ERROR!!!!")

# Clever if else
  # <var>=(false_val, true_val)[condition]

age = int(input("age: "))
vote = ("yes","no") [age<18]  
print(vote)
