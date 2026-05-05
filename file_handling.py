print("file handling in python")

file=open("student.txt","r")
content=file.read()
print(content)

#readline()

file=open("student.txt","r")
print(file.readline())
file.close()

#readlines()

file=open("student.txt","r")
print(file.readlines())
file.close()

#writing files:

file=open("student1.txt","w")
file.write("hello world\n")
file.write("hello all")
print(file)
file.close()

#appending files:

file=open("student1.txt","a")
file.write("hello Good Morning\n")
print(file)
file.close()