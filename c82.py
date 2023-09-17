# Input from User in numpy in 2D Array

from numpy import *
m = int(input("Enter Number Of Rows : "))
n = int(input("Enter Number Of Columns : "))
a = zeros((m, n), dtype=int)
print(a)

#For Loop

u = len(a)

# for i in range(u):
#     for j in range(len(a[i])):
#         x = int(input("Enter Element : "))
#         a[i][j] = x


#With Index

# for i in range(u):
#     for j in range(len(a[i])):
#         print(a[i][j])
# print(a)


#Without Index

# for r in a:
#     for c in r:
#         print(c)
# print(a)

#While Loop

i = 0
while i < u :
    j = 0
    while j < len(a[i]):
        x = int(input("Enter Element : "))
        a[i][j] = x
        j += 1
    i += 1

i = 0
while i < u:
    j = 0
    while j < len(a[i]):
        print("index", i, j, "=", a[i][j])
        j += 1
    i += 1
print(a)