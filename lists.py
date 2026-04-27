# fruits=["apple", "banana", "cherry"]
# print(fruits[0])
# print(fruits[-1])

#Slicing list:

fruits=["apple", "banana", "cherry"]
print(fruits[0:2])

#modifying lists" replace the value

fruits=["apple", "banana", "cherry"]
fruits[1]="orange"
print(fruits)

#modifying lists" add one more fruits without replace
fruits=["apple", "banana", "cherry"]
fruits.append("avakoda")
print(fruits)

#modifying lists" add one more fruits between two values like need to add the new value in index2

fruits=["apple", "banana", "cherry"]
fruits.insert(2,"watermelon")
print(fruits)

#Removing elements from the list: Remove
fruits=["apple", "banana", "cherry"]
fruits.remove("apple")
print(fruits)

#Removing elements from the list: pop()
fruits=["apple", "banana", "cherry"]
fruits.pop()
print(fruits)

#Removing elements from the list: pop with index
fruits=["apple", "banana", "cherry"]
fruits.pop(2)
print(fruits)

#Removing elements from the list: del
fruits=["apple", "banana", "cherry"]
del fruits[0]
print(fruits)

#Removing elements from the list: clear
fruits=["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

#loops through lists:
students=["selva", "kani", "Vishnu", "sankar"]
for student in students:
    print(student)
    
#loops through lists: len
students=["selva", "kani", "Vishnu", "sankar", "nandhu", "dhanam"]
for i in range(len(students)):
    print(i, students[i])
    
students=["selva", "kani", "Vishnu", "sankar", "nandhu"]
for i in range(len(students)):
    if students[i] == "selva":
         print("Selva is present in the class", i)
         
students=["selva", "kani", "Vishnu", "sankar", "nandhu"]
if "dhanam" in students:
    print("member is available in the class")
else:
    print("member is not available")
    
membership check:
    
fruits=["apple", "banana", "cherry"]
if "orange" in fruits:
    print("yes available")
else:
    print("not available")
    
#list methods and functions:

numbers=[3,1,5,7,2,8]
numbers.sort()
print(numbers)

#reverse
numbers=[3,1,5,7,2,8]
numbers.reverse()
print(numbers)


#count
numbers=[2,2,3,4,5,7]
print(numbers.count(2))

#index:
students=["selva", "kani", "vishnu", "sankar"]
print(students.index("sankar"))

#copy:
students=["selva", "kani", "vishnu", "sankar"]
stu= students.copy()
print(stu)

#list concatenation and repetition:

a= [1,2]
b=[3,4]
print (a+b)

a= [1,2]
b=[3,4]
print (a*3)

#nested lists:
matrix = [[1,2],[3,4]]
print(matrix[0][1])

a,*b=[1,2,3,4]

print(a)
print(b)

matrix = [[1.1, [1.2, 1.3]], [2.1, 2.2]]

print(matrix[0][1][1])

#Sorting with key

words=["apple", "banana", "Cherry", "kiwi"]
words.sort(key=len)
print(words)


    

