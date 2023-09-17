# Aliasing List
a = [10, 20, 30, 40, 50]
b = a
print("A :",a)

print()

print("B :",b)

print("Modifying A")
a[1] = 55
print("A :",a)

print()

print("B :",b)

print("Modifying B")
b[2] = 66
print("A :",a)

print()

print("B :",b)



print()
print("*****************************************************************************")
print()


# Copying List *************************************************** and Cloning List

a = [10, 20, 30, 40, 50]
b = a.copy()

# Cloning List
c = a[:]

print("A :",a)

print()

print("B :",b)

print()

print("Modifying A")
a[1] = 55
print("A :",a)

print()

print("B :",b)


print()

print("Modifying B")
b[2] = 66
print("A :",a)

print()

print("B :",b)



print()
print("*****************************************************************************")
print()


# Cloning List ***************************************************

a = [10, 20, 30, 40, 50]

b = a[:]

print("A :",a)

print()

print("B :",b)

print()

print("Modifying A")
a[1] = 55
print("A :",a)

print()

print("B :",b)


print()

print("Modifying B")
b[2] = 66
print("A :",a)

print()

print("B :",b)
