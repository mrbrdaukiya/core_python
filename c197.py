# copy() Method in Dictionary

student = {101 : "rahul", 102 : "sonam", 103 : "raj"}

print(id(student))
print("Original dict : ",student)
print()

new_stu =student.copy()

print(id(new_stu))
print("Copied dict : ",new_stu)
print()


print()
print("***************************************************************")
print()



# fromkeys() Method in Dictionary

key = (101, 102, 103)
Value = "Guru"
# Value = ("Gurr", "Raj", "sonam")
d = dict.fromkeys(key, Value)
print(d)


print()
print("***************************************************************")
print()



# get() Method in Dictionary

student = {101 : "rahul", 102 : "sonam", 103 : "raj"}

print("Original dict : ",student)
print()

print(student.get(102))