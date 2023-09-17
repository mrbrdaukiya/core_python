from numpy import *
n = int(input("Enter numer of elements: "))
a = zeros(n, dtype=int)

# For Loop


# for i in range(len(a)):
#     x = int(input("Enter Element: "))
#     a[i] = x

# for i in range(len(a)):
#     print(a[i])



#While Loop

u = len(a)
i = 0
j = 0
while i < u:
    x = int(input("Enter Elelment: "))
    a[i] = x
    i+=1

while j < len(a):
    print(a[j])
    j += 1
print(type(a))