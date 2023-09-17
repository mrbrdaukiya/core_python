# Access Set using for Loop

a = {10, 20, 30, "Guru", 50}

for i in a:
    print(i)



print()
print("***************************************************************")
print()



# Getting Input from user in set

a = set()
print(id(a))

n = int(input("Enter Number of Element : "))

for el in range(n):
    el = input("Enter Element : ")
    a.add(el)

print(id(a))
print(a)

print()

for i in a:
    print(i)