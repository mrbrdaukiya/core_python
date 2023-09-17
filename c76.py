# 2D array by array() Function
# Syntax
# array_name = numpy.array(object , dtype= None, copy = True, order = "K", subok=False, ndmin=0)

# import numpy
# a = numpy.array([[10, 20, 30], [40, 50,60]])
# print(a)


from numpy import *
a = array([["a", 20, 30, 40],
        [50,60, 70, 80]])

# a[1][0] = 100

# print(a.dtype)
# print(a[0][0])
# print(a[0][1])
# print(a[0][2])
# print(a[0][3])
# print(a[1][0])
# print(a[1][1])
# print(a[1][2])
# print(a[1][3])

#For Loop

# for i in a:
#     for j in i:
#         print(j)
#     print()

# a[1][2] = 1000
# n = len(a)
# for i in range(n):
#     for j in range(len(a[i])):
#         print(a[i][j])
#     print()

#While Loop

a[1][2] = 1000

n = len(a)
i = 0
while i < n:
    j = 0
    while j < len(a[i]):
        print("index",i, j, "=", a[i][j])
        j += 1
    i += 1
    print()
print("End Of The Code")