#for loop:

for i in range(6):
    print ("hello world")
    
for i in range(5):
    print(i)
    
#Range in for loop:

for i in range(0,10):
    print(i)

for i in range(0,10):
    print("genAI Class is conducting on daily basis")
    
    
for i in range(0,30,5):
    print(i)
    
#break in for loop:

for i in range(5):
   if i == 3:
       break
   print(i)
   
# continue in for loop:
for i in range(5):
    if i == 4: 
        continue
    print(i)
    
#nested loop:

for i in range(2):
    for j in range(3):
        print(i,j)
        
#String in loop:

for letter in ("python"):
    print(letter)
    
    
    #while loop:
i=1
while i<=5:
    print(i)
    i+=1
    
#excercise
#1. write a program to print numbers 1 to 20
for i in range(1,21):
    print(i)
    
#2. Write a program to print even numbers from 0 to 50

for i in range(0,50,2):
    print(i)
    
#3. Count characters in the string "Generative AI" (including space)
text = "Generative AI"
count=len(text)
print("Total Characters are", count)
#4. #3. Count characters in the string "Generative AI" (Without space)

text = "Generative AI"
count=len(text.replace(" ",""))
print("Total Characters are without space", count)

#5. Print the pattern:
*
**
***
****
*****

for i in range(1,6):
    print("*" *i)