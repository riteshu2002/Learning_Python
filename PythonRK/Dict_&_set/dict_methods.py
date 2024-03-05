stud = {
    "name" : "Reeteshu",
    "subjects":{ # nesting in dict
        "phy":67,
        "chem":78
    }
}

print(stud.keys()) # print all the keys in dict
print(list(stud.keys())) # typecasted in list
print(len(stud)) # length of the dict

print(stud.values()) # returns all the values rather then keys
print(stud.items()) # returns all (key, values) pairs as tuple

print(stud.get("name"))  # get value of the keys


