# Nested Tuple
a = (10, 20, 30, (50, 60))

b = (50, 60)

a = (10, 20, 30, b)

print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3][0])
print(a[3][1])


print()
print("*************************************************************************")
print()


a = ((10, 20, 30), (40, 50, 60))


print(a)
print("A[0] :",a[0])
print("A[1] :",a[1])

print()

print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[1][0])
print(a[1][1])
print(a[1][2])