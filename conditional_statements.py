age = 19
if age> 18:
    print("You are eligilbe to vote")
    
    
    #IF-ELSE STATEMENT
    
age= 19
if age>18:
    print("Eligible for vote")
else:
    print("Not Eligible for vote")
    
    #if-elif-else statement
    
marks= 70
if marks<35:
    print("Fail")
elif marks<50:
    print("pass")
elif marks<75:
    print("good")
else:
    print("Excellent")
    
x=5
if x>=7:
    print("x is greater than 7")
else:
    print("x is less than 7")

#And operators

age = 61
if age>=18 and age<=60:
    print("Eligible to work")
    
#or operators
day= "Friday"
if day =="Saturday" or day ==("sunday"):
    print("Weekend")
else:
    print("weekdays")    

#not operators

is_logged_in = False
if not is_logged_in:
    print("please login")\
        
#Nested if statement

age=15
if age>=18:
   if age<60:
    print ("Eligible adult")
else:
    print("minor")
    
#Even or odd number
number= int(input("Enter a number"))
if number %2==0:
    print("Even number")
else:
    print("odd number")
    
#Positive, Negative, zero

number=int(input("enter a number"))

if number>0:
    print("positive")
elif number<0:
    print("Negative")
else:
    print("zero")
    
#Voting Eligibility

age = int(input("Enter age"))
if age>=18:
    print("Eligible for vote")
else:
    print("not eligible for vote")
    
#find out largest number
number1 = input("Enter first number")
number2 = input("Enter second number")
if number1>number2:
    print("largest number is", number1)
elif number2>number1:
    print("largest number is", number2)
else:
    print("Both are equals")
    
#Grade Calculator
marks = int(input("enter a mark"))
if marks>90:
    print("grade is A")
elif marks >=60 and marks <=89:
    print("grade is B")
else:
    print("grade is C")

        

    
    