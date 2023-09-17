# input By user Tuple
a = []
n = int(input("Enter Number Of Elemenet :"))

for i in range(n):
    a.append(int(input("Enter Elemenet :")))

print(type(a))
print()

a = tuple(a)
print(type(a))
print("Tuples :")
for i in a:
    print(i)

print()
print("*******************************************")
print()

# Repetition of Tuple

a = (10, 20, 30)

print(a)

print()

result = a * 3

print(result)