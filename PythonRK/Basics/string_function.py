str = "i am a coder"

print(str.endswith("er")) # returns true if string ends with er
print(str.capitalize())# capitalizes 1es cahracter
print(str.replace("o","a")) # replaces all occurrences of old with new
print(str.find("am")) # returns the 1st index of this word
print(str.count("a")) # counts the occurrence of a

# WAP to input user's first name & prints its length

str1 = input("First name: ")
print("Length : ",len(str1))