print("view() Method") 

from numpy import *
a = array([10, 20, 30, 40, 50])
b = a.view()
a[1] = 80 
b[2] = 300
print(a)
print(b)
print("a", id(a))
print("b", id(b))

print("***************************************************")

print("copy() Method")

from numpy import *
c = array([10, 20, 30, 40, 50])
d = copy(c)
c[1] = 80 
d[2] = 300
print(c)
print(d)
print("c", id(c))
print("d", id(d))
