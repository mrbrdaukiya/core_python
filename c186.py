a = {10, 20, 30, "Guru"}
print(a)
print(id(a))
print()

new_a = a.copy()

print("After Copy : ", new_a)
print(id(new_a))



print()
print("***************************************************************")
print()



# Clearing All Element

a = {10, 20, 30, "Guru"}
print("Before Clear : ",a)
print(id(a))
print()

a.clear()

print("After Clear : ", a)
print(id(a))

