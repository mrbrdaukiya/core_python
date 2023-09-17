# Modifying Element in Tuple

a = (10, 20, -50, 20.5, "Guru")

print(a)
c = (101, 102)


tup1 = a[0:2]
# tup2 = a[2:] 
tup2 = a[3:] 

tup3 = tup1+ c + tup2

# print(tup3)

print()
print("************************************************************************")
print()

a = (10, 20, -50, 20.5, "Guru")

print(a)

# tup1 = a[0:3]
# print(tup1)

s1 = a[0:2]
s2 = a[3:]

tup = s1 + s2
print(tup)