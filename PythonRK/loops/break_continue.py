# Break: used to terminate the loop when encountered 
# Continue: terminate execution in the current iteration & continues execution of the loop with the next iteration

i=0
# while i<=6:
#     print(i)
#     if(i==3):
#         break
#     i+=1

while i<=6:
    
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1