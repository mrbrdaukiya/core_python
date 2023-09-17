#zeros()Function

#syntex numpy 
# from numpy import *
# array_name = zeros(shape, dtype=float , order='C')

from numpy import *
a = zeros(5, dtype=int)
# print(a)


# For Loop
n = len(a)


# for el in a:
#     print(el)

# for el in range(n):
#     print("index",el ,"=", a[el] )



#While Loop
i = 0
while i<n:
    print("index", i,"=",a[i])
    i+=1