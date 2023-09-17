# append() Method in List

a = [10, 20, -50, 21.5, "Guru Choudhary"]

print("Before Append")
for element in a:
    print(element)

a.append(100)
print()
print("After Append")
for element in a:
    print(element)

print()
print("************************************************")
print()

# input() Method in List

a = []
print(a)

n = int(input("Enter Number of Element: "))

for i in range(n):
    a.append(int(input("Enter Element: ")))

print("List: ")
for element in a:
    print(element)

print(a)