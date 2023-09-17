# updete() Method in Dictionary

student = {101 : "rahul", 102 : "sonam", 103 : "raj"}

print(id(student))
print("Original dict : ",student)
print()

vals = {"name": "Guru", "addrs": "Jodhpur", 105: "Choudhary"}

# student.update({104 : "Guru"})
student.update(vals)

print(id(student))
print("Updated dict : ",student)
print()



print()
print("***************************************************************")
print()


# pop() Method in Dictionary

student = {101 : "rahul", 102 : "sonam", 103 : "raj"}

print(id(student))
print("Original dict : ",student)
print()

removed_value = student.pop(102)
# removed_value = student.pop(106, "Guru")

print(id(student))
print("After Removeing dict : ",student)
print()
print("removed value :", removed_value)



print()
print("***************************************************************")
print()


# popitem() Method in Dictionary

student = {101 : "rahul", 102 : "sonam", 103 : "raj"}

print(id(student))
print("Original dict : ",student)
print()

removed_value = student.popitem()

print(id(student))
print("After Removeing dict : ",student)
print()
print("removed value :", removed_value)

