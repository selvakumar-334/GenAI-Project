def add(a,b):
    print(a+b)

add(5,9)

def multiply(a,b):
    return(a*b)
result= multiply(5,5)
print(result)

def divide(a,b):
    return(a/b)
result=divide(100,10)
print(result)

def subtraction(a,b):
    return(a-b)
result=subtraction(10,5)
print(result)

def squre(n):
    return (n*n)
result = squre(5)
print(result)  

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

text= "HELLO"
print("HELLO".lower())

print("hello".upper())

text = "  hello  "  
print(text.strip())

text= "hello world"
print(text.replace("world","python"))

text = "a,b,c"
print(text.split(","))

list= ["a","b","c"]
print("-".join(list))


text ="hello"
print(text.find("o"))

text ="hello"
print(text.count("l"))

text = "python"
print(text[0:4])

text = "python"
print(text[::-1])

name="Selva"
age = 40
print(f"my name is{name} and i am {age} years old")

print("hello\tworld")