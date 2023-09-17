# Aliasing Tuple

a = (10, 20, 30, 40, 50)

b = a

a = a[:3]

print("A :", a)
print("B :", b)

print( "ID of A :", id(a))
print( "ID of B :", id(b))


print()
print("*************************************************************************")
print()


# Copying Tuple

a = (10, 20, 30, 40, 50)

b = a
print("A :", a)
print("B :", b)
print("ID of A :",id(a))
print("ID of B :",id(b))
print()


b = a[0:5]
print("A :", a)
print("B :", b)
print("ID of A :",id(a))
print("ID of B :",id(b))