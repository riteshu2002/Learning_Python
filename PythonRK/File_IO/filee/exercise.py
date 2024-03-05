with open("sample.txt","w") as f: # it will automatically create a file and oopen it in write mode
    f.write("I am learning java \n")
    f.write("And also Javascript")

# replace java with python
# with open("sample.txt","w") as f:
#     data = f.read()

# new = data.replace("Java","Python")
# print(new)
    


# finding certain values in file
word ="learning"
with open("sample.txt","r") as f: 
    data = f.read()
    if(data.find(word)!= -1):
        print("found")
    else:
        print("Not Found")


# WAP to find in which line of the file does the word "learning" occurs first

def check_line():
    word = "learning"
    data = True
    line =1
    with open("sample.txt","r") as f:
        while data:
            data = f.readline()
            if(data.find(word)):
                print(line)
                return
            line+=1
    return -1

check_line()






