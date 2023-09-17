# Important Set

a = {"Rahul", "Raja", "Sonam", "Rani"}
b = {"Sumit", "Rahul", "Python", "Rani", "java"}

print("A : ", a)
print("B : ", b)
print()

# ism = a.intersection(b)
# ism = a.union(b)
# ism = a.difference(b)
# ism = b.difference(a)
# ism = a.issubset(b)
ism = a.issuperset(b)



print("Result : ",ism)



print()
print("***************************************************************")
print()



# Passing Set To Function

def show(s):
    print(s)
    print(type(s))
    for i in s:
        print(i)

st = {10, 20, 30, "Guru"}
show(st)



print()
print("***************************************************************")
print()



# Passing and Returning Set To Function

def show(s):
    print(s)
    print(type(s))
    for i in s:
        print(i)
    return s

st = {10, 20, 30, "Guru"}
new_st = show(st)
print(new_st)
print(type(new_st))