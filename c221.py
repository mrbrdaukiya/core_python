from sys import * #getsizeof

a = 10
b = 30.33
c = "String"
d = [10, 20, 30]
e = (10, 20, 30)
f = {10, 20, 30}
g  = {101 : "rahul", 102 : "sonam", 103 : "raj"}




# id() Function
print(id(g))
print()

print(type(g))
print()

print(getsizeof(a))
print(getsizeof(b))
print(getsizeof(c))
print(getsizeof(d))
print(getsizeof(e))
print(getsizeof(f))
print(getsizeof(g))
