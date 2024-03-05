
# while True: # it will print for infinite time
count =1
while count<=5:
    print("heelooo")
    count+=1
 
 # multiplication table 
# print("----- Multiplicatioon table----")
# num = int(input("Enter the number : "))
# i=1
# while i<=10:
#     print( num * i)
#     i+=1

# printing list using loops
print("printing ele of list-------")
nums = [1,3,5,2,6,4,7,8,6,9,53]
index=0
while index< len(nums):
    print(nums[index])
    index+=1

# searching 
print("searching -----------")
num1 = (1,2,4,7,3,8,5,9,0,4)
i=0
search = 7
while i< len(num1):
    if(num1[i] == search):
        print("Element found at index :",i)
    i+=1