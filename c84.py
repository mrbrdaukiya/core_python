from numpy import *
n = array ([[10, 20, 30],
            [40, 50, 60],
            [70, 80, 90]])
print("Orignal Array")
print(n)
print()
# a = n[:,0]

# a = n[raw , colum]
a = n[0:3, 1:3]

b = n[0, :]
print(a)
# print(b)