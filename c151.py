# Nested List
a = [10, 20, 30,[50, 60]]
print(a)
print()

# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[3][0])
# print(a[3][1])

print("Before Modification A :", a)
print()
a[1]= 100
a[3][0] = 5

print("After Modification A :", a)


print()
print("********************************************************************")
print()

b = [50, 60]
a = [10, 20, 30, b]
print("A :", a)
print("B :", b)
print()

print("Before Modification A :", a)
print()
a[1]= 100
a[3][0] = 5

print("After Modification A :", a)


print()
print("********************************************************************")
print()

a = [[10, 20, 30],[40, 50, 60]]
print("A :", a)


# print(a[0][0])
# print(a[0][1])
# print(a[0][2])
# print(a[1][0])
# print(a[1][1])
# print(a[1][2])


print()
print("Before Modification A :", a)
print()
a[0][1]= 2
a[1][2] = 6

print("After Modification A :", a)
