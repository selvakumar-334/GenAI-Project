age =17
if age >=18:
    print("eligible for vote")
else:
    print("not eligible for vote")

marks = 45
if marks>=90:
    print("Excellent")
elif marks>=75:
    print("good")
elif marks>=50:
    print("pass")
else:
    print("fail")

for i in range(6):
    print(i)
    
for i in range(0,20):
    print(i)
    
for i in range(8):
    if i == 5:
        break
    print(i)
    
for i in range(8):
    if i == 5:
        continue
    print(i)
    
for i in range(2):
    for j in range(3):
        print(i,j)
        
i=1
while i<=4:
    print(i)
    i+=1
    
for i in range(0,50):
    if i %2 ==0:
        print ("Even number")
    else:
        print ("odd number")    
    
name= input("Enter the name")
age = input("enter the age")
city = input("Enter the city")

print("name is:", name) 
print("age is:", str(age))
print("city is:", city)  

product=input("Enter a product name")
price=int(input("Enter a price value"))
quantity=int(input("Enter a quanitity"))
total_cost=price*quantity
print(total_cost)

age=int(input("Enter the age"))

if age >=18:
    print("Eligible for vote")
else:
    print("not eligible for vote")
    
marks =int(input("Enter the mark"))
if marks>=90:
    print("grade A")
elif marks>=60:
    print("grade B")
elif marks>=50:
    print("grade C")
else:
    print("fail")
    
    

x=5
if x !=5:
    print("value is not matching")
else:
    print("value is good")
    
age = 17
if age >=18 and age<=60:
    print("Working person")
else:
    print("not working person")
    
day= "monday"
if day == "saturday" or day == "sunday":
    print("Weekend")
else:
    print("weekday") 
    
number = int(input("enter a number"))
if number %2==0:
    print("Even number")
else:
    print("odd number")
    
num1 =int(input("Enter a frist number"))
num2= int(input("Enter a second number"))
if num1>num2:
    print("num1 is greater than num2")
elif num2>num1:
    print("num2 is greater than num1")


for i in range(0,10):
    print(i)
    


for i in range(0,10,2):
    print(i)
    
for i in range(1,6):
    print(i)
    
for i in range(10):
    if i==5:
        continue
    print(i)

i=1
while i<=5:
        print(i)
        i=i+1
        
for i in range(3):
    for j in range(3):
        print(i,j)
    
    
for i in range(1,21):
    print(i)
    
for i in range(0,50,2):
    print(i)
    
text="Generative AI"
print(len(text))

secret_number=7

while True:
    guess=int(input("enter a number"))
    
    if guess==secret_number:
        print("correct! You guessed the secret number")
        break
    else:
        print("Wrong guess Plesae try again")
        
        *
        **
        ***
        ****
        *****
        ******
        
for i in range(1,7):
    print("*" *i)   
        