# Slicing on Tuple

x = (101, 102, 103, 104, 105, 106, 107)

print("Orignal Tuple")

n = len(x)
for i in range(n):
    print(i , "= ", x[i])


print()


print("From 1st Position to 4th Position")
a = x[1:5]
for i in a:
    print(i)

print(a)
print()



print("From 0th Position to last Position")
b = x[0:]
for i in b:
    print(i)

print(b)
print()



print("From 0th Position to 4th Position")
c = x[0:5]
for i in c:
    print(i)

print(c)
print()


print("Last 4 Element")
d = x[-4:]
for i in d:
    print(i)

print(d)
print()



print("From 0th Position to 6th Position stride 2")
e = x[0:7:2]
for i in e:
    print(i)

print(e)
print()


print("Last 5 Element with [-5-(-3)] = 2 Element Tworads Right")
f = x[-5:-3]
for i in f:
    print(i)

print(f)
print()