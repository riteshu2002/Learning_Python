# Dictionaries are used to store data values in key:values pairs
# They are unordered, murable(changeable) & don't allow duplicate keys
# use {} for dict
dict = {
    "key":"value",
    "name":"Reeteshu",
    "cgpa": 8.5,
    "is_adult":True,
    "subjects":["Python","c++","java"], # list can be also store in dict
    "topic":("dict","sets") # tuple can be also stored
}
print(dict)
print(type(dict))

print(dict["name"]) # accessing particular value using key
dict["surname"] = "Kushwaha"