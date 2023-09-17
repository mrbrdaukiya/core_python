# Inserting / Adding new Item in Dictionary

student = {101 : "rahul", 102 : "sonam", 103 : "raj"}

print(id(student))
print("Before Adding : ",student)
print()

student[104] = "Guru"

print(id(student))
print("After Adding : ",student)
print()



print()
print("***************************************************************")
print()


# Deletion Dictionary

student = {101 : "rahul", 102 : "sonam", 103 : "raj"}

print(id(student))
print("Before deletion : ",student)
print()

del student[102]
# del student

print(id(student))
print("After deletion : ",student)
print()



print()
print("***************************************************************")
print()


# Testing Key in Dictionary

student = {101 : "rahul", 102 : "sonam", 103 : "raj"}

print(101 in student)
print( 101 not in student)



print()
print("***************************************************************")
print()


# clearing in Dictionary

student = {101 : "rahul", 102 : "sonam", 103 : "raj"}

print(id(student))
print("Before clearing : ",student)
print()

student.clear()

print(id(student))
print("After clearing : ",student)
print()
