# WAP to ask the user to enter names of thier 3 favorite movies & store them in alist

movie =[]
m1=input("Enter 1st movie: ")
m2=input("Enter 1st movie: ")

movie.append(m1)
movie.append(m2)

print(movie)






# WAP to check if a list contain a palindromic of elements 
l1 = [1,2,3,2,1]
a= l1.copy() # copy the list ele in new variable 
a.reverse() # reverse it
if(a==l1):
    print("Yes")
else:
    print("No")
