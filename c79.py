# 2D array by zeros() Function
# Syntax
# array_name = numpy.zeros(shape , dtype= float , order='C')

from numpy import *

a = zeros((5 , 3), dtype=int)
# print(a[0][0])

#For Loop 


n = len(a)
for r in range(n):
    for s in range(len(a[r])):
        print("index", r, s, "= ", a[r][s])
    print()

print("*************************")

#While Loop

n = len(a)
i = 0
while i < n:
    j = 0
    while j < len(a[i]):
        print("index", i, j, "= ", a[i][j])
        j += 1
    i += 1
print()

print("*************************")