# Nested Tuple for Loop

a = (10, 20, 30, (50, 60))

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


a = ((10, 20, 30), (40, 50, 60))

#  Without Index
# for i in a:
#     for j in i:
#         print(j)
#     print()

n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j," = ",a[i][j])
    print()



print()
print("*****************************************************")
print()


# Nested Tuple While Loop

a = (10, 20, 30, (50, 60))

n = len(a)
i = 0
while i < n:
    if type(a[i]) is tuple:
        if len(a[i])>1:
            j = 0
            m = len(a[i])
            while j < m:
                print(i, j, "= " ,a[i][j])
                j += 1
            i += 1
        
    else:
        print(i ,"= " ,a[i])
        i += 1




print()
print("*****************************************************")
print()


a = ((10, 20, 30), (40, 50, 60))

n = len(a)

i = 0
while i < n:
    j = 0
    while j < len(a[i]):
        print(i, j, "= " ,a[i][j])
        j += 1
    i += 1