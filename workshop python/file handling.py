# file handling is a fundamental concept in python that allows you to work with files on your computer
#here are some common operation related to file handling

#1. creating a file : you can create a new file using the open() function in write mode("w")

# file = open("myfile.txt","w")
# file.close()

# 2.  opening a file:  you can open an existing file using the open() function. you specify the
# file's path and the  mode.


# 3. appending to a file: to add content to an existing file without overwriting its content
# ,open it in append mode('a')

# file = open("myfile.txt","a")
# file.write("this is appended\n")
# file.close()


# 4. reading from a file: you can read the content of a file using the read() method or by iterating through its lines
file = open("myfile.txt","r")
content = file.read()
print(content)
file.close()