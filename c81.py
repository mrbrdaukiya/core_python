#reshape Array

from numpy import *
a = array([1, 2, 3, 4, 5, 6])
b = reshape(a,(2,3))

print(a)
print(b)

print("********************************")


from numpy import *
c = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
d = reshape(c,(2,3, 2))

print(c)
print(d)

print("********************************")

from numpy import *
e = array([[1, 2, 3],[ 4, 5, 6]])
f = reshape(e,(6))

print(e)
print(f)


print("********************************")

#flatten() Method

from numpy import *
g = array([[1, 2, 3],[ 4, 5, 6]])
h = g.flatten()
print(g)
print(h)