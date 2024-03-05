# Set is the collection of the unordere items.
# Each elements in the set must be unique & immutable (unchangeabble)
# we cannot store list and dict in sets because they are mutable


sets = {1,2,4,5,7}
print(sets)
set1 = {1,2,3,4,3,5,7,7,"hello","hello","world"} # all the repeated elements will be printed only once and rest get ignored
print(set1)
 # to create empty set 
set2 = set()  

# Set methods
set2.add(2)
set2.add(4)

print(set2)

# set.add(element)  -- adds an element into set
# set.remove(el) --- removes the element
# set.close() --  empties the set
# set.pop()  -- removes a random value

# set.union(set2)  -- combines both set values & returns new
# set.intersection(set2) -- combines common values & returns new

val = {1,2,4,56,8,4,3,5,0}
val1 = {3,4,2,6,83,18,0,4,5}
print("Union of set ------------------")
print(val.union(val1))

print("intersection of set --------------")
print(val.intersection(val1))