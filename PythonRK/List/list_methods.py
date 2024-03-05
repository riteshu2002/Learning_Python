l1 = [23,53,765,34,76,44]
l1.append(78) # it will add 34 at the last of the list
print(l1)
l1.sort() # sort is ascending order
print("sort in ascendig order: ",l1)
l1.sort(reverse=True) # sort in descending order
print("sort in descending order: ",l1)

l1.reverse() #reverse the list
print("Reverse: ",l1)

l1.insert(1,433) # insert at particular index
print("inserted at index 1: ",l1)

l1.remove(34) # remove the particular element 
print("Removed 34: ",l1)

l1.pop(2) # remove the element at the particular index
print("Remove the element at index 2: ",l1)

a=l1.count(23) # count the occurence of the element
print(a)