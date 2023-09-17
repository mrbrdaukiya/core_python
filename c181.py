# <<<<<<<<<<<<<<<<< Set Type {} >>>>>>>>>>>>>>>>>>>

a = {10, 20, 30, "Guru", 10, 50, 20.5, -50}

print(a)
print(type(a))
print(id(a))

print()
print("***************************************************************")
print()

# Adding Element in set

a = {10, 20, 30, "Guru"}
a.add("python")     # for one element
# a.update({50, 60,70})

print("Before adding : ", a)
print(id(a))

x = [101, 102, 103]
a.update(x)

print()

print("After adding : ", a)
print(id(a))



print()
print("***************************************************************")
print()

# Delete element in set

a = {10, 20, 30, "Guru"}
print("Original Set : ", a)
print(id(a))
print()

# a.remove("Guru")
a.discard("guru")

print("After Removeing Set : ", a)
print(id(a))