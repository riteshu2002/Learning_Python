#Accessing parts of a string
# str[starting_idx : ending_idx]

str = "Accessing parts of a sttring"
print(str[1:8])
print(str[2: len(str)]) # by this it will go at the end of the sring
print(str[4:]) # now pyhton know that you want to go at the end of the string 
print(str[:7]) # [0:7]now it knows that it should start from index 0
print(str[-6:-1]) # this print backword in negetive indexing
