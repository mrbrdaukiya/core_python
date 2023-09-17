# List of Tuples
a = [10, 20, (30, 40)]

print("Original List A:",a)
print(id(a))
print(type(a))

print()

# a.append((50,60))
# print("After Appending a tuple A:",a)
# print(id(a))
# print(type(a))



# Accessing List of Tuple using for Loop
n = len(a)

for i in range(n):
    if type(a[i]) is tuple:
        if len(a[i])>1:
            m = len(a[i])
            for j in range(m):
                print(i, j, "= " ,a[i][j])
    else:
        print(i ,"= " ,a[i])







print()
print("*****************************************************")
print()







print()
a = [(10, 20, 30), (40, 50, 60)]
print("Original List A:",a)
print(id(a))
print(type(a))

print()


# a.append((50,60))
# print("After Appending a tuple A:",a)
# print(id(a))
# print(type(a))


n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j," = ",a[i][j])
    print()


