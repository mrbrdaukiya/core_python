from numpy import *
a = array([100, 200, 300, 400, 500])
b = array([100, 20, 30, 400, 50])
# result = a == b
# result = a > b
result = a <= b
# print(result)

# For Loop
n = len(result)


# for el in a:
#     print(el)

for el in range(n):
    print("index",el ,"=", result[el] )