from numpy import *
a = array([101, 102, 103, 104, 105])
# b = a + 5
b = array([1, 2, 3, 4, 5])
c = a + b


# print(b)


# For Loop
n = len(c)


# for el in a:
#     print(el)

for el in range(n):
    print("index",el ,"=", c[el] )