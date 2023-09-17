# Nested List - For Loop

a = [10, 20, 30, [50, 60]]

n = len(a)

for i in range(n):
    if type(a[i]) is list:
        if len(a[i])>1:
            m = len(a[i])
            for j in range(m):
                print(i, j, a[i][j])

    else:
        print(i, a[i])



print()
print("********************************************************************")
print()

a = [[10, 20, 30],[40, 50, 60]]

# Without Index

# for r in a:
#     for c in r:
#         print(c)
#     print()


# With Index

n = len(a)

for i in  range(n):
    for j in range(len(a[i])):

        print(i,j,"= ", a[i][j])
    
    print()