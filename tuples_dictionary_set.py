#lists order

student = ["Selva", "kani", "sankar"]
students = ["kani", "Selva", "sankar"]
print(student)
print(students)

#lists mutable

student = ["Selva", "kani", "sankar", "vishnu"]
print(student)

#lists duplicates

student = ["Selva", "kani", "sankar", "vishnu", "selva"]
print(student)

#lists indexing

student = ["Selva", "kani", "sankar", "vishnu", "selva"]
student[1]="gomathi"
print(student)

#lists key values pair

student= ["name":"selva", "age":"40"]
print(student)
    
#tuple ordered

student=("selva","kani", "Sankar")
students= ("kani", "Selva", "sankar")
print(student)
print(students)

#tuple immutable:
student=("selva","kani", "Sankar", "vishnu")
student[1]= "nandhu"
print(student)

#tuple duplicate:

student=("selva","kani", "Sankar", "vishnu", "selva")
print(student)

#tuple Indexing:

student=("selva","kani", "Sankar", "vishnu", "selva")
print(student[2])

#tuple key values pair:

student= ("name":"selva", "age":"40")
print(student)

#dictionay ordered:

student = {"name":"Selva",
           "age":40,
           "city":"Chennai"}

student["course"]= "python"

print(student)


#dictionay mutable:

student = {"name":"Selva",
           "age":40,
           "city":"Chennai"}

student["age"]= 25

print(student)

#dictionay duplicates:

tudent = {"name":"Selva",
           "age":40,
           "city":"Chennai"}

student["age"]= 25

print(student)

student["age"]= 25

print(student)

#dictionay indexing:
student = {"name":"Selva",
           "age":40,
           "city":"Chennai"}

print(student[0])









