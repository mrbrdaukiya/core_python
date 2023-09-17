# setdefault() Method in Dictionary

student = {101 : "rahul", 102 : "sonam", 103 : "raj"}

print(id(student))
print("Original dict : ",student)
print()

retuned_value = student.setdefault(109 , "Guru")

print(id(student))
print("After setdefault dict : ",student)
print()
print("retuned value :", retuned_value)


print()
print("***************************************************************")
print()


# Accessing Dictionary using for loop

student = {101 : "rahul", 102 : "sonam", 103 : "raj"}

for k in student:
    print(k,":",student[k])





print()
print("***************************************************************")
print()




#Getting Input from user

a = {}

n = int(input("Enter Number Of Element :"))

for i in range(n):
    k = input("Enter Key :")
    v = input("Enter Value :")
    a.update({k:v})

print(a)