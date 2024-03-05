# In recursion - when a fuction calls itself repeatedly
 

def show(n):
    if(n==0): # base case or stopping case
        return
    print(n)
    show(n-1) # calling the function again and again till n=0

show(5)

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
    
print(fact(4))

def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

l1=["a","b","c","d"]
print_list(l1)


