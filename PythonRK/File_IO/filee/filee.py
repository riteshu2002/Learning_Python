"""
    Python can be used to perform operations on a file ( read and write)
    Types of files
    1- Text files = .txt, .docs, .log
    2- Binary files = .mp4, .mov, .png, .jpeg etc

    Note --
        we have to oopen a file before reading or writing
        f= open("file_name", "modes")
"""

# reading a file

# f = open("F:/PythonRK/File_IO/filee/demo.txt","r")    
# # data = f.read()
# # print(data)
# line1 = f.readline()
# print(line1)
# f.close()

# writing in a file
# f = open("F:/PythonRK/File_IO/filee/demo.txt","w")  # w= write mode
# f.write("I want to learn Java ")
# f.close

# using append mode to write in data
f = open("F:/PythonRK/File_IO/filee/demo.txt","a")  # a= append mode
f.write("\n I want to learn Java Tomorrow")
f.close

