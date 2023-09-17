# Dictionary

student = {101 : "rahul", 102 : "sonam", 103 : "raj"}
print(type(student))
print(student)
print(student[101])
print(student[102])
print(student[103])

fees = {"rahul":2000, "sonam": 3000, "raj" :8000}

print(type(fees))
print(fees)
print(fees["rahul"])
print(fees["sonam"])
print(fees["raj"])



print()
print("***************************************************************")
print()



# Modifying Dictionary

student = {101 : "rahul", 102 : "sonam", 103 : "raj"}

print(id(student))
print("Before Modification : ",student)
print()

student[102] = "Guru"

print(id(student))
print("After Modification : ",student)
print()

