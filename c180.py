# Tuple of Lists
a = (10, 20, [30, 40])
print("Original Tuple A:",a)
print(id(a))
print(type(a))

print()

#modifying Lists
# a[2][0] = 90

# print("After modifying Tuple A:",a)
# print(id(a))
# print(type(a))



# Accessing Tuple of List using for Loop
n = len(a)

for i in range(n):
    if type(a[i]) is list:
        if len(a[i])>1:
            m = len(a[i])
            for j in range(m):
                print(i, j, "= " ,a[i][j])
    else:
        print(i ,"= " ,a[i])







print()
print("*****************************************************")
print()

# Tuple of Lists
a = ([10, 15, 20], [30, 35, 40])
print("Original Tuple A:",a)
print(id(a))
print(type(a))

print()

#modifying Lists

# a[0][0] = 90

# print("After modifying Tuple A:",a)
# print(id(a))
# print(type(a))

# Accessing Tuple of List using for Loop

n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j," = ",a[i][j])
    print()


