# Slicing Nested Tuple
x = ((10, 20, 30),
     (40, 50, 60),
     (70, 80, 90),
     (11, 22, 33),
     (44, 55, 66),
     (77, 88, 99),
     (12, 13, 14))
print("Original Tuple")
print(x)
print()

print("From 1st Position to 4th Position")
a = x[1:5]
print(a)
print()


print("From 0th Position to last Position")
b = x[0:]
print(b)
print()



print("From 0th Position to 4th Position")
c = x[:5]
print(c)
print()


print("Last 4 Tuple")
d = x[-4:]
print(d)
print()



print("From 0th Position to 6th Position with stepsize 2")
e = x[0:7:2]
print(e)
print()



print("Last 5 List with [-5-(-3)] = 2 List Towards Right")
f = x[-5:-3]
print(f)
print()

print("*******************************************************************************")

print("slice Nested 2nd position , 0th Position")
m = x[2:3]
print(m)
print()
g = x[2:3][0]
print(g)
print()


print("slice 2nd list then extract element")
h = x[2:3][0][0]
print(h)
print()
i = x[2:3][0]
for el in i:
    print(el)
print()



print("Last Nested 4 List then 1st Position ")
# Extracting only one
n = x[-4:]
print(n)
print()
# Extracting all
j = x[-4:][1]
print(j)
print()



print("Last Nested 4 List then 1st Position then extract element")
# Extracting only one
k = x[-4:][1][0]
print(k)
print()
# Extracting all
l = x[-4:][1]
for el in l:
    print(el)
print()
